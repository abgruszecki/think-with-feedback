<think>
Okay, let's tackle this problem. So the task is to determine if there's a non-empty subsequence of the given array whose sum is divisible by m. Hmm. Let's think about the possible approaches.

First, the constraints. The n can be up to 1e6 and m up to 1e3. So any O(n^2) approach is definitely out of the question. We need something efficient, probably linear or O(m^2) time.

Wait, what's the key here? The sum modulo m. Because if the sum of some subset is congruent to 0 mod m, then that's our answer. So maybe using the pigeonhole principle here. Like, if n >= m, then by the pigeonhole principle, there must be a subset whose sum mod m is zero. Wait, is that true? Let me think. Because the prefix sums modulo m. If any prefix sum is 0 mod m, then the subset up to that point is the answer. Otherwise, with n >= m, there are m possible remainders (from 1 to m-1), so if there are m+1 elements, two of them must have the same remainder, so the difference between those two prefix sums would be divisible by m. Wait, but the problem allows any subsequence, not just consecutive elements. So maybe the pigeonhole applies here differently.

Wait, but in the case where n >= m, there's a theorem called Erdős–Ginzburg–Ziv theorem which states that any 2m-1 integers have a subset of m integers whose sum is divisible by m. But in our problem, we can choose any non-empty subset. So if n >= m, then according to the theorem, the answer is definitely yes. Wait, but the theorem requires 2m-1 elements. Hmm. So maybe if n >= m, the answer is yes? Wait, maybe not. Wait, the Erdős–Ginzburg–Ziv theorem says that for any 2m-1 integers, there exists a subset of m integers whose sum is divisible by m. So if the original array has n >= m, but perhaps n is m, but the elements are all 0s mod m, except for some, maybe not. Wait, maybe not. So perhaps the pigeonhole approach isn't directly applicable here.

Alternatively, let's think about the problem. For the case where n >= m, even if all elements are 1 mod m, then after m elements, the sum would be m mod m, which is 0. So yes. Wait, that's correct. Because if any element is 0 mod m, then that's the subset. Otherwise, if there are m elements, all non-zero mod m. Then the possible sums of the first k elements (for k from 1 to m) mod m. If any of these is 0 mod m, then yes. Otherwise, by the pigeonhole principle, there are m sums and m possible remainders (1 to m-1, and 0). Wait, but if we have m elements, then the number of prefix sums (summing first 1, first 2, ..., first m elements) is m. So if none of them is 0 mod m, then among these m sums, there are m remainders (but possible 0). Wait, no. Because if any of the prefix sums is 0 mod m, then we have a solution. So if after m elements, none of the prefix sums is 0 mod m, then the m prefix sums must have all non-zero remainders. But there are m-1 possible non-zero remainders. So by pigeonhole, two of them must have the same remainder. The difference between those two would be a consecutive subset whose sum is 0 mod m. So in that case, there exists a consecutive subset (but the problem allows any subsequence). So even then, there's a solution. Wait, but the problem allows any subsequence, but in this case, the consecutive subset is a valid subsequence. So if n >= m, then the answer is always yes. Because either there's a prefix sum that's 0 mod m, or there's two prefix sums with the same remainder, and their difference is a subset sum that's 0 mod m.

So for n >= m, the answer is YES. That's a key insight. So for the problem, if the given n is >= m, then we can immediately return YES. Otherwise, if n < m, then we need to check if any subset of the array has a sum divisible by m. Because when n is less than m, the pigeonhole approach might not work. For example, if n is 5 and m is 6. Then we can't apply the same logic.

So the approach is: if n >= m, return YES. Else, check all possible subsets (since n is up to 1e3 when m is 1e3, but wait, in this case, when n is up to 1e6, but m is up to 1e3. Wait, no. Because when n >= m, the answer is YES. So the case when n < m, the maximum n can be up to m-1, which is 1e3-1. So even if n is 1e3, checking all possible subsets for sum mod m is manageable via dynamic programming. Because the DP approach can track possible remainders with O(m) space and O(n*m) time. Since n is up to 1e3 and m up to 1e3, 1e6 operations are manageable.

So the plan is:

1. Check if n >= m: if yes, output YES.

2. Else, check if there's a subset of the elements (non-empty) whose sum is divisible by m. For this, we can use a dynamic programming approach where we track possible remainders as we process each element.

So, steps:

First, read n and m. Then read the array. If any element in the array is 0 mod m, then immediately return YES. Otherwise, if n >= m, return YES. Else, proceed with the DP approach.

Wait, but even in the case where n >= m, there might be elements that are 0 mod m. So in that case, the answer is already YES. So maybe first check if any element is 0 mod m. If yes, output YES. Then check if n >= m. If yes, output YES. Else, proceed with DP.

But checking for any element 0 mod m is O(n), which is acceptable.

So the algorithm steps:

Check if any element in the array is divisible by m. If yes, return YES.

Else, if n >= m, return YES.

Else, use dynamic programming to check all possible subsets.

The DP approach works as follows:

We can track possible remainders after adding elements. For each element a_i, we can consider adding it to existing subsets. The possible remainders are from 0 to m-1.

Initialize a boolean array dp of size m, where dp[r] is True if there's a subset with sum congruent to r mod m.

Initially, dp is all False. Then for each element a_i, compute its mod m (call it rem). Then, for each existing remainder in dp, we can create new remainders (existing_rem + rem) mod m. Also, we can take the element by itself (rem). So for each step, we can update a new_dp array.

But since the elements can be processed one by one, here's how to handle it:

Initially, the possible remainders are empty. For the first element, the possible remainders are rem. Then for each subsequent element, we take all previous remainders and combine them with the new rem. Also, adding the new rem by itself.

But the DP approach can be implemented efficiently by using a set to track current possible remainders. For each element, we compute the new possible remainders by adding the current element's remainder to each existing remainder and taking mod m, and also including the current element's remainder. Then, check if 0 is in the set. If yes, return YES. Otherwise, proceed.

But with m up to 1e3, and n up to 1e3 (since for n < m and m up to 1e3), this approach is O(n*m) time, which is acceptable.

So here's the plan:

- Iterate over all elements, check if any is 0 mod m. If yes, output YES.

- Else, if n >= m, output YES.

- Else, process the elements using a set to track possible remainders. For each element, compute its remainder. For each remainder in the existing set, add (existing_remainder + current_rem) mod m to a new set. Also, add the current_rem. Then, check if 0 is present. If yes, return YES. Otherwise, update the set with the new remainders.

But to optimize this, we can use a list (array) of booleans. Because the possible remainders are up to m-1, we can track them in a list. For each step, we create a new array indicating possible remainders after considering the current element. However, this can be optimized by using a bitmask or a set.

Let's see. Let's use a dynamic programming array where dp is a set of current possible remainders.

Initialize dp as an empty set.

For each a in the array:

    rem = a % m

    if rem == 0:  # but we already checked this earlier, so perhaps this is redundant
        return YES

    new_rem = set()
    new_rem.add(rem)
    for r in dp:
        nr = (r + rem) % m
        new_rem.add(nr)
    if 0 in new_rem:
        return YES
    dp = dp.union(new_rem)

If after processing all elements, 0 is not found, return NO.

But this approach can be optimized by using a list (array) of booleans. Let's say we have a boolean array of size m, where each index represents a remainder. Initially, the array is all False. Then, for each element, we compute rem, and for each possible remainder in the current array, we mark (rem + current_remainder) mod m as possible.

But since the order of processing can affect this, perhaps a better way is to use a temporary array to track the new possibilities. For each element, we can create a new array temp, which is a copy of the existing dp array. Then, for each possible remainder in the existing dp, we add the current rem and mark the new remainder. Then, we OR the temp array with the existing dp.

Wait, perhaps using a bitmask approach. Let's represent possible remainders as bits in an integer. For example, if m is 5, then the bits 0-4 are possible. Then, for each element, the new remainders are (existing_remainder + current_rem) mod m, and current_rem itself. So the new bitmask is the OR of (current_bitmask << rem) | (1 << rem) | ... ?

Alternatively, perhaps using a list of booleans, and for each step, we iterate through the current list and mark new remainders. Here's the approach:

Initialize a dp array of size m, all False. Then, for each element a in the array:

    rem = a % m
    if rem == 0:
        return YES
    # Create a copy of the current dp
    temp = dp.copy()
    # Add the current remainder itself
    if not temp[rem]:
        temp[rem] = True
        if rem == 0:
            return YES
    # For each existing remainder in the previous dp, add (r + rem) mod m
    for r in range(m):
        if dp[r]:
            new_r = (r + rem) % m
            if not temp[new_r]:
                temp[new_r] = True
                if new_r == 0:
                    return YES
    dp = temp.copy()

After processing all elements, if dp[0] is True, return YES else NO.

But this approach is O(n*m), which is acceptable when n is up to 1e3 and m up to 1e3 (so 1e6 operations). So for the problem, this is manageable.

So, putting it all together:

Read n and m.

Read the array a.

Check if any element in a is 0 mod m. If yes, output YES.

Else, if n >= m, output YES.

Else, process the array using the dynamic programming approach as described.

This covers all cases.

Now, let's test this against the examples.

First example:

3 5

1 2 3.

Check if any element is 0 mod 5. 1,2,3: no. Then n=3 <5. Proceed to DP.

Processing 1:

rem = 1. DP becomes [False, True, False, False, False]. Check if 0 is in? No.

Processing 2:

rem is 2. For existing r=1, new_r is (1+2)=3. So new remainders are 2 and 3. Check if any is 0: no.

Processing 3: rem is 3. Existing remainders are 1, 2, 3. Adding 3:

current elements: 3. Then for each existing remainder (1, 2, 3), add 3 mod 5.

For 1: 1+3=4. For 2: 2+3=5 mod5=0. So when processing 3, when new_r is 0, we return YES.

So the code would return YES here.

Second example:

1 6

5. Check 5 mod6 is 5. n=1 <6. DP step: rem is 5. Check if 5 is 0? No. So DP after processing is [False, False, False, False, False, True]. No 0. Output NO.

Third example:

4 6

3 1 1 3.

Check if any element is 0 mod6. 3 mod6=3, 1, etc. No. n=4 <6. So DP.

Process 3 mod6=3. DP[3] = True. Not 0.

Process 1: rem=1. Add 1. Then for existing 3, 3+1=4 mod6. So new remainders are 1,3,4. None is 0.

Process next 1: rem=1. Existing remainders are 1,3,4.

Add 1: new remainder 1. For existing:

1+1=2, 3+1=4, 4+1=5. So new remainders are 1,2,3,4,5. Check if any is 0? No.

Process next 3: rem=3. Existing remainders are 1,2,3,4,5.

Add 3: new remainder 3. Then for existing:

1+3=4 mod6=4 (already exists).

2+3=5 mod6=5 (exists).

3+3=6 mod6=0. So new_r is 0. So return YES.

Hence, output is YES.

Fourth example:

6 6

5 5 5 5 5 5.

n=6 >= m=6. So output is YES.

So the code works for all test cases.

Now, the code implementation.

In Python, for the DP approach, we can use a list of booleans. But for handling the elements, each step, we need to make a copy of the current dp, then update the temp array with the new remainders.

But in Python, for each element, we can create a new set of possible remainders. Alternatively, using a bitmask (but for m up to 1e3, a list is manageable).

So code steps:

Read n, m.

Read the array as list of integers.

Check if any element mod m is 0. If yes, print YES and exit.

Else, if n >= m: print YES and exit.

Else, proceed with DP.

Initialize a list dp of size m, all False.

For each number in the array:

    rem = num % m

    if rem == 0:  # but we checked earlier, so this might not be needed here
        print("YES")
        exit()

    temp = [False] * m
    # Add the current rem to temp
    temp[rem] = True

    # Also, for all existing remainders in dp, add (r + rem) mod m
    for r in range(m):
        if dp[r]:
            new_r = (r + rem) % m
            temp[new_r] = True

    # Check if any new remainder is 0
    if temp[0]:
        print("YES")
        exit()

    # Update dp by OR-ing with temp
    for r in range(m):
        if temp[r]:
            dp[r] = True

    # Also, check if the current rem is 0 (but earlier check already handled this)

After processing all elements, check if dp[0] is True. If yes, output YES else NO.

Wait, but in the code above, after creating temp, which includes the new possible remainders from adding the current rem to existing ones and the current rem itself, we need to merge temp with the existing dp.

Wait, no. Because in the step where temp is created as the new possibilities from adding the current element. So temp is the possible remainders from the current element plus the existing remainders added with the current element. But wait, perhaps the code is not merging the previous dp with the new temp. Because in each iteration, the new possible remainders are the existing dp's remainders plus the current rem added to them, plus the current rem itself.

Wait, perhaps the code should create a new_temp that is the union of the existing dp and the new possibilities generated by adding the current rem to existing dp's remainders, as well as the current rem itself.

Wait, no. The approach is: when processing the current element, the new subsets that can be formed are either:

1. The subset consisting of just this element.

2. Any existing subset combined with this element.

So, the possible remainders after processing this element are the union of:

- The previous remainders (so existing subsets not including this element)

- The new remainders formed by adding this element to existing subsets (so (r + rem) mod m for each r in previous dp)

- The new remainder rem (the subset consisting of this element)

Wait, but this is not correct. Because the existing subsets (from previous steps) can be either kept (not including the current element) or combined with the current element (to form new subsets). So the new possible remainders are the previous dp's remainders (unchanged, since the subsets not including the current element) plus the new remainders (existing remainders + current rem mod m, plus the current rem mod m).

But in the code above, the code is considering the current element and the existing subsets. However, the code is not preserving the previous subsets. For example, if the previous dp had remainder r, then in the new dp, r is still possible (by not including the current element), and (r + rem) is possible (by including the current element). So the code should take the union of the previous dp and the new possibilities (current rem and existing remainders + rem).

But in the code above, when we process the current element, the code is creating temp as the new possibilities (current rem and existing + rem), and then merging those into the dp. But the code is not considering that the previous remainders are still possible (since you can choose to not take the current element). Wait, that's a problem.

Because in the code as written, the current approach overwrites the dp with temp. But that would lose the previous remainders, which are possible by not including the current element.

So this is a mistake. Oh right, because the code is supposed to track all possible remainders that can be formed by any subset up to the current element. So when processing the current element, the new remainders are either the ones from not including it (so the previous dp) or including it (the new possibilities). So the code should take the union of the previous dp and the new possibilities.

In other words, for each step, the new dp is the union of the previous dp and the new possibilities (rem and existing + rem).

So the code should:

- For each element, create a new_temp which is the union of:

   a) previous dp (subsets not including current element)

   b) new subsets formed by adding current element to previous subsets (existing_r + rem)

   c) the subset consisting of the current element (rem)

But that's equivalent to:

new_remainders = previous_dp_remainders U (previous_dp_remainders + rem) U {rem}

But in code, we can generate this as:

Initialize new_remainders as a copy of the current dp.

Then, for each r in current dp, add (r + rem) mod m to new_remainders.

Also, add rem mod m.

Wait, but the code should take the union. So the code should generate all possible remainders from existing subsets and the new subsets formed by adding the current element.

So the correct approach is:

new_remainders = existing_remainders | (existing_remainders + rem) | {rem}

But in code, how to represent this?

The code should:

For each element:

1. Compute rem = num % m.

2. If rem is 0, return YES.

3. Create a new set of remainders which includes all existing remainders, all (r + rem) mod m for existing remainders, and rem.

4. Check if 0 is in this new set. If yes, return YES.

5. Update the existing_remainders to be the new set.

But in the code above, the code is not considering the existing_remainders. Instead, in the code:

temp is the new possibilities (rem and existing_remainders + rem), but the code is setting dp to the OR of temp and existing dp. Wait, no.

Looking back at the code:

The code initializes temp as [False] * m. Then, for each r in dp, if dp[r] is True, then new_r is (r + rem) mod m, which is marked in temp. Also, temp[rem] is True.

Wait, no. The code does:

temp is initialized as [False] * m.

Then, temp[rem] is set to True (the subset consisting of current element alone).

Then, for each r in dp (i.e., where dp[r] is True), new_r is computed and temp[new_r] is set to True.

Then, the code checks if temp has 0. If yes, output YES.

Then, the code updates dp by OR-ing with temp. Wait, no. The code says:

for r in range(m):

    if temp[r]:

        dp[r] = True

So the code is merging the new possibilities (temp) into the existing dp. But this is incorrect, because the previous remainders (the existing dp) are not being preserved. Because the code is only adding the new possibilities from temp to the existing dp. But the existing subsets (those not including the current element) are already in the dp. So when the current element is processed, the new remainders are:

- All existing remainders (from subsets not including current element)

- All (existing_remainder + rem) mod m (subsets that include current element)

- rem (the subset consisting of current element)

So the code should merge the existing dp (before processing this element) with the new possibilities (temp). But in the code, the code is processing the existing dp (before the current element) to generate temp, which includes the new possibilities. Then, the code merges temp into dp. But the existing dp (before processing) is the same as the previous step's dp. So in the code, after processing each element, the dp includes all previous possibilities (the subsets not including current element) plus the new possibilities (subsets that do include current element). Wait, but in code, the code is not doing that. Let me see.

Suppose dp is initially [False, False, False]. Then, processing an element with rem=1:

temp is [False, True, False] (since temp[1] is set to True). Then, for each r in dp (which are all False), nothing is added. So temp remains [False, True, False]. Then, the code updates dp by setting each r in temp to True. So dp becomes [False, True, False]. Then, check if temp[0] is True (no). So proceed.

Next, process an element with rem=2. The existing dp is [False, True, False]. So temp is initialized as [False, False, True] (temp[2] is set to True). Then, for each r in existing dp (r=1 is True), compute new_r=1+2=3 mod m (assuming m=3), so new_r=0. So temp[0] is True. Then, the code checks if temp[0] is True, returns YES.

So the code works here.

But in this example, the code is correct. But what about when existing dp has some remainders, and the new possibilities are added. Because the code for each element is generating temp as the new possibilities (the subsets that include the current element), and then adding those possibilities to the existing dp.

Wait, the code's approach is:

After processing each element, the new dp is the union of the previous dp and the temp (the new possibilities generated by adding the current element). So the code is correct. Because the previous dp represents the subsets not including the current element, and the temp represents the subsets that do include the current element. So the union of these gives all possible subsets after processing this element.

Wait, no. Because the code is, for each element, generating the temp as the possible remainders when the current element is added to existing subsets (and also the current element alone). Then, the code merges the temp into the existing dp. So the new dp is the previous dp (not modified) plus the temp.

Wait, in the code:

The initial code is:

for each num in array:

    rem = num % m

    if rem ==0: return YES

    temp = [False]*m

    temp[rem] = True

    for r in range(m):

        if dp[r]:

            new_r = (r + rem) %m

            temp[new_r] = True

    if temp[0] is True: return YES

    for r in range(m):

        if temp[r]:

            dp[r] = True

So in this code, the temp is the new possible remainders when the current element is added to existing subsets (including the current element alone). Then, the code merges these temp remainders into the existing dp. So the existing dp (before processing the element) is the remainders possible by not including the current element. The temp is the remainders possible by including the current element (either alone or in combination with previous subsets). Then, merging temp into dp (by OR-ing) gives all possible remainders after processing the element (either subsets that include the element or not).

Wait, no. Because when you process the element, the existing dp is from before processing the element. The temp represents the subsets that include the element. So the new dp after processing the element is the union of the previous dp (subsets that don't include the element) and the temp (subsets that do include the element). So the code's approach is correct.

Yes. Because the previous dp (before processing the element) contains all possible remainders from subsets not including the current element. The temp contains all possible remainders from subsets that include the current element (either alone or in combination with previous subsets). So merging them (by setting dp[r] to True if either previous dp[r] or temp[r] is True) gives all possible remainders after processing the element.

So the code correctly updates the dp to include all possibilities.

Therefore, this approach is correct.

Now, the code in Python.

But for handling the array, since m can be up to 1e3, and n up to 1e3, it's manageable.

In Python, using a list of booleans:

n, m = map(int, input().split())

a = list(map(int, input().split()))

for num in a:

    if num % m == 0:

        print("YES")

        exit()

if n >= m:

    print("YES")

    exit()

# Now proceed with DP

dp = [False] * m

for num in a:

    rem = num % m

    # Since we already checked for 0 mod m, rem is not 0 here

    temp = [False] * m

    temp[rem] = True

    for r in range(m):

        if dp[r]:

            new_r = (r + rem) % m

            temp[new_r] = True

    if temp[0]:

        print("YES")

        exit()

    # Update dp by OR-ing with temp

    for r in range(m):

        if temp[r]:

            dp[r] = True

print("NO")

Wait, but this code may have a problem. For example, in the step where the temp is generated. For the first element, after creating temp, the code checks if temp[0] is True. If yes, returns YES. Else, updates the dp. So the code is correct.

But let's test the third example:

Input:

4 6

3 1 1 3.

The array after checking for 0 mod6 is all 3,1,1,3.

n=4 <6.

Processing first element: 3 mod6=3. temp is set to True for 3. Check temp[0] (no). Then update dp to [False, False, False, True, False, False].

Processing second element: 1 mod6=1.

temp is initialized to True for 1. Then, for each r in dp (r=3 is True). new_r = 3+1=4 mod6=4. So temp is 1 and 4. Check temp[0] (no). Update dp: set 1,3,4 to True.

Processing third element: 1 mod6=1.

temp is initialized to 1. Then, for each r in dp (1,3,4):

new_r for 1+1=2 mod6=2.

3+1=4 mod6=4.

4+1=5 mod6=5.

So temp is 1,2,4,5. Check if 0 is in temp (no). Update dp by adding these to current dp (1,3,4, 2,5). So dp now has 1,2,3,4,5.

Processing fourth element: 3 mod6=3.

temp is initialized to 3. Then, for each r in dp (1,2,3,4,5):

1+3=4 → temp[4] = True.

2+3=5 → temp[5] = True.

3+3=6 mod6=0 → temp[0] = True.

So when checking temp[0], it is True, so return YES.

Hence, code works.

So the code is correct.

But in the code, when processing each element, the temp is built as the new remainders generated by adding the current element to existing subsets (including the current element alone). Then, the code checks if any of those new remainders is 0. If yes, return YES. Otherwise, the code merges the new remainders into the dp.

This approach works because the new remainders (temp) are the ones generated by including the current element in some subset (either alone or with previous elements). However, the existing dp (before processing this element) is the set of remainders from subsets that do not include the current element. The code checks the temp for 0 because if any subset that includes the current element (and possibly previous elements) has a sum divisible by m, we can return YES immediately. Otherwise, after merging, the dp now includes all possible remainders (both those that include and exclude the current element).

Thus, the code is correct.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))

for num in a:
    if num % m == 0:
        print("YES")
        exit()

if n >= m:
    print("YES")
    exit()

dp = [False] * m
for num in a:
    rem = num % m
    temp = [False] * m
    temp[rem] = True
    for r in range(m):
        if dp[r]:
            new_r = (r + rem) % m
            temp[new_r] = True
    if temp[0]:
        print("YES")
        exit()
    for r in range(m):
        if temp[r]:
            dp[r] = True

print("NO")
```