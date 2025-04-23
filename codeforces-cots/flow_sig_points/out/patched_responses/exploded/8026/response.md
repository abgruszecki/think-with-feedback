<think>
Okay, I need to solve this programming problem. Let's read the problem statement carefully.

So, the problem is about simulating the state of a dome's color based on a sequence of messages. The initial color is blue, and the state starts unlocked. The messages can be lock, unlock, or a color. The color changes only if the state is unlocked. Lock and unlock toggle the state, but only if they are in the opposite state. For example, if we get a lock when already locked, it's ignored.

The task is to determine the final color after processing all messages.

Hmm. The constraints are small, n up to 100, so any approach should be efficient enough. But since the problem is straightforward, the solution needs to model the state correctly.

Let me think about the variables I need. We need to track two things: the current color (starts as blue) and whether the system is locked (starts as unlocked). For each message in order:

- If the message is 'lock' or 'unlock', we toggle the lock state, but only if the current state is different. Like, 'lock' when unlocked changes to locked; if already locked, do nothing.
- If the message is a color (like red, orange, etc.), then we check if the current state is unlocked. If yes, we change the color to that color. If locked, ignore the message.

So the steps are:

1. Initialize current_color to 'blue' and locked to False (since it's unlocked initially).
2. Iterate over each message in order.
3. For each message:
   a. If it's 'lock', set locked to True if it's not already locked.
   b. If it's 'unlock', set locked to False if it's not already unlocked.
   c. If it's a color, check if locked is False. If so, update current_color to this color.
4. After processing all messages, output current_color.

Wait, but the messages are given as strings. So in code, for each message in the input lines:

Check what type of message it is. For colors, the message could be any of the color options.

So the code structure would be:

Read n.

Then read n lines, processing each one.

Initialize current_color as 'blue' and is_locked as False.

For each message in the list of messages:

   if message is 'lock':

       if not is_locked:

           is_locked = True

   elif message is 'unlock':

       if is_locked:

           is_locked = False

   else: # it's a color

       if not is_locked:

           current_color = message

So that's the plan. Now, how to implement this in Python.

Read n, then read n lines. The input lines can be read via input().strip() for each of n times.

Yes.

Now, edge cases to consider:

- All messages are locks and unlocks, and the color remains blue. Like the second example.

- Messages that are colors when locked: they are ignored.

What if after a lock, then unlock again? Then subsequent colors can be processed.

So the code is straightforward. Let's test with the first example.

Example 1:

7 messages:

red → since unlocked, color becomes red.

violet → unlocked → color becomes violet.

unlock → but current state is unlocked, so ignored.

red → unlocked → color red.

orange → unlocked → color orange.

lock → now lock (state becomes locked).

indigo → since locked, ignored. So final color is orange. Which matches the example.

Yes.

Another example: 

5 messages, all lock and unlock.

Start with blue, unlocked.

First message is lock: state becomes locked.

Second unlock: unlocked.

Third lock: locked.

Fourth unlock: unlocked.

Fifth unlock: already unlocked, ignored.

So final color is blue.

Yes, which matches the second example.

So the code should handle these cases correctly.

Now, in code:

Read n.

current_color = 'blue'

is_locked = False

n = int(input())

for _ in range(n):

    msg = input().strip()

    if msg == 'lock':

        if not is_locked:

            is_locked = True

    elif msg == 'unlock':

        if is_locked:

            is_locked = False

    else:  # color

        if not is_locked:

            current_color = msg

At the end, print(current_color).

That's the code. It seems simple. Let me check if there's any case I'm missing.

For example, after a lock, any color messages are ignored. Then an unlock allows colors again.

Yes.

Another test case: all messages are colors. Then the last color would be the answer, assuming it's the last one processed while unlocked.

Yes.

Another case: lock is sent multiple times. Only the first one takes effect.

Like:

lock → lock → lock → all after the first are ignored.

So the code works.

So I think this code will handle all cases correctly.
</think>

```python
n = int(input())
current_color = 'blue'
locked = False
for _ in range(n):
    msg = input().strip()
    if msg == 'lock':
        if not locked:
            locked = True
    elif msg == 'unlock':
        if locked:
            locked = False
    else:
        if not locked:
            current_color = msg
print(current_color)
```