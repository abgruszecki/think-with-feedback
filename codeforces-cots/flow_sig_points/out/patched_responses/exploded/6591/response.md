<think>
Okay, let's see. The problem is about arranging some light bulbs in a garland such that the complexity (number of adjacent pairs with different parity) is minimized. Some bulbs are missing (marked as 0), and we need to fill them in with the remaining numbers.

Hmm. So first, we need to figure out which numbers are missing. The initial array has some 0s which are the positions where bulbs are missing. The bulbs that are present are the non-zero values. So the missing numbers are all the numbers from 1 to n that are not present in the given array.

Once we have the missing numbers, we need to place them in the 0 positions such that the resulting arrangement has the minimal possible complexity.

But how to model this? The problem seems to require trying different possibilities, but with n up to 100, that's a lot. Wait, but the missing numbers could be up to n, which is 100. So the positions with 0s need to be filled with these numbers. So the problem is similar to permutation generation where we replace the 0s with the missing numbers in all possible orders and compute the complexity each time, then take the minimum.

But wait, the number of possible permutations could be factorial in the number of missing numbers. For example, if there are k missing numbers, then k! possibilities. If k is up to 100, that's impossible. So a brute-force approach is not feasible.

So we need a smarter approach. Let's think about dynamic programming. The state would need to capture the current position, the last parity (since the next choice's parity affects the current transition), and which numbers have been used.

Alternatively, since the missing numbers are a set, perhaps we can model the state based on which of them have been used so far and the last parity. But even that might be tricky.

Wait, the problem is that each 0 in the original array must be filled with a unique number from the missing set. So the missing numbers form a set S. The 0 positions are the places where these numbers must be placed. The order in which we place them in those positions affects the complexity.

So, the key is to model the problem as a permutation of the missing numbers, which are placed into the 0 positions. Each such permutation contributes to the complexity based on adjacent elements and their parities.

The challenge is to find the permutation that, when placed into the 0 positions, results in the minimal total complexity.

So the approach could be:

1. Determine the positions where the numbers are missing (the 0s) and the list of missing numbers (S).

2. Generate all possible permutations of S, place them into the 0 positions, compute the complexity, and take the minimum. But for S size up to 100, this is impossible. So this is only feasible for small S sizes.

Wait, but the constraints say n can be up to 100. If all numbers are missing (like the input array is all zeros), then S has 100 numbers. The permutations of 100 elements are way too many. So brute-force is impossible. So we need a dynamic programming approach that can handle this.

Alternative approach: model the problem in terms of the order in which the missing numbers are placed into the 0 positions, keeping track of the necessary state to compute the transitions.

Let's think about the dynamic programming approach. Let's process each position in order. For each position, if it's a fixed number (non-zero), then its parity is known. If it's a 0 (to be filled), then we need to choose a missing number that hasn't been used yet and track how that affects the transitions between parities.

But the problem is that the missing numbers can be placed in any order in the 0 positions, so the DP state must track which numbers have been used (as a bitmask) and the previous parity (to compute transitions with the next element). However, for n up to 100, the bitmask approach is impossible because 100 missing numbers would require a bitmask of 100 bits, which is way too big (2^100 states). So that's not feasible.

Hmm. So the DP state needs to track:

- The position in the array being processed.

- The previous element's parity (since the next element's parity affects the transition).

- Which missing numbers have been used so far.

But again, the "used" part is a problem when the missing numbers are many. So maybe we can find another way to model the state.

Wait, perhaps the order of the missing numbers in the 0 positions is important, but the parities of the numbers in those positions are what affects the transitions. So maybe the state can track the count of even and odd numbers used so far, along with the previous parity. But this would only work if the missing numbers have a certain count of even and odd. Wait, the missing numbers' parities are fixed. Because each number's parity is determined (even or odd). So for example, the set S (missing numbers) may have a certain number of even and odd numbers. When we place them into the 0 positions, each 0 can be filled with a number of a specific parity, but the actual selection of which even/odd number to use may not matter as long as the parity is correct. Because the exact number's parity is all that matters for the transitions.

Wait, this is a key insight. Suppose that in the missing numbers, there are 'e' even numbers and 'o' odd numbers. When filling the 0 positions, each 0 must be filled with an even or odd number (depending on what's left in S). But the exact choice of even or odd may not matter for the transitions between elements. So the DP can track the count of even and odd numbers left, along with the previous parity, and the current position.

But how do the 0 positions work? Let's think: the array is fixed except for the 0 positions. So the array is a sequence of fixed elements (non-zero) and variable elements (0s). So when processing the array, when we hit a fixed element, we just compute the transition between previous parity and its parity. When we hit a 0, we need to choose a parity (even or odd) from the remaining available in the missing numbers. Then, the next state would have that parity as the previous, and the count of evens and odds reduced accordingly.

But this would work only if, when we have to choose a parity for a 0, the number of even and odd numbers left allows that choice. For example, if there are 3 even numbers left, choosing even for the next 0 would decrease even count by 1.

But this model would ignore the actual numbers, but instead track the parity counts. However, this approach would only be valid if the order in which even and odd numbers are placed in the 0 positions doesn't affect the total complexity. Wait, but the exact positions of even and odd in the 0s can affect the transitions between adjacent elements. For example, the choice of even or odd in a 0 affects the transition between the previous element (fixed or another 0) and the next element (fixed or another 0).

So the DP state can model:

- The current position in the array.

- The previous parity (even or odd) that the next element's parity will be compared to.

- The number of even and odd missing numbers remaining.

So for each step:

- If the current position is a fixed number (non-zero), then its parity is known. The transition cost is 1 if the previous parity is different. Then proceed to the next position with the new previous parity.

- If the current position is a 0, then we have to choose between using an even or an odd (if available). For each possible choice (if possible), compute the cost (1 if previous parity is different from the chosen parity), then update the even and odd counts accordingly, and proceed to the next position with the chosen parity as the previous.

This seems feasible. The DP state is (pos, prev_parity, evens, odds), where evens and odds are the number of even and odd missing numbers left to place. The transitions are manageable.

The number of possible states would be:

- pos: up to n (100)

- prev_parity: 2 (even or odd)

- evens: up to the initial count of even missing numbers (say up to 100)

- odds: up to the initial count of odd missing numbers (up to 100)

So total states are 100 * 2 * (100) * (100) = 2,000,000. That's manageable for Python with memoization (using lru_cache or a memo table). But 100 * 100 is 10,000 for evens and odds, multiplied by 100*2 gives 2,000,000 states. For each state, transitions could be up to 2 options (even or odd, if available).

So this approach is feasible.

So the steps to solve the problem are:

1. Parse the input array.

2. Collect the existing numbers (non-zero) to find which numbers are missing.

3. Missing numbers are all numbers from 1 to n not present in the input array.

4. Compute the number of even and odd missing numbers (e and o).

5. Process the array, keeping track of the current position, the previous parity (from the previous element), and the remaining even and odd counts.

6. Use dynamic programming to compute the minimal total complexity.

But how to handle the initial state? The first element of the array can be a fixed number or a 0. Let's think:

At the start of processing, the previous parity is None (since there's no previous element). Wait, for the first element, there's no previous, so transitions start from the second element. So for the first element, when processing, the next elements (the second one) will compare to the first's parity.

Wait, the first element's parity will affect the transition to the second element, but the first element doesn't have a transition on its own. For example, the array has elements a1, a2, ..., an. The transitions are between a1 and a2, a2 and a3, etc. So the first element's parity is only used in the transition with a2.

So when processing the array, for each position i, the transition is between the previous element (i-1) and the current element (i). Wait, maybe it's easier to model the DP as moving through the array, and for each position, track the parity of the previous element (the one at position i-1). Then, when processing position i, we compute the transition between i-1 and i.

Wait, maybe the DP state should track the parity of the last element (the previous element) so that when processing the next element, we can compute the transition cost.

For example:

The DP state is (current position, last_parity, evens_left, odds_left). The current position is the index we are about to process. Wait, perhaps it's better to model the DP as follows:

We process the array from left to right. For each position i (from 0 to n-1), we need to know the parity of the element at i-1 (since the transition is between i-1 and i). So the state includes the parity of the previous element (i-1), and the counts of even and odd missing numbers left.

Wait, let's think of the array as being processed in order, and for each position i, after placing all numbers up to i, the next step is to process i+1. So the transitions are between consecutive elements.

So for example, when processing position i, the parity of the i-th element is known (either fixed or determined by the choice made in the 0 case). Then, when processing i+1, we compare the i-th parity with the (i+1)-th parity to determine if a transition is counted.

Wait, maybe the DP should track the parity of the current element (i-th), and when processing the next element (i+1), compute the transition cost between the current parity and the next element's parity.

Alternatively, perhaps the DP state represents that after processing the first k elements, the last element's parity is p, and there are e even and o odd numbers left. Then, when processing the (k+1)-th element, we can compute the transition cost between p and the next element's parity.

Yes, this makes sense.

So the DP state is (position k, last_parity, evens_left, odds_left).

The initial state is (position 0, None, e, o), since before processing any elements, there's no previous parity. But wait, the first element (position 0) has a parity that affects the transition between position 0 and 1. So when processing the first element (position 0), the transition between 0 and 1 depends on the parity of position 0 and position 1. So for the first element, we need to determine its parity, which affects the next transition.

Wait, the first element is either fixed (non-zero) or a 0. If it's fixed, its parity is known. If it's a 0, then we need to choose a parity (even or odd) based on the available evens and odds.

So, the DP approach would work as follows:

Start at position 0. For each position, if it's a fixed number, then its parity is known, and the next state's last_parity is this parity, and the even/odd counts are unchanged (since this number is already present, not part of the missing). If the position is a 0, then we have to choose between placing an even or odd (if available), which affects the even/odd counts and the next last_parity.

But how to model the transitions for each element. Let's think step by step.

For each state (k, last_p, e, o), where k is the current position (0-based, up to n-1), last_p is the parity of the element at position k (since we've processed up to k), and e and o are the remaining even and odd numbers to be placed.

Wait, no. Wait, the positions are 0 to n-1. We process each position in order. For each position i, we need to determine the parity of the element at i, and then compute the transition cost between i and i+1 (when i+1 is processed).

But how?

Alternative approach:

The transitions are between consecutive elements. For each pair of consecutive elements, we compare their parities and add 1 to the complexity if they differ.

So, the total complexity is the sum over i from 0 to n-2 of (parity[i] != parity[i+1]).

Thus, for the DP, we can model the state as (current index i, prev_parity, e_left, o_left), which represents that we have filled up to index i (inclusive), the parity of i is prev_parity, and have e_left even and o_left odd numbers left to place in the remaining 0 positions. The DP would then compute the minimal complexity for the remaining elements from i+1 onwards.

So, the recursive case would be:

At state (i, prev_p, e, o), for the next element i+1:

If the element at i+1 is fixed (non-zero), then its parity is known. The cost added is (prev_p != parity of this element). Then proceed to state (i+1, this_parity, e, o).

If the element at i+1 is 0, then we need to choose between placing an even or an odd (if available). For each possible choice (even or odd):

- If even is chosen (e > 0), the cost is (prev_p != even_parity (which is 0)), then proceed with e-1, new_prev_p is 0.

- Similarly for odd.

We take the minimal cost among all possible choices.

So the DP transitions are as follows.

The base case is when i == n-1. In this case, there are no more transitions, so the cost is 0.

So the DP would start from the first element (i=0) and track the state after processing up to i=0, then i=1, etc.

Wait, but for the first element (i=0), how do we model it? Let's see:

For i=0, the element is either fixed or a 0.

If fixed: its parity is known. The state after processing i=0 is (0, p, e, o), where p is the parity of the fixed element. Then, when processing i=1, the transition between i=0 and i=1 is considered.

If the element is 0: then we can choose between even or odd (if available), and the state after processing i=0 would be (0, chosen_p, e - (chosen_p is even), o - (chosen_p is odd)), and the transition to i=1 would use this chosen_p as prev_p.

But the initial state depends on the first element.

So the initial state is determined by the first element:

If the first element is fixed (non-zero):

Then, the initial state is (0, parity of first element, e, o), and the cost is 0 (since there's no previous element to compare to yet).

If the first element is 0:

Then, the initial choice is to place even (if e>0) or odd (if o>0), each of which leads to a different state with e and o decreased by 1, and the cost is 0 (since it's the first element).

Wait, but the cost is only added when comparing to the next element. So for the first element (i=0), there's no transition cost. The cost starts to be added when processing i=1 (the transition between i=0 and i=1).

So the DP needs to handle the first element correctly.

Putting it all together:

The DP will process each element in order. For each element i, after choosing its parity (if it's a 0), the next element's parity (i+1) will determine the transition cost.

The steps to implement this:

1. Preprocess the input array to find which elements are missing. Collect all existing numbers (non-zero), then the missing numbers are those not present. Then split them into even and odd counts (e and o).

2. For each position in the array, determine if it's fixed (non-zero) or a 0 (needs to be filled).

3. Implement a memoization-based DP function that tracks (i, prev_p, e, o) and returns the minimal cost from i to the end.

Now, let's outline the code structure.

First, parse the input:

n = int(input())
p = list(map(int, input().split()))

existing = set()
missing = []
for num in p:
    if num != 0:
        existing.add(num)
for num in range(1, n+1):
    if num not in existing:
        missing.append(num)

e = sum(1 for num in missing if num % 2 == 0)
o = len(missing) - e

But wait, the missing numbers are those not present in the array. So existing is the set of non-zero elements in p. Then, missing is [1..n] minus existing.

Yes.

Now, the positions in the array can be either fixed (non-zero) or 0. So for each position i, we can precompute whether it's a fixed value (and its parity) or a 0.

So for each i in 0..n-1:

if p[i] is non-zero:

    parity = p[i] % 2

else:

    needs to be filled with a missing number (even or odd)

So, the code can precompute a list where for each position, we know if it's fixed or not, and its parity (if fixed).

Then, the DP can process each position, considering whether it's fixed or a 0.

Now, the DP function.

We can use memoization, perhaps with lru_cache, but since the parameters are i (up to 100), prev_p (0 or 1), e (up to 100), o (up to 100), the number of states is manageable.

But in Python, using lru_cache for 2 million states may be possible, but recursion might hit stack limits. So perhaps an iterative DP approach is better.

Alternatively, use memoization with a helper function.

But for code simplicity, let's try to model it with memoization.

But in Python, for memoization with mutable parameters (like e and o), we need to make them as arguments. Wait, but in our case, the state is (i, prev_p, e, o). So for each state, the parameters are integers, which can be handled by the memoization decorator.

So, let's model the DP as follows:

Define a function dp(i, prev_p, e, o) that returns the minimal complexity for processing from position i onwards, given that the previous parity is prev_p, and we have e even and o odd numbers left.

The base case is when i == n. Then, there are no more transitions, so the cost is 0.

Wait, but the array has n elements. So when processing i from 0 to n-1, the transitions are between i and i+1. So for i == n-1, there is no next element. So the base case is when i == n-1, return 0.

So:

def dp(i, prev_p, e, o):

    if i == n-1:

        return 0

    current element is at position i+1 (wait, no: the current element is i. Wait, maybe I need to re-express the DP.)

Wait, perhaps the function is designed as follows: we have processed up to position i (inclusive), and need to process positions i+1 onwards. Then, when considering position i+1, the transition is between i and i+1.

Alternatively, perhaps the DP function is called with the current position (i) and the previous parity (from i-1). Then, for the current position i, we determine the parity (if fixed or 0) and compute the transition from the previous parity.

Hmm, maybe the initial approach was better. Let me think again.

Let's model the DP as follows:

We are at position i, and the previous parity (from position i-1) is prev_p. We need to process position i, determine its parity (based on fixed or missing), and compute the transition between i-1 and i. Then, proceed to process i+1.

Wait, but this would require the transition to be between i-1 and i. But how to model the first element, which has no previous.

Alternative approach: the DP state is (i, last_parity, e, o), where i is the current position (the one we are about to process). The 'last_parity' is the parity of the element at position i-1 (if i > 0). For i = 0, 'last_parity' is None, but when i is 0, the next element is 1. So the transition between 0 and 1 is between i=0 and i=1.

Hmm, perhaps this is getting complicated. Let's instead think of the array as being processed from left to right, and for each position i, after processing it, the next position is i+1.

For each position i, the state includes the parity of the i-th element (since that's needed for the transition to i+1), along with the counts of even and odd remaining numbers.

So, the DP state is (i, curr_p, e, o), where curr_p is the parity of the i-th element, and we need to compute transitions to i+1.

Wait, but how do we handle the transition between i and i+1?

The transition between i and i+1 depends on curr_p and the parity of i+1. So when processing i+1, we need to know the parity of i (curr_p) and then compute the cost of the transition.

So the DP function would be:

After placing the i-th element with parity curr_p, and having e and o remaining numbers, what's the minimal cost for the rest of the array.

So, the function would be:

def dp(i, curr_p, e, o):

    if i == n-1:

        return 0  # no more transitions

    next_element = array[i+1]

    if next_element is not zero:

        next_parity = next_element % 2

        cost = (curr_p != next_parity)

        return cost + dp(i+1, next_parity, e, o)

    else:

        # next_element is a 0, need to choose between even or odd

        min_cost = infinity

        # try even

        if e > 0:

            new_e = e - 1

            new_parity = 0

            cost = (curr_p != new_parity)

            res = cost + dp(i+1, new_parity, new_e, o)

            if res < min_cost:

                min_cost = res

        # try odd

        if o > 0:

            new_o = o - 1

            new_parity = 1

            cost = (curr_p != new_parity)

            res = cost + dp(i+1, new_parity, e, new_o)

            if res < min_cost:

                min_cost = res

        return min_cost

But wait, the next_element is the (i+1)-th position in the array. So when the (i+1)-th element is fixed (non-zero), its parity is known, and the function can proceed. If it's a zero, then the code must choose between even or odd (if available), and subtract accordingly from e or o.

But how to model the initial call?

The first element (i=0) can be fixed or zero.

If i=0 is fixed, then curr_p is its parity, and the DP starts at i=0, curr_p, e, o.

If i=0 is zero, then we have to choose between even and odd (if available), then proceed to i=1 with the new parity.

So the initial call depends on the first element:

If the first element is fixed:

    initial_parity = p[0] % 2

    answer = dp(0, initial_parity, e, o)

Else:

    min between choosing even (if e >0) and odd (if o>0) for the first element, and then proceed to i=1.

Wait, but the first element's parity affects the transition to the second element. So for i=0, after processing (placing the first element), the next element (i=1) is compared to the first.

But the initial call to DP must start at i=0, with the first element's parity known (if fixed) or chosen (if zero), and then proceed.

So the overall approach is:

- For each position in the array, check if it's fixed or zero.

- For the first element, if it's fixed, then the initial state is (i=0, curr_p, e, o), and the cost starts adding from the next element.

Wait, no. Because the transition between i=0 and i=1 is part of the total complexity.

But according to the DP function above, when processing i=0, the next element is i+1=1. The transition cost between i=0 and i=1 is computed as part of the DP.

So the initial call is to process the first element (i=0) and compute all transitions for the rest of the array.

But how?

Wait, the code would need to handle the first element's parity, whether fixed or chosen (if 0). Then, for the rest of the elements, the DP proceeds.

So the code would need to:

If the first element is fixed:

    curr_p = p[0] % 2

    call dp(0, curr_p, e, o)

Else:

    min between placing even (if possible) and odd (if possible).

Wait, but the first element is a 0. So in this case, the code has to choose even or odd, and the initial state is (i=0, chosen_p, e - (chosen_p is even), o - (chosen_p is odd)), and then call dp(0, chosen_p, new_e, new_o).

But according to the DP function, when i=0, the next element is i+1=1. So the transition between 0 and 1 is computed.

But the first element (i=0) is part of the array. The transition between 0 and 1 is part of the complexity. So the initial call must start with i=0 and curr_p being the parity of the first element.

So the initial code would have to handle the first element as follows:

If the first element is fixed:

    initial_parity = p[0] % 2

    total_cost = dp(0, initial_parity, e, o)

If the first element is 0:

    possible_choices = []

    if e > 0:

        new_e = e - 1

        new_o = o

        cost = 0  # no transition since it's the first element.

        # Then, the next element is i=1.

        # So the initial call would be:

        res = dp(0, 0, new_e, new_o)

        possible_choices.append(res)

    if o > 0:

        new_e = e

        new_o = o - 1

        res = dp(0, 1, new_e, new_o)

        possible_choices.append(res)

    if possible_choices:

        total_cost = min(possible_choices)

    else:

        # e and o are 0, but since the first element is 0 and we have missing numbers, this can't happen.

But wait, if the first element is 0, then it's part of the missing numbers. So in this case, the missing numbers must include the first element. So e + o is the number of missing numbers, which includes the first element. So when placing the first element, which is 0, e and o are the counts of even and odd in the missing numbers. So if the first element is 0, then e + o must be >=1. Because otherwise, the array would have no missing numbers, but the first element is 0 which is invalid. So the code can assume that if the first element is 0, then e + o >=1.

But how to handle the initial call when the first element is 0?

Wait, perhaps the code needs to process the entire array, starting with the first element, which may be fixed or 0.

So the code would first process the array from left to right. For each element, if it's fixed, use its parity. If it's 0, choose between even and odd (if available).

The problem is that the DP function needs to be called with the correct parameters, taking into account the choices made for the zeros.

But in the case where the first element is 0, we have to choose whether to place even or odd, which affects the remaining counts and the parity for the next transition.

So the code would need to handle the first element as a special case if it's a 0.

Alternatively, the DP function can be designed to handle all elements, including the first one.

Wait, let's think again.

The DP function is called as follows:

For each position i, after processing it (so the parity is known), and with e and o remaining even and odd numbers left, what is the minimal cost to process the remaining positions (i+1 to n-1).

In the first call, if the first element is fixed (i=0), then curr_p is its parity, and the function proceeds to i=0 (processing the next element i+1=1).

Wait, no. The function is called with i=0 and curr_p being the parity of the first element. Then, for the next element (i=1), we check if it's fixed or 0.

So the code would look something like this:

For each element in the array:

At position i, the current element's parity is curr_p (either fixed or chosen from even/odd if it's a 0).

The next element is i+1.

If the next element is fixed, then its parity is known, and the transition cost is added.

If the next element is 0, then choose even or odd (if available), subtract from e or o, and proceed.

But the initial call to the DP function starts at i=0 with the curr_p as the first element's parity.

Thus, the code can handle all elements, including the first, as part of the DP.

But for the first element, if it's a 0, then the code must choose between even and odd, which affects the e and o counts and the curr_p.

So the code would need to start by checking if the first element is 0. If so, the DP function is called with possible choices of even or odd (if available). If not, the DP function is called with the fixed parity.

So the main code would:

Process the array to find e and o (even and odd missing numbers).

Check the first element (position 0):

if p[0] is not zero:

    curr_p = p[0] % 2

    result = dp(0, curr_p, e, o)

else:

    possible_results = []

    if e > 0:

        possible_results.append(dp(0, 0, e-1, o))

    if o > 0:

        possible_results.append(dp(0, 1, e, o-1))

    result = min(possible_results) if possible_results else 0  # but this case can't happen since missing numbers exist

But how do we compute the transitions starting from i=0.

Wait, when the first element is a 0, and we choose to place even (for example), then the DP starts at i=0, curr_p=0. Then, the next element is i=1, and the transition between i=0 (curr_p=0) and i=1's parity is computed.

So the code seems correct.

Now, the DP function needs to process each position, considering the next element.

Let's outline the code for the DP function.

But since Python's recursion can be slow for 2 million states, perhaps memoization using lru_cache with maxsize set to a large number is feasible, but may require memoization of a function with parameters i, curr_p, e, o.

But in Python, integers can be up to any size, and lru_cache can handle that.

So the code would look something like this:

import sys
from functools import lru_cache

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

existing = set()
missing = []
for num in p:
    if num != 0:
        existing.add(num)
for num in range(1, n+1):
    if num not in existing:
        missing.append(num)

e = sum(1 for num in missing if num % 2 == 0)
o = len(missing) - e

# Precompute whether each position is fixed or zero, and their parity if fixed
is_fixed = []
parities = []
for num in p:
    if num == 0:
        is_fixed.append(False)
        parities.append(None)
    else:
        is_fixed.append(True)
        parities.append(num % 2)

@lru_cache(maxsize=None)
def dp(i, curr_p, e_left, o_left):
    if i == n - 1:
        return 0  # no next element
    next_i = i + 1
    if is_fixed[next_i]:
        next_p = parities[next_i]
        cost = 1 if (curr_p != next_p) else 0
        return cost + dp(next_i, next_p, e_left, o_left)
    else:
        # next_i is a zero; need to choose between even and odd
        min_cost = float('inf')
        # Try even
        if e_left > 0:
            new_e = e_left - 1
            new_p = 0
            cost = 1 if (curr_p != new_p) else 0
            res = cost + dp(next_i, new_p, new_e, o_left)
            if res < min_cost:
                min_cost = res
        # Try odd
        if o_left > 0:
            new_o = o_left - 1
            new_p = 1
            cost = 1 if (curr_p != new_p) else 0
            res = cost + dp(next_i, new_p, e_left, new_o)
            if res < min_cost:
                min_cost = res
        return min_cost

# Now handle the initial call
if not is_fixed[0]:
    # First element is 0, need to choose even or odd
    possible = []
    if e > 0:
        possible.append(dp(0, 0, e-1, o))
    if o > 0:
        possible.append(dp(0, 1, e, o-1))
    print(min(possible))
else:
    # First element is fixed
    initial_p = parities[0]
    print(dp(0, initial_p, e, o))

Wait, but this code has a problem. For example, the is_fixed and parities arrays are built for the entire array. For the next_i (i+1) position, when we are processing the next_i-th element, which is a zero, the code checks if is_fixed[next_i] is True. If it is, uses its parity. Otherwise, it's a zero and needs to choose even or odd.

But in the code above, the is_fixed array is built based on the original p array. So the code correctly identifies which positions are fixed (non-zero) and which are zeros.

But the code's DP function is designed to process the array positions in order. Let's test this logic with the first example.

First example input:

5

0 5 0 2 3

The array is [0,5,0,2,3]. The existing numbers are 5,2,3. Missing numbers are 1,4.

So e = 1 (4 is even), o=1 (1 is odd).

The code's is_fixed array for each position:

0: False (0), so handled by choosing even or odd.

But wait, in the original array, the first element is 0. So the code checks if the first element is fixed. If not, it starts by choosing even or odd.

Wait, according to the code:

For the first element (position 0), it's 0 (not fixed). So the code enters the else branch and tries choosing even (e=1) and odd (o=1). For each choice, it calls dp(0, chosen_p, e-1 or o-1, ...).

For example, if even is chosen (4), then curr_p is 0, and the next element is i=1 (which is fixed as 5, which is 1).

The code will call dp(0, 0, 0, 1). Then, processing next_i=1, which is fixed (5, parity 1). The transition cost between 0 and 1 is 1. Then, the next step is to call dp(1, 1, 0, 1). But next_i is 2 (third element, which is 0).

In that case, the code will need to process position 2 (next_i=2), which is a zero. So the code will try even or odd. But e_left is 0 (since we used the only even in the first step), so only odd (1) is left.

So for next_i=2 (position 2), the code chooses odd (parity 1). Transition cost between previous parity (1) and new_p (1) is 0. Then, proceed to next_i=3 (position 3), which is fixed (2, parity 0). Transition cost 1. Then next_i=4 (position 4, fixed 3, parity 1). Transition cost 1. Then i=4 is the last position, so return 0. The total cost is 1 (from 0 to 1) + 0 (1 to 1) + 1 (1 to 0) + 1 (0 to 1) = 3. But the sample output is 2. So this indicates a problem.

Wait, perhaps the code isn't considering all possible permutations. For example, in the first sample, the optimal arrangement is 1 5 4 2 3. Let's see the transitions:

1 (odd) and 5 (odd): no cost.

5 (odd) and 4 (even): cost 1.

4 (even) and 2 (even): no cost.

2 (even) and 3 (odd): cost 1.

Total: 2.

So the code's current approach would not find this arrangement. Because in the code's example, the first element (position 0) is filled with even (4), but the optimal solution uses odd (1) in position 0.

Ah, right. So in the first example, the code would try both options for the first element. Choosing odd (1) in position 0:

In this case, the code calls dp(0, 1, 1 (e=1, o=0). Wait, no. Original e is 1 (even missing is 4), o is 1 (odd missing is 1). So if the first element is chosen as odd (1), then o becomes 0, and e remains 1.

So initial call is dp(0, 1, e=1, o=0).

Then, next_i is 1 (fixed 5, parity 1). Transition cost 0. Proceed to dp(1, 1, 1, 0).

Next element is position 2 (0). So code can choose even (since e_left=1). New_p=0. Transition cost between 1 (previous) and 0: 1. Then proceed to next_i=3 (fixed 2, parity 0). Transition cost 0. Next_i=4 (fixed 3, parity 1). Transition cost 1. Total cost 0 (from 0-1) + 1 (1-0) + 0 (0-0) + 1 (0-1) = 2. Which matches the sample. So the code should return 2.

But according to the code's initial call, when the first element is chosen as odd (o=1 is possible), then the code calls dp(0, 1, e=1, o=0). Then, the code's DP function would proceed to compute this path correctly.

So the code should handle this case correctly.

So the code's approach is correct.

Now, let's check for the second sample input:

7

1 0 0 5 0 0 2

Existing numbers are 1,5,2. Missing numbers are 3,4,6,7.

Wait, n=7, so numbers are 1-7. Existing numbers are 1,5,2. So missing are 3,4,6,7. Among these, 3 and 7 are odd (count o=2), 4 and 6 are even (count e=2).

The initial array is [1,0,0,5,0,0,2]. So first element is fixed (1, parity 1).

The code starts by processing the first element (fixed), initial_p=1, e=2, o=2.

Then, the next element is position 1 (0). So in the DP function, for i=0, curr_p=1, e=2, o=2.

The next_i is 1 (0). So code has to choose between even and odd.

If even is chosen (e_left=1), new_p=0. Cost is 1 (1 vs 0). Then, next_i=1.

Then, processing next_i=1 (0), code will again choose even or odd.

But this seems complex. However, the code's DP will explore all possibilities and find the minimal cost.

The sample output is 1, which is achieved by the arrangement 1 7 3 5 6 4 2. Let's see the transitions:

1 (1) →7 (1): 0 cost.

7 →3 (1): 0.

3 →5 (1): 0.

5 →6 (0): cost 1.

6 →4 (0): 0.

4 →2 (0):0.

Total cost is 1.

So the code's DP function should find this arrangement.

But how?

In the code's DP function, the initial_p is 1 (first element is 1). Then, the next element (position 1) is 0, so code can choose even or odd. Choosing odd (o=2 →1) would give new_p=1, cost 0. Then, next element (position 2) is 0, choose odd (o=1→0), new_p=1, cost 0. Next element (position 3) is 5 (fixed, parity 1). Cost 0. Then position 4 is 0. Now, even count is 2 (since in this scenario, even numbers are 4,6). So for position 4, choose even (e=2→1), new_p=0. Cost 1 (previous parity 1). Then, next element (position 5) is 0. Choose even (e=1→0), new_p=0. Cost 0. Then, next element is 2 (fixed, parity 0). Cost 0. So total cost is 1.

So the code's DP function would explore this path and find the minimal cost.

Thus, the code should handle the samples correctly.

Now, the code must be written accordingly.

But wait, in the code above, the DP function is called with i=0 and curr_p as the parity of the first element. However, when the next element is position i+1, which is the next position.

For example, for the first sample:

After choosing even in position 0 (parity 0), next_i is 1. But the code would process next_i=1 as the current position i=0's next step. Wait, perhaps the code has a mistake in how the positions are processed.

Wait, the code's DP function is defined as:

def dp(i, curr_p, e_left, o_left):

    if i == n-1:

        return 0

    next_i = i + 1

    ... process next_i ...

But when i is 0, next_i is 1. So for the first element (i=0), the code processes the transition between i=0 and i=1.

Yes, this is correct.

Thus, the code should work.

But now, testing the code with the first sample.

But in the first sample, after the first element is chosen as odd (1), the code proceeds to process i=0, curr_p=1, e=1, o=0.

next_i=1 (element 5, fixed parity 1). So cost is 0 (curr_p=1 and next_p=1). Add to the result.

Then, next call is dp(1, 1, e=1, o=0).

Now, next_i=2 (element 0). So need to choose even (since e=1).

new_p=0. cost is 1 (prev_p=1 vs 0). Then, next call is dp(2, 0, e=0, o=0).

Then, next_i=3 (element 2, parity 0). cost is 0 (0 vs 0). Call dp(3, 0, e=0, o=0).

next_i=4 (element 3, parity 1). cost is 1 (0 vs 1). Call dp(4, 1, e=0, o=0).

Then, next_i=5 (n-1 is 4, since n=5). i=4 is n-1, so return 0. So total cost is 0 (from 0 to 1) +1 (from 1 to 0) +0 (from 0 to 0) +1 (from 0 to 1) = 2. So the code would return 2.

Thus, the code works for the first sample.

Now, the code must be written in Python, using the above logic.

But there's a possible mistake in the code: when the next_i is a zero, the code subtracts e_left or o_left. But when the next_i is a zero, the code is processing the next_i-th position, which is a zero. So when the code is at position i, the next_i is i+1, which is a zero. The code then chooses even or odd for that position.

But the code's DP function uses the e_left and o_left to track the remaining even and odd numbers. So when a zero is filled with even, e_left is decremented by 1.

Yes.

Thus, the code should correctly model the selection of even and odd numbers for each zero position.

Now, the code must read input, process it as per above, and output the correct minimal complexity.

So the code should handle all cases correctly.

Now, testing for the case where the entire array is zeros. For example:

n=3

0 0 0

The missing numbers are 1,2,3. e=2 (2 is even), o=2 (1 and 3 are odd). Wait, no: 1 is odd, 2 even, 3 odd. So e=1, o=2.

The code would need to find the best arrangement.

The optimal arrangement could be even, even, odd (but missing numbers are 1,2,3: e=1 (2), o=2 (1,3). So possible arrangement: 2,1,3. Complexity: 1 (even and odd) + 1 (odd and odd) → total 2. But wait, between 2 (even) and 1 (odd): cost 1. Between 1 and 3: no cost. Total is 1. So the optimal complexity is 1.

The code should handle this case.

But in this case, the first element is zero. So code would try even and odd.

If even is chosen (2), then e_left becomes 0, o_left is 2.

Next element is zero. The code must choose between even (but e_left=0) and odd. So choose odd (1). Transition cost: 1 (even to odd).

Next element is zero. The code must choose between odd (3). Transition cost: 0 (odd to odd). Total cost is 1.

So the code should return 1.

Thus, the code should work.

Overall, the code seems correct.
</think>

```python
import sys
from functools import lru_cache

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

existing = set()
for num in p:
    if num != 0:
        existing.add(num)
missing = []
for num in range(1, n+1):
    if num not in existing:
        missing.append(num)

e = sum(1 for num in missing if num % 2 == 0)
o = len(missing) - e

is_fixed = []
parities = []
for num in p:
    if num == 0:
        is_fixed.append(False)
        parities.append(None)
    else:
        is_fixed.append(True)
        parities.append(num % 2)

@lru_cache(maxsize=None)
def dp(i, curr_p, e_left, o_left):
    if i == n - 1:
        return 0
    next_i = i + 1
    if is_fixed[next_i]:
        next_p = parities[next_i]
        cost = 1 if (curr_p != next_p) else 0
        return cost + dp(next_i, next_p, e_left, o_left)
    else:
        min_cost = float('inf')
        if e_left > 0:
            new_e = e_left - 1
            new_p = 0
            cost = 1 if (curr_p != new_p) else 0
            res = cost + dp(next_i, new_p, new_e, o_left)
            if res < min_cost:
                min_cost = res
        if o_left > 0:
            new_o = o_left - 1
            new_p = 1
            cost = 1 if (curr_p != new_p) else 0
            res = cost + dp(next_i, new_p, e_left, new_o)
            if res < min_cost:
                min_cost = res
        return min_cost

if is_fixed[0]:
    initial_p = parities[0]
    print(dp(0, initial_p, e, o))
else:
    possible = []
    if e > 0:
        possible.append(dp(0, 0, e-1, o))
    if o > 0:
        possible.append(dp(0, 1, e, o-1))
    print(min(possible) if possible else 0)
```