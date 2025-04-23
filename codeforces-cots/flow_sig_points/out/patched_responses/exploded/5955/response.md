<think>
Okay, let's see. The problem is to find the maximum length of a regular bracket sequence that can be formed by deleting some brackets from the given string. So the key points are that the resulting sequence must be regular, and we want the longest possible such sequence.

Hmm, regular brackets must have a balanced number of opening and closing brackets, and at no point should the number of closing brackets exceed the opening ones when scanning from left to right.

So the approach here might be similar to the standard problem where we track the balance of brackets. Let's think: when processing each character, we can keep track of the number of open brackets. For each closing bracket, if there's an available open bracket, we can use it. But we also need to account for cases where there are more closing brackets than opens in the middle, which would make the sequence invalid.

Wait, but how do we count the maximum possible valid pairs?

Another idea: the maximum possible length is twice the minimum between the total number of valid opening and closing brackets, considering the balance as we process the string.

Let me think. For example, in the first example input: (()))( 

Processing from left to right:

We can track the balance. The valid pairs would be the ones that contribute to a balanced sequence. But maybe we need two passes. One from left to right to count the valid closing brackets, and another from right to left to count the valid opening brackets. Wait, no, maybe there's a smarter way.

Alternatively, here's a standard approach I remember. To compute the maximum valid length, we can:

1. Traverse the string from left to right, keeping track of the current balance (open brackets minus close). If at any point the balance becomes negative, we reset it to zero and ignore those closing brackets. This gives us the maximum possible closing brackets that can be used without causing imbalance.

But wait, maybe that's not enough. Because after that, there might be an excess of opening brackets. So then, we need to do a similar check from the right side as well.

Wait, another approach: the maximum valid parentheses is determined by the number of pairs that can be formed without violating the balance condition. So during the first pass (left to right), we can count the number of valid closing brackets. Then, during the second pass (right to left), count the valid opening brackets. The answer is the minimum of these two counts multiplied by two, but maybe that's not accurate.

Wait, no. Let's think again. The correct approach might be:

- Keep track of the number of open and close brackets. But during the left-to-right pass, whenever a closing bracket would make the balance negative, we can't include it, so we ignore it. Then, the total number of valid closing brackets is the number of close brackets we could take. Similarly, the total number of valid opening brackets is limited by the same logic but processed from right to left. Then, the answer is the minimum between these two counts multiplied by 2.

Wait, maybe not. Let's see.

Let's take the first example: (()))( 

Left to right pass:

Initialize left balance to 0, right_balance to 0 (maybe not). Let's see:

The left pass would track the maximum possible closing brackets that can be used without the balance going negative.

Wait, here's the standard approach for the maximum valid substring problem. But in this problem, the substring can be any sequence (not necessarily contiguous). So maybe we need to adjust.

Alternatively, the problem is equivalent to finding the maximum number of matching pairs such that the balance never goes negative. So during processing, we can keep track of the current balance. For each '(', we increase the balance, for each ')', if the balance is positive, we decrease it and count a pair. But that would count all possible valid pairs, right?

Wait, let's take the first example:

Input: (()))( 

Processing left to right:

Balance starts at 0.

First '(', balance becomes 1. Total pairs so far 0.

Second '(', balance 2. Pairs 0.

Third ')', balance 1. Pairs 1.

Fourth ')', balance 0. Pairs 2.

Fifth ')', balance is 0, so can't take this ')', so pairs remain 2.

Sixth '(', balance 1. Pairs 2.

So total pairs is 2, so the answer would be 4. Which matches the first example's output.

Similarly, the second example input is ((()()). Let's process:

Each step:

'(', balance 1, pairs 0.

'(', balance 2.

'(', balance 3.

')', balance 2, pairs 1.

'(', balance 3.

')', balance 2, pairs 2.

')', balance 1, pairs 3.

Total pairs 3*2=6. Which matches the second example.

So this seems to work.

So the algorithm is:

- Traverse the string from left to right.

- Keep track of the current balance (open count minus close count).

- Also, keep a variable left_count for the number of '(' processed so far, and a variable right_count for the number of ')' processed.

Wait, no. Let's think again. The correct approach is:

Initialize left and right counts. Let's say left is the number of '(', right the number of ')'.

But no. Wait, in the first pass (left to right), we can track the maximum possible valid closing brackets. For example:

Initialize open = 0, close = 0.

For each character in the string:

   if the character is '(', then open +=1.

   else (it's ')'):

       if open > close:  # wait, no. Because balance is open - close. So if after adding this close, balance would be open - (close+1) >=0.

       So, if open > close:

           close +=1.

So the maximum number of pairs is the minimum of close and the total possible.

Wait, but after processing all characters, the number of pairs is the minimum between the total number of valid closing brackets and valid opening brackets.

Wait, for example, suppose we have a lot of '(' but not enough ')', then the number of pairs is limited by the number of ')'. Conversely, if there are more ')', but after processing, the valid pairs are limited by the opening brackets that could be matched.

So in the left to right pass, the close variable counts the number of closing brackets that can be matched with opening brackets. Then, the total pairs is min(close, open) if after processing all, the balance is open - close. But I'm not sure.

Alternatively, the algorithm would be:

Initialize open_count and close_count to 0.

Traverse the string from left to right:

   if char == '(', then open_count +=1.

   else:

       if open_count > close_count:

           close_count +=1.

So after this, the number of pairs is min(open_count, close_count). But this is not correct.

Wait, for example, input "(()))(".

In the left to right pass:

open_count starts at 0, close_count 0.

First '(', open becomes 1.

Second '(', open 2.

Third ')', since open (2) > close (0), close becomes 1.

Fourth ')', open (2) > close (1), so close becomes 2.

Fifth ')', open (2) is not > close (2), so no change.

Sixth '(', open becomes 3.

So after processing, open is 3, close is 2.

So the minimum is 2, so the answer is 4. Which is correct.

Another example: "((()())". Let's see.

Processing left to right:

'(', open 1.

'(', open 2.

'(', open 3.

')', open (3) > close (0), close becomes 1.

'(', open 4.

')', open (4) > close (1), close becomes 2.

')', open (4) > close (2), close becomes 3.

So open is 4, close is 3. So min(4,3) is 3, answer is 6. Correct.

So this approach works. But wait, what if the total number of opening and closing brackets is such that after processing, open_count is larger than close_count? Then the actual pairs is the close_count. Because every closing bracket is matched with an opening. So the total pairs is min(close_count, open_count). But since after processing, close_count can't exceed open_count. Because in the left to right pass, we only increment close_count if open_count is larger than the current close_count. So close_count will be <= open_count. Thus, the total pairs is close_count. But in the first example, close_count is 2, which is the correct answer. In the second example, close_count is 3, but open_count is 4, so the answer is 3. So the correct answer is close_count multiplied by 2.

Wait, in the second example, the answer is 3 *2=6, which is correct.

So the algorithm is: in left to right pass, count the maximum possible close brackets that can be matched (close_count). Then, the answer is close_count *2.

Wait, but how? Because in the left to right pass, each time we process a ')', we check if open_count (current number of '(' seen) is greater than the current close_count (number of ')' matched so far). So for each ')', if there's an available '(', we can match it. So the close_count is the number of matched pairs. But the actual number of pairs is close_count. So the answer is close_count *2.

Yes. Because each pair is one '(', one ')', so two characters. So the maximum length is 2 * close_count.

So this approach seems to work.

But wait, what about cases where the opening brackets are in excess but some of them are not properly closed. For example, a string like "((()". Then, the left to right pass would process:

'(', open 1.

'(', open 2.

'(', open3.

')', close 1.

So close_count is 1, open is 3. So answer would be 2*1=2. But the correct answer is 2. Because the valid sequence is "()".

Yes. So that's correct.

Another example: ")(".

Left to right pass:

First ')', open is 0, so no increment to close_count.

Then '(', open becomes 1.

close_count is 0. So answer is 0. Which is correct.

So this algorithm works.

But wait, another case: "())". Left to right:

'(', open 1.

')', open>close (0), so close becomes 1.

')', open is 1, close is 1. So no increment. So close_count is 1. Answer is 2. Which is correct.

So this approach seems to handle all cases.

So the code can be written as follows:

Initialize open_count and close_count to 0.

Loop through each character in the string:

   if char is '(':

       open_count +=1

   else:

       if open_count > close_count:

           close_count +=1

Then, the result is close_count * 2.

Wait, but what about cases where the close_count is less than the open_count, but there are enough closing brackets to the left of some opens. For example, suppose the string is "(()". Then open_count is 3, close_count is 1. So answer is 2. But the maximum is 2, which is correct.

So yes.

So this seems to be the correct approach.

Wait, but wait another example: "(()())". The code would process:

All opens and closes. The close_count would be 3. Answer is 6. Correct.

But what if the string is "())()("?

Wait, let's process left to right:

')', open is 0, close_count remains 0.

')', open is 0, close_count 0.

'(', open 1.

')', open (1) > close (0), so close becomes 1.

'(', open 2.

Result: close_count is 1. So answer is 2. But the actual maximum is 2, from the "()" in positions 3 and 4.

Yes, correct.

So the algorithm works.

Thus, the code can be written as:

Read the input string.

Initialize open_count = 0, close_count =0.

For c in s:

   if c == '(':

       open_count +=1

   else:

       if close_count < open_count:

           close_count +=1

result = close_count *2

print(result)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    open_count = 0
    close_count = 0
    for c in s:
        if c == '(':
            open_count += 1
        else:
            if close_count < open_count:
                close_count += 1
    print(close_count * 2, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
((()())
""",
            "output": \
"""\
6
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

Another example: "(()))(" → same result.

Yes. So this code works.

But wait, what about the case where there are more closing brackets but they are in the right order. For example: "()))((...(" (a lot of closing first, then opens). For example: "))((()".

Processing left to right:

First two ')', open is 0, so close_count remains 0.

Then two '(', open becomes 2.

Then '(', open 3.

Then ')', close_count is 0, open is 3. So close_count increments to 1.

So the answer is 2.

Which is correct. The maximum valid is "()".

So the code is correct.

So the code seems to handle all cases. Thus, the optimal approach is O(n) time and O(1) space. Which is perfect for the constraints (up to 1e6 characters).

So the code is simple, efficient, and meets the requirements.
</think>

To solve this problem, we need to determine the maximum length of a regular bracket sequence that can be formed by removing some brackets from the given string. A regular bracket sequence is one where every opening bracket has a corresponding closing bracket in the correct order.

### Approach
The key insight to solve this problem efficiently is to track the balance of opening and closing brackets as we traverse the string from left to right. We maintain two counters:
1. `open_count` to keep track of the number of opening brackets encountered.
2. `close_count` to keep track of the number of valid closing brackets that can form pairs with the encountered opening brackets.

For each character in the string:
- If the character is an opening bracket `'('`, we increment `open_count`.
- If the character is a closing bracket `')'`, we check if there are more opening brackets than closing brackets encountered so far. If true, we increment `close_count` as this closing bracket can form a valid pair with a previous opening bracket.

The maximum length of the regular bracket sequence is twice the value of `close_count` since each valid pair consists of one opening and one closing bracket.

### Solution Code
```python
s = input().strip()
open_count = 0
close_count = 0
for c in s:
    if c == '(':
        open_count += 1
    else:
        if close_count < open_count:
            close_count += 1
print(close_count * 2)
```

### Explanation
- **Initialization**: We start with both `open_count` and `close_count` set to 0.
- **Traversal**: As we traverse each character in the string:
  - For each opening bracket `'('`, we increment `open_count`.
  - For each closing bracket `')'`, we check if there are more opening brackets than closing brackets encountered so far. If there are, we increment `close_count` to form a valid pair.
- **Result Calculation**: The result is twice the value of `close_count` because each valid pair contributes 2 characters to the length of the regular bracket sequence.

This approach ensures we efficiently determine the maximum length of a valid bracket sequence in linear time, O(n), where n is the length of the input string. The space complexity is O(1) as we only use a constant amount of additional space. This makes the solution optimal for handling the upper constraint of the input size efficiently.
