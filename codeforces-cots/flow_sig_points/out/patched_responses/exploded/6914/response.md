<think>
Okay, I need to solve this problem where I check if a given bracket sequence is balanced. Let's think about how to approach this.

First, the problem states that a balanced sequence can be turned into a valid math expression by adding + and 1. So, essentially, the brackets must be properly nested and each opening bracket has a corresponding closing one in the right order. Like the classic valid parentheses problem.

So, the standard approach for checking balanced parentheses is using a stack. For every '(', we push it onto the stack, and for every ')', we pop if the stack is not empty and the top is '('. If at any point a closing bracket doesn't have a matching opening, it's invalid. Also, at the end, the stack must be empty.

But wait, there's another condition here. Even if the stack doesn't underflow, but the number of closing brackets exceeds the opening ones at any point, it's invalid. For example, if the string starts with ')', then it's immediately unbalanced.

So the steps would be:

1. Initialize a counter (or a stack-like counter, since we don't need to track the actual brackets, just the balance).
2. Iterate through each character in the string.
3. For each '(', increment the counter.
4. For each ')', decrement the counter.
5. If at any point the counter goes negative, return NO because there's a closing bracket without a matching opener before it.
6. After processing all characters, check if the counter is zero. If yes, return YES, else NO.

Wait, that's right. Because the counter represents the current balance of open brackets. If it's ever negative, there's more closing than open, which can't be balanced. And at the end, if it's zero, all opens are closed properly.

So using a simple integer variable as a stack counter is sufficient here. No need for a full stack. That's efficient in terms of both time and space.

Now, let's think about possible edge cases.

Test case 1: Empty string. But according to the input constraints, the string is between 1 and 100 characters. So no empty input.

Test case 2: All opening brackets. Like "(((", which would leave the counter at 3. So output NO.

Test case 3: All closing: ")))", counter goes negative immediately. So output NO.

Test case 4: Balanced but with some points where the counter is zero. Like "()()". That's okay.

Another example: ")(", which would first decrement the counter to -1, so we return NO immediately.

So the algorithm should work.

Now, implement this in Python.

Read the input string. Then iterate through each character.

Initialize balance = 0.

For each char in the string:

    if char is '(', balance +=1
    else: balance -=1
    if balance <0: break and return NO.

After processing all chars, if balance is 0: YES else NO.

Yes. That's O(n) time and O(1) space, which is optimal.

Let me check the sample inputs.

Sample 1: "(()(()))()"

Processing:

Characters:

( ( ) ( ( ) ) ) ( )

Balances:

1, 2, 1, 2, 3, 2, 1, 0, 1, 0.

No negatives. At the end balance is 0. So YES.

Sample 2: "())()"

Processing:

( →1, ) →0, ) →-1. At this point, balance is -1. So return NO. So correct.

Another example, "(()))(" would have a balance of 1,2,1,0,-1 → returns NO.

So the algorithm works.

Now, implement this in Python.

Read the input string with input().strip().

But need to make sure to read the entire line correctly.

Then loop through each character.

Now code:

s = input().strip()

balance = 0

for c in s:
    if c == '(':
        balance +=1
    else:
        balance -=1
    if balance <0:
        print("NO")
        exit()
print("YES" if balance ==0 else "NO")

Wait, but in Python, using exit() would terminate the program immediately, which is allowed here. So as soon as balance is negative, output NO and exit. Otherwise, after processing all characters, check balance.

Yes, this should work.

Testing the code against the samples.

First sample:

Input: (()(())). Let's see:

After each step:

balance increments and decrements as before. At end, balance is 0. So output YES.

Second sample: "())()" → first ) takes balance to 0, second ) takes to -1 → print NO.

Another test case: "(()))((" → balance after third ) is 2-1=1? Wait, let's see:

Wait, let's track step by step.

Suppose s is "(()))((".

Processing:

1. '(' → balance 1
2. '(', balance 2
3. ')', balance 1
4. ')', balance 0
5. ')', balance -1 → break and print NO.

So code returns NO.

Yes.

Another test case: ")(" → first character ')', balance becomes -1 → output NO.

Yes.

So the code seems correct.

This should handle all cases efficiently. Time is O(n), which for n up to 100 is trivial, but even for larger n (though constraints here are small) it's optimal. Space is O(1). So this should be the correct solution.
</think>

```python
s = input().strip()
balance = 0
for c in s:
    balance += 1 if c == '(' else -1
    if balance < 0:
        print("NO")
        exit()
print("YES" if balance == 0 else "NO")
```