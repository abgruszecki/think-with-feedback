<think>
Okay, let's see the problem here. So, we need to check if the pile of letters can exactly form the combination of the guest's name and the host's name. No extra letters, no missing ones. 

Hmm, the approach here would probably involve counting the letters. Like, we need to count all the letters in the first two lines (guest and host) and see if the third line (the pile) has exactly those letters in the same quantities.

So the steps would be: 

1. Concatenate the guest name and host name into a single string. Let's call this combined_str.
2. Create a frequency count (like a dictionary) of each character in combined_str.
3. Create a frequency count for the pile letters.
4. Compare the two frequency counts. If they are exactly the same, output YES, else NO.

That makes sense. Because the order doesn't matter, just the counts. So the key is to check if the combined letters of guest and host match exactly the pile's letters.

Now, how to implement this efficiently in Python.

In Python, using the collections.Counter class would be straightforward. But wait, since the input lines could be up to 100 each, the combined length could be up to 200, and the pile up to 100+100=200 (if the third line is as per the problem). So the maximum possible is 200 characters each. So even a straightforward method would work, as the data is small. So there's no problem with time here. Even O(n) algorithms would be fine.

So the code steps:

Read the three lines: guest, host, pile.

Combine guest and host into a single string. Then compare the Counter of this combined string with the Counter of the pile.

If they are equal, output YES, else NO.

But wait, there's a possible edge case where the combined length of guest + host is not equal to the pile's length. For example, if guest is "A", host is "B", and the pile is "AA", then even if counts for A and B in the pile don't match, but the lengths are different. Wait, no. Because if combined length is 2 (guest + host), and the pile is length 2, then each character must be present exactly once. But if the pile is longer or shorter, then the counts can't possibly match. So checking the total length first would be a quick way to catch this.

So first, check if the sum of the lengths of guest and host equals the length of the pile. If not, immediately output NO. Otherwise, proceed to check the counts.

That's a good optimization. Because if the lengths are different, it's impossible. So adding this check can save us some computation. For example, if the combined length is 5 and pile is 6, then even if counts are same but with an extra letter, the sum is different, so we can return NO immediately.

So the steps would be:

1. Read guest, host, pile.
2. Check if len(guest) + len(host) == len(pile). If not, output NO.
3. Else, check if Counter(guest + host) equals Counter(pile). If yes, output YES, else NO.

Yes. That's the plan.

Now, code-wise, how to implement this.

In Python:

We can use the Counter class from the collections module. But since the problem might have uppercase letters only, and the counts are straightforward.

So code:

Read the three lines:

guest = input().strip()
host = input().strip()
pile = input().strip()

Then, combined = guest + host

if len(combined) != len(pile):
    print("NO")
else:
    from collections import Counter
    if Counter(combined) == Counter(pile):
        print("YES")
    else:
        print("NO")

Wait, but importing inside the else block might not be allowed. Or perhaps better to import at the top. But in Python, importing inside a function or conditional is allowed, though it's not the best practice. So perhaps moving the import to the top.

But in code submission, it's better to have the imports at the top. So let's adjust:

So the code would be:

Testing against sample input 1.

```python
from collections import Counter


def main(input_stream, output_stream):
    guest = input_stream.readline().rstrip("\n").strip()
    host = input_stream.readline().rstrip("\n").strip()
    pile = input_stream.readline().rstrip("\n").strip()

    combined = guest + host

    if len(combined) != len(pile):
        print("NO", file=output_stream)
    else:
        if Counter(combined) == Counter(pile):
            print("YES", file=output_stream)
        else:
            print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
PAPAINOEL
JOULUPUKKI
JOULNAPAOILELUPUKKI
""",
            "output": \
"""\
NO
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
from collections import Counter


def main(input_stream, output_stream):
    guest = input_stream.readline().rstrip("\n").strip()
    host = input_stream.readline().rstrip("\n").strip()
    pile = input_stream.readline().rstrip("\n").strip()

    combined = guest + host

    if len(combined) != len(pile):
        print("NO", file=output_stream)
    else:
        if Counter(combined) == Counter(pile):
            print("YES", file=output_stream)
        else:
            print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
BABBONATALE
FATHERCHRISTMAS
BABCHRISTMASBONATALLEFATHER
""",
            "output": \
"""\
NO
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

Third sample: combined length is len(BABBONATALE) = 10, len(FATHERCHRISTMAS) is 15 → combined is 25. Pile is BABCHRISTMASBONATALLEFATHER → let's see: BABCHRISTMASBONATALLEFATHER → how many letters? Well, the code checks the length. If the combined is 10+15=25, and the pile is 25, then proceed. But in the sample output, there's an extra L, so the counts would differ. So the code will output NO.

So the code handles all the cases.

Another test case: when the combined length is same as pile, but letters are different. Like guest is "A", host is "B", pile is "AB" → YES. If pile is "AC" → NO. If combined is "AB" and pile is "AAB" → len check would fail (combined is 2, pile is 3 → output NO).

Yes. So this code should work.

But what about the order of the letters? Because the code uses Counter, which is unordered, so the order doesn't matter. So it's correct.

Therefore, this approach is optimal. The time and space are O(1) because the input is small. Even for maximum input (each line up to 100, so combined up to 200), the code runs in linear time, which is acceptable.

So the code should pass all test cases.
</think>

```python
from collections import Counter

guest = input().strip()
host = input().strip()
pile = input().strip()

combined = guest + host

if len(combined) != len(pile):
    print("NO")
else:
    print("YES" if Counter(combined) == Counter(pile) else "NO")
```
