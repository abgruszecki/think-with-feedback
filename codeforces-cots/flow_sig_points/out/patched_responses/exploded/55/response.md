<think>
Okay, let's tackle this problem. So the task is to find the longest valid parentheses substring and count how many times such maximum-length substrings occur. Hmm. I remember that there's a dynamic programming approach for the longest valid parentheses problem. But wait, how do we also count the number of those maximum-length substrings?

Let's think. The classic problem just finds the maximum length, but here we need to also count the occurrences. So, maybe during the DP process, we can track both the maximum length and the count of substrings that achieve that length.

Alternatively, there's another approach using a stack. The stack method for longest valid parentheses uses a stack to keep track of the indices of the parentheses. For example, when we encounter a '(', we push its index. When we encounter a ')', we pop the top and calculate the length. But how do we track the count?

Wait, let's recall the stack approach. The stack usually starts with a -1 as a base for calculating lengths. For each ')', if the stack is not empty after popping, the current index minus the top of the stack gives the length of a valid substring. So maybe during this process, whenever we find a valid length, we can check if this length is equal to the current maximum and update the count accordingly.

But there's a problem here. For example, when we have multiple valid substrings of the same maximum length, how do we count them without overlapping or missing some cases? Also, how do we track the positions of these valid substrings to ensure they are distinct?

Hmm. Let's think of a scenario. Suppose the input is "(()())". The valid substrings are of length 6. But how many times does this occur? Once. So in this case, the count is 1. Another example: the sample input given is ")((())))(()())", which outputs 6 2. So there are two substrings of length 6. Let's see: ((())) and (()()). Oh wait, maybe the first part is ((())) and then the second part is (()()) but in the input, maybe there are two separate sections that are valid and each of length 6.

So the idea is that each time we find a valid substring of length equal to the current maximum, we increment the count. If we find a longer length, we reset the count and update the maximum.

But how to do this efficiently.

Another idea is to track for each possible valid substring length, the number of times it occurs. Then, once the maximum is found, the count is the sum of the entries for that maximum length. But that could be memory intensive if we track all possible lengths. But perhaps during the process, we can keep track of the current maximum and the count, updating them as we go.

Let's consider the stack approach. Let's have a stack that starts with -1. For each character in the string:

- If '(', push index.
- If ')', pop the top. If the stack is now empty, push current index. Otherwise, the current length is i - stack[-1]. We can then check if this length is greater than the current maximum, and update accordingly. If it's equal to the current maximum, increment the count. But wait, this might not capture all possible cases. Because multiple valid substrings could be overlapping in their way of contributing to the same maximum.

Wait, for example, in the string "()()()", each pair is a valid substring of length 2, but the entire string is of length 6. So when we process each ')', the stack would have -1, 0, etc. Wait, let's step through this example.

Indices: 0 1 2 3 4 5 6 (assuming 0-based)

Wait, let's take the string "()()()":

Indices 0: '(', push 0. Stack becomes [-1, 0].

Index 1: ')', pop 0. Stack is now [-1]. Current length is 1 - (-1) = 2. Max is 2, count is 1.

Index 2: '(', push 2. Stack is [-1, 2].

Index 3: ')', pop 2. Stack becomes [-1]. Length is 3 - (-1) =4. So new max is 4, count becomes 1.

Index 4: '(', push 4. Stack is [-1,4].

Index5: ')', pop 4. Stack becomes [-1]. Length is 5 - (-1) =6. New max 6, count 1.

So in this case, the algorithm would correctly find the maximum length as 6, count 1.

But how does the algorithm track overlapping sequences that contribute to the same maximum?

Another example: the sample input given, ((())))(()()). Let's see:

The input is ")((())))(()())".

Breaking it down:

The valid substrings are ((())) (indices 2-7, length 6) and (()()) (indices 9-14, length 6). So two substrings. So the algorithm should count these two.

In the stack approach, when processing each ')', the calculated length is i - stack[-1]. For the first ((())) part, the stack after processing each ')': for example, when index is 5, which is a ')', pop, then check stack. Let's see:

But let's imagine the stack processing.

Let me think through the sample input step by step.

Sample input: ")((())))(()())"

Indices 0-based:

0: ')', stack is initially [-1]. So we pop -1, stack is empty, push 0. Now, stack is [0].

1: '(', push 1. Stack [0,1].

2: '(', push 2. Stack [0,1,2].

3: '(', push 3. Stack [0,1,2,3].

4: ')', pop 3. Stack is [0,1,2]. Current length is 4 - 2 = 2. Max is 2, count 1.

5: ')', pop 2. Stack [0,1]. Current length 5-1=4. Max becomes 4, count 1.

6: ')', pop 1. Stack [0]. Current length 6-0=6. Max becomes 6, count 1.

7: ')', stack is [0], pop 0. Stack is empty, so push 7.

8: '(', push 8. Stack [7,8].

9: '(', push 9. Stack [7,8,9].

10: ')', pop 9. Stack [7,8]. Length 10-8=2. Current max is 6, so this doesn't affect.

11: '(', push 10. Stack [7,8,10].

12: ')', pop 10. Stack [7,8]. Length 12-8=4. Still not longer than 6.

13: ')', pop 8. Stack [7]. Length 13-7=6. This equals the current max, so count becomes 2.

So in this case, the algorithm would find two instances where the length is 6. So the count is 2. Which matches the sample.

So the approach here is:

- Use a stack to track the positions of the parentheses.

- For each ')', after popping the top, calculate the current length as i - stack[-1].

- Compare this length with the current maximum. If it's larger, update the max and reset the count to 1. If it's equal to the max, increment the count. If it's smaller, do nothing.

But wait, how do we handle multiple occurrences of the same max length that are part of the same valid substring? For example, in a case where there's a long valid substring, but during the processing, the same max is found multiple times. But in reality, it's part of one substring, but how does the algorithm count this.

Wait, perhaps that's a problem. For example, consider the string "((()))". The stack processing would be:

- stack starts with -1.

Indices 0: '(', push 0. stack [-1,0].

1: '(', push 1. stack [-1,0,1].

2: '(', push 2. stack [-1,0,1,2].

3: ')', pop 2. stack becomes [-1,0,1]. current length 3 -1 = 2. max is 2, count 1.

4: ')', pop 1. stack becomes [-1,0]. current length 4 -0 =4. new max 4, count 1.

5: ')', pop 0. stack becomes [-1]. current length 5 - (-1) =6. new max 6, count 1.

So the algorithm correctly counts 1 here.

So, the approach seems to work. Each time a valid substring is found, the length is calculated, and if it's the current max, the count is updated.

But how to handle overlapping valid substrings. For example, in the case of "()(())", the entire string is valid. The maximum is 6. But during processing, the algorithm would find the length 2, then 4, then 6. Each time, the max increases, so the count is reset. So in the end, count is 1.

But there's only one valid substring of length 6. So it's correct.

Another example: "()()()". The max is 6. The algorithm, during processing the last ')', would calculate 6 as the length, which is larger than previous max of 4. So the count becomes 1.

So in this case, the algorithm returns 6 and 1, which is correct.

So the stack approach seems to work. So the steps would be:

Initialize a stack with -1.

Initialize max_length to 0 and count to 0.

For each index i in the string:

   if s[i] is '(', push i to stack.

   else:

      pop the top.

      if stack is empty:

          push i

      else:

          current_length = i - stack[-1]

          if current_length > max_length:

              max_length = current_length

              count = 1

          elif current_length == max_length:

              count +=1

But wait, there's a problem here. For example, consider the case where a valid substring is part of a longer valid substring. For instance, in the case of "(()())", the entire string is valid. Let's see:

Indices 0: '(', stack becomes [-1,0]

1: '(', stack becomes [-1,0,1]

2: ')', pop 1. stack becomes [-1,0]. current_length = 2-0=2. So max_length is 2, count 1.

3: '(', push 3. stack [-1,0,3]

4: ')', pop 3. stack [-1,0]. current_length =4-0=4. new max_length 4, count 1.

5: ')', pop 0. stack [-1]. current_length=5 - (-1) =6. new max_length 6, count 1.

So in this case, the count is 1, which is correct.

But what if there are multiple valid substrings of the same maximum length?

Like in the sample input. When processing the first ((())) part, it's 6 length. Then later, processing the (()()), it's 6 again. So during each of those steps, the count is incremented.

So the algorithm as described would work.

But wait, when the algorithm processes each ')', it checks the current length. So each time a valid substring is found, even if it's part of a larger one, it's considered. But in the case where a longer substring is found, the count is reset. So overlapping or smaller valid substrings within a larger one are accounted for only if they reach the same max length.

So this approach seems to capture the number of times a valid substring of maximum length occurs.

But wait, in some cases, the same valid substring could be counted multiple times. For example, consider a string like "(()())". Let's see:

Indices 0: '(', stack [-1,0]

1: '(', stack [-1,0,1]

2: ')', pop 1. Stack is [-1,0], current_length 2-0=2. max 2, count 1.

3: '(', stack becomes [-1,0,3]

4: ')', pop 3. Stack is [-1,0]. current_length 4-0=4. new max 4, count 1.

5: ')', pop 0. Stack is [-1]. current_length 5-(-1)=6. new max 6, count 1.

So the count is 1. Correct.

But in a case like "((())))(()())", the two 6-length substrings are separate. Each time when the algorithm processes the end of each substring, it calculates the length and increments the count.

But how does the algorithm detect that they are separate? Because the stack's top after popping gives the base index. For example, the first 6-length substring ends at index 6 (the third ')'). Then after that, the stack is pushed with index 7 (because after popping 0, the stack is empty and we push 7). Then later, when processing the substring (()()), the last ')', index 13, after popping 8, stack has 7. current_length is 13-7=6. Which is equal to the max_length, so count increments to 2. So this correctly counts two separate substrings.

So this approach works.

So the algorithm is:

- Use a stack to track the indices of the parentheses.

- Keep track of the maximum length found so far and the count of substrings with that length.

- For each ')', after popping, if the stack is not empty, compute the current_length. Update max_length and count as needed.

Now, the next step is to implement this in Python, ensuring that it's efficient for large input sizes (up to 1e6 characters). So the code must be O(n) time and O(n) space.

But in Python, for strings up to 1e6, O(n) space should be manageable. The stack can have up to O(n) elements in the worst case (all '('s). So for 1e6, that's 4MB per int (but in Python, ints take more memory, but 1e6 elements are manageable).

Now, the code:

We'll need to process each character in the input string. We'll initialize a stack with -1. Then, iterate through each character, track the index. For each ')', pop the top. If stack is empty, push current index. Else, compute current_length = i - stack[-1]. Compare with max_length.

But we have to handle the case where current_length is equal to the max_length. So:

Initialize max_length = 0, count = 0.

For each i in range(len(s)):

   if s[i] is '(':

       stack.append(i)

   else:

       stack.pop()

       if not stack:

           stack.append(i)

       else:

           current_length = i - stack[-1]

           if current_length > max_length:

               max_length = current_length

               count = 1

           elif current_length == max_length:

               count +=1

But wait, in the case where the same valid substring is extended. For example, when processing a ')', the current_length is i - stack[-1]. If a previous valid substring had the same length, but it's part of the same larger substring, this approach might count multiple times. But in reality, each time you extend the valid substring, the current_length is the entire length. So for example, in "(()())", the processing steps when the first '()' is processed, then the next '()' is processed, but the algorithm only counts the full length once.

Wait, let's take the example of "(()())".

Indices 0: '(', stack [-1,0]

1: '(', stack becomes [-1,0,1]

2: ')', pop 1. Stack is [-1,0]. current_length =2-0=2. max_length=2, count=1.

3: '(', stack becomes [-1,0,3]

4: ')', pop 3. Stack is [-1,0]. current_length=4-0=4. So now, max_length is 4, count=1.

5: ')', pop 0. Stack is [-1]. current_length=5-(-1)=6. So max becomes 6, count=1.

So the code correctly captures that. So each time a longer length is found, the count is reset to 1. If the same max is found again, the count is incremented.

But what about when a substring is part of a longer substring? Like, suppose the string is "()()". The maximum length is 4. But during processing, when the second '()' is processed, the current_length would be 3 - stack[-1] (stack[-1] is 0, after popping 1). So 3-0=3. Which is longer than the previous max of 2. So max becomes 3, count=1. Then when processing the fourth character, which is ')', stack after pop is [-1]. current_length is 3-(-1)=4. So max becomes 4, count=1. So even though the entire string is valid, the code captures it once.

But in reality, the entire string is a single valid substring of length 4, and two smaller ones of length 2. But the code counts the maximum correctly.

So the code seems to be correct.

But what about the case where multiple substrings of the same maximum length are present but not overlapping? For example, "(())(())". The maximum is 4, and there are two such substrings. Let's see:

Indices 0: '(', stack [-1,0]

1: '(', stack becomes [-1,0,1]

2: ')', pop 1, stack [-1,0]. current_length=2-0=2. max=2, count=1.

3: ')', pop 0, stack [-1]. current_length=3-(-1)=4. max becomes 4, count=1.

4: '(', stack becomes [-1,4]

5: '(', stack becomes [-1,4,5]

6: ')', pop5, stack [-1,4]. current_length=6-4=2. which is less than 4, so no change.

7: ')', pop4, stack [-1]. current_length=7-(-1)=8. new max is 8, count=1. So here, the code would return 8 as the max, count 1, which is correct because the entire string is a valid substring of length 8. But the example I thought of was "(())(())" which is two substrings of length 4, but the code shows that they are part of a larger substring. So perhaps that example isn't valid. Let's check: the entire string "(())(())" is actually "(())(())", which is valid. So the code would find a max of 8, count 1. So in this case, the code is correct. So the example I should think of is a case where two separate substrings of the same maximum length exist, not part of a longer substring.

Like the first sample input. So the code works for that case.

So the code seems to handle all the cases.

Now, edge cases:

Case 1: empty string. But according to the problem statement, the input is a non-empty string. So no need to handle that.

Case 2: all '('s. Then the max is 0, count 1 (since there are no valid substrings, the output is 0 1). Wait, the problem states: if there are no valid substrings, output 0 1. So when the maximum length is 0, the count is 1. So the code must handle that.

Wait, in the code as written, when the input is "))(", the code will process as:

stack starts with -1.

index 0: ')', pop -1, stack is empty. Push 0.

index 1: ')', pop 0. stack empty. Push 1.

index 2: '(', push 2. Stack becomes [1,2].

At the end, the max_length remains 0. So the code would output max_length (0) and count (0). But according to the sample input 2, which is "))(", the output is 0 1.

So the code as written would output 0 0. Which is wrong.

So what's the issue here?

Ah, right. Because in cases where no valid substrings exist, the code's count remains 0, but the problem requires outputting 0 1.

So we need to handle the case where the maximum length is 0: set count to 1.

So after processing all characters, if max_length is 0, then the count is 1. Else, use the count as computed.

So in the code, after the loop, if max_length is 0, then output 0 1. Else, output max_length and count.

So that's a crucial point.

So in the code:

After processing all characters, check if max_length is 0. If so, output 0 1. Else, output max_length and count.

So the code would need to account for this.

Another example: input ")()".

Indices:

0: ')', pop -1, stack empty. Push 0.

1: '(', push 1. Stack [0,1].

2: ')', pop 1. Stack [0]. current_length =2 -0 =2. So max_length is 2, count 1.

So output is 2 1. Which is correct.

Another example: input "))(", the code processes all characters, ends up with max_length 0. So output 0 1.

So the code must have this final check.

Therefore, the code steps are:

Initialize stack with -1.

max_length = 0

count = 0

for each i in range(len(s)):

    if s[i] == '(':

        stack.append(i)

    else:

        stack.pop()

        if not stack:

            stack.append(i)

        else:

            current_length = i - stack[-1]

            if current_length > max_length:

                max_length = current_length

                count = 1

            elif current_length == max_length:

                count +=1

After processing all characters:

if max_length == 0:

    print("0 1")

else:

    print(f"{max_length} {count}")

But wait, in the case where there are no valid substrings, but max_length is 0, but there are multiple possible ways (like overlapping zero-length), but according to the problem statement, when there are no valid substrings, output 0 1. So regardless of how many zero-length substrings there are (which is impossible since zero-length is not valid), but the problem says, when there are no valid substrings, output 0 1. So even if there are multiple separate valid substrings of length 0 (which is impossible), but the problem's note says: if there are no valid substrings, output 0 1.

So whenever the maximum length is zero, output 0 1.

So in the code, after processing all characters, if max_length is zero, output 0 1. Else, output the max and count.

So in the case where the input is "())", the valid substrings are "()" (length 2), and another "()" (length 2). So the code would count two.

Wait, let's see:

input "())"

Indices 0: '(', push 0. Stack [-1,0].

1: ')', pop 0. Stack [-1]. current_length 1 - (-1) =2. max_length 2, count 1.

2: ')', pop -1. Stack is empty, push 2.

So max_length is 2, count is 1. So output 2 1.

But in the input "())", the valid substrings are at indices 0-1 and 2 (but there's a third character? No. Let's see. The input "())" has two ')', but the valid substrings are the first two characters (0 and 1: '()') which is valid. The third character is ')', so no other valid substrings. So the code's output of 2 1 is correct.

So the code's approach is correct.

So the code now needs to handle the case where the maximum is zero.

Thus, the code structure is:

Read the input string.

Initialize stack with -1.

max_len = 0

count = 0

for i, char in enumerate(s):

    if char == '(':

        stack.append(i)

    else:

        stack.pop()

        if not stack:

            stack.append(i)

        else:

            curr_len = i - stack[-1]

            if curr_len > max_len:

                max_len = curr_len

                count = 1

            elif curr_len == max_len:

                count +=1

if max_len ==0:

    print("0 1")

else:

    print(f"{max_len} {count}")

This should handle all cases.

Testing the sample input 1:

Sample Input 1: ")((())))(()())"

Processing steps:

stack starts with [-1]

i=0, char is ')', stack.pop() is -1. stack is empty. append 0. stack [0]

i=1, char is '(', append 1. stack [0,1]

i=2, char '(', append 2. stack [0,1,2]

i=3, char '(', append3. stack [0,1,2,3]

i=4, char ')', pop3. stack [0,1,2]. curr_len=4-2=2. max_len=2, count=1.

i=5, char ')', pop2. stack [0,1]. curr_len=5-1=4. max_len=4, count=1.

i=6, char ')', pop1. stack [0]. curr_len=6-0=6. max_len=6, count=1.

i=7, char ')', pop0. stack is empty. append7. stack [7]

i=8, char '(', append8. stack [7,8]

i=9, char '(', append9. stack [7,8,9]

i=10, char ')', pop9. stack [7,8]. curr_len=10-8=2. less than 6.

i=11, char '(', append10. stack [7,8,10]

i=12, char ')', pop10. stack [7,8]. curr_len=12-8=4. less than 6.

i=13, char ')', pop8. stack [7]. curr_len=13-7=6. equals max_len, count becomes 2.

i=14, char ')', pop7. stack is empty. append14.

So max_len is 6, count is 2. So output is 6 2. Correct.

Sample Input 2: "))(".

Processing:

i=0: ')', stack.pop(-1) → stack empty. append0. stack [0]

i=1: ')', stack.pop0. stack empty. append1. stack [1]

i=2: '(', append2. stack [1,2]

At the end, max_len remains 0. So output 0 1. Correct.

So the code seems to handle all cases.

Now, considering the constraints. The input can be up to 1e6 characters. Python's for loop should handle that efficiently. The stack operations are O(1) per step, so O(n) time. The space is O(n) for the stack, which is acceptable.

Thus, this code should work.
</think>

```python
s = input().strip()
stack = [-1]  # Initial base for length calculation
max_len = 0
count = 0

for i, char in enumerate(s):
    if char == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            curr_len = i - stack[-1]
            if curr_len > max_len:
                max_len = curr_len
                count = 1
            elif curr_len == max_len:
                count += 1

if max_len == 0:
    print("0 1")
else:
    print(f"{max_len} {count}")
```