<think>
Okay, let's see. The problem is about calculating the total hours Vasily can keep the candles burning. The initial input is two numbers a and b. So, the approach here is to consider that each time he burns some candles, the leftovers can be converted into new candles.

So the initial a candles give a hours. Then, the stubs from those a candles (since each burns for an hour, each gives one stub) can be combined. For every b stubs, he can make a new candle. Each new candle adds an hour of burning and produces another stub. So this process continues until there's not enough stubs left to make a new candle.

Let's think about how this works. For example, the first sample input is 4 and 2. So he starts with 4 candles, burning 4 hours. Then he has 4 stubs. Since 4 divided by 2 is 2, he makes 2 new candles. Those take 2 hours, adding to the total. Now he has 2 stubs again (from the 2 new ones). 2 divided by 2 is 1, so he makes another candle. That's 1 more hour. Now he has 1 stub left, but 1 is less than b (2), so he can't make more. Total is 4+2+1=7.

The second example is 6 and 3. 6 hours from the initial. Then 6 stubs, divided by 3 gives 2 new candles. Those take 2 hours. Then 2 stubs. But 2 is less than 3, so can't proceed. Total 6+2=8. Wait, but the output is 8. Wait, why isn't there any more steps? Oh right, because after burning those two, you get two stubs. 2 <3, so no more. So the total is 6+2=8. Which matches the sample.

So the process is:

Total hours = a + (a // b) + ( (a//b + (a % b)) // b ) + ... until the number of stubs is less than b.

Wait, but how to model this? Let's see. Let's denote the initial stubs as s = a.

Wait, but when you burn the initial a candles, the stubs are a. Then, each time you make new candles, you take s // b. Each new candle contributes s//b hours, and then the stubs from those new candles are s//b. Then the leftover stubs after making the new candles is (s % b). So the new stubs after each step are (s // b) + (s % b). Wait, no. Because when you make new candles, you take s stubs. For example, if s is 4 and b is 2, you take 4 stubs to make 2 new candles. Each new candle when burned gives 1 stub. So after burning those 2, you get 2 stubs. So the leftover stubs after making the new candles would be (s // b) * 1 + (s % b). Wait, no. Wait, when you make new candles from s stubs, you use (s // b) * b stubs. So the leftover is s % b. Then, when you burn the new candles (which is s//b in number), each gives 1 stub. So the total stubs after that step is (s % b) + (s // b). Because the new candles burn and add their stubs.

So the process is:

start with total = a

current_stubs = a

while current_stubs >= b:

    new_candles = current_stubs // b

    total += new_candles

    current_stubs = (current_stubs % b) + new_candles

So in code, this loop would run until current_stubs is less than b.

For example, first sample:

a=4, b=2.

Initial total=4, current_stubs=4.

Loop: 4 >=2 → new_candles=2. Total becomes 4+2=6. current_stubs=4%2 +2=0+2=2.

Loop again: 2 >=2 → new_candles=1. Total becomes 6+1=7. current_stubs=0 +1=1. Now 1 <2 → exit. So total is 7.

Second example:

a=6, b=3.

total=6, current_stubs=6.

loop: 6//3=2 → total=8. current_stubs=0 +2=2. 2 <3 → exit. So total 8.

Yes. So this approach works.

So the algorithm is straightforward: accumulate the initial a into total, then track the stubs. Then, while the stubs are enough to make new candles, compute how many, add to total, and update the stubs as (stubs % b) + new_candles (since each new candle gives 1 stub).

So the code will be:

Read a and b.

total = a

stubs = a

while stubs >= b:

    new = stubs // b

    total += new

    stubs = (stubs % b) + new

print(total)

Yes. That's the plan.

Now, let's test this logic with a testable snippet.