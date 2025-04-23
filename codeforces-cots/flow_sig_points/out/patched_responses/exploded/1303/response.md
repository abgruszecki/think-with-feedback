<think>
Okay, let's see. The problem is to compute for each element a_i in the array, the sum of F(a_i + a_j) for all j from 1 to n. F(x) is the sum of the digits of x. The constraints are up to 2e5 elements, so any O(n^2) solution is definitely out of the question. We need a way to compute this efficiently.

Hmm. Let's think about the maximum possible a_i. Since a_i can be up to 1e9, adding two a_i's could be up to 2e9. The sum of digits for such a number could be up to like 9*10 digits (since 2e9 is 10 digits). But calculating the sum of digits for each pair is O(n^2), which is 4e10 operations. That's way too slow. So we need a smarter approach.

Wait, maybe the key is to find the frequency of each possible sum, then precompute the digit sums once for all possible sums and multiply by their frequencies. But how do we get the frequencies of a_i + a_j efficiently?

But for that, even if we count the frequency of each a_i, the possible sums can be up to 2e9, which is way too big to precompute. So that's not feasible. So that approach might not work directly.

Alternative idea: group numbers by their digit sums when added to some value. Wait, but how?

Wait, perhaps the sum of digits of (x + y) can be broken down into the sum of digits of x + y. But digit sum has a property that sum_digits(x + y) = sum_digits(x) + sum_digits(y) - 9 * k, where k is the number of carries when adding x and y. But I'm not sure if that helps here.

Alternatively, perhaps for each a_i, when we add it to another a_j, we can precompute the digit sum of a_i + a_j. But again, for each a_i, we have to process all a_j's, which is O(n^2).

Another angle: notice that when you add two numbers, the sum's digit sum can be computed by looking at each digit position. For example, when adding two digits in a position, if there's a carryover from the previous position, it affects the current digit. But this seems complicated to model.

Wait, maybe we can precompute for each possible a_j, the sum of digits when a_j is added to a particular a_i. But how can we find a way to compute this sum efficiently for all j for a given i?

Alternatively, for each a_i, the problem is to compute sum_j (sum_digits(a_i + a_j)). Let's think of a_i as fixed. Then, for each a_j, we compute sum_digits(a_i + a_j). How can we compute the sum over all a_j quickly?

Let’s see, for a_i + a_j, the digits of their sum depend on the individual digits of a_i and a_j, considering the carries. But this seems hard to model. However, perhaps for a given a_i, we can precompute some data structure that allows us to calculate the sum of digits for a_i + a_j for all j efficiently.

Wait, maybe for each a_j, we can represent it as a string of digits, and then when added to a_i's digits, compute how the carries propagate. But even that seems challenging.

Alternatively, for each a_i, we can precompute the digit sum of a_i + x, where x is any number. Then, if we can find the sum over x in the array. But how?

Another thought: since a_i and a_j can be up to 1e9, but their sum's digit sum can be up to 9*10 = 90. So, maybe for each a_i, we can find the count of a_j's such that a_i + a_j has a digit sum of k, and then multiply each k by its count and sum all those. But how to compute the counts of k for each a_i + a_j?

But how to compute how many a_j's when added to a_i have a digit sum of k. That's the crux. If we can group the a_j's into certain categories based on how their addition to a_i affects the digit sum, then we can precompute for each possible a_i the required counts.

But how? Let's think about the digits. For example, when adding a_i and a_j, each digit position contributes to the sum, but with possible carries. The total sum of digits depends on the digits of a_i + a_j, which in turn depends on the digits of a_i and a_j and the carries that occur when adding them.

This seems complicated, but perhaps there's a pattern. Let's take a_i and a_j as numbers. Let's denote their sum as S = a_i + a_j. The digit sum of S is the sum of all digits in S. For example, 123 + 45 = 168, digit sum is 1+6+8=15.

The sum of digits can also be calculated as the sum of the digits of a_i and a_j minus 9 multiplied by the number of carries during the addition. Because whenever a carry occurs, the current digit's sum is reduced by 10 (so 1+9=10, sum digits 1+0=1, which is 1+9-10=0, but 1 + 9's sum is 10, which digit sum is 1, which is 10-9*1). Wait, perhaps sum_digits(a + b) = sum_digits(a) + sum_digits(b) - 9 * (number of carries). Let me check this.

Take a=19 (1+9=10), b=1 (1). Sum is 20, sum_digits is 2. sum_digits(a) is 10, sum_digits(b) is 1. 10+1 -9 *1= 2. Yes. Another example: a=99, b=1. sum_digits(a) is 18, sum_digits(b)=1. sum is 100, sum_digits is 1. 18+1 - 9*2= 19-18=1. Yes. So the formula holds: sum_digits(a + b) = sum_digits(a) + sum_digits(b) - 9 * carries, where carries is the number of carryovers when adding a and b.

So, for each a_i and a_j, sum_digits(a_i +a_j) = sum_digits(a_i) + sum_digits(a_j) -9 * c, where c is the number of carries when adding a_i and a_j.

So, the total sum for a_i would be sum over all j (sum_digits(a_i) + sum_digits(a_j) -9*c_ij) = n * sum_digits(a_i) + sum(sum_digits(a_j)) for all j - 9*sum(c_ij over j).

So the problem can be broken down into two parts:

1. Compute for each i, the sum of sum_digits(a_i) multiplied by n (since each j contributes sum_digits(a_i) once) plus the total sum of all sum_digits(a_j) (since each j contributes their sum once for each i). Wait, no. Wait, for each a_i, the sum over j is sum_digits(a_i) + sum_digits(a_j) -9c_ij. So the sum is sum_digits(a_i)*n + sum_digits_total (sum_digits_total is the sum of all a_j's sum_digits) -9*sum(c_ij for j in 1..n).

Wait, sum_digits(a_i) is added for each j (since for each j, the term is sum_digits(a_i) + sum_digits(a_j) - ...). So sum over j (sum_digits(a_i) + ...) is sum_digits(a_i)*n + sum_digits_total -9 * sum_c_ij.

So the problem reduces to, for each a_i, compute sum_digits(a_i)*n + sum_digits_total -9 * sum_c_ij, where sum_c_ij is the total number of carries when a_i is added to each a_j.

Now, sum_digits(a_i) can be precomputed for each a_i. sum_digits_total is the sum of all sum_digits(a_j), which is a constant for the problem. So the main challenge is to compute sum_c_ij for each i.

The key is to compute sum_c_ij for each i. How?

Carries occur when adding digits in a_i and a_j. So for each a_i, when added to a_j, the number of carries is the count of positions where the sum of the digits (including previous carries) is >=10.

Hmm. So, for each a_i, we need to process all a_j and count the total number of carries when adding a_i and a_j.

This seems difficult. But perhaps we can model the digits of a_j in such a way that for a given a_i, we can quickly compute how adding a_j's digits affects the carry count.

Another approach: For each a_i, represent it as a list of digits (from least significant to most, or vice versa). Then, for each a_j, when adding to a_i's digits, track the carries. But even this approach is O(n * digits) which for 2e5 elements and 10 digits per element is 2e6 operations. But each a_j has to be processed for each a_i, leading to O(n^2 * digits) time, which is 2e6 * 2e5 = 4e11 operations. Which is way too slow.

So we need a smarter way to compute the total carries across all a_j for each a_i.

Wait, but perhaps we can precompute some data structures that allow us to group a_j's based on certain properties related to a_i's digits. For example, for a given a_i's digits, we can partition the a_j's into groups where adding a_j to a_i in a certain digit position would or would not produce a carry. Then, the total number of carries would be the sum over all digits of the number of a_j's that, when added to a_i in that digit position, cause a carry, adjusted for the fact that carries in earlier digits can affect later ones.

But handling this seems complicated, especially since carries can propagate. For example, adding digits in the first position (units) could carry over to the tens, which affects the next digit's sum, etc. So the presence of a carry in a lower digit can cause a carry in a higher digit even if the digits in higher positions wouldn't have caused a carry otherwise.

This interdependency between digits makes it hard to model. So perhaps another approach is needed.

Alternative idea: For each a_i, precompute the number of a_j's that, when added to a_i, result in exactly k carries. Then, sum over k multiplied by the count for each k. But how to compute this?

Another thought: The problem of counting the number of carries when adding two numbers is equivalent to the problem of comparing the digit-wise sums and carries. Let's model this.

Let’s denote the digits of a_i as d_0 (LSB) to d_m (MSB), and similarly for a_j. When adding a_i and a_j, the sum in each digit is s = d_i_k + d_j_k + carry_in. If s >= 10, carry_out is 1, else 0. The carry_in for the next digit is the carry_out from the current.

The total number of carries is the number of digits where carry_out is 1.

But calculating this for each pair (a_i, a_j) is O(digits) per pair, which is again O(n^2 * digits) time.

Hmm. But perhaps for all a_j's, there's a way to precompute some information that allows us to compute the total number of carries when added to a_i.

Alternatively, for each digit position, we can determine how a_j's digits influence the carry in that position when added to a_i's digits.

But how? Let's consider each digit position in a_i. Let's say a_i has digit d in position k. For a_j's digit in position k, let it be e. Then, the sum in this position is d + e + carry_in. If this sum >=10, there's a carry_out, which affects the next digit.

But the carry_in for position k is the carry_out from position k-1. This makes the problem dependent on the previous digits.

This is a chain of dependencies. So the carry in position k depends on the carry from position k-1. Therefore, the number of carries when adding a_i and a_j depends on all the digits of a_j up to the maximum digit position of a_i and a_j.

This seems very hard to model in a way that allows us to precompute for all a_j's.

Alternative idea inspired by digit DP: for a given a_i, precompute for each possible a_j the number of carries. But again, this seems impossible for large n.

Wait, but maybe the number of digits in a_j that are relevant for a_i's digits can be processed in a way that allows us to compute the sum of carries for all a_j's.

Let me think differently. Let's consider the digits of a_i in each position. For each digit position k, a_i has a digit d. Let's consider the possible digits e of a_j in position k.

But the presence of a carry_in (from previous digits) affects whether d + e + carry_in >= 10. So, the carry_in for position k is determined by the previous digits.

This makes the problem of counting the total carries over all a_j's for a given a_i a problem that requires considering all possible combinations of digits and their carry states. Which is similar to digit dynamic programming.

But for each a_i, perhaps we can build a trie or some structure that allows us to process all a_j's digits in a way that tracks carry propagation.

Alternatively, for each a_i, we can model the process of adding a_j's digits digit by digit, keeping track of the carry state, and for each possible carry state, count how many a_j's digits up to the current position would lead to that carry state.

This sounds like a digit DP approach. Let me think:

For a given a_i, we can model the addition of a_j as a process where each digit is processed, and for each digit position, we track the carry (0 or 1). The total number of carries is the sum over all positions where a carry occurred.

For all a_j's, the way they contribute to the carry count when added to a_i depends on their digits. So for a_i, we can precompute a DP table that, for each digit position, and for each possible carry state (0 or 1), keeps track of the number of a_j's that, when added to a_i up to this digit, would have a carry state and contribute to the total carry count.

This approach could be feasible if for each a_i, we process all a_j's through this DP, which would take O(n * digits) time. Then, for all a_i's, the total time would be O(n * digits * n), which is O(2e5 * 2e5 * 10) = 4e10 operations. That's way too slow.

So this approach is not feasible.

Alternative Idea: The sum of carries when adding a_i and a_j can be computed as the number of positions where (d_ik + e_jk) + carry_prev >=10. But since carry_prev depends on previous digits, this is tricky. However, perhaps the sum of all carries across all pairs (i,j) can be found by considering each digit position independently, but I'm not sure.

Wait, maybe in some cases, the carry in a digit position is independent of previous digits. But that's not true. For example, if a previous digit causes a carry, then the current digit's sum is increased by 1. So digits are dependent.

Hmm. So perhaps this problem is impossible to solve in O(n) or O(n log n) time, and the only way is to find an alternative approach that doesn't compute the carries directly.

Wait, let's go back to the original problem. The sum for each i is sum_digits(a_i + a_j) for all j. We can precompute the sum of digits for all pairs. But how?

Another Idea: For each possible a_i, precompute the sum of digits of a_i + a_j for all j. But with n up to 2e5, even precomputing this for all i would be O(n^2), which is 4e10 operations. That's way too slow.

So, this approach is impossible.

Alternative Idea: Let's precompute the sum of digits for all possible numbers. But the maximum possible a_i + a_j is 2e9, so the maximum x is 2e9, which has 10 digits. Precomputing the sum of digits for all x up to 2e9 is impossible due to memory constraints. But maybe we can compute the sum on the fly for a_i +a_j. But that's again O(n^2) time.

Hmm. So perhaps the problem is designed in such a way that the sum of carries can be determined through some mathematical pattern.

Wait, the formula we have is sum = sum_digits(a_i) *n + sum_digits_total -9*sum_c_ij.

So if we can compute sum_c_ij for each i, then the problem is solved.

So how to compute sum_c_ij for each i.

The sum_c_ij is the sum over all j of the number of carries when a_i and a_j are added.

Let's consider the sum of carries for each pair (a_i, a_j). How can we model this sum?

Alternative Idea: For each a_i, we can split the problem into individual digits. For each digit position, compute how many a_j's would, when added to a_i's digit in this position, cause a carry, considering any possible carry from the previous digits.

But this is again complex due to the carry dependencies.

Another Idea inspired by the fact that the numbers are up to 1e9 (so 9 digits at most). Let's represent each number as a string of digits, padded with leading zeros to 18 digits (since two 9-digit numbers added together could have up to 10 digits, but perhaps 18 digits is easier for processing). Then, for each a_i, process each digit position and determine for each possible a_j how the carry propagates.

But how?

Alternatively, for each a_i, we can model the process of adding a_j's digits and track the number of carries. This would require considering the digits of a_j in reverse order (from least significant to most). For each digit position, we can track how the carry affects the next digit.

But again, this seems difficult.

Alternative Idea: Let's think of the addition of two numbers a and b as follows. The number of carries when adding a and b is equal to (sum_digits(a) + sum_digits(b) - sum_digits(a+b)) ) /9. Because sum_digits(a+b) = sum_digits(a) + sum_digits(b) -9*c, so c = (sum_digits(a) + sum_digits(b) - sum_digits(a+b)) ) /9.

But this doesn't directly help us, as sum_digits(a+b) is needed, which is what we are trying to compute. But perhaps if we can find another way to compute c.

Wait, but for the sum over j, sum_c_ij is equal to (sum_digits(a_i) + sum_digits(a_j) - sum_digits(a_i +a_j )) /9 summed over all j.

So, sum_c_ij = [sum_digits(a_i)*n + sum_digits_total - sum_total_ij] /9, where sum_total_ij is the sum of sum_digits(a_i +a_j) for j.

But wait, sum_total_ij is exactly the value we are trying to compute. So substituting back into the earlier formula, we get:

sum_total_ij = sum_digits(a_i)*n + sum_digits_total -9*sum_c_ij.

But sum_total_ij is the same as the desired output for a_i. So substituting gives us an identity, which doesn't help.

So this approach is not helpful.

Alternative Idea: Let's think about the carry propagation. When adding two numbers, the maximum number of carries is the number of consecutive digits where the sum is 9. For example, adding 999 and 1 gives 1000, which has 3 carries (each 9 + 0 plus carry of 1, until the last digit).

But I'm not sure how to use this.

Another Idea: For each a_i, the sum of carries when adding to a_j can be computed by considering the digits of a_i and a_j. Let's process each digit position for a_i and a_j, and for each position, count how many a_j's would cause a carry at that position when added to a_i, considering any possible carry from the previous digits.

But how to model the carry-in from previous digits?

This seems like a problem that can be approached using digit dynamic programming. For each a_i, we can process all a_j's digits in a way that tracks the carry state. For example, for each digit position, we can track the number of a_j's that have a certain digit and carry state, and then compute the total number of carries.

But how to implement this efficiently for all a_i's and a_j's.

Here's a possible approach:

1. Precompute for each a_j, its digits in each position (from 0 to 9, padding with zeros to make all numbers 18 digits long).

2. For each a_i, process each digit position from left to right (or right to left), and for each possible carry state (0 or 1), track how many a_j's would result in a carry at this position.

But even this seems complicated.

Alternatively, here's a possible digit DP approach for a single a_i:

The idea is that when adding a_i and a_j, we process each digit of a_j (along with a_i's digits) and track the carry state. For each a_i, we can build a trie-like structure that for each digit position and carry state, counts the number of a_j's that have certain digits and would result in a certain carry state.

But how to model this for all a_j's.

An alternative approach inspired by the fact that a_j can be up to 1e9, but each a_j's digits can be represented as a string. Let's see:

For each a_i, when adding a_j, the number of carries is determined by the digits of a_i and a_j. For example, the first digit (least significant digit) of a_i and a_j:

d = a_i's digit, e = a_j's digit.

sum = d + e.

carry_in is 0 initially. So if sum >=10, carry_out is 1. Otherwise 0.

Then, for the next digit (tens place), the sum is a_i's digit + a_j's digit + carry_in from previous.

And so on.

So, the carry_out for each digit depends on the sum of the digits and the previous carry_in.

The total number of carries is the number of times carry_out is 1.

So for each a_j, the number of carries when added to a_i depends on the digits of a_j and the digits of a_i.

The challenge is to precompute for each a_i, the sum of carries over all a_j's.

This seems like a problem where we can precompute for each a_i, the digits and then model the carry propagation using some kind of digit DP for all a_j's.

But how?

Let’s consider the digits of a_i as fixed, and for each a_j, process their digits from least significant to most. For each digit position k (starting from 0), we can model the carry state (0 or 1) after processing that digit. For each state, we can track how many a_j's have certain digits that would lead to that carry state.

This is similar to building a state machine for each a_i's digits.

For example, for a_i's digits (d0, d1, d2, ..., d18), padded with zeros to 18 digits.

Then, for each a_j, we process each digit e_k (from k=0 to 18) and model the carry transitions.

The initial state is carry=0.

At each step, the sum is d_k + e_k + carry_in.

carry_out is 1 if sum >= 10, else 0.

The number of carries increases by 1 if carry_out is 1.

So, for each a_i, we can model this as a DP problem where we track the current carry state and the number of a_j's that reach this state, along with the accumulated number of carries.

But how to compute this for all a_j's.

The key is to precompute for each a_i and for each possible digit position and carry state, the number of a_j's that, when processed up to that digit, would lead to a certain carry state and contribute to the carry count.

This approach is feasible if we can represent the a_j's in a trie-like structure, grouped by their digits. However, building such a structure for 2e5 elements with 18 digits each would be memory-intensive.

Alternative Idea: Preprocess all a_j's into a frequency array based on their digits. For each digit position, we can store the count of a_j's that have a certain digit in that position. But how does this help in modeling the carry propagation.

Alternatively, for each digit position k, and for each possible digit e (0-9), we can count how many a_j's have digit e in position k. Then, for a_i's digit d in position k, the sum of e_j's digits in position k for a_j's is sum_e (count[e] * e). But this doesn't directly relate to the carries.

Hmm. Let's think of the carry for each digit position in isolation. Suppose we can find the number of a_j's where, when added to a_i's digits up to position k, the sum produces a carry.

But due to carry propagation from previous digits, this is not possible to compute in isolation.

This seems like a dead end.

Alternative Idea: Let's consider that the sum of carries for all pairs (i,j) can be computed by considering each digit position and counting the number of pairs where the sum of digits (plus any necessary carry) in that position and all previous positions leads to a carry.

But again, this is complicated.

Another Idea: Since the numbers are up to 1e9, perhaps the maximum number of digits is 10. So for each a_i, we can represent it as a 10-digit number with leading zeros. Then, for each a_j, process each digit in reverse order (from least significant to most). For each a_i, we can precompute for each digit position the digits of a_j that would cause a carry when added to a_i's digit, considering the possible carry_in from the previous digit.

But the carry_in depends on the previous digits. So, for example, the carry_in for position k is determined by whether the sum of digits in position k-1 plus carry_in from k-2 was >=10.

So the carry_in for position k is the carry_out from position k-1.

This dependency chain means that the carry_in for each position is determined by the previous positions. Therefore, the total number of carries for a pair (a_i, a_j) is determined by the entire sequence of digits of a_i and a_j, and their interactions with carry propagation.

This makes the problem very complex. So perhaps there's a mathematical shortcut here.

Alternative Idea: For the purposes of this problem, perhaps the sum of carries can be approximated by considering each digit position independently, but this is not accurate. However, perhaps there's a way to model the expected number of carries and find a pattern.

But given the problem's constraints, this seems unlikely.

Wait, but perhaps the number of carries is equal to the number of digits where the sum of the digits of a_i and a_j (without considering previous carries) plus the maximum possible carry_in from previous digits would exceed 9. But again, this is not precise.

Another Idea: Let's try to find for each a_i and for each digit position k, how many a_j's have a digit e such that e >= (10 - d_i_k - carry_in). But since carry_in depends on previous digits, this approach is not directly applicable.

But perhaps for each a_i, we can precompute for each digit position k, the required digit e in a_j that would cause a carry_out. The problem is that carry_out depends on the carry_in, which depends on the previous digits.

But what if we ignore the carry_in from previous digits? Then, the number of carries would be the sum over all digits of the number of a_j's digits that, when added to a_i's digit, are >= 10. But this is not correct, as it doesn't account for carries from previous digits.

However, perhaps this can be a starting point. Let's compute for each a_i, the number of a_j's where, in each digit position, the sum of a_i's digit and a_j's digit is >= 10. Then, the sum of these counts is an upper bound on the number of carries, but the actual number is lower due to carries that are caused by previous digits.

But this upper bound is not helpful. For example, if two consecutive digits have sums >=10, then the second digit's sum would be a_i's digit + a_j's digit + 1 (carry from previous), which may increase the carry count.

Hmm. So this approach is not directly applicable.

Another Idea inspired by the fact that for two numbers, the maximum number of carries is the number of consecutive 9's in their digits. But this is not necessarily true.

Alternative Idea: Let's precompute for each a_j, its digits in each position. Then, for each a_i, for each digit position k, we can compute how many a_j's have a digit e in position k such that e >= (10 - d_i_k). This would give the number of carries in position k if there's no carry_in from position k-1. But since carry_in can be 1, this is not accurate.

But perhaps for a given a_i and digit position k, the number of a_j's where e >= (10 - d_i_k) is a component of the total carries. But the presence of a carry_in from position k-1 can increase the number of carries in position k.

But how to model this?

Perhaps the total number of carries is equal to the sum over all positions k of the number of a_j's where the sum of digits from 0 to k in a_i and a_j leads to a carry in position k.

But this seems difficult.

Alternative Idea: For a given a_i, the carries when adding a_j can be determined by the digits of a_j and the digits of a_i. For example, adding a_j to a_i can be viewed as follows:

Initialize carry = 0 and total_carries =0.

For each digit position from 0 (LSB) to 9 (MSB):

sum = a_i.digits[k] + a_j.digits[k] + carry

if sum >=10:

carry =1

total_carries +=1

else:

carry =0

So, for each a_j, the total_carries is determined by the digits of a_j and the carry propagation.

The key is to find, for each a_i, the sum of total_carries over all a_j's.

This is a classic problem where each a_j is processed through a state machine determined by a_i's digits and the carry propagation.

To model this efficiently, we can preprocess the a_j's and for each a_i, use a trie-like structure to track the possible digits and carry states.

However, building such a structure for each a_i is time-consuming.

Alternative Idea inspired by the fact that the number of carry transitions is small (since each a_j has at most 10 digits):

For each a_j, precompute its digits in each position (up to 10 digits, padded with zeros), and store them as a list. Then, for each a_i, process all a_j's and compute the total_carries using their digit lists.

But this would take O(n * 10) = 2e5 * 10 = 2e6 operations per a_i, leading to O(n^2 * 10) = 4e11 operations, which is way too slow.

This is not feasible.

Thus, we need to find a way to compute the sum of carries for all a_j's for each a_i efficiently.

Another Idea: Let's represent each a_j as a string of digits, and for each a_i, precompute a digit-wise mask that allows us to compute the carries. For example, for each a_i's digit in position k, we can precompute a threshold (10 - digit) and count the number of a_j's with digits in position k that meet this threshold, considering carry_in.

But carry_in depends on previous digits, making this approach challenging.

Perhaps, for a_i's digits, we can precompute for each possible carry_in (0 or 1) in each digit position, the number of a_j's digits that would result in a carry_out.

But how?

For example, in digit position k:

If carry_in is c (0 or 1), then the sum is a_i.digit[k] + a_j.digit[k] + c.

carry_out is 1 if sum >=10, else 0.

So, for a given a_i.digit[k], and carry_in c, the number of a_j's where a_j.digit[k] >= (10 - a_i.digit[k] - c) is the count for that scenario.

But since carry_in c depends on the previous digit's processing, this creates a dependency between digit positions.

This seems like a problem that can be modeled using dynamic programming.

For each a_i, and for each possible carry_in state (0 or 1) at each digit position, we can compute the number of a_j's that would generate that carry_in state and the accumulated carry count.

But how to do this for all a_j's efficiently.

Here's a possible approach:

1. For each a_j, precompute its digit string (d_0 to d_18, padded with zeros).

2. For each a_i, create a dynamic programming table that tracks the carry state and the number of a_j's that reach that state, along with the accumulated carries.

The DP would proceed digit by digit, from the least significant digit (k=0) to the most (k=18). For each digit position k, and for each possible carry_in state (0 or 1), we track the number of a_j's that, when added to a_i's digits up to position k-1, result in a carry_in of that state, and the total number of carries accumulated up to that point.

At each step k, for each carry_in state c_in (0 or 1), we process all a_j's and compute how many of them would transition to a carry_out state c_out, and add the number of carries (c_out) multiplied by the count of a_j's leading to this transition.

The initial state is carry_in 0, count 1 (assuming all a_j's start with no carry).

But wait, for each a_j, the carry_in for the first digit (k=0) is 0. Then, the carry_out for k=0 becomes the carry_in for k=1, and so on.

So, for each a_i, we can process all a_j's by building a DP table for each digit position and carry state.

Let's formalize this:

For each a_i, digits are d_0, d_1, ..., d_18.

For each a_j, digits are e_0, e_1, ..., e_18.

For each digit position k from 0 to 18:

For each possible carry_in c_in (0 or 1):

sum_e = d_k + e_j_k + c_in

carry_out = 1 if sum_e >=10 else 0

The number of carries contributed by this digit is carry_out.

So, for each a_j and a_i, the total number of carries is the sum of carry_out for each digit position.

Thus, for each a_i, we need to compute the sum over all j of the sum of carry_out for each digit position.

To compute this, for each a_i, we can process each digit position k, and for each possible carry_in state c_in, compute the number of a_j's where, given the previous carry_in state, the digit e_j_k would result in a carry_out. Multiply this count by 1 (since each such a_j contributes a carry_out of 1) and sum over all digits.

But how to model the carry_in states for each digit.

The idea is to use dynamic programming, where for each digit position, we track the possible carry_in states and the number of a_j's that reach those states, along with the total carries accumulated up to that point.

The steps would be:

For each a_i:

   Initialize a DP array where dp[k][c_in] represents the number of a_j's that, after processing the first k digits, have a carry_in state c_in (0 or 1), and the total number of carries accumulated up to that point.

   Initially, dp[0][0] = 1 (all a_j's start with carry_in 0) and dp[0][1] = 0.

   For each digit position k from 0 to 18:

      For each carry_in state c_in (0 or 1):

          For each possible e_j_k (0-9):

              sum_d_e = d_i_k + e_j_k + c_in

              c_out = 1 if sum_d_e >=10 else 0

              The number of a_j's that have e_j_k as their k-th digit is count[e_j_k].

              We then add to dp[k+1][c_out] the number of a_j's with e_j_k multiplied by dp[k][c_in].

              Additionally, the total carries contributed by this digit is c_out multiplied by the number of a_j's processed.

   After processing all digits, the sum of carries is the accumulated total.

But wait, this approach counts the number of a_j's that have a certain carry_out at each step and the total carries contributed by each a_j. However, this would require tracking for each a_j the path through the carry states and summing the carries.

But this is not feasible for n=2e5 and 19 digits, as each a_i would require O(2*19) operations per a_j.

Alternative Idea: Instead of tracking the exact carry_in states for each a_j, perhaps we can model the carry_in state as a parameter and compute for each a_i and each digit position, the number of a_j's that would transition between carry_in states based on their digits.

This is possible using the following approach:

For each a_i:

   We initialize a carry_in frequency: for digit position 0, all a_j's have carry_in 0.

   For each digit position k in 0..18:

      For each possible carry_in state c_in (0 or 1):

          For each possible digit e in 0..9:

              sum = d_i_k + e + c_in

              c_out = 1 if sum >=10 else 0

              The number of a_j's with digit e in position k is cnt[e].

              The number of a_j's that are in carry_in c_in and have digit e in position k is cnt[e] * freq[c_in].

              The number of carries contributed by these a_j's is c_out * (cnt[e] * freq[c_in]).

              Add this to the total carries.

              Update the next carry_in frequency: next_freq[c_out] += cnt[e] * freq[c_in]

      Set freq = next_freq for the next digit.

But this approach requires, for each a_i, processing each digit position and each possible carry_in state and digit. For each a_i, this would take O(19 * 2 * 10) = 380 operations. For n=2e5 a_i's, this would be 2e5 * 380 = 7.6e7 operations, which is acceptable.

Yes! This seems feasible.

Here's how this works:

For each a_i:

- We model the carry_in states as a frequency array. Initially, before any digits are processed, all a_j's are in carry_in 0.

- For each digit position k of a_i (from 0 to 18):

   - For each possible carry_in state (0 or 1), we check how many a_j's would have that state.

   - For each a_j's digit e in position k, we compute the sum (a_i's digit at k) + e + carry_in.

   - This gives a carry_out state (0 or 1).

   - The number of a_j's that transition from carry_in to carry_out is cnt[e] * freq[c_in], where cnt[e] is the number of a_j's with digit e in position k.

   - The total carries contributed by these a_j's is the number of a_j's that transition multiplied by carry_out (which is 1 if there's a carry, 0 otherwise).

   - We accumulate this to the total carries.

   - We update the frequency for the next digit's carry_in state.

So, for each a_i, the process is:

total_carries = 0

freq = {0: 1, 1: 0}  # Initially, all a_j's have carry_in 0 for the first digit.

for each digit position k in 0 to 18:

    next_freq = {0: 0, 1: 0}

    for c_in in [0, 1]:

        if freq[c_in] == 0:

            continue

        for e in 0..9:

            count_e = cnt[k][e]

            if count_e == 0:

                continue

            sum_e = d_i_k + e + c_in

            c_out = 1 if sum_e >=10 else 0

            total_carries += c_out * count_e * freq[c_in]

            next_freq[c_out] += count_e * freq[c_in]

    freq = next_freq

Thus, the sum_c_ij for a_i is the total_carries accumulated after processing all digit positions.

The key here is that for each digit position k of a_j, we can precompute the count of a_j's with each possible digit e. We can precompute a 2D array cnt[k][e] where cnt[k][e] is the number of a_j's that have digit e in position k.

This preprocessing step is O(n * digits) time, which is acceptable.

Once we have this cnt array, for each a_i, we process each digit position k, and for each possible carry_in state, compute how many a_j's contribute to carry_out and the total carries.

This approach would have a time complexity of O(n * digits) for preprocessing, and O(n * digits * 2 * 10) for processing all a_i's, which should be acceptable.

So, the steps are:

1. Precompute for each digit position k (0 to 18), the count of a_j's digits e in position k. This can be done by converting each a_j into a list of digits (padded to 19 digits), and for each position, increment a counter for each digit.

2. For each a_i:

   a. Convert a_i into a list of digits (padded to 19 digits).

   b. Initialize freq = [1, 0] (carry_in 0 for the first digit).

   c. Initialize total_carries = 0.

   d. For each digit position k from 0 to 18:

      i. Get the digit d = a_i_digits[k].

      ii. For each carry_in c_in (0 and 1):

          if freq[c_in] is 0, skip.

          for each possible digit e in 0..9:

              count_e = cnt[k][e]

              if count_e == 0, skip.

              sum_e = d + e + c_in

              c_out = 1 if sum_e >=10 else 0

              total_carries += c_out * count_e * freq[c_in]

              next_freq[c_out] += count_e * freq[c_in]

      iii. Update freq to next_freq, reset next_freq for next iteration.

   e. After processing all digits, the sum_c_ij for this a_i is total_carries.

   f. Compute the total sum for this a_i as sum_digits(a_i)*n + sum_digits_total -9*total_carries.

3. Output the computed sums for all a_i.

Now, let's think about the implementation.

First, we need to precompute the sum_digits for each a_j. This can be done in O(n) time.

Second, we need to pad each a_i and a_j to 19 digits (since 1e9 has 9 digits, so sum can have up to 10 digits. But to be safe, we can pad to 19 digits, which is sufficient for 1e9 + 1e9 = 2e9 (10 digits). But for the code, it's easier to process numbers as strings padded to 19 digits, but since 1e9 is 9 digits, adding two 9-digit numbers gives a 10-digit number. So we need to pad to 10 digits. Wait, no. Wait, the maximum sum is 2e9, which is 10 digits. So each a_j is padded to 10 digits. So, for example, 42 becomes '0000000042'.

Wait, but when adding two numbers, the carry can propagate to higher digits. For example, 999 + 1 = 1000. So we need to process all digits up to the maximum possible position. So each a_j should be padded to 19 digits (or some sufficient length). However, this may be overkill. But since in practice, a_j can be up to 1e9-1 (9 digits), adding two of them gives 2e9-2, which is 10 digits. So the maximum number of digits is 10. So padding to 10 digits is sufficient. But we need to process all digits up to the maximum possible.

So, in code, for each a_j, we convert it to a string of digits, padded with leading zeros to 10 digits. Then, for each position k from 0 (LSB) to 9 (MSB), we store the digit.

But wait, leading zeros are padded to the left. For example, the number 42 is padded to 10 digits as '0000000042'. The digits, when processed from 0 to 9 (right to left), are '4', '2', then 8 zeros. Wait, no. If the string is '0000000042', then index 0 is the last digit (2), index 1 is 4, and indexes 2-9 are 0.

Wait, perhaps the best way is to process the digits from least significant to most. So, for example, the number 123 is stored as [3,2,1,0,0,0,0,0,0,0] for 10 digits.

So, for each number, we can process it as follows:

1. Convert the number to a string, e.g., 123 becomes "123".

2. Reverse the string to get the digits from LSB to MSB: "321".

3. Pad the reversed string to 10 digits with '0's: "3210000000".

4. For each position k (0 to 9), the digit is the character at index k in this padded string.

So, for example, for 123, digit 0 is '3', digit 1 is '2', digit 2 is '1', and digits 3-9 are '0'.

Thus, when processing the digits from 0 (LSB) to 9 (MSB), we get the correct digits.

Once we have this representation for all a_j's, we can precompute the cnt array: for each position k (0 to 9), cnt[k][e] is the number of a_j's with digit e at position k.

But wait, the sum of two a_j's can have up to 10 digits (e.g., 1e9-1 + 1e9-1 = 1999999998, which is 9+9=18, digits 1 followed by 9 digits of 9's and 8. But wait, 1e9 is 1 followed by 9 zeros, so 1e9-1 is 999,999,999. Adding two of them gives 1,999,999,998. So the sum is 10 digits. So the maximum digit positions we need to consider is 10. So padding to 10 digits is sufficient.

So, in code:

Each number is padded to 10 digits, reversed, and then each digit is processed.

So, for each a_j, digits are stored as a list of 10 digits, where the 0th index is the least significant digit.

Once this is done, we can precompute cnt[k][e], which is the number of a_j's with digit e at position k.

Next, for each a_i, we need to compute their digits in the same format.

Then, for each a_i's digits, we process each position k, and compute the contribution to the carry count.

The code outline would be as follows:

Read n.

Read the array a.

Precompute sum_digits for each a_j, and compute sum_digits_total = sum(sum_digits).

Precompute the digits for each a_j:

digits_j = [[] for _ in range(n)]

for each j in 0..n-1:

    s = str(a[j])

    reversed_s = s[::-1]

    padded_s = reversed_s.ljust(10, '0')  # pad with zeros to 10 digits

    digits = [int(c) for c in padded_s[:10]]  # ensure we have 10 digits

    digits_j[j] = digits

precompute cnt[k][e]: a 10x10 array.

for k in 0..9:

    cnt_k = [0] * 10

    for j in 0..n-1:

        e = digits_j[j][k]

        cnt_k[e] += 1

    cnt[k] = cnt_k

Now, for each a_i:

    compute its digits as described.

    initialize freq = [1, 0]  # frequency of carry_in states

    total_carries =0

    for k in 0..9:

        d = digits_i[k]

        next_freq = [0, 0]

        for c_in in 0,1:

            if freq[c_in] ==0:

                continue

            for e in 0..9:

                count_e = cnt[k][e]

                if count_e ==0:

                    continue

                sum_e = d + e + c_in

                c_out = 1 if sum_e >=10 else 0

                total_carries += c_out * count_e * freq[c_in]

                next_freq[c_out] += count_e * freq[c_in]

        freq = next_freq

    # After processing all 10 digits, sum_c_ij = total_carries

    res = sum_digits_i *n + sum_digits_total -9* total_carries

    append res to the result list

Output the result list.

But wait, what about digits beyond 9? For example, when a_i and a_j have digits beyond the 9th position (k=9). But according to our padding, all numbers are padded to 10 digits, so k ranges from 0 to9. This covers all possible digits since the maximum sum has 10 digits.

Thus, the code should work.

Now, let's test this approach with the first example:

Sample Input 1:

4

1 3 3 7

sum_digits of each:

1: sum is 1.

3: sum is 3.

3: sum is3.

7: sum is7.

sum_digits_total = 1+3+3+7=14.

sum_digits_i *4 +14 -9* sum_c_ij.

For i=0 (a_i=1):

sum_digits_i =1.

sum_c_ij is the total carries when adding 1 to each of the 4 elements.

Let's compute sum_c_ij for a_i=1.

The digits of 1 are [1,0,0,0,0,0,0,0,0,0] (since reversed and padded to 10 digits). So for k=0, digit is 1; others are 0.

For each a_j in the array:

a_j=1: digits are [1,0,0,...0]

sum for k=0: 1+1 +0 (carry_in=0) =2, no carry. sum_c_ij=0.

Similarly, other digits are 0, so no carries. So total carries 0.

But according to the code's processing:

For k=0:

d=1.

freq starts as [1,0].

For c_in=0:

sum_e for each e in 0-9.

For e=1 (a_j=1 has e=1 at k=0):

sum_e =1+1 +0=2 <10. c_out=0.

So total_carries += 0 * 1 * 1 (count_e for e=1 is 1? Or in the sample, how many a_j's have e=1 at k=0?

Wait, in the first sample input, the a_j's are 1,3,3,7.

Their digits when padded:

For a_j=1: reversed is '1', padded to 10 digits -> '1000000000' (wait, no, perhaps I have a mistake here).

Wait, wait. Let's clarify.

For a_j=1:

The number is 1. As a string, it's '1'. Reversed is '1'. Padded to 10 digits with zeros to the right (since reversed) gives '1' + '0'*9 → '1000000000' (but wait, no. Let's think again.

Wait, when we reverse the string to get the digits from LSB to MSB, for the number 1, the reversed string is '1'. Then, padding with zeros to get 10 digits would make '1' followed by 9 zeros? Or is it '1' as the first character (LSB) and then zeros added to the right (MSB) direction.

For example, the number 123, when reversed, is '321'. Padding to 10 digits would be '3210000000'. So digits are stored as 3 (k=0), 2 (k=1), 1 (k=2), 0 (k=3), etc.

So for the number 1, reversed is '1', padded to 10 digits would be '1' followed by 9 zeros. So the digits are:

k=0: '1'

k=1: '0'

k=2: '0'

...

k=9: '0'

So digits_j[0] for a_j=1 is [1,0,0,0,0,0,0,0,0,0].

Similarly, a_j=3: digits are [3,0,0,...0].

a_j=3: same.

a_j=7: digits are [7,0,0,...0].

Thus, for k=0, the cnt[0][e] is:

e=1: 1 (from a_j=1)

e=3: 2 (from two 3s)

e=7:1 (from a_j=7)

others:0.

So for a_i=1, processing digit k=0:

d=1, c_in starts as 0.

For e in 0-9:

count_e is cnt[0][e], which is 1 for e=1, 2 for e=3, 1 for e=7, others 0.

So for c_in=0:

sum_e =1 + e +0.

For e=1: sum=2 <10 → c_out=0. total_carries +=0 *1 *1 =0.

e=3: sum=4 → c_out=0. total_carries +=0*2*1=0.

e=7: sum=8 → c_out=0. total_carries +=0*1*1=0.

For other e's, sum is 1+e, which is <=9.

Thus, no carries are added.

next_freq[c_out] += count_e * freq[c_in] → all e's contribute to c_out=0.

So next_freq[0] = (1+2+1) *1 =4.

 freq becomes [4,0].

Then, for k=1 to 9:

d_i's digits are 0. So d=0 for all these positions.

For k=1:

d=0.

For c_in=0:

sum_e =0 + e +0.

Any e >=10 -0 -0 → e >=10. Impossible. So no carries. So for all e in 0-9, sum_e =e. So c_out=0 if e<10. So no carries.

Thus, no contribution to total_carries.

next_freq remains 4 * cnt[1][e] for e=0. But cnt[1][0] is 4 (since all a_j's have 0 in k=1).

So next_freq[0] =4 *4? No. Let's see:

For k=1, c_in=0.

sum_e=0+e+0 =e.

c_out=0 for all e <10.

So for all e in 0-9, count_e is cnt[1][e], which for all a_j's is 4 (since k=1 digits are all 0).

So for each e, count_e =4 if e=0, 0 otherwise.

So sum_e=0+0+0=0 → c_out=0.

So for c_in=0:

count_e=4 (e=0) → sum_e=0 → c_out=0.

Thus, total_carries +=0 *4 *4 =0.

next_freq[0] +=4 *4 → 4*4 =16? No, no. Wait, freq[c_in] is 4 (current freq is [4,0]).

So for e=0:

count_e =4 (since all a_j's have 0 in k=1).

sum_e=0+0+0=0 → c_out=0.

next_freq[0] +=4 *4 (count_e=4, freq[c_in]=4) → 4*4=16.

Thus, next_freq[0] =16, and next_freq[1] remains 0.

This process continues for all remaining k=2 to 9.

Each k from 1 to 9:

d_i's digit is 0.

All a_j's digits in these positions are 0.

So for each k:

sum_e =0 +0 +c_in → c_in is 0 (since the previous carry is 0).

Thus, sum_e=0 → c_out=0.

So for all k from 1 to9:

At each step, freq is multiplied by the count of e=0 (which is 4), and next_freq[0] becomes 4 * freq[c_in] (since count_e=4 for e=0).

Thus, after k=0, freq is [4,0].

After k=1: freq is [4*4=16,0].

After k=2: 16 *4=64.

...

After k=9: freq is 4^10 = 1048576.

But for the total_carries, no carries are contributed in any of these steps.

Thus, the total_carries is 0.

Thus, sum for a_i=1 is 1*4 +14 -9*0 =4+14=18. Which matches the sample output.

Similarly, for a_i=3:

sum_digits_i=3.

sum_c_ij is computed as follows:

For k=0: d=3.

The a_j's digits at k=0 are 1,3,3,7 → e=1,3,3,7.

For each e in 0-9:

count_e=1 for e=1, 2 for e=3, 1 for e=7.

Processing c_in=0.

sum_e =3 + e +0.

For e=1: sum=4 → no carry.

e=3: sum=6 → no carry.

e=7: sum=10 → carry_out=1.

So for e=7, sum_e=10 → c_out=1.

Thus, contribution to total_carries: 1*1*1 (count_e=1, freq[c_in]=1).

So total_carries +=1*1*1=1.

Thus, the total_carries for this a_i is 1.

But wait, let's recheck:

For a_i=3:

digits are [3,0,0, ... 0].

Processing k=0:

d=3.

For c_in=0:

sum_e =3 + e +0.

e=1: sum=4 → no carry. contributes 0.

e=3: sum=6 → no carry. 2 instances → 0.

e=7: sum=10 → carry_out=1. 1 instance → 1 *1*1=1.

Thus, total_carries increases by 1.

next_freq[c_out] for e=7 is 1 *1 =1 (c_out=1).

Other e's (0,1,2,4-6,8-9): count_e=0, so no contribution.

For e=3 (count=2):

sum=6 → c_out=0. contributes 0.

Thus, next_freq[0] += (1+2) *1 =3? Or no: for e=1, count_e=1, sum=4 → c_out=0. So next_freq[0] +=1*1=1.

e=3: count_e=2 → sum=6 → c_out=0. next_freq[0] +=2*1=2 → total 3.

e=7: count_e=1 → next_freq[1] +=1*1=1.

So after k=0:

next_freq[0] =3, next_freq[1] =1.

Wait, wait. Let's re-calculate.

For c_in=0:

for e=1: count_e=1.

sum_e=3+1+0=4 → c_out=0.

contributions to next_freq[0] +=1 *1 (since count_e=1, freq[c_in=0]=1).

e=3: count_e=2.

sum_e=3+3=6 → c_out=0.

contributions to next_freq[0] +=2 *1=2.

e=7: count_e=1.

sum_e=3+7=10 → c_out=1.

contributions to next_freq[1] +=1*1=1.

other e's have count_e=0.

Thus, next_freq[0] =1+2=3, next_freq[1] =1.

Thus, freq becomes [3,1].

Then, for k=1:

d=0.

For c_in=0 and 1.

For c_in=0 (freq=3):

sum_e=0 +e +0.

For e=0 (count_e=4):

sum_e=0 → c_out=0.

contributions to next_freq[0] +=4 *3 =12.

For other e's: count_e=0.

For c_in=1 (freq=1):

sum_e=0 +e +1.

e can be 0 → sum_e=1 → no carry.

For e=0 (count_e=4):

sum_e=1 → c_out=0.

contributions to next_freq[0] +=4 *1=4.

Thus, next_freq[0] =12+4=16.

next_freq[1] remains 0.

So freq is now [16,0].

Processing k=2:

d=0.

For c_in=0 (freq=16):

sum_e=0 +e +0.

e=0 → count_e=4.

sum_e=0 → c_out=0.

contributions to next_freq[0] +=4 *16 =64.

So next_freq[0] =64.

This continues up to k=9.

At each step, the freq is multiplied by 4 (since cnt[k][0] =4 for k>0).

Thus, after k=1, freq becomes 16.

k=2: 16 *4=64.

k=3: 64 *4=256.

...

k=9: 4^9 * 16 = 4^10 = 1048576.

But during these steps, no carries are added except for k=0.

Thus, total_carries is 1.

But wait, what about other digits? For k=0, we have 1 carry. Then, for k=1 to 9, no carries.

Thus, sum_c_ij =1.

So the result is 3*4 +14 -9*1 = 12+14-9=17, which matches the sample.

Thus, the approach works.

Now, the code needs to:

- Precompute the digits for each a_j.

- Precompute cnt[k][e] for each digit position and digit e.

- For each a_i, compute their digits.

- Compute sum_c_ij using the dynamic programming approach.

- Compute the result using sum_digits_i *n + sum_digits_total -9*sum_c_ij.

Now, let's write the code.

First, precompute the sum_digits for each a_j.

Then, precompute the digits for each a_j.

Then, precompute cnt[k][e].

Then, for each a_i:

   compute their digits.

   process each digit position k.

   compute the sum_c_ij.

   compute the result.

Implementing this in Python.

But for large n, it's important to optimize the code.

But Python can handle 2e5 elements.

So, code steps:

Read n.

Read the list a.

Compute sum_digits for each element in a.

Compute sum_digits_total.

Precompute the digits for each a_j.

Precompute cnt[k][e].

Then, for each a_i:

   compute its digits.

   compute the sum_c_ij.

   compute the result.

Implementing the digits:

For a given x, we can compute its digits as follows:

def get_digits(x):

    s = str(x)

    reversed_s = s[::-1]

    padded = reversed_s.ljust(10, '0')[:10]

    digits = [int(c) for c in padded]

    return digits

But for large x, this is manageable.

But for x=0, it's handled properly.

Now, code:

Read n.

a = list(map(int, input().split()))

sum_digits = [sum(map(int, str(num))) for num in a]

sum_digits_total = sum(sum_digits)

precompute digits_j.

digits_j = [get_digits(num) for num in a]

precompute cnt.

cnt = [[0]*10 for _ in range(10)]

for k in range(10):

    for j in range(n):

        e = digits_j[j][k]

        cnt[k][e] += 1

Wait, no. The digits_j is a list of lists. For each j, digits_j[j] is a list of 10 digits (k from 0 to9).

Thus, for each k in 0..9, and e in 0..9:

cnt[k][e] is the number of j's where digits_j[j][k] ==e.

Thus, code:

cnt = [[0]*10 for _ in range(10)]

for j in range(n):

    for k in range(10):

        e = digits_j[j][k]

        cnt[k][e] += 1

Yes.

Now, for each a_i in a:

compute digits_i = get_digits(a_i).

sum_digits_i = sum_digits[i]

initialize freq = [1, 0]

total_carries =0

for k in 0..9:

    d = digits_i[k]

    next_freq = [0, 0]

    for c_in in [0, 1]:

        if freq[c_in] ==0:

            continue

        for e in 0..9:

            count_e = cnt[k][e]

            if count_e ==0:

                continue

            sum_e = d + e + c_in

            c_out = 1 if sum_e >=10 else 0

            total_carries += c_out * count_e * freq[c_in]

            next_freq[c_out] += count_e * freq[c_in]

    freq = next_freq

Thus, after processing all 10 digits, sum_c_ij is total_carries.

Then, the result is sum_digits_i *n + sum_digits_total -9 * total_carries.

Collect all results and print.

Now, code:

But in Python, digits can be computed as follows.

def get_digits(x):

    s = str(x)

    reversed_s = s[::-1]

    padded = reversed_s.ljust(10, '0')[:10]

    return [int(c) for c in padded]

Then, the code:

n = int(input())

a = list(map(int, input().split()))

sum_digits = [sum(map(int, str(num))) for num in a]

sum_digits_total = sum(sum_digits)

# Precompute digits for each a_j

digits_j = []

for num in a:

    s = str(num)[::-1]

    padded = s.ljust(10, '0')[:10]

    digits = [int(c) for c in padded]

    digits_j.append(digits)

# Precompute cnt[k][e]

cnt = [[0]*10 for _ in range(10)]

for k in range(10):

    for j in range(n):

        e = digits_j[j][k]

        cnt[k][e] += 1

# Process each a_i

result = []

for i in range(n):

    num = a[i]

    # Compute digits_i

    s = str(num)[::-1]

    padded = s.ljust(10, '0')[:10]

    digits_i = [int(c) for c in padded]

    sum_digits_i = sum_digits[i]

    # Compute sum_c_ij

    freq = [1, 0]

    total_carries = 0

    for k in range(10):

        d = digits_i[k]

        next_freq = [0, 0]

        for c_in in [0, 1]:

            if not freq[c_in]:

                continue

            for e in range(10):

                count_e = cnt[k][e]

                if not count_e:

                    continue

                sum_e = d + e + c_in

                c_out = 1 if sum_e >= 10 else 0

                total_carries += c_out * count_e * freq[c_in]

                next_freq[c_out] += count_e * freq[c_in]

        freq = next_freq

    res = sum_digits_i * n + sum_digits_total - 9 * total_carries

    result.append(str(res))

print(' '.join(result))

This should work.

Now, let's test it against the first sample input.

Sample Input 1:

4

1 3 3 7

sum_digits_total =1+3+3+7=14.

For i=0 (1):

digits_i = [1,0,0,0,0,0,0,0,0,0].

Processing each k:

k=0, d=1.

freq starts as [1,0].

For c_in=0:

e=1: count_e=1 (from the first a_j=1).

sum_e=1+1+0=2 <10 → c_out=0. total_carries +=0*1*1=0.

e=3: count_e=2 (two a_j's have 3 in k=0).

sum_e=3+1+0=4 → c_out=0. total_carries +=0*2*1=0.

e=7: count_e=1 (from a_j=7).

sum_e=7+1+0=8 → c_out=0. total_carries +=0*1*1=0.

Other e's are 0, count_e=0.

Thus, next_freq[0] += 1+2+1=4.

So freq becomes [4,0].

k=1 to 9: digits_i[k] is 0.

At k=1, d=0.

c_in=0:

e=0: count_e=4 (all a_j's have 0 in k=1).

sum_e=0+0+0=0 → c_out=0. total_carries +=0*4*4=0.

next_freq[0] +=4*4=16.

Thus, freq becomes [16,0].

k=2: same as k=1.

next_freq[0] = 16 *4=64.

etc., all other steps contribute 0 to total_carries.

Thus, total_carries is 0.

res =1*4 +14 -0 → 4+14=18.

Which matches the sample.

Thus, the code works.

The code should handle large inputs efficiently, as the preprocessing is O(n*10), and processing each a_i is O(10*2*10) = 200 operations per a_i. For 2e5 a_i's, this is 4e7 operations, which is acceptable.

Thus, this is the optimal approach.
</think>

```python
def get_digits(x):
    s = str(x)[::-1]
    padded = s.ljust(10, '0')[:10]
    return [int(c) for c in padded]

n = int(input())
a = list(map(int, input().split()))

sum_digits = [sum(map(int, str(num))) for num in a]
sum_digits_total = sum(sum_digits)

# Precompute digits for each a_j
digits_j = [get_digits(num) for num in a]

# Precompute cnt[k][e]
cnt = [[0] * 10 for _ in range(10)]
for k in range(10):
    for j in range(n):
        e = digits_j[j][k]
        cnt[k][e] += 1

result = []
for i in range(n):
    digits_i = get_digits(a[i])
    sum_di = sum_digits[i]
    
    freq = [1, 0]
    total_carries = 0
    
    for k in range(10):
        d = digits_i[k]
        next_freq = [0, 0]
        for c_in in (0, 1):
            current_freq = freq[c_in]
            if current_freq == 0:
                continue
            for e in range(10):
                count_e = cnt[k][e]
                if count_e == 0:
                    continue
                sum_e = d + e + c_in
                c_out = 1 if sum_e >= 10 else 0
                total_carries += c_out * count_e * current_freq
                next_freq[c_out] += count_e * current_freq
        freq = next_freq
    
    res = sum_di * n + sum_digits_total - 9 * total_carries
    result.append(str(res))

print(' '.join(result))
```