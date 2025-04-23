<think>
Okay, let's see. The problem is about figuring out which button press turned off each light. The buttons are pressed in a certain order, and each button when pressed turns off all lights with index not less than its own that are still on. So for each light, we need to find the first button press (in the given order) that caused it to turn off.

Hmm. Let's think about how the button presses affect the lights. When a button bi is pressed, any light with index >= bi that's still on gets turned off. The key here is that each button press affects a range starting from bi upwards. But since the buttons are pressed in some order, the effective button for a light i is the earliest button in the sequence that is <= i and is the maximum such value. Wait, maybe not. Let me think again.

For example, consider the first sample input: buttons pressed are 4,3,1,2. Let's track each light:

Light 1: It's turned off when button 1 is pressed. Because button 4 and 3 are >=1, but when pressed, they turn off all lights not less than their index. So when button 4 is pressed, lights 4 and 5 are turned off. Then button 3 turns off light 3. Then button 1 turns off lights 1 and 2. So for light 1, the button is 1. For light 2, it's also button 1. Light 3 is turned off by button 3. Light 4 by button 4. Light5 by button4.

So, the idea is that for each light i, we need to find the earliest button in the sequence that is <=i and is the smallest possible (or the earliest possible such that when it's pressed, it's the first time that a button <=i is pressed). Wait, no. Because when a button bi is pressed, all lights >= bi that are still on are turned off. So the button responsible for turning off light i is the earliest button in the sequence that is <=i and is the smallest possible (no, wait). Wait, perhaps the correct approach is to find the maximum bi such that bi <= i, and among all such bi, the earliest occurrence in the sequence. Because when a button is pressed, any lights >= bi and still on are turned off. So for a light i, any button press that is <=i and is the latest such (but earliest in the sequence) will determine when it's turned off.

Wait, no. Let's think of it this way. Once a button b is pressed, all lights >=b that are still on are turned off. So for a light i, the first button in the sequence (when processed in order) that is <=i and is the smallest (no, wait, maybe the largest possible) will turn it off. Because if there's a button with a higher value (but <=i) that comes earlier in the sequence, then that button would have turned off the light i. For example, consider i=2. Suppose the buttons pressed are 3, then 2. But 3 is larger than 2, so when 3 is pressed, light 3 and above are turned off. Then when 2 is pressed, light 2 is turned off. So for light 2, the responsible button is 2. But in another scenario, if buttons are pressed in the order 1, 2. For light 2, the first button is 1 (which is <=2), but when pressed, it turns off light 1. Then button 2 is pressed, which turns off light 2. So the responsible button is 2. Wait, but if the button pressed first is 2, then that would turn off light 2. So the earliest button in the sequence that is <=i and is the maximum possible among those <=i. Because a larger b (<=i) pressed earlier would turn off the light earlier. So the maximum value of b in the sequence that is <=i, and the earliest occurrence of such a maximum.

Wait, maybe for each i, the responsible button is the maximum b in the sequence (earliest occurrence) that is <=i. Because when that button is pressed, it turns off all lights >=b that are still on. Since i >=b, and if this is the first button in the sequence that is <=i and has the maximum possible value up to that point, then it will turn off the light.

Alternatively, for each i, we can iterate through the buttons in the order they were pressed. For each button b in the sequence, if b <=i, then we take the maximum such b. Because when that button is pressed, it turns off the light i (assuming it's still on). So the latest (in the sequence) maximum b that is <=i. Wait, maybe that's not right. Because once a button is pressed, it affects all higher or equal index lights. So for example, if buttons are pressed in order 3, 2, 1. For i=1:

Button 3 is pressed first. Since 3>1, it's not <=1. So no effect. Then button 2: 2>1, no effect. Then button 1: 1<=1. So this is the button that turns off light 1. So for i=1, the responsible button is 1. For i=2, the buttons in order are 3 (no effect), 2 (turns off 2), then 1 (but 2 is already off). So responsible is 2. For i=3, it's the first button 3.

So the maximum b in the sequence that is <=i. But we have to find the earliest occurrence of that maximum b. Wait, because if there are multiple buttons <=i, the latest one (in the sequence) with the maximum possible value would be the one that turns off the light. Because the first occurrence of a high value would turn it off, and later buttons with lower values won't affect it anymore.

Wait, maybe not. Let's take an example. Suppose buttons are pressed in order 2, 3. For i=3:

Button 2 is pressed first. Since 2 <=3, and when pressed, turns off all lights >=2. So light 2 and 3 are turned off. Then button 3 is pressed, but lights 3 is already off. So the responsible button for i=3 is 2. But according to the logic of taking the maximum b <=i, the maximum would be 3. But in this case, the button 3 was pressed after button 2, but when pressed, the light is already off.

So, the correct approach is that for each i, the responsible button is the first button in the sequence (earliest occurrence) that is <=i and is the maximum possible such b in the entire sequence (but perhaps that's not correct). Wait, perhaps the correct approach is that for each i, we look for the earliest button in the sequence where b is the minimal possible value that is <=i. No, that doesn't make sense. Let's think of the first sample.

In the first sample, the buttons are 4,3,1,2. Let's see for i=2. The buttons in order are 4 (which is >2, no effect), 3 (>2, no), then 1 (<=2). So when button 1 is pressed, it turns off all lights >=1 that are on. At that point, lights 1 and 2 are on (since buttons 4 and 3 turned off 4,5 and 3, respectively). So button 1 turns off 1 and 2. Then button 2 is pressed, but those lights are already off. So for i=2, the responsible button is 1.

So the responsible button is the first button in the sequence that is <=i and is the smallest possible? No. Because in this case, 1 is the first button <=2. But if in the sequence there was a button 2 pressed earlier, it would have turned off light 2. So the correct approach is: for each light i, the responsible button is the earliest button in the sequence such that when pressed, it is the first time a button <=i is pressed. Because once such a button is pressed, the light is turned off. But wait, if the button is pressed and is <=i, but i was already turned off by a previous button with a higher value. Like in the first example for light 2: button 1 is pressed, but before that, there were buttons 4 and 3 which are higher than 2 but didn't affect light 2. So when button 1 is pressed, light 2 is turned off.

So, the correct logic is: for each light i, we need to find the earliest button in the sequence that is <=i and is the maximum possible such button up to that point. Wait, perhaps the correct way is to track for each i the minimal button (in the sequence) that is the first one to turn it off.

Alternatively, here's an approach. For each light i, the button that turns it off is the first button in the sequence that is <=i and is the maximum possible in the sequence up to that point. Wait, maybe not. Let me think again.

Let's think of each button press. When a button b is pressed, it affects all lights >=b that are still on. So for a light i, the earliest button in the sequence where b <=i and after this button is pressed, the light i is turned off.

So, for light i, the responsible button is the first button in the sequence that is <=i and is the maximum among all buttons up to that point that are <=i. Wait, maybe not. Let's take the example where the buttons are pressed in order 3,4. For i=4: first button is 3 (<=4), which turns off all >=3. So light 4 is turned off by button 3. Then button 4 is pressed, but light 4 is already off. So the responsible button is 3. But according to the maximum button <=i, 4 is the maximum and is pressed later. But in this case, the first button that is <=4 is 3, which is pressed first. So when 3 is pressed, it turns off light 4. So the responsible button is 3, not 4. But 4 is also <=4 and is a larger value. So the logic here is that the first button in the sequence that is <=i and is the maximum possible up to that point. Because once such a button is pressed, all lights >=b are turned off, and subsequent buttons (even if larger) would not affect them.

Wait, but in this example, the buttons are 3,4. For i=4, the first button is 3. When pressed, light 4 is turned off. Then button 4 is pressed but has no effect. So the responsible button is 3. But 4 is larger than 3 and is pressed later. So in this case, the responsible button is the first occurrence of the maximum possible value <=i in the entire sequence. So the maximum possible value is 4, which is <=i=4 and is present in the sequence. But since it's pressed after 3, the light i=4 is turned off by button 3. So the maximum value is 4, but it's pressed later, so the light is already turned off. So the responsible button is the first occurrence of the maximum value <=i in the entire sequence. Wait, no. Because the maximum value is 4, which is pressed second, but that button is pressed after the light was turned off. So the responsible button is 3.

Hmm. So this suggests that the responsible button for i is the earliest occurrence of the largest possible b <=i in the entire sequence. Wait, but in the example where the sequence is 3,4, the maximum b <=4 is 4. But it's pressed after 3, which already turned off the light. So the responsible button is 3, not 4.

Therefore, the correct logic must be: For each light i, the responsible button is the earliest occurrence in the button sequence where b is the maximum among all buttons that are <=i and have been pressed up to that point. So, as we process each button in order, for each button b, we can update the answer for all i >=b where the current answer for i is not set yet. Because when the button is pressed, it turns off all i >=b that are still on. So for those i, their answer becomes the current button's index (the button's original value, not the order in the sequence). But how to track this efficiently.

Ah, this seems like a possible approach. Let's think of it this way: Initially, all lights are on. For each button in the order they are pressed, when we press button b, we turn off all lights >=b that are still on. So for each such light, we set their answer to be the current button's value (b). So the approach is to track for each light i the first button (earlier in the sequence) that turned it off. 

But how to efficiently compute this? For example, if the buttons are pressed in the order 4,3,1,2. Let's process each button:

- Press 4: all lights >=4 are turned off. So lights 4 and 5 now have answer 4. Remaining on: 1,2,3.
- Press 3: all >=3 (and still on) are 3. So light 3's answer is 3.
- Press 1: all >=1 (still on: 1,2). So their answers are set to 1.
- Press 2: all >=2 (but 2 is already off). So no changes.

So the answers are as per the first sample.

So the way to model this is to track for each light whether it's on or off, and when a button is pressed, for all lights >=b that are on, set their answer to this button's value and mark them as off. But for n up to 1e5 (wait, no, wait the constraints say n and m up to 100. Oh, the problem constraints are n and m up to 100. So even a O(n*m) approach is acceptable. So the code can be straightforward.

So the steps are:

1. Initialize an array ans of size n, all None (or 0) initially. Also, a list of on/off flags, initially all True (on).

2. For each button b in the sequence (in order of pressing):

   a. For each light i from b to n:

      i. If i is still on, set ans[i-1] = b (since the indices are 1-based), and mark it as off.

3. After processing all buttons, output the ans array.

But since n is up to 100, this approach is feasible. Because for each of the m buttons, we iterate up to n steps. 100 * 100 = 1e4 operations, which is acceptable.

Wait, but in the first sample, when we process button 4, we check all lights >=4. Which are 4 and 5. Then when processing button 3, check lights >=3. So 3, 4,5. But 4 and 5 are already off, so only 3 is processed. Then button 1: check all >=1, which are 1,2,3 (but 3 is off). So 1 and 2 are set. Then button 2: check >=2. 2 is already off, so nothing.

So for each button, we can iterate from b to n, and check if the light is on. If yes, set the answer and mark it as off.

But how to do this efficiently. For small n (up to 100), this is trivial.

So the code can be written as:

Read n and m.

Read the list of buttons (as a list of integers).

Initialize ans array with 0s, and a list on_flags with True for all elements.

For each b in the buttons:

    for i in range(b, n+1):

        if on_flags[i-1] is True:

            ans[i-1] = b

            on_flags[i-1] = False

Then print the ans array as space-separated integers.

Yes. This would correctly compute the answer. Let's test against the first sample.

Sample 1:

n=5, m=4. Buttons [4,3,1,2].

Processing buttons in order:

Button 4:

i ranges from 4 to 5:

i=4: on_flags[3] is True. Set ans[3] =4, mark as off.

i=5: on_flags[4] is True. Set ans[4] =4, mark off.

ans now [0,0,0,4,4]

on_flags: [True, True, True, False, False]

Button3:

i from3 to5:

i=3: on_flags[2] is True. ans[2] =3. mark off.

i=4: already off.

i=5: already off.

ans now [0,0,3,4,4]

on_flags: [True, True, False, False, False]

Button1:

i from1 to5:

i=1: on_flags[0] is True. ans[0] =1. mark off.

i=2: on_flags[1] is True. ans[1] =1. mark off.

i=3: off.

i=4: off.

i=5: off.

ans now [1,1,3,4,4]

Button2:

i from2 to5:

i=2: already off.

others: off.

So ans is correct.

Yes. So this approach works.

In the second sample, buttons pressed in order 5,4,3,2,1.

Each button is pressed in order. For button5, all lights >=5 (only 5) is turned off. Then button4: light4, etc. So each light is turned off by the button equal to their index. So ans is 1,2,3,4,5.

Wait, no. Wait the buttons are 5,4,3,2,1.

Processing button5: turns off 5. ans[4] =5.

button4: turns off4. ans[3] =4.

button3: turns off3. ans[2]=3.

button2: turns off2. ans[1]=2.

button1: turns off1. ans[0]=1.

So the output is 1 2 3 4 5. Which matches the sample.

So the code works.

Thus, the code can be written as described.

Now, for the code:

Read n and m from input.

Read the list of m integers, b list.

Initialize ans as a list of n zeros.

on_flags as list of True for n elements.

Then loop through each button in b:

   for i in range(b, n+1):

       if on_flags[i-1] is True:

           ans[i-1] = button

           on_flags[i-1] = False

Then print ans as space-separated.

Yes. Now code.

But in Python, list indices start at 0. So for light i (1-based), the index is i-1.

So for each button in the buttons list, which is given as b1, b2, ..., bm. We process them in order.

Now code.

Testing the first sample:

n=5, m=4, buttons [4,3,1,2].

ans starts as [0,0,0,0,0]

on_flags [True, True, True, True, True]

Processing 4:

i runs from 4 to 5:

i=4: index 3. on_flags[3] is True. ans[3] =4. set to False.

i=5: index4. on_flags[4] True. ans[4] =4. set to False.

Processing 3:

i runs from3 to5.

i=3: index2. on True. ans[2] =3. set to False.

Processing1:

i runs from1 to5:

i=1: index0. True. ans[0]=1. False.

i=2: index1. True. ans[1] =1. False.

i=3: index2. already False.

i=4: etc. no.

Processing2:

i runs from2 to5:

index1: False (since set by 1). So nothing.

Thus, ans is [1,1,3,4,4], which is correct.

Yes.

So the code works.
</think>

```python
n, m = map(int, input().split())
buttons = list(map(int, input().split()))
ans = [0] * n
on = [True] * n

for b in buttons:
    for i in range(b, n + 1):
        if on[i - 1]:
            ans[i - 1] = b
            on[i - 1] = False

print(' '.join(map(str, ans)))
```