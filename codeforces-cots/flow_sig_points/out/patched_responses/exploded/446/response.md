<think>
Okay, let's see. So the problem is about maintaining a list of chats where whenever a message is sent to a friend, their chat moves to the top. If the friend isn't already in the list, they're added to the top. And the output is the final order of the chats after all messages.

Hmm. So the key points here are:

1. Each time a message is sent to a friend, their chat moves to the top, unless they are already there. But if they are present elsewhere in the list, they are moved to the top, and the others shift down. Otherwise, insert at the top.

The task is to process all messages and output the final order.

The challenge is handling this efficiently, especially since n can be up to 200,000. So any approach that requires O(n) time per operation would be too slow. Because for 2e5 operations, O(n) each would be 4e10 operations, which is way beyond the time limit.

So we need an O(1) per operation approach.

Let's think about data structures. The naive approach would be to maintain a list and, for each message, check if the friend is in the list. If yes, remove them and insert at the beginning. If not, insert at the beginning. However, for a list, checking if an element exists is O(n), which would be O(n^2) overall. That's way too slow for n=2e5.

So we need a way to track the presence of each friend and their current position in the list, but also maintain the order.

Hmm. So perhaps using a linked list structure with a hash map to track nodes. But implementing a linked list in Python can be tricky for efficiency. Alternatively, using a combination of a set to track existing elements and a data structure that allows O(1) insertion and moving to front.

Wait, another idea: Since the order is determined by the last occurrence of each friend, except that each occurrence moves the friend to the front, the final list is the order of the last occurrence of each friend, but in reverse order. Wait, no. Because each time a friend is sent a message, they are moved to the top, so the most recent messages are at the top. So the final list should have the friends in the order of their last occurrence, but when they were last moved to the top. Wait, no. Let's see.

For example, in the first sample input:

Messages: alex, ivan, roman, ivan.

The final list is ivan, roman, alex. Because after the fourth message (ivan), ivan is moved to the top. So the order is determined by the last time each friend was mentioned, but arranged such that the most recent are first.

Wait, but the first occurrence of ivan is at position 2 (after alex), then the fourth occurrence moves it to top. Roman was added third, then ivan is added fourth, moving to top. So the order is ivan (fourth), roman (third), alex (first). So the friends are ordered by the time of their last occurrence, but in reverse. Because the last occurrence of ivan is fourth, roman is third, alex is first. So the order in the output is sorted by the latest occurrence, in reverse order. So the order is all unique friends sorted in the order of their last occurrence, from latest to earliest.

Wait, that's a key insight. Because every time a friend is mentioned, they are moved to the top. So the final list is the order of the last occurrence of each friend, but arranged such that the friend with the most recent last occurrence is first, then the next most recent, etc.

So the final list can be obtained by keeping track of the last occurrence index of each friend. Then, we collect all unique friends, sort them in descending order of their last occurrence index.

Wait, yes. Because each time a friend is mentioned, their last occurrence is updated. The final order is that the friend with the latest (highest) last occurrence is first, then the next, etc.

For example, in the first sample:

Messages:

1: alex (last occurrence index 1)
2: ivan (last occurrence index 2)
3: roman (last occurrence index 3)
4: ivan (last occurrence index 4)

So the unique friends are alex (1), ivan (4), roman (3). Sorting their last occurrence in descending order gives ivan (4), roman (3), alex (1). Which matches the sample output.

In the second sample:

Messages are:

alina (1)
maria (2)
ekaterina (3)
darya (4)
darya (5)
ekaterina (6)
maria (7)
alina (8)

The last occurrences are:

alina: 8
maria:7
ekaterina:6
darya:5

So sorted in descending order of last occurrence: alina (8), maria (7), ekaterina (6), darya (5) → but wait the output is alina, maria, ekaterina, darya. Wait, no. Wait the sample output for the second input is:

alina
maria
ekaterina
darya

Wait the input is 8 messages. Let's see the steps:

After each message, the order is:

1. alina → [alina]

2. maria → [maria, alina]

3. ekaterina → [ekaterina, maria, alina]

4. darya → [darya, ekaterina, maria, alina]

5. darya again → move to front → [darya, ekaterina, maria, alina]

Wait no: when the fifth message is darya, it's already at the top, so the order remains. But then sixth message is ekaterina: now ekaterina is moved to front. So after sixth message, the list is [ekaterina, darya, maria, alina].

Then seventh message is maria → moved to front: [maria, ekaterina, darya, alina].

Eighth message is alina → moved to front: [alina, maria, ekaterina, darya].

So the output is alina, maria, ekaterina, darya.

But according to the last occurrence approach:

Each friend's last occurrence index is:

alina:8

maria:7

ekaterina:6

darya:5

So sorted in descending order of last occurrence would be 8,7,6,5 → alina, maria, ekaterina, darya. Which matches the output.

So the key insight is that the final list is exactly the list of unique friends, sorted in the order of their last occurrence in the input, with the latest occurrence first.

So to solve the problem, we can:

- Keep a dictionary to track the last occurrence index of each friend.

- Then, collect all the unique friends, and sort them in descending order of their last occurrence index.

- Output them in that order.

Yes! That's a much more efficient approach. Because for each message, we just update the last occurrence index of the friend. Then, at the end, we collect the friends, sort them by their last occurrence in reverse order.

This approach is O(n) time (assuming dictionary operations are O(1)), and then O(m log m) for the sorting, where m is the number of unique friends.

But since m can be up to n (if all friends are unique), in the worst case, the sorting is O(n log n), which for n=2e5 is acceptable (since 2e5 log 2e5 is around 2e5 * 18 ≈ 3.6e6 operations, which is manageable).

This approach avoids any linked list or list manipulations, which would be O(n) time per operation.

So the steps are:

1. Read all the messages, keeping track of the order (indices from 1 to n).

2. For each friend, record the last occurrence index (i.e., the maximum index where they appear).

3. Collect all unique friends, sort them by their last occurrence index in descending order.

4. Output the sorted list.

This approach is O(n) time for processing all messages, and O(m log m) for sorting, which is acceptable.

Now, how to implement this in Python.

Implementation steps:

- Read n.

- Read the next n lines into a list. Let's say messages.

- Create a dictionary (last_occurrence) where the key is the friend's name, and the value is the index (starting from 0 or 1? Since the first message is index 1, as per the sample. Wait in the first sample, the last occurrence of ivan is 4, which is the fourth message. So the indexes are 1-based.

So when processing each message, for the i-th message (starting from 1 to n), we update the last_occurrence of the friend to i.

Then, collect all the keys of last_occurrence into a list.

Sort this list in descending order of their last_occurrence values.

Then print each friend in that order.

Yes. That's straightforward.

Testing this approach with the samples:

First sample:

Messages: alex, ivan, roman, ivan (indices 1-4).

last_occurrence:

alex:1, ivan:4, roman:3.

sorted by last_occurrence descending: 4,3,1 → ivan, roman, alex. Which is correct.

Second sample:

messages 1-8:

last_occurrence:

alina:8

maria:7

ekaterina:6

darya:5.

sorted by descending order: 8,7,6,5 → alina, maria, ekaterina, darya. But the sample output is alina, maria, ekaterina, darya. But according to the actual steps, the final list is [alina, maria, ekaterina, darya]. Which matches the sorted list here.

Wait, but according to the actual processing steps in the second sample, the final list is alina, maria, ekaterina, darya. Which is the same as sorted by last occurrence.

So this approach works.

Therefore, this is the optimal solution.

Now, implementing this in Python.

But what about the order of elements with the same last occurrence? Well, since each message is processed in order, the last occurrence is unique for each friend (since each friend's last occurrence is when they were last mentioned). So no two friends will have the same last occurrence index.

So the sort is stable in that sense.

Now, code steps:

Read n.

Then read n lines, stripping whitespace (though problem says each name is a non-empty sequence, so input().strip() is safe).

Then, for each name in messages, track the last occurrence.

Then collect the keys of the last_occurrence dict.

Sort them in reverse order of their last_occurrence value.

Print each in that order.

In Python, the code would be:

n = int(input())

last_occurrence = {}

for i in range(n):

    name = input().strip()

    last_occurrence[name] = i  # since the index is 0-based? Wait, but in the samples, the indexes are 1-based. Wait no.

Wait, in the first sample, the messages are 1-4. If i is 0-based (0,1,2,3), then the last occurrence of ivan is 3 (the fourth message). So when sorted, 3, 2, 0. Then ivan (3), roman (2), alex (0). Which is correct. But in the sample, ivan's last occurrence is 4 (the fourth message, 1-based). So in the code, we need to use 1-based indexes.

So the loop should be for i from 1 to n, and store i as the index.

But in Python, when iterating through n lines, perhaps using enumerate:

for idx in range(n):

    name = input().strip()

    last_occurrence[name] = idx + 1  # 1-based index.

Then, when sorting, we sort the keys based on their value (which is 1-based) in descending order.

Yes.

So code:

n = int(input())

last_occurrence = {}

for i in range(n):

    name = input().strip()

    # Update the last occurrence to the current index (1-based)

    last_occurrence[name] = i + 1

# Now collect the names and sort them

sorted_names = sorted(last_occurrence.keys(), key=lambda x: -last_occurrence[x])

for name in sorted_names:

    print(name)

Wait, but in the second sample, the code would produce alina (8), maria (7), ekaterina (6), darya (5). Which is correct.

Yes, this code works for both samples.

But what about the time and memory?

For n=2e5, the loop is O(n) time, and the dictionary has up to 2e5 entries. Then, sorted in O(m log m), m up to 2e5. Which is acceptable.

In Python, sorted is TimSort, which is efficient.

But the problem says that the code must read input via input() and output via print(). So the code as written is correct.

But for handling large inputs, using sys.stdin might be faster. Because input() can be slow for 2e5 lines.

So perhaps using sys.stdin to read all lines at once.

But in Python, for 2e5 lines, the standard input methods can be slow if read line by line.

So perhaps using:

import sys

n = int(sys.stdin.readline())

last_occurrence = {}

for _ in range(n):

    name = sys.stdin.readline().strip()

    last_occurrence[name] = _ + 1

Then proceed as before.

But even that may not be the fastest. Alternatively, read all lines at once.

But for the problem constraints, perhaps the code as written is acceptable.

But in practice, for Python, reading 2e5 lines with input() is slow. So using sys.stdin would be better.

So the code should be optimized to read the input quickly.

So the code would be:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    last_occurrence = {}

    for idx in range(n):

        name = input_stream.readline().strip()

        last_occurrence[name] = idx + 1  # 1-based index

    # Sort the keys by descending order of their last occurrence index

    sorted_names = sorted(last_occurrence.keys(), key=lambda x: -last_occurrence[x])

    # Print the names in order

    print('\n'.join(sorted_names), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
alina
maria
ekaterina
darya
darya
ekaterina
maria
alina
""",
            "output": \
"""\
alina
maria
ekaterina
darya
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

Yes.

So this code should work.

The code is O(n) time and O(m) space, with m being the number of unique names. Then the sort is O(m log m), which is acceptable.

Therefore, this is the optimal solution.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    last_occurrence = {}
    for idx in range(n):
        name = sys.stdin.readline().strip()
        last_occurrence[name] = idx + 1  # Using 1-based index
    sorted_names = sorted(last_occurrence.keys(), key=lambda x: -last_occurrence[x])
    print('\n'.join(sorted_names))

if __name__ == "__main__":
    main()
```
