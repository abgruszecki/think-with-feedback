<think>
Okay, let's tackle this problem. So, the task is to determine how many terms of a geometric progression Masha will write on the board, considering that some terms are bad and she skips them. Also, if the terms keep getting added infinitely without exceeding the limit l, we have to output "inf". 

First, let's understand the problem step by step. The geometric progression starts with b1 and each subsequent term is multiplied by q. The terms are written as long as their absolute value is ≤ l. But any term that's in the bad list is skipped. We need to count all the valid terms that are not in the bad list and are within the absolute value limit. 

But the tricky part is handling cases where there are infinite terms. For example, if the progression keeps cycling between values that are within l and not in the bad list, then it's infinite. Or if after some point, the terms repeat and are all allowed. 

Let me think about possible scenarios where the count is infinite. 

Case 1: The progression term becomes zero. Wait, zero can be in the progression. For example, if q is 0, then after the first term, all terms are zero. If zero is not in the bad list and |0| ≤ l, then those zeros would be added infinitely. But if zero is a bad term, then they are skipped. So, if after a certain term, the progression becomes zero and it's allowed (not in the bad list and |0| ≤ l), then the count is infinite. 

Wait, but if the progression is 0, q is 0, then the terms are 0, 0, 0, etc. So if the initial term is zero, then all terms are zero. So in that case, if zero is allowed (not in bad list and l >=0), then it's infinite. But if zero is in the bad list, then each term is skipped, so the count is zero. 

Another case for infinity is when the progression cycles between values that are allowed. For example, if after some steps, the terms start repeating and all those terms are allowed. Like, if q is 1, then all terms are b1. So if b1 is allowed (not in the bad list and |b1| ≤ l), then it's infinite. Or if q is -1, then the terms alternate between b1 and -b1. If both are allowed, then it's infinite. 

So, the key is to detect whether the progression will enter a cycle of allowed terms. 

So, how do we approach this? 

First, we need to process each term in the progression until it's absolute value exceeds l. For each term, check if it's in the bad list. If not, count it. But for some cases, the progression might loop forever without exceeding l, leading to an infinite count. 

So, the algorithm needs to:

1. Check for infinite cases before processing all possible terms. Because once we detect an infinite loop, we can immediately return "inf".

2. Otherwise, simulate each term until it goes beyond l, but avoiding infinite loops. 

But how to detect infinite loops efficiently? 

Let's think about the possible conditions that lead to infinite terms:

- The progression stays within the absolute limit l forever, and the terms are not in the bad list. 

So, for example:

a) If q is 1: then all terms are b1. If |b1| ≤ l and b1 is not in the bad list, then it's infinite. 

b) If q is -1: then the terms alternate between b1 and -b1. If both are allowed (not in bad list and their absolute values are ≤ l), then it's infinite. 

c) If the progression starts cycling between values (like q=0, leading to terms that are 0 forever after the first term). 

But wait, in the case of q=0, after the first term (b1), the next terms are 0, 0, 0... So if the first term is allowed, then subsequent zeros may or may not be allowed. Wait, no. Wait, the first term is b1. Then next term is b1 * q. So if q is 0, then after the first term (b1), the second term is b1*0=0, third is 0*0=0, etc. So if the first term is, say, 3, l is 5. Then 3, 0, 0, 0... So if 3 is allowed (not in bad list) and 0 is allowed, then the count would be 1 (3) plus infinitely many zeros. But in that case, the total is infinite. But if the first term is 3 (allowed) and 0 is in the bad list, then 3 is counted once, and all 0s are skipped. So the count is 1. 

So, for infinite cases, the key is that the progression will continue generating terms within l, and those terms are allowed (not in the bad list). 

So, the steps to solve this problem:

1. Read the input: b1, q, l, m. Then the m bad numbers. 

2. Check if any of the terms in the progression will be generated infinitely, and whether those terms are allowed. 

But how to model this? Let's think of the possible scenarios where the progression can generate infinitely many terms that are allowed.

Possible scenarios for infinite terms:

- The progression reaches a term that is allowed and then continues to generate terms that are allowed and remain within l. 

So, for example:

- q=1: all terms are b1. If |b1| <= l and not in bad list: infinite.

- q=-1: terms alternate between b1 and -b1. If both are allowed (not in bad list) and their absolute values are <= l: infinite.

- q=0: after the first term (if allowed), the subsequent terms are 0. If 0 is allowed and |0| <= l: infinite.

Wait, but for q=0, the second term is b1 * q = 0. Third term is 0 * q = 0. So if after some term (like the second term) the value becomes 0 and that's allowed, then all subsequent terms are 0, leading to infinite count. 

But to get into this scenario, the terms must keep being allowed and not exceed l.

So, the approach is to check for such possibilities.

So, the steps could be:

- For each term generated in the progression, check if it's allowed and within l. Also, check if in the next steps, the terms start repeating (i.e., the progression enters a cycle of allowed terms).

But simulating all terms until they exceed l is not feasible for cases where the terms are infinite, as it would loop forever. So, we need a way to detect these infinite cases without simulating all terms.

So, perhaps we can precompute possible cases where the progression will generate an infinite number of allowed terms.

Let's list the possible cases:

Case 1: The progression stays at a fixed value (q=1). So:

If |current term| <= l, and current term is allowed, and q=1, then infinite.

Case 2: The progression alternates between two values (q=-1). So:

If current term and next term are allowed and their absolute values are <= l, and q=-1. Then each cycle adds two terms (current and next), and since q=-1, the terms alternate. So, this would generate infinite terms.

Case 3: The progression becomes zero and stays there. For example, if any term is zero, allowed, and |0| <= l, and subsequent terms are zero (so q can be 0, but even if q is something else, if the term is zero and then multiplied by q, it remains zero). So, if after a term, the next terms are zero and allowed, then infinite.

Wait, for example, if the current term is zero, allowed, and l >=0, then all subsequent terms will be zero (since 0 * q = 0). So in that case, if zero is allowed (not in bad list), then infinite.

So, these are the main cases. So during the simulation of the terms, if any of these scenarios is encountered, we can return "inf".

But how to check for these cases during the progression?

So, the plan is:

For each term generated, before adding it to the count, check if this term is allowed and within l. Then, check if the next term would be the same (q=1) leading to infinite terms, or alternates (q=-1), etc. 

But the problem is, how to detect these cases early, without having to simulate all terms. Because in the worst case, the progression could have a cycle after some steps, but we need to detect that.

Alternatively, after generating each term, check whether the next term would repeat a value that's already allowed, leading to an infinite loop.

So, here's the approach:

We can track the terms generated so far. If a term is allowed, and the next term is the same as a previous allowed term (and so on), leading to an infinite loop. But for a geometric progression, the next term is determined by multiplying by q. So, if after a term 'x', the next term is x * q, and then x * q * q, etc. So, unless q is 1 or -1, the terms can keep changing. 

Wait, but for example, if q is 2 and the term is 1, then the next terms are 2,4,8... but once the term exceeds l, it stops. So infinite only if terms stay within l and are allowed.

But for some q values, like 0, the progression could become zero. 

So, perhaps the steps are:

1. Check if the initial term (b1) is outside l. If yes, output 0.

2. Otherwise, proceed to generate terms, checking each term's validity.

But to avoid infinite loops, during each step, after generating a term, check if adding this term could lead to an infinite loop. For example:

For the current term 'current_b', check if:

a) current_b is allowed and within l.

b) The next term (current_b * q) will have absolute value <= l.

c) The next term is the same as current_b (so q=1). Then, if current_b is allowed, this would generate infinite terms.

Or, if q is -1, the next term is -current_b. If both current_b and -current_b are allowed, and their absolute values are <= l, then infinite.

Or, after some steps, the term becomes zero. Then, if allowed, all subsequent terms are zero, leading to infinite.

So, during each iteration, after adding a term (if allowed), we need to check whether the next terms will repeat in a way that allowed terms are generated infinitely.

So, the algorithm could be:

Initialize count to 0.

Create a set of bad numbers for O(1) lookups.

Keep track of terms we've already seen. If a term repeats, and the progression is such that it will keep cycling through those terms, which are allowed, then return 'inf'.

But since the problem allows m up to 1e5, using a set is feasible.

So, steps:

1. Check if the absolute value of the current term exceeds l. If yes, break.

2. Check if the current term is not in the bad set. If yes, count +=1.

3. Now, check if the next term would cause the progression to enter a loop that allows infinite terms. For example:

   a) If q is 1:

      Then, next term is same as current. So, if current is allowed (counted), and next term's absolute value is <= l, and current is not in the bad set, then infinite.

   b) If q is -1:

      Next term is -current. Then, if both current and -current are allowed, and their absolute values are <= l, and next term's absolute value is <= l, then infinite.

   c) If q is 0:

      Then next term is 0, and all subsequent terms are 0. So if current term is allowed (and not in bad list), and after multiplying by q (0) gives 0, which is allowed, then infinite.

But how to check all possible scenarios?

Alternatively, after generating each term, check if the next term would lead to an infinite loop. For example:

For the current term b_i:

- Compute next term: b_i * q.

- Check if next term's absolute value is <= l.

   - If yes, and the next term is the same as the current term (q=1), then check if current term is allowed. If so, then infinite.

   - If next term is different, but after some steps, the terms start repeating. But for a geometric progression, unless q is 1, -1, or 0, the terms may not repeat. 

Wait, for example, if q is 2, then the terms will keep increasing (unless |b1| is 0). So unless |b1| * |q|^k <= l for all k, but that's possible only if |q| <=1.

But for |q| <1, the terms approach zero. But unless q is 0, but in that case, once a term is zero, all subsequent are zero.

Hmm. This seems complicated.

So, perhaps the way to approach this is: after each term generated, check if the next term would result in a cycle that allows infinite terms.

So, for each term b_i:

If after processing b_i, the next term is such that:

- |next_b| <= l.

- next_b is allowed (not in bad set).

And, the progression will cycle between terms that are allowed and within l.

Wait, but how to check that? 

Alternatively, after processing the current term, compute the next term and see if the progression can generate terms infinitely from this point. 

For example:

If current term is x, next term is x*q. If x*q is allowed and |x*q| <= l, and the next term after that is x*q*q, and so on. But unless q is 1, 0, or -1, the terms will change each time.

So, only in cases where q is 1, 0, or -1, the terms can cycle or stay the same.

So, let's check for each of these cases:

Case 1: q == 1

In this case, all terms are x = current term. If x is allowed and |x| <= l, then infinite terms. Otherwise, if x is allowed, then each subsequent term is x, leading to infinite count. But wait, if x is allowed, then all terms are x, and since they are allowed, each term is counted. So if the current term x is allowed and |x| <= l, then the count is infinite. So in this case, during processing the first term (b1), if q is 1 and |b1| <= l and b1 is not in the bad set, then output is 'inf'. Because all subsequent terms are the same, and are allowed.

Case 2: q == -1

In this case, the terms alternate between x and -x. So after processing x, the next term is -x, then x again, etc. So if both x and -x are allowed and their absolute values are <= l, then the count is infinite. Because each pair of terms (x, -x) will be added, and since they are allowed, this repeats infinitely.

Case 3: q == 0

In this case, the next term is zero. Then, all subsequent terms are zero. So:

If the next term (zero) is allowed and |0| <= l, then after the current term, all zeros are allowed, leading to infinite count.

So, for example, if current term is x (allowed), and q is 0. Then, next term is x*0=0. If 0 is allowed and |0| <= l, then the next term is allowed, and all subsequent terms are 0 (allowed), so count is infinite.

But wait, the current term x could be the first term. For example, if the initial term is 5, q is 0, l is 10. So the terms are 5, 0, 0, 0... So if 5 is allowed and 0 is allowed, then the count is 1 (for 5) plus infinitely many zeros. So in this case, the total is infinite.

So, during processing the current term x, if the next term is 0 and allowed, then infinite.

But how to check all these cases?

So, the approach could be:

For each term generated, check if adding it to the count (if allowed) and then check if the next term would create an infinite loop. 

So, here's the plan:

1. Read the input values.

2. Convert the bad numbers into a set for O(1) lookups.

3. Check if |b1| > l: if yes, output 0.

4. Else:

   a. Initialize count to 0.

   b. Keep track of terms we have seen to detect cycles. But since geometric progression can have terms that grow exponentially, storing all terms could lead to memory issues. So we need another approach.

   c. For each term in the progression:

      i. If the absolute value exceeds l: break.

      ii. If the term is not in the bad set: increment count.

      iii. Compute the next term as current * q.

      iv. Check if after this term, the progression could generate infinitely many terms. 

          So, check the following scenarios:

          - If q == 1:

              The next term is same as current. So, if current is allowed (not in bad) and |current| <= l, then infinite.

          - If q == -1:

              The next term is -current. If current and -current are allowed, and their absolute values are <= l, then infinite.

          - If next term is 0:

              Check if 0 is allowed (not in bad) and |0| <= l. If yes, then next term is 0, and all subsequent terms are 0. So infinite.

          Also, after checking these, we need to make sure that the next term's absolute value is <= l. Otherwise, even if the conditions are met, but the next term exceeds l, then it's not infinite.

      v. If any of these scenarios is true and the next term's absolute value is <= l, then return 'inf'.

      vi. Else, proceed to the next term.

      vii. Check if the next term is same as current term (to prevent infinite loops). For example, if the progression is stuck in a loop, but the terms are allowed, but we haven't covered the scenarios above.

      Wait, but for other q values, like q=2, the terms will keep growing. So even if the next term is allowed, but after that, it exceeds l, then no problem.

So, the key is to check after each term whether the next term would lead to an infinite loop. So, during step iv, after generating a term, check if the next term would fall into one of the infinite scenarios.

So, during each iteration:

current_b = term being processed.

next_b = current_b * q.

if next_b is allowed and |next_b| <= l:

   check for infinite scenarios.

   if any of the scenarios applies, output 'inf'.

So, the code could look like:

current = b1

seen = set()

while True:

   if abs(current) > l:

      break

   if current not in bad_set:

      count +=1

   next_term = current * q

   # Check for infinite scenarios

   if next_term in allowed and abs(next_term) <= l:

      check cases:

      case1: q == 1. Then, next_term is same as current. So if current is allowed and next_term is allowed, then infinite.

      case2: q == -1. Then, next_term is -current. So if current and next_term are allowed, then infinite.

      case3: next_term is 0. Then, all subsequent terms are 0. So if 0 is allowed, then infinite.

   if any of the cases is true, output 'inf' and exit.

   current = next_term

But wait, how to check if next_term is allowed? Because next_term could be in the bad list.

Wait, in the code, after generating next_term, check whether it is allowed (not in the bad list) and its absolute value is <= l.

So, for example, in case of q=1:

current is allowed (so current not in bad set). next_term is current. So next_term is allowed. If |next_term| <= l, then the next term is allowed. Then, since q=1, all subsequent terms are current. So, infinite.

But in code, after processing current term, compute next_term. If next_term is allowed and |next_term| <= l, and q=1, then yes, infinite.

So, the code would check:

if (next_term is allowed) and (abs(next_term) <= l) and (q == 1):

   output 'inf'

Similarly for other cases.

But how to code these checks?

Let me outline the steps in code:

After generating next_term:

if (abs(next_term) <= l) and (next_term not in bad_set):

   then, check for infinite scenarios.

   check:

   if (q == 1) and (current == next_term):

       # then, all subsequent terms are next_term, which is allowed and within l. So infinite.

       print("inf")

       exit()

   elif (q == -1) and (next_term * q == current):

       # the terms alternate between current and next_term. So check if both are allowed.

       if (current not in bad_set) and (next_term not in bad_set):

           print("inf")

           exit()

   elif (next_term == 0):

       # after next_term, all terms are 0. So check if next_term is allowed (already checked) and 0 is allowed (since next_term is allowed), then all terms after are 0, allowed. So infinite.

       print("inf")

       exit()

Wait, but in the case of q=0, next_term is 0. Then, after that, all terms are 0. So if next_term is allowed (not in bad set), then infinite.

But in code, the check for next_term is allowed and within l would have already been done. So, if next_term is allowed (since we checked next_term not in bad set), then all terms after next_term are 0, which are allowed and within l. So, the count would be infinite.

So, in code, if next_term is 0 and allowed and within l, then infinite.

So, during processing each term, after generating next_term, if next_term is allowed and within l, we check these conditions.

But also, we need to check whether the next_term's absolute value is <= l. Because even if next_term is 0, but l is negative (but l is given as >=1 in the problem statement). Wait, the problem says 1 ≤ l ≤ 1e9. So l is always >=1. So |0| =0 ≤ l. So if next_term is 0 and allowed, then it's within l.

So, the code steps would be:

For the current term, after processing it (checking if allowed and adding to count), generate next_term.

Check if next_term is allowed and within l (abs(next_term) <= l and not in bad_set). 

If yes, then:

Check for q ==1: next_term is same as current. So, the terms will repeat. So, infinite.

Check for q ==-1: next_term is -current. So, the terms alternate between current and next_term. If both are allowed, then infinite.

Check if next_term is zero. Then, all subsequent terms are zero. So, infinite.

If any of these is true, output 'inf'.

But how to structure this in code.

Alternatively, for the next_term:

if next_term is allowed and within l:

   if q == 1:

       print("inf")

       exit()

   elif q == -1:

       # check if current is allowed, next_term is allowed, and next_term * q == current (i.e., next_term is -current)

       if (current not in bad_set) and (next_term not in bad_set) and (next_term * q == current):

           print("inf")

           exit()

   elif next_term == 0:

       print("inf")

       exit()

Wait, but in the case of q=0:

current term is x, next_term is 0. If 0 is allowed, then next_term is allowed. Then, the next terms after that are 0*0=0, so all zeros. So infinite.

So, whenever next_term is 0 and allowed, output 'inf'.

But wait, what if current term is 3, q=0, l=5. So next_term is 0. If 0 is allowed, then after this, all terms are 0, so infinite. So yes, in this case, output 'inf'.

So, the code can check for next_term being 0 and allowed. So, whenever next_term is 0, and allowed, and |0| <= l (which it is, since l >=1), then output 'inf'.

But wait, l can be 0? Wait, according to the problem statement, the input constraint for l is 1 ≤ l ≤ 1e9. So l is always >=1. So 0's absolute value is 0 <= l. So, if next_term is 0 and allowed, then output 'inf'.

So, in code:

after processing current term, compute next_term.

if next_term is allowed (not in bad set) and abs(next_term) <= l:

   if q ==1:

       then, all subsequent terms are next_term (same as current). So infinite.

   elif q ==-1 and next_term * q == current:

       then terms alternate between current and next_term. So if both are allowed, infinite.

   elif next_term == 0:

       then all subsequent terms are 0, which is allowed and within l. So infinite.

So, code steps:

if next_term not in bad and abs(next_term) <= l:

   if q == 1:

       print("inf")

       exit()

   elif q == -1 and next_term == -current:

       if current not in bad and next_term not in bad:

           print("inf")

           exit()

   elif next_term == 0:

       print("inf")

       exit()

But wait, the first condition (next_term not in bad and abs(next_term) <= l) already checks that next_term is allowed. So for the q=-1 case:

next_term is allowed. current is allowed if the current term was allowed (but current is the term we just processed). Wait, current could be in the bad set. Because in the code, when we process current, we check if it is allowed. But the next_term is allowed only if next_term is not in the bad set.

So, for the q=-1 case:

current term could be in the bad set. For example, current is in the bad set, but next_term is allowed. Then, in the next iteration, next_term (allowed) is processed, and the next next term is next_term * q = next_term * (-1). So, that term would be -next_term. If that term is allowed, then we have a cycle.

But in code, when processing the next_term (allowed), we check for q=-1 and see if the next term is allowed.

But perhaps the code is overcomplicating. Maybe the code should, after generating next_term (allowed and within l), check if the progression can generate infinite terms. 

But perhaps the code can handle the three cases:

Case 1: next_term is allowed, and q=1. Then, all subsequent terms are next_term. Since next_term is allowed, it's infinite.

Case 2: next_term is allowed, q=-1, and next_term * q == current (i.e., next_term is -current). Then, the next next term is next_term * (-1) = current. So if both current and next_term are allowed, then the terms alternate, leading to infinite count.

Case 3: next_term is allowed and is zero, leading to infinite zeros.

So, in code:

after generating next_term and checking it's allowed and within l:

if q == 1:

   # since next_term is allowed and same as all future terms, infinite

   print("inf")

   exit()

elif q == -1 and next_term == -current:

   # check if current is allowed

   if current not in bad_set:

       # then, next_term is allowed, current is allowed, and terms alternate. So infinite.

       print("inf")

       exit()

elif next_term == 0:

   print("inf")

   exit()

But wait, in the q=-1 case, the current term may or may not be allowed. For example, current term is allowed, but next_term is allowed. Then, the next term (current * q) is -current. If next_term is allowed, but current term is allowed, then when processing next_term, which is allowed, the next next term will be current again. So if current is allowed and next_term is allowed, then the cycle continues. So, in this case, after processing current term (allowed), and next term (allowed), the code would check q=-1 and see if next_term is -current. If so, then check if current is allowed (which it is, since we processed it and added to count) and next_term is allowed (which it is). Then, the code returns 'inf'.

But how to implement this.

Alternatively, during processing the current term:

if next_term is allowed and within l:

   if q is 1:

       then return 'inf'

   elif q is -1 and next_term is -current:

       then check if current is allowed and next_term is allowed. Since next_term is allowed (as per initial check), and current is allowed if current is not in bad set. But current is the current term being processed. So, during processing current term, we have checked if it's allowed (and added to count). So, if current is allowed (current not in bad set), then:

       after next_term (allowed) is processed, the next next term is current again (since next_term * q = -current * (-1) = current). So, if current is allowed and next_term is allowed, then each time the terms cycle between current and next_term. So, if both are allowed, then infinite.

   elif next_term is 0:

       return 'inf'

So, in code:

if next_term is allowed and within l:

   if q == 1:

       print('inf')

   elif q == -1 and next_term == -current:

       if current not in bad_set:

           print('inf')

   elif next_term == 0:

       print('inf')

   exit in all cases.

But how to structure this.

Let me try to code this step by step.

First, read the inputs.

b1, q, l, m = map(int, input().split())
bad = set(map(int, input().split()))

Then, check if |b1| > l. If so, output 0.

current = b1
count = 0

But wait, need to process each term:

So, the loop will process each term until it exceeds l. But need to avoid infinite loops.

But in some cases, the terms can loop without exceeding l. So, to prevent infinite loops, we need to track the terms we have seen before. If a term is repeated, and the progression is entering a cycle, but we haven't detected the infinite conditions earlier, then it's a cycle of terms that are allowed but not covered by the earlier checks. For example, if q=2 and the progression is 2, 4, 8, 16, etc., but l is large enough. But this is not possible because the terms would eventually exceed l. But if l is infinity (but l is given as up to 1e9). So, perhaps, in practice, the loop will eventually exit.

But for the problem constraints, the terms can grow exponentially, leading to the loop running O(log l) times. For example, if b1 is 1, q is 2, l is 1e9. The number of terms is log2(1e9) ~30. So it's manageable.

But if q is 1, then the terms are all b1. So, the loop would run indefinitely. So, the code must handle the cases where the progression can generate infinite terms before entering the loop.

So, the code structure:

current = b1

seen = set()

count = 0

if abs(current) > l:

    print(0)

    exit()

while True:

    # Check if current term is within l.

    if abs(current) > l:

        break

    # Check if current is allowed.

    if current not in bad:

        count +=1

    # Compute next term.

    next_term = current * q

    # Check if next term is allowed and within l.

    next_allowed = (abs(next_term) <= l) and (next_term not in bad)

    # Check for infinite conditions.

    if next_allowed:

        if q == 1:

            print("inf")

            exit()

        elif q == -1 and next_term == -current:

            if current not in bad:

                print("inf")

                exit()

        elif next_term == 0:

            print("inf")

            exit()

    # Check for cycles. If current has been seen before, it's a cycle. But if the terms in the cycle are not allowed, then it's not infinite.

    # But how to track this. For example, if current is seen again, but the next terms are the same, and are allowed, but not covered by the earlier checks.

    # For example, q=2 and current = 1, l is 1e9. Then the terms are 1, 2,4,8... which eventually exceed l. But if l is very large, but in code, the loop will generate all terms until they exceed l.

    # So, perhaps, to prevent infinite loops, we can track the terms we've seen. If a term repeats, then it's a cycle. But for geometric progression, the only way terms repeat is if q is 1, -1, or 0. But those cases are already covered by the earlier checks.

    # For example, q=1: terms are same. Checked earlier.

    # q=-1: terms alternate between current and -current. Checked earlier.

    # q=0: after next term, terms are 0. Checked earlier.

    # So, for other q values, the terms will either grow or shrink, and eventually exceed l.

    # So, in the loop, if the current term is added to 'seen', and then appears again, then we can break the loop (but how?).

    # Alternatively, the code can proceed to generate terms until the next_term exceeds l or the current term repeats.

    # But how to handle terms that repeat but aren't in the infinite cases.

    # For example, q=2, current term is 3, next term is 6, then 12, etc. No cycles here.

    # So, the code can proceed to generate terms until the next term exceeds l.

    # So, the code:

    # Update current to next_term.

    # Check if current is in 'seen' (to detect cycles not covered by earlier checks). If yes, break.

    # Else, add to 'seen'.

    # But how to manage 'seen' when the terms are generated exponentially. For example, terms could be up to 1e30, which can't be stored in a set.

    # So, this approach is not feasible. So, perhaps, we can limit the number of iterations to a certain threshold. Like, after 1e5 iterations, break and assume no infinite loop. But this is risky.

    # Alternative idea: the code will process the terms until either the term exceeds l or it has processed a certain number of steps (say 100) steps. Because for cases where the progression can generate infinite terms, the conditions must be met within a few steps. For example, if q=1, the next term is same as current. So, after one iteration, the code would detect the infinite case. Similarly for q=-1 and q=0.

    # So, if after, say, 1e4 iterations, the code is still not in an infinite scenario, then it's safe to assume that the terms will eventually exceed l.

    # But how to choose the threshold. Because for example, if l is 1e9 and q is 2, the maximum number of steps is log2(1e9) ≈ 30.

    # So, perhaps, a threshold of 100 steps is sufficient.

    # So, the code can track the number of steps and break after a certain threshold.

    # But the problem is, how to handle cases where the progression is infinite but not covered by the earlier checks. For example, a cycle of 3 terms allowed. But this can't happen in a geometric progression unless q is a root of unity, which in integer terms, only possible for q=1 and q=-1. So, for other q values, cycles of longer length are impossible. So, the earlier checks for q=1, q=-1, and q=0 cover all possible infinite cases.

    # Therefore, in code, once the next_term is computed and the infinite checks are done, the current is updated to next_term. If this process continues and the next_term exceeds l, then the code breaks and outputs the count.

    # So, the code can proceed as follows:

    # Update current to next_term.

    current = next_term

    # Check if current is in seen. If yes, then there's a cycle. But if the code hasn't detected the infinite case, then the terms in the cycle must not be allowed. So, the code can break.

    if current in seen:

        break

    seen.add(current)

But wait, the 'seen' set can grow indefinitely. For example, if q=2 and l is large. So, storing all terms in 'seen' is not feasible for large l.

So, perhaps, the code should not track 'seen' terms. Because, for a geometric progression with |q| > 1, the terms will eventually exceed l. For |q| < 1, the terms will approach zero, but unless q is 0, they will not cycle. So, the only possible cycles are covered by the earlier checks (q=1, q=-1, q=0). Therefore, the code can proceed without tracking seen terms. Because in other cases, the terms will either grow or shrink until they exceed l. 

So, the code can safely loop until the current term exceeds l. Because if the code hasn't detected the infinite cases, then the terms must eventually exceed l.

So, the code can be structured as:

current = b1

count = 0

bad_set = set(bad)

if abs(current) > l:

    print(0)

    exit()

steps = 0

max_steps = 100

while steps < max_steps and abs(current) <= l:

    # process current term

    if current not in bad_set:

        count +=1

    # compute next term

    next_term = current * q

    # check for infinite conditions

    if abs(next_term) <= l and next_term not in bad_set:

        if q == 1:

            print("inf")

            exit()

        elif q == -1 and next_term == -current:

            if current not in bad_set:

                print("inf")

                exit()

        elif next_term == 0:

            print("inf")

            exit()

    current = next_term

    steps +=1

    # check if current exceeds l

    if abs(current) > l:

        break

print(count)

Wait, but this approach may not handle all cases. For example, suppose after max_steps steps, the terms are still within l, but not in an infinite loop. Then, the code will break and output the current count, but there might be more terms. 

But this approach is risky. Because, for example, if the progression is allowed to have terms for more than max_steps steps, but each term is allowed, then the code will output an incorrect count. 

But according to the problem statement, the time limit is 1 second, and Python can handle about 1e6 operations per second. So, setting a higher max_steps, like 1e5, might be feasible. But considering that the terms can be up to l = 1e9 and q can be 2, the number of steps needed to reach l is about log2(1e9) ~30 steps. So, even setting max_steps to 100 is more than enough. 

But in cases where the progression can have a lot of terms within l, but not infinite, the code would need to process all of them. For example, if q is 1 and current term is allowed, but the code didn't detect the infinite case. But that's impossible because in the code, when q is 1, the code checks if next_term is allowed and within l, and if so, outputs 'inf'.

Wait, in the code above, after processing current term, compute next_term. If next_term is allowed and within l, and q is 1, then the code outputs 'inf'.

So, for example, if current term is allowed, and next_term is same as current (q=1), then code outputs 'inf'.

But what if current term is allowed, but next_term is allowed and q=1. Then, code outputs 'inf'.

Yes.

So, the code will correctly detect the infinite cases for q=1, q=-1, and q=0. For other cases, the terms will eventually exceed l after a finite number of steps. 

So, the code can safely process the terms in a loop until either the current term exceeds l, or until a certain number of steps (like 100) to avoid infinite loops. 

But why 100 steps? Because for q=2, even with l=1e9, the maximum steps would be log2(1e9) ≈30. For q=3, even less. So 100 steps is more than enough. 

But what if the code needs to process more than 100 steps? For example, if q is 1/2 and current term is 1. Then, the terms would be 1, 0.5, 0.25, etc. But since the problem states that the progression terms are integers. Wait, the problem says that the progression is defined by integers b1 and q. So, the terms are integers. Because the input constraints are that b1 and q are integers. 

Wait, the problem statement says that b1 and q are integers. So, all terms are integers. 

So, if q is a fraction, like 1/2, but the problem says q is an integer. So, q must be integer. 

Ah, that's an important point. Because all terms are integers. So, the code doesn't have to handle non-integer terms. 

So, for example, if q is 2, then terms are integers. If q is 0, then terms are 0 after the first term. 

So, given that, the code can proceed to generate the terms until either the term exceeds l, or a step limit is reached to avoid infinite loops.

But the question is, can the code enter an infinite loop? For example, if the progression cycles between allowed terms, but the code didn't detect it via the earlier checks.

But according to the problem statement, since q is integer, the only possible cycles are when q is 1, -1, or 0. Because for any other q, the terms will either grow or shrink, and eventually exceed l. 

For example, if q is 2, the terms will grow exponentially. 

If q is -2, the terms alternate in sign and grow in magnitude. So, the absolute value will eventually exceed l. 

So, in code, after generating a term, check if it's allowed and within l. Then, compute next_term. Check the infinite conditions. 

Thus, the code can proceed to generate terms until the current term exceeds l. The code doesn't need to track seen terms, because the only possible infinite loops are those already checked. 

So, the code can be:

current = b1

count = 0

bad_set = set(bad)

if abs(current) > l:

    print(0)

    exit()

while True:

    if abs(current) > l:

        break

    # Check if current is allowed.

    if current not in bad_set:

        count +=1

    # Compute next term.

    next_term = current * q

    # Check for infinite conditions.

    if abs(next_term) <= l and next_term not in bad_set:

        # Check for q ==1

        if q == 1:

            print("inf")

            exit()

        # Check for q ==-1 and next_term is -current.

        elif q == -1 and next_term == -current:

            # Check if current is allowed.

            if current not in bad_set:

                print("inf")

                exit()

        # Check if next_term is zero.

        elif next_term == 0:

            print("inf")

            exit()

    # Update current.

    # But what if next_term is same as current? (q=1)

    # But in that case, the code would have already detected and exited.

    current = next_term

    # Check if the loop is repeating.

    # For example, if current is same as previous term, but q=1 (but code already checked q==1 and exited).

    # So, the code can proceed.

    # To prevent infinite loops, check if next_term's absolute value is same as current's (for q=1 or q=-1), but code would have handled those cases.

    # For example, if q=1 and code is here, then next_term is allowed but code didn't detect infinite, which can't happen.

    # So, perhaps, the code can proceed.

But wait, after processing the current term, the code updates current to next_term. Then, in the next iteration, current is processed. 

But this can loop indefinitely if the code doesn't detect the infinite cases.

For example, suppose q=1, current term is allowed, but the next term is allowed and within l. Then, in the infinite condition check, the code would have printed 'inf' and exited. So, why are we here?

Ah, because the code is processing the current term, then generates next_term, checks for infinite conditions. If the condition is met, code exits. Otherwise, current is updated to next_term.

So, the loop will proceed to process the next_term.

But, in the case where the code has missed an infinite loop scenario, the loop could run forever. For example, in the code, if the progression is allowed to cycle between terms that are allowed, but the code's infinite check didn't cover that.

But according to the earlier analysis, such scenarios can only occur when q is 1, -1, or 0. Which are already covered in the infinite checks.

So, the code should handle all possible cases of infinite terms. 

So, in code:

current = b1

count = 0

bad_set = set(bad)

if abs(current) > l:

    print(0)

    exit()

steps = 0

while steps < 100: # limit steps to prevent infinite loops.

    if abs(current) > l:

        break

    # Check if current is allowed.

    if current not in bad_set:

        count +=1

    next_term = current * q

    # Check for infinite conditions.

    if abs(next_term) <= l and next_term not in bad_set:

        if q == 1:

            print("inf")

            exit()

        elif q == -1 and next_term == -current:

            if current not in bad_set:

                print("inf")

                exit()

        elif next_term ==0:

            print("inf")

            exit()

    current = next_term

    steps +=1

# After the loop, check if current is still within l. If yes, but steps have exceeded, then there's a possibility of infinite terms. But according to our analysis, this is not possible.

print(count)

Wait, but this code could have steps up to 100. But if the progression is allowed to have more than 100 terms within l, then this code would break early and output an incorrect count.

But for example, if the progression is 1, 0, 0, 0... but the code allowed steps up to 100. For this case, after the first iteration, next_term is 0, which is allowed. The code would check for next_term ==0, output 'inf' and exit. So that's handled.

So, the code may not need a steps limit. Because the only possible infinite loops are those where the code correctly detects and exits. For other cases, the terms will eventually exceed l.

But in practice, what if the code processes a term that is within l, but the next term is also within l, and so on, but the code's infinite check didn't catch it? For example, if q is 1 and the code's infinite check for q==1 is triggered. But if q is 1 and the next_term is allowed, then the code would have printed 'inf' and exited.

So, perhaps the code can proceed without a steps limit. 

But, to avoid infinite loops in code, perhaps it's better to have a steps limit. 

But how to determine what that limit should be. 

The maximum possible number of terms in the progression before exceeding l is log_|q|(l / |b1|). For example, if |b1|=1, q=2, l=1e9, then the number of terms is log2(1e9) ≈30. So, even with a steps limit of 100, it's more than enough.

So, the code can proceed with a steps limit of 100. 

Thus, the code will loop up to 100 times. If after that, the current term is still within l, the code will exit the loop and output the current count. 

But this can lead to incorrect results if there are more than 100 terms. 

But according to the problem's examples and constraints, this is not possible. For example, in the third sample input:

123 1 2143435 4
54343 -13 6 124

Here, q is 1. So, all terms are 123. So, the code will process current=123, next_term=123*1=123. Then, check if next_term is allowed (since bad list is 54343, -13, 6, 124). So, next_term is 123, which is not in the bad set. So, q=1, so code outputs 'inf'.

So, the code works correctly.

Another example where q=2, b1=1, l=1e9. The code will process the terms 1, 2,4,8, ..., until the term exceeds l. Which for 1e9 is 2^30 is about 1e9, which is 30 steps. So the code will process 30 steps and output the count.

So, the code with steps limit of 100 is sufficient.

But what if the code has steps limit of 100 and the progression has more than 100 terms within l? For example, q=0, b1=0, l=1e9. So, the terms are 0, 0, 0... So, the code would process current=0 (allowed), next_term=0. Check next_term is allowed. Since q=0, code would check if next_term is zero. So, code outputs 'inf'.

So, this is handled.

Another case: q=0, b1=5, l=1e9. The terms are 5, 0, 0, 0... So, after processing 5 (allowed), next_term is 0. If 0 is allowed, code outputs 'inf'. Otherwise, count is 1. So handled.

Thus, the code with steps limit of 100 is sufficient.

So, the code can be written as:

Read the input.

Check if b1's absolute value is > l: output 0.

Else, initialize count to 0.

Loop steps up to 100:

   process current term.

   compute next term.

   check for infinite conditions.

   update current.

So, the code:

b1, q, l, m = map(int, input().split())
bad = set(map(int, input().split()))

current = b1
count = 0
bad_set = bad

if abs(current) > l:
    print(0)
    exit()

steps = 0
max_steps = 100  # Adjust this if needed.

while steps < max_steps and abs(current) <= l:
    if current not in bad_set:
        count +=1

    next_term = current * q

    # Check for infinite conditions
    if abs(next_term) <= l and next_term not in bad_set:
        if q == 1:
            print("inf")
            exit()
        elif q == -1 and next_term == -current:
            if current not in bad_set:
                print("inf")
                exit()
        elif next_term == 0:
            print("inf")
            exit()

    current = next_term
    steps +=1

    # Check if current exceeds l after update
    if abs(current) > l:
        break

print(count)

But what about the following case: 

q= -1, current term is 2, bad_set doesn't include 2 or -2. l is 3.

The terms would be 2, -2, 2, -2, etc. 

In the code:

current = 2 (allowed, count +=1)

next_term = -2 (allowed and within l).

Check for infinite conditions:

q ==-1 and next_term ==-current (true).

current is allowed (yes).

so, code prints 'inf' and exits.

Yes.

Another example: q=1, current term is 5, allowed. l is 10.

next_term is 5 (allowed). code checks q ==1 and next_term allowed. So code prints 'inf'.

Yes.

Another example: q=0, current term is 3. bad_set does not include 0. l is 10.

next_term is 0 (allowed). code checks next_term is zero. So, prints 'inf'.

Yes.

So, the code works for these cases.

Testing the sample inputs:

Sample 1:

Input:
3 2 30 4
6 14 25 48

Progression terms: 3, 6, 12, 24, 48, ... 

But l=30. So terms are 3 (allowed), 6 (bad), 12 (allowed?), 24 (allowed?), 48 (exceeds l). 

But in the input, the bad numbers are 6,14,25,48. So:

3: allowed. Count 1.

next_term=6 (bad), but in code, the check for infinite conditions is not met. So code proceeds.

current becomes 6. steps=1. 6's absolute value is 6 <=30. But since 6 is in bad_set, it's not counted. 

next_term=6*2=12. Check if 12 is allowed and within l. 

12 is not in bad_set (since bad numbers are 6,14,25,48). So yes. 

Check for infinite conditions: q=2, next_term=12. So, no. So code continues.

current becomes 12. steps=2. 

12 is allowed. count becomes 2.

next_term=24. allowed. Check infinite conditions. q=2, no. 

current becomes 24. steps=3. 

24 is allowed. count becomes 3.

next_term=48. 48 is in bad_set. 

Check infinite conditions: next_term is 48, which is not in bad_set? No, 48 is in bad_set. So code doesn't check. 

current becomes 48. steps=4. 

48's absolute value is 48 >30. So loop breaks. 

Final count is 3. Which matches sample 1.

Sample 2:

Input:
123 1 2143435 4
123 11 -5453 141245

q=1. So all terms are 123. 

current=123. allowed? Bad_set includes 123, so no. count remains 0.

next_term=123. Check infinite conditions: q=1, next_term is 123. But next_term is in bad_set. So code does not print 'inf'. 

current becomes 123. steps=1. 

Again, check if allowed: no. count remains 0. 

This loop will continue. But in code, steps is limited to 100. 

But after the first iteration:

In the code:

current is 123. allowed? No. count remains 0.

next_term is 123.

check if next_term is allowed: 123 is in bad_set. So no.

code proceeds. current is 123 again.

steps increments to 1.

In the next iteration, current is 123 again. steps=2.

This would loop until steps reach 100. 

But since q=1, and next_term is 123, which is in bad_set, the code's infinite check is not triggered. 

Thus, after 100 steps, the loop breaks and count is 0. 

Sample 2's output is 0. Which is correct.

Sample 3:

Input:
123 1 2143435 4
54343 -13 6 124

current=123. allowed? Yes, since not in bad_set.

count=1.

next_term=123. q=1. 

check infinite conditions: next_term is allowed (123 not in bad_set), q=1. So code prints 'inf' and exits.

Thus, sample 3's output is 'inf'.

Thus, the code works for the samples.

Another test case: 

Input: 

0 5 5 1 

10 

So, b1=0, q=5, l=5, bad_set={10}. 

The terms are 0, 0*5=0, 0*5=0, etc. 

current=0. allowed (not in bad_set). count=1.

next_term=0. allowed (0 not in bad_set). 

Check infinite conditions: next_term is 0. So code prints 'inf' and exits. 

Thus, output is 'inf'.

Another test case:

Input:

5 0 10 2 

0 5 

Progression terms:5,0,0,...

current=5. allowed? 5 is in bad_set? bad_set contains 0 and 5. So yes. So count remains 0.

next_term=0. allowed (0 is in bad_set? Yes. So no.

code proceeds. current becomes 0. steps=1.

abs(0) <=10. 

current is 0: allowed? No. count remains 0.

next_term=0. allowed? No. code proceeds.

steps increments to 2.

current is 0. steps=2.

This will loop until steps=100.

But in each iteration, current is 0, which is in bad_set. So count remains 0.

Thus, output is 0.

Another test case:

Input:

5 -1 10 1 

-5 

Progression terms:5, -5, 5, -5,...

current=5: allowed (not in bad_set). count=1.

next_term=-5. allowed? bad_set has -5. So no.

code proceeds. current becomes -5. steps=1.

abs(-5) <=10. 

current=-5 is in bad_set. count remains 1.

next_term=5. allowed. 

Check infinite conditions: q=-1, next_term == -current (current is -5. next_term=5. next_term * q = 5 * -1 = -5 == current. So yes.

current is not in bad_set (current is -5, which is in bad_set). So code does not print 'inf'.

Thus, in this case, the code proceeds.

current becomes 5. steps=2.

current is allowed. count=2.

next_term=-5. allowed? No.

code continues.

Thus, after steps reach 100, code outputs count=50 (since each pair of steps adds 1 to count). But in reality, the code would process 50 pairs of 5 and -5 (allowed only 5), so count increases by 1 each two steps. 

But in this test case, the bad_set includes -5. So each term is 5 (allowed) and -5 (bad). So code counts every other term. So after 100 steps, the code would have processed 50 terms (5) and 50 terms (-5). So count=50. But the code would output 50.

But according to the problem statement, the correct answer is 'inf' if the terms alternate between allowed and not allowed. But in this case, the code would not detect infinite conditions. 

Wait, let's see:

current term is 5 (allowed). 

next_term = 5 * -1 = -5. 

Check if next_term is allowed: -5 is in bad_set. So no.

Thus, code proceeds. 

current becomes -5. steps=1.

current is -5, allowed? No. 

next_term=-5 *-1=5. allowed? Yes.

Check for infinite conditions:

next_term=5. allowed and within l.

q=-1. next_term ==-current? current is -5. next_term is 5. So yes.

current is not in bad_set? current is -5, which is in bad_set. So code does not print 'inf'.

Thus, code proceeds.

So, code doesn't detect the infinite case because only one of the terms in the cycle is allowed. So the code correctly counts the allowed terms until steps reach 100.

But in reality, the allowed terms are 5, 5, 5... (no, wait, no. The terms are 5, -5,5,-5,... So the allowed terms are 5 (step 0), step 2 (5 again), step 4 (5), etc. So for steps even number, current is 5 (allowed). Steps=0,2,4, etc. 

But code steps up to 100, which is even.

Thus, the code would process current=5 50 times (steps even: 0, 2,4,... 98) → 50 times. So count=50.

But in reality, there are infinitely many terms allowed. But in this case, no, because the allowed terms are 5, which is allowed, but the next term is -5 (not allowed), then 5 (allowed), and so on. So each allowed term is followed by a bad term, but the allowed terms are 5, which is not part of a cycle where both terms are allowed. 

So the correct count is infinite? Or finite?

No. The code's logic is correct. Because the terms alternate between 5 (allowed) and -5 (bad). So, each allowed term is followed by a bad term. But the allowed terms are 5, which is allowed. 

But in the code's infinite check, after processing current=5:

next_term=-5. 

next_term is in bad_set. So the code does not check for infinite conditions. 

Thus, the code proceeds to count each 5 term. 

But since the code loops 100 steps, and each time current is 5 every two steps, the count is 50. But in reality, there are infinitely many 5 terms, each appearing at even steps. But since the code is limited to 100 steps, it counts 50.

But this is incorrect, as the code should output 'inf' in this case. 

Wait, why? Because after each 5 term, the next term is -5 (bad), then next term is 5 again. 

But the code's infinite check is only triggered when the next term is allowed. 

In this case, next_term is -5 (bad). So the code does not check for infinite conditions. 

Thus, the code counts 50 terms. 

But the correct answer is infinite, because there are infinitely many 5 terms that are allowed. 

But why is that?

Because the progression is 5, -5,5,-5,5,... 

The code counts each 5 term. 

So, the code would count each 5 term, which occurs infinitely. So the correct answer is 'inf'. 

But according to the code, after 100 steps, it would exit and return 50. 

This indicates a flaw in the code. 

Ah, because the code is limited to 100 steps, but the actual number of allowed terms is infinite. 

So, the code's step limit is causing an incorrect result. 

Thus, the step limit approach is not correct. 

So, what's the issue here?

The problem is that the code's infinite check only checks the next_term for the infinite conditions. But in this case, the current term is allowed, but the next term is not. Then, the next next term is allowed. But the code's infinite check is only triggered when the next term is allowed. 

So, in this case, the code is missing an infinite loop scenario where the allowed terms appear every other step. 

But according to the code's infinite checks, this scenario is not covered. 

Thus, the code's infinite checks are not sufficient to detect this case. 

So, how can we detect such a scenario?

In this case, the progression terms are allowed every other step, but the code's infinite checks are only triggered when the next term is allowed. 

But in this case, the code's infinite check for q=-1 is not triggered because the next term is -current (5 * -1 = -5), which is in bad_set. So the code's check for q=-1 and next_term ==-current is:

if next_term is allowed (not in bad_set) and current is allowed. 

But in this case, next_term is in bad_set, so code doesn't check. 

Thus, the code proceeds to process each allowed term. 

But since there are infinitely many allowed terms, the code's step limit leads to an incorrect count. 

Thus, the code's step limit is a problem. 

So, the step limit approach is incorrect and must be removed. 

But how to handle such cases without a step limit?

In this example, the code would loop forever, counting each allowed term. 

But in reality, the allowed terms are infinitely many. 

But how can we detect this? 

The problem is that the code is in a loop where the allowed terms are generated periodically. 

So, in this case, the allowed terms are 5,5,5,... (every other step). 

But the code's infinite check for q=-1 is only triggered when both current and next_term are allowed. 

But in this case, only current is allowed; next_term is not. 

So, the code doesn't detect the infinite case. 

Thus, the code's current logic is insufficient to handle such cases. 

But according to the problem statement, such cases are finite or infinite?

In this example, the allowed terms are generated infinitely often. But each allowed term is 5, which is within l. So, Masha would write each 5 term. 

So, the correct answer is 'inf', but the code's logic would not detect it. 

But according to the problem statement, the count is the number of terms written, which is infinite. 

Thus, the code's logic is incorrect for this case. 

But how to handle such cases?

This requires detecting that the progression is generating allowed terms infinitely often. 

But how to detect this in code?

One approach is to track the terms and detect that a cycle of allowed terms is formed. 

But for a geometric progression with q=-1, the terms alternate between current and -current. 

But if current is allowed and next_term is not, then the code's current logic will process each allowed term and count it. But since the code's step limit is in place, it will not process all terms. 

Thus, the step limit approach is not correct.

So, to correctly handle all cases, the code must simulate all terms until the term's absolute value exceeds l. 

But without a step limit, the code could run into infinite loops when allowed terms are generated infinitely often. 

But according to the problem's constraints, such cases can only occur when the progression is allowed to generate terms infinitely. Which is covered by the earlier checks. 

But in the example I presented, the code's earlier checks are not triggered. 

Thus, the code's logic has a bug. 

So, what is the correct approach?

The correct approach is to realize that in a geometric progression with integer terms and q != 1, -1, or 0, the terms will eventually exceed l. 

Thus, the code can safely process terms until their absolute value exceeds l, and only the cases where q is 1, -1, or 0 can lead to infinite terms. 

But in the example where q is -1 and current term is allowed but next term is not, the code would process terms infinitely often. 

But according to the problem statement, the code must output the count of allowed terms. 

But how to handle this case?

In this case, the allowed terms are generated infinitely often. Thus, the correct answer is 'inf'. 

But according to the code's current logic, it would process terms in a loop and count each allowed term, leading to an infinite loop. 

Thus, the code's approach is incorrect. 

So, how to detect this scenario?

This is a case where the allowed terms are generated infinitely often, but the code's current infinite checks are not triggered. 

So, the code must check for this scenario. 

In this example, after processing current=5 (allowed), the next term is-5 (not allowed). Then, the next term is 5 (allowed). So, after two steps, the code returns to the same allowed term. 

Thus, this is a cycle of two steps, generating an allowed term every other step. 

So, the code must track seen terms and detect such cycles. 

But how?

The solution is to keep track of the current term and the next term. If the code encounters the same pair (current, next_term) again, it means that the progression is in a cycle. 

In this case, the pair (5, -5) would be followed by (-5,5), and then (5, -5) again. 

Thus, the code can track pairs of consecutive terms. If a pair repeats, the code is in a cycle. 

If during the cycle, the allowed terms are being generated infinitely, then the answer is 'inf'. 

But how to detect this.

The code can track the set of seen pairs. If a pair is seen again, then the code is in a cycle. 

But since the progression can generate terms up to 1e9, the number of pairs could be large. 

But for cases where the progression is generating allowed terms infinitely often, the code must detect a cycle where at least one allowed term is generated in each cycle. 

So, the code can track the pairs of current and next_term. If a pair repeats, then it's a cycle. 

If the cycle includes at least one allowed term, then the count is infinite. 

But how to implement this.

But this approach could be memory-intensive for large cycles, but for cases where the progression can generate terms infinitely, the code must detect it. 

Thus, the code can:

- Keep track of seen pairs of (current, next_term).

- For each iteration, compute the pair (current, next_term).

- If the pair is already in seen, then a cycle is detected.

- Check if there are any allowed terms in the cycle.

- If yes, output 'inf'.

- Else, break and output the count.

Thus, the code can handle such cases.

But how to implement this efficiently.

So, the code can proceed as follows:

Initialize a set to track seen pairs.

current = b1

if abs(current) > l:

    print(0)

    exit()

count =0

seen = set()

while True:

    if abs(current) > l:

        break

    # Check if current is allowed.

    allowed = current not in bad_set

    if allowed:

        count +=1

    # Compute next_term.

    next_term = current * q

    # Check for infinite conditions.

    if abs(next_term) <= l and next_term not in bad_set:

        if q == 1:

            print("inf")

            exit()

        elif q == -1 and next_term == -current:

            if current not in bad_set:

                print("inf")

                exit()

        elif next_term == 0:

            print("inf")

            exit()

    # Check for cycles.

    pair = (current, next_term)

    if pair in seen:

        # Cycle detected.

        # Check if there's any allowed term in the cycle.

        # If during the cycle, there's at least one allowed term, output 'inf'.

        # Otherwise, break.

        # To check, we need to see if in the current cycle, any term is allowed.

        # But how?

        # Alternatively, if count has increased since the last time this pair was seen, then there's an allowed term in the cycle.

        # So, if count has increased, output 'inf'.

        # But this may not be reliable.

        # Another approach: if during this iteration, the current term is allowed, then output 'inf'.

        # Because the cycle will repeat, and the allowed term will be processed again.

        if allowed:

            print("inf")

            exit()

        else:

            # Check if any term in the cycle is allowed.

            # But how?

            # We can simulate a few steps and check.

            # For example, simulate a few iterations and see if any term is allowed.

            temp_current = current

            temp_next = next_term

            for _ in range(100):

                temp_current = temp_next

                temp_next = temp_current * q

                if abs(temp_current) > l:

                    break

                if temp_current not in bad_set:

                    print("inf")

                    exit()

            # After simulation, if no allowed terms, break.

            break

    else:

        seen.add(pair)

    current = next_term

print(count)

But this approach adds complexity. 

But in the example where q=-1, current=5, bad_set contains -5:

The code will process current=5 (allowed, count=1). next_term=-5. pair=(5,-5) is added to 'seen'.

current becomes -5. next_term=5. pair=(-5,5) is added to 'seen'.

current becomes 5. next_term=-5. pair=(5,-5) is already in 'seen'. So, cycle detected. 

Check if current is allowed (5 is allowed, so allowed is True). 

Thus, code prints 'inf' and exits. 

Which is correct.

Thus, this approach would handle the example correctly.

Thus, the code must track pairs of (current, next_term) to detect cycles. 

Thus, the code can be modified as follows:

current = b1

count = 0

bad_set = set(bad)

if abs(current) > l:

    print(0)

    exit()

seen_pairs = set()

while True:

    if abs(current) > l:

        break

    allowed = current not in bad_set

    if allowed:

        count +=1

    next_term = current * q

    # Check for infinite conditions.

    if abs(next_term) <= l and next_term not in bad_set:

        if q == 1:

            print("inf")

            exit()

        elif q == -1 and next_term == -current:

            if current not in bad_set:

                print("inf")

                exit()

        elif next_term == 0:

            print("inf")

            exit()

    pair = (current, next_term)

    if pair in seen_pairs:

        # Cycle detected.

        # Check if any term in the cycle is allowed.

        # Simulate the cycle and check if any allowed terms.

        temp_current = current

        temp_next = next_term

        has_allowed = False

        while True:

            temp_current = temp_next

            temp_next = temp_current * q

            if abs(temp_current) > l:

                break

            if temp_current not in bad_set:

                has_allowed = True

                break

            new_pair = (temp_current, temp_next)

            if new_pair == pair:

                # Full cycle completed.
                break
        if has_allowed:
            print("inf")
            exit()
        else:
            break
    else:
        seen_pairs.add(pair)

    current = next_term

print(count)

But this adds complexity and may not handle all cases. 

Alternatively, when a cycle is detected, the code can check if there's any allowed term in the current cycle. If yes, output 'inf'. Else, break.

But this requires simulating the cycle to check for allowed terms. 

But this could be time-consuming, but given that the code is limited to a few steps, it's manageable.

Thus, the code with pair tracking and cycle detection can handle the example.

But for the code to be efficient and handle all cases, this approach is needed.

Thus, the final code is as follows.
</think>

```python
b1, q, l, m = map(int, input().split())
bad = set(map(int, input().split()))
current = b1
count = 0
bad_set = bad

if abs(current) > l:
    print(0)
    exit()

seen_pairs = set()

while True:
    if abs(current) > l:
        break
    allowed = current not in bad_set
    if allowed:
        count += 1
    next_term = current * q

    # Check for infinite conditions
    if abs(next_term) <= l and next_term not in bad_set:
        if q == 1:
            print("inf")
            exit()
        elif q == -1 and next_term == -current:
            if current not in bad_set:
                print("inf")
                exit()
        elif next_term == 0:
            print("inf")
            exit()

    pair = (current, next_term)
    if pair in seen_pairs:
        # Check if any term in the cycle is allowed
        temp_current = current
        temp_next = next_term
        has_allowed = False
        while True:
            temp_current = temp_next
            temp_next = temp_current * q
            if abs(temp_current) > l:
                break
            if temp_current not in bad_set:
                has_allowed = True
                break
            if (temp_current, temp_next) == pair:
                break
        if has_allowed:
            print("inf")
            exit()
        else:
            break
    seen_pairs.add(pair)

    current = next_term

print(count)
```