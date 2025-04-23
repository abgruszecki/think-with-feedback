<think>
Okay, let's tackle this problem. So, the task is to determine the exact floor of flat n based on some remembered data, and if there's ambiguity, return -1. Hmm.

First, I need to understand the problem. The building has floors, each with the same number of flats. The flats are numbered sequentially starting from 1. For example, if each floor has 3 flats, then floors are 1-3, 4-6, etc. So the first floor is flats 1 to k, the second k+1 to 2k, etc. The key is to find possible values of k (flats per floor) that are consistent with the remembered data. Then, for each valid k, compute the floor of the nth flat and check if all possible k's give the same floor. If not, return -1.

So the steps are:

1. Find all possible values of k (flats per floor) that satisfy all the remembered flats (ki, fi). For each (ki, fi), k must satisfy that ki is in the fi-th floor. Which means (fi-1)*k < ki <= fi*k. So for each ki, fi, the possible k must be in the range ceil(ki / fi) <= k < ceil(ki/(fi-1)), but wait, how?

Wait, for a given ki and fi, the floor fi has k flats. So the fi-th floor contains the flats from (fi-1)*k +1 to fi*k. So ki must be in this range. So (fi-1)*k +1 <= ki <= fi*k. For example, if fi is 2 and ki is 6, then  k >= (ki-1)/ (fi-1) +1? Wait, let's re-express the inequalities.

For each (ki, fi), we have:

(fi-1)*k +1 <= ki <= fi*k

So solving for k:

k >= (ki -1)/fi  (since (fi-1)*k +1 <= ki → k <= (ki-1)/(fi-1) ? Wait, let's re-arrange.

Wait, the left inequality: (fi-1)*k +1 <= ki → (fi-1)*k <= ki-1 → k <= (ki-1)/(fi-1) if fi-1 is positive. But fi can be 1. Oh right. Wait, when fi is 1, the first floor has flats 1 to k. So ki must be <= k. So for fi=1, the constraint is k >= ki (since ki must be <= fi*k = 1*k → ki ≤ k → k ≥ ki).

Wait, let's split into cases where fi=1 and fi>1.

For a given (ki, fi):

If fi == 1: then ki must be ≤ k. So k >= ki.

If fi >1: then (fi-1)*k +1 <= ki <= fi*k → (ki-1)/(fi) < k <= (ki)/(fi-1)

Wait, let's see:

We have (fi-1)*k +1 <= ki → (fi-1)*k <= ki-1 → k <= (ki-1)/(fi-1)

But wait, that's only the left part. The right part is ki <= fi*k → k >= ki/fi.

But since k must be an integer (since it's the number of flats per floor), we can express this as k >= ceil(ki/(fi)) when fi>1. Wait, no. Let's see.

Wait, for fi>1:

The two inequalities are:

k >= (ki-1 +1 - (fi-1)*k) ?

Wait, perhaps it's better to rephrase the inequalities.

For fi>1, the constraints are:

k must be such that (fi-1)*k < ki ≤ fi*k → because (fi-1)*k is the last flat of the previous floor. So the first flat of fi-th floor is (fi-1)*k +1, and the last is fi*k.

Wait, no. Wait, the fi-th floor has k flats. The first floor is 1..k, second (k+1)..2k, etc. So for the fi-th floor, the first flat is (fi-1)*k +1 and the last is fi*k. So ki must be in [(fi-1)*k +1, fi*k].

So for each (ki, fi), we have:

(fi-1)*k +1 <= ki <= fi *k.

So for each (ki, fi), we can find the possible k's.

So for each (ki, fi), possible k must be >= ceil( (ki) / fi ), since fi*k >= ki → k >= ki / fi. But since k is integer, ceil(ki/(fi)) ?

Wait, no. Let's take an example. Suppose ki=6, fi=2. Then for k to satisfy (2-1)*k +1 <=6 <=2k → k+1 <=6 <=2k → k+1 <=6 → k <=5, and 6 <=2k →k >=3. So k is between 3 and 5 inclusive.

So for (ki=6, fi=2), possible k is 3,4,5.

Another example: ki=2, fi=1. Then, since fi=1, ki must be <=k. So k >=2.

So for each (ki, fi), we can compute the possible k ranges, and then the intersection of all these ranges (for all remembered data) is the set of possible k's that are valid. Then, for each of these k's, compute the floor of the nth flat, and see if all possible k's give the same floor. If yes, output that floor. Otherwise, output -1.

So the plan is:

1. Collect all possible k values that satisfy all the given (ki, fi) constraints.

2. For each possible k in this set, compute the floor of the nth flat. The floor is (n-1)//k +1.

Wait, yes. For example, n=6, k=3: (6-1)/3 +1 = 5/3=1 (integer division), +1 → 2. Which is correct.

So floor = ((n-1) //k) +1.

3. Collect all possible floor numbers for each valid k.

4. If all floor numbers are the same, output that. Otherwise, output -1.

Now, how do we compute the set of possible k's?

First, for each (ki, fi) in the input, compute the possible k's for that (ki, fi), then take the intersection across all (ki, fi) to get the valid k's.

So for each (ki, fi), we can compute the range of k that satisfies the constraints for that (ki, fi). Then, the valid k's are the intersection of all these ranges.

But how to represent these ranges efficiently?

Let's think about the possible k for each (ki, fi):

Case 1: fi =1.

Then, ki must be <=k. So k >= ki.

So the possible k's are [ki, infinity).

But since n can be up to 100, and ki up to 100, but in the problem, the building can be considered infinitely high, but for practical purposes, the possible k's can be up to n (since for n, the floor is (n-1)//k +1. So for k larger than n, the floor would be 1. But if the remembered data allows k to be larger than n, but the floor for n is 1, but other k's may also be possible. Wait, but the problem requires that the building must have a certain k, and the k must be compatible with all remembered data.

But when m=0 (no remembered data), then any k is possible. So for m=0, the answer is -1 unless all possible k's give the same floor for n. But when m=0, since k can be any positive integer (since all possible k's are allowed), then the floor of n is (n-1)//k +1. So for different k's, this value can vary.

For example, if n=8, when k=3, floor is (8-1)/3 +1 = 2+1=3. For k=4, floor is (7//4) +1=1+1=2. So if m=0, the answer is -1.

But back to the approach.

For each (ki, fi), the possible k's must be in certain ranges. For example, (ki, fi) = (6,2) gives k in [3,5]. (ki=2, fi=1) gives k >=2.

So for each (ki, fi), the allowed k's are the ones in their range. The overall allowed k's are the intersection of all these ranges.

Now, the problem is to compute this intersection.

But how do we compute the intersection when there are multiple ranges?

The approach is:

Initialize the possible k's as all possible integers >=1.

For each (ki, fi) in the memory, compute the allowed k's for that entry and intersect with the current possible k's.

After processing all entries, the possible k's are those that are allowed by all entries.

But how to compute this efficiently.

Let's think about each (ki, fi) generating a lower and upper bound for k.

For (ki, fi):

If fi ==1:

lower bound: k >= ki

upper bound: infinity.

Else:

lower bound: ceil( (ki) / (fi) )

upper bound: floor( (ki -1) / (fi-1) )

Wait, how?

Wait, for fi >1:

From (fi-1)*k +1 <= ki <= fi *k.

Rearranged:

k >= (ki)/fi (since fi*k >= ki → k >= ki / fi). But since k must be an integer, we take ceil(ki / fi).

Wait, no. Wait, let's see: fi*k >= ki → k >= ki / fi. Since k is integer, the minimum k is ceil(ki / fi). Wait, no. For example, ki=6, fi=2. ki/fi is 3. So k >=3. That's correct. For ki=7, fi=3: 7/3 is ~2.333, so ceil(7/3) is 3. So k >=3.

But the upper bound comes from (fi-1)*k +1 <=ki → (fi-1)*k <= ki-1 → k <= (ki-1)/(fi-1). So since k must be integer, the upper bound is floor( (ki-1)/(fi-1) ).

So for fi>1, k must be >= ceil(ki/fi) and <= floor( (ki-1)/(fi-1) )

But wait, let's check the example where ki=6, fi=2:

ceil(6/2) =3, floor( (6-1)/(2-1) )=5. So k is in 3..5, which matches.

Another example: ki=7, fi=3.

ceil(7/3) is 3, floor(6/2)=3. So k must be >=3 and <=3. So k=3.

So for (7,3), the allowed k is 3.

So for each (ki, fi) where fi>1, the allowed k's are in [ceil(ki/fi), floor( (ki-1)/(fi-1) ) ]

But what if the lower bound is greater than the upper bound? Then there's no possible k for this (ki, fi), which can't happen as the problem states that the input is not self-contradictory. So we can assume that for all (ki, fi) in input, there exists at least one k that satisfies all constraints.

So the steps for each (ki, fi):

If fi ==1: allowed k's are k >= ki.

Else: allowed k's are in [ceil(ki / fi), floor( (ki-1) / (fi-1) ) ]

So how do we compute the possible k's?

We can start with all possible k's (from 1 to some maximum possible value) and then for each (ki, fi), filter the k's according to their constraints.

But what's the maximum possible k we need to consider?

Well, for the problem's constraints, ki is up to 100, and m up to 100. But after processing all (ki, fi), the allowed k's can be up to the maximum possible from all constraints.

But in the case when fi=1, the allowed k can be up to any value. So for example, if one of the (ki, fi) pairs is (100, 1), then k can be 100, 101, etc. But for the nth flat (up to 100), when k is larger than n, the floor would be 1.

So if possible k's include values larger than n, then the floor for n would be 1. But if other possible k's (smaller than n) result in higher floors, then the answer is -1.

So for example, if the possible k's are 5 and 100. For n=10, with k=5: floor is (10-1)//5 +1 = 9//5=1 +1=2. For k=100: floor is 0 +1=1. So the floors are 2 and 1, so output is -1.

So to compute all possible k's, including those up to infinity, but that's impossible. How to handle this?

Hmm. But since n is up to 100, the maximum possible k that could affect the floor of n is n, because if k is larger than n, then (n-1)//k is 0, so floor is 1. But if k is <=n, then the floor can vary.

So for k's larger than n, the floor is 1. So if any k in the possible set is larger than n, then the floor for that k is 1. So if the possible k's include any value >n, then we have to check if all such k's (including those >n) give the same floor (1) as well as the possible k's <=n.

But how to model this?

The possible k's can be:

All k >= some value, and possibly up to some upper bound, or unbounded.

For example, if a constraint is k >=5, and other constraints have upper bounds, but if not, then k can be any number >=5.

In such a case, the possible k's are 5,6,7,... up to infinity.

But how can we handle this?

An alternative approach is:

For each (ki, fi) in the input, generate a lower and upper bound for k.

The overall possible k's are the intersection of all these ranges.

But when some ranges have upper bounds and others don't (like fi=1), then the upper bound is infinity.

But since in the problem, we need to compute the possible floor of n, and for k> n, the floor is 1.

So the possible k's can be divided into two parts:

1. k <=n: for these, compute floor as ((n-1)//k)+1.

2. k >n: for these, floor is 1.

So, the possible floor values are:

- All possible floors from k <=n (for each valid k in the possible k's and <=n) → F.

- Plus 1, if there exists a valid k >n.

If there exists a valid k >n, then floor 1 is possible.

So, to compute the set of possible floors:

- For the valid k's that are <=n, compute their floors.

- Check if any valid k >n exists. If yes, add 1 to the set of possible floors.

If all possible floors are the same, output that. Otherwise, output -1.

So how to compute the possible k's and see if any of them is >n?

But how to represent the possible k's when there's a lower bound and no upper bound?

For example, if the possible k's are all k >=5. Then, any k >=5 is valid, including those >n. So in this case, if n is 10, then for k=5,6,...,10, compute their floors, and check if there's a k>10 (which would contribute floor 1).

So the possible floors would be the floors from k=5 to 10, and floor 1 (since k can be 11, 12, etc.). So we need to collect all possible floors from all possible k's, including those beyond n.

But how?

This seems tricky. Because when the possible k's include all values >=x, where x could be less than or equal to n, then for k >=x and <=n, each of their floors is computed, and for k >n, the floor is 1.

So the set of possible floors includes:

- All floors for k in [x, n], where x is the lower bound.

- And floor 1 if x <=n (since k can be n+1, which is >=x (if x <=n+1)).

Wait, no. For example, if x is 5, and n is 10. Then possible k's are >=5. So k can be 5,6,...,10 (which are <=n) and 11,12,... (which are >n). So the floors would be:

For k in 5-10: floor is ((n-1)//k)+1.

For k>10: floor is 1.

So the possible floors are the union of these values and 1.

Thus, to compute the possible floors, we need to:

1. Find all possible k's that are allowed and <=n. For each of these, compute their floor.

2. Also, check if there are any allowed k's that are >n. If yes, add 1 to the possible floors.

So how do we check if there are any allowed k's >n?

We can model the possible k's as a range [k_min, k_max], where k_max can be infinity (represented as some large number, say, 1e18). Then, if k_max >=n+1, then there are allowed k's >n. But how?

Alternatively, during the processing of each (ki, fi), we can track the lower and upper bounds.

Let's think of the possible k's as being in the interval [current_low, current_high], where current_high could be infinity.

Initially, current_low is 1, current_high is infinity (but perhaps represented as a large number, like 1e18).

For each (ki, fi):

Compute the new_low and new_high for this (ki, fi).

If fi ==1:

new_low = max(current_low, ki)

new_high remains current_high (since there's no upper bound).

Else:

low = ceil(ki / fi)

high = floor( (ki-1) / (fi-1) )

new_low = max(current_low, low)

new_high = min(current_high, high)

If at any step, new_low > new_high, then it's impossible, but the problem says the input is not self-contradictory, so this won't happen.

So after processing all (ki, fi), the possible k's are in [current_low, current_high].

If current_high is infinity (like in the case where some (ki, fi) has fi=1 and no upper bound), then possible k's are >= current_low.

Else, possible k's are in [current_low, current_high].

So after processing all (ki, fi) pairs, we can represent the possible k's as:

if current_high is infinity (i.e., there's a fi=1 in the input and no upper bound), then possible k's are all k >= current_low.

Else, possible k's are between current_low and current_high, inclusive.

Now, given this, how to compute all possible floors for n.

Case 1: current_high is infinity.

In this case, possible k's are >= current_low.

We can split into two subcases:

a) current_low <=n:

Possible k's include those from current_low to n, and also k>n.

For the k>n, floor is 1.

For k in [current_low, n], compute their floors.

So the possible floors are the floors from k=current_low to k=n, plus 1 (since k>n is allowed).

Unless all k >= current_low and <=n have the same floor, and that floor is 1. Then, adding 1 doesn't change anything.

But if any of the k in [current_low, n] gives a floor different from 1, then adding 1 (from k>n) would mean two different floors.

So in this case, the possible floors are:

floors = { ((n-1)//k +1) for k in [current_low, n] } ∪ {1}

So if this set has size 1, then output that. Else, -1.

But calculating this for all possible k in [current_low, n] could be O(n), which for n=100 is manageable.

But wait, n is up to 100. So even if current_low is 1 and current_high is infinity, and n is 100, we need to check k from 1 to 100, and also consider if there are k>100 (which would contribute 1).

So for each possible k in [current_low, current_high_upper], where current_high_upper is min(current_high, n), and also check if any k>n is allowed.

Wait, but current_high could be infinity. So when current_high is infinity, then the possible k's are all >= current_low.

So in this scenario:

If current_high is infinity:

Then possible k's are all >= current_low.

So to compute possible floors:

- For k in [current_low, n], compute their floors.

- Also, if current_low <=n, then there are k's >n (since current_high is infinity), which contribute floor 1.

Thus, in this case:

if current_low <=n:

   possible_floors = { floor(k) for k in [current_low, n] } ∪ {1}

else:

   possible_floors = {1} (since all k's are >=current_low >n, so floor is 1)

So in this case, if current_low >n, all possible k's are larger than n → floor is 1. So output 1.

Case 2: current_high is finite.

In this case, possible k's are in [current_low, current_high].

So possible k's are from current_low to current_high, inclusive.

But current_high can be <=n or >n.

So:

If current_high <=n:

   then possible_floors = { ((n-1)//k +1) for k in [current_low, current_high] }

   and check if any k in that range >n → but current_high <=n implies all k's are <=n.

   So possible_floors are as above.

Else if current_high >n:

   possible_floors = { ((n-1)//k +1) for k in [current_low, n] } ∪ {1} (since k can be from n+1 to current_high → which contributes 1)

So in this scenario:

- For k in [current_low, n], compute floors.

- If current_high >n, then add 1.

But how to determine if current_high >n.

So overall steps:

1. Compute current_low and current_high after processing all (ki, fi).

   For current_high, during processing, if any (ki, fi) with fi=1 is encountered, then current_high remains infinity.

   Else, current_high is the minimum of the upper bounds from all (ki, fi).

2. Once current_low and current_high are determined:

   a) If current_high is not infinity:

      i) If current_high < current_low → no solution (but problem says input is not self-contradictory).

      ii) Else:

          - collect all k in [current_low, min(current_high, n)] → compute their floors.

          - if current_high >n → add 1 to possible_floors.

   b) If current_high is infinity:

      i) If current_low >n → possible_floors = {1}.

      ii) Else:

          - collect all k in [current_low, n] → compute their floors.

          - add 1 to possible_floors (since there are k's >n).

3. Once possible_floors is built, check if all elements are the same. If yes, output that. Else, output -1.

Now, the challenge is to implement this logic.

Let's think about how to handle current_high as infinity. Maybe represent it as a very large number, like 1e18.

But during processing, when a (ki, fi) with fi=1 is encountered, which has upper bound infinity (since k can be any >=ki), then the new_high would be current_high (which may have been infinity before).

So during processing each (ki, fi):

- Initialize current_low = 1, current_high = 1e18 (as a representation of infinity).

But wait, initially, possible k's are all possible. Wait, no. Wait, initially, the possible k's are all k >=1. Because the problem says that the building can have any number of flats per floor. So the initial current_low is 1, current_high is infinity (1e18 in code).

But the first (ki, fi) in the input will constrain the possible k's.

So during processing each (ki, fi):

For example, first (ki=6, fi=2):

fi>1, so:

low = ceil(6/2) =3.

high = floor( (6-1)/(2-1) )=5.

So new_low = max(1,3) =3.

new_high = min(1e18,5) =5.

current_low and current_high are updated to 3 and 5.

Then, next (ki=2, fi=1):

fi=1, so:

low = max(3, 2) →3.

high remains 5 (since fi=1's upper bound is infinity, but current_high is 5, so new_high is min(5, infinity) →5).

Wait, no. For (ki=2, fi=1):

The allowed k's are k >=2.

But the current_high is 5 from previous steps.

So after processing this (ki=2, fi=1), the new_low is max(3,2) →3.

new_high is min(5, infinity) →5.

So current_high remains 5.

Wait, that's not correct. Because (ki=2, fi=1) allows k >=2, but the previous current_high was 5. So the new constraints are k >=3 (since the new_low is 3) and <=5. But the (ki=2, fi=1) allows k >=2. So the intersection would be k >=3 and <=5. So the new_low is 3, new_high is 5.

So the code's logic would correctly compute this.

So in code, for each (ki, fi):

if fi ==1:

   low = ki

   high = 1e18  # representing infinity

else:

   low = ceil(ki / fi)

   high = (ki-1) // (fi-1)

   if (ki-1) < (fi-1):

       high = 0 → which would make low > high, but input is non-contradictory, so this won't happen.

Then, current_low is updated to max(current_low, low).

current_high is updated to min(current_high, high).

But when fi=1, high is 1e18 (infinity), so min(current_high, 1e18) would be current_high.

So in code:

We can represent current_high as a variable that is either a finite number or infinity (represented as 1e18). Then, when fi=1, the new_high is 1e18.

So processing each (ki, fi):

compute low and high.

current_low = max(current_low, low)

current_high = min(current_high, high)

After processing all (ki, fi), we have current_low and current_high.

Now, after processing all entries, we need to compute the possible_floors.

So let's proceed.

First, check if current_high is 1e18 (infinity) or not.

In code, we can represent infinity as a large value, say 1e18.

So, possible_floors is a set.

Case 1: current_high == 1e18 (so there are no upper bounds except possibly from other constraints).

Wait, no. current_high is min of all high from each (ki, fi). If any (ki, fi) has fi=1, then high is 1e18, so current_high can be 1e18 (if at least one (ki, fi) has fi=1 and other high are >=1e18) ?

Wait, during processing, when any (ki, fi) with fi=1 is encountered, the high becomes 1e18. So, the current_high is the minimum of all previous high and the new high. If the new high is 1e18, then the current_high remains whatever it was before (since min(prev_high, 1e18) is prev_high). Unless the previous current_high was also 1e18.

Wait, perhaps it's better to track whether current_high is infinity. For example, use a boolean variable is_infinite to indicate if current_high is infinity.

Alternatively, represent current_high as a variable, and when processing (ki, fi) with fi=1, the high is set to a very large number (1e18), and then current_high is min(current_high, high). So if current_high was already 1e18, it remains so.

But perhaps in code, this can be handled with the following approach:

Set current_low = 1, current_high = 1e18.

For each (ki, fi):

   if fi ==1:

      new_low = ki

      new_high = 1e18

   else:

      low = ceil(ki / fi)

      high = (ki-1) // (fi-1)

      new_low = low

      new_high = high

   current_low = max(current_low, new_low)

   current_high = min(current_high, new_high)

So after processing all (ki, fi), current_low and current_high are the lower and upper bounds.

But if any (ki, fi) had fi=1, then the new_high could be 1e18. So current_high could be 1e18 (if any (ki, fi) with fi=1 and the other constraints allowed higher k's).

But for example, if there are multiple (ki, fi) with fi=1 and other constraints, then current_high may be finite.

Wait, for example:

Suppose we have two (ki, fi) entries:

(ki=2, fi=1) → new_low=2, new_high=1e18.

(ki=5, fi=2) → compute new_low = ceil(5/2) =3, new_high= (5-1)/(2-1) =4.

So after first (2,1), current_low=2, current_high=1e18.

After processing (5,2), current_low = max(2,3)=3, current_high= min(1e18,4) =4.

So after this, current_high is 4, even though one of the (ki, fi) entries had fi=1.

So the code correctly handles the cases.

Now, after processing all entries, current_low and current_high are set.

Now, possible_floors is computed as follows:

If current_high is 1e18:

   So possible k's are >= current_low and <= 1e18 (i.e., any k >= current_low).

   So in this case:

   - For k >= current_low, if any k <=n exists (current_low <=n), then possible_floors includes floors from current_low to min(n, 1e18) → which is current_low to n.

   - Also, possible_floors includes 1 if current_low <=n+1 (because k can be >= current_low and some k >n).

   But wait, if current_low <=n, then there are k's in [current_low, n], and also k's >n. So possible_floors includes 1.

   So in code:

   if current_low >n:

       possible_floors = {1}

   else:

       possible_floors = { ((n-1)//k +1) for k in range(current_low, n+1) }

       possible_floors.add(1)

Else:

   possible k's are in [current_low, current_high]

   So:

   min_k = current_low

   max_k = current_high

   if max_k >n:

       possible_floors includes floors from k= min_k to n, plus 1 (because k can be from n+1 to max_k, which contribute 1).

       So possible_floors = { ((n-1)//k +1) for k in range(min_k, min(max_k, n)+1) }

       possible_floors.add(1)

   else:

       possible_floors = { ((n-1)//k +1) for k in range(min_k, max_k+1) }

So in code:

possible_floors = set()

if current_high == 1e18:  # infinite case

    if current_low > n:

        # all possible k are >n → floor is 1.

        possible_floors.add(1)

    else:

        # add all k from current_low to n, then add 1.

        for k in range(current_low, n+1):

            possible_floors.add( (n-1) // k + 1 )

        possible_floors.add(1)

else:

    # finite case

    if current_low > current_high:

        # impossible, but problem says input is non-contradictory.

        pass

    min_k = current_low

    max_k = current_high

    # collect k from min_k to min(max_k, n)

    upper = min(max_k, n)

    for k in range(min_k, upper +1):

        possible_floors.add( (n-1) //k +1 )

    # check if max_k >n → add 1.

    if max_k >n:

        possible_floors.add(1)

So after building possible_floors, if the size is 1, output the element. Else, output -1.

Now, code this.

Let's test with the first example:

Input:

10 3

6 2

2 1

7 3

Processing the first entry (6,2):

fi>1.

low = ceil(6/2) =3.

high = (6-1)/(2-1) =5.

current_low=3, current_high=5.

Second entry (2,1):

fi=1 → new_low=2, new_high=1e18.

current_low is max(3,2) →3.

current_high is min(5, 1e18) →5.

Third entry (7,3):

fi>1.

low = ceil(7/3) =3.

high = (7-1)/(3-1) =6/2=3.

current_low = max(3,3) →3.

current_high = min(5,3) →3.

So after all three entries, current_low=3, current_high=3.

current_high is not 1e18.

max_k is 3.

n is 10.

max_k is 3, which is <=10.

So collect k from 3 to 3.

For k=3: (10-1)//3 +1 →9//3=3 +1=4.

possible_floors = {4}

since max_k is 3 <=10 → no need to add 1.

so possible_floors has size 1 → output 4.

Which matches the example.

Second example:

Input:

8 4

3 1

6 2

5 2

2 1

Processing:

current_low starts at 1, current_high 1e18.

First (3,1):

fi=1 → new_low=3, new_high=1e18.

current_low=3, current_high=1e18.

Second (6,2):

low = 6/2=3 →ceil is 3.

high = (6-1)/(2-1)=5.

current_low = max(3,3) =3.

current_high = min(1e18,5) →5.

Third (5,2):

low =5/2=2.5 →ceil(5/2) =3.

high = (5-1)/(2-1) =4.

current_low = max(3,3)=3.

current_high = min(5,4) →4.

Fourth (2,1):

fi=1 → new_low=2, new_high=1e18.

current_low = max(3,2) →3.

current_high = min(4, 1e18) →4.

So after processing all, current_low=3, current_high=4.

current_high is finite (4).

n is 8.

max_k=4, which is <=8.

So collect k from 3 to4.

For k=3:

(8-1)/3 +1 →7//3=2 +1=3.

k=4:

7//4=1 +1=2.

possible_floors = {3,2}

Also, since max_k=4 <=8 → no need to add 1.

so possible_floors has {2,3} → output -1.

Which matches the example.

Another example: when m=0.

n=5, m=0.

current_low=1, current_high=1e18.

possible_floors:

since current_high is 1e18 and current_low=1 <=5.

So possible_floors is:

for k=1-5:

floor for k=1 → (5-1)//1 +1=4+1=5.

k=2 →4//2=2+1=3.

k=3 →4//3=1+1=2.

k=4 →4//4=1+1=2.

k=5 →4//5=0+1=1.

possible_floors includes all these (5,3,2,2,1) plus 1 (from k>5).

So possible_floors = {5,3,2,1, ...} → output -1.

So the code would correctly return -1.

Another example where current_low is 5, current_high is 1e18, and n=4.

current_low=5>4 → possible_floors is {1}.

So output 1.

So the code seems to handle all cases.

Now, let's code this.

The code steps:

Read n and m.

current_low = 1

current_high = 1e18

Then for each of the m lines:

read ki, fi.

if fi ==1:

   new_low = ki

   new_high = 1e18

else:

   new_low = (ki + fi -1) // fi  # ceil(ki/fi)

   new_high = (ki-1) // (fi-1)

current_low = max(current_low, new_low)

current_high = min(current_high, new_high)

Once all are processed:

possible_floors is built.

Now, code the possible_floors as discussed.

But how to handle the 1e18 in code.

In code, we can represent current_high as a very large number, say 1e18.

So:

possible_floors = set()

if current_high == 1e18:

   # handle infinite case

   if current_low >n:

       possible_floors.add(1)

   else:

       for k in range(current_low, n+1):

           possible_floors.add( (n-1) //k +1 )

       possible_floors.add(1)

else:

   # finite case

   if current_low > current_high:

       # impossible, but problem says input is valid.

       pass

   else:

       upper = min(current_high, n)

       for k in range(current_low, upper +1):

           possible_floors.add( (n-1) //k +1 )

       if current_high >n:

           possible_floors.add(1)

Then, if len(possible_floors) ==1:

   print(possible_floors.pop())

else:

   print(-1)

But wait, what if there are no entries (m=0)?

Then current_low is 1, current_high is 1e18.

possible_floors is built for k from 1 to n, and add 1.

So for m=0, possible_floors will have all possible floors from k=1 to n, plus 1. Unless n=1.

For example, n=1:

possible_floors for m=0.

current_low=1, current_high=1e18.

current_low <=1.

So for k in 1 to 1:

floor is (0)//1 +1=1.

Add 1 (from k>1). So possible_floors is {1}. Output 1.

But in the problem statement, when m=0, it's allowed and the code should handle.

Now, code.

But code needs to read m=0 case, where no ki,fi are given.

Now, code:

Read n and m.

current_low =1

current_high = 1e18

for _ in range(m):

    ki, fi = map(int, input().split())

    if fi ==1:

        new_low = ki

        new_high = 1e18

    else:

        new_low = (ki + fi -1) // fi  # ceil(ki/fi)

        new_high = (ki-1) // (fi-1)

    current_low = max(current_low, new_low)

    current_high = min(current_high, new_high)

Then build possible_floors.

Now, code.

Test case 1:

n=10, m=3.

After processing:

current_low=3, current_high=3.

possible_floors:

finite case.

current_high=3, n=10.

upper =3.

loop k=3:

floor is 9//3 +1=3+1=4.

current_high=3 <=10 → no add 1.

possible_floors={4}.

So output 4.

Test case 2:

n=8, m=4.

current_low=3, current_high=4.

finite case.

upper =4.

k=3: (7//3)=2 +1=3.

k=4:7//4=1+1=2.

possible_floors={3,2}.

current_high=4 <=8 → no add 1.

output is -1.

Another test case where current_high is 1e18 and current_low <=n.

For example, n=5, current_low=3, current_high=1e18.

possible_floors:

k ranges from 3 to5:

k=3:4//3=1 +1=2.

k=4:4//4=1 +1=2.

k=5:4//5=0 +1=1.

plus add 1 (from k>5).

so possible_floors is {2,1} → output -1.

Another case where current_low=6 and current_high=1e18, n=5.

current_low=6>5 → possible_floors={1} → output 1.

So code works.

Now, code:

Now, in Python.

But wait, in Python, when current_high is 1e18, but when m=0, current_low is 1.

So code:

n, m = map(int, input().split())

current_low = 1

current_high = 10**18

for _ in range(m):

    ki, fi = map(int, input().split())

    if fi ==1:

        new_low = ki

        new_high = 10**18

    else:

        new_low = (ki + fi -1) // fi  # ceil(ki/fi)

        new_high = (ki -1) // (fi-1)

    current_low = max(current_low, new_low)

    current_high = min(current_high, new_high)

possible_floors = set()

if current_high == 10**18:

    # handle infinite case

    if current_low > n:

        possible_floors.add(1)

    else:

        # add all k from current_low to n, and add 1.

        for k in range(current_low, n+1):

            floor = (n-1) //k +1

            possible_floors.add(floor)

        possible_floors.add(1)

else:

    # finite case

    if current_low <= current_high:

        # collect k from current_low to min(current_high, n)

        upper = min(current_high, n)

        for k in range(current_low, upper +1):

            floor = (n-1) //k +1

            possible_floors.add(floor)

        # check if current_high >n

        if current_high >n:

            possible_floors.add(1)

if len(possible_floors) ==1:

    print(possible_floors.pop())

else:

    print(-1)

This should handle all cases.

Testing the code with the examples.

First example:

Input:

10 3

6 2

2 1

7 3

current_low=3, current_high=3.

possible_floors is finite.

current_high=3 <=10.

k ranges 3-3.

floor for k=3: (10-1)//3 +1= 3 +1=4.

possible_floors={4}.

output 4.

Second example:

Input:

8 4

3 1

6 2

5 2

2 1

current_low=3, current_high=4.

possible_floors is finite.

upper=4 (min(4,8)).

k ranges 3-4.

k=3: (8-1)//3 +1=2+1=3.

k=4:7//4+1=1+1=2.

possible_floors={3,2}.

current_high=4 <=8 → no add 1.

so output -1.

Another test case where m=0:

n=1, m=0.

current_low=1, current_high=1e18.

possible_floors is:

current_low<=1 → add k=1.

floor is (0//1)+1=1.

add 1.

possible_floors={1}.

output 1.

Another test case where m=0, n=2.

possible_floors for k=1,2, and 1 (from k>2).

floor for k=1: (2-1)//1 +1=1+1=2.

k=2:1//2=0+1=1.

possible_floors={2,1, 1} → {1,2}.

output -1.

So code works.
</think>

```python
n, m = map(int, input().split())
current_low = 1
current_high = 10**18

for _ in range(m):
    ki, fi = map(int, input().split())
    if fi == 1:
        new_low = ki
        new_high = 10**18
    else:
        new_low = (ki + fi - 1) // fi
        new_high = (ki - 1) // (fi - 1)
    current_low = max(current_low, new_low)
    current_high = min(current_high, new_high)

possible_floors = set()

if current_high == 10**18:
    if current_low > n:
        possible_floors.add(1)
    else:
        for k in range(current_low, n + 1):
            possible_floors.add((n - 1) // k + 1)
        possible_floors.add(1)
else:
    if current_low <= current_high:
        upper = min(current_high, n)
        for k in range(current_low, upper + 1):
            possible_floors.add((n - 1) // k + 1)
        if current_high > n:
            possible_floors.add(1)

print(possible_floors.pop() if len(possible_floors) == 1 else -1)
```