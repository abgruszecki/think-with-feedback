<think>
Okay, let's try to figure out this problem. So, the problem is about a stack of red and blue balls, and we need to find the maximum number of operations we can perform. Let's understand the operations step by step.

The operation is as follows:
1. While the top ball is red, pop it. So, remove all consecutive red balls from the top.
2. Then, if there's a blue ball on top (since we removed all reds from top), replace it with a red.
3. Then, add blue balls until the stack has n balls again.

So each operation converts a blue into red and possibly adds some blues. But each time, the position where the blue is changed depends on the current stack.

The key is to model how each operation affects the stack and compute how many times this can be done until there are no blue balls left.

Hmm. Let's think about the example given. For instance, the first example is RBR. Let's process step by step.

First operation:
- Remove all top reds. The top is R, so pop. Now the stack is BR (since the original stack is top to bottom R, B, R? Wait wait, the input is given with the i-th character being the i-th ball from top to bottom. Wait, the problem statement says: "the i-th character of the string s denotes the color of the i-th ball (we'll number the balls from top to bottom of the stack)." Oh right, so the first character is the top ball, second is next, etc. So for input RBR, the stack is R (top), B, R (bottom).

Wait, but the first example's initial stack is RBR. So the initial stack is:

Top: R, then B, then R (bottom). Wait, but when you pop the top R, the stack becomes B, R. Then, step 2: replace the top (which is B) with R. Then, step 3: add blue balls until the stack has 3 again. So after step 3, the stack becomes R (from replacing B), then R (original R?), and add one blue. Wait, maybe not. Let's re-examine.

Wait, during the first step of the first operation:

Original stack: R (top), B, R (bottom). So step 1: while top is red, pop. So pop R, then check next top. Now the stack is B, R. The top is B, so step 1 stops. Then, step 2: replace the top (B) with R. So the stack now is R (from replacing B), and then R. Then step 3: add blue balls until the stack has n=3 balls. So add one blue. Now the stack is R (top), R, B (bottom). 

So after the first operation, the stack becomes R R B. Then, the second operation:

Step 1: the top is R. Pop all reds. So pop R, then next R, then check next top is B. So after popping, stack is B. Then step 2: replace B with R. Then step 3: add two blues to reach 3. So stack becomes R, B, B. 

Now, no blue balls left? Wait, no. After step 2, the stack has one R. Then adding two blues. So the stack is R (top), B, B (bottom). Now, there are two blue balls. So another operation could be possible. Wait, but according to the example, after two operations, the stack is all R? Or maybe after two operations, there's no blues left. Wait, the first example's output is 2. So after two operations, there's no blue left.

Wait, let's see the example explanation. After the second operation, the stack's top is R. So when they apply the next operation, there's no blue left. Wait, perhaps in the second operation, after step 2, there's no blue left. Let me re-examine the example explanation.

The first example's note says:

After the first operation, the stack is R R B. Then the second operation's explanation says: he will not pop any reds (since the top is R? Wait, no. Wait, the first step is to pop all reds from top. Wait, the initial stack before the second operation is R R B. So step 1: top is R, pop. Now stack is R B. Then step 1 again: top is R, pop. Now stack is B. Then step 2: replace B with R. Then add two blues to reach 3. So after this operation, the stack is R B B.

Wait, but then in that case, there are two blues. So why can't we perform another operation?

Hmm, maybe I'm misunderstanding the example. Let me read the note again.

In the first example, after the second operation:

The note says: "he simply changes the color of the ball on the top from blue to red." So perhaps after the first operation, the stack is R (from replacing B), and then adds one blue. So after first operation, stack is R (top), R, B (bottom). Then, the second operation:

Step 1: pop all reds. So top is R, pop. Then stack is R B. Top is R again, pop. Stack is B. Then step 2: replace B with R. Add two blues. So stack is R B B. Then, the next operation would have to process this stack. But then, the top is R, so step 1 pops it. Then stack is B B. Step 2: replace first B with R. Then add two blues. Now the stack is R B B again. Wait, this seems like it can go on indefinitely, but that's not possible. Wait, maybe I'm getting the example wrong.

Alternatively, perhaps the example's initial stack is R B R (top to bottom). So during the first operation:

Step 1: pop R. Stack becomes B R. Then step 2: replace B with R. Now stack is R R. Then step 3: add one blue to reach 3. So stack is R R B. Then second operation:

Step 1: pop R, then R. Stack becomes B. Step 2: replace B with R. Add two blues. Stack is R B B. Now, there are two blue balls. But in the next operation, the top is R. So step 1 pops R, stack becomes B B. Then step 2: replace top B with R. Stack becomes R B. Then add one blue. So stack is R B B. Then again, another operation. So this seems to have a loop. But according to the example, the maximum is 2. So perhaps the example's explanation is different.

Wait, maybe the example's note is different. Let me re-read the note for the first example:

In the first example:

After the first operation: stack is R R B.

Second operation: he doesn't pop any reds. Wait, why? Because in the second operation, when he starts, the stack is R R B. So the top is R. So step 1 is to pop all reds. So he pops both Rs, leaving B. Then step 2: replace B with R. Then add two blues. So stack is R B B. Then, next operation: top is R. So step 1 pops R. Now stack is B B. Step 2: replace first B with R. Then add two blues. Wait, n=3, so after adding, stack is R B B. So this seems like the same as before. But according to the note, after two operations, there's no blue balls. Hmm, perhaps I'm misunderstanding the process.

Wait, the problem says that the operation can only be applied if there is a blue ball in the stack. So after some operations, when all balls are red, you can't apply any more.

But according to the example's note, after two operations, there are no blue balls. Let's see:

After first operation: stack is R R B.

Second operation: step 1: pop both Rs. Stack is B. Then step 2: replace B with R. Now, stack is R. Then add two Bs. So stack is R B B.

Wait, but here there are two B's. So why does the example say that after the second operation, there are no blue balls? That's conflicting. Oh wait, perhaps the example's note is wrong, or perhaps I'm misunderstanding.

Alternatively, maybe the example's note is for a different initial stack. Let me check the first example again.

Input is:

3

RBR

So the stack is R (top), B, R (bottom). So step 1 of the first operation: pop all top R's. So the stack becomes B, R. Then step 2: replace B with R. So stack becomes R, R. Then step 3: add one blue to make total 3. So stack is R, R, B.

Second operation: step 1: pop all R's. So stack becomes B. Then step 2: replace with R. Add two B's. So stack is R, B, B.

Now, after two operations, there are two blue balls. So why can't we perform more operations?

Ah, wait maybe the problem requires that during the operation, after replacing the top blue with red, you add blue balls. So the presence of blue balls in the stack is determined by the current stack after replacement and before adding blues. Because adding blues is part of the same operation.

Wait, no. The operation is: after replacing the top blue with red, you add blue balls. So during the operation, after step 2, the stack has some number of balls (say m, which could be less than n). Then step 3 adds (n - m) blue balls. So the blue balls added are part of the same operation. So after the operation is completed, the stack has m + (n - m) = n balls. So in the first example, after the second operation:

After step 2, the stack is R (after replacing B). Then step 3 adds two B's. So the stack becomes R, B, B. So there are two B's. Then, the next operation is possible, but according to the example, it's not. What's wrong here?

Wait, the example's note says that after the second operation, there are no blue balls. That suggests that the stack after the second operation is all R's. So perhaps I'm misunderstanding the steps.

Alternatively, perhaps the stack is represented as the top being the first element. Let me re-examine the first example's note explanation.

In the first example's note:

First operation explanation:

- He pops one R. Stack is B R. Then changes B to R. Now stack has R R. Then adds one B. So stack is R R B.

Second operation explanation:

- He does not pop any Rs. Then changes the top B to R. Then adds two B's. Wait, why does he not pop any Rs?

Wait, according to the note, during the second operation, the stack is R R B. So step 1 is to pop all R's. So pop R, then next R, stack is B. Then step 2: replace B with R. Then add two B's. So stack becomes R B B. Then, in the next operation, the top is R, so step 1 removes it. Stack becomes B B. Step 2: replace top B with R. Then add two B's. Stack becomes R B B again. So this would loop, but the example says that after two operations, there are no B's. So there's a contradiction here.

This suggests that I have a misunderstanding of the process. Let me re-read the problem statement carefully.

Problem statement:

The operation steps are:

1. While the top ball is red, pop it. So all consecutive reds on top are removed.

2. Replace the blue ball (now on top) with a red.

3. Push blue balls until the stack has n balls again.

If there are no blue balls, can't apply.

So after step 1, if there is a blue ball, step 2 and 3 are done. Otherwise, the operation is invalid.

Wait, no. Step 2 requires that after step 1, the stack has a blue on top. Otherwise, you can't perform the operation. Because the problem says "if there are no blue balls inside the stack, ainta can't apply this operation."

Wait, no. The problem says: "if there are no blue balls inside the stack, can't apply." So the operation is possible only if, after step 1, the stack is not empty and the top is a blue ball. Otherwise, you can't perform the operation.

Wait, but step 1 is part of the operation. So during the operation:

After popping all the reds from the top (step 1), if the stack is empty (all balls were red and popped), then there's no blue ball to replace, so the operation can't be done. So the operation can only be applied if after step 1, there is at least one ball (the top being blue).

So in the first example's second operation:

After step 1, the stack becomes B (from R R B). Then step 2: replace B with R. Then step 3: add two blues. Now the stack is R B B.

In the next operation:

Step 1: pop the top R. Then stack becomes B B. The top is B, so step 1 stops. Then step 2: replace B with R. Add one blue (since n=3, current stack has R B after step 2. So add one blue to make total 3). So stack becomes R B B again.

Wait, but then each operation would replace a blue into red, but adding a blue each time. So the number of operations would be infinite? But that can't be. So there's a mistake here. Therefore, I must have misunderstood the process.

Alternatively, perhaps the operation's step 3 adds the blues regardless of their color. So after step 2, the stack has m balls (m can be 0?), and then step 3 adds (n - m) blue balls. So the added balls are all blue.

In that case, after each operation, the number of blue balls added is (n - m). But if m is 1 (like in the second step of the first example), then step 3 adds two blues. So in the example's second operation:

After step 1: stack is B (from R R B → pop Rs, so stack becomes B). Step 2: replace B with R. Now stack has 1 R. Step 3: add two blues. So stack is R (top), B, B (bottom). So the stack has two blues. Then in the next operation:

Step 1: top is R → pop. Stack becomes B B. Step 2: replace top B with R. Now stack is R B. Step 3: add one blue. So stack is R B B again. So each operation adds a blue. So the number of operations could be infinite, but the example says two. So this is conflicting.

This suggests that I must have a wrong understanding of the operation steps. Let me re-express the steps properly.

Let's break down the operation step by step.

Original stack: S (size n).

Operation:

1. Pop all consecutive R's from the top. Let's say after popping, the stack is S'. If S' is empty (all were R's), then there's no blue to replace, so the operation is invalid.

2. If S' is not empty, the top is B. Replace this B with R. Let's call this modified stack S''. The size of S'' is now (original S' size) - 1 + 1 = same as S' size (since replacing top).

3. Push (n - len(S'')) blue balls to make the total size n. So these added are all B's.

After the operation, the new stack is S'' followed by the added B's.

So for the first example:

Initial stack: R B R (n=3).

First operation:

Step 1: pop all R's from top. So S' becomes B R. Because initial stack is R (top), B, R (bottom). After popping R, stack becomes B, R.

Step 2: replace top B with R → S'' is R, R.

Step 3: add (3 - 2) = 1 B. So new stack is R, R, B.

Second operation:

Step 1: pop all R's. Stack becomes B.

Step 2: replace B with R. Stack becomes [R].

Step 3: add 2 B's. New stack: R, B, B.

Third operation:

Step 1: pop R. Stack becomes B, B.

Step 2: replace top B with R. Stack becomes R, B.

Step 3: add 1 B. Stack becomes R, B, B. So this is same as after second operation. So this loop would continue indefinitely, but the example says output is 2.

This suggests that after two operations, the stack has no blue balls. But in the scenario I described, after two operations, there are two B's. So why is the example output 2?

Ah! Maybe I'm miscalculating the number of blue balls after each operation. Wait, the problem requires that the operation can only be applied if there's at least one blue ball in the stack. So after each operation, the stack must have at least one blue ball. Wait, no. The problem says that if there are no blue balls, you can't apply the operation. So during each operation, after step 1, there must be at least one blue ball (i.e., the top is B). Otherwise, the operation can't be done.

Wait, during the operation, step 1 removes all R's. Then, if the stack is empty, or the top is not B (but that's impossible because step 1 removes all R's and stack is not empty because there must be a B to proceed), then the operation can't be done.

So the operation can only be applied if, after step 1, the stack has at least one B. So after step 3, the stack has some B's (the added ones). So the number of operations is the number of times you can find a B in the stack after step 1.

But the example's output is 2. So how does that happen?

Alternatively, perhaps the example's note is not accurate. Let me check the note again.

In the first example's note, after the second operation, the stack is R (from replacing B) and then adds two B's. So the stack is R B B. Then, the problem says that there are no blue balls left. That's not possible. So perhaps the note's explanation is wrong, or perhaps I'm misunderstanding the process.

Alternatively, maybe after step 2, the stack may have a B.

Wait, no. Step 2 replaces the top B with R. So after step 2, the top is R. Then step 3 adds B's. So the stack after step 3 will have R followed by some B's. So during the next operation, step 1 would pop the top R, and then the new top is B.

So each operation requires that the stack after step 1 has at least one B. So in the first example, after two operations, the stack is R B B. Then, in the next operation:

Step 1: pop R → stack is B B. Then step 2: replace top B with R. Now stack is R B. Step 3: add one B. So stack is R B B. So this process can be done again. But the example's output is 2. So why is that?

This suggests that the example's explanation is incorrect, or perhaps the problem has a different approach.

Alternatively, perhaps the maximum number of operations is determined by the positions of the B's in the initial stack, and each B in the i-th position contributes 2^(i-1) operations. So for example, if the stack is B R R R, then the B in the first position (top) contributes 1 operation. If the B is in the second position (after popping the top R's), then each occurrence contributes 2^(i-1) operations.

This is similar to a binary approach. Let's look at the examples.

First example: RBR → positions 0 (top) is R, position 1 is B, position 2 is R.

In the first operation, the B is in position 1 (after popping the top R). So this would contribute 2^0 = 1 operation. Then, after the operation, the stack becomes R R B. The B is now in position 2. So in the next operation, it contributes 2^1 = 2 operations. But according to the example, the total is 2. Hmm, perhaps the sum of 2^(k-1) for each B at position k (from top to bottom, after popping the top R's) is the total operations.

Wait, maybe each B in the i-th layer (with i being the depth in the stack after popping top R's) contributes 2^{i-1} operations. Let's test this.

Second example input is 4, RBBR. The stack is R (top), B, B, R.

Let's see:

In the first operation:

Step 1: pop R. Stack becomes B B R.

Step 2: replace top B with R. Stack becomes R B R. Add 1 B (since stack size is 3, add 1 to make 4). New stack is R B R B.

Wait, but perhaps I'm miscalculating. Let's see the example's output is 6. How does that happen?

Alternatively, perhaps the number of operations is the sum of 2^{position} - 1 for each B in the initial stack.

For example, in the first example, the B is at position 1 (after popping the first R). So 2^1 -1 =1. Then, after the first operation, the B is at position 2. So 2^2 -1 =3. But total is 2. So this doesn't fit.

Alternatively, perhaps each B contributes a certain amount based on its position. Let's think of the stack as a list where each B's position determines the number of operations.

Another approach: model each operation as a transformation of the stack. The key is that each B in the stack contributes to the total operations. For example, a B at position i (after popping the leading R's) contributes 2^{i} to the total. But I'm not sure.

Alternatively, think of the problem as a binary number. Each B in the stack represents a bit. The number of operations is the sum of 2^{k} for each B at position k (starting from 0). For example:

In the first example:

Initial stack after popping R's: B R. The B is at position 0. So contributes 1. Then after first operation, the stack becomes R R B. Then, when processing this, step 1 pops R's, leaving B (position 0). So contributes 1 again. Total 2.

In the second example:

After popping the initial R, the stack is B B R. The top B is at position 0, the next B at position 1. So contributes 1 + 2 =3. Then after first operation, the stack becomes R B R and add B (step 3). So new stack is R B R B. Then, next operation step 1 pops R, stack becomes B R B. Top B is position 0, contributes 1. Then after replacing, stack becomes R R B. Next operation, after popping R's, B at position 0. Contributes 1. Then after replacing, stack becomes R B. Add two B's. Now, stack is R B B B. Next operation: step 1 pops R, stack becomes B B B. Contributes 1 (position 0). So sum up all these contributions.

But this is getting complicated. Perhaps the correct approach is to model each B as a binary digit, and the total number of operations is the sum of 2^{i} for each B in position i (0-based from the top after popping all leading R's).

In the first example, the initial B is in position 1 (since after popping the first R, the B is at position 0). Then after the first operation, the B is in position 2 (since after popping the two R's, B is at position 0 again).

Wait, maybe each time we process a B in position k, it contributes 2^{k} operations. For example:

In the first example's initial stack: R B R. After popping R, the B is in position 0. So contributes 1. Then, after replacing with R and adding B, the new stack is R R B. So when processing this, after popping R's, B is in position 0 again. Contributes 1. Total 2.

In the second example, the initial stack is R B B R. After popping R, the stack becomes B B R. The B's are in positions 0 and 1. So contributes 1 + 2 = 3. Then after the first operation, the stack becomes R B R B. Then step 1 pops R, stack becomes B R B. B is in position 0. contributes 1. Then stack becomes R R B B. Step 1 pops R's, stack becomes B B. contributes 1 + 2 =3. But this is for one operation, but the sum might be adding up.

But I'm not sure. Let's think of the sample inputs.

Sample 2:

Input:

4

RBBR → stack is R (top), B, B, R.

After step 1 of first operation: pop R → stack is B, B, R.

Then step 2: replace top B with R. Now stack is R, B, R. Step 3: add one B (since n=4, current size is 3). So new stack is R B R B.

Second operation:

Step 1: pop R. stack becomes B R B.

Step 2: replace B with R. stack becomes R R B. step 3: add one B. new stack R R B B.

Third operation:

Step 1: pop R R. stack becomes B B.

Step 2: replace top B with R. stack becomes R B. step 3: add two B's. new stack R B B B.

Fourth operation:

Step 1: pop R. stack becomes B B B.

Step 2: replace top B with R. stack becomes R B B. step 3: add one B. new stack R B B B.

Fifth operation: same as fourth, perhaps? No, because after fourth operation, the stack is R B B B. Then step 1: pop R → stack B B B. replace top B with R. add three B's. new stack R B B B again. So each step after the fourth would contribute 1 operation. But according to the sample, the output is 6. So how?

Alternatively, perhaps the initial approach is to model each B's position as a binary digit. For example, each B at position i (after popping R's) contributes 2^i to the total operations. Then, the total sum is the answer.

For example, the first example:

The initial stack after popping R's is B R. So B is at position 0. Contribution is 1.

After first operation, the stack becomes R R B. When processing this, after popping R's (R R), stack is B. So B is at position 0. Contribution 1. Total 2.

Second example:

Initial stack after popping R's: B B R. B's are at positions 0 and 1. Contribution 1+2=3. Then after first operation, the stack becomes R B R B. When processing this, after popping R, stack becomes B R B. B at position 0. Contribution 1. Then after this operation, stack becomes R R B B. After popping R's, stack is B B. B's at positions 0 and 1. Contribution 1+2=3. Total sum is 3+1+3=7? But sample output is 6.

Hmm, not matching. So this approach may not be correct.

Alternatively, maybe each B contributes a certain value based on its position, but when processed, it's replaced and the new B's added are lower in the stack and thus contribute less. This seems to suggest that the optimal approach is to process the B's from bottom to top, with each B contributing 2^{k}, where k is the number of B's below it.

Alternatively, perhaps the maximum number of operations is the sum for each B in the initial stack of 2^{d}, where d is the depth of the B in the stack (from the top, after popping all R's above it).

This is similar to the way binary numbers work. For example, each B at a certain depth adds a value that is a power of two. Let's test this.

First example:

Initial stack is R B R. After popping R's, the first B is at depth 0 (since after popping the first R, the next is B). So contributes 1. Then after processing, the stack becomes R R B. When processing this, after popping R's, the B is at depth 0 again. So contributes another 1. Total 2. Which matches the first example.

Second example:

Initial stack is R B B R. After popping R, the stack is B B R. The B's are at depths 0 and 1. So contribute 1 + 2 =3. After processing, the stack becomes R B R B. When processing this, after popping R, the stack is B R B. B at depth 0. Contributes 1. Then stack becomes R R B B. After popping R's, B B. Depths 0 and 1. Contribute 1+2=3. Then after processing, stack becomes R B B B. Processing this: after popping R, B's at depths 0,1,2. So contribute 1+2+4=7? But sample output is 6. So this doesn't fit.

But sample output is 6. So perhaps this approach is wrong.

Alternatively, perhaps the B's in the initial stack contribute 2^{i} where i is their position (from 1-based index) after the first R's are popped.

Wait, perhaps each B in the stack contributes a value equal to 2^{k}, where k is the number of B's below it (including itself) when considering the initial stack after popping the leading R's.

Alternatively, perhaps the answer is the sum of 2^{i} for each B, where i is the position of the B in the stack (0-based from the top) after the leading R's are popped.

In the first example, the B is at position 0 (after popping leading R), so contributes 1. Then, after the first operation, the B is added at position 2. When processing that, after popping leading R's (two R's), the B is at position 0 again, contributes another 1. Total 2.

Second example's initial B's are at positions 0 and 1 (after popping leading R). So 1 + 2 =3. Then, after processing, the stack becomes R B R B. Next, when processing that stack, after popping R, the B is at position 0. So contributes 1. Then stack becomes R R B B. Popping R's, the B's are at positions 0 and 1. Contribute 3. Then after processing, stack becomes R B B B. Popping R, B's are at 0,1,2. Contribute 7? But sample output is 6.

Hmm. So this approach doesn't fit.

Alternative idea: the maximum number of operations is the sum for each B in the stack of 2^{d} - 1, where d is the depth of the B in the stack (after popping R's). For example, the first example's B is at depth 0: 2^0 -1 =0. Not sure.

Alternatively, perhaps the problem can be modeled as a binary number where each B in the stack represents a digit. For example, each B in position i (after popping R's) represents 2^i, and the sum of all such values gives the total number of operations.

In the first example, this sum is 1 (from first B) + 1 (second B) =2, which matches. In the second example, initial sum is 1+2=3. Then after first operation, the sum becomes 1 (from new B) and then another 3. So 3+1+3=7? But sample output is 6.

This suggests that perhaps the correct approach is to model the stack as a binary number where each B contributes 2^{i} for the position i (after popping R's). And each operation converts a B to R and adds B's to the end. So the total operations are the sum of all 2^{i} for each B in the initial stack.

But how?

Let's take the first example:

Initial stack after popping R's is B R. The B is at position 0. So 2^0 =1.

Then, after the operation, the new stack is R R B. After popping R's, the B is at position 0 again. So 2^0=1. Total 2.

Second example:

Initial stack after popping R's: B B R. So positions 0 and 1. Sum is 1+2=3. Then after first operation, new stack is R B R B. After popping R's, B R B. B at position 0. Sum is 1. Then after operation, stack is R R B B. After popping R's, B B. sum 1+2=3. Then after operation, stack is R B B B. After popping R, B B B. sum 1+2+4=7. Total sum is 3+1+3+7=14, which is way over the sample output.

Hmm. Clearly, this approach is not working.

Alternative idea: the number of operations is equal to the sum for each B in the stack (in the initial state) of 2^{k} -1, where k is the number of B's to the right of and including that B.

For example, in the first example:

The initial stack is R B R. So the B is the second character. The B has one R to its right. So k=1 (number of B's to the right including itself? No, maybe not. Or maybe the number of B's in the stack after popping all R's and including this B. Not sure.

Alternatively, each B in the stack contributes 2^{x} -1, where x is the number of B's in the stack after popping the leading R's. For example, initial stack in first example: after popping R's, the B is the first. So x=1. So contribution 1. Then after first operation, the B is added, x=1 again. So another 1. Total 2.

In the second example: initial x=2 (B B R), contribution 3. Then after first operation, x=1 (B R B), contribution 1. Then after that operation, x=2 (B B), contribution 3. Then after that operation, x=3 (B B B), contribution 7. But sample output is 6, so this also doesn't fit.

This suggests that perhaps the correct approach is to model the stack as a list of B's, and each B contributes 2^{i} where i is the position in the list.

But how?

Alternatively, think of each B as contributing a certain number of operations based on its position. For example, a B at position i (after popping the leading R's) contributes 2^i operations. The total is the sum of all such contributions.

In the first example, the sum is 1 + 1 = 2. Correct.

In the second example:

Initial stack after popping R's has two B's. Sum is 1+2=3.

After first operation: new stack's B is at position 0 (after popping R's). Sum +=1.

Then after that operation, the B's are at positions 0 and 1. Sum +=3.

Total sum 3+1+3=7, but sample output is 6.

So this approach is not correct.

Hmm. This is getting really stuck. Let's think of the problem differently.

Each time a B is converted into R, it contributes to the total operations. The B's in lower positions (deeper in the stack) contribute more operations. Because converting a B requires that all B's above it have already been converted.

For example, consider a stack like B R R R. The first B is on top. Converting it requires 1 operation. Then after that, the stack is R R R R. No more B's. So total 1.

If the stack is B B R R. First, the top B is converted, contributing 1. Then the stack becomes R B R R. Then, when processing, pop the R, then convert the B, contributing 1 again. Then stack becomes R R R R. Total 2.

But according to the formula of summing 2^i, the sum would be 1+2=3. Which is not the case.

So this approach is also incorrect.

Alternative idea: The number of operations is equal to the sum of 2^{k} - 1 for each B, where k is the position of the B in the stack when viewed from the bottom.

For example, in the first example, the B is at position 1 (from the bottom). So 2^(1) -1 =1. But the total is 2. Not matching.

Alternatively, perhaps each B in the stack contributes a certain number of operations based on the number of B's below it.

But this is unclear.

Alternatively, think recursively. Each time a B is processed, it generates new B's in lower positions. For example, when you process a B at position i, you replace it with R and add B's below. Each of these new B's will generate their own operations.

But how?

Let's model the stack as follows. When we process a B at position i (the i-th position from the top, after popping the R's), the operation replaces it with R, and adds m B's at the end (step 3). The number of operations contributed by this B is 1 plus the operations contributed by the new B's added.

But since the new B's are added in the positions below, their contributions would be based on their positions.

Wait, perhaps each B in position i contributes 2^i operations. Because when you process it, you have to process all the B's added below it.

For example:

Processing a B in position 0 (top after popping R's) gives 1 operation (itself). Then, after replacing it with R, you add B's in positions >=1. Each of those B's would contribute 2^{position} operations. But this is getting complicated.

Alternatively, think of each B in the stack as representing a bit in a binary number. Each B in position i (after popping R's) adds 2^i to the total. For example:

Initial stack R B R. After popping R's, B is at position 0. So adds 1.

After converting to R, the new B's added are at positions 0 (since the stack after step 2 is R R. Then adding 1 B. So the new stack is R R B. When processing this, after popping R's, the B is at position 0 again. So adds another 1. Total 2.

In the second example:

Initial stack R B B R. After popping R's, B's are at positions 0 and 1. Sum is 1 + 2 =3.

Then converting the first B (position 0) to R. Add 1 B. Stack becomes R B R B. Processing this stack: after popping R's, B is at position 0. Sum +=1. Then converting this B, add 1 B. Stack becomes R R B B. Processing: after popping R's, B's are at positions 0 and 1. Sum +=3. Then converting the first B (0), sum +=1. Then stack becomes R B B B. Processing: after popping R, B's are 0,1,2. Sum +=1+2+4=7. But sample output is 6. So this approach gives 3+1+3+7=14, which is way over.

This suggests that this model is incorrect.

Alternative approach: Let's model the process for the second example:

Sample 2 input: RBBR → stack is R B B R.

First operation:

Step 1: pop R. Stack becomes B B R.

Step 2: replace first B with R. Stack becomes R B R.

Step 3: add 1 B. Stack becomes R B R B.

Second operation:

Step 1: pop R. Stack becomes B R B.

Step 2: replace B with R. Stack becomes R R B.

Step 3: add 1 B. Stack becomes R R B B.

Third operation:

Step 1: pop R R. Stack becomes B B.

Step 2: replace B with R. Stack becomes R B.

Step 3: add 2 B's. Stack becomes R B B B.

Fourth operation:

Step 1: pop R. Stack becomes B B B.

Step 2: replace B with R. Stack becomes R B B.

Step 3: add 1 B. Stack becomes R B B B.

Fifth operation:

Step 1: pop R. Stack becomes B B B.

Step 2: replace B with R. Stack becomes R B B.

Step 3: add 1 B. Stack becomes R B B B.

Sixth operation: same as fourth and fifth.

Wait, but sample output is 6. So what's happening here?

The operations are:

1. RBBR → first operation.

2. After first → R B R B.

3. After second → R R B B.

4. Third → R B B B.

5. Fourth → R B B B (after replacing top B). Then, fifth operation: step 1 pop R → B B B. Replace top B → R B B. Add one B → R B B B. Sixth operation: pop R → B B B. Replace → R B B. Add one B. Now, after six operations, we have R B B B. But the stack has B's, so operations can continue. So why the sample output is 6?

This suggests that perhaps I'm missing something. Let me check the sample explanation for the second example.

The second sample's note says the output is 6. So perhaps there's a certain way the operations are counted.

Perhaps the correct model is to think of each B in the stack as contributing a certain number of operations, and the total is the sum of 2^{i} for each B in the stack after popping the leading R's, but subtracting 1. Because each B's contribution is 2^{i} -1.

In the first example:

After popping R's, B is at position 0 → 2^0 -1 =0. But sum is 0. Not matching.

Hmm.

Alternatively, perhaps each B contributes 2^{k} where k is the number of B's to the right of it (including itself) in the initial stack.

For example, in the first example, the B is the only B. So 2^1 -1=1. Then after processing, the B is added again. So 2^1 -1=1. Total 2.

Sample output is correct.

Second example: initial stack R B B R. The B's are in positions 1 and 2 (original stack). So each B has 2 B's to the right. For the first B, the B's to the right are 2 (including itself). So 2^2-1=3. For the second B, there's one B to the right (itself). 2^1-1=1. So sum 3+1=4. But sample output is 6. So this approach is wrong.

Alternatively, perhaps each B contributes 2^{i} -1, where i is the number of B's in the stack after popping the leading R's.

For example, first example: after popping R's, one B. So 1 contribution. Then after operation, one B again. So 1+1=2.

Second example: initial 2 B's → 2^2 -1=3. Then after first operation, 1 B →1. Then after second operation, 2 B's →3. 3+1+3=7. Sample output is 6.

Hmm.

At this point, it's clear that the initial approach is not leading to the correct solution. Perhaps the correct way is to model the problem as a binary number, where each B in the stack contributes a certain value, and the total operations is the sum of these values.

After some research, I recall that this problem is similar to the problem of incrementing a binary number, where each operation corresponds to adding 1. The number of operations is the value of the binary number formed by the B's (with R as 0 and B as 1), but reversed. For example, if the stack is B B R R, the binary number is 1100 (assuming top to bottom is left to right), but reversed, it's 0011 → 3. So the number of operations is 3.

Wait, let's test this hypothesis.

First example:

Initial stack is R B R → the B's are at position 1 (top is 0). So the binary number is 0 1 0 → reversed (since top is first) → 010, which is 2. But the sample output is 2. So this fits.

Second example: initial stack is R B B R → binary is 0 1 1 0 → reversed is 0110 → 6. Sample output is 6. This matches.

Third example: input is RBBRR → stack is R B B R R. So binary is 0 1 1 0 0 → reversed is 00110 → which is 6. Sample output is 6. Which matches.

So this seems to fit all the examples.

So the approach is to treat the stack as a binary number where each B represents a 1 and each R represents 0, then reverse the order, and convert to a decimal number. That decimal number is the maximum number of operations.

Yes! This seems to be the correct approach.

So for example:

First sample input: R B R → binary digits [R, B, R] → [0, 1, 0]. Reverse to [0, 1, 0] → 010 in binary is 2. Which matches the sample output.

Second sample input: R B B R → digits [0, 1, 1, 0]. Reverse → 0110 → binary 6.

Third sample input: R B B R R → digits [0, 1, 1, 0, 0]. Reverse → 00110 → 6.

So the solution is to reverse the string, interpret it as a binary number (B=1, R=0), and output its value.

Wow, that's a clever insight. So the problem reduces to converting the initial stack into a binary number where B is 1 and R is 0, reverse the string, and compute its value.

Thus, the code can be written as follows:

Read the string s, reverse it, then for each character, compute the binary value where B is 1 and R is 0. Sum the values of 2^i for each i where the reversed string's i-th character is 'B'.

For example:

Sample 1: reversed s is R B R → but wait, original s is R B R. So reversed is R B R → wait, no. Wait, the string is written from top to bottom. So when you reverse it, you get the order from bottom to top.

Wait, the original string s represents the stack from top to bottom. So the first character is the top, second is next, etc.

To treat it as a binary number where the top is the least significant bit (since when you process the stack, the top B contributes 1, the next B contributes 2, etc.), we need to reverse the string. Because in binary numbers, the rightmost digit is least significant.

For example, the first sample's s is R B R. The reversed string is R B R reversed → R B R becomes R B R (since it's length 3). Wait, no. Wait, for example, the original string is "RBR" (indexes 0,1,2). Reversed is "RBR" reversed → "RBR" → indexes 2,1,0. So the reversed string is "R B R" → reversed to R B R. Wait, no. Wait, "RBR" reversed is "RBR" → same as original? No, wait, "RBR" is the original. Reversed would be "RBR" → no. Wait, "RBR" is a 3-character string. Reversing it would be "RBR" → the same. Because the first character is R, second B, third R. Reversed, it's R, B, R → same as original. So reversing it would not change it. Then treating each 'B' as 1 and others as 0, we get 0 1 0. Which is 2 in binary. So the sample's output is 2. Which matches.

So the code would be:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    reversed_s = s[::-1]

    total = 0

    for i in range(len(reversed_s)):

        if reversed_s[i] == 'B':

            total += 2**i

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
RBBRR
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
Traceback (most recent call last):
  File "/workdir/snippet.py", line 50, in <module>
    test()
    ~~~~^^
  File "/workdir/snippet.py", line 43, in test
    assert real_output == expected_output, \
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Test case 0 failed.
Expected: '6'
Got: '0'

```

So for the second sample input, reversed_s is 'RBBR'. Then, we check each character:

i=0: 'R' → 0.

i=1: 'B' → 2^1=2.

i=2: 'B' → 2^2=4.

i=3: 'R' → 0.

Sum is 2+4=6. Which matches the sample output.

Third sample input is 'RBBRR' → reversed is 'R R B B R' → no, original string is 'RBBRR' (R, B, B, R, R). Reversed is 'R R B B R' → reversed_s is 'RRBBR'. 

Processing each character:

i=0: 'R' → 0.

i=1: 'R' → 0.

i=2: 'B' → 4.

i=3: 'B' → 8.

i=4: 'R' → 0.

Sum is 4+8=12 → but sample output is 6. Wait, but sample output is 6. Wait, this contradicts.

Wait, third sample input:

Input is 5

RBBRR → the string is 'RBBRR'.

Reversed string is 'RRBBR' → 'R R B B R'.

Now, for each character in reversed_s:

i=0: 'R' → 0.

i=1: 'R' → 0.

i=2: 'B' → 2^2 =4.

i=3: 'B' → 2^3=8.

i=4: 'R' → 0.

Sum is 4+8=12. But the sample output is 6. So this approach is incorrect.

Wait, this is a problem. The third sample's expected output is 6, but according to this approach, it's 12. So why the discrepancy?

Ah, here's the mistake. The reversed string should be 'RRBBR' → but when we treat this as a binary number, the digits are:

RRBBR → each character in reversed_s is 'R', 'R', 'B', 'B', 'R'.

So reversed_s is 'RRBBR', which in binary (B=1, R=0) is 0 0 1 1 0 → which is 6 in decimal (since 0*16 + 0*8 + 1*4 + 1*2 + 0*1 = 4+2=6). So the sum would be 2^2 + 2^3 =4+8=12. But this contradicts the sample output.

Wait, this suggests that the approach is incorrect. But why?

Wait, let's look at the third sample's input. The initial stack is R B B R R (top to bottom). So after popping all R's from the top, the stack is B B R R. So the B's are at positions 0 and 1. According to the previous approach, the sum should be 2^0 + 2^1 = 1+2=3. But the sample output is 6.

So what's wrong here?

Ah! I think I made a mistake in the model. The correct way is to reverse the string and then, for each character, if it's B, add 2^i, where i is the index in the reversed string.

But wait, the third sample's reversed string is 'RRBBR', which is 'R', 'R', 'B', 'B', 'R'.

So indices 0: R → 0.

1: R → 0.

2: B → 4 (2^2=4).

3: B → 8 (2^3=8).

4: R → 0.

Sum is 4+8=12. But the sample output is 6.

This is a contradiction, so the model must be wrong.

But the sample's expected output is 6. So what's the correct model?

Alternative idea: perhaps the reversed string is not the correct way. Perhaps the string is processed from bottom to top, and each B contributes 2^ (position from bottom).

For example, third sample's initial stack is R B B R R (top to bottom). The bottom is R. So the positions from bottom are:

Position 0: R (bottom).

Position 1: R.

Position 2: B.

Position 3: B.

Position 4: R (top).

But this may not be the right way.

Alternatively, perhaps the correct approach is to process the stack as follows:

For each B in the stack, its contribution is 2^{number of B's to its right}.

Wait, let's see:

In the third sample's initial stack: R B B R R.

The B's are at positions 1 and 2 (0-based from the top).

The number of B's to their right (including themselves):

For position 1: B at 1 and 2 → 2 B's to the right (including itself). So 2^2-1=3.

For position 2: one B (itself). 2^1-1=1.

Sum 3+1=4. But sample output is 6.

No.

Alternatively, the contribution is 2^{number of B's to the left} including itself.

But this also doesn't fit.

At this point, it's clear that the initial approach works for the first two samples but not the third. So there must be a mistake in the model.

Let's re-examine the third sample.

Third sample input: 5 RBBRR → stack is R B B R R (top to bottom).

Let's compute the number of operations:

First operation:

Step 1: pop R. Stack becomes B B R R.

Step 2: replace top B with R. Stack becomes R B R R.

Step 3: add 1 B (since n=5, current size is 4 → add 1). Stack becomes R B R R B.

Second operation:

Step 1: pop R. Stack becomes B R R B.

Step 2: replace B with R. Stack becomes R R R B.

Step 3: add 1 B. Stack becomes R R R B B.

Third operation:

Step 1: pop R R R. Stack becomes B B.

Step 2: replace top B with R. Stack becomes R B.

Step 3: add 3 B's. Stack becomes R B B B B.

Fourth operation:

Step 1: pop R. Stack becomes B B B B.

Step 2: replace top B with R. Stack becomes R B B B.

Step 3: add 1 B. Stack becomes R B B B B.

Fifth operation:

Step 1: pop R. Stack becomes B B B B.

Step 2: replace top B with R. Stack becomes R B B B.

Step 3: add 1 B. Stack becomes R B B B B.

Sixth operation: same as fourth and fifth.

So after six operations, the stack is R B B B B. Then, each operation would process the top B, replace it with R, and add B's. This would contribute one operation each time, leading to infinite operations. But the sample output is 6.

So why is the sample output 6?

The sample output is 6, which suggests that after six operations, there are no more B's. But according to this scenario, after six operations, there are B's. So what's the correct way to model this?

Ah! Perhaps there's a mistake in the way I'm counting the operations.

Let's re-calculate step by step for the third sample.

Third sample input:

n=5, initial stack R B B R R (top to bottom).

Operation 1:

Step 1: pop R. Stack becomes B B R R.

Step 2: replace top B with R → R B R R.

Step 3: add 1 B → stack becomes R B R R B. (size 5).

Operation 2:

Step 1: pop R. Stack becomes B R R B.

Step 2: replace B with R → R R R B.

Step 3: add 1 B → R R R B B.

Operation 3:

Step 1: pop R R R → stack becomes B B.

Step 2: replace top B with R → R B.

Step 3: add 3 B's → R B B B B.

Operation 4:

Step 1: pop R → stack becomes B B B B.

Step 2: replace top B with R → R B B B.

Step 3: add 1 B → R B B B B.

Operation 5:

Step 1: pop R → stack becomes B B B B.

Step 2: replace top B with R → R B B B.

Step 3: add 1 B → R B B B B.

Operation 6:

Step 1: pop R → stack becomes B B B B.

Step 2: replace top B with R → R B B B.

Step 3: add 1 B → R B B B B.

After six operations, the stack is R B B B B. So there are B's left, but the sample output is 6. So according to this, the sample's output is 6. But why?

Ah! Because after six operations, the stack is R B B B B, which has four B's. So operations can continue. But the sample output is 6. So this suggests that the initial approach is wrong.

But according to the initial approach (reversed string as binary), the third sample's reversed string is 'RRBBR' → which is R R B B R → B's at positions 2 and 3 (0-based). So 2^2 + 2^3 =4+8=12, which is not matching the sample output of 6. So there's a problem.

This suggests that the initial approach is incorrect, and there's a different way to model the problem.

Wait, let's re-examine the third sample's expected output. The sample output is 6. How is that possible?

Perhaps the correct approach is to model the problem as follows: the maximum number of operations is the sum of 2^{i} for each B in the stack, where i is the number of R's below the B.

For example:

Third sample's initial stack is R B B R R. The B's are at positions 1 and 2 (0-based from top to bottom).

For B at position 1: the number of R's below it (i.e., in the stack below it, including itself?) Not sure.

Alternatively, the number of R's above the B.

For example, a B at position k in the stack (0-based from top to bottom) has to wait until all R's above it are popped. Each time a B is processed, it may add more B's below it.

This is getting complicated.

Alternative idea: the maximum number of operations is the sum of 2^{d} for each B in the initial stack, where d is the number of B's to the left of the current B (including itself) in the stack.

But this is not clear.

Alternatively, the number of operations is the sum of the positions of B's in the initial stack, where each position is counted from the top, but each B's contribution is 2^{position}.

Wait, let's re-calculate the third sample.

Initial stack: R B B R R → B's are at positions 1 and 2 (0-based from top).

Sum is 2^1 + 2^2 = 2 +4=6. Which matches the sample output.

Ah! This seems to be the correct approach. So the contribution of each B is 2^i, where i is its 0-based position from the top of the stack (after popping the R's above it).

Wait, but how to determine the positions after popping R's.

In the initial stack of the third sample:

After popping R's, the stack is B B R R. So B's are at positions 0 and 1.

So their contributions are 2^0 + 2^1 =1+2=3.

But sample output is 6. So this doesn't fit.

Hmm.

Alternatively, perhaps the B's in the initial stack contribute based on their positions in the initial stack, not after popping R's.

For example, third sample's B's are at positions 1 and 2 (original stack). So 2^1 + 2^2 =2+4=6. Which matches the sample output.

This seems to fit all samples.

First sample's B is at position 1 (original stack) → 2^1=2.

Which matches sample output 2.

Second sample's B's are at positions 1 and 2 → 2+4=6. Which matches the sample output.

Third sample's B's are at positions 1 and 2 → 2+4=6. Which matches the sample output.

So this model fits all examples. So the solution is to compute the sum of 2^i for each B in the initial string, where i is the 0-based index of the B in the original stack (from top to bottom).

Yes, this seems to be the correct approach.

But why? Let's see why this works.

Each B in position i contributes 2^i operations. For example:

In the first sample, the B is at position 1 → 2^1=2.

In the second sample, B's are at positions 1 and 2 → 2^1 + 2^2 = 2+4=6.

Third sample: B's at positions 1 and 2 → 2+4=6.

So this model fits all samples.

But how does this model align with the process of operations?

Let's take the third sample. The B's are at positions 1 and 2. Each contributes 2 and 4, totaling 6.

But how does each operation correspond to this?

Well, each B in position i contributes 2^i operations. For example, a B in position 1 (0-based) contributes 2 operations, and one in position 2 contributes 4.

But why?

It seems that the model is to treat each B as a bit in a binary number, where the position is the bit's weight. The total number of operations is the sum of the bits (B's) multiplied by their corresponding weights (2^position).

This makes sense because when you process a B in position i, it requires 2^i operations to process all the B's that are added as a result.

But how to see this?

Perhaps each B in position i is processed once, but each time you process it, you generate B's in lower positions, which require additional operations. This leads to a sum that is 2^i for each B.

But this requires more detailed analysis.

Regardless, this model works for all given samples and is efficient to compute.

Thus, the correct approach is to iterate over each character in the string s, and for each 'B', add 2^i to the total, where i is the 0-based index of the character.

So the code is:

n = int(input())
s = input().strip()
ans = 0
for i in range(n):
    if s[i] == 'B':
        ans += 2 ** i
print(ans)

Wait, no. Because in the first sample, the B is at index 1 (0-based), so 2^1=2. Which matches the sample output. Second sample's B's are at indices 1 and 2 → 2+4=6. Third sample's B's are at indices 1 and 2 → 2+4=6. All correct.

But wait, the third sample's input is RBBRR → 'R', 'B', 'B', 'R', 'R' → B's are at indices 1 and 2 → 2^1=2, 2^2=4 → sum 6. Which matches the sample output.

Yes, this approach works.

But how does this align with the process?

For example, the first sample's B is at index 1. Each time it is processed, it contributes 1 operation. But according to this model, it's 2.

But the sample's output is 2.

Wait, no. The model says that the sum is 2^1 = 2, which matches the sample. So this works.

Thus, the correct code is to iterate over each character in the string, and for each 'B', add 2^i to the total, where i is the 0-based index of the character.

This is very efficient and straightforward. It handles all the test cases correctly.

So the code is:

n = int(input())
s = input().strip()
result = 0
for i in range(n):
    if s[i] == 'B':
        result += (1 << i)
print(result)

This code is O(n) time and O(1) space, which is optimal given the constraints.

Now, let's test this code with the third sample:

Input:

5

RBBRR

s is 'RBBRR'. The B's are at indices 1 and 2.

result = 2^1 + 2^2 = 2 +4=6. Which matches the sample output.

Yes. This is the correct approach.
</think>

```python
n = int(input())
s = input().strip()
result = 0
for i in range(n):
    if s[i] == 'B':
        result += 1 << i
print(result)
```
