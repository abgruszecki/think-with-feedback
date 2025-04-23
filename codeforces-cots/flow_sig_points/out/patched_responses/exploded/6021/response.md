<think>
Okay, I need to solve this problem where I have to count the number of strictly increasing sequences of positions in the string that are 'a's, and between each consecutive pair of a's in the sequence, there has to be at least one 'b'. Let's see how to approach this.

First, let's understand the problem with examples. For the first example input "abbaa", the valid sequences are [1], [4], [5], [1,4], [1,5]. Wait, why can't there be [4,5]? Because between positions 4 and 5 (assuming 1-based), position 4 is 'a', position 5 is 'a', but there's nothing in between. So there's no 'b' there, so that sequence is invalid. Right. So the 'b's must be present between consecutive a's in the sequence.

So the key is that after selecting a sequence of a's (p1 < p2 < ... < pk), each consecutive pair must have at least one b in between them.

Hmm. So how can we model this?

Let's think of grouping the a's based on the presence of b's between them. Like, each group is a set of a's that are contiguous or separated by non-b characters, but once a b appears, any a's after that (before the next b) can form a new group.

Wait, maybe the correct way is to split the string into segments separated by b's. Because between any two a's in the sequence, there must be at least one b. So for two consecutive a's in the sequence, they must lie in different segments separated by at least one b. So the sequence is a subset of a's where each consecutive pair comes from different segments.

So the first step is to split the original string into groups of a's that are separated by segments containing at least one b. So each group is a maximal consecutive a's separated by at least one b. For example, consider "abbaa":

Breaking it down:
a (group 0), then 'bb' (so the next a's are in group 1), then 'aa' (so group 1). Wait, wait. Wait, the initial groups would be determined by splitting the string into parts where each part is a set of a's that are not separated by any b's. But to have a valid transition between two a's in the sequence, there must be at least one b between them, which implies that they are in different groups. So each group is a consecutive sequence of a's (possibly with other characters, but no b's in between). Wait, no. Wait, the group is a set of a's where between any two a's in the same group, there's no b. So when you split the string into groups, each group is a collection of a's where each a in the group is followed by some characters (without any b) until the next a. Or perhaps, the groups are the a's that are separated by segments that contain at least one b. For example, the string could be split into runs of a's and other characters, but the key is that between two groups of a's, there's at least one b. So, whenever a b occurs, it separates the a's into different groups.

Let me think of the first example: "abbaa". The groups of a's are:

- The first 'a' (position 1). Then there are two b's. Then there are two a's (positions 4 and 5). But wait, positions 4 and 5 are consecutive a's. So between them, there's no b. So these two a's are in the same group. So the groups are group 0: [1], group 1: [4,5].

In this case, the valid sequences are sequences where the a's are chosen from different groups, and in order. So each selected a in the sequence must come from a higher group than the previous.

So for each group, we can select any subset of the a's in that group, but once a group is selected, the next a in the sequence must come from a later group. Wait, no. Because each a in the sequence must be part of the sequence, and consecutive a's must be in different groups.

So the problem reduces to selecting a sequence of a's where each consecutive a is in a higher group than the previous, and for each group, the selected a's must be in increasing order (since the sequence is strictly increasing). Wait, but the groups are ordered as per their positions. So group 0 comes before group 1, which comes before group 2, etc.

So the way the groups are arranged is in the order they appear in the string. For example, group 0 is the first set of a's (possibly with non-b characters between them), followed by a segment that includes at least one b, then group 1's a's, and so on.

Wait, but how are the groups formed? Let's consider the string:

Each group is a collection of a's that are in regions separated by b's. So when a b occurs, it marks the end of the current group. Any a's after the next b (but before another b) form the next group.

Wait, maybe the process is:

- Split the string into runs separated by 'b's. Each run is a segment between two b's (or before the first b or after the last b). Each such segment can contain a's (along with other characters), but the presence of a's in a segment forms a group. So for example, if a segment (after splitting by b's) has some a's, those a's form a group. But in that segment, between the a's, there might be other characters (non-b), so they are part of the same group. Because between those a's, there's no b. So the group is all the a's in a segment between two b's (or the start/end of the string and a b).

Wait, perhaps the correct approach is to split the string into parts that are separated by any occurrence of 'b's. For example, the string 'abbaa' is split into ['a', '', 'aa'] when split by 'b's. Then, for each of these parts, the number of a's present in the part (i.e., the count of a's in that part) is the size of the group. But no, because even if a part has other characters, like 'c', the a's in that part are part of the same group. So each group is the a's in a segment between two b's (or start/end), and the group's a's are those that are in that segment. The segments between the b's can have other characters, but the a's in them are part of the same group. So for example, the segment 'acxya' would contribute a group with two a's (positions where the a's are in that segment).

But how do we model this? Let's process the string and split into groups where each group is a set of a's that are in a segment between two b's. So each time a b is encountered, any subsequent a's (until another b is found) form a new group. So the groups are determined by the positions of the b's.

So the steps would be:

1. Iterate through the string, track when a b is encountered. Every time a b is encountered, it marks the start of a new group for any future a's. But even if there are multiple consecutive b's, they just mark the separation between groups. So groups are separated by one or more b's. So between two groups, there must be at least one b.

So the first group is formed by a's before the first b. Then, the next group is formed by a's after the first b and before the next b, and so on. Then, the a's in each group are all in their positions. For each group, we can collect the indices of the a's.

Once the groups are formed, the problem reduces to selecting a sequence of a's where each a in the sequence must come from a different group, and the groups must be in order. Moreover, in the sequence, the a's must be in strictly increasing order (since the positions are strictly increasing). So within a group, the a's are in order. So for a group, the a's are already in order. So when building the sequence, when selecting a's from group i, then group j (j > i), etc.

But the sequence can have any number of a's, as long as each is from a higher group than the previous. So the total number of valid sequences is the product of (1 + the number of a's in each group) minus 1. Wait, no. Because for each group, we can choose to take none or one of its a's, but once you take an a from a group, you can't take another from the same group in the sequence. Wait, but the sequence is a sequence of a's. Each a in the sequence must be from a different group. So for each group, we can choose to take any number of a's (but in the sequence, each a must be from a different group than the previous). Wait, no. Because consecutive a's in the sequence must be from different groups, but non-consecutive a's can be from the same group? No, no. Because the sequence is strictly increasing, and each element must be a's. But the problem allows that between two a's in the sequence, there's a b, but the groups are determined by the presence of at least one b between them. So if two a's are in the same group, then there is no b between them, so they can't be consecutive in the sequence. But if they are in the same group but not consecutive, like in the sequence [a1, a3] where a1 and a3 are in the same group (but a2 is not selected), then between a1 and a3, there's no b. So such a sequence is invalid. So the sequence must be such that consecutive a's are in different groups, but also all a's in the sequence must be in order, but non-consecutive a's can be from any groups as long as they are ordered. Wait, no. Because the sequence is strictly increasing, the positions are strictly increasing, so the a's are in order. But between any two a's in the sequence, there must be a b. So even if two a's are in the same group, but there's a b between them, then they can't be in the same group. Wait, that's a contradiction. So the group is determined by the presence of a b between the a's. So two a's in the same group cannot have a b between them. Therefore, consecutive a's in the same group are not separated by a b, so they cannot be consecutive in the sequence. So the sequence must consist of a's from different groups, each group after the previous. So each group can contribute 0 or more a's to the sequence, but the a's in the sequence must come from groups in order, and between consecutive a's in the sequence, their groups must be strictly increasing. Wait, no. The sequence is of a's that are in strictly increasing order. The groups are ordered as per their positions in the string. So if the sequence picks an a from group 0, then the next a must come from a group after 0, say group 1. Then the next a must come from a group after 1, and so on. So the groups must be in increasing order. So the sequence's groups are a subset of the group order. For example, group 0, group 2, group 3, etc. Each subsequent group in the sequence is after the previous.

But in the problem statement, the a's in the sequence must be strictly increasing. So their positions are in order. So the groups must be in the same order as their positions in the string. So each group is in order.

So the problem reduces to:

Each group can contribute any number of a's, but the sequence must be formed by selecting a's from the groups in order, and each a in the sequence must come from a group that is after the previous a's group.

Wait, no. Because if the groups are ordered as they appear in the string, then the a's in the sequence are selected in order, but each a must come from a group that is after the previous a's group. So group i, then group j>i, then group k>j, etc. So the sequence is built by selecting one or more groups in order, and for each selected group, you can choose one a from that group. Wait, no. Because between the a's in the sequence, there can be multiple groups in between, as long as there's a b in between. So for example, if group 0 has a1, group 1 has a2, group 2 has a3, then a sequence could be a1, a3. Because between group 0 and group 2, there are groups (group 1) which have a b, so the a's are in different groups. So the key is that between any two consecutive a's in the sequence, there must be at least one b in between. Which is ensured by the groups: consecutive a's in the sequence must be from different groups, and the groups are ordered.

Wait, perhaps the correct model is that each group is separated by at least one b. So any a's in different groups are separated by at least one b. Therefore, if the sequence selects a's from group i and group j where j > i, then between those two a's, there's a b. So the condition is satisfied.

Therefore, the sequence can consist of any subset of a's from the groups, with the following constraints:

1. The a's in the sequence must be in strictly increasing order of their positions (which is automatically satisfied if we process the groups in order and pick a's from each group in their order).

2. The a's in the sequence must come from groups in strictly increasing order (so, each a in the sequence comes from a group that is later than the previous a's group).

Therefore, the problem is equivalent to selecting a sequence of a's such that each consecutive a comes from a higher group than the previous. Because groups are in the order of their appearance in the string, and each group's a's are in order. So the sequence is a sequence of a's where each a is from a group after the previous's group.

So the problem reduces to, for each group, choosing how many a's to take (0 or 1?), but wait, no. Because each group can contribute multiple a's to the sequence. Wait, no. Because if you take two a's from the same group, then between them there's no b. So such a sequence would be invalid. Because for consecutive a's in the sequence, there must be at least one b between them. So two a's from the same group cannot be consecutive in the sequence. But what if there's another a in between from a different group? For example, group 0: a1, group 1: a2, group 0: a3. Then a sequence like [a1, a2, a3] would be invalid because between a2 and a3, there's no b. Wait, no. Because group 0 comes before group 1. So a3 is in group 0, which is before group 1. So the sequence [a1, a2, a3] would have a1 in group 0, a2 in group 1, a3 in group 0. But a3 is in group 0, which is before group 1. So their positions are increasing (assuming a3 is after a2), but group 0 is before group 1, so this would not be allowed. So this is impossible. Because groups are ordered by their occurrence in the string. So any a's in group i come before group j if i < j. So the a's in a higher group are after the a's in a lower group.

So the a's in the sequence must come from groups in increasing order. So group i < group j < group k, etc. So the sequence is formed by choosing a subset of a's where each a is in a group higher than the previous.

Thus, the problem is similar to choosing a subset of a's, each from a group higher than the previous, and each a's position is strictly increasing. Since the groups are in order, and the a's in each group are in order, the positions will automatically be increasing as long as we process the groups in order and select a's in their group order.

But how to model this. Let's think of each group as a list of a positions. For example, group 0 has a list [p1, p2, ...], group 1 has [q1, q2, ...], etc. Then, the sequence must be formed by selecting a's from these groups in order, and each selected a must be after the previous in position and in a later group.

Wait, but the groups are ordered. So once you have selected a group, any subsequent a's must come from groups after it. So for each group, we can decide how many a's to take (possibly zero, but at least one if we include it in the sequence). But the sequence can be any combination of a's from the groups, as long as they are selected in group order. For example, group 0 can have two a's: but in the sequence, you can take the first a from group 0, then any a from group 1, group 2, etc. But if you take two a's from group 0, they can't be consecutive in the sequence. But that's impossible because the groups are in order, so group 0 comes before group 1. So once you take an a from group 0, the next a must come from group 1 or higher.

So each group can contribute at most once to the sequence, but each group can contribute any of its a's. Wait, no. Because you can have a sequence where you take one a from group 0, then one a from group 2, then another a from group 3. Each group is higher than the previous. But for a single group, you can have multiple a's in the sequence only if they are separated by a's from other groups. But that's not possible. Because once you take an a from group 0, the next a must come from a higher group. Then, the next a must come from a group higher than that. So each group can contribute at most once in the sequence. So the sequence is a list of a's, each from a distinct group, in order.

Wait, this seems like a misunderstanding. Let's clarify with an example. Suppose a group 0 has a's at positions 1, 3, 5. Then group 1 has a's at positions 7, 9. Then group 2 has an a at 11. Then, can the sequence be [1,3,7]? No, because between the first two a's (positions 1 and 3) there's no b. So group 0 is formed by a's that are in a segment between b's. So group 0's a's are in a segment where there are no b's. So between 1 and 3, there are no b's. Therefore, the sequence [1,3] is invalid, as there's no b between them. But according to the group model, group 0's a's are in the same group. So taking two a's from group 0 would not satisfy the condition. Therefore, in the sequence, all a's must come from different groups, and each group can contribute at most one a. Because otherwise, two a's from the same group would not have a b between them.

So the conclusion is that each group can contribute at most one a to the sequence. Because if you take two a's from the same group, there's no b between them, so they can't be consecutive. And since the groups are processed in order, once you take an a from group i, the next a must come from group j > i, so you can't take another a from group i again. Therefore, each group can contribute 0 or 1 a's to the sequence. So the problem reduces to selecting a subset of groups, and for each selected group, choosing one of its a's, such that the selected a's are in order (which they are, as groups are in order and each group's a's are in order).

So the total number of sequences is the product of (1 + the number of choices in each group) minus 1. The minus 1 is to exclude the empty sequence (since the problem requires sequences of length >=1? Wait, looking at the problem statement, the sequences can be of any length k >=1. So the empty sequence is not considered. So the formula is:

For each group, the number of options is (number of a's in the group) + 1 (the option to take none). But since we must take at least one group, the total is the product of (1 + a_i) for all groups, minus 1 (the product where all groups are not taken).

Wait, but that's not correct. Because in this case, for each group, you can choose to take none or take one of the a's. Then, the product (1 + a_i) represents all possible subsets (including choosing none). Subtracting 1 removes the empty selection. But this is exactly the count of all possible non-empty sequences where each a comes from a different group, and the order is determined by the groups.

Yes. Because for each group, you can choose to take any of its a's (counted by a_i options), or not take any (1 option). The product of (a_i + 1) for all groups gives all possible subsets (including the empty selection). Subtract 1 to exclude the empty subset. This gives the total number of non-empty sequences where each a is from a distinct group, and groups are in order. But wait, the order of the groups in the sequence is determined by their order in the string, so the product (a_1 + 1) * (a_2 + 1) ... (a_k + 1) - 1 gives all possible non-empty combinations of selecting one a from each group (if selected), in the order of the groups. Which is exactly what the problem requires. Because each group can contribute 0 or 1 a, but when selected, the a's are in the order of the groups, which ensures that their positions are strictly increasing, and between consecutive a's there is at least one b (since the groups are separated by at least one b).

So the problem reduces to:

1. Split the string into groups of a's, where each group is separated by at least one b.

2. For each group, count the number of a's in it (let's call it c).

3. The answer is (product of (c_i + 1) for all groups) - 1, modulo 1e9+7.

But wait, let's check the examples.

First example:

Input: abbaa → groups are ['a', 'aa'] (after splitting by b's). So group 0 has 1 a, group 1 has 2 a's. The product is (1+1) * (2+1) = 2 *3=6. Subtract 1 →5, which matches the first example's output.

Second example: input 'baaaa' → split by b's gives ['', 'aaaa']. So group 0 is empty (no a's), group 1 has 4 a's. The product is (0+1) * (4+1) = 1 *5=5. Subtract 1 →4, which matches the second example.

Third example: input 'agaa' → split by b's. But there are no b's in the string. So the entire string is one group. So group 0 has 3 a's (positions 1,3,4). The product is (3+1) →4. Subtract 1 →3, which matches the third example.

So this seems to work.

Therefore, the approach is:

- Split the string into groups separated by 'b's. For each group, count the number of a's. Then compute the product of (count + 1) for each group, subtract 1, mod 1e9+7.

But wait, the groups are split on 'b's. So any part between two b's (or before the first, after the last) is a group. But in those parts, we need to count the number of a's. So for example, the group could be 'axya', which has 2 a's. So the group is a part of the string that's between two 'b's (or the start/end), and in that part, we count how many a's are present.

So the steps are:

1. Split the original string into parts whenever a 'b' is encountered. For example, 'abbaa' is split into ['a', '', 'aa'].

2. For each part, count the number of 'a's in it. So group 0: 1 a, group 1: 0, group 2:2. But group 1 has zero a's, so it's ignored. Because for a group with zero a's, (count +1) is 1, which doesn't contribute to the product.

So, but how to split the groups correctly. Because in the example where a part is between two 'b's (like 'bb'), the part is the empty string, which has zero a's. So when splitting by 'b's, the split will create parts that may have zero a's. But those groups with zero a's can be ignored, since (0+1) =1, and multiplying by 1 doesn't change the product. So perhaps we can process each split part, count the a's, and if the count is zero, we can skip it. Because groups with zero a's do not contribute to the product (since (0+1) is 1). So the steps can be modified to:

- Split the string into parts by 'b's.

- For each part, count the number of a's.

- For each count, if it's >0, multiply the result by (count +1). If the count is 0, it's (0+1) =1, which can be ignored in the product.

So the code can process all split parts, count the a's, and for each, compute the product of (count +1). Then subtract 1.

So the algorithm is:

Initialize the result as 1.

For each group (split part) in the split by 'b's:

   count = number of 'a's in the split part.

   if count >0:

       result *= (count +1)

       result %= MOD

At the end, subtract 1, mod MOD again, and output.

This approach works because groups with zero a's contribute a factor of 1, so they can be ignored. So the code can process each split part, count the a's, and multiply the result by (count +1).

So the code steps are:

- Split the input string into parts separated by 'b's. The split can be done via splitting the string on each 'b' (but in Python, splitting on 'b' would split the string into parts whenever a 'b' occurs, regardless of consecutive 'b's). For example, 'abbaa' would split into ['a', '', 'aa'].

- For each part in the split list, count the number of 'a's. For example, the first part 'a' has 1 a, the second part is empty (0 a's), third part 'aa' has 2 a's.

- For each part with a non-zero count of a's, multiply the result by (count +1). But even if the count is zero, it's (0+1) =1, which doesn't change the product. So in code, even parts with zero a's can be processed.

- Finally, subtract 1 (to exclude the empty selection) and output modulo 1e9+7.

So the code can be written as follows.

In Python, splitting the string on 'b' is done via s.split('b'). Then, for each part in s.split('b'), count the number of 'a's in it.

So for example, for the third example, 'agaa' → split on 'b' gives ['agaa'], which has 3 a's (positions 1,3,4). So the code would compute (3+1) →4, subtract 1 →3.

But wait, the part is 'agaa' → the count of a's is 3. So (3+1) =4. Correct.

So the code is:

Read the input string.

MOD = 10**9 +7.

Initialize res =1.

Split the string into parts via s.split('b').

For each part in the split:

   cnt = part.count('a')

   res = res * (cnt +1) % MOD

res = (res -1) % MOD

print(res)

But wait, this would process all split parts, including those with zero a's. For example, the split part after the first 'b' in 'abbaa' is empty string, which has 0 a's. Then (0+1) =1, which doesn't affect the product. So even parts with zero a's are handled correctly.

Yes.

So the code is straightforward. Let's check the examples:

First example: 'abbaa' → split into ['a', '', 'aa'] → counts are 1,0,2. (1+1)=2, (0+1)=1, (2+1)=3. product is 2*1*3 =6. 6-1=5. Correct.

Second example: 'baaaa' → split into ['', 'aaaa'] → counts are 0,4. product is 1 *5 →5. 5-1=4. Correct.

Third example: 'agaa' → split into ['agaa'] → count is 3. product is 4 →4-1=3. Correct.

So the code works for the examples.

Now, considering the time constraints. The string can be up to 1e5 characters. Splitting on 'b' is O(n), as each character is processed once. Then, for each part in the split list, counting the 'a's is O(k), where k is the length of the part. The total sum of k's is O(n), since each character is processed once. So overall, the code runs in O(n) time, which is acceptable for n=1e5.

Space-wise, splitting the string into parts could take O(n) space (if all parts are kept as strings), but in practice, each part is processed immediately, and the strings can be handled in a way that doesn't require storing them all. But in Python, s.split('b') will create a list of all parts, which for a string of 1e5 characters, each split part can be up to 1e5 in the worst case. However, in practice, it's manageable. For example, for a string like 'a' repeated 1e5 times, split on 'b' would create a single part of length 1e5, which is acceptable. For a string with many 'b's, split parts are smaller.

Alternatively, perhaps the code can process the string in a way that doesn't split into parts, but instead tracks the current group's a count. For example:

Initialize current_a =0.

res =1.

for c in s:

   if c == 'b':

       if current_a >0:

           res = res * (current_a +1) % MOD

           current_a =0

       # else, continue

   elif c == 'a':

       current_a +=1

   else:

       # other characters, but we count a's in current group.

       pass

After the loop ends, check if current_a >0, multiply res by (current_a +1) mod MOD.

Then subtract 1, mod MOD again, and output.

This approach is more efficient in terms of space, as it processes the string character by character and doesn't split into parts. This is better for large strings. Let's see:

For example, in the string 'abbaa':

- first character 'a' → current_a=1.

Then 'b' → since current_a>0, multiply res by 2 (1+1). res=2. current_a reset to 0.

Next 'b' → current_a is 0, no action.

Next 'a' → current_a=1. Then another 'a' → current_a=2.

After the loop ends, process the current_a=2 → multiply res by 3 → 2*3=6.

Then subtract 1 →5.

This approach works and is more efficient. Because splitting the entire string into parts can take O(n) space, which is acceptable but perhaps not optimal. But processing character by character uses O(1) space (except for the input string, which is necessary).

So the code can be optimized as follows:

Read the input string.

current_a =0

res =1

for c in s:

    if c == 'b':

        if current_a >0:

            res = res * (current_a +1) % MOD

            current_a =0

    elif c == 'a':

        current_a +=1

# After processing all characters, check if current_a >0

if current_a >0:

    res = res * (current_a +1) % MOD

res = (res -1) % MOD

print(res)

This approach is more efficient and handles all cases correctly.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 + 7
    s = input_stream.readline().rstrip("\n").strip()

    res = 1
    current_a = 0

    for c in s:
        if c == 'b':
            if current_a > 0:
                res = res * (current_a + 1) % MOD
                current_a = 0
        elif c == 'a':
            current_a += 1

    if current_a > 0:
        res = res * (current_a + 1) % MOD

    print((res - 1) % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
baaaa
""",
            "output": \
"""\
4
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
    MOD = 10**9 + 7
    s = input_stream.readline().rstrip("\n").strip()

    res = 1
    current_a = 0

    for c in s:
        if c == 'b':
            if current_a > 0:
                res = res * (current_a + 1) % MOD
                current_a = 0
        elif c == 'a':
            current_a += 1

    if current_a > 0:
        res = res * (current_a + 1) % MOD

    print((res - 1) % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
agaa
""",
            "output": \
"""\
3
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

Third example: 'agaa' → no 'b's. So current_a increases for each 'a' → count is 3. Multiply res by 4 (3+1). res=4. 4-1=3. Correct.

Another test case: input 'aabbaab' → split into ['aa', '', 'aab'] → counts 2,0,2. So product (3 * 1 * 3) =9. 9-1=8.

The code would process:

current_a starts at 0.

Processing 'a's → current_a=2. Then 'b' → multiply res by 3 → res=3. current_a=0.

Then 'b' → no current_a.

Then 'a' → current_a=1, then 'a' → current_a=2, then 'b' → current_a=2 → multiply res by 3 → 3*3=9. current_a=0.

Then loop ends. res=9. 9-1=8. Correct.

This approach is correct.

Therefore, the code is correct and efficient. It runs in O(n) time and O(1) space (excluding the input string), which is optimal for the constraints.
</think>

```python
MOD = 10**9 + 7
s = input().strip()

res = 1
current_a = 0

for c in s:
    if c == 'b':
        if current_a > 0:
            res = res * (current_a + 1) % MOD
            current_a = 0
    elif c == 'a':
        current_a += 1

if current_a > 0:
    res = res * (current_a + 1) % MOD

print((res - 1) % MOD)
```
