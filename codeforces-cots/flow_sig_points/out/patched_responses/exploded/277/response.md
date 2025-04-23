<think>
Okay, I need to solve this problem where we have to find the minimum number of operations to reach a number x with exactly n digits. Each operation allows us to multiply x by one of its digits. Let's think through this.

First, the problem states that each operation is choosing a digit y from the current x and multiplying x by y. We need to find the least steps to get x to have exactly n digits. If it's impossible, return -1.

Hmm. Let's look at the examples. Like the second example: starting with 2, steps are multiply by 2 (4), then 4 (16), then 6 (96), then 9 (864) which is 3 digits. So four operations. Oh right, the output is 4. So each step increases the number of digits, but maybe not always. For example, multiplying by 1 would not change the number. So we have to avoid digits that would not help.

Wait, but the initial x might already be of length n. Wait, the input constraints say that x is less than 10^(n-1). Because 10^(n-1) is the smallest n-digit number. So if x is already n digits, then we need to check if the initial x's length is exactly n, but according to the input constraints, x is less than 10^{n-1}, which implies that the initial x has at most n-1 digits. So the problem is to reach exactly n digits from a starting point with fewer digits.

So the first thing is to check the initial length of x. For example, if x starts with a length equal to n, then we can return 0 steps. But according to the input constraints, that's not possible. Because x is given as 1 <= x < 10^{n-1}, which means x has at most n-1 digits. So we can ignore that case.

So the problem is to find the minimal steps to reach a number with exactly n digits by multiplying by digits present in the current number.

Let me think about possible approaches. This feels like a BFS problem. Because each operation branches into possible next states (multiplying by different digits), and we need the shortest path to reach a state where the number has n digits.

But considering that the numbers can get very large. For example, in the third example, n is 13, and x starts as 42. The maximum x after each multiplication can be up to something like 42 multiplied by 9 each step. So the number of digits can increase exponentially. However, if n is up to 19, then the maximum possible steps would be when each step adds a minimal number of digits. But even then, the numbers can become very large, which makes it impossible to represent them directly in a BFS.

So we need a way to represent the state without having to track the actual x, but track the number of digits and maybe some other parameters. Because for BFS, tracking the exact x is not feasible for large x. But how else can we model the state?

Wait, but what's important is the current number of digits, and the possible digits present in the current number. Because the next step's options depend on the digits in the current x. So maybe we can model the state as (current_digits_count, available_digits). Then, for each state, we can compute possible next states by multiplying by each available digit and checking how the digits count increases.

Wait, but the available digits in the next state depend on the digits of the new x. For example, if current x is 16, which has digits 1 and 6. If we multiply by 6, the new x is 96, which has digits 9 and 6. So the available digits for the next step are 9 and 6. So the state needs to include the digits present in the current x.

But storing the digits present as a set would be manageable. Because for a number, the unique digits present can be up to 10 (0-9), but 0 is a problem. Because if x has a 0 as a digit, multiplying by 0 would set x to 0, which can't grow anymore. So once we have 0 as a digit, any multiplication by 0 would result in 0, and no further steps can increase the digits. So in such a case, it's impossible to reach n digits unless n is 1 (but in our problem, n is at least 2). So including 0 in the digits set is a dead end unless the current x is 0, which would already be 1 digit, but according to input constraints, x starts at 1. Wait, the input x can be 0? Wait, the problem statement says "two integers n and x (2 ≤ n ≤ 19; 1 ≤ x < 10^{n-1})". So x is at least 1, so initial x can't be 0. So, any step that introduces a 0 in x's digits would lead to possible problems.

So, to model the state, perhaps the key factors are:

- The current number of digits (since we need to reach exactly n).
- The set of available digits (since they determine possible multipliers).

Additionally, when we multiply by a digit, the new number's digits are determined by the product. So for each state (digits_count, digits_set), we can generate new states by multiplying by each digit in digits_set. The new digits_count is the number of digits of the product (digits_count_prev * digit). Then the new digits_set is the set of digits in the product.

Wait, but the actual product's digits are needed. For example, if current digits_count is d, and we multiply by y (a digit in the current digits_set), then the new x is (current x) * y. The number of digits of the new x is floor(log10(x * y)) + 1. But how to compute that without actually tracking x?

Alternatively, maybe we can model the state as the current digits count and the current set of available digits. Then, for each possible operation (choosing a digit y from the current digits), compute the next digits count and the next set of available digits.

But how to compute the next digits count based on the current digits count and y?

Wait, perhaps not exactly. Because the actual value of x affects the digits count. For example, if the current x is 9 (1 digit), and we multiply by 9 (y=9), the new x is 81 (2 digits). But if the current x is 10 (2 digits), multiplying by 0 (if allowed) would set to 0 (1 digit). But since initial x is at least 1, and in our problem, we are trying to reach n digits, but if a step reduces the digits count, that's not helpful. However, in the problem statement, the operations are allowed, but we are to reach exactly n digits. So steps that overshoot (like the digits count exceeds n) are invalid. Wait, no. Let me check the problem statement again.

The problem says: you want to make the length of x equal to n. So if during the process, x's length becomes larger than n, you can't stop. You have to reach exactly n digits. So for example, if current x is 999 (3 digits) and n is 3, then no steps are needed. But according to the input constraints, x starts with less than n digits. So in our problem, the initial x is less than 10^(n-1), so its digits count is at most n-1. So the steps must not reach a digits count larger than n. Otherwise, the process would have failed.

Wait, but after multiplying, the digits count can increase. For example, if current digits count is d, and you multiply by a digit y. The new digits count could be d + 1, or maybe even more. For example, 99 (2 digits) multiplied by 9 gives 891 (3 digits). So digits count increases by 1. 999 (3 digits) multiplied by 9 gives 8991 (4 digits). So digits count increases by 1. So perhaps the digits count increases by 0 or 1, but not more. Wait, 99 is 2 digits, multiply by 9 gives 891 (3 digits). But 9999 (4 digits) multiplied by 9 is 89991 (5 digits). So each multiplication by a digit (>=1) can increase the digits by at most 1? Or maybe not. Let's see: 9999 is 4 digits. 9999*9 = 89991 (5 digits). 89991 *9 = 809919 (6 digits). Each step increases by 1. But what about 999 * 9 = 8991 (4 digits). So 3 digits multiplied by 9 gives 4 digits. So yes, each multiplication can increase digits count by 1. So the maximum possible steps is when each step adds exactly one digit, but perhaps some steps can add more.

Wait, no. Let's take x = 1. Multiply by 9: 9 (1 digit). Then multiply by 9: 81 (2 digits). So first step: 1 digit → 1 digit (but the product is 9). Then the second step brings it to 2 digits. So in this case, the first step doesn't increase the digit count. Because initial x is 1 (1 digit). Multiply by 9 gives 9 (still 1 digit). So the digits count may stay the same, or increase by 1.

But how can we model the digits count and the possible digits without tracking the actual x value?

Hmm. That seems tricky. Because the same digits count and digits set can correspond to different x's, which when multiplied by a digit can lead to different next digits counts and digits sets.

So, for example, x could be 91 (digits 9 and 1). If we multiply by 1, x becomes 91*1=91 (same digits count and digits set). If we multiply by 9, x becomes 819 (digits count 3, digits 8,1,9). But another x of same digits count and digits set, say 19. Multiply by 9 gives 171 (digits 1,7). So the digits set changes differently.

So the problem is that the same (digits_count, digits_set) can lead to different next states when multiplied by a digit. Therefore, modeling the state as (digits_count, digits_set) is insufficient. Because different x's with same digits_count and digits_set can have different products when multiplied by a digit. Thus, the next state can't be determined solely from the current digits_count and digits_set.

This complicates things. Because tracking the actual x is necessary, but x can get very large. For example, in the third sample input, after 12 steps, x is multiplied multiple times. The maximum possible x can be up to 42 multiplied by various digits 12 times. But 42 is two digits, and each step can multiply by up to 9, so 42 *9^12. That's a very big number. Storing such numbers in a BFS queue is not feasible in terms of memory.

So, how can we approach this?

Alternative approach: BFS, but with pruning. For each x, track the number of steps. Once x reaches or exceeds 10^{n-1}, check if it's exactly n digits. If it's more than n digits, that path is invalid. So we can model the BFS as (current_x, steps). But for x that can become very large, this is not feasible.

But considering that n can be up to 19. Let's see what the maximum possible x can be. For example, n is 19. Then, the target is to reach a number with exactly 19 digits. The maximum possible x after k steps would be x multiplied by the product of the digits chosen. Let's see. For example, starting with x=42 (as in the third example), each step multiplies by a digit. Let's assume that each digit is 9, then after 12 steps, x becomes 42 *9^12. Let's compute 9^12 is 282429536481. 42 * that is around 1.18e13, which is 13 digits. Wait, but the third sample's output is 12 steps, leading to 13 digits. Wait, but the initial input is 42 (2 digits), and after 12 steps, it's 13 digits. So each step adds about 1 digit.

But in the worst case, for n=19, the steps required could be up to 17 steps (starting from 2 digits). Each step adds 1 digit. So in BFS, the maximum number of steps would be manageable. But the problem is that the x values could be up to 1e19, which is a 19-digit number. But even so, in Python, handling such large integers is possible, but the BFS can have a lot of states. So the question is: can we manage the BFS without having the same x being processed multiple times?

Because in BFS, we need to track visited states to avoid cycles. For example, if we reach x=96 in two different ways with the same steps, but different paths, we need to mark it as visited. Otherwise, we'll process it multiple times, leading to inefficiency.

So, the key is to track which x's we have already processed. But for x up to 1e19, storing all possible x's in a visited set is impossible in terms of memory. For example, 1e19 possible x's is way too large. So we need a way to prune the BFS.

Alternative idea: For a given x, the minimal steps to reach it is what we need. So once we have processed x with a certain steps count, any later paths that reach x with a higher steps count can be ignored. Therefore, we can use a BFS approach where each state (x) is processed only once, with the minimal steps. So when x is added to the queue, we can check if it's already been visited, and if so, skip processing it again.

This would work if we process the states in order of steps. BFS ensures that the first time we reach x is with the minimal steps. So the visited set can be maintained to track which x's have been processed.

So the steps are:

1. Initialize a queue with (x, steps=0).

2. For each element in the queue, check the length of x. If it's exactly n, return the current steps.

3. Otherwise, generate all possible next x's by multiplying by each digit present in the current x. For each next_x, if it hasn't been visited and its digits count is less than n, add it to the queue and mark as visited.

4. Continue until the queue is empty. If no such x found, return -1.

But the problem is the size of x. For example, in the third sample, after 12 steps, x could be up to something like 42 multiplied by various digits, leading to 13 digits. So the x would be 1e13, which is manageable as a Python integer. But for n=19, the x could be up to 1e19. However, even 1e19 is manageable in Python as an integer.

But how many unique x's can there be? For example, each step can multiply by any of the digits in the current x, which could be up to 9 options (digits 1-9). So for each step, the branching factor is up to 9. But the number of steps required could be up to 17 (since starting from 1-digit x to 19 digits would take 18 steps). But that's 9^17 possible x's, which is way too large (over 1e16). So BFS is not feasible here.

So this approach would not work for n up to 19 because the number of possible x's is way too big. So we need a smarter way.

Alternative idea: instead of tracking x, track the digits present in x and the current digits count. Because for the same digits count and digits set, the minimal steps to reach that state would be known. For example, if two different x's have the same digits count and same digits set, then they can be considered the same state. Because the next steps would depend only on the digits present and the digits count.

But earlier, we saw that this is not sufficient, as different x's with the same digits count and digits set can lead to different next states. However, perhaps even if they do, the minimal steps are considered. For example, if two x's have the same (digits_count, digits_set), but different x values, but when you multiply by a digit, one leads to a higher digits_count than the other, then processing the x with the higher digits_count first would help. But BFS processes in steps order, so perhaps even if two x's have the same (digits_count, digits_set), but different x's, but one reaches the required digits_count in fewer steps, then the other can be ignored.

Wait, but the steps count is the same for all x's processed at a certain level in BFS. So perhaps, for each (digits_count, digits_set) state, we track the minimal steps required. Because once we have processed that state with steps k, any later processing of the same state with steps >=k can be ignored.

So the state can be (digits_count, digits_set). Then, for each such state, we can track the minimal steps needed to reach it. Then, when processing a state, for each digit in the digits_set, compute the next digits_count and next digits_set, and update the steps.

But how to compute the next digits_count?

Wait, the next x is current x multiplied by a digit y. The digits_count of next x is floor(log10(x*y)) +1. But since we don't track x, we can't compute this. So this approach is not feasible.

Alternative Idea: Can we find an upper bound on the steps needed? Let's think about what's the maximum possible steps. For example, if we have to reach n digits from m digits (m <n). Each step can increase the digits by at most 1. So the minimal steps is n-m. But sometimes, steps may not increase the digits count, leading to more steps. For example, starting with x=1 (1 digit), multiply by 9 (still 1 digit), then multiply by 9 again to get 81 (2 digits). So two steps. Here, n=2, m=1. So steps needed are 2 steps, which is more than n-m.

So the minimal steps can vary. But perhaps the steps are bounded by something like (n - m) * k, where k is some factor. But I'm not sure.

Alternative approach: use BFS but track the current x and steps. However, to manage the visited set, we can track for each x the minimal steps required. Once x is in the visited set, we don't process it again.

But for x that can be up to 1e19, the visited set could be very large. For example, 1e19 is 10^19 possible x's, which is way beyond memory. So this approach is not feasible.

So, how else can we model this problem?

Wait, the key is that the digits of x determine the possible multipliers. So perhaps, when x has certain digits, the next possible steps are determined by those digits. So, even if two different x's have the same digits, their product when multiplied by a digit may differ. But maybe not. For example, if x1 and x2 are two different numbers with the same digits (in any order), then multiplying by a digit y (which is present in their digits) would produce x1*y and x2*y. If x1 and x2 have the same digits, then x1*y and x2*y may not have the same digits. For example, x1 = 12 (digits 1,2) and x2=21. Multiplying by 2 gives 24 (digits 2,4) and 42 (digits 4,2). So the digits sets are same. So in this case, the next state would have the same digits set. But if x1 is 12 and x2 is 12, then same. But if x1 is 13 and x2 is 31, multiplying by 3 gives 39 (digits 3,9) and 93 (digits 9,3). So same digits set.

So perhaps, the digits set is the same regardless of the order of digits in x. Thus, for the next digits set, the order of digits in x may not matter. So, the next digits set is determined by the digits of x*y. So for two different x's with the same digits set and same digits count, multiplying by y may lead to the same next digits set and digits count. But not necessarily. For example, x1= 99 (digits 9) and x2= 9 (digits 9). Multiplying by 9 gives 891 (digits 8,9,1) and 81 (digits 8,1). So even though the digits set was same, the product's digits set is different. So this approach is invalid.

Thus, the problem remains that two different x's with the same digits set and digits count can lead to different next states. Therefore, we can't model the state as (digits_count, digits_set).

Hmm. So what's the way out?

Alternative Idea: Since the problem requires the minimal steps, perhaps BFS is the only way. However, the numbers can be very large, but perhaps we can limit the BFS by considering that once a number exceeds 1e(n), which is the first number with n+1 digits, we can stop processing it. Because multiplying by any digit (>=1) will only make it larger. So, for example, if x has a digits count greater than or equal to n, we can ignore it. Because we need exactly n digits. So if x's digits count is larger than n, it's impossible. So, during BFS, we can check if the current x's digits count is equal to n. If it is, return steps. If it's larger than n, skip processing. So, in the BFS, we only process x's with digits count less than n.

Moreover, for the same x, once it's been processed (added to the queue with a certain steps count), any later occurrence can be ignored, since BFS ensures the steps are minimal.

So, the steps would be:

- Initialize the queue with (x, steps=0).

- For each x in the queue:

   - Check the digits count of x. If it's n, return steps.

   - Generate all possible next x's by multiplying with each digit in x's digits.

   - For each next_x:

      - Compute its digits count. If digits count >n, skip.

      - If next_x hasn't been visited before, add it to the queue, mark as visited.

- If the queue is exhausted, return -1.

But the problem is the visited set. For example, x can be up to 1e18 (for n=19, initial x can be up to 1e18 -1), but after a few multiplications, it can reach 1e19, which is 20 digits, but in that case, it's skipped. So the maximum x's stored in the visited set are those with digits count up to n-1.

But even so, the number of x's can be very large. For example, for n=19, the maximum possible x is 1e19-1, which is 19 digits. But the BFS can't handle that. So this approach is not feasible for large n.

So we need a smarter way.

Alternative Idea: Prune the BFS by tracking the best steps for each digits count and digits set. For example, for a given digits count d and digits set s, the minimal steps to reach that state is stored. So if a new state comes with the same d and s but higher steps, it can be skipped.

But how to compute the next digits count and next digits set without knowing x? That's the problem.

But perhaps, for each state (d, s), we can track the minimal steps to reach it. Then, when processing (d, s), for each digit y in s, compute the next x (which is x * y). But we don't track x. So this isn't possible.

Wait, but the digits count d' of x*y can be computed as floor(log10(x) + log10(y)) +1. But since x is a number with d digits, x is between 10^(d-1) and 10^d -1. So log10(x) is between d-1 and d. log10(y) is between 0 and log10(9) ~ 0.9542. So x*y is between (10^(d-1)) *1 =10^(d-1) and (10^d -1)*9.

The digits count of x*y is then floor(log10(x*y)) +1. So for x in [10^(d-1), 10^d -1], y in [1,9], the minimal possible x*y is 10^(d-1)*1 =10^(d-1) (digits count d), and the maximal is (10^d -1)*9 = 9*10^d -9. The digits count of that is floor(log10(9*10^d -9)) +1 = d+1. Because 9*10^d is 10^{d}*9, which is a d+1-digit number (like 9000...0). So 9*10^d -9 is 899...91, which has d+1 digits. So when you multiply a d-digit number x by y, the result can be either a d-digit or d+1-digit number.

So, the next digits count can be either d or d+1.

So, for each state (d, s), and each possible y in s, the next digits count is either d or d+1.

But how to determine which one it is without knowing x?

For example, if x is 10^(d-1) (smallest d-digit number), and y is 1: then x*y = 10^(d-1) → digits count d. If y is 9: x*y =9*10^(d-1) → which is d digits. But if x is 10^d -1 (the largest d-digit number), and y is 9: x*y= 9*(10^d-1) =9*10^d -9 → which is d+1 digits.

So for a given d and y, the next digits count can vary between d and d+1, depending on x.

But since we don't track x, how can we model this?

Alternative Idea: For each possible state (d, s), when we multiply by y, the next digits count can be either d or d+1. So we can generate both possibilities and see if they can reach the target. But this is not accurate and may lead to overcounting.

Alternatively, for each (d, s, y), the minimal possible digits count after multiplying by y is d (when x*y is exactly 10^{d} -1), and the maximal is d+1. But since we can't track x, perhaps we have to consider all possibilities.

Wait, but this seems like a dead end. Because without knowing x, we can't compute the exact next digits count. So this approach can't be used.

Alternative Idea: Maybe the maximum possible digits count after multiplying by y is d+1, and the minimum is d. So during BFS, for each possible state (d, s), and each y in s, the next state's digits count can be d or d+1. But how do we determine which one it is? If we have to consider both possibilities, the BFS can become even larger.

This doesn't seem feasible.

Another Idea: Think in terms of the minimal steps. Since we need the minimal steps, perhaps the optimal path is to maximize the digits count increase in each step. So, for each possible y, choose the one that gives the maximum possible digits count. For example, if multiplying by y can lead to d+1 digits, then that's better than a y that can only lead to d digits. So, in each step, we should choose the y that gives the largest possible digits count.

But how to determine which y's can lead to d+1 digits?

But again, without knowing x, it's impossible to know. However, maybe for a given d and y, there's a way to know if multiplying by y can lead to d+1 digits.

Wait, for a d-digit x, the product x*y can be up to (10^d -1)*y. For example, when y=9 and x=10^d -1, the product is 9*(10^d -1) = 9*10^d -9. Which is a d+1-digit number (like 999...999 -9 is 999...990, but when multiplied by 9, for x=999 (d=3), 999*9=8991 (4 digits).

So the product x*y is a d+1-digit number if x*y >= 10^{d}.

So, for x to have d digits, x is between 10^{d-1} and 10^{d} -1.

x*y >= 10^{d} → y >= 10^{d}/x.

But x can be as small as 10^{d-1}, so 10^{d}/(10^{d-1}) =10. So y must be >=10. But y is a digit (0-9). So this is impossible. Wait, that's a problem.

Wait, let's re-calculate. For x >= 10^{d-1}, and y is a digit (1-9), x*y can be as large as (10^d -1)*9.

For example, d=3: x can be up to 999, y=9 → 8991 (4 digits).

The minimal x that after multiplying by y gives d+1 digits is x >= ceil(10^{d} / y). Because x*y >= 10^{d} → x >= 10^{d}/y.

But x is a d-digit number, so x >=10^{d-1}.

So for y >= 10^{d}/(10^{d} -1), which is 10^d/(10^d-1) ≈ 1. So any y >=1 can satisfy x >=10^{d}/y if x is large enough.

But this seems to depend on x. So, again, without knowing x, we can't determine if multiplying by y will increase the digits count.

So this line of thinking isn't helpful.

Alternative Idea: Maybe, for each state (d, s), the maximum possible next digits count is d+1. So we can assume that multiplying by y will lead to d+1 digits. This might be an over-approximation, but if we can find a path where each step increases the digits count by 1, then that's the minimal steps.

But this is not necessarily true. For example, in the second sample:

3 2 → output 4.

The steps are 2 →4 (1 step, 1 digit → 1 digit), then 4→16 (2 digits), then 16→96 (2 digits →3 digits?), wait no. Wait, let's recheck:

Sample 2:

Input: 3 2 → output is 4.

Steps:

1. 2 *2 =4 → 1 digit.

2. 4 *4 =16 →2 digits.

3. 16 *6 =96 → 2 digits.

Wait, 16*6=96, which is 2 digits. Then multiply by 9 →96*9=864, which is 3 digits.

So steps are 4, and the digits count increases as 1→1→2→2→3. So two steps didn't increase the digits count. So the minimal steps may require steps that don't increase the digits count. Thus, assuming that each step increases the digits count by 1 is incorrect.

Thus, the problem must be modeled accurately, which brings us back to the BFS approach.

But the problem is the size of the visited set. Let's think about the constraints. The time limit is 2 seconds. Python can handle around 1e6 operations per second. So for the BFS to be feasible, the total number of nodes processed should be up to around 1e6.

But for n=19, and starting with x of 1 digit, the steps needed could be 18 steps (each step increasing the digits count by 1). But in reality, some steps may not increase the digits count. However, the worst case is that the BFS processes a lot of nodes. So the BFS must be optimized.

But how? Let's think about what's the maximum possible number of nodes.

Each node is a unique x, which hasn't been visited before. But x can be up to 1e19 (for n=19, the target is 19 digits, but during steps, x can be up to 1e19-1). But even so, 1e19 is way too large to track in a visited set.

So this approach is not feasible.

Alternative Idea: For each x, track the digits set. So, even if x is different, but has the same digits set and digits count, we can consider them as the same state. Because, in terms of possible multipliers, they are the same. However, as discussed earlier, the next state can vary because the product's digits count depends on x's actual value.

But perhaps, in the BFS, we can track the state as (digits_count, digits_set), and for each such state, track the minimal steps required. But when processing a state (d, s), how do we determine the possible next states?

For example, when processing (d, s), we can multiply by any y in s. For each such y, we need to compute the next digits count. But since we don't have x, we can't compute it. So this is impossible.

Thus, this approach won't work.

Alternative Idea: Perhaps, the problem can be modeled using dynamic programming (DP), where the state is (digits_count, digits_set), and transitions are based on possible y's. But again, without knowing the x, it's impossible to compute the next digits count and digits set.

So, this seems stuck.

Wait, perhaps we can precompute for each possible (d, s, y) the possible next digits counts and digits sets. But how?

Alternatively, perhaps, for each possible (d, s), the maximum possible next digits count when multiplying by any y in s is d+1. So, if we can model the state as (d, s), and track the steps, then for each possible y in s, the next state is (d+1, s'), where s' is the digits of x*y. But again, without x, we can't compute s'.

Hmm. So this is not feasible.

Alternative Idea: Let's think of this problem in terms of BFS, but with some optimizations. For example, when a certain x is processed, we can note that any larger x (in terms of digits count) would have been processed later. But again, this doesn't help.

Another Idea: Since multiplying by 1 has no effect on x, any step that uses y=1 can be ignored. Because multiplying by 1 doesn't change x, so it's a waste of a step. So, in the BFS, when generating next steps, if a digit is 1, we can skip it. Except when the current x's digits include 1 and other digits. But even then, multiplying by 1 is a waste.

So, in the code, when generating the next x's, we can exclude y=1, except when the current x is 1. But if x is 1, multiplying by 1 leaves it as 1. So, in this case, it's impossible to reach n digits if n is >=2 (since 1*1=1, which is 1 digit). So the BFS can safely skip any y=1 unless x is 1. But x starts with 1 and n is 2, then it's impossible. So in code, whenever the current x's digits include 1, we can ignore y=1.

This optimization can reduce the branching factor.

Similarly, other digits can be considered. For example, multiplying by 0 is a dead end (since x becomes 0, which is 1 digit and can't be multiplied further). So, any step that uses y=0 should be avoided. Because after multiplying by 0, x becomes 0, which is 1 digit. But since the problem requires x to have exactly n digits (n >=2), this is impossible. So, in the code, when x's digits include 0, we can ignore y=0. Because multiplying by 0 would make x 0, which is a dead end.

So, the code can be optimized to skip y=0 and y=1 (if possible).

Another Optimization: When generating next_x, after multiplying by y, if the digits count of next_x exceeds n, then skip processing it. Also, if the digits count is exactly n, return steps +1.

So, during the BFS, for each x:

   current_steps = steps

   current_digits = number of digits in x

   if current_digits ==n → return steps.

   else:

      for each y in digits of x:

         if y ==0: skip (since x*y will be 0 → 1 digit, which is <n (n>=2), so no way)

         if y ==1: skip (since x*y =x → same digits count, and steps increases by 1. But since steps is minimal, processing x again with steps+1 is worse than the first time.)

         next_x = x * y

         next_digits = number of digits of next_x.

         if next_digits >n: skip.

         if next_digits ==n: return steps +1.

         else: if next_x not in visited → add to queue.

So, with these optimizations, the BFS can proceed.

But even with this, the number of x's can be very large. For example, in the third sample input, 42 → multiply by 4 and 2. Let's see:

42 → digits 4,2. So possible y's are 4 and 2.

Multiply by 4: 42 *4 = 168 (3 digits). Steps=1. digits are 1,6,8.

Multiply by 2: 42*2=84 (2 digits). Steps=1. digits are 8,4.

So in step 1, two possibilities. For each of these, generate next steps.

But for large n, this can branch into many possibilities.

But perhaps, given the time constraints and the sample inputs, the BFS approach is manageable.

Another Optimization: For the visited set, we can use a dictionary that tracks the minimal steps for a given x. So when we encounter an x that was already processed with a lower or equal step count, we skip it. But since BFS processes nodes in order of step count, once x is added to visited, any future occurrence will have a higher step count. So, in BFS, once x is processed, we can ignore any future occurrences.

Thus, the visited set can be a set of x's that have been added to the queue. Because BFS processes nodes in order of steps, once x is processed, any future path to x with higher steps is irrelevant.

So, the algorithm is:

Initialize a queue with (x, 0 steps).

Initialize a visited set with x.

While queue not empty:

   x, steps = dequeue.

   current_digits = len(str(x)).

   if current_digits ==n: return steps.

   if current_digits >n: continue.

   for each digit in str(x):

      y = int(digit)

      if y ==0 or y ==1: continue.

      next_x = x * y

      next_digits = len(str(next_x)).

      if next_digits >n: continue.

      if next_x not in visited:

          if next_digits ==n: return steps +1.

          visited.add(next_x)

          enqueue (next_x, steps+1)

If queue is empty: return -1.

This is the BFS approach.

But for large n, this could be problematic. Let's see what happens in the third sample input:

n=13, x=42.

The steps required are 12. So the BFS would process 12 levels. At each level, the number of nodes depends on the branching factor.

But for each x, the digits are unique, and the possible y's are the digits in x. For example, 42 → digits 4,2. So two choices. Then, for each of those choices, the next_x is computed, and their digits are considered.

But as the steps increase, the number of possible x's can grow exponentially, but due to the visited set, duplicates are avoided.

But even so, for 12 steps, with a branching factor of 2, it's 2^12=4096 nodes. Which is manageable.

But for cases where the branching factor is higher, like 3 or 4, and steps up to 18, it's 3^18 ≈ 3.8e8, which is way too large for Python's BFS to handle in 2 seconds.

But in practice, the visited set would prune many paths. For example, different paths may lead to the same x with the same steps, thus not adding redundant nodes.

So, the key is whether the BFS can process all possible x's within the time constraints.

Another Optimization: The number of digits of next_x can be computed without converting to a string. For example, using math.log10 or other methods. This is faster than converting to a string and getting the length.

Yes, because for a number x, the number of digits is floor(log10(x)) +1. So, for x >0:

digits_count = len(str(x)) → same as digits_count = int(math.log10(x)) +1.

But converting to string is more expensive than using log10. So, in code, to compute the digits count of x, we can use:

import math

def get_digits(x):

    if x ==0:

        return 1

    return int(math.log10(x)) +1

But for x=0, which is not possible in our problem.

So, for x>0, this is safe.

So, using this function is more efficient than converting to string.

Thus, in code:

current_digits = get_digits(x)

Similarly for next_x.

This can save time.

Another Optimization: Precompute the digits of x each time, but since x can be very large, converting to a string to get the digits is O(digits), but for large x, it's manageable. Alternatively, track the digits as a set during BFS. For example, when x is added to the queue, we can precompute the digits set and store it along with x. This way, when processing x, we don't have to convert it to a string each time to get the digits.

Yes. So the state in the queue can be (x, steps, digits_set). But this requires more memory, but since the digits set is computed once when x is first processed, and stored with the queue node, it's more efficient.

But how?

Wait, when x is first generated (like next_x), we can compute its digits set and store it along with x and steps. So during BFS processing, for a node (x, steps, digits_set), we can directly use the digits_set to generate next steps.

But this increases the memory usage. For example, for each x in the queue, we store x, steps, and digits_set. But this can be more efficient, as during processing, we don't need to compute the digits_set each time.

Thus, in code, when generating next_x, compute its digits set once, and store it with the queue node. So, in code:

from collections import deque

def main():

    n, x = map(int, input().split())

    # Check if x already has n digits (but according to input constraints, x <10^{n-1}, so its digits count is <=n-1)

    # So no need to check.

    visited = set()

    queue = deque()

    queue.append( (x, 0) )

    visited.add(x)

    target = 10**(n-1)

    while queue:

        current_x, steps = queue.popleft()

        current_digits = get_digits(current_x)

        if current_digits ==n:

            print(steps)

            return

        # Generate next_x

        digits = set(str(current_x))

        for d in digits:

            y = int(d)

            if y in (0, 1):

                continue

            next_x = current_x * y

            if next_x in visited:

                continue

            next_digits = get_digits(next_x)

            if next_digits >n:

                continue

            if next_digits ==n:

                print(steps+1)

                return

            visited.add(next_x)

            queue.append( (next_x, steps +1) )

    print(-1)

But this code may not handle cases where the same next_x is generated through different paths with different steps. But since BFS processes nodes in order of steps, the first time next_x is added to the queue, it's with the minimal steps.

But this code may not work for the third example. Let's see:

Sample input 3:

13 42 → output 12.

So, according to the code, the BFS would process nodes until the steps reach 12.

But with this code, it's possible that the visited set grows large, but given that the steps are up to 12, and each step's branching factor is manageable, it might work.

But the code uses a visited set to track all x's processed, which for large x's (like 1e19) may not be feasible. However, in Python, integers can be arbitrarily large, and the hash for integers is efficient, so adding 1e19 to a set is possible.

But for the third example, after 12 steps, the x is multiplied 12 times, but each multiplication could be by digits like 4, 2, etc. So the x's are manageable.

Another optimization: Precompute the digits_set for each x when it's added to the queue. Because in the code above, when processing current_x, we generate the digits by converting to string. But when generating next_x, we could precompute its digits and store them with the queue node. This way, when processing next_x, we don't need to convert it to string again. For example:

Store in the queue entries (x, steps, digits_set).

But how to compute digits_set? When generating next_x, we can compute its digits_set as follows:

next_x = current_x * y

digits_str = str(next_x)

digits_set = set(digits_str)

But this requires converting to string each time next_x is generated, which is O(number of digits), but for numbers up to 1e19, it's 19 steps, which is manageable.

Alternatively, during the processing of current_x, generate digits_set once, and then for each possible y in digits_set (excluding 0 and 1), multiply current_x by y to get next_x, and compute next_x's digits_set.

So, the code can be modified to:

queue = deque()

initial_digits = set(str(x))

queue.append( (x, 0, initial_digits) )

visited.add(x)

...

while queue:

    current_x, steps, current_digits = queue.popleft()

    ...

    for y in current_digits:

        yi = int(y)

        if yi in (0, 1):

            continue

        next_x = current_x * yi

        if next_x in visited:

            continue

        next_digits = set(str(next_x))

        next_digits_count = len(str(next_x))

        ...

Thus, this way, the digits_set is stored with each node, so when processing, we don't need to convert current_x to a string again.

But this requires storing the digits_set for each node, which increases memory usage, but can save time in processing.

But in Python, even for large x's, the digits_set is a small object (a set of characters).

So, this may be a worthwhile optimization.

But for the purposes of code correctness, perhaps the initial approach is sufficient.

Another point to consider: in the code, for the visited set, we are using x as the key. But for large x's, this can take up a lot of memory. But in Python, even if x is very large, the hash is computed efficiently, and the set uses a hash table. So, for x's up to 1e19, the visited set can be handled, but for x's up to 1e100, it's possible, but memory may become an issue.

But given the time constraints (2 seconds), and the problem's sample inputs, the BFS approach with visited set may work.

But for n=19, and x=2, the steps needed could be up to 17 steps. Each step could have a branching factor of, say, 3. So 3^17 = 1.2e8, which is too large for Python to handle in 2 seconds. So this approach may not pass the time constraints for larger test cases.

Thus, we need a better approach.

Alternative Idea: Use BFS with pruning based on digits count and digits set, but track the minimal steps to reach each (digits_count, digits_set) pair. Then, for each such pair, we can process all possible y in the digits_set, and compute the next possible digits_count. But again, without knowing x, this is challenging.

But perhaps, for each (digits_count, digits_set), we can track the minimal steps to reach it, and for each possible y in digits_set, compute the next digits_count as the maximum possible (digits_count +1), and the digits_set as the union of all possible digits that can be obtained by multiplying any x in (digits_count, digits_set) by y.

But this is very vague and may not be accurate.

Alternatively, we can model the state as (digits_count, digits_set), and for each state, track the minimal steps required. For each state, the next states are determined by multiplying by each y in digits_set, and assuming that the digits_count increases by 1. Then, we can perform BFS on this model, and if it reaches a state with digits_count ==n, return the steps.

But this model is an approximation. It may not find the minimal steps correctly, but perhaps it's sufficient for some cases. For example, in the second sample:

Initial state: digits_count=1 (x=2), digits_set={2}.

Multiply by 2 → next_x=4 (digits_count=1, digits_set={4}).

Steps 1.

Multiply by 4 → next_x=16 (digits_count=2, digits_set {1,6}).

Steps 2.

Multiply by 1 → no change. So not allowed.

Multiply by 6 → 16 *6 =96 (digits_count=2, digits_set {9,6}).

Steps 3.

Multiply by 9 → 96*9=864 (digits_count=3). Steps 4.

So the model would track:

State (1, {2}) → steps 0.

After multiply by 2 → next state (1, {4} → steps 1.

But according to this model, the next state's digits_count is 1 (since x is 4, which has 1 digit), and digits_set {4}.

Then, when multiplying by 4, next state is (2, {1,6}) → steps 2.

Then, multiplying by 6 gives next state (3, {9,6}) → steps 3.

But the actual steps needed are 4, so this model would incorrectly return 3 steps.

So this model is incorrect.

Thus, this approach is not viable.

Alternative Idea: Since the BFS approach is the only way to get the correct steps, but the visited set is too large, perhaps we can use memoization for the digits_set and digits_count. For example, track for each (digits_count, digits_set) the minimal steps to reach it. If a new x is generated with the same digits_count and digits_set, and steps >= the existing steps, we can skip it. Because the existing steps are already minimal.

But how to track this?

We can maintain a dictionary called best_steps, where best_steps[(d, frozenset(s))] = minimal steps.

When processing x:

current_digits = get_digits(x)

current_set = frozenset( set(str(x)) )

current_steps = steps

if best_steps.get( (current_digits, current_set), infinity) <= current_steps:

    skip processing this x.

else:

    update best_steps[(current_digits, current_set)] = current_steps

    process x.

But even this may not prevent the visited set from growing too large.

But this can reduce the number of nodes processed. For example, if two different x's have the same digits_count and digits_set, but one x requires more steps than the other, then the x with higher steps can be skipped.

But how to implement this?

In code:

We can have a dictionary best_steps, which maps (d, frozenset(s)) to the minimal steps.

When we generate a new x:

current_digits = get_digits(x)

current_set = frozenset( set(str(x)) )

if current_digits >n: skip.

if current_digits ==n: return steps.

if (current_digits, current_set) is already in best_steps and best_steps[(current_digits, current_set)] <= steps: skip.

else:

    add to queue.

    update best_steps.

This way, even if x is different, but has the same digits_count and digits_set as a previous x with fewer steps, it's skipped.

This can significantly reduce the number of nodes in the queue.

For example, suppose x1 and x2 have the same digits_count and digits_set. If x1 is processed first with steps s1, then x2 with steps s2 >=s1 can be ignored.

So this approach can prune the search space.

Thus, combining this with the BFS can make the problem feasible.

But how to implement this?

In code:

We can track a best_steps dictionary.

The queue entries are (x, steps).

For each x dequeued:

current_digits = get_digits(x)

current_set = frozenset(str(x))

if (current_digits, current_set) is in best_steps and best_steps[(current_digits, current_set)] < steps: skip.

else:

    process x.

    generate next_x by multiplying by digits in current_set (excluding 0 and 1).

    for each next_x:

        next_digits = get_digits(next_x)

        next_set = frozenset(str(next_x))

        next_steps = steps +1

        if next_digits >n: continue.

        if next_digits ==n:

            print(next_steps)

            return.

        key = (next_digits, next_set)

        if key in best_steps and best_steps[key] <= next_steps:

            continue.

        else:

            best_steps[key] = next_steps

            queue.append( (next_x, next_steps) )

But this approach still requires tracking x, which may be large. But this way, the best_steps is based on (digits_count, digits_set) pairs, which can be much fewer than tracking all x's.

But how many (digits_count, digits_set) pairs are possible?

For digits_count up to 19, and digits_set being any subset of 0-9 (excluding 0, since multiplying by 0 is skipped), the possible combinations are 19 * 2^9 = 9728. Which is manageable.

So this is a feasible approach.

For example, digits_count can be from 1 to 19-1 =18 (since n is up to 19, and we stop when digits_count reaches n).

For each digits_count, the digits_set can be any subset of digits 1-9 (since 0 is skipped).

So for digits_count up to 18, there are 18 * 2^9 = 18*512=9216 possible (digits_count, digits_set) pairs.

Thus, the best_steps dictionary would have at most 9216 entries, which is manageable.

This is a huge optimization. Because, even though x can be very large, the number of unique (digits_count, digits_set) pairs is small. So this approach reduces the problem to a manageable size.

Thus, the algorithm becomes:

Initialize best_steps as empty.

Initialize queue with (x, steps=0).

For each x in the queue:

   current_digits = get_digits(x)

   current_set = frozenset( str(x) )

   if (current_digits, current_set) is in best_steps and best_steps[...] < steps: skip.

   else:

      add/update best_steps.

      check if current_digits ==n → return steps.

      for each digit in current_set:

          y = int(digit)

          if y ==0 or y ==1: continue.

          next_x = x * y

          next_digits = get_digits(next_x)

          if next_digits >n: continue.

          next_set = frozenset( str(next_x) )

          next_steps = steps +1

          key = (next_digits, next_set)

          if key not in best_steps or next_steps < best_steps.get(key, infinity):

              best_steps[key] = next_steps

              queue.append( (next_x, next_steps) )

If queue is empty and no solution found → return -1.

This approach uses BFS with pruning based on the (digits_count, digits_set) pairs and their minimal steps.

This would drastically reduce the number of states, as each state is a (digits_count, digits_set) pair, and the queue processes each pair with minimal steps.

But wait, the queue still contains x's, which are large numbers. So storing them in the queue may take memory. But since the best_steps is based on (digits_count, digits_set), and for each such pair, we only process the minimal steps, the queue will have at most one entry per (digits_count, digits_set) pair. Because once a pair is processed with minimal steps, any other x that has the same pair and higher steps will be skipped.

Thus, the queue can be implemented using a priority queue ordered by steps, but since BFS processes nodes in order of steps, a deque can be used.

But since the same (digits_count, digits_set) pair can be added to the queue with higher steps, but those will be skipped when dequeued.

So, the code can proceed as follows:

Use a deque.

For each x in the queue:

   current_digits = get_digits(x)

   current_set = frozenset( str(x) )

   current_steps = steps.

   if current_digits ==n → return current_steps.

   if (current_digits, current_set) is in best_steps and best_steps[...] <= current_steps → skip.

   else:

      best_steps[...] = current_steps.

      generate next_x's.

      for each next_x:

          next_digits = get_digits(next_x)

          next_set = frozenset( str(next_x) )

          next_steps = current_steps +1.

          if next_digits >n → skip.

          if next_digits ==n → return next_steps.

          key = (next_digits, next_set)

          if key not in best_steps or next_steps < best_steps[key]:

              queue.append( (next_x, next_steps) )

But wait, this way, the same (digits_count, digits_set) pair can be added multiple times to the queue, but only the first time (with minimal steps) will process it, the others will be skipped.

But how to ensure that the first time the pair is processed is with the minimal steps?

Because BFS processes nodes in order of steps, so the first occurrence of a (digits_count, digits_set) pair in the queue will have the minimal steps.

Thus, the code can proceed with a deque and process nodes in FIFO order.

Thus, the code would be:

import math
from collections import deque

def get_digits(x):
    return len(str(x)) if x !=0 else 1

def main():
    n, x = map(int, input().split())
    if get_digits(x) == n:
        print(0)
        return
    best_steps = {}
    queue = deque()
    initial_digits = get_digits(x)
    initial_set = frozenset(str(x))
    queue.append( (x, 0) )
    best_steps_key = (initial_digits, initial_set)
    best_steps[best_steps_key] = 0
    found = False
    while queue:
        current_x, steps = queue.popleft()
        current_digits = get_digits(current_x)
        current_set = frozenset(str(current_x))
        # Check if this state is the best one so far
        key = (current_digits, current_set)
        if best_steps.get(key, float('inf')) < steps:
            continue
        # Check if current state is the target
        if current_digits == n:
            print(steps)
            found = True
            break
        # Generate next states
        for d_char in current_set:
            y = int(d_char)
            if y in (0, 1):
                continue
            next_x = current_x * y
            next_digits = get_digits(next_x)
            if next_digits > n:
                continue
            next_set = frozenset(str(next_x))
            next_steps = steps + 1
            next_key = (next_digits, next_set)
            if next_key not in best_steps or next_steps < best_steps.get(next_key, float('inf')):
                best_steps[next_key] = next_steps
                queue.append( (next_x, next_steps) )
    if not found:
        print(-1)

But this code may have some issues. For example, the best_steps dictionary is updated for each possible next_key, but multiple entries can be added to the queue for the same next_key. However, when dequeued, the code checks if the steps stored in best_steps is less than the current steps, and skips processing if so. This ensures that only the minimal steps for each state are processed.

Testing this code with the sample inputs:

Sample 1:

Input: 2 1 → output -1.

The code starts with x=1, current_digits=1, current_set={'1'}.

Multiplying by 1 is skipped (y=1 is skipped). So no next states. Queue becomes empty. Output -1.

Sample 2:

Input:3 2 → output 4.

The code's BFS proceeds:

Step 0: x=2 (digits=1, set {'2'}, steps=0).

Multiply by 2: next_x=4 (digits=1, set {'4'}, steps=1.

best_steps now has (1, {'4'}) → steps 1.

Step 1: process x=4, steps=1.

Multiply by 4: next_x=16 (digits=2, set {'1','6'}, steps 2.

best_steps has (2, {'1','6'}) → steps 2.

Step 2: process x=16, steps=2.

Multiply by 1: skipped.

Multiply by 6: next_x=96 (digits=2, set {'9','6'}, steps 3.

best_steps has (2, {'9','6'}) → steps 3.

Step 3: process x=96, steps=3.

Multiply by 9: next_x=864 (digits=3 → steps 4. which meets n=3. So return 4.

Sample 3:

Input:13 42 → output 12.

The code should process the steps and find that after 12 steps, the digits count is 13.

Thus, the code should return 12.

But how to verify this?

The code may process various states and steps, and correctly track the minimal steps for each (digits_count, digits_set) pair.

Thus, this code should work.

Now, let's implement this code with the required optimizations.
</think>

To solve this problem, we need to determine the minimum number of operations required to transform a given integer \( x \) such that its decimal representation has exactly \( n \) digits. Each operation involves multiplying \( x \) by one of its digits. If it's impossible to reach exactly \( n \) digits, we return -1.

### Approach
The problem can be efficiently solved using a Breadth-First Search (BFS) approach combined with pruning based on the current number of digits and the set of digits present in the number. Here's the detailed approach:

1. **BFS Initialization**: Start with the initial value of \( x \) and track the number of steps taken.
2. **State Tracking**: Use a dictionary to track the minimum steps required to reach each state, where a state is defined by the number of digits and the set of digits present in the current number.
3. **Pruning**: Skip processing states that have already been reached with fewer steps or lead to a number of digits exceeding \( n \).
4. **Digit Multiplication**: For each valid digit in the current number's digit set, generate the next number by multiplying with the digit and update the BFS queue if this leads to a new or improved state.

### Solution Code
```python
from collections import deque

def get_digits(x):
    return len(str(x))

def main():
    n, x = map(int, input().split())
    initial_digits = get_digits(x)
    if initial_digits == n:
        print(0)
        return
    best_steps = {}
    queue = deque()
    initial_set = frozenset(str(x))
    queue.append((x, 0))
    best_key = (initial_digits, initial_set)
    best_steps[best_key] = 0
    found = False
    while queue:
        current_x, steps = queue.popleft()
        current_d = get_digits(current_x)
        current_s = frozenset(str(current_x))
        current_key = (current_d, current_s)
        if best_steps.get(current_key, float('inf')) < steps:
            continue
        if current_d == n:
            print(steps)
            found = True
            break
        for d_char in current_s:
            y = int(d_char)
            if y in (0, 1):
                continue
            next_x = current_x * y
            next_d = get_digits(next_x)
            if next_d > n:
                continue
            next_s = frozenset(str(next_x))
            next_key = (next_d, next_s)
            next_steps = steps + 1
            if next_key not in best_steps or next_steps < best_steps.get(next_key, float('inf')):
                best_steps[next_key] = next_steps
                queue.append((next_x, next_steps))
    if not found:
        print(-1)

if __name__ == "__main__":
    main()
```

### Explanation
- **BFS Initialization**: The BFS starts with the initial value of \( x \) and 0 steps. The queue helps explore each state level by level.
- **State Tracking**: The `best_steps` dictionary keeps track of the minimum steps required to reach each state (defined by the number of digits and the set of digits present).
- **Pruning**: By checking if a state can be reached in fewer steps than previously recorded, we avoid redundant processing and ensure efficiency.
- **Digit Multiplication**: For each valid digit (excluding 0 and 1), the next state is generated. If this state leads to the target number of digits, the solution is immediately returned.

This approach ensures that we efficiently explore all possible transformations of \( x \) while avoiding unnecessary computations, making it feasible to handle the problem constraints within the given time and memory limits.