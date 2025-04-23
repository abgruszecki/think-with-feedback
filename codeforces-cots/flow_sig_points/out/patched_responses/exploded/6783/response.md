<think>
Okay, let's see. The problem is to find the best and worst possible ranks Vasya can have, given that his total is at least x. The sum of his first and second tour points must be >=x, and we need to find the best (smallest) and worst (largest) possible positions he could get, considering all possible valid pairs (a_i + b_j >=x) and the way the competition's total scores are sorted.

Hmm, first, let's understand how the rankings work. The total score for each participant is the sum of their first and second tour points. The list is sorted in non-increasing order of these sums. But when two people have the same sum, their order can be arbitrary. So for the best possible rank, we need to maximize the number of people with a sum less than Vasya's sum. For the worst possible rank, we need to minimize the number of people with a sum strictly greater than Vasya's sum.

Wait, no. Wait. Let's think again. The best possible position occurs when Vasya's sum is as high as possible. Wait, but he can choose any a_i and b_j such that a_i + b_j >=x. So to get the best possible position, we need to select the pair (a_i, b_j) that gives the maximum possible sum. Then, in the best case, how many people have a sum higher than or equal to Vasya's sum? Well, since the sum is maximum possible, the best rank is 1. But maybe that's not always the case. For example, if someone else also has the same maximum sum, then Vasya could be first or second, but the best possible is 1.

Wait, but the problem says that the best possible rank is when Vasya's sum is as high as possible, and as many people as possible have lower sums. So for the best rank, we need the maximum possible sum for Vasya, then the number of people with sum strictly greater than that would be zero. But if others have the same sum, then the best possible rank is 1, but the worst possible could be higher.

Wait, no. Let's see. Let's say we choose Vasya's sum as S. Then, the best possible rank is 1 plus the number of people who have sum > S. But since the jury can arrange the same sums in any order, so if there are k people with sum > S, then Vasya's best possible rank is k+1. Because all those k people would be placed before him. But if there are others with sum equal to S, then in the best case, he can be placed first among those, so his rank is k+1. For the worst case, if there are m people with sum >= S, then his worst possible rank is m. Because all of them could be placed before him.

Wait, let's think again:

For a given S (Vasya's sum), the best possible rank is 1 + the number of people with sum > S. Because all those people are ranked higher than him, but any with sum equal can be placed after him, so he can be first in the equal group. So the best possible rank for S is (number of people with sum > S) + 1.

The worst possible rank for S is the total number of people with sum >= S. Because all those people could be ranked before him, so his rank is that count.

So, for each possible S (a_i + b_j >=x), we need to compute the possible best and worst ranks, and then find the overall minimum possible best rank and maximum possible worst rank.

So the approach is:

1. Find all possible pairs (a_i, b_j) where a_i + b_j >=x. For each such pair, S = a_i + b_j.

2. For each S, compute:

   best_rank = (number of people with sum > S) + 1

   worst_rank = (number of people with sum >= S)

   Then, among all possible S, find the minimum best_rank and the maximum worst_rank.

Wait, but how do we get the counts for all possible sums?

First, we need to compute all possible sums for the participants. Because each participant has their own a and b. Wait, no. The input gives two lists, a and b, but each participant is a pair of a_i and b_j? Or is each a_i and b_i part of the same participant?

Wait, the problem statement says: "The second line contains n space-separated integers: a1, a2, ..., an (0 ≤ ai ≤ 1e5) — the participants' points in the first tour. The third line contains n space-separated integers: b1, b2, ..., bn (0 ≤ bi ≤ 1e5) — the participants' points in the second tour. The participants' points are given in arbitrary order. It is guaranteed that Vasya was present in the Olympiad — there are two integers i, j (1 ≤ i, j ≤n) such that ai + bj >=x."

Wait, this is a bit ambiguous. Are the a's and b's for each participant given as a_i and b_i (i.e., participant 1 has a1 and b1, participant 2 has a2 and b2, etc.), or are the a's and b's given in arbitrary order, and each a_i is paired with some b_j to form a participant?

Wait, the input is structured as follows: The second line is a list of a's, third line a list of b's, but in arbitrary order. So each participant is a pair of a_i and b_j, but i and j can be different. Wait, no. Wait, the problem says "it is guaranteed that Vasya was present in the Olympiad — there are two integers i,j (1 ≤i,j ≤n) such that ai + bj ≥x." So that suggests that Vasya's a is from the first list, and b from the second list. So each participant is a combination of some a_i and b_j. Wait, no, that can't be. Because then the number of participants would be n², but the problem says the first line has n as the number of participants.

Wait, this is confusing. Let's read the problem statement again.

The problem statement says: "the number of Olympiad participants is n, x. The second line is a1...an, the third line is b1...bn. The problem says that the participants' points are given in arbitrary order. It is guaranteed that Vasya was present in the Olympiad — there are two integers i,j such that ai + bj >=x."

Wait, perhaps each participant has a first tour score and a second tour score. The a and b lists are the first and second tour scores of the n participants, but in arbitrary order. So participant 1 has a1 and b1, but the order of the a and b lists is not the same as the participants. Wait, no. That's possible. Wait, but the problem says "the teacher has the results of the first and the second tour of the Olympiad but the problem is, the results have only points, no names. The teacher has to know Vasya's chances."

Ah, so the teacher has for each tour, the list of all participants' points, but they are not linked. So the first tour's list is a1 to an (scores), and the second tour's list is b1 to bn (scores), but they are in arbitrary order. So the actual participants are pairs of (a_i, b_j) where i and j are from 1 to n, but the teacher doesn't know which a is paired with which b. But since Vasya is a participant, there exists at least one pair (i,j) such that a_i + b_j >=x. So Vasya's actual score is a_i + b_j for some i and j. So the problem is to find all possible possible pairs (i,j) (since the actual pairing is unknown) where a_i + b_j >=x, and for each such possible pair, compute the best and worst possible rank that Vasya could have, then select the best possible (minimum) best rank and the worst possible (maximum) worst rank.

Wait, but the problem says that each participant is present in both tours. So for each participant, their first tour and second tour scores are part of the lists. But since the lists are not linked (the a's and b's are in arbitrary order), the teacher doesn't know which a_i corresponds to which b_j. So the actual possible pairings are all possible permutations of the a's and b's. But the problem states that in reality, the actual participants are the pairs (a_i, b_i) for each i. Because how else can there be n participants? Otherwise, if the participants are all possible pairs of a and b, then there would be n² participants, which contradicts the first line's n. So this must be a misunderstanding.

Wait, the problem statement says: "the problem is, the results have only points, no names. The teacher has to know Vasya's chances." So the teacher has two lists: the first tour's scores (a1..an) and the second tour's scores (b1..bn), but these are just the lists of all participants' scores for each tour, but the teacher doesn't know which a corresponds to which b. So the actual possible combinations of a and b for the participants are all possible permutations of the a and b lists. But each participant must have exactly one a and one b. So the teacher has to consider all possible ways to pair the a's and b's into n pairs (each a and b used exactly once). Then, for each such possible pairing, there must be one pair (a_i, b_j) that is Vasya's (since he is a participant). So the problem is to find, among all possible permutations of the b's (since pairing a_i with b_j as a permutation), which permutations allow for a pair (a_i, b_j) that is >=x, and then compute the possible ranks for each such pair, and then find the best and worst possible ranks.

But this seems computationally infeasible, given that n can be up to 1e5. So maybe that's not the case.

Alternatively, perhaps each participant has an a_i and a b_i, but the lists are given in arbitrary order. So the a list is shuffled, the b list is shuffled, but the actual participants are the pairs (a_i, b_i) after being sorted. But then the problem's input is given as two shuffled lists. So the teacher doesn't know the correct pairing.

But then, how to model Vasya's possible scores? Because Vasya's actual a_i and b_j are part of the lists. So in this scenario, Vasya is one of the participants, and his a and b are in the lists. But since the teacher doesn't know the pairing, he has to consider all possible valid pairings where there exists a pair (a_i, b_j) that is >=x (as per the problem's input guarantee).

But the problem's note in the first example says that all participants have 2 points each. So in that case, the best possible rank is 1 and the worst is 5 (since all have the same sum). So in that scenario, the pairing would be such that each a_i is 1 and each b_j is 1. Then, the sum for each participant is 2. So the pairing is such that each a_i is paired with a b_j, but all sums are 2.

So, the problem is: the actual participants' sums are the sums of a_i and b_j, where each a and b is part of exactly one pair. So each a is paired with exactly one b, and each b is paired with exactly one a. So the pairing is a permutation. So the possible sums for the participants are a_1 + b_{p(1)}, a_2 + b_{p(2)}, ..., a_n + b_{p(n)}, where p is a permutation of 1..n.

But then, the problem requires us to find the best and worst possible rank Vasya can have, considering all possible permutations p where there exists at least one i such that a_i + b_{p(i)} >=x (as per the input guarantee). But how to model this?

Alternatively, perhaps the problem considers that Vasya is one of the participants, and his a and b are a_i and b_i (for some i). But the teacher doesn't know which i. So the possible Vasya's sum is a_i + b_i for some i, but the input is such that at least one of those sums is >=x. But that's not what the problem says. The problem's input says that there exists i and j such that a_i + b_j >=x. So this suggests that the pairing is between a_i and b_j where i and j can be different.

But that's conflicting with the structure of the problem. Because then, the actual participants would have a sum that's a_i + b_j for some i and j, but the problem says there are n participants, which would require that each a and each b is used exactly once, leading to permutation-based pairings.

Alternatively, perhaps each participant is represented by a unique a and a unique b, but the pairing is arbitrary, and the problem is to find the best and worst possible ranks for Vasya, assuming that in the actual correct pairing (which is a permutation) there exists at least one pair (a_i, b_j) in the permutation that is >=x, and that this is Vasya's pair.

But this seems very complicated. So perhaps the key insight is that the problem's actual setup is that each participant has a first tour score and a second tour score, but the teacher's data is the two lists a and b (each of size n) in arbitrary order. So, the actual participants are the pairs (a_i, b_j) where i and j are indices in 1..n, but each a and each b is used exactly once, so the pairing is a permutation.

But the problem requires us to consider all possible permutations of the b list, and for each permutation, consider that there exists at least one i where a_i + b_{p(i)} >=x. Then, for each such permutation, find Vasya's possible sum (which would be a_i + b_{p(i)} for some i), and compute his possible rank. Then, among all possible permutations and all possible positions of Vasya in the permutation (but given that there is at least one pair in the permutation with sum >=x), find the best and worst possible ranks.

But this seems impossible to compute directly for large n, so there must be a smarter way.

Alternatively, perhaps the problem is not about permutations but that Vasya can choose any a_i and b_j (not necessarily in a permutation) as his own scores. Then, the other participants' scores are the remaining a's and b's. But this would lead to n² possible participants, which is impossible given that the first line says there are n participants.

So perhaps the correct way to model this is: each participant has an a_i and a b_i. The lists a and b are given in arbitrary order. So the actual pairs are (a_1, b_1), (a_2, b_2), ..., (a_n, b_n). But the lists are shuffled, so the teacher can't know which a_i is paired with which b_j. However, Vasya's actual sum is a_i + b_j for some i and j (not necessarily the same index). Wait, but that's not possible because each participant's sum is a_i + b_i. So perhaps the problem is that the a's and b's are shuffled, so the teacher doesn't know which a_i is paired with which b_j, but the actual participants are the pairs (a_1, b_1), etc., but in the teacher's view, the a and b lists are in arbitrary order. So the teacher needs to consider all possible permutations of the b list paired with the a list. Then, in each permutation, the sum for each participant is a_i + b_{p(i)}, where p is a permutation. Then, in each such permutation, find the sum for Vasya (which would be a_i + b_{p(i)} for some i) that is >=x. Then, find the best and worst possible ranks across all permutations.

But even this approach seems computationally infeasible, given that n can be up to 1e5. So there's definitely a smarter approach.

But let's re-examine the problem statement's sample inputs.

In the first sample:

Input:

5 2

1 1 1 1 1

1 1 1 1 1

Output: 1 5

Explanation: All participants have sum 2. So in any permutation pairing, the sum is 2 for all. So the best and worst possible ranks are 1 and 5.

In the second sample:

Input:

6 7

4 3 5 6 4 4

8 6 0 4 3 4

The best case is when the sum is 4+8=12. Then, how many participants have sum higher than 12? None, so best rank is 1.

The worst case is when the sum is 4+3=7. Then, how many participants have sum >=7? Let's see:

The other participants' sums would be 4+8=12, 4+6=10, 6+4=10, 5+0=5, 3+3=6. So in this case, Vasya's sum is 7, and the other sums are 12, 10,10,5,6. So the sum >=7 are 12,10,10,7. So there are 4 sums >=7. So worst rank is 4. But the sample output is 1 5. Wait, perhaps I'm misunderstanding the sample.

Wait the sample's output is 1 5. Hmm, maybe I'm not getting the correct pairing.

Alternatively, perhaps the way to model this is that Vasya can choose any a_i and b_j (regardless of permutation), and the other participants' sums are the remaining a's and b's, but again, this leads to a problem with n² participants, which contradicts the first line's n.

This suggests that the initial approach is incorrect, and perhaps there's a different way to model the problem.

Wait, perhaps the problem is as follows: the actual participants' sums are a_i + b_i for each i. However, the teacher has the two lists a and b, but they are given in arbitrary order. So for example, the teacher's list a could be [a_1, a_3, a_2, ...], and the list b could be [b_3, b_1, b_2, ...], but the actual pairs are a_i and b_i of the original lists. But since the lists are in arbitrary order, the teacher can't know which a's and b's are paired. However, the problem states that Vasya is one of the participants, which implies that in the actual correct pairing (the original order), his sum is a_i + b_i >=x for some i. But the problem's input may not have that, since the input's a and b lists are in arbitrary order. Wait, but the problem says that the input is such that there exists i and j (not necessarily same) such that a_i + b_j >=x. So Vasya's sum could be a_i + b_j, but that's possible only if the teacher considers that the actual pairing is a permutation of the b list. So the teacher is considering all possible pairings (permutations) of the a and b lists. For each possible permutation (pairing of a's and b's), there will be n sums, and in each permutation, there must be at least one sum >=x (as per the input's guarantee). For each such permutation, Vasya is one of the participants in that permutation, and his sum is a_i + b_p(i) (where p is the permutation). The problem is to find the best and worst possible ranks Vasya can have across all possible permutations p and across all possible positions i in the permutation (as long as a_i + b_p(i) >=x).

But how to model this?

The key insight here is that the best possible rank for Vasya is determined by the maximum possible sum he can have, given that a_i + b_j >=x. Because the higher his sum, the better his rank. Similarly, the worst possible rank is determined by the minimum possible sum he can have, given a_i + b_j >=x. Because the lower his sum, the worse his rank.

Wait, but this is only true if the other participants' sums are as high as possible. Because in the worst case, for Vasya's sum S, other participants can have sums higher than S. So for the best possible rank, we need to choose the maximum possible sum S, and the best possible rank is 1 plus the number of participants (from the original lists) that can have sum greater than S. Wait, but how to compute that?

Alternatively, perhaps the best possible rank is when we select a_i and b_j such that their sum is as large as possible, and then the number of participants (from the original a and b lists) who have a sum greater than or equal to this S is minimized.

Wait, no. Let's think:

For the best possible rank:

We need to choose a pair (a_i, b_j) such that a_i + b_j >=x. Then, we can assign this sum to Vasya. The other participants are the remaining a's and b's, but how? Because this approach would leave (n-1) a's and (n-1) b's. So the other participants' sums would be (a_k, b_l) where k !=i and l !=j. But that's not possible, since each participant must have exactly one a and one b.

So this line of thinking is incorrect. Therefore, the correct model must involve permutations.

So the correct model is:

Each participant is formed by a unique a_i and a unique b_j. All a's and b's are used exactly once. So the pairing is a permutation p, where each a_i is paired with b_{p(i)}. The sum for each participant is a_i + b_{p(i)}.

Vasya is one of the participants in this permutation. For the problem, we need to find the best and worst possible ranks that Vasya can have in the sum list (sorted in non-increasing order) across all possible permutations p where there exists at least one i such that a_i + b_{p(i)} >=x. For each such permutation, in the sum list, Vasya's rank is determined by his sum S. The best possible rank is the minimum possible rank across all possible permutations and all possible i where a_i + b_{p(i)} >=x. The worst possible rank is the maximum possible rank across all permutations and i where a_i + b_{p(i)} >=x.

But with n up to 1e5, considering all permutations is impossible. So there must be a mathematical way to compute the best and worst possible ranks without enumerating permutations.

Let's think about the best possible rank. To get the best possible rank, we need to maximize Vasya's sum. So the maximum possible sum S that can be formed by a_i + b_j >=x. Once S is determined, the best possible rank is 1 plus the number of participants (from all possible pairs) that have sum > S. But wait, but in the permutation model, the other participants are formed by other pairs, but their sums are a_k + b_{p(k)}. So in the best case scenario, for Vasya's sum S (maximum possible), how many other pairs in the permutation have sums > S?

But since the permutation can be any possible pairing, to minimize the rank, we want to arrange the permutation such that the other pairs have sums as small as possible. Wait, but how?

Alternatively, perhaps the best possible rank for Vasya is determined by the maximum possible sum S (a_i + b_j) >=x. Then, the number of pairs in the entire list of possible pairs (not the permutation) that have sum > S is zero. Because S is the maximum possible sum. So the best possible rank is 1.

But in the first sample, when all sums are equal to 2, the maximum sum is 2, and there are no pairs with sum >2. So the best possible rank is 1.

Yes, that matches the sample output.

So the best possible rank is determined by the maximum possible S that Vasya can have (the maximum a_i + b_j >=x). Then, the best possible rank is the number of pairs (a_k, b_l) where a_k + b_l > S plus 1. But since S is the maximum possible, there are no pairs with sum > S, so the best rank is 1.

But how to compute the maximum possible S. The maximum possible S is the maximum of all a_i + b_j where a_i + b_j >=x. So to find the best possible rank, we need to find the maximum possible S = a_i + b_j >=x, then the best rank is 1 + the number of pairs (k,l) where a_k + b_l > S. But since S is the maximum, this count is zero, so best rank is 1.

But wait, in the second sample input:

The a list is [4,3,5,6,4,4], the b list is [8,6,0,4,3,4].

The possible pairs a_i + b_j >=7.

The maximum sum would be 4 +8=12 (a_i is 4, b_j is8). Let's see. Then, the number of pairs (k,l) where a_k +b_l >12 is zero. So the best rank is 1.

Which matches the sample output.

So for the best possible rank, the approach is:

Find the maximum possible S where a_i + b_j >=x. Then, the best possible rank is 1 + the number of pairs (k,l) with a_k +b_l > S.

But since S is the maximum possible, this number is zero. So best rank is 1.

So that's easy.

Now for the worst possible rank. Here, we need to find the minimum possible S (but >=x) such that when Vasya's sum is S, the number of participants in the permutation that have sum >=S is maximized.

But how?

Wait, the worst possible rank for Vasya is when his sum is as small as possible (but >=x), and the other participants in the permutation have as many sums >=S as possible.

But the other participants' sums are determined by the permutation. So the worst case is when Vasya's sum is the smallest possible S >=x, and there are as many other participants' sums >=S as possible.

But how to compute that?

Let's think. To maximize the worst possible rank, we need to find the minimum possible S (>=x), and then compute how many pairs (a_i, b_j) can have sum >=S. Because in the worst case, all those pairs can be part of the permutation, and thus Vasya's rank is equal to the number of such pairs.

But since the permutation has exactly n pairs, but each a and b is used exactly once, the number of pairs with sum >=S in the permutation can vary depending on how the permutation is arranged.

Wait, but how many pairs (a_i, b_j) are there in the entire universe where a_i +b_j >=S, and how does that affect the permutation?

Alternatively, perhaps the worst possible rank is determined by the minimal possible S (>=x) that Vasya can have, and then the number of pairs (a_i, b_j) that are >=S. But the permutation can include as many of those pairs as possible.

But since each a and b can be used exactly once, the maximum number of pairs in the permutation with sum >=S is the maximum possible for that S. So the worst possible rank would be the maximum possible number of pairs >=S in any permutation.

But how to find this maximum possible count for a given S.

Alternatively, perhaps for the worst possible rank, the approach is:

Choose the minimal possible S (>=x) that Vasya can have. Then, the worst possible rank is the number of pairs (a_i, b_j) in the entire list where a_i + b_j >= S. Because in the best case for the worst rank, the permutation includes as many pairs as possible with sum >=S. But this is not possible because each a and b can be used once.

But how to model this?

Alternatively, the maximum possible number of pairs in the permutation with sum >=S is the maximum number of such pairs that can be formed given that each a and b is used exactly once.

But this is equivalent to finding a bipartite graph where the left nodes are the a's, the right nodes are the b's, and edges connect a_i and b_j if a_i +b_j >=S. Then, finding the maximum matching in this graph, which would give the maximum number of pairs in the permutation that have sum >=S.

But the problem is that for each S, we need to find the maximum matching size, and then the worst possible rank for S would be that maximum matching size. But since S is the minimal possible (>=x), we need to find the minimal S where S >=x, and the maximum matching size for that S is as large as possible.

But this approach is computationally expensive for large n. So perhaps we need a different way.

But maybe there's another way. Let's think: the worst possible rank for Vasya is the maximum number of pairs (i,j) such that a_i +b_j >= S, where S is the minimal possible sum Vasya can have (>=x). And then, the permutation is arranged to include as many of these pairs as possible, so Vasya's rank is the number of pairs >=S in the permutation.

But how to compute this.

Alternatively, here's a different approach:

For the worst possible rank, we need to choose a pair (a_i, b_j) such that a_i + b_j >=x, and S =a_i +b_j is as small as possible. Then, in the permutation, we want to include as many pairs (a_k, b_l) that have a_k +b_l >=S as possible. The number of such pairs is the maximum possible number of pairs that can be formed in a permutation where each a and b is used exactly once, and each pair has sum >=S. Then, the worst possible rank is that count.

But again, how to compute this.

Alternatively, the worst possible rank is determined by the minimal S (>=x) such that there exists a pair (i,j) with a_i +b_j = S, and the maximum possible number of pairs (k,l) with a_k +b_l >= S is as large as possible. The worst possible rank is that maximum possible number.

But how to compute the maximum possible number of pairs (k,l) in a permutation where each a and b is used exactly once, and their sum >=S.

This seems like a bipartite matching problem. But for large n, this is not feasible.

But perhaps there's a greedy way to compute this. For example, the maximum number of pairs in the permutation with sum >=S can be found by the following:

Sort the a's in ascending order and the b's in descending order. Then pair the smallest a's with largest possible b's to get the maximum number of sums >=S.

Wait, this is a standard approach in matching problems. For example, to maximize the number of pairs where a_i +b_j >=S, you can sort a in ascending order and b in descending order. Then, for each i, check if a_i +b_i >=S. If yes, increment the count. The maximum possible count is the largest k where a_i +b_{n- i +1} >=S for i=0 to k-1.

Alternatively, to maximize the number of pairs with sum >=S, you can sort the a's in ascending order and the b's in descending order, then pair the smallest a with the largest b, next smallest a with next largest b, etc., and count how many pairs meet the sum >=S. This is the standard approach for this kind of problem.

Yes, that's right. For example, in the problem where you need to form pairs from two arrays such that as many pairs as possible meet a certain condition (like sum >=S), the optimal way is to sort one array in ascending order and the other in descending order, then pair the elements in order. This gives the maximum possible count.

So, given that, the approach for the worst possible rank is:

1. Find all possible S where S =a_i +b_j >=x.

2. For each S, compute the maximum number of pairs possible in a permutation where sum >=S. This can be done by sorting a in ascending order, b in descending order, then pair a[0] with b[0], a[1] with b[1], etc., and count how many pairs have sum >=S.

3. For the worst possible rank, we need to find the minimal S (>=x) such that the maximum number of pairs (as computed in step 2) is maximized. The worst rank would be that maximum count.

Wait, no. Because we are trying to find the worst possible rank for Vasya. So we need to choose the minimal possible S (>=x) and compute the maximum possible number of pairs >=S. The worst possible rank is then that number.

But why minimal S? Because the lower S is, the more pairs can potentially have sum >=S. So for the worst rank, we want the minimal S (>=x) that allows the maximum number of pairs >=S. However, we need to choose S as the minimal possible among all possible (a_i +b_j >=x), and then compute the maximum possible pairs >=S.

So the steps for the worst rank are:

- Find the minimal possible S such that S =a_i +b_j >=x.

- For that S, compute the maximum possible number of pairs (k,l) in a permutation that have sum >=S. This is done by sorting a in ascending order and b in descending order, then pairing each a[i] with b[i], and counting how many pairs >=S.

- The worst possible rank is the maximum count.

But wait, what if there are multiple S's (>=x) and we need to choose the one that allows for the maximum count of pairs >=S? For example, a higher S may allow a higher count (if possible), but that's unlikely. Because higher S would result in fewer pairs >=S. So the minimal S would allow for the maximum possible pairs >=S.

Thus, to find the worst possible rank, we need to choose the minimal S (>=x), and compute the maximum possible pairs >=S.

But how to compute the minimal possible S that is >=x, and is the sum of some a_i +b_j.

So first, find all possible pairs (a_i, b_j) where a_i +b_j >=x, and collect all such S values. Then, find the minimal S among them.

Once we have that S, we can compute the maximum possible pairs >=S using the sorted a and b approach.

But for large n, computing all possible S values would be O(n²), which is impossible for n=1e5.

So we need a way to find the minimal possible S that is >=x and is achievable by some pair (a_i, b_j).

But how to find the minimal S >=x.

The minimal S is the minimal a_i +b_j >=x.

So how to find the minimal a_i +b_j that is >=x, given the arrays a and b.

This is similar to finding the minimal sum >=x among all possible pairs.

To find this efficiently, we can:

1. Sort one array, say, a in ascending order.

2. Sort the other array, b in ascending order.

3. Then, for each element a_i in a, find the smallest b_j such that a_i +b_j >=x. The minimal sum for a_i is a_i +b_j. We can find this using binary search.

But since the arrays are sorted, this approach can be O(n log n).

Let's see:

Sort array a in ascending order.

Sort array b in ascending order.

For each a_i in a:

We need to find the smallest b_j in b such that a_i +b_j >=x. The minimal possible sum for this a_i is a_i +b_j.

We can find the minimal j using binary search (since b is sorted). For example, the first j where b_j >=x -a_i. Then, the minimal sum for this a_i is a_i +b[j]. If there is no such j, then this a_i can't form a pair with any b_j >=x -a_i.

We track the minimal sum across all possible a_i and their corresponding b_j.

But how to handle this for all a_i.

Let me think. We can do the following:

Sort a in ascending order.

Sort b in ascending order.

Initialize the minimal S to a very large value.

For each a_i in a:

   target = x -a_i.

   find the smallest index j in b where b[j] >= target.

   if j exists (i.e., there is a b[j] >= target):

       sum_candidate = a_i +b[j]

       if sum_candidate < current minimal S:

           update minimal S to sum_candidate.

So after processing all a_i, the minimal S is the minimal possible sum >=x.

But this approach requires O(n log n) time (sorting plus binary search for each a_i).

Yes, this is feasible for n=1e5.

Once we have the minimal S, we then need to compute the maximum number of pairs in a permutation where each pair's sum is >=S.

To compute this maximum count, we can sort a in ascending order and b in descending order, then pair each a[i] with b[i], and count how many pairs have sum >=S.

Wait, no. Wait, to maximize the number of pairs with sum >=S, the standard approach is to sort a in ascending order and b in descending order. Then, for each i, pair a[i] with b[i], and count how many pairs have sum >=S.

Wait, no. Let me think. If we want to maximize the number of pairs >=S, we can sort a in ascending order and b in descending order, then pair them. Alternatively, sorting a and b in opposite orders and then pairing.

Yes, that's the standard approach. For example, in the problem of maximum pairs with sum >= S.

So, the steps to compute the maximum possible count are:

Sort array a in ascending order.

Sort array b in descending order.

For each i from 0 to n-1:

   if a[i] + b[i] >= S: count +=1.

The total count is the maximum possible number of pairs in a permutation where the sum is >=S.

So, this is O(n log n) time.

So the overall approach is:

Compute the minimal possible S >=x (using the sorted a and b with binary search).

Then, compute the maximum possible pairs in a permutation (by sorting a ascending, b descending) where the sum >=S. The worst possible rank is that count.

But wait, the worst possible rank is the number of pairs >=S, which includes Vasya's own pair. So if the count is k, then the worst possible rank is k.

But why is that? Because in the permutation that allows the maximum number of pairs >=S, Vasya's pair is one of them. So the worst possible rank is the maximum possible count.

So putting it all together:

Best rank:

Find the maximum possible sum S where a_i +b_j >=x. Then best rank is 1 + the number of pairs (k,l) with a_k +b_l >S. Since S is the maximum, this count is zero. So best rank is 1.

Worst rank:

Find the minimal possible S >=x. Then compute the maximum possible number of pairs (k,l) in a permutation where sum >=S. This count is done by sorting a ascending, b descending, and pairing each a[i] with b[i]. Then, the worst rank is that count.

So the steps are:

For best rank:

Compute maximum S = max(a_i + b_j for all pairs where a_i + b_j >=x). Then best rank is 1.

Wait, but how to compute the maximum S?

The maximum S is simply the maximum a_i + maximum b_j, provided that their sum is >=x. Or perhaps not. Because the maximum a_i is, say, a_max, and maximum b_j is b_max. So their sum is a_max +b_max, which is the maximum possible sum.

So for best rank, the maximum S is a_max +b_max. But we need to ensure that this sum is >=x. If not, then we need to find the next possible maximum sum >=x.

But the problem's input guarantees that there exists at least one pair with sum >=x. So the maximum sum will definitely be >=x.

So the best rank is always 1.

Wait, but wait. What if the maximum sum is S, and there are multiple pairs that have sum S. Then, when we choose S as the sum for Vasya, there are other pairs with the same sum. But the best rank is 1, because all those pairs can be ordered before or after him. But since the jury can arrange them in any order, the best possible rank is 1.

So the best possible rank is always 1, because we can choose the maximum possible sum, and then arrange the others to have sums <=S. But wait, how? Because the other pairs in the permutation are part of the same permutation.

Wait, but for the best rank, we can arrange the permutation in such a way that Vasya's pair (the maximum S) is first. The other pairs can have any sums. But the maximum possible sum is S, so in any permutation, the best rank for Vasya is 1.

So the best possible rank is 1.

Wait, but that's not the case in the second sample input. The sample input's output is 1, but the maximum sum is 4+8=12. Then, all other pairs in the permutation can have sums up to, but not exceeding 12. So the best possible rank is 1.

Yes, this matches the sample.

So the best possible rank is always 1.

Wait, but in the first sample, all pairs sum to 2, which is the maximum possible. So the best rank is 1.

Yes.

So the best possible rank is always 1.

Wait, this seems to be the case. Because the maximum possible sum S is >=x, and any other pair in the permutation can have sum <= S. So when we choose S as Vasya's sum, the best possible rank is 1, because no other pair in the permutation can have sum higher than S.

But wait, how is this possible? Because in the permutation, each pair is a unique a and b. So for example, the maximum sum may be S =a_max +b_max, and in the permutation, we pair a_max with b_max, and other pairs can have sums <=S. So the best possible rank is 1.

So the best rank is always 1. That's a crucial insight.

So the best rank is 1.

Now, the worst possible rank is the maximum possible rank Vasya can have, which depends on the minimal possible S (>=x) and the maximum possible number of pairs >=S in a permutation.

So the steps are:

1. Find the minimal possible S >=x (the minimal sum of any pair a_i +b_j >=x).

2. Sort a in ascending order and b in descending order.

3. Pair a[i] with b[i] for all i, count how many pairs have sum >=S. This count is the maximum possible number of pairs with sum >=S in any permutation.

4. The worst possible rank is this count.

So the code steps:

Implement these steps.

Now, let's think about how to compute the minimal S >=x.

Approach:

Sort a in ascending order, sort b in ascending order.

For each a_i in a, find the smallest b_j in b such that a_i +b_j >=x. The minimal sum for a_i is a_i + b_j. Then, the minimal S is the minimum of all these sums.

This can be done as follows:

Sort a in ascending order.

Sort b in ascending order.

Initialize minimal S to infinity.

For each a_i in a:

   target = x -a_i.

   left = 0, right =n-1.

   while left <=right:

       mid = (left + right) //2.

       if b[mid] >= target:

           right = mid -1.

       else:

           left = mid +1.

   if left <n:

       current_sum =a_i +b[left]

       if current_sum < minimal_S:

           minimal_S = current_sum

So for each a_i, we find the smallest b_j >= target (x -a_i), then compute the sum. The minimal sum across all a_i and their corresponding b_j is our S.

Now, after finding S, we need to compute the maximum possible pairs >=S in a permutation.

For this, sort a in ascending order and sort b in descending order.

Then, for each i in 0..n-1:

   if a[i] +b[i] >=S, increment count.

The count is the maximum possible pairs >=S.

So the worst possible rank is this count.

Thus, the code would proceed as follows.

But wait, what if there are multiple pairs (a_i, b_j) that sum to exactly S, and we need to choose the minimal S.

For example, in the first sample, x=2. All pairs sum to 2. So S is 2. Then, the maximum possible pairs >=S is 5. So worst rank is 5.

Which matches the sample.

In the second sample, the minimal S is 4+3=7 (since x=7). Then, the maximum number of pairs >=7 is found by sorting a in ascending order and b in descending order.

Let's see:

Original a: [4,3,5,6,4,4] → sorted ascending: [3,4,4,4,5,6]

Original b: [8,6,0,4,3,4] → sorted descending: [8,6,4,4,3,0]

Pair each a[i] with b[i]:

3 +8 =11 >=7 → yes.

4 +6 =10 >=7 → yes.

4 +4=8 >=7 → yes.

4 +4=8 >=7 → yes.

5 +3=8 >=7 → yes.

6 +0=6 <7 → no.

So count is 5. But the sample's worst rank is 5. But sample output is 1 5.

Wait, the sample's output is 1 5, which matches. So the worst rank is 5.

But according to this, the count is 5. So why is the worst rank 5?

Because Vasya is one of those 5 pairs. So the worst possible rank is 5.

Yes.

So the code correctly computes this.

Now, let's proceed to code.

First, read n and x.

Then read a and b.

Then compute the minimal S.

To compute S:

Sort a ascending.

Sort b ascending.

For each a_i in a:

   find the first b_j in b that is >= (x -a_i).

   if found, sum_candidate is a_i +b_j.

   keep track of the minimal sum_candidate.

Once all a_i are processed, S is the minimal sum_candidate.

But what if x is zero? Well, according to the constraints, x can be zero. But since it's guaranteed that there exists at least one pair >=x, which is zero, so there is at least one sum >=0.

Once S is found, then compute the maximum number of pairs >=S in a permutation.

To do this:

Sort a ascending.

Sort b descending.

Then, pair each a[i] with b[i], and count how many pairs have sum >=S.

This count is the worst possible rank.

Thus, the code would be:

Read n, x.

Read a as list.

Read b as list.

Sort a ascending.

Sort b ascending.

# compute minimal S

min_s = float('inf')

for ai in a:

    target = x - ai

    left, right = 0, len(b)-1

    res = None

    while left <= right:

        mid = (left + right) // 2

        if b[mid] >= target:

            res = mid

            right = mid -1

        else:

            left = mid +1

    if res is not None:

        current_sum = ai + b[res]

        if current_sum < min_s:

            min_s = current_sum

# Now, compute the maximum count of pairs >= min_s

a_sorted = sorted(a)

b_sorted_desc = sorted(b, reverse=True)

count =0

for i in range(n):

    if a_sorted[i] + b_sorted_desc[i] >= min_s:

        count +=1

print(1, count)

Wait, but in the code, after sorting a ascending, and b in ascending order, then for each a_i, we find the minimal b_j that is >=x -a_i.

But when we sort b in ascending order, the binary search finds the first occurrence of b_j >= target.

Yes.

Then, for the maximum count, sort a ascending and sort b in descending order, then pair each a[i] with b[i].

So the code should work.

Testing the first sample:

Sample 1:

n=5, x=2.

a = [1,1,1,1,1]

b = [1,1,1,1,1]

sorted a is [1,1,1,1,1]

sorted b is [1,1,1,1,1]

for each a_i (1):

target = 2-1=1.

binary search in b (sorted ascending) for first element >=1.

The first element is 1.

sum_candidate is 1+1=2. So min_s is 2.

Now, compute maximum count:

a_sorted = [1,1,1,1,1]

b_sorted_desc = [1,1,1,1,1]

each pair sums to 2 >=2 → count=5.

So output 1 5.

Which matches.

Sample 2:

n=6, x=7.

a = [4,3,5,6,4,4]

sorted a: [3,4,4,4,5,6]

b = [8,6,0,4,3,4]

sorted b ascending: [0,3,4,4,6,8]

Processing each a_i:

For a_i=3:

target=7-3=4. Looking in b for first >=4.

b[2] is 4 (indexes 0-based). sum is 3+4=7. current_sum=7.

For a_i=4 (next elements):

target=7-4=3. first b >=3 is 3 (index 1). sum is4+3=7. current_sum is 7.

Same for other a_i=4: sum 4+3=7.

a_i=5: target=7-5=2. first b >=2 is 0? No. Wait, sorted b is [0,3,4,4,6,8]. So for target 2, the first b >=2 is 3 (index 1). sum is5+3=8. current_sum=8.

But since we are looking for minimal S, this is higher than 7, so doesn't affect the minimal S.

a_i=6: target 7-6=1. first b >=1 is 0 → no? Wait, the sorted b is [0,3,4,4,6,8]. target=1. The first element >=1 is 3 (index 1). sum is 6+3=9. Which is higher than 7.

So after processing all a_i, the minimal S is 7.

Then, sort a in ascending [3,4,4,4,5,6], sort b in descending [8,6,4,4,3,0].

Pair each:

3 +8 =11 >=7 → yes.

4+6=10 → yes.

4+4=8 → yes.

4+4=8 → yes.

5+3=8 → yes.

6+0=6 <7 → no.

Count is 5. So output 1 5.

Which matches the sample.

Thus, the code should work.

Now, the code needs to handle large n (1e5) efficiently. The steps are:

Sorting a and b: O(n log n) each.

Computing minimal S: O(n log n) (binary search for each a_i).

Computing the count: O(n log n) for sorting and O(n) for iteration.

Thus, the total time is O(n log n), which is acceptable for n=1e5.

The code should work.

Now, let's write the Python code.

But in Python, sorting is done via the sorted() function. For large n, this is efficient.

In the code:

Read n, x.

Read a list as integers.

Read b list as integers.

Sort a in ascending order.

Sort b in ascending order.

Compute the minimal S.

Then sort a in ascending order again (though it's already sorted), and sort b in descending order.

Then count pairs.

But wait, after the first sort, a is already sorted. So for the second part, we can reuse the sorted a.

But in the code above, after sorting a, we can just use it again.

In code:

But let's see:

After sorting a in ascending order for the minimal S step, the a list is already sorted. So when we compute a_sorted = sorted(a), it's redundant. So we can use the same sorted a.

So the code can be optimized.

But for clarity, let's proceed.

The code:

Read n, x.

Read a as list.

Read b as list.

Sort a in ascending.

Sort b in ascending.

Compute minimal S.

Then, sort a in ascending (again, already sorted).

Sort b in descending.

Count.

So the code:

n, x = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

a_sorted = sorted(a)

b_sorted = sorted(b)

min_s = float('inf')

for ai in a_sorted:

    target = x - ai

    left = 0

    right = len(b_sorted) - 1

    res = None

    while left <= right:

        mid = (left + right) // 2

        if b_sorted[mid] >= target:

            res = mid

            right = mid - 1

        else:

            left = mid + 1

    if res is not None:

        current_sum = ai + b_sorted[res]

        if current_sum < min_s:

            min_s = current_sum

# Now compute the count

a_asc = a_sorted  # already sorted

b_desc = sorted(b, reverse=True)

count = 0

for i in range(n):

    if a_asc[i] + b_desc[i] >= min_s:

        count +=1

print(1, count)

But in the code above, when sorting b in descending order for the count step, we need to sort the original b list, but since the b_sorted is already sorted ascending, perhaps it's better to reverse it.

So, for the count step:

b_sorted_asc = sorted(b)

b_sorted_desc = b_sorted_asc[::-1]

But wait, in the code above, for the minimal S step, we sorted b into b_sorted (ascending). Then, for the count step, we sort the original b again into descending order. This is redundant; we can just reverse the b_sorted_asc list.

So in code:

b_sorted_asc = sorted(b)

b_sorted_desc = list(reversed(b_sorted_asc))

This way, we avoid sorting again.

Thus, the code can be optimized as follows:

n, x = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

a_sorted = sorted(a)

b_sorted_asc = sorted(b)

min_s = float('inf')

for ai in a_sorted:

    target = x - ai

    left = 0

    right = len(b_sorted_asc) - 1

    res = None

    while left <= right:

        mid = (left + right) // 2

        if b_sorted_asc[mid] >= target:

            res = mid

            right = mid - 1

        else:

            left = mid + 1

    if res is not None:

        current_sum = ai + b_sorted_asc[res]

        if current_sum < min_s:

            min_s = current_sum

# Now compute the count

b_sorted_desc = list(reversed(b_sorted_asc))

count = 0

for i in range(n):

    if a_sorted[i] + b_sorted_desc[i] >= min_s:

        count +=1

print(1, count)

This should work.

Let's test the first sample:

Sample 1:

After sorting a and b_asc, both are [1,1,1,1,1].

For each ai (1):

target = 2-1=1. The first element in b_asc >=1 is 1 (index 0). sum 2.

min_s is 2.

b_sorted_desc is [1,1,1,1,1].

Pairing each a_sorted[i] (1) with b_sorted_desc[i] (1): sum is 2 >=2. count 5.

Output 1 5.

Sample 2:

a_sorted is [3,4,4,4,5,6].

b_sorted_asc is [0,3,4,4,6,8].

For each ai in a_sorted:

ai=3: target 7-3=4. Find first >=4 in b_sorted_asc (index 2:4). sum 7.

ai=4: target 3. find first >=3 in b_sorted_asc (index 1:3). sum 7.

Similarly for others.

min_s is 7.

b_sorted_desc is [8,6,4,4,3,0].

pairing:

3+8=11 >=7: yes.

4+6=10 >=7: yes.

4+4=8 >=7: yes.

4+4=8 >=7: yes.

5+3=8 >=7: yes.

6+0=6 <7: no.

count=5. output 1 5.

Thus, the code works.

Now, in terms of handling large inputs, this code should be efficient. The binary search is O(n log n), and the other steps are O(n log n) as well. So for n=1e5, it's feasible.
</think>

```python
n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sorted = sorted(a)
b_sorted_asc = sorted(b)

min_s = float('inf')
for ai in a_sorted:
    target = x - ai
    left, right = 0, len(b_sorted_asc) - 1
    res = None
    while left <= right:
        mid = (left + right) // 2
        if b_sorted_asc[mid] >= target:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    if res is not None:
        current_sum = ai + b_sorted_asc[res]
        if current_sum < min_s:
            min_s = current_sum

b_sorted_desc = b_sorted_asc[::-1]
count = 0
for i in range(n):
    if a_sorted[i] + b_sorted_desc[i] >= min_s:
        count += 1

print(1, count)
```