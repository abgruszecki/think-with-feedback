<think>
Okay, let's see. So the problem is about Polycarp eating chocolate bars during his workday. The goal is to arrange the eating times so that the maximum break between eating is as small as possible. Hmm.

The constraints are that in some minutes he's busy (marked with 1) and can't eat. The first and last minutes are always 0, and he eats in those. Also, k is the number of bars he has, but he doesn't have to eat all. But since he starts with k, he can choose to eat up to k bars. Wait, but the problem says "the next bar in the minute y" so the bars he eats must be in order. So the key is to select k positions (including the first and last minute) where he eats, such that all those positions are 0, and the maximum break between consecutive eats is minimized.

Wait, but he must eat exactly k bars. Because the problem statement says "the order of eating chocolate bars" and the note says in the first example he can't eat the second bar. Wait, in the first example, input is 3 3 and '010'. So the workday is 3 minutes. He has 3 bars. But in the second minute (index 1 or 2?), he's busy. So he can only eat in the first, third minutes. But that's two bars. But since k is 3, but there's no way to eat three. Wait, the problem says "it is guaranteed that k is strictly greater than 1". Wait, the first example's input is 3 3. So the first and third minutes are 0. The second is 1. So he can't eat there. So how can he eat 3 bars? Oh wait, maybe the problem statement's note is wrong. Wait, the first example's output is 1. Let's see: the input is 3 3, which implies n=3 minutes. The string is '010'. So the available minutes are 0 (first), 2 (third). But those are two minutes. So how can he eat three bars? That's impossible. But the note says that he can't eat the second minute. So maybe the problem statement allows not eating all the bars? Wait, the problem says "it is not necessary for Polycarp to eat all bars he has." So the actual number of bars eaten is between 2 (the first and last) and min(k, available positions). Wait, but in the first example, he has 3 bars but only 2 possible positions. So he must eat two bars. Then the maximum break is 1 (between first and third minute). So the output is 1, which matches the example. So the problem allows eating any number of bars (as long as you have enough), but you must choose exactly k bars? Or no, wait, the problem says "the order of eating chocolate bars that the maximum break time between eating bars is as minimum as possible." So Polycarp can choose to eat any subset of the available positions, as long as it's at most k bars, but in order to minimize the maximum break, he might need to eat as many as possible. Because adding more bars would split the intervals into smaller breaks.

Wait, the problem says that the order of eating is such that the maximum break between eating is minimized. So the optimal strategy is to select the positions (including first and last) to eat, such that the number of bars is exactly k (since eating more bars allows us to split the breaks into smaller intervals, which reduces the maximum). Because if he can eat k bars, then he can split the intervals into smaller parts than if he eats fewer. So the problem likely requires that we select exactly k positions (including first and last) to eat, all of which are 0 in the string, and arrange them such that the maximum gap between consecutive positions is minimized.

So the approach is to find the positions where he can eat (the 0s in the string), and choose k of them (including first and last) to split the available slots into intervals with gaps as small as possible.

But how to model this? Let's think.

First, we need to collect all the positions where he can eat. Then, among these positions, select exactly k, including first and last, such that the maximum gap between consecutive selected positions is minimized.

This sounds similar to the problem of placing k elements to minimize the maximum distance between adjacent elements. But in this case, the elements must be chosen from the available positions (the zeros in the string).

But the available positions are given as a string. So first, we need to extract all the indices where the character is '0', as those are the possible eating times.

Once we have that list, let's call it available, which is sorted (since the indices are in order from 0 to n-1). We must select a subset of these available positions, starting with the first, ending with the last, and including exactly k elements. The goal is to choose the k elements such that the maximum of (y - x -1) between consecutive x and y is as small as possible.

Wait, no. The break time is y - x -1. For example, if he eats at minute 1 and then minute 3, the break is 3 -1 -1 = 1 minute. So in the first example, the available positions are 0, 2 (assuming 0-based or 1-based? Let's check the problem statement. The problem says "the i-th symbol in the string equals to zero..." and "the first and the last characters are zero". So for n=3, the string is of length 3. The first minute is 0 (0-based?), but probably the indices are 1-based? Wait, the first example's input is '010' which is 3 characters. So the workday is 3 minutes. The first and last are 0. So the positions are 1, 3 (if 1-based) or 0, 2 (0-based). Then, in the first example, he can't eat in the second position (1-based: 2nd minute is busy). So available positions are 1 and 3 (assuming 1-based). But then, the first and last positions must be included. So he has to pick those two. But k is 3, which is more than 2. So how can that be possible? Wait, the problem says that k is the number of bars he has. But he doesn't have to eat all. So in this case, he can't eat all 3, so he has to eat exactly 2. But k is 3. Oh, right, the problem statement says "it is guaranteed that k is strictly greater than 1". So in the first example, the first and last are required, but the other positions may not be available. So the solution in the first example is that he has to eat the first and last, which gives a break of 1. So even though k is 3, but there's no way to eat 3, so he eats 2. So in the problem, the actual number of bars eaten is the minimum between k and the number of available positions (but since the first and last are required, the minimum is between k and the available count). Wait, but the problem says that the first and last are always 0, and he must eat in those. So the initial positions are the first and last. Then, the rest of the selected positions must be a subset of the available (0s) in between. So the problem requires that the first and last are always selected, and the other selected positions are from the available 0s. So the number of selected positions is at least 2 (the first and last). Then, given k, which can be up to n. But the available positions may be more or less than k.

Wait, the problem says that Polycarp has k bars at the beginning. So he can eat up to k bars. But he must eat at least 2 (the first and last). So the number of positions selected is exactly min(k, the total number of available positions). Because adding more positions (up to k) allows splitting the breaks into smaller intervals, which reduces the maximum. So the optimal approach is to select as many positions as possible (up to k) to minimize the maximum break.

So the steps are:

1. Collect all the positions where the character is 0. Let's call this list zeros. The first element is 0 (assuming 0-based) or 1 (1-based?), and the last element is n-1 (0-based) or n (1-based). Wait, the problem says the first and last are zero. So for example, in the first sample, the input is 3 3 and the string is '010', which for 0-based indices is positions 0, 2 (since index 0 is '0', 1 is '1', 2 is '0'). So zeros would be [0, 2]. Then, the required positions are 0 and 2. Since k is 3, but there's only 2 available positions, he can't eat 3. So he must select all possible 2 positions, which gives a maximum break of 1.

In the second example, input is 8 3 and string '01010110'. Let's parse the string: index 0 is 0 (assuming 0-based?), index 1 is 1, index 2 is 0, index 3 is 1, index4 is 0, index5 is1, index6 is1, index7 is0. So zeros are at positions 0, 2,4,7. So in the sample, the first and last (0 and7) are included. Since k is3, we need to select 3 positions. So the first and last, plus one more. The possible options are 0, 2,7 → breaks between 0-2 (1) and 2-7 (4). Then the maximum is4. Or 0,4,7 → breaks 3 and 2. Max is3. Or 0,2,4,7 (but that's 4 positions and k=3. So wait, the sample's output is3. So the optimal selection is 0,4,7. So the breaks are 4-0-1=3, 7-4-1=2. Max is3. So the answer is3.

So the problem is, given the list of zeros (including first and last), select m positions, where m is min(k, len(zeros)), such that the maximum gap between consecutive positions (y -x -1) is minimized.

Now, the problem is to choose m-2 positions (since first and last are fixed) from the list of zeros. Wait, no. The first and last are part of the zeros list, so the list is already sorted. We need to select a subset of these zeros, starting with the first and ending with the last, with exactly m elements (where m is the min(k, len(zeros))). Then, compute the maximum break between consecutive elements and minimize it.

So how to model this?

This is similar to placing k-1 markers in the zeros list (since first and last are fixed) to split the list into intervals. But the question is, which positions to add to minimize the maximum gap between consecutive selected positions.

This is a classic binary search problem. The approach would be to binary search on the possible maximum gap and check if it's possible to select m positions (including first and last) such that all gaps between consecutive selected positions are <= the current candidate.

But how to compute that efficiently.

Alternatively, since we have to choose m positions (including first and last) from the zeros list, which is sorted, the optimal way to select the positions is to greedily add the positions that allow us to split the largest gaps first.

Wait, but how?

Another approach is to model the problem as follows: after selecting all the zeros, the maximum gap is the maximum of (zeros[i+1] - zeros[i] -1) for consecutive elements. When you add a new position (a zero from the list) between two existing consecutive positions, you split that gap into two smaller gaps. So, to minimize the maximum gap, we need to split the largest gaps first.

So the optimal strategy is to select the m-2 largest gaps (since first and last are already included) and split each of them by inserting additional positions. The maximum gap after splitting will be the largest of the split parts.

Wait, for example, if there's a gap of 10 between two consecutive zeros. If you split it by inserting one position in between, then the two new gaps are (split into 5 and 4, for example). The maximum of those would be 5. So inserting the middle position gives the maximum possible split. So each split can divide the original gap into two parts, and the maximum of those parts is minimized by splitting in the middle.

But the problem is, given that we can split the largest gaps first, how many splits can we do (which is m-2, since first and last are fixed). So the maximum gap after splitting will be the maximum of the gaps in the original list, after splitting the largest (m-2) gaps.

So the approach would be:

1. Collect the list of zeros.

2. Compute all the gaps between consecutive zeros (i.e., zeros[i+1] - zeros[i] -1 for each i from 0 to len(zeros)-2).

3. The initial maximum gap is the maximum of these gaps.

4. The problem is to split these gaps by adding (m-2) positions (since adding a position between two existing zeros splits a gap into two parts). Each split can split a gap into two, and the maximum among the splits for that gap is the value that would contribute to the overall maximum.

5. The optimal way to minimize the maximum is to split the largest gaps first, each split as many times as possible (i.e., split into as many parts as possible, which would be (split_count +1) splits). For example, for a gap of 10, splitting once gives two parts (5 and 4), maximum 5. Splitting again (adding another position) would split one of the parts again, perhaps into 3 and 2, etc.

But this seems complicated. How do we model this?

Alternatively, for each gap, the minimal possible maximum after s splits (s is the number of times we can split this gap) is floor(gap/(s+1)), but I'm not sure. Wait, let's think: the gap is g. If we can split it into s+1 parts, then the maximum possible break after splitting is ceil(g/(s+1 +1))? Wait, perhaps I'm getting confused.

Wait, the original gap is g = zeros[i+1] - zeros[i] -1.

If we add s splits (insert s positions into this gap), then the gap is split into s+1 intervals. Each interval's break is (next - prev -1), which would be (split_point_1 - prev -1), (split_point_2 - split_point_1 -1), etc. To minimize the maximum of these, the splits should be as evenly spaced as possible.

So for a gap g, when split into s+1 parts (after inserting s points), the minimal possible maximum is ceil(g / (s+1)) -1. Wait, maybe. For example:

g=10, s=1 (split into two parts). The minimal maximum is 5 (if split at 5 and 5+1). Then the two breaks are 5-0-1=4, 10-5-1=4. So the maximum is4. Wait, original gap is 10 (between 0 and 10+1=11?), maybe not. Let's see:

Original positions are a and b. The gap between a and b is (b -a -1). For example, a=0, b=3. The gap is 3-0-1=2. So if you split once, you insert a point in between, say c. Then the two gaps are (c -a -1) and (b -c -1). To minimize the maximum of these two, you choose c as a+ (gap +1)/2. For example, gap is 2. So split into 1 and 1. So each break is 1-0-1=0 and 3-1-1=1. Wait, no. Wait, the positions are a, c, b. So the breaks between a and c is (c - a -1) and between c and b is (b -c -1). For a=0, c=1, b=3. The breaks are 1-0-1=0 and 3-1-1=1. The maximum is1. So the minimal possible maximum is1.

Wait, so for a gap g, when split into s+1 intervals (after inserting s splits), the minimal possible maximum is ceil(g/(s+1)).

So for example, g=10, split into 2 intervals (s=1 split): maximum is ceil(10/2)=5. Which gives 5 and 5. Breaks are 5-0-1=4 and 10-5-1=4. So maximum is4. Wait, that's conflicting. Hmm. Maybe I'm miscalculating.

Wait, the original gap is zeros[i+1] - zeros[i] -1. For example, zeros[i] is 0, zeros[i+1] is 3. The gap is 3-0-1 = 2. So inserting a split at 1, the breaks between 0 and1 is 1-0-1=0, between 1 and3 is 3-1-1=1. Max is1. Which is ceil(2/(1+1)) = 1.

So the formula holds. For a gap g, when split into s+1 intervals (s splits), the maximum possible break is ceil(g/(s+1)) -1? Or is it ceil(g/(s+1 +1))? Wait, in the example:

g=2, s=1 split. Then the number of intervals is s+1=2. Each interval's break is (interval_length -1). So for splitting into 2 intervals, the split would be into two parts, each of length 1. So the breaks are 1-0-1=0 and 3-1-1=1. Max is1. So the formula would be ceil(g/(s+1)) = ceil(2/2) =1. So yes.

So the minimal possible maximum after s splits in a gap g is ceil(g/(s+1)).

So the approach is to:

1. Collect all the gaps between consecutive zeros (list of g's).

2. For each gap, how many splits can be assigned to it (s_i splits) such that the sum of s_i over all gaps is equal to (m - (len(zeros) -1)), where len(zeros)-1 is the initial number of gaps (since len(zeros) positions have len(zeros)-1 gaps between them). Because initially, there are len(zeros)-1 gaps, each with 0 splits. When you add s splits, the total number of splits is sum(s_i) = (m-1) - (len(zeros)-1). Because when you have m positions, the number of gaps is m-1, and each split adds a gap. So (m-1) = initial_gaps + sum(s_i). So sum(s_i) = (m-1) - (len(zeros)-1) = m - len(zeros).

So the number of splits available is s_total = m - len(zeros). Because initially, there are (len(zeros)-1) gaps, and after splitting, the total number of gaps is m-1. So the splits added are (m-1) - (len(zeros)-1) = m - len(zeros).

So, the problem reduces to distributing s_total splits among the gaps, such that the maximum ceil(g/(s_i +1)) is minimized.

Each split s_i for gap i contributes s_i splits, and the maximum for that gap is ceil(g_i/(s_i +1)).

Our goal is to find the minimal possible maximum of all the ceil(g_i/(s_i +1)) across all gaps, given that sum(s_i) = s_total.

This is a classic problem that can be solved using binary search. We can binary search on the possible maximum value, and check if it's possible to assign splits such that all gaps' ceil(g_i/(s_i+1)) <= candidate_max and sum(s_i) <= s_total.

So steps:

1. Precompute the list of gaps.

2. Compute the required number of splits: s_total = (m-1) - (len(zeros)-1) = m - len(zeros).

   But m is min(k, len(zeros)), because we can't select more positions than available. So m = min(k, len(zeros)).

   So s_total = (m -1) - (len(zeros) -1) = m - len(zeros). But if m is len(zeros), then s_total is zero. So in that case, the initial gaps are the same as the splits. So the maximum is the maximum of the initial gaps.

   If m is greater than len(zeros), but since m can't exceed len(zeros) (because m is min(k, len(zeros))), this case won't happen.

   So s_total can be zero (if m == len(zeros)) or positive (if m > len(zeros)? No, because m is min(k, len(zeros)). Wait, no. If len(zeros) is 5, and k is 7, then m is 5. So len(zeros) is 5. So s_total is 5-5=0. So no splits. So the maximum gap is the maximum of the initial gaps.

   So for example, when the available positions are exactly k, then we can't split any gaps. So the maximum is the maximum of the initial gaps.

   But when m is larger than len(zeros), but that's impossible. Because m is the minimum of k and len(zeros). So when len(zeros) >=k, then m is k. So in that case, s_total is k - len(zeros), which would be negative. Wait, that can't be. Wait, perhaps I made a mistake in the formula.

   Let's think again.

   The initial number of gaps is (len(zeros) -1).

   After selecting m positions, the number of gaps is (m-1).

   So the number of splits added is (m-1) - (len(zeros) -1) = m - len(zeros).

   But if m is less than len(zeros), then m - len(zeros) is negative. Which is impossible. So this suggests that when m < len(zeros), we have to remove some positions, which would merge gaps. But that would increase the maximum gap. So this contradicts the initial logic. Therefore, perhaps m can't be less than len(zeros), because when you have len(zeros) positions available, and you need to choose m positions (including first and last), you can't have m less than len(zeros) because that would imply you're not choosing some positions, which would merge gaps. But how can that be possible? For example, suppose len(zeros) is 5, and m is 3. Then we have to select 3 positions (including first and last). So we have to choose two other positions. But merging some gaps. But this would require that the gaps between the selected positions are larger. So the approach would be different.

   Wait, this indicates that my previous approach is only applicable when m >= len(zeros), which is not possible. So I think I have misunderstood the problem.

   Let me re-express the problem. The available positions are all the zeros in the string, sorted. We must select exactly m positions (including first and last), where m is the minimum of k and the number of available positions (len(zeros)). Because if k is larger than len(zeros), then we can't choose more positions than available. So m = min(k, len(zeros)).

   So, when len(zeros) >=k, then m=k. So in this case, we need to choose k positions (including first and last) from the available zeros, such that the maximum gap between consecutive selected positions is minimized. But how?

   When len(zeros) >=k, then we have to choose k positions, which implies that we have to select some of the available positions and skip others. For example, if there are 5 zeros and k=3, we have to select 3 (including first and last). So the problem is to select the positions in such a way that the maximum gap between consecutive selected positions is minimized.

   This is the classic problem of placing k elements on a line to minimize the maximum distance between adjacent elements. However, the elements must be chosen from the given list (the zeros).

   For example, given a sorted list of zeros, select k elements (including first and last) such that the maximum gap between consecutive elements is as small as possible.

   This is similar to the problem of finding the minimal possible maximum gap when you have to choose k points from a list.

   The standard approach for this is to binary search on the possible maximum gap and check if it's possible to select at least k points. But in this case, we need exactly k points, and we have to select exactly k points from the zeros list.

   Wait, but the zeros list is sorted. So the problem becomes selecting a subset of the zeros list of size m = min(k, len(zeros)), which includes first and last, and the maximum gap between consecutive elements is minimized.

   So, how to compute that?

   Let's consider the case when m <= len(zeros). Then, the problem is to select m elements from the zeros list (including first and last) such that the maximum gap is minimized. For example, when len(zeros) is 5 and m is 3, then we need to choose three positions, including first and last, and one in between, such that the maximum of the gaps between consecutive chosen positions is minimized.

   So how to model this? One approach is to find the best positions to select among the zeros list to minimize the maximum gap. For this, a dynamic programming approach is possible, but with len(zeros) up to 2e5, we need an O(n) or O(n log n) approach.

   Another approach is to realize that the minimal maximum gap is the minimal possible value such that there exists a way to select m positions with all consecutive gaps <= that value. So binary search on the possible gap.

   Let's try to model this.

   For a given candidate value D, can we select m positions (including first and last) such that all consecutive gaps are <= D?

   How to check this:

   The first position is zeros[0], the last is zeros[-1]. We need to select m-2 more positions from zeros[1...-2], such that between any two consecutive selected positions, the gap (next - prev) -1 <= D.

   Wait, the gap between two selected positions is (next_pos - prev_pos -1). We need this to be <= D.

   So, given that, how can we check if it's possible to select m positions (including first and last) such that all gaps are <= D?

   To check this, we can greedily select the earliest possible positions.

   Start with prev = zeros[0]. Then, for each subsequent position in zeros, if the gap (current - prev -1) > D, then we must include the current position. Otherwise, we can skip it. Wait, no. Wait, the idea is to select as few positions as possible (since m is the minimum between k and len(zeros)), but in this scenario, we need to select exactly m positions. Hmm, perhaps this approach is not straightforward.

   Alternatively, the problem can be transformed into the following: find the minimal D such that when we select the first and last positions, and select as many positions as possible from the zeros list in between, ensuring that the gaps between consecutive selected positions are <= D, the total number of selected positions is at least m.

   Wait, no. Because m is the maximum possible (since when m is len(zeros), we can't select more than that). So if we can select >=m positions with gaps <= D, then D is a possible candidate, but we need to select exactly m positions. So perhaps the binary search approach is not directly applicable.

   Alternatively, perhaps the problem can be viewed as finding the minimal D such that the maximum number of positions that can be selected (including first and last) with gaps <= D is at least m.

   If that is the case, then the minimal D is the answer.

   So binary search on D. For each D, compute the maximum number of positions that can be selected (including first and last) with all gaps <= D. If this number is >= m, then D is a candidate, and we can try smaller D. Else, need to try larger D.

   Then, the minimal such D is the answer.

   So how to compute the maximum number of positions that can be selected for a given D.

   Let's see. The first position is selected. Then, for each next position, we can select the earliest possible position that is more than D+1 away from the previous selected position.

   For example:

   prev = zeros[0]

   count =1

   for i in 1 to len(zeros)-1:

       if zeros[i] - prev -1 > D:

           count +=1

           prev = zeros[i]

   Also, we must include the last position. So after the loop, check if the last position is selected. If not, count +=1.

   Wait, no. Because the last position is zeros[-1], and in the loop, if we have prev as the last selected position, and zeros[i] is the last one, then when zeros[i] - prev -1 > D, we must select it. So after processing all positions, the last one will be included.

   So the algorithm would be:

   def possible(D):

       selected = [zeros[0]]

       for pos in zeros[1:]:

           if (pos - selected[-1] -1) > D:

               selected.append(pos)

       # selected includes first and last?

       # check if the last element is zeros[-1]

       if selected[-1] != zeros[-1]:

           selected.append(zeros[-1])

       return len(selected) <= m

   Wait, no. Because in this case, the code appends the last position only if it's not already included. But for example, if during the loop, the last position is added because the gap between the previous selected and last is > D, then the last is already in the selected list.

   So the code above ensures that the selected list includes the first and last positions (assuming that the loop iterates through all zeros including the last one).

   Wait, the loop is for pos in zeros[1:], which includes zeros[-1]. Let's see:

   For example, zeros = [0,2,3,5]. Then, during the loop:

   first selected is 0.

   pos=2: 2-0-1=1 <= D. So not added.

   pos=3: 3-0-1=2. If D is 2, then allowed. So not added.

   pos=5: 5-0-1=4. If D is 4, allowed. Not added.

   Then, after the loop, selected is [0]. So the code checks if the last element is 5. No. So it appends 5. Now, selected is [0,5]. So len(selected) is 2. If m is 3, then this is not enough.

   So the function would return whether len(selected) <= m. Wait, no. Because if we need to select m positions, but the code as written selects as few as possible (the minimal number of positions required to have all gaps <= D), then the function returns whether the required minimal positions is <= m. Because if the minimal number of positions is <=m, then we can add more positions (up to m) in between to split the gaps further, which would reduce the maximum gap. But the code checks whether the minimal number of positions is <=m. But wait, no. For example, if the minimal number of positions required is 2, and m is 3, then we can select 3 positions by adding one more. But the maximum gap may be <= D.

   Wait, the code computes the minimal number of positions required to have all gaps <= D. If this number is <=m, then it's possible to select m positions (since we can add extra positions, which splits gaps into smaller ones, thus ensuring that the gaps are still <=D). But how?

   For example, in the code above, the minimal number of positions is len(selected). For D, if len(selected) <= m, then it's possible to select more positions (up to m) such that all gaps are <=D. Because the more positions you add, the more the gaps are split, which can only decrease the maximum gap. So if the minimal required positions is <=m, then the answer is possible.

   So for example, if D is 3 and the minimal required positions is 2, and m is 3, then we can choose to add one more position, which would split a gap into two parts. Since the original gap was <=3, the split parts would be <=3.

   So in this case, the function possible(D) returns True when len(selected) <=m.

   Therefore, the binary search approach is:

   - Find the minimal D such that possible(D) is True.

   So the steps are:

   1. Collect zeros.

   2. Compute m = min(k, len(zeros)).

   3. If m == len(zeros): the answer is the maximum gap between consecutive zeros.

   4. Else: perform binary search on D between 0 and max_gap.

   5. For each D in binary search, compute the minimal number of positions required (using the greedy algorithm) and check if it's <=m.

   6. The minimal D where this is True is the answer.

   This approach is O(n) for each check, and the binary search is up to log(max_gap), which is O(1e9) for n up to 2e5, but each check is O(n), so overall O(n log(max_gap)) which is acceptable for n=2e5 and log(2e5) is around 20.

   Let's test this approach on the first example.

   First example:

   zeros = [0,2]. len(zeros) =2. k=3. m= min(3, 2)=2. So m is equal to len(zeros). So the answer is the maximum of the gaps. The gaps is 2-0-1 =1. So answer is1.

   Which matches the sample.

   Second example:

   zeros are [0,2,4,7]. len(zeros)=4. k=3. m=3.

   So m is less than len(zeros). So we need to find the minimal D such that the minimal required positions (greedily selected) is <=3.

   The initial gaps are 2-0-1=1, 4-2-1=1, 7-4-1=2. The maximum is2.

   Now, when m=3, the code will perform binary search to find the minimal D.

   Let's compute possible(D) for various D.

   For D=3:

   Greedy selection:

   prev =0.

   next pos is2. 2-0-1=1 <=3. So not added.

   next pos4. 4-0-1=3 <=3. So not added.

   next pos7.7-0-1=6>3. So add 7. Now selected is [0,7]. So len(selected)=2. Then, since we have m=3, we can add one more position. For example, between 0 and7, add 4. So the gaps are 4-0-1=3 (<=3), 7-4-1=2 (<=3). So possible. So for D=3, the minimal required positions is 2, which is <=3. So it's possible. But can we find a lower D?

   For D=2.

   Check if possible.

   selected starts with 0.

   next pos 2: 2-0-1=1 <=2. Not added.

   next pos4:4-0-1=3>2. So add 4. selected becomes [0,4].

   next pos7:7-4-1=2 <=2. Not added.

   After loop, selected is [0,4]. But last position is7. So code appends 7. selected becomes [0,4,7]. len(selected)=3. Which equals m=3. So possible. So D=2 is a candidate. But the sample's answer is3. So this suggests that my approach is incorrect.

   Wait, in the second sample, the correct answer is3. But according to this, D=2 is possible.

   What's wrong here?

   Wait, the sample's input is:

   8 3

   01010110 → which is '0','1','0','1','0','1','1','0'. So the zeros are at positions 0, 2,4,7 (assuming 0-based). So len(zeros)=4.

   So m=3. So need to select 3 positions. So the minimal required positions for D=2 is3. So according to the code, D=2 is possible, but the sample's answer is3. This suggests a mistake in the logic.

   What's wrong?

   Let's see. For D=2:

   The code's possible function will select positions 0,4,7. The gaps between them are:

   4-0-1=3 (break is3, which is >2). So this is invalid.

   Oh wait, no. The code's possible function counts the gaps between selected positions and checks if they are <=D. So the code's algorithm for possible(D) is:

   prev = zeros[0] (0).

   Next positions are 2,4,7.

   For pos=2: 2-0-1=1 <=2 → not added.

   pos=4:4-0-1=3>2 → added. So selected is [0,4].

   pos=7:7-4-1=2 <=2 → not added.

   After the loop, selected is [0,4]. Then, since the last position is7, which is not in selected, append it. So selected becomes [0,4,7]. The len is3.

   But the gaps between selected positions are 4-0-1=3 (break is3) and 7-4-1=2 (break is2). So the maximum break is3. Which is greater than D=2. So the code's possible function incorrectly returns True.

   So the code's logic is flawed.

   So why? Because the code's algorithm for possible(D) is not checking the maximum gap. It's just counting how many positions are selected, but the actual maximum gap may be larger than D. So the code is wrong.

   Oh! This is a critical mistake. The possible(D) function in the binary search approach is supposed to check whether there exists a selection of positions where all gaps are <=D. But the code is greedily selecting the minimal number of positions required to have all gaps <=D. However, in this code's approach, the selection is done by greedily adding a position whenever the current position's gap from the previous selected is larger than D. But in the example above, when D=2, the code selects 0,4,7. The gap between 0 and4 is3, which is larger than D=2. So the code's approach is wrong.

   So why is that happening?

   Because the code's logic for selecting positions is incorrect. The code's logic is:

   Start with the first position. For each subsequent position in zeros, if the gap between current pos and the last selected pos is >D, then select this current pos. Otherwise, skip.

   But this approach may not actually ensure that all gaps are <=D, because the code is only checking against the last selected position, not all previous.

   Wait, but after selecting a position, the next positions are checked against that last selected position. So between the last selected and the current position, if the gap is <=D, then it's allowed. But the previous selected positions may have a larger gap.

   Wait, no. Let's see:

   For example, in the code's selection for D=2 and zeros [0,2,4,7].

   selected starts with [0].

   pos=2: 2-0-1=1 <=2 → not added.

   pos=4:4-0-1=3 >2 → added. Now selected is [0,4].

   pos=7:7-4-1=2 <=2 → not added.

   After loop, append 7. selected is [0,4,7]. The gaps between consecutive selected positions are:

   4-0-1=3 (break is3).

   7-4-1=2 (break is2).

   The maximum is3, which is larger than D=2. But the code's possible function returns True because len(selected) <=m=3.

   So the code's logic is incorrect. It's counting the number of positions, but not ensuring that all gaps are <=D.

   So the binary search approach is not correct. The mistake is in the possible function.

   So what's the correct way to check whether there's a way to select at most m positions (including first and last) such that all gaps are <=D?

   Alternatively, the problem requires that when we select exactly m positions, the maximum gap is minimized. So the code's approach is to find the minimal D such that the minimal number of required positions is <=m. However, when the code selects positions in a greedy way, the gaps may exceed D. So the approach is wrong.

   This indicates that the binary search approach is not directly applicable, and a different approach is needed.

   So what's the correct way to model this problem?

   Let's think again. The problem requires selecting exactly m positions from the zeros list, including first and last, such that the maximum gap between consecutive selected positions is minimized.

   This is similar to the problem of placing m-2 additional points in the list to minimize the maximum gap.

   For example, given the zeros list, we have to select m positions from them. The first and last are already selected, so we need to choose m-2 positions from the remaining zeros[1:-1].

   The goal is to select these positions such that the maximum gap between consecutive selected positions is minimized.

   This is similar to the problem where you have to choose m-2 points from the list (excluding first and last) to split the initial gaps into smaller ones.

   So the approach is to find the m-1 largest gaps in the initial list and split each of them by inserting as many points as possible.

   But how?

   Another approach is to model the problem as follows:

   The initial gaps between consecutive zeros are the list gaps = [zeros[i+1] - zeros[i] -1 for i in 0..len(zeros)-2].

   The maximum of these gaps is the initial answer if m == len(zeros).

   When m < len(zeros), we need to choose (len(zeros) - m) gaps to split, each split can reduce the maximum.

   Wait, but how?

   For example, suppose we have gaps of 10, 5, 3. The maximum is 10. If m is 3, which is less than len(zeros) (say 4), then we need to choose (4-3) =1 gap to split. Splitting the largest gap (10) into two parts. The new maximum would be 5 (if split into 5 and5). So the maximum is5.

   So the strategy is to split the largest gaps first. Each split of a gap into s parts reduces that gap's contribution to the maximum.

   So for the case when m < len(zeros), the minimal maximum gap is the minimal possible maximum after splitting (len(zeros) - m) gaps.

   The way to compute this is to take the gaps list, sort them in descending order, and then split the first (len(zeros) - m) gaps. For each such gap, split it into s+1 parts, where s is the number of splits. The maximum after splitting is the maximum of the remaining gaps (after splitting the largest ones).

   For example, in the second sample:

   zeros are [0,2,4,7], gaps are 2-0-1=1, 4-2-1=1, 7-4-1=2. So gaps = [1,1,2]. The initial maximum is2.

   m=3. len(zeros)=4. len(zeros) -m =1. So split the largest gap (2) into s+1 parts, where s=1. So split into two parts, each of ceil(2/2) =1. So the maximum becomes 1.

   So the answer would be1. But the sample's answer is3. This is conflicting.

   So what's wrong here?

   Let's re-examine the second sample:

   input is 8 3.

   zeros are positions 0,2,4,7.

   m is min(3,4) =3. So we need to select 3 positions. The first and last are included. The third must be selected from positions 2 or4.

   If we select 0,4,7:

   gaps are 4-0-1=3, and 7-4-1=2. The maximum is3.

   If we select 0,2,7:

   gaps are 2-0-1=1, and7-2-1=4. Maximum is4.

   If we select 0,2,4,7: but m is3. So this is not allowed.

   So the best option is to select 0,4,7, giving a maximum of3.

   So according to the sample, the answer is3.

   But according to the approach of splitting the largest gaps, the largest gap is 2 (between4 and7). Splitting this once would split it into two parts, each of 2/(1+1) =1. So the maximum becomes1. But this is not possible.

   So this indicates that the approach is incorrect.

   The problem is that the gaps in the zeros list are not the same as the gaps between selected positions. For example, when you select positions 0,4,7 from the zeros list [0,2,4,7], the gaps between them are (4-0-1)=3 and (7-4-1)=2. So the maximum is3. But according to the initial gaps of the zeros list, the largest gap is2 (between4 and7). So the approach of splitting the largest gaps in the zeros list does not directly translate to the gaps between the selected positions.

   So the correct way to model the problem is that the gaps between selected positions are determined by the positions in the zeros list. So when you select a subset of positions from the zeros list, the gaps between consecutive selected positions are computed as (y -x -1), where x and y are consecutive selected positions.

   The goal is to select m positions from the zeros list (including first and last) such that the maximum of these (y-x-1) is minimized.

   So the problem is to choose m-2 positions from the zeros list (excluding first and last) such that the maximum gap between consecutive selected positions is minimized.

   This is a classical problem in dynamic programming, but with len(zeros) up to 2e5, a DP approach would be O(m*len(zeros)), which is O(2e5 * 2e5) = 4e10, which is impossible.

   So we need a different approach.

   Another approach is to binary search the answer and use a sliding window to check if it's possible to select m positions.

   For a given D, can we select m positions from the zeros list such that:

   - The first and last are included.

   - All consecutive selected positions have gaps <=D.

   How to check this?

   We can use a greedy approach:

   1. Start with the first position (zeros[0]).

   2. The next position should be the farthest possible position in zeros such that the gap between the current and next is <=D. We select that position.

   3. Repeat until we reach the last position.

   4. If the number of selected positions is <=m, then it's possible.

   For example, in the second sample with D=3:

   zeros are [0,2,4,7].

   selected = [0]. Look for the farthest next position where 7-0-1=6>3. So we need to find the last position in zeros that is <=0+3+1=4. So the next position can be 4. Now selected becomes [0,4]. Next, from4, look for positions after4 where the gap between4 and pos is <=3. The next positions is7:7-4-1=2 <=3. So selected is [0,4,7]. The number of positions is3, which is equal to m=3. So possible.

   So D=3 is possible.

   For D=2:

   selected = [0]. Look for next position in zeros such that pos-0-1 <=2 → pos-0 <=3 → pos <=3. The next positions are 2 and4. The farthest is2. But after selecting2, the next positions must be <=2+2+1=5. The next position after2 is4.4-2-1=1 <=2. So selected becomes [0,2,4]. Then, from4, looking for next positions <=4+2+1=7. 7 is in zeros. So selected becomes [0,2,4,7]. The count is4, which is >m=3. So we need to see if there's a way to select exactly3 positions.

   Hmm, this suggests that the greedy approach of selecting the farthest possible position each time gives the minimal number of positions required. But in this case, the minimal required positions is4, which is more than m=3. So D=2 is not possible. So possible(2) returns False.

   So the code's approach would be to binary search D, and for each D, compute the minimal number of positions required. If this minimal number is <=m, then it's possible. Else, not.

   But how does this work?

   For D=3, the minimal required positions is3 <=m=3 → possible.

   For D=2, the minimal required positions is4>3 → not possible.

   So the correct answer is3.

   So the code's approach was wrong because the way the minimal required positions were calculated was incorrect. The correct way is to select the farthest possible position at each step.

   So the correct algorithm for possible(D) is:

   def possible(D):

       count =1

       last = zeros[0]

       for i in range(1, len(zeros)):

           if zeros[i] - last -1 > D:

               count +=1

               last = zeros[i]

       # check if last is zeros[-1]

       if last != zeros[-1]:

           count +=1

       return count <=m

   Wait, no. Because if the last selected position is not the last zeros, then we have to add it, which increases the count. But in the code above, after the loop, the code checks if the last is zeros[-1]. If not, then count +=1. But in reality, if the last selected position is not the last zeros, then the code must add the last zeros. But the gap between the last selected and the last zeros is (zeros[-1] - last -1), which may be larger than D. So in this case, the code is adding the last position even if the gap is larger than D. So the code would allow a gap larger than D, which violates the condition.

   So the code is incorrect.

   So the correct approach is:

   The algorithm must select the first and last zeros, and the gaps between all consecutive selected positions must be <=D.

   So the algorithm should be:

   selected = [zeros[0]]

   for each position in zeros[1:-1]:

       if position - selected[-1] -1 > D:

           selected.append(position)

   selected.append(zeros[-1])

   Then, check if len(selected) <=m.

   But even this may not work, because when you append positions from zeros[1:-1], the last step is to append zeros[-1], but the gap between the last selected position and zeros[-1] may be larger than D.

   So the correct approach is:

   selected = [zeros[0]]

   for i in range(1, len(zeros)):

       if zeros[i] - selected[-1] -1 > D:

           selected.append(zeros[i])

   if selected[-1] != zeros[-1]:

       selected.append(zeros[-1])

   then, check if len(selected) <=m.

   But this will ensure that all gaps between consecutive selected positions are <=D. Because each time you add a position, the gap between it and the previous selected is checked.

   So for example, in the second sample with D=3:

   selected starts with 0.

   zeros[1] is2. 2-0-1=1 <=3 → not added.

   zeros[2] is4.4-0-1=3 <=3 → not added.

   zeros[3] is7.7-0-1=6>3 → added. selected becomes [0,7].

   Then, after loop, check if 7 is last. Yes. So selected is [0,7], count=2. Then, len(selected) is2 <=3 → possible. So the code returns True. But this would allow gaps of 6, which is larger than D=3. So the code's possible function is incorrect.

   So the code's logic is wrong. It's allowing gaps larger than D.

   So what is the correct way to model the possible function?

   The correct approach is to select positions such that all consecutive pairs have gaps <=D. So the algorithm must ensure that.

   The correct way to do this is to track the previous selected position, and for each subsequent position in zeros, if the gap between this position and the previous selected is >D, then select it. Otherwise, skip.

   But this approach can lead to gaps between selected positions that are larger than D, because the previous selected position is not the previous in the zeros list.

   For example, in the second sample, after selecting 0, the next possible position is7. But the gap between0 and7 is7-0-1=6>3 (if D=3). So this would not be allowed. So the code's approach is incorrect.

   So the problem is that the code's possible function is not ensuring that all gaps between consecutive selected positions are <=D. It's allowing the first selected to jump to a later position, resulting in a large gap.

   So the correct way to select positions is to greedily select the earliest possible positions such that the gap between consecutive selected positions is <=D.

   Here's the correct approach:

   Start with the first position. For the next position, find the farthest position in zeros that is <= (current position + D +1). Select that position. Repeat.

   This ensures that the gap between the current position and the next selected is <=D.

   So the algorithm is:

   def possible(D):

       count =1

       prev = zeros[0]

       i=1

       while i < len(zeros):

           # find the farthest position in zeros[i..] such that pos - prev -1 <=D

           # pos - prev -1 <=D → pos <= prev + D +1

           max_pos = prev + D +1

           # find the largest j where zeros[j] <= max_pos

           j = bisect.bisect_right(zeros, max_pos) -1

           if j <i:

               # no possible position → can't select next, so return False

               return False

           prev = zeros[j]

           count +=1

           i =j +1

       # after loop, check if we have covered the last position

       if prev != zeros[-1]:

           return False

       return count <=m

   This approach uses binary search to find the farthest position that can be selected next. This way, the gaps between consecutive selected positions are <=D.

   Let's test this for the second sample:

   zeros = [0,2,4,7]. D=3. m=3.

   prev =0.

   i=1.

   max_pos =0 +3 +1=4.

   j =bisect_right(zeros,4)-1 → zeros[3] is7>4. bisect_right returns3. j=2 (index of4).

   So select4. count=2. i=3.

   Now, prev=4. i=3.

   max_pos=4+3+1=8. j =bisect_right(zeros,8)-1=3.

   Select7. count=3. i=4.

   Now, i=4 == len(zeros), loop ends. prev is7 == zeros[-1]. So return count=3 <=3 → True.

   So possible(D=3) returns True.

   For D=2:

   max_pos=0+2+1=3. j is bisect_right([0,2,4,7],3)-1. zeros[j] is2.

   select2. count=2. i=2.

   next prev is2. max_pos=2+2+1=5. j =bisect_right([0,2,4,7],5)-1. zeros[3] is7>5. j=2 (4). 4<=5. select4. count=3. i=3.

   prev=4. max_pos=4+2+1=7. j=3. select7. count=4. i=4. check if prev is7. yes. return count=4 <=3 → False.

   So possible(D=2) is False.

   So the binary search will find that D=3 is the minimal possible.

   This matches the sample.

   So the correct approach is to use a binary search with a possible function that uses binary search to select the farthest possible position in each step.

   So now, the algorithm is:

   1. Collect zeros list.

   2. Compute m = min(k, len(zeros)).

   3. If m == len(zeros), return the maximum gap between consecutive zeros.

   4. Else, perform binary search on D from 0 to max_gap.

   5. For each D, check possible(D) as described.

   6. The minimal possible D is the answer.

   Now, the possible function uses binary search for each step, leading to O(log n) steps per possible check, and the binary search is O(log max_gap) steps. For n=2e5, the possible function would be O(log n) per step, and overall time is O(n log n log max_gap), which is acceptable for n=2e5.

   So, let's implement this.

   Now, the code:

   First, collect the zeros.

   Then compute the gaps between consecutive zeros.

   Then handle the case where m is the same as len(zeros), return the maximum gap.

   Else, binary search between 0 and max_gap.

   For the possible function, use binary search to find the farthest possible position.

   Now, in Python, we can use bisect.bisect_right from the bisect module.

   So, the code would look like:

   import bisect

   n, k = map(int, input().split())
   s = input().strip()

   zeros = [i for i, c in enumerate(s) if c == '0']

   m = min(k, len(zeros))

   if m == len(zeros):
       max_gap = 0
       for i in range(1, len(zeros)):
           gap = zeros[i] - zeros[i-1] -1
           if gap > max_gap:
               max_gap = gap
       print(max_gap)
       exit()

   # Binary search
   left = 0
   right = zeros[-1] - zeros[0] -1  # max possible gap

   answer = right

   while left <= right:
       mid = (left + right) // 2
       # Check if possible with mid
       count =1
       prev = zeros[0]
       i=1
       possible = True
       while i < len(zeros):
           max_pos = prev + mid +1
           j = bisect.bisect_right(zeros, max_pos) -1
           if j <i:
               possible = False
               break
           prev = zeros[j]
           count +=1
           i =j +1
       # Check if we reached the end
       if prev != zeros[-1]:
           possible = False
       if possible and count <=m:
           answer = mid
           right = mid -1
       else:
           left = mid +1

   print(answer)

   Let's test this code against the first sample.

   First sample input:

   3 3
   010

   zeros = [0,2]

   m = min(3, 2) =2.

   So, m == len(zeros). Compute maximum gap between consecutive zeros:

   2-0-1=1. So print1. Correct.

   Second sample:

   8 3
   01010110 → zeros are [0,2,4,7].

   m =3.

   Binary search between 0 and7-0-1=6.

   The binary search proceeds:

   left=0, right=6, mid=3.

   possible(3):

   count=1, prev=0.

   i=1.

   max_pos=0+3+1=4.

   j =bisect.bisect_right(zeros,4) -1 → zeros[3] is7>4. So bisect_right returns3. j=2 (since zeros[2]=4 <=4).

   prev=4, count=2. i=3.

   max_pos=4+3+1=8.

   j = bisect.bisect_right(zeros,8)-1 =3. zeros[3]=7 <=8.

   prev=7. count=3. i=4. loop ends.

   prev is7 == zeros[-1]. possible is True. count=3 <=3. So possible.

   answer=3. right=2.

   left=0, right=2. mid=1.

   possible(1):

   count=1, prev=0.

   i=1.

   max_pos=0+1+1=2.

   j =bisect_right(zeros,2)-1. zeros is [0,2,4,7]. bisect_right finds the first element >2. So index=2. j=1.

   prev=2. count=2. i=2.

   max_pos=2+1+1=4.

   j =bisect_right(zeros,4)-1 → index of4 is2. j=2.

   prev=4. count=3. i=3.

   max_pos=4+1+1=6.

   j = bisect_right(zeros,6)-1 → zeros[3] is7>6. j=2 (4 is <=6). So j=2.

   prev=4. i=3.

   prev=4. max_pos=4+1+1=6.

   j=2, but i=3. So j <i → possible=False. So returns False.

   So possible(1) is False. So left=2.

   mid= (2+2)/2=2.

   possible(2):

   count=1, prev=0.

   i=1.

   max_pos=0+2+1=3. bisect_right(zeros,3) is index=2 (since zeros[2]=4>3). j=1.

   prev=2. count=2. i=2.

   max_pos=2+2+1=5. bisect_right(zeros,5) is3 (zeros[3]=7>5). j=2 (zeros[2]=4 <=5). prev=4. count=3. i=3.

   max_pos=4+2+1=7. bisect_right(zeros,7) is4. j=3. prev=7. count=4. i=4. loop ends.

   count=4>3. So possible is False.

   So left=3. Now left>right. loop ends.

   answer=3. Correct.

   So this code should work.

   Edge Cases:

   - When k=2. Then, m=2. So the maximum gap is zeros[-1] - zeros[0] -1. Which is the gap between first and last.

   So the code will handle this case.

   So this should be correct.
</think>

```python
import bisect

n, k = map(int, input().split())
s = input().strip()

zeros = [i for i, c in enumerate(s) if c == '0']
m = min(k, len(zeros))

if m == len(zeros):
    max_gap = 0
    for i in range(1, len(zeros)):
        gap = zeros[i] - zeros[i-1] - 1
        if gap > max_gap:
            max_gap = gap
    print(max_gap)
else:
    left, right = 0, zeros[-1] - zeros[0] - 1
    answer = right

    while left <= right:
        mid = (left + right) // 2
        count = 1
        prev = zeros[0]
        i = 1
        possible = True

        while i < len(zeros):
            max_pos = prev + mid + 1
            j = bisect.bisect_right(zeros, max_pos) - 1
            if j < i:
                possible = False
                break
            prev = zeros[j]
            count += 1
            i = j + 1

        if possible and prev == zeros[-1] and count <= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
```