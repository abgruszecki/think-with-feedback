<think>
Okay, let's try to understand this problem. So, Arkady is making marks each day based on the water level. Each day, if the water level is the same as any previous mark, no new mark is made. Otherwise, a new mark is added. The m_i values represent the number of marks strictly above the water level on day i. We need to find the minimum possible sum of d_i, which is the number of marks strictly below the water level each day. The goal is to minimize the total sum of all d_i.

Hmm. Let's break this down. For each day i, the number of marks above is m_i. The total number of marks after day i is equal to the number of unique water levels up to and including day i. Because each day, if the current water level is new, a mark is added. So the count of marks after day i is equal to the number of unique levels up to that day.

Wait, but the initial marks start empty. So on day 1, there's no existing mark, so if the level is new (which it must be, since there are no marks before), a mark is added. So after day 1, there's 1 mark.

But the problem says that on day i, m_i is the number of marks strictly above the water. So for day i, let's think: the number of marks above is m_i. The number of marks below is d_i. The total number of marks existing before this day is equal to (m_i + d_i + 1) if the current day's level is new. Wait, no. Wait, the total number of existing marks after day i depends on whether today's level is new or not.

Wait, let's think for day i. Before the day starts, there are some existing marks. Then, the current day's water level is such that if it's already present, no new mark is added. Otherwise, a new mark is added.

So, on day i, the marks are the ones from previous days plus possibly today's. So the total marks after day i is previous_marks + (if current level is new then 1 else 0). But the m_i is the number of marks strictly above on day i. So on day i, after adding the mark (if needed), the marks are split into three parts: those above (m_i), those below (d_i), and the current level's mark. Wait, but the current level's mark is exactly the one that is at the same height as the water. So the current mark is not above or below.

So, the total number of marks after day i is m_i (above) + d_i (below) + 1 (current level's mark). But this must equal the number of unique levels up to day i. Wait, because each level added is a new mark. So for example, after day i, the total marks is the number of unique levels up to day i.

But how does that relate to m_i and d_i for day i? Because for the current day's level, the marks are split into above (m_i) and below (d_i), plus the current level's mark. So m_i + d_i + 1 equals the total number of marks after day i. But the total marks after day i is the number of unique levels up to day i, because each day adds a mark if it's a new level.

Wait, maybe not. For example, on day i, the water level is same as a previous day. Then, no new mark is added. So the total marks after day i is same as the total after day i-1. But in this case, m_i + d_i + 1 would equal the total after day i. So that could be equal to the total from day i-1 if the level wasn't new. Hmm, this seems conflicting.

Alternatively, let's think for each day i:

Let s_i be the set of all marks present after day i. Then, |s_i| is the number of unique levels up to day i. Now, on day i, the current water level is l_i. The marks above are those in s_i that are > l_i, which is m_i. The marks below are those in s_i that are < l_i, which is d_i. The current mark l_i is part of s_i (if it was added on or before day i). So the total |s_i| = m_i + d_i + 1 (if l_i is in s_i). But since s_i includes all marks up to day i, l_i is definitely in s_i if it was added on any day up to i. Wait, no. Because if on day i, the current level l_i is not present in the existing marks (s_{i-1}), then we add it, making s_i = s_{i-1} ∪ {l_i}. So |s_i| = |s_{i-1}| + 1. Otherwise, if l_i is already in s_{i-1}, then s_i = s_{i-1}, so |s_i| = |s_{i-1}|.

But in any case, on day i, the marks present are s_i. So for that day, the split is m_i (above), d_i (below), and 1 (current). So:

m_i + d_i + 1 = |s_i| ?

Wait, that can't be right. Because |s_i| could be the same as |s_{i-1}| if l_i is already present. So for example, if on day 1, l_1 is new, then |s_1| =1. On day 2, if l_2 is same as l_1, then |s_2|=1. But according to the formula m_2 + d_2 +1 = |s_2|. So m_2 is the number of marks above l_2 (which is 0, since there's only one mark at l_2). d_2 is the number below (0 as well). So 0+0+1=1 which equals |s_2|. That works. Another example: on day 3, if l_3 is a new level higher than previous ones. Then |s_3|=2. m_3 is 0 (no marks above), d_3 is 1 (the previous mark is below). So 0+1+1=2, which matches. So the formula holds.

So for each day i, m_i + d_i +1 = |s_i|.

But |s_i| is the number of unique levels up to day i. So for the sum of d_i, we can express each d_i as |s_i| - m_i -1. So the sum of d_i over all i is sum(|s_i| - m_i -1) for each i. So the sum is sum(|s_i|) - sum(m_i) -n. Because each term subtracts 1, and there are n terms.

So the problem reduces to minimizing sum(|s_i|) - sum(m_i) -n. Since sum(m_i) is given as input, and n is known, the problem is equivalent to minimizing sum(|s_i|) over all possible valid sequences of levels l_1, l_2, ..., l_n that satisfy the constraints given by m_i.

Therefore, the key is to find the minimal possible sum of |s_i| for all i, given the m_i constraints. Then subtract sum(m_i) and n to get the answer.

So the problem now is to model how |s_i| can be determined based on the m_i. Because for each day i, m_i is given, and |s_i| is the number of marks after day i, which can be either equal to |s_{i-1}| (if the current level is a duplicate) or |s_{i-1}| +1 (if it's a new level).

But how do the m_i constraints affect this? For each day i, the m_i must equal the number of marks above the current level l_i in s_i.

Wait, but s_i is the set after day i. So the marks above l_i in s_i are exactly the number of levels in s_i that are higher than l_i. So for each day i, after choosing l_i (which can be new or existing), m_i must equal the count of elements in s_i that are > l_i.

So how can we model the minimal sum of |s_i|, given that for each i, m_i is the number of elements in s_i greater than l_i, and l_i can be either a new element or an existing one from s_{i-1}?

Hmm. Let's model this step by step. Let's track the possible |s_i| values and how they can be chosen.

For each day i, the possible cases are:

1. The current level l_i is a new level not present in s_{i-1}. Then |s_i| = |s_{i-1}| +1. Also, the number of elements in s_i greater than l_i is m_i. But since s_i = s_{i-1} ∪ {l_i}, the count of elements > l_i in s_i is the same as the count in s_{i-1} plus whether l_i is inserted in such a way that some elements are above it. Wait, no. Because when we add a new level l_i, the count of elements above is exactly m_i. So when we add a new level, the m_i must equal the number of elements in s_{i} that are > l_i. But s_i is s_{i-1} plus l_i. So the number of elements in s_i greater than l_i is the number of elements in s_{i-1} greater than l_i. Because the new element is l_i itself. So for this to be possible, there must be exactly m_i elements in s_{i-1} that are greater than l_i. But since l_i is a new element, the count of elements greater than l_i in s_i is the same as in s_{i-1} (since s_i includes s_{i-1} and l_i is added, but l_i is not part of s_{i-1}).

Wait, I'm getting confused. Let me think again. Let's say we have s_{i-1} as the set of existing marks. Then, when adding l_i (which is new), s_i is s_{i-1} ∪ {l_i}. The number of elements in s_i greater than l_i is the same as the number of elements in s_{i-1} greater than l_i. Because the new element l_i is not part of s_{i-1} and is equal to itself. So for m_i to be the count of elements in s_i greater than l_i, m_i must be equal to the count of elements in s_{i-1} that are greater than l_i. But when adding l_i, we can choose any value (as long as the count in s_{i-1} of elements > l_i equals m_i). Because l_i is a new value, we can arrange its position to satisfy this.

Alternatively, perhaps the problem can be modeled using a multiset or a sorted list. Let's think of the set of marks as being kept in a sorted order. Each time a new level is added, we insert it into the sorted list. The position where it's inserted determines the number of elements above it. For example, inserting a new element at a position where there are exactly m_i elements above would satisfy the condition. But how do we model this for the minimal sum of |s_i|?

Wait, but the sum of |s_i| is the sum of the sizes of s_i for each day. So adding a new element increases the size by 1, which contributes 1 to the sum for each subsequent day. So to minimize the sum, we want to minimize the number of new elements added as early as possible. Because each new element adds 1 to the size for all days after that. So adding a new element early on would increase the sum more than adding it later. Therefore, to minimize the total sum, we should add as few new elements as possible. Wait, but the constraints of m_i might force us to add new elements.

But this is conflicting. Because for each day i, when m_i is given, we might have to add a new element to satisfy the m_i condition.

So the problem is to find a way to arrange the elements (adding new ones when necessary) such that for each i, the number of elements in s_i greater than l_i is m_i, and the sum of |s_i| over all days is minimized.

But how can we model this? Let's think for each day i:

Case 1: We do not add a new element (i.e., l_i is an existing element from s_{i-1}).

In this case, |s_i| = |s_{i-1}|. Also, the number of elements in s_i greater than l_i is m_i. But since s_i is s_{i-1}, the count of elements > l_i in s_i is the same as in s_{i-1} for that element. So if l_i is an existing element, then m_i must be equal to the count of elements in s_{i-1} greater than l_i.

Case 2: We add a new element. Then |s_i| = |s_{i-1}| + 1. The count of elements greater than l_i in s_i is m_i. Since l_i is new, this count is equal to the number of elements in s_{i-1} that are greater than l_i. So m_i must be equal to that count.

So for each day, we can choose to either add a new element (case 2) or reuse an existing element (case 1), subject to the constraints that in case 1, the existing element must have exactly m_i elements greater than it in s_{i-1}.

Our goal is to choose for each day whether to add a new element or not, such that the sum of |s_i| is minimized. Since |s_i| is the size of the set after day i, and each addition increases the size by 1, the sum over all days is the sum of 1 for each day up to the first occurrence of each new element. Wait, no. The sum of |s_i| for each day is the sum of the sizes after each day. For example, if on day 3 we add a new element, then |s_3| = |s_2| +1. So the sum increases by |s_3| compared to previous days. So each new element added on day i contributes (n - i + 1) to the total sum, because it increases the size by 1 for each subsequent day (including day i). For example, adding a new element on day i increases |s_i| by 1, and all |s_j| for j >= i by 1. So the total added to the sum is (n - i + 1) * 1. Therefore, to minimize the sum, we should add as few new elements as possible, and add them as late as possible.

Ah! So the optimal strategy is to add new elements only when necessary, and when possible, add them as late as possible. Because adding a new element earlier contributes more to the sum. So we need to find the minimal number of new elements added, and add them in the latest possible days where they are required.

But how do we determine when we must add a new element? For each day i, m_i must be <= |s_{i-1}|, because in case 1, m_i is the number of elements greater than an existing element in s_{i-1}, which can't be larger than |s_{i-1}|-1 (since the existing element itself is part of the set). Wait, no. For case 1, if we reuse an existing element, the number of elements in s_{i-1} greater than that element must be exactly m_i. But s_{i-1} has |s_{i-1}| elements. So for some x in s_{i-1}, the count of elements >x in s_{i-1} is m_i. So m_i can be up to |s_{i-1}|-1 (if x is the smallest element). So if we can find such an x in s_{i-1}, then we can choose to reuse it. Otherwise, we have to add a new element.

So for day i, when processing the m_i:

If there exists a value in s_{i-1} such that the number of elements greater than it is m_i, then we can reuse that value (case 1), and |s_i| remains the same as |s_{i-1}|. Otherwise, we have to add a new element (case 2), which increases |s_i| by 1, and the new element's m_i must be equal to the number of elements in s_{i-1} greater than it (which is m_i).

So the problem reduces to tracking the possible m_i values and determining when a new element must be added.

But how can we model this efficiently? Let's think about the possible m_i constraints.

At any step i, the set s_{i-1} is a set of elements arranged in a sorted order. For case 1 to be possible, there must be an x in s_{i-1} where the number of elements in s_{i-1} greater than x is exactly m_i.

But since the set is sorted, the count of elements greater than x is the number of elements after x in the sorted list. So for example, if the sorted list is [a_1, a_2, ..., a_k], where a_1 < a_2 < ... < a_k, then for element a_j, the number of elements greater than it is k - j. So m_i must equal k - j for some j in 1..k.

So for case 1 to be possible, m_i must be one of the possible values of k - j, where k is |s_{i-1}|. So possible m_i can range from 0 to k-1.

Wait, but the m_i given in the input is 0 ≤ m_i < i. And for day i, the maximum possible k (size of s_{i-1}) is i-1 (since each day can add at most one new element). So for m_i to be possible in case 1, m_i must be ≤ k-1, where k is the size of s_{i-1}.

But if case 1 is possible (i.e., there exists an x in s_{i-1} such that the count of elements >x is m_i), then we can avoid adding a new element. Otherwise, we must add a new one.

So the algorithm needs to track the current set s_{i-1} (but storing all elements is not feasible for n up to 1e5). So we need a way to represent the possible m_i values that can be handled without adding new elements.

Alternatively, since the elements are ordered, perhaps we can track the possible multiset of possible m_i values that can be handled by the existing elements. For example, for the current set s_{i-1} of size k, the possible m_i values for case 1 are the numbers of elements greater than x for each x in s_{i-1}. These are 0, 1, ..., k-1. Because for the sorted elements a_1 < a_2 < ... < a_k, the number of elements greater than a_j is k-j. So j can be from 1 to k, giving k-j values from k-1 (when j=1) down to 0 (j=k). So for the existing set of size k, the possible m_i values that can be handled in case 1 are 0, 1, ..., k-1.

Wait, but if the set is size k, then the possible m_i values for case 1 are exactly the numbers 0, 1, ..., k-1. Because for any of those m_i, we can choose the x in s_{i-1} such that the count of elements greater than x is m_i. For example, if m_i is m, then choose x to be the element at position k - m in the sorted list. Because there are m elements after it (since the elements are sorted). So for any m_i in 0 to k-1, case 1 is possible. But if m_i >= k, case 1 is impossible, so we have to add a new element.

Wait, that's a crucial insight! For example, when processing day i, the size of s_{i-1} is k. Then, for case 1 to be possible, m_i must be <= k-1, since the possible values are 0 to k-1. But if m_i is >=k, then case 1 is impossible, so we have to add a new element. However, according to the problem's constraints, the input m_i is such that m_i < i. But i can be larger than k. For example, after several days where no new elements are added, the size k can be less than i. So for example, if i is 5 and k is 3, then m_i could be 3, which is >=k (3 >=3). So case 1 would be impossible. Then, we have to add a new element.

So the algorithm can be structured as follows:

Initialize k=0 (the size of the set after 0 days). For each day i from 1 to n:

- The input is m_i.

- The current set size is k (since s_{i-1} has size k).

- If m_i <= k-1: then case 1 is possible. We can reuse an existing element, so k remains the same. The new set size is k (no change). So sum +=k.

- Else: case 1 is impossible. We have to add a new element. The new set size becomes k+1. So sum += (k+1). Also, the m_i must be equal to the number of elements in s_{i-1} (size k) that are greater than the new element. But how is this possible?

Wait, in case 2, when adding a new element, the new element's m_i is equal to the number of elements in s_{i-1} that are greater than it. So for the new element to have exactly m_i elements above it in s_i (which is s_{i-1} plus the new element), then the new element must be placed in the sorted order such that exactly m_i elements of s_{i-1} are above it.

But how do we model this? Because the new element can be placed anywhere as long as exactly m_i elements of s_{i-1} are above it. But the placement affects the possible m_i for future days.

Wait, but regardless of where the new element is placed, when we add it, the set s_i will have size k+1, and the new element's position in the sorted order will be such that there are m_i elements above it (since we have to choose to place it so that m_i elements are above). So this new element's position in the sorted list of s_i will have m_i elements after it (since the elements in s_i are sorted in increasing order). So when we add a new element, the m_i for that day must equal the number of elements in s_{i-1} that are greater than the new element. But how can we model this to track possible future m_i values?

Actually, when we add a new element, the new set s_i will have size k+1. The possible m_i for future days can then be up to k (since s_i's size is k+1, so possible m_i can be up to k for case 1 in future days). But in terms of the algorithm, the key is to track the possible positions where new elements can be added so that m_i constraints are satisfied.

But how does this affect the sum of |s_i|?

In the algorithm, for each day i, if m_i <= k-1, then we can choose case 1 (no new element added). So |s_i| =k. If m_i > k-1 (so case 2 is needed), then |s_i| =k+1.

But this only holds if, in case 2, it's possible to have m_i elements in s_{i-1} greater than the new element. Because s_{i-1} has size k. So when we add a new element, the number of elements in s_{i-1} greater than it is m_i. So m_i must be <=k. Because s_{i-1} has k elements. So the maximum possible number of elements greater than the new element is k.

But the problem's input constraints say that m_i <i. So for example, when i=5, m_i can be up to 4. But if k (the size of s_{i-1}) is 3, then m_i can be 3, which is <=k. So adding a new element would be allowed.

So the algorithm would proceed as follows:

We track k, the current size of the set. For each day i:

If m_i <= k-1: then we can choose to not add a new element. So sum +=k.

Else: we must add a new element. So sum += (k+1), and k increases by 1.

But wait, this approach would work only if in case 2, m_i is <=k. Because the maximum possible m_i when adding a new element is the number of elements in s_{i-1} (size k) that are greater than the new element. So m_i can be from 0 to k. But according to the problem statement, m_i is given, and for case 2 to be possible, m_i must be <=k.

But according to the problem's input constraints, m_i is <i. So when i is the current day, and k is the size of s_{i-1}, which is up to (i-1). So when adding a new element, k increases to (k+1), but in the next day, i+1, the maximum possible m_i would be i, but according to the input constraints, m_{i+1} <i+1. So the problem allows m_i up to i-1, which could be larger than k (size of s_{i-1}).

Wait, but according to the algorithm above, when processing day i:

If m_i >k-1, then case 1 is not possible. So we must add a new element. But to do this, m_i must be <=k (the size of s_{i-1} is k, so the maximum possible number of elements greater than the new element is k). So if m_i >k, then case 2 is impossible. But according to the problem statement, the input m_i must be possible.

But the problem statement says that the input is such that there exists a valid sequence of l_i's. So the given m_i's are valid, so whenever we have to process m_i, the case where it's possible.

But according to the algorithm outlined, when we process day i, the current k is the size of s_{i-1}. So for case 2, m_i must be <=k. Because s_{i-1} has k elements, and the new element's position in the sorted list must have exactly m_i elements of s_{i-1} greater than it. So m_i can be 0 to k. So in the algorithm, for case 2, m_i must be <=k. But according to the problem's constraints, m_i <i. So when i>k, this is possible.

But how can we ensure that when processing day i, m_i is <=k (the size of s_{i-1}) in case 2?

Wait, maybe we can model this step by step. Let's take the first example:

Sample Input 1:

6

0 1 0 3 0 2

Sample Output:6

Let's track the algorithm:

Initialize k=0.

Day 1:

m_i=0.

Check if 0 <=k-1. k is 0, so k-1 is -1. 0 is not <=-1. So we have to add a new element. So k becomes 1. Sum is 1.

Day 2:

m_i=1. Check if 1 <=k-1 (k is 1, k-1=0). 1>0. So add new element. k becomes 2. Sum +=2 (total 1+2=3).

Day 3:

m_i=0. Check if 0 <=2-1=1. Yes. So case 1 is possible. sum +=2 (total 5). k remains 2.

Day4: m_i=3. Check 3 <=2-1=1. No. So add new element. k becomes3. Sum +=3 (total 8).

Day5: m_i=0. Check 0 <=3-1=2. Yes. Sum +=3 (11).

Day6: m_i=2. Check 2 <=3-1=2. Yes. Sum +=3 (14).

Sum of |s_i| is 14. sum(m_i) is 0+1+0+3+0+2=6. The answer is 14 -6 -6 =2. But the sample output is6. Wait, this is conflicting. So something is wrong here.

Wait, wait, no. Wait the sample output is 6. Let's recheck.

Wait according to the problem statement, the answer is the sum of d_i, which is sum(|s_i| -m_i -1) for all i. The sum of |s_i| in the first example would be 1 (day1) +2 (day2) +2 (day3) +3 (day4) +3 (day5) +3 (day6) = sum is 1+2+2+3+3+3=14. sum(m_i) is 0+1+0+3+0+2=6. n=6. So 14-6-6=2. But the sample output is6. So this approach is wrong.

Hmm. So the approach I outlined is incorrect. That means there's a flaw in my reasoning.

So what's wrong here?

Ah! Oh wait, the formula sum(d_i) is sum(|s_i| -m_i -1) for each i. So the answer in the first example would be (1-0-1)+(2-1-1)+(2-0-1)+(3-3-1)+(3-0-1)+(3-2-1) = 0 +0 +1 +(-1) +2 +0 = 2. But the sample output is6. So clearly, this approach is incorrect.

So there's a mistake in the reasoning. Let me re-examine the problem.

The mistake is in the formula for d_i.

Wait, d_i is the number of marks strictly under the water on day i. Let's rederive the formula.

For day i:

The marks present after day i are s_i. The current level is l_i. The number of marks above is m_i. The number of marks below is d_i. And the current level's mark is part of s_i. So:

m_i + d_i +1 = |s_i|.

So d_i = |s_i| - m_i -1.

So the sum of d_i is sum(|s_i| -m_i -1) over all days.

In the first example, according to the note, the sum of d_i is 0+0+2+0+3+1=6.

But according to the approach I outlined, the sum of |s_i| is 14 (summing 1,2,2,3,3,3), sum(m_i) is6, so 14-6-6=2, which is different from the sample output. So the approach is wrong.

So why is there a discrepancy?

Because the approach's way of modeling |s_i| is incorrect. Because the way the algorithm adds new elements may not model the actual possible |s_i| correctly.

So let's re-examine the first sample input and see what the correct |s_i| sequence is.

Sample Input 1:

6

0 1 0 3 0 2

Sample Output 6.

The note says:

On day3, a new mark is created. Because otherwise, day4 can't have 3 marks above.

So let's see the days:

Day1: m=0. So the current level is new. So s_1 has 1 mark. d_1=0.

sum_d starts at 0.

Day2: m=1. So the current level is new (since in the note, day4 requires it). So s_2 has 2 marks. d_2=0 (since 2-1-1=0).

sum_d now 0+0=0.

Day3: m=0. According to note, a new mark is created. So s_3=3. d_3=3-0-1=2.

sum_d 0+0+2=2.

Day4: m=3. Now, s_3 has 3 elements. Adding a new mark (since m=3=3 elements in s_3? Because s_3 has 3 elements. So the new element must be placed such that 3 elements are above it, but s_3 has 3 elements. Wait, when adding a new element, the new element is inserted after 3 elements? So the new element is higher than all existing elements. So s_4 now has 4 elements. So m_i for day4 is3, which is exactly the number of elements in s_3 (3 elements) that are above the new element. So yes.

d_4=4-3-1=0. sum_d becomes 2+0=2.

But according to the note, the sum for day4 is 0.

Day5: m=0. The current level could be existing. So s_4 has4 elements. m=0, which is <=3 (4-1). So case1 possible. So s_5 remains4. d_5=4-0-1=3. sum_d now 2+0+3=5.

Day6: m=2. s_5 has4 elements. 2 <=3. So case1 possible. d_6=4-2-1=1. sum_d 5+1=6. Which matches the sample.

So the sum of |s_i| is:

Day1:1, day2:2, day3:3, day4:4, day5:4, day6:4.

Sum is 1+2+3+4+4+4 =18. sum(m_i) is0+1+0+3+0+2=6. n=6. So sum_d=18-6-6=6, which matches the sample.

So in this case, the algorithm's approach of adding new elements only when m_i exceeds k-1 is incorrect. Because in day3, m_i=0 which is <=k-1 (k=2 after day2). So according to the algorithm, case1 is possible, and no new element is added. But in reality, in this example, a new element is added on day3.

So why does this happen? Because in some cases, even though m_i is <=k-1, we have to add a new element to satisfy future constraints.

Ah! So the previous approach is incorrect because it greedily chooses to not add a new element whenever possible, but this may not be optimal. Because adding a new element now may allow more case1 choices in the future, leading to a lower overall sum.

Wait, but how? For example, in the first sample, adding a new element on day3 (even though m_i=0 is <=k-1=1) allows the sum of |s_i| to be higher, but the future constraints (like day4's m=3) require adding a new element which can only be done if the previous days have added enough elements.

Wait, in the first sample:

Day3: m=0. According to the algorithm's approach, k after day2 is2. So m=0 <=1. So case1 is possible. So no new element added. So |s_3|=2. Then day4's m=3. Then k is2 (from s_3). So 3>1 (k-1=1). So case2 is needed. So we must add a new element. Then k becomes3. |s_4|=3.

But m_i=3 must be equal to the number of elements in s_3 (size 2) that are greater than the new element. So the new element must have 3 elements greater than it. But s_3 has size 2. So 3>2. This is impossible. So the algorithm's approach would not be able to handle day4's m_i=3.

Which is why the example requires adding a new element on day3. So the algorithm's approach is incorrect. Because the algorithm would proceed as follows:

Day1: m=0. k=0. m_i=0>k-1=-1. So add new element. k=1. sum=1.

Day2: m=1. k=1. m_i=1>k-1=0. Add new. k=2. sum=1+2=3.

Day3: m=0. k=2. m_i=0 <=1. No new. sum +=2. total=5. k remains2.

Day4: m=3. k=2. m_i=3>1. So add new. But the new element must have exactly 3 elements in s_{i-1} (size2) greater than it. Which is impossible. So this scenario is invalid. Hence, the algorithm's approach would not handle the first sample input.

Thus, the initial approach is wrong. The algorithm must not greedily choose to avoid adding new elements when possible, because that may lead to impossible cases in the future.

So the problem is more complex. We need to find a way to model the required additions of new elements even when m_i allows not adding them, but future m_i's require it.

Thus, the correct approach must find when adding a new element is necessary for future days, even if the current m_i allows not adding it.

This suggests that the algorithm needs to track not just the current size k, but also the possible ranges of m_i that can be handled in the future. However, this is computationally challenging, especially for n up to 1e5.

So what's the correct way to model this?

Alternative approach: The key insight is that each time we add a new element, we can cover certain m_i values in the future. For example, when you add a new element, the size k increases, allowing larger m_i values to be handled in case1 in future days.

So, when processing day i, even if m_i can be handled by case1 (m_i <=k-1), adding a new element might be necessary to allow higher m_i values in future days.

But how can we model this? For example, in the first sample, on day3, even though m_i=0 <=1 (k=2), adding a new element allows k to increase to3, so that on day4, m_i=3 can be handled as case2 (since in that case, after adding a new element, the new element's m_i=3 must be equal to the number of elements in s_{i-1} (which is3) that are greater than it. Which would be possible if the new element is placed such that all 3 elements are greater than it (i.e., the new element is the smallest). So m_i=3 would require that there are 3 elements in s_{i-1} (which is3 elements) greater than the new element. Which is possible.

So the problem requires that, for each day i, we have to decide whether to add a new element or not, even if m_i allows case1, but in a way that future m_i's can be handled.

So the correct approach must track not only the current size k but also the possible positions where new elements can be inserted, which affects the possible m_i's in future days.

But how can this be done efficiently?

Another observation: Each time a new element is added, the new element can be placed in a position that allows certain m_i's in the future.

But modeling this for all possible positions is not feasible for large n.

Alternative idea: For each new element added, we can track the possible m_i's that can be achieved by inserting it into the sorted list. For example, inserting a new element at a position that allows m_i (for that day) creates new possible ranges of m_i for future days.

But how to model this efficiently?

An alternative approach inspired by the problem's sample:

The problem requires that whenever adding a new element is possible (i.e., when m_i equals the number of elements in s_{i-1} that are greater than the new element), we can choose to add it, which increases k by 1 and allows future days to have larger m_i's.

But the decision to add a new element even when case1 is possible depends on future m_i's.

This sounds like a dynamic programming problem where the state is the current k and some other parameters. However, with n up to 1e5, this approach must be O(n) time.

Another idea: The minimal sum is achieved by adding new elements as early as possible when required by future m_i's. So the algorithm needs to find the earliest days where a new element must be added, given the future m_i's.

This suggests processing the days in reverse order. Let's think about this.

If we process the days from the end to the beginning, we can determine the minimal required k for each day.

For example, the last day (day n) must have m_n <=k_{n-1} -1 if case1 is possible, or k_{n-1} must be such that adding a new element allows m_n =k_{n-1}.

But this is not obvious.

Alternatively, for each day i in reverse order, compute the minimal possible k that must be present at day i-1 to satisfy the current m_i and all future days.

This approach is inspired by the problem of determining the minimal number of elements needed in the set to satisfy all m_i constraints.

Let's try this.

Let's process the days in reverse order, keeping track of the minimal required k for day i-1.

Initially, after day n, there's no day n+1, so the required k for day n is determined by the m_n.

For each day i from n down to 1:

- To handle day i's m_i, if we choose to add a new element, then the required k for day i-1 is m_i. Because the new element must have exactly m_i elements in s_{i-1} that are greater than it. So the size of s_{i-1} must be >= m_i. But when adding a new element, the new k for day i is (k_{i-1} +1).

But how does this help in determining the required k?

Alternatively, here's the key idea: For each day i, the minimal possible k after day i (i.e., the size of s_i) is determined by the constraints of m_i and the future days.

When processing in reverse:

- We start with the last day. For the last day, the possible k after day n (which is the size of s_n) must satisfy m_n <=k-1 (case1) or case2.

But case2 requires that m_n =k_{n-1}, where k_{n-1} is the size before day n.

But this seems complicated.

Another approach inspired by the problem's note:

The correct way to model the problem is to track not just the current k, but also the allowable range of m_i's that can be handled in future steps. For example, when adding a new element, the new element's position in the sorted list determines the possible m_i's for future days.

But this is difficult to model.

Alternative approach:

The correct way to model the problem is to realize that each new element added must allow certain m_i's in the future. Thus, the algorithm must find the minimal number of new elements added, but arranged such that for each new element added on day i, the m_i equals the number of elements in s_{i-1} that are greater than it.

But how to determine this?

In the first sample, day3's m_i is0. If we do not add a new element, then s_3 is size 2. For day4's m_i=3, we need to add a new element, but s_{i-1} is size2, so m_i=3>2. Which is impossible. Hence, the algorithm must add a new element on day3, even though m_i=0 allows case1.

Thus, the algorithm must look ahead to future m_i's and determine whether adding a new element now is required.

But how can this be done efficiently?

Perhaps the solution is to keep track of the minimal required size of s_i for each day, considering future constraints.

Let's process the days in reverse order.

Initialize a variable required =0.

For day i from n downto 1:

   current m is m_i.

   case1: if we do not add a new element for day i. Then, the required size of s_{i-1} must allow m_i <= (size of s_{i-1}) -1. Also, the size of s_i is the same as s_{i-1}. But in this case, the required size for s_{i-1} is at least (m_i +1).

   case2: if we add a new element for day i. Then, m_i must equal the number of elements in s_{i-1} that are greater than the new element. So the new element is inserted such that there are m_i elements above it. Thus, the size of s_{i-1} must be at least m_i. The size of s_i is s_{i-1} +1. But for the next days (processed in reverse), the required size is s_i.

So the required size for s_{i-1} is max(m_i, required_prev -1). Because:

- If case1 is possible, then s_{i} (after day i) is s_{i-1}, which must be >= required_prev.

   So s_{i-1} >= required_prev.

   Also, m_i must be <= s_{i-1} -1.

   So s_{i-1} >= max(m_i +1, required_prev).

- If case2 is taken, then s_{i-1} must be >= m_i.

   And s_i = s_{i-1} +1, which must >= required_prev.

   So s_{i-1} +1 >= required_prev.

   Thus, s_{i-1} >= max(m_i, required_prev -1).

But we want to choose the minimal possible s_{i-1} to minimize the sum.

But we need to choose between case1 and case2, whichever allows the minimal s_{i-1}.

But since we process in reverse, the required_prev is the minimal required size for s_i. For each day i, we can compute the minimal required size for s_{i-1} as the minimal between the two cases.

Let's formalize this:

When processing day i in reverse order, the minimal required size for s_{i-1} is:

case1: s_{i-1} must be >= max(m_i +1, required_prev)

case2: s_{i-1} must be >= max(m_i, required_prev -1)

We choose the minimal possible s_{i-1} between the two options.

But since we want to minimize the sum of s_i, which is the sum of the required sizes after each day, we need to choose the option that leads to the smallest possible sum.

But how to model this? For example, if case1 requires s_{i-1} to be larger than case2, but allows s_i to be smaller.

The key idea is to compute the required_prev for each day i as the minimal possible s_{i-1} for either case1 or case2.

Let's proceed with an example using the first sample.

Sample Input 1:

n=6, m = [0,1,0,3,0,2]

Process in reverse order:

Initialize required_prev =0.

Day6: m=2.

We can choose case1 or case2.

case1: s_6 = s_5, and s_5 must be >= max(2+1=3, required_prev=0). So s_5 >=3.

case2: s_5 must be >= max(2, required_prev-1= -1). So s_5 >=2. And s_6 = s_5 +1.

But required_prev is the minimal required s_6. Since this is the first day processed (last day), required_prev is 0. So for case2, s_5 >=2. Then s_6= s_5+1 >=3.

But since required_prev is0, any s_6 >=0 is acceptable. So case2 allows s_5 >=2. So the minimal s_5 for case2 is 2. Then s_6=3.

For case1, s_5 >=3. So s_6=3.

So for day6, the minimal s_5 is min between case1 (3) and case2 (2). We choose case2, which requires s_5 >=2. So required_prev for day5 is 2.

But required_prev for day6's case2 is required_prev=0. So s_5 must be >= max(2, 0-1) =2. So required_prev for day5 becomes 2+1=3? No. Let me re-examine.

Wait, when processing day i in reverse, required_prev is the required size for s_i. For case1, s_i is s_{i-1}, so s_{i-1} must be >= required_prev.

For case2, s_i is s_{i-1} +1. So s_{i-1} +1 >= required_prev. Thus, s_{i-1} >= required_prev -1.

So for day i, when processing in reverse, required_prev is the required size for s_i (the size after day i).

So for day6, required_prev is 0. Because after processing day6, there are no days left. So s_6 can be any size >=0.

But we need to find the minimal possible s_{i-1} (s_5) for day6.

case1: s_6 = s_5. required_prev is 0. So s_5 >= max(m_i +1=3, required_prev=0) → s_5 >=3.

case2: s_5 must be >= max(m_i=2, required_prev-1= -1) → s_5 >=2. And s_6 = s_5 +1. Since required_prev=0, this means s_5+1 >=0 → s_5 >=-1. But since s_5 is at least0, this is always true.

So between case1 and case2, case2 requires s_5 >=2, which is smaller than case1's 3. So the minimal s_5 is 2.

But wait, this would imply that for day6, we choose case2 (add a new element). So s_5 is 2, and s_6 is3. But day6's m_i is2. The new element added in case2 must have m_i equal to the number of elements in s_5 (size2) that are greater than it. So m_i=2 requires that the new element is inserted such that there are 2 elements in s_5 greater than it. Which is possible only if s_5 contains two elements, and the new element is smaller than both. But how?

Because s_5 is of size2. So when adding a new element on day6, the number of elements greater than it is 2. So the new element must be the smallest in the sorted list. Then, the two existing elements are larger. So yes.

So this is possible.

Thus, required_prev for day5 is 2 (s_5 >=2).

Day5: m=0.

Process in reverse.

required_prev=2.

case1: s_5 = s_4. So s_4 >= max(0+1=1, required_prev=2) → s_4 >=2.

case2: s_4 >= max(0, required_prev-1=1) → s_4 >=1. And s_5 =s_4 +1. So s_5 >=2 (required_prev=2).

So s_4 +1 >=2 → s_4 >=1.

case2 requires s_4 >=1, and case1 requires s_4 >=2.

The minimal is case2's s_4 >=1. So required_prev for day4 is 1.

But s_5 =s_4 +1 must >=2 → s_4 >=1. So s_4 can be 1, leading to s_5=2, which is sufficient.

Day4: m=3.

required_prev=1.

case1: s_4 =s_3. s_3 >= max(3+1=4, required_prev=1) → s_3 >=4.

case2: s_3 >= max(3, required_prev-1=0) → s_3 >=3. s_4 =s_3 +1 >=1 → s_3 >=0. So s_3 >=3.

So the minimal between case1 (s_3 >=4) and case2 (s_3 >=3) is case2's 3. So required_prev for day3 is3.

But for case2, adding a new element on day4 requires that m_i=3 equals the number of elements in s_3 that are greater than the new element. So s_3 must be >=3. For example, s_3=3. Then, the new element must be inserted such that exactly3 elements in s_3 are greater than it. But s_3 has size3. So this is possible only if all elements in s_3 are greater than the new element, i.e., the new element is the smallest. So when added, s_4=4, and the new element has3 elements greater than it. So yes.

Day3: m=0.

required_prev=3.

case1: s_3 =s_2. s_2 >= max(0+1=1, required_prev=3) → s_2 >=3.

case2: s_2 >= max(0, required_prev-1=2) → s_2 >=2. s_3 =s_2 +1 >=3 → s_2 >=2.

So the minimal is case2's s_2 >=2. required_prev for day2 is 2.

So s_2=2. s_3=3.

Day2: m=1.

required_prev=2.

case1: s_2 =s_1. s_1 >= max(1+1=2, required_prev=2) → s_1 >=2.

case2: s_1 >= max(1, required_prev-1=1) → s_1 >=1. s_2 =s_1 +1 >=2 → s_1 >=1.

So case1 requires s_1 >=2, case2 requires s_1 >=1. So case2 is better. required_prev for day1 is1.

Day1: m=0.

required_prev=1.

case1: s_1 =s_0 (s_0 is0). s_0 >= max(0+1=1, required_prev=1) → s_0 >=1. But s_0 is0. Impossible.

case2: s_0 >= max(0, required_prev-1=0) → s_0 >=0. s_1 =s_0 +1 >=1.

So s_0=0. s_1=1.

Thus, the required_prev for day0 is0.

So the required_prev for each day:

Day1: s_0=0 → s_1=1.

Day2: s_1=1 → s_2=2 (case2).

Day3: s_2=2 → s_3=3 (case2).

Day4: s_3=3 → s_4=4 (case2).

Day5: s_4=1 → s_5=2 (case2).

Day6: s_5=2 → s_6=3 (case2).

But the sum of s_i from day1 to day6 is 1+2+3+4+2+3= 1+2 is3, +3=6, +4=10, +2=12, +3=15. But this doesn't match the sample's sum of 18. So something's wrong.

Wait, this approach calculates the required_prev for each day, but the sum is computed as the sum of s_i, which is the required_prev for each day. But when processing in reverse, required_prev is the required s_i for day i. So for the first sample, the sum would be s_1=1, s_2=2, s_3=3, s_4=4, s_5=2, s_6=3. But this sum is 1+2+3+4+2+3=15. The sample's sum is 18, which is higher. So this approach is not correctly capturing the sum.

Ah, no. Because the required_prev for each day is the minimal required s_i. But the sum of s_i is determined by the required_prev values. For example, after processing day6, the required_prev is3 (s_6=3), and for day5, required_prev is2 (s_5=2). But in reality, s_5 can be 2, but the way s_4 is computed must allow s_5=2.

But according to the example, s_4 is4. So how is this possible?

Hmm, perhaps the reverse approach is not capturing the actual sizes but the minimal possible sizes required to satisfy the constraints.

So the sum of s_i is not directly the sum of the required_prev values but is derived from the required_prev values processed in reverse.

But this is getting complicated.

Alternative approach:

The correct way to model this problem is to track for each day whether adding a new element is required, considering future constraints.

This requires that for day i, if there exists a future day j where m_j >=k, where k is the current size after day j-1, then we must have added enough elements before j.

Thus, for each day i, we need to track the maximum m_j for j >=i. If any m_j >=k, then k must be increased to at least m_j by adding new elements.

So the algorithm can be as follows:

- Compute the maximum m_j for each position i to n.

- Then, for each day i from1 to n:

   if m_i >= current k or the maximum future m_j exceeds current k:

      add a new element.

      current k +=1

   else:

      do not add.

Thus, the algorithm ensures that current k is at least the maximum m_j for all future j.

But how to implement this efficiently?

We can precompute an array of the maximum m_j from i to n.

Let's try this approach for the first sample:

max_m array:

For each i from1 to6:

max_m[i] = max(m_i, m_{i+1}, ..., m6)

Sample m = [0,1,0,3,0,2]

max_m[1] =3 (maximum of 0,1,0,3,0,2)

max_m[2] =3 (1,0,3,0,2)

max_m[3] =3 (0,3,0,2)

max_m[4] =3 (3,0,2)

max_m[5] =2 (0,2)

max_m[6] =2 (2)

Processing day1 to day6:

k starts at0.

For each day i:

if m_i >=k or max_m[i] >k:

   add new element.

   k +=1

Else:

   do not add.

Day1:

max_m[1] is3. current k is0.

m_i=0 <0 → no. But max_m[1] =3 >0. So add new. k=1.

sum_s +=1.

Day2:

max_m[2] is3. current k=1.

m_i=1 >=1 → add new. k=2. sum_s +=2.

Day3:

max_m[3] is3. current k=2.

m_i=0 <2. but max_m[3] =3>2. So add new. k=3. sum_s +=3.

Day4:

max_m[4] is3. current k=3.

m_i=3 >=3 → add new. k=4. sum_s +=4.

Day5:

max_m[5] is2. current k=4.

m_i=0 <4. max_m[5] is2 <4. So no add. sum_s +=4.

Day6:

max_m[6] is2. current k=4.

m_i=2 <4. max_m[6] is2 <4. So no add. sum_s +=4.

Sum_s is1+2+3+4+4+4=18. Which matches the sample's sum of 18.

The sum of d_i is18-6-6=6, which matches the sample.

So this approach seems to work.

Another test case:

Sample Input 2:

5

0 1 2 1 2

Output is1.

max_m array:

For i=1: max(m1, m2, m3, m4, m5) =2.

i=2: max(1,2,1,2) =2.

i=3: max(2,1,2) =2.

i=4: max(1,2) =2.

i=5: 2.

Processing:

k=0.

Day1:

m=0 <0? No. max_m[1]=2>0. Add new. k=1. sum=1.

Day2:

m=1 >=1. Add new. k=2. sum=1+2=3.

Day3:

m=2 >=2. Add new. k=3. sum=6.

Day4:

m=1 <3. But max_m[4] is2 <3. So no add. sum +=3.

Day5:

m=2 <3. max_m[5]=2 <3. No add. sum +=3.

Total sum is 1+2+3+3+3=12. sum(m) is0+1+2+1+2=6. sum_d=12-6-5=1. Which matches the sample.

Another sample input:

Sample3:

5

0 1 1 2 2

Output is0.

max_m array:

i=1: max(0,1,1,2,2) →2.

i=2: max(1,1,2,2) →2.

i=3: max(1,2,2) →2.

i=4: max(2,2) →2.

i=5:2.

Processing:

k=0.

Day1:

max_m[1]=2>0. Add new. k=1. sum=1.

Day2:

m=1 >=1. Add new. k=2. sum=3.

Day3:

m=1 <2. But max_m[3] is2>=2. So add new. k=3. sum=6.

Day4:

m=2 <3. max_m[4]=2 <3. No add. sum +=3.

Day5:

m=2 <3. No add. sum +=3.

Sum is1+2+3+3+3=12. sum(m) is0+1+1+2+2=6. sum_d=12-6-5=1. But sample output is0.

Wait, this contradicts. So what's wrong here?

Wait sample3's output is0. According to this approach, the sum of s_i is12. sum(m) is6. n=5. 12-6-5=1. But sample output is0. So the approach is incorrect.

But sample3's explanation says that the sum of d_i is0.

Wait sample3's input is:

5

0 1 1 2 2

The correct sequence of adding elements:

Day1: add new. s_1=1. d_1=0.

Day2: add new. s_2=2. d_2=0.

Day3: no new. s_3=2. d_3=2-1-1=0.

Day4: add new. s_4=3. d_4=3-2-1=0.

Day5: no new. s_5=3. d_5=3-2-1=0.

Sum of d_i is0.

Sum of s_i is1+2+2+3+3=11. sum(m) is6. sum_d=11-6-5=0.

But according to the approach's processing:

Day3: max_m[3] is2, current k=2. So max_m[3] is2 >=k=2. So add new. k=3. sum becomes1+2+3=6.

Day4: m=2 <3. max_m[4]=2 <3. So no add. sum +=3 →9.

Day5: m=2 <3. max_m[5]=2 <3. No add. sum +=3 →12.

Thus, the approach's sum is12, leading to sum_d=12-6-5=1. But the correct sum is11.

So the approach is incorrect.

Thus, the previous approach of adding a new element when either m_i >=k or max_m[i] >k is not correct.

So what's the mistake?

In sample3, day3's m_i is1. The current k is2. max_m[i=3] is2. So according to the approach, since max_m[i=3] >=k (2 >=2), we add a new element. But in the correct solution, no new element is added on day3. So the approach's logic is incorrect.

This suggests that the algorithm needs to be revised.

So why is the correct solution possible without adding a new element on day3, even though the future m_i's (day4 and day5) require m_i=2, which is equal to the current k=2?

Because in this case, after day3, the set size is2. For day4, m_i=2. But the current k is2. So case2 (adding a new element) is required. The new element must have exactly2 elements in s_{i-1} (size2) greater than it. So s_{i-1} is size2. So m_i=2 can be achieved by adding a new element that is smaller than both existing elements. Because s_{i-1} has size2. So when adding a new element, the new element is placed such that there are2 elements greater than it. So this is possible.

Thus, the correct solution adds a new element on day4, but not on day3.

Thus, the algorithm's previous approach of adding a new element when max_m[i] >=k is incorrect. Because even if future m_i's are equal to the current k, adding a new element may be possible.

So the correct condition should be to add a new element when the future maximum m_j exceeds the current k, or when m_i is greater than or equal to the current k.

But in sample3, the future maximum after day3 is2. The current k after day3 is2. So 2 <=k, so no need to add new elements.

Thus, the condition should be if m_i >=k or the future maximum m_j >=k+1.

Because if future m_j can be handled by adding new elements when needed, as long as the current k is at least the future m_j.

But this is getting complex.

Alternative idea:

The algorithm should track the current k and the required k for each day.

For each day i from left to right:

   required_k = max(m_i, required_k_prev)

But this is unclear.

Another approach inspired by the correct solution for sample3:

The algorithm should add a new element on day i if and only if m_i > current k-1 or there exists a future day j where m_j >= current k.

But again, how to compute this.

Alternatively, the minimal number of new elements to add is the maximum of m_i for all i, plus 1.

But sample1 has maximum m_i=3. So new elements are4. Which matches the sample.

Sample3's maximum m_i=2. So new elements are3. But the correct sum of s_i is 1+2+2+3+3=11, which has 3 new elements.

Thus, this approach may not directly apply.

Another idea: the minimal number of new elements to add is the maximum m_i plus 1 minus the number of days that have m_i= max_m.

But this is not clear.

Alternative approach:

The correct algorithm should add a new element on day i if m_i is greater than the number of existing elements minus1, or if there exists a future m_j that requires a larger k than the current.

Thus, the algorithm must look ahead and determine the required k after each day.

This can be done by precomputing the maximum m_j for each day i to n. Let's call this max_future[i].

Then, for each day i:

   if m_i > k-1 or max_future[i+1] >k:

      add a new element.

      k +=1

   else:

      do not add.

But how to compute max_future[i+1]?

Yes, but when processing day i, we can look ahead to the maximum m_j for days i+1 to n.

So, precompute max_future array where max_future[i] is the maximum m_j for j >=i.

For sample3:

max_future array:

i=1:2, i=2:2, i=3:2, i=4:2, i=5:2.

Processing:

k=0.

Day1: m=0 >k-1 (0-1= -1). No. But max_future[2]=2 >k=0. So add new. k=1.

sum_s +=1.

Day2: m=1 >k-1=0. Yes. Add new. k=2. sum=3.

Day3: m=1 <=k-1=1. Check max_future[4] (which is2). max_future[4] =2. Is 2>k=2? No. So do not add. sum +=2. sum=5.

Day4: m=2 >k-1=1. Add new. k=3. sum +=3. sum=8.

Day5: m=2 <=k-1=2. Check max_future[6] (which is0, assuming max_future[6]=0). So do not add. sum +=3. sum=11.

Sum of s_i is1+2+2+3+3=11. sum(m_i) is6. sum_d=11-6-5=0. Which is correct.

So the algorithm needs to check if max_future[i+1] >k. If so, add a new element.

Thus, the correct approach is to add a new element on day i if either:

1. m_i > current k-1, or

2. the maximum m_j from day i+1 to n exceeds current k.

This way, adding a new element ensures that future m_j's can be handled.

This approach seems to handle all samples correctly.

Let's test this algorithm on sample3:

Processing:

max_future array:

max_future[i] for i=1 to5 is2,2,2,2,2.

For day3:

max_future[i+1] =max_future[4] =2.

current k=2.

max_future[4] =2 <=k. So no need to add. Thus, day3 does not add a new element.

But for day4:

m_i=2 >k-1=1. So add new. k becomes3.

Thus, the algorithm works.

Another test: sample1:

max_future array:

i=1:3, i=2:3, i=3:3, i=4:3, i=5:2, i=6:2.

Day3:

max_future[4] =3. current k=2. 3>2. So add new.

Thus, the algorithm adds a new element on day3.

Day4: m=3> k-1=3-1=3. 3>3? No. But max_future[5]=0. So add new? No. Wait, day4's m_i=3. current k after day3 is3. So k-1=2. 3>2. So add new. Thus, k becomes4.

Which is correct.

Thus, the algorithm seems to work.

The algorithm is:

precompute max_future array, where max_future[i] is the maximum m_j for j >=i.

Then, for each day i from1 to n:

   if m_i >k-1 or (i <n and max_future[i+1] >k):

      add new element.

      k +=1

      sum_s +=k

   else:

      sum_s +=k

Thus, the code can be written as follows.

Now, let's implement this.

First, precompute max_future array.

We can compute it by iterating from the end to the beginning.

For example:

max_future = [0]*(n+2)

max_future[n] = m[n-1]

for i in range(n-1, 0, -1):

   max_future[i] = max(m[i-1], max_future[i+1])

Then, for each day i from1 to n:

   if m[i-1] >k-1 or (i <n and max_future[i+1] >k):

      add new element.

      k +=1

   sum_s +=k

Yes.

Now, let's code this.

Testing sample3:

n=5, m=[0,1,1,2,2].

max_future array:

i=5: max_future[5] =2.

i=4: max(2, max_future[5])=2.

i=3: max(1, max_future[4])=2.

i=2: max(1, max_future[3])=2.

i=1: max(0, max_future[2])=2.

Processing:

k=0.

day1:

m_i=0 <=k-1=-1 is false.

Check if i <n and max_future[2] (2) >k=0: yes. So add new. k=1. sum_s=1.

day2:

m_i=1 >k-1=0: yes. add new. k=2. sum=1+2=3.

day3:

m_i=1 <=k-1=1. Check i <n (yes) and max_future[4]=2 >k=2? 2>2 no. So no add. sum +=2 →5.

day4:

m_i=2 >k-1=1: yes. add new. k=3. sum=8.

day5:

m_i=2 <=k-1=2. Check i <n (no). So no add. sum +=3 →11.

sum_s=11. sum(m)=0+1+1+2+2=6. answer=11-6-5=0. Correct.

Sample1:

max_future for i=1 is3.

Processing:

k=0.

day1:

0>k-1 (no). i <n. max_future[2]=3>0 →yes. add new. k=1. sum=1.

day2:

1>1-1=0 → yes. add new. k=2. sum=3.

day3:

0>2-1=1 →no. i <n. max_future[4]=3>2 → yes. add new. k=3. sum=6.

day4:

3>3-1=2 → yes. add new. k=4. sum=10.

day5:

0>4-1=3 → no. i <n. max_future[6]=2 <=4. no add. sum=14.

day6:

2>4-1=3 → no. i >=n. no add. sum=17. sum(m)=6. 17-6-6=5. But sample1's answer is6. Wait, this is conflicting.

Wait sample1's sum of s_i according to the correct solution is18. But according to this approach, the sum is1+2+3+4+4+4=1+2=3+3=6+4=10+4=14+4=18.

Ah, yes. So day4:

k=3. add new →k=4. sum +=4 (10).

day5:

k=4. add? m_i=0 >4-1=3? No. i <n. max_future[6] (i+1=6) is 2>4? No. So no add. sum +=4 →14.

day6:

m_i=2>4-1=3? No. i is6 (n=6). no add. sum +=4 →18.

sum_s=18. sum(m)=6. answer=18-6-6=6. Correct.

Thus, this approach works.

Thus, the correct code is to precompute the max_future array, then iterate each day, adding a new element if either m_i exceeds k-1 or if the max_future[i+1] exceeds the current k.

Thus, the code in Python would be as follows.
</think>

```python
n = int(input())
m = list(map(int, input().split()))

max_future = [0] * (n + 2)  # 1-based to n
for i in range(n, 0, -1):
    if i == n:
        max_future[i] = m[i-1]
    else:
        max_future[i] = max(m[i-1], max_future[i+1])

k = 0
total = 0
for i in range(1, n + 1):
    if m[i-1] > k - 1 or (i < n and max_future[i+1] > k):
        k += 1
    total += k

sum_m = sum(m)
print(total - sum_m - n)
```