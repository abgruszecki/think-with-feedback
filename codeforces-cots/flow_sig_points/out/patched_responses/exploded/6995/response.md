<think>
Okay, let's tackle this problem. So, the task is to reverse the process of inserting WUBs into the original song. The original song's words were separated by at least one WUB, and possibly more. Also, there could be any number of WUBs before the first word and after the last. Our job is to split the remixed string back into the original words, joining them with single spaces.

Hmm, the key here is that the original words don't contain "WUB". So when we split the remix string by occurrences of "WUB", the original words are the non-empty parts left. But since there can be multiple WUBs between words, those would split into empty strings. So the approach is to split the input string on "WUB" and then filter out any empty strings from the result. Then, join the remaining parts with spaces.

Wait, right. For example, take the first sample input: "WUBWUBABCWUB". Splitting on "WUB" gives ['', '', 'ABC', '']. Filtering out the empty strings leaves ['ABC'], which is the correct output. The second example: the input splits into parts where the non-empty parts are the original words. So after splitting and filtering, the list of words is correct.

So the steps are:

1. Split the input string by "WUB".
2. Remove all empty strings from the resulting list.
3. Join the remaining elements with a single space.

But how to split in Python? The split method by default splits on consecutive occurrences, so for example, "WUBWUB" would split into ['', ''] and then those are removed, leading to nothing. But when there are multiple WUBs between words, like in the second example between "ARE" and "THE" (two WUBs), splitting on "WUB" would split into ['ARE', '', 'THE'], then filtering gives ['ARE', 'THE'].

So the split function in Python's string.split('WUB') will split on each occurrence, even consecutive ones. So for example, 'WUBWUB' would split into ['', ''].

Therefore, the approach is to split the input string using 'WUB' as the delimiter, then filter out any empty strings from the resulting list, and then join those elements with spaces.

Now, the code would look something like:

s = input().strip()
parts = s.split('WUB')
words = [part for part in parts if part]
print(' '.join(words))

Wait, but let's test this against the examples.

First example: input is 'WUBWUBABCWUB'. Split into ['', '', 'ABC', '']. Filter gives ['ABC'], joined gives 'ABC' which is correct.

Second example: the input after split is parts like ['', 'WE', 'ARE', '', 'THE', 'CHAMPIONS', 'MY', 'FRIEND', ''], then filtering gives ['WE', 'ARE', 'THE', 'CHAMPIONS', 'MY', 'FRIEND'], which is the correct output.

Yes, that works. So this approach should handle all cases. Because even if there are leading or trailing WUBs, split will include them as empty parts which are then filtered out.

So the code is straightforward. No need for any complex data structures. Split, filter, join.

What about edge cases? Like the original song is a single word. For example, input is 'WUBHELLOWUB' → split into ['', 'HELLO', ''] → filter gives ['HELLO'] → output correct. Another case where the input is just the original word with no WUBs, like input is 'TEST'. Split into ['TEST'], filter gives ['TEST'] → correct.

So this solution should handle all possible cases as per the problem constraints.

In terms of time and memory constraints: the input string is up to 200 characters, which is very small. Splitting and filtering is O(n) time and space, which is acceptable. So the code should work efficiently.
</think>

```python
print(' '.join(filter(None, input().split('WUB'))))
```