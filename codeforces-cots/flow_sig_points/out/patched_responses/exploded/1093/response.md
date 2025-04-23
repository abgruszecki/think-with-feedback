<think>
Okay, let's tackle this problem. So the task is to find the minimum cost to send a message by possibly replacing each word in the message with another word from the same group (same meaning). Each group has words that can replace each other. For each word in the message, we need to choose the word in its group with the minimum cost and sum all those up.

First, let's understand the input. We have n words, each with a cost. Then, they are divided into k groups. The message has m words. For each word in the message, find the group it belongs to, then select the minimum cost in that group, and add that to the total.

So the steps are:

1. Read the words and their costs.
2. For each group, track which words are in the group.
3. For each group, find the minimum cost among its words. So that when a word from the group is encountered in the message, we can replace it with the minimum cost in its group.
4. For each word in the message, look up its group's minimum cost and sum all those.

Now, the main challenge is efficiently mapping each word to its group's minimum cost.

Let's think about data structures. The words are given as a list (second line of input). Each group is a list of indices. For each group, we can compute the minimum a_i of the words in that group. Then, create a dictionary that maps each word (string) to the minimum cost of its group.

So the steps would be:

- Read n, k, m.
- Read the list of words. Let's call this 'words_list', which is a list of strings.
- Read the list of a_i's. Let's call this 'costs', a list of integers.
- Then, for each of the next k lines (the groups), we need to process the group and find the minimum cost in that group. For each index in the group, we can check its cost and track the minimum.
- For each group, after finding the minimum cost, we need to map each word in the group to this minimum. So for each index in the group, we get the word from words_list and set it in the dictionary to point to the minimum cost.

Wait, yes. Because any word in the group can be replaced by any other word in the same group. So for each word in the group, the minimum possible cost is the minimum a_i among all words in the group. So, for each word in the message, we replace it with the one in its group that has the lowest a_i, or leave it as is (since the original word's a_i might already be the minimum).

So the key is, for each word in the message, find the group it's in, get the group's minimum cost, and sum all those.

So the plan is:

- Create a dictionary (word_to_min) where each key is the word string, and the value is the minimum cost for its group.

Processing the groups:

For each group in the k groups:

- Read the x followed by x indices. The indices are 1-based (since the input says "indices of words in this group"). So we need to adjust to 0-based if we're using Python lists.

Wait, the words in the input are given as a list in the second line, which is 0-based (since the first word is index 0 in Python if we read them into a list). But the problem statement says the third line is n integers a_1 to a_n, which probably are 1-based in the problem's input, but in the code, when read into a list, the first element is a[0], which would correspond to a_1. Wait, no. Wait, the third line has a1, a2, ..., an. So for the i-th word (from the second line), the cost is a_i. For example, if the second line is "i loser am the second", then words_list[0] is "i", words_list[1] is "loser", etc. The third line has a1 to a5, which would be the costs for each of these words. So words_list[0] has cost a1, words_list[1] has a2, etc. So the indices in the groups are 1-based. So when the group lists the indices, like 1, that's the first word in the words_list (index 0 in Python). So need to subtract 1 from the indices when processing the groups.

So, for each group:

- Read x and then x integers. Each integer is the index (1-based) of the word in the words_list. So for each of these, we take (index-1) to get the 0-based index in the words_list and costs list.

Then, for each index in the group, get the cost (costs[index]), find the minimum in the group. Then, for all words in this group (their strings from words_list), set in the word_to_min dictionary to this minimum.

So, for example, in the first sample input:

The groups are:

1 1 → which is index 0 (since 1-1=0). So the group contains only the first word, "i", which has cost 100. The minimum is 100. So word_to_min["i"] = 100.

Next group: 1 3 → which is index 2 (since 3-1=2). The word is "am" with cost 1. So word_to_min["am"] = 1.

Third group: 2 2 5 → 2-1=1 (word "loser", cost 1), 5-1=4 (word "second", cost 10). The minimum is 1. So "loser" and "second" in the group. So word_to_min["loser"] = 1, word_to_min["second"] = 1.

Fourth group: 1 4 → index 3 ("the", cost 5). So min is 5. word_to_min["the"] =5.

So when the message is "i am the second", each word is looked up:

i →100, am→1, the→5, second→1. Sum is 100+1+5+1=107.

In the second sample, the third group has words 2 and 5 (indices 1 and 4). The costs are 20 and 10. So the min is 10. So the word "second" (index 4, which is "second") has cost 10. So when "second" is in the message, it's replaced with the min of the group, which is 10. But in the second sample's input, the costs are 100, 20, 1,5,10. So group 3 has indices 2 and 5 (1-based). Wait, no, in the second sample's input, the third group is 2 2 5 (same as first sample). So for that group, the indices are 2 and 5 (1-based?), but wait no. Let me check:

In the group description, the third line in first sample is 2 2 5. So x=2, followed by 2 and 5. These are 1-based indices. So 2 corresponds to words_list[1], which is "loser", and 5 is words_list[4], "second". The costs for these are 1 and 10 in the first sample, so min is 1. But in the second sample, the third line of input is 2 2 5 again, and the costs for these indices (2-1=1: cost 20, 5-1=4: cost 10). So the min is 10. So "loser" is in this group (word "loser") and "second". So the group's min is 10. So "loser" would map to 10, and "second" to 10. But in the second sample's message, the words are "i am the second". So "second" is replaced with 10, leading to sum 100 +1 +5 +10 = 116.

So the approach is correct.

So the steps are:

1. Read all the words and their costs.

2. For each group, collect the indices (converted to 0-based), find the minimum cost in that group, then assign that min to each word in the group in the dictionary.

3. For the message, sum the values from the dictionary for each word.

Now, the key is processing the groups efficiently.

But the problem is that the input groups can have up to 1e5 words in total (since each group's x can be up to n, which is up to 1e5, and k can be up to 1e5). So the total sum of x across all groups is n, since each word is in exactly one group.

So processing each group in O(x) time is acceptable, as that's O(n) total.

So the steps:

- Create a list of words and costs.

- Create a dictionary to map word to its group's min cost.

But how to process the groups? For each group, read x and x indices. Then, for each index in the group (after converting to 0-based), collect the cost, find the min. Then, for each word in the group (using the words in words_list for those indices), assign the min to the word in the dictionary.

Wait, yes. For example, group with indices [0,1] (0-based) would have words_list[0] and words_list[1]. The group's min is the min of a0 and a1. Then, both words are mapped to this min.

So for the group processing loop:

for each of the k groups:

   read x and the x indices (as list)

   convert the indices to 0-based (subtract 1)

   collect the costs of these indices: [costs[i] for i in indices]

   find the min in this list

   for each index in indices:

       word = words_list[index]

       word_to_min[word] = min_cost

This way, even if a group is processed later and overwrites some entries, but since each word is in exactly one group, this is safe. Because the groups are processed in order, and each word is in exactly one group, so each word is processed once.

So this approach works.

Once the dictionary is built, the message words can be processed in O(m) time, summing the values from the dictionary.

So the overall time complexity is O(n + m), which is acceptable for n and m up to 1e5 each.

Now, considering the input reading. The words are given in the second line as a list of n words. Then the third line has n integers. Then, k groups. Then the message has m words.

But in Python, reading large inputs with input() can be slow. So for handling large inputs, it's better to read the entire input at once and split it into tokens. Using sys.stdin.read() and splitting into tokens can be much faster.

So for handling this, in Python, the code should read the entire input as a buffer, split into tokens, and process them as a list via a generator or a pointer.

Yes. Let's see:

We can read all the input at once using:

import sys

data = sys.stdin.read().split()

Then process the data as a list, using a pointer to track the current position.

For example:

ptr = 0

n = int(data[ptr]); ptr +=1

k = int(data[ptr]); ptr +=1

m = int(data[ptr]); ptr +=1

Then the next line is the list of n words:

words_list = data[ptr:ptr+n]

ptr +=n

Then the third line is n integers:

costs = list(map(int, data[ptr:ptr+n]))

ptr +=n

Then the next k lines describe the groups. Each group starts with x, followed by x indices.

But since the entire data is in a list, processing these groups requires for each group:

Read x (data[ptr], then ptr +=1). Then read x numbers (data[ptr:ptr+x], ptr +=x).

So for each group in k groups:

x = int(data[ptr])

ptr +=1

group_indices = list(map(int, data[ptr:ptr+x]))

ptr +=x

Then, process these group_indices (convert to 0-based) and compute the min cost.

So this is manageable.

Then, the message is the next line: m words.

message = data[ptr:ptr+m]

ptr +=m

So processing the input in this way is efficient.

Now, creating the word_to_min dictionary. For each group:

group_indices = list of x integers (1-based), converted to 0-based.

min_cost = min of costs[i] for i in group_indices_0.

Then, for each i in group_indices_0:

word = words_list[i]

word_to_min[word] = min_cost

But since each word is in exactly one group, this is correct.

Once the dictionary is built, sum all the word_to_min[word] for each word in the message.

So the code outline is:

Read n, k, m.

Read the words list.

Read the costs list.

Read k groups, process each to build the word_to_min dictionary.

Read the message, sum the min costs.

This should work.

Now, let's test with the first sample input.

Sample 1:

5 4 4

i loser am the second

100 1 1 5 10

Groups:

1 1 → x=1, indices [1] (1-based). Converted to 0-based: [0]. The cost is 100. So word 'i' →100.

1 3 → indices [3] (1-based) → 2. Cost is 1. Word 'am' →1.

2 2 5 → indices 2 and 5 (1-based) →1 and 4. Costs are 1 and 10. Min is 1. Words 'loser' and 'second' (words_list[1] is 'loser', words_list[4] is 'second') → both mapped to 1.

1 4 → index 4 (1-based) →3. Cost 5. Word 'the' →5.

Message: 'i am the second' → sum 100 +1 +5 +1 =107.

Sample 2:

Third line of input is 100 20 1 5 10.

Groups again:

Third group is 2 2 5 → indices 1 and 4 (0-based). Costs are 20 and 10. Min is 10. So 'loser' and 'second' mapped to 10.

But the message has 'second' which is in the group, so cost is 10. So sum 100 (i) +1 (am) +5 (the) +10 (second) →116.

Yes.

So the code works.

Now, the code in Python.

But in Python, dictionaries are O(1) access, so for 1e5 elements, it's efficient.

Now, code steps:

Import sys, read data.

Process data.

But in Python, using a generator or a pointer approach.

The code:

Read all data into a list.

Process as per steps.

Then sum the message.

Now, code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    data = input_stream.read().split()
    ptr = 0
    n, k, m = map(int, data[ptr:ptr+3])
    ptr +=3
    words = data[ptr:ptr+n]
    ptr +=n
    a = list(map(int, data[ptr:ptr+n]))
    ptr +=n
    word_min = {}
    for _ in range(k):
        x = int(data[ptr])
        ptr +=1
        indices = list(map(int, data[ptr:ptr+x]))
        ptr +=x
        # convert to 0-based
        indices_0 = [i-1 for i in indices]
        # find min cost in this group
        min_cost = min(a[i] for i in indices_0)
        # update the dictionary for each word in the group
        for idx in indices_0:
            word = words[idx]
            word_min[word] = min_cost
    # process the message
    message = data[ptr:ptr+m]
    total = sum(word_min[word] for word in message)
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 4 4
i loser am the second
100 20 1 5 10
1 1
1 3
2 2 5
1 4
i am the second
""",
            "output": \
"""\
116
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
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n, k, m = map(int, data[ptr:ptr+3])
    ptr += 3
    words = data[ptr:ptr+n]
    ptr += n
    costs = list(map(int, data[ptr:ptr+n]))
    ptr += n
    word_min = {}
    for _ in range(k):
        x = int(data[ptr])
        ptr += 1
        group = list(map(int, data[ptr:ptr+x]))
        ptr += x
        min_cost = min(costs[i-1] for i in group)
        for idx in group:
            word = words[idx-1]
            word_min[word] = min_cost
    message = data[ptr:ptr+m]
    total = sum(word_min[word] for word in message)
    print(total)

if __name__ == "__main__":
    main()
```
