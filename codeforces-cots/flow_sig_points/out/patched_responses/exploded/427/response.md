<think>
Okay, let's tackle this problem. So, the problem is that Valentine wants to exclude all movies of one genre, and we need to find out which genre to exclude so that the total number of stresses (mood changes) is minimized. If there are multiple options, pick the smallest genre number.

First, I need to understand what constitutes a stress. From the description, whenever the genre changes from the previous movie to the next, that's a stress. So consecutive movies of the same genre don't add any stress. For example, if the sequence is 1,1,2, then there's one stress between the second and third movies.

When we remove a certain genre x, all the movies of that genre are excluded. So the original list is filtered by removing all x's. Then, we need to count the number of transitions between different genres in this new list. That's the number of stresses.

The challenge is to compute for each possible x, the number of stresses after removing x, and find the x with the minimum such count (and smallest x if there's a tie).

But how do we compute this efficiently, especially given the constraints where n can be up to 1e5? A brute-force approach where for each x we iterate through the list and compute the stresses would be O(k*n), which could be up to 1e10 operations. That's way too slow.

So we need a smarter approach.

Let's think about the original list. The number of stresses in the original list is the number of times consecutive elements are different. For example, in the list [1,1,2,3,2], the stresses are between 1-2, 2-3, 3-2, so 3 stresses.

When we remove a genre x, we process the original list and skip all x's. The new list is the original with all x's removed. The number of stresses in this new list is the number of adjacent pairs in this new list that are different.

So, the key is to find, for each x, how many transitions (i,i+1) in the original list are such that either a[i] or a[i+1] is x, and in the new list, this transition is eliminated. Also, transitions that are split into multiple transitions when x's are removed might actually decrease the total stresses.

Wait, no. Let's think again. When we remove x, any two consecutive elements in the new list (after removing x) that are different contribute to a stress. So, the problem reduces to counting the number of adjacent pairs in the filtered list where the two elements are different.

But how to compute this efficiently for all x?

Alternative approach: For each x, the new list is the original list with x's removed. The number of stresses is the number of adjacent pairs in this new list that are different.

Let's denote the original stress count as S. Then, when we remove x, some transitions are removed and some new transitions might be introduced.

Wait, no. For example, consider the original list [a, x, b]. After removing x, the new list is [a, b]. So the transition a→b is new, but in the original list, there were transitions a→x and x→b, which are now replaced by a→b. So the stress count in this case depends on whether a and b are different.

Hmm. So the problem is that when consecutive x's are removed, adjacent elements in the original list that are separated by x's could now form new transitions. So the total number of stresses after removing x is not straightforward to compute from the original transitions.

This suggests that we need a way to model how removing x affects the transitions between elements.

Let me think. Let's process the original list and create a list without x. Then, count the number of adjacent differences in this new list.

But doing this for each x would be O(n) per x, which is not feasible for n=1e5 and k=1e5. Wait, but the problem says k is up to n, but in the constraints, k is up to n. However, the problem statement says that each of the k genres appears at least once, so for k=1e5, n must be at least 1e5, but perhaps in such cases, k is 1e5 and n is 1e5. But even then, O(k*n) is 1e10, which is way too slow.

So we need a way to compute for each x the number of stresses in O(1) or O(1) per x, after some preprocessing.

So let's think about the structure of the original list. Let's imagine that the original list is a sequence of runs: consecutive elements of the same genre. For example, 1,1,2,3,3 becomes runs of [1 (x2), 2 (x1), 3 (x2)]. Each run is a group of the same genre.

In this case, the number of original stresses is the number of transitions between runs, which is (number of runs -1). For example, 3 runs have 2 transitions.

But when we remove x, the runs that are of genre x are removed, and the remaining runs are concatenated. However, if two runs (from different genres) become adjacent after removing x runs, they form a new transition if they are different.

Wait, for example: original runs are A (x's) → B → C (x's) → D. After removing x, B and D are adjacent. If B's genre is different from D's, this adds a transition. So the total transitions in the new list is the number of adjacent runs (non-x) pairs that are different.

So, here's the key idea: the original list can be represented as a list of runs. For each x, when we remove all runs of x, the new list of runs is the original runs minus the x runs. The number of stresses in the new list is the number of transitions between consecutive runs in this new list. Each such transition contributes 1 if the two runs are different genres, 0 otherwise.

So, for each x, the number of transitions after removing x is equal to the sum over consecutive pairs (u, v) in the filtered runs (without x) of 1 if u.genre != v.genre, else 0. Which is the same as the number of adjacent pairs of runs (after removing x) that are different.

The original runs can be preprocessed. Let's process the original list into runs. For example, the example input 1:

Original list is 1 1 2 3 2 3 3 1 1 3. The runs are:

1 (2), 2 (1), 3 (1), 2 (1), 3 (2), 1 (2), 3 (1).

Wait, let's count them step by step:

Original sequence: 1,1,2,3,2,3,3,1,1,3.

Runs:

1 (from index 0-1, count 2)

2 (index 2, count 1)

3 (index 3, count 1)

2 (index4, count1)

3 (index5-6, count2)

1 (index7-8, count2)

3 (index9, count1)

So the runs are:

genres = [1,2,3,2,3,1,3]

Then the original stress count is (7 runs -1) =6. But the original example says when we exclude x=3, the filtered genres are 1,1,2,2,1,1. So runs would be 1 (2), 2 (2), 1 (2). The number of stresses is 2 (transitions 1→2 and 2→1).

Which is 2. So the approach here is that when you remove x=3, the runs that are x are removed. Then, the adjacent runs in the remaining list are checked for transitions.

So, the problem reduces to, for each x, the number of transitions between consecutive runs in the filtered list (after removing x runs). Then, the stress count is the sum of transitions (1 if consecutive runs are different, else 0).

Thus, the plan is:

1. Preprocess the original list into runs. Each run has a genre and a length (though length might not matter here, just the genre and the order).

2. For each x, iterate through the runs and compute the number of transitions between consecutive non-x runs. But how to do this efficiently.

But how to compute this efficiently for all x?

Alternative idea: For each run, note the previous and next non-x runs in the original sequence, and see how transitions are added or removed.

But perhaps the optimal approach is to precompute for each x, the number of transitions that are removed and added when x is excluded.

Alternatively, for each x, the total number of transitions after removal is equal to the number of transitions in the original list minus the transitions that are in the original list and involve x, plus any new transitions that are created by merging adjacent runs that are now next to each other after x runs are removed.

Wait, maybe not. Let's think:

Original transitions are between consecutive runs. For example, in the original list of runs R1, R2, R3, ..., Rm, transitions are between R1 and R2, R2 and R3, etc. The total is m-1.

Now, when we remove x's runs, the transitions that are between two non-x runs that were separated by one or more x runs will now become transitions in the filtered list. For example, if we have runs A, X, B (where X is x), then in the original list, transitions are A-X and X-B. When X is removed, A and B become adjacent. If A's genre != B's genre, then the transition A-B contributes 1 stress. So, the original transitions (A-X and X-B) are removed, and a new transition (A-B) is added if A and B are different.

But how do we track all such cases?

This seems complicated. Let's think of it in terms of the runs list.

For each x, the filtered runs are all runs where the genre is not x. Let's call this list S. Then, the number of transitions in S is (length of S - 1) minus the number of consecutive pairs in S that are the same genre.

Wait, no. The number of transitions is the number of consecutive pairs in S that are different. For example, if S has elements [A, B, B, C], the transitions are A-B (different, 1), B-B (same, 0), B-C (different, 1). Total transitions is 2.

Which is equal to (length of S -1) minus the number of consecutive pairs that are same. So transitions = (len(S)-1) - same_pairs.

But same_pairs is the number of consecutive pairs in S where the two runs have the same genre. So for S of length L, transitions = (L-1) - same_pairs.

Alternatively, transitions can be computed by iterating through S and counting how many adjacent pairs are different.

But how does this relate to the original runs?

The key is that when you remove x's runs, you have to look at the original runs and see how their adjacency changes. For example, after removing x runs, two runs A and B (which were originally separated by x runs) now become adjacent. If A and B are different, this adds a transition. If they are the same, then they would merge into a single run, but in our runs list, they are consecutive in S. So in the runs list S, consecutive runs that are same would merge, but the runs list S may have same consecutive genres. Wait, no. Because the runs list is built by grouping consecutive same genres. So in the original runs list, consecutive runs are of different genres. So, in the original runs list, runs are such that consecutive runs have different genres.

Wait, that's important. Because each run in the original list is a maximal sequence of the same genre. So consecutive runs in the original list are of different genres. So the original transitions are exactly the number of runs minus 1. Because each consecutive pair is a different genre.

Wait yes. Because runs are sequences of same genre, so consecutive runs are different. So in the original runs list, the number of transitions is (number of runs -1). Because each transition between runs is a different genre.

So when we remove x's runs, the new runs list S consists of the original runs that are not x. However, since consecutive runs in the original list are of different genres, consecutive runs in S can now be of the same genre. For example, original runs: A (genre 1), X (genre x), B (genre 1). So after removing X runs, the new runs are A and B, which are both genre 1. So in the new runs list, A and B are consecutive. Since they are the same genre, in the new list, they would be merged into a single run. So the new runs list after merging would be a single run of genre 1. But when we build S by removing x runs, how does that affect the transitions?

Wait, but the problem states that the new list is the original list with x's removed. So the runs in the new list are formed by consecutive elements in the filtered list. So in the filtered list, consecutive same genres would form runs. So for example, original runs [A (1), X (x), B (1)], when X is removed, the new list is A followed by B. But in the original list, A and B were separated by X. So in the filtered list, the elements of A and B are now adjacent. So in the new list, the runs would be a single run of genre 1. So the transitions in the new list would be zero. So the number of stresses is (number of runs in the new list -1) = 0.

But the original runs list after removing X would have two runs (A and B), which are same genre. So when we form the new runs list, the two runs would merge into one. Thus, the number of transitions in the new list is (number of runs in the new merged list -1).

Therefore, to compute the number of transitions after removing x, we need to consider the merged runs in the filtered list.

But how to compute this?

Alternative approach:

After removing x, the new list is the original list with x's removed. So the new list is a sequence of genres, and the number of transitions is the number of times consecutive elements in this new list are different.

But the problem is that this sequence can be very long (up to 1e5 elements), and for each x, we can't process it directly.

So we need a way to compute the number of transitions for the new list without processing each element.

But the original runs list is a list of runs where consecutive runs are different. So when we remove x's runs, the remaining runs are those not of x, but they are still in order. But consecutive runs in the original list may now be adjacent in the filtered list. However, since original runs are consecutive and different, the new runs in the filtered list may have consecutive runs of the same genre. For example, in original runs [A, X, B], where A and B are same genre. Then, after removing X, the new runs list is [A, B], which are same genre. So when merged into a single run, the transitions are zero.

But how to model this?

So, the steps for x:

1. Remove all runs of x from the original runs list. Let the new list be S.

2. Now, process S to merge consecutive runs of the same genre. The merged runs form the new runs list S'.

3. The number of transitions is (length of S' -1).

So the problem reduces to, for each x, compute the length of S' after merging, then subtract 1.

But how to compute this efficiently for all x?

The key is that S is the original runs list with x runs removed. Then, S' is formed by merging consecutive runs in S that are same genre.

The original runs list has runs with consecutive genres different. So S is the list of original runs not x. But when two runs in S are consecutive in S (i.e., in the original runs list, there were x runs between them), and have the same genre, they will merge into one.

So for example, in the original runs list: A (1), X (x), B (1), after removing X, S is [A, B]. But since A and B are same genre, in S' they merge into one run, so S' has length 1.

So, for each x, the merged runs list S' is formed by merging consecutive same-genre runs in S.

The number of transitions is (len(S') - 1).

So how can we compute len(S') for each x efficiently?

The original runs list is a list where consecutive runs are different. So in S (after removing x runs), consecutive runs in S can be same or different. Each pair of consecutive same-genre runs in S will merge into a single run, thus reducing the total length.

So the number of merges needed is the number of consecutive pairs in S that are same-genre. So len(S') = len(S) - number of consecutive same-genre pairs in S.

Because each such pair reduces the length by 1.

For example, S has [A, B, B], where A and B are same genre. Then consecutive pairs (A,B) and (B,B). Wait, no. Wait, S is a list of runs that are not x. So in S, consecutive runs are from the original runs list, which are different. But in S, two runs may have same genre if they were separated by x runs in the original list.

So for example, original runs: [A (1), X (x), B (1)], S becomes [A, B]. Both are genre 1, so when merged, len(S') is 1.

The consecutive pair (A,B) in S is same genre, so this contributes to a merge. So in S, consecutive runs may be same genre, and each such occurrence reduces len(S') by 1.

Thus, for each x:

len(S') = len(S) - (number of consecutive pairs in S with same genre)

Therefore, transitions after removing x is len(S') -1 = (len(S) - same_pairs) -1.

But len(S) is the number of original runs minus the number of x runs. So len(S) = total_runs - cnt_runs[x], where cnt_runs[x] is the count of x runs in the original runs list.

So transitions after x is removed is ( (total_runs - cnt_runs[x] - same_pairs) -1 ) = (total_runs - cnt_runs[x] - same_pairs -1).

Wait, no: len(S) is (original number of runs) minus cnt_runs[x], since we remove all x runs. Then, len(S) = original_runs_count - cnt_runs[x].

Then, len(S') = len(S) - same_pairs, where same_pairs is the number of consecutive pairs in S with same genre.

Thus, transitions = len(S') -1 = (len(S) - same_pairs) -1 = (original_runs_count - cnt_runs[x] - same_pairs) -1.

But how to compute same_pairs for each x.

Same_pairs is the number of consecutive pairs in S (original runs list with x runs removed) where the two runs have the same genre.

So for each x, we need to count how many consecutive pairs in the original runs list (after removing x runs) are of the same genre.

But how to compute this efficiently.

The approach here is to precompute for each x, the number of same-genre consecutive pairs that would exist in S (the list after x runs are removed). This can be done by looking at all pairs of runs in the original list that are not x, and see if they are consecutive in S and have same genre.

But how?

For example, in the original runs list, suppose we have runs R1, R2, R3, R4, etc. For x, we remove all runs with genre x. Then, S is the list of remaining runs.

In S, consecutive runs are those that were not x and are adjacent in S, but in the original list they were separated by some x runs.

For example, in original runs: R1 (genre A), R2 (x), R3 (genre B), R4 (x), R5 (genre A).

After removing x runs, S is [R1, R3, R5]. Now, consecutive pairs in S are (R1, R3) and (R3, R5). If R1's genre is A, R3's genre is B, R5's genre is A, then (R1, R3) is different (A vs B), (R3, R5) is B vs A (different). So same_pairs is 0. So transitions would be (3 - 0) -1 = 2.

But if in another example, S has runs R1 (A), R3 (A), R5 (A), then same_pairs would be 2 (since (R1, R3) and (R3, R5) are both same genre). Then transitions would be (3 - 2) -1 = 0.

So same_pairs is the number of pairs of consecutive runs in S where their genres are the same.

So for each x, same_pairs is the count of pairs (R_i, R_j) in the original runs list such that:

- R_i is not x, R_j is not x.

- Between R_i and R_j, there are some runs of x.

- R_i and R_j are consecutive in S (i.e., all runs between them in original list are x).

- R_i.genre == R_j.genre.

So the problem is to count for each x, the number of such pairs (R_i, R_j) in the original runs list where R_i and R_j are separated by x runs (possibly multiple x runs) and R_i.genre == R_j.genre.

So, for each x, the same_pairs is the number of times in the original runs list that two non-x runs are separated by any number of x runs and have the same genre.

So the approach to compute same_pairs for x is:

- Iterate through the original runs list, and for every pair of runs (R_prev, R_curr) where all runs between them are x, check if R_prev.genre == R_curr.genre. Count how many such pairs exist.

But how to do this efficiently?

We can pre-process for each x, all the runs that are not x, and see when they are consecutive in S (i.e., in the original runs list, between them are only x runs).

So here's the plan:

1. Precompute the original runs list. Let's call this list runs.

   For example, runs is a list of genres, each consecutive element different.

2. For each x, collect all the indices of runs that are x. Then, the remaining runs (non-x) form S.

3. The same_pairs for x is the number of pairs of consecutive runs in S (i.e., runs in the original list that are not x and are consecutive in S) where their genres are equal.

   These consecutive runs in S are pairs (runs[i], runs[j]) where j = i+1 in S, which in the original runs list, all the runs between runs[i] and runs[j] are x.

So, for each x, same_pairs is the count of all pairs of runs in the original runs list where runs[i] and runs[j] are not x, and between them are one or more x runs, and runs[i].genre == runs[j].genre.

So how do we find all such pairs for each x?

Alternative idea: For each x, iterate through the original runs list, and whenever we find a sequence of runs where between two non-x runs, there are x runs, check if the two non-x runs are same.

But for n=1e5 runs, and k=1e5, this is O(n) per x, which is O(nk) time. Not feasible.

Alternative approach: For each run, for each run after it, check if all runs in between are x. But this is O(n^2), which is impossible.

Alternative idea: For each x, collect all the non-x runs in order. Then, for each consecutive pair in this list, check if their genres are same, and also if in the original runs list, the runs between them are all x.

Wait, but the non-x runs in the original list are ordered. For x, the runs not x are in S, in their original order. So consecutive pairs in S are consecutive in the original list's order, but possibly with x runs in between.

So, the same_pairs for x is the number of pairs of consecutive runs in the S list (i.e., in the original list, non-x runs, in order) where their genres are same, and all runs between them in the original list are x.

So for example, in the original runs list:

R1 (A), R2 (x), R3 (x), R4 (B), R5 (x), R6 (A), R7 (C).

For x, the S list is [R1, R4, R6, R7]. Now, consecutive pairs are (R1, R4), (R4, R6), (R6, R7).

Check for each pair:

- R1 and R4: all runs between are x (R2, R3). Genres are A and B: different. So not counted.

- R4 and R6: runs between R4 and R6 are R5 (x). Genres B and A: different. Not counted.

- R6 and R7: genres A and C: different. Not counted.

So same_pairs is 0.

Another example: original runs R1 (A), R2 (x), R3 (A), R4 (B), R5 (x), R6 (A), R7 (x), R8 (A).

For x, the S list is [R1, R3, R4, R6, R8].

Check consecutive pairs:

R1 and R3: genres A and A. Between them is R2 (x). So same, count 1.

R3 and R4: A and B. Different.

R4 and R6: B and A. Different.

R6 and R8: A and A. Between them R7 (x). Count 1.

So same_pairs is 2.

So transitions would be (5 - 2) -1 = 2.

So the same_pairs is the number of consecutive pairs in S where genres are same and between them in original runs are all x.

The key is that for x, the same_pairs is the number of consecutive pairs in S (non-x runs) where their genres are same and the runs between them in the original list are all x.

Thus, to compute same_pairs for x, we can process all consecutive pairs of non-x runs in the original list and check if the runs between them are all x.

But how to do this efficiently.

Alternative approach: Precompute for each x, all the non-x runs. Then, for each consecutive pair in this list, check if the runs between them (in the original list) are all x.

If yes, and their genres are same, then same_pairs for x increments by 1.

But how to check if the runs between them are all x.

For example, if in the original runs list, we have two non-x runs at positions i and j (i < j), and all runs from i+1 to j-1 are x, then this pair contributes to same_pairs for x if their genres are same.

So for each x, we need to find all pairs of runs (i, j) where:

1. runs[i].genre != x,

2. runs[j].genre != x,

3. for all k in i+1 to j-1, runs[k].genre == x,

4. runs[i].genre == runs[j].genre.

Then, the total same_pairs for x is the number of such pairs.

Now, how can we find these pairs efficiently.

Let's think about the runs list. For each x, the runs of x split the non-x runs into groups. Between two non-x runs, there might be x runs. If between two non-x runs, all intermediate runs are x, then these two non-x runs are consecutive in the S list (when x is removed). So their genres are checked for equality.

So, for each x, the same_pairs is the number of pairs of consecutive non-x runs in the original runs list that are separated by one or more x runs and have the same genre.

So for x, we can:

- Iterate through the runs list, track the previous non-x run. For each current non-x run, check if the previous non-x run is separated by only x runs. If so, and their genres are same, increment same_pairs.

This would take O(n) time per x, but with k up to 1e5, this is O(nk) time, which is not feasible.

So we need a better approach.

Alternative idea: Precompute for each x, all the positions where x runs occur. Then, for each pair of non-x runs that are adjacent in the S list (i.e., between them are only x runs), check if their genres are same.

But how?

An alternative approach is to precompute for each x, the list of non-x runs in order. Then, for each consecutive pair in this list, check if the runs between them in the original list are all x.

But again, this is O(n) per x, which is not feasible.

Hmm. So perhaps we need to find a way to represent for each possible pair of non-x runs (i, j) whether the runs between them are all x. But even that is O(n^2) space.

Alternative idea: For each x, same_pairs is the sum over all pairs of non-x runs (i, j) in consecutive positions in the S list (i.e., between i and j are only x runs) where genres are same.

So, the same_pairs can be found by processing the original runs and for each x, track the previous non-x run. For example:

prev_non_x_genre = None

for run in runs:

    if run.genre == x:

        continue

    if prev_non_x_genre is not None:

        # check if between prev_non_x and current run, all runs were x

        # but how to track that?

        # if between prev_non_x and current run, all runs are x, then we have a consecutive pair in S

        if prev_non_x_genre.genre == current.genre:

            same_pairs +=1

    prev_non_x_genre = current

But how do we check that between prev_non_x and current run, all the runs are x?

Wait, if we process the runs list in order, and for each x, track the previous non-x run, then between the previous and current non-x run, the runs in between are x.

Because, in the original runs list, runs are ordered, and any non-x run followed by x runs followed by another non-x run would have the previous non-x run and current non-x run separated by x runs.

But this is not necessarily true. Because between prev_non_x and current run, there could be other non-x runs. For example, if x is 3, and runs are 1, 2, 3, 4. Then, the non-x runs are 1,2,4. So between 2 and 4, there's a 3 run. But between 1 and 2, there are no x runs, so they are consecutive in S (since x runs are removed). So for x=3, the pair (1,2) is consecutive in S, and no x runs are between them.

Wait, but in the original runs list, the runs are ordered, and consecutive. So if prev_non_x and current are consecutive in the original runs list, then between them there are no runs (they are consecutive). So between them, there's no x runs, so they are consecutive in S (since x runs are removed). So, for example, in runs [1,2,3], x=3. The non-x runs are 1 and 2. They are consecutive in the original runs list (no runs in between), so they are consecutive in S.

So, for each x, in the runs list, the non-x runs are in order, and consecutive pairs in S are pairs of non-x runs that are consecutive in the original runs list (so no runs between them) or separated by x runs.

Wait, no. For example, original runs are 1,3,2,3,4. For x=3, the non-x runs are 1,2,4. These are consecutive in S. The original runs between 1 and 2 are 3 (x) and between 2 and 4 are 3 (x). So the pairs (1,2) and (2,4) are consecutive in S, and between each pair are x runs.

But if the runs list is 1,2,3,4, then for x=3, the non-x runs are 1,2,4. The pairs (1,2) are consecutive in the original runs list (no x runs between them) and (2,4) are separated by x runs (3). So in this case, the pair (1,2) is consecutive in S, but they are adjacent in the original runs list.

Thus, when we iterate through the runs list, for x, we can collect the non-x runs in a list S'. Then, consecutive pairs in S' are consecutive in S', regardless of whether they were consecutive in the original runs list or not. For example, if two non-x runs are separated by any number of x runs (and possibly other non-x runs?), no. Because the non-x runs are those not equal to x. So if between two non-x runs in the original list, there are other non-x runs (of different genres), then those would also be in S', making the original two runs not consecutive in S'.

Wait, no. The S' list for x is formed by taking all runs from the original list that are not x. So if two runs are non-x and are separated by other non-x runs, then in S' they are not consecutive. Only if all runs between them are x can they be consecutive in S'.

Ah, right! So for two non-x runs to be consecutive in S', all the runs between them in the original runs list must be x. Because if there's any non-x run between them, then that run is also in S', so they are not consecutive.

So for example:

Original runs list: [A, B, C, X, D], x=X.

S' is [A, B, C, D]. So consecutive pairs are (A,B), (B,C), (C,D). Between A and B there are no X runs (they are consecutive in the original list). Between B and C, there are no X runs. Between C and D, there is an X run. So in S', all pairs are consecutive, but the X run is between C and D.

Wait, no. The original runs list is [A, B, C, X, D]. So when x is X, the S' list is [A, B, C, D]. The runs between C and D in the original list is X (single run). So in S', C and D are consecutive. But between C and D in the original list is X, which is removed. So consecutive in S' implies that in the original list, the two runs are separated by some X runs.

But in this example, between A and B there are no X runs, but they are consecutive in S'.

So the condition for two non-x runs to be consecutive in S' is that in the original runs list, between them are any number of x runs (including zero). Wait, no. Wait, if in the original runs list, two non-x runs are consecutive (i.e., no runs in between), then they are consecutive in S' if and only if there are no x runs between them, which is zero x runs. But in that case, they are consecutive in S'. So the same_pairs for x is the count of consecutive pairs in S' where their genres are same, regardless of how many x runs were between them in the original runs list.

But how to model this.

The problem is that for any x, when we process the original runs list, the S' list is the non-x runs. The consecutive pairs in S' are pairs of runs where in the original list, there are only x runs between them.

So, for example, if in the original runs list, two non-x runs are adjacent (i.e., no runs between them), then they are consecutive in S' if and only if there are zero x runs between them. Which is possible only if they are adjacent in the original list.

Wait, no. For example, two non-x runs are adjacent in the original list. So there are no runs between them. So in S', they are consecutive. So any consecutive pair in the original list of non-x runs are consecutive in S'.

So, the same_pairs for x is the number of consecutive pairs in S' (the non-x runs) where their genres are the same.

So, for x, same_pairs is the number of consecutive pairs in S' (non-x runs in order) where genres are same.

But how to compute this.

The S' list for x is the list of non-x runs, in order. For consecutive pairs in S', we need to count how many have the same genre.

But to compute this, for each x, we can iterate through the runs list, collect the non-x runs into a list S', then iterate through S' and count the number of consecutive pairs with same genre.

But for n=1e5 and k=1e5, this is O(nk), which is too slow.

So we need a way to compute, for each x, the number of consecutive pairs in S' with same genre, without explicitly building S' for each x.

Another observation: For a consecutive pair in the original runs list (runs[i], runs[i+1]), the pair is consecutive in S' for x if and only if both runs are not x. Because if they are not x, then they are in S', and since they are consecutive in the original runs list, they are consecutive in S'. Otherwise, if either is x, then they are not in S' or are skipped.

But that's not the only way consecutive pairs in S' can be formed. For example, runs[i] and runs[j], j > i+1, where runs[i+1 ... j-1] are all x. In this case, runs[i] and runs[j] are consecutive in S'.

So, consecutive pairs in S' can be of two types:

1. Consecutive in the original runs list (i and i+1), and both are not x.

2. Non-consecutive in the original runs list, but all runs between them are x.

This makes it complicated.

But how to model this for all possible x.

Alternative idea: For each x, the S' list is formed by taking all runs not equal to x, in order. The consecutive pairs in S' are pairs of runs in the original list where all the runs between them are x.

So, for each x, the consecutive pairs in S' are all pairs (runs[i], runs[j]) where i < j, runs[i].genre != x, runs[j].genre != x, and for all k in i+1 to j-1, runs[k].genre == x.

But how to find the number of such pairs where runs[i].genre == runs[j].genre.

This seems difficult.

Alternative approach: Precompute for each pair of runs (i, j) where i < j, whether all runs between i and j are x. But this is O(n^2), which is impossible.

Alternative idea: For each x, the same_pairs can be computed as the sum of:

a) The number of consecutive pairs in the original runs list that are both not x and have the same genre. Because these pairs are consecutive in S'.

b) The number of non-consecutive pairs in the original runs list that are separated by x runs and have the same genre.

But how to compute this.

Alternatively, think of it as:

For x, the same_pairs is equal to the number of pairs of runs (i, j) where:

- runs[i].genre != x,

- runs[j].genre != x,

- i < j,

- all runs between i and j are x,

- runs[i].genre == runs[j].genre.

So the problem reduces to counting, for each x, all such pairs.

How can we do this efficiently?

Let's think of the original runs list as a list of genres. For each x, we can build a list of positions where the genre is not x. Then, for each consecutive pair in this list, check if all runs between them are x.

But this is O(m) per x, where m is the number of non-x runs. For x with many non-x runs, this is O(n) per x.

But with k=1e5, this is O(nk) time again.

Alternative idea: For each run i, collect all x's such that i is a run not x, and there exists a run j > i, not x, such that all runs between i and j are x, and runs[i].genre == runs[j].genre.

But this is not helpful.

Alternative approach: Let's model the runs list as a list of genres. For each x, the same_pairs is the number of times two runs of the same genre are separated by one or more x runs.

So for example, if the runs list is A, X, X, A, then x=X would have same_pairs = 1.

But how to compute this for all x quickly.

This feels like a problem where we need to precompute for each possible x, the pairs of runs that are same genre and are separated by x runs.

But how.

Alternative idea: For each pair of runs (i, j) where i < j and runs[i].genre == runs[j].genre, and all runs between i and j are x (for some x), we can increment a counter for x by 1.

But how to find such pairs.

For each pair (i, j) where i < j and runs[i].genre == runs[j].genre:

- Check if all runs between i and j are x for some x.

Wait, but the runs between i and j could be of multiple x genres. For example, between i and j, there are runs of x and y. Then, this pair would contribute to x and y.

But in reality, all runs between i and j must be x for a particular x. So for the pair (i,j) to be considered for x, all runs between i and j must be of genre x.

So for example, if between i and j there are runs of x and y, then this pair (i,j) is not considered for any x.

So for a pair (i,j) to contribute to same_pairs for x, all the runs between i and j must be x, and runs[i].genre must equal runs[j].genre.

Thus, for each pair (i,j) where runs[i].genre == runs[j].genre, and all runs between i and j are x (some x), then x is the genre of those runs. So x must be the same for all the runs between i and j.

If all runs between i and j are x, then x is the genre of those runs, and this pair (i,j) contributes 1 to same_pairs for x.

So the approach is:

- Iterate through all possible pairs (i,j) in the runs list where i < j and runs[i].genre == runs[j].genre.

- For each such pair, check if all runs between i and j are of the same genre x (which could be any x).

- If yes, then for that x, increment same_pairs by 1.

But how to do this efficiently.

The number of pairs (i,j) where runs[i].genre == runs[j].genre is O(n^2), which is not feasible for n=1e5.

This approach is not feasible.

Alternative idea: For each run, track previous runs of the same genre and check if the runs between are of the same x.

But this also seems to be O(n^2) in worst cases.

Alternative plan: For each x, the same_pairs is the number of pairs of non-x runs (i,j) in the runs list such that i < j, runs[i].genre == runs[j].genre, and all runs between i and j are x.

To compute this, perhaps we can precompute for each run i, the next run j where runs[j].genre is the same as runs[i], and all runs between are x.

But again, this seems difficult.

Alternative approach inspired by the examples:

Let's think of the original runs list as a sequence of genres. For each run, we can track for each genre x, the next run of the same genre as the current run, with all intervening runs being x.

But this seems too ambitious.

Alternative idea: For each x, the same_pairs is the number of times there are two runs of the same genre, separated by only x runs.

So, for each x, same_pairs is the count of pairs of runs (i, j) where:

- runs[i].genre == runs[j].genre,

- for all k in i+1 to j-1, runs[k].genre == x,

- runs[i].genre != x.

This way, when x is removed, these two runs become consecutive in S' and their genres are same, so they contribute to same_pairs.

So, for each x, how many such pairs exist.

But how to find this.

Let's imagine that for each x, we can process the runs list and for each run i where runs[i].genre != x, track the next run j > i where runs[j].genre != x and all runs between i and j are x.

If runs[j].genre == runs[i].genre, then this contributes to same_pairs.

But how to compute this.

For example, let's process the runs list and for each run i, look ahead until we find the next non-x run j. If between i and j are all x runs, and runs[j].genre == runs[i].genre, then increment same_pairs for x by 1.

But for n=1e5 and k=1e5, this is O(nk), which is not feasible.

Alternative idea: Preprocess for each run i, the next run j where runs[j].genre is the same as runs[i], and all runs between i and j are x.

But again, this is O(n^2).

Hmm.

Another approach: Let's note that the runs list is such that consecutive runs are of different genres. So between any two runs of the same genre, there must be at least one run of a different genre.

So for two runs i and j (i < j) with runs[i].genre == runs[j].genre, the runs between i and j must have at least one run of a different genre. But in between, if there are multiple x runs, but all are of the same x, then the pair (i,j) would contribute to x's same_pairs.

So for example, runs: A, X, X, X, A. Here, runs[0] and runs[4] are A, and between them are X runs. So for x=X, this pair contributes 1 to same_pairs.

But if between the two A's there are runs of X and Y, then this pair would not contribute to any x's same_pairs.

So, for a pair (i,j) to contribute to same_pairs for x, the runs between i and j must all be x, and x must be the same for all those runs.

So, for each such pair (i,j), the runs between i and j are all x, so x is uniquely determined as the genre of those runs.

Thus, for a pair (i,j) where runs[i].genre == runs[j].genre and between them are runs of the same genre x, this pair contributes to same_pairs of x.

So the plan is:

1. Preprocess all pairs (i,j) where i < j, runs[i].genre == runs[j].genre, and all runs between i and j are of the same genre x.

But how to find these pairs.

An alternative idea is to iterate through the runs list and for each run, track the next run of the same genre, and check if all runs between them are of the same genre.

For example:

for i in 0 to m-1:

    for j in i+1 to m-1:

        if runs[j].genre == runs[i].genre:

            check if all runs between i and j are of the same genre x.

            if yes:

                same_pairs[x] +=1

            break

But even this is O(n^2) in worst cases.

But given that runs are such that consecutive runs are different genres, perhaps the number of pairs (i,j) where runs[i].genre == runs[j].genre is O(n), not O(n^2). Because for each genre g, the runs of g are spread out. For example, if there are m runs of genre g, then there are O(m^2) pairs. So for genres that appear many times, this is O(n^2), which is not feasible.

Thus, this approach is not feasible.

Alternative Idea:

Let's think about the runs list and look for sequences where a run is followed by one or more x runs, then another run of the same genre.

For example, if we have a run A, followed by one or more x runs, followed by another A run, then for x, this pair contributes 1 to same_pairs.

Thus, for each x, the same_pairs is the number of occurrences where a run of genre g is followed by one or more x runs, followed by another run of genre g.

So, for each x, we can look for patterns of the form g, x+, g.

For example, in the runs list:

g, x, x, g → same_pairs[x] +=1.

g, x, x, x, g → same_pairs[x] +=1.

But how to count such patterns for all x and g.

This seems manageable.

Thus, for each run i, we can check if the next run after i is x, and the run after the x runs is g (same as i's genre).

But again, for n=1e5, this would be O(n) time per x.

Alternative approach: Iterate through the runs list once, and for each pair of consecutive runs (i, i+1) that are x, check if the previous non-x run and the next non-x run are the same genre.

But this is not sufficient, since there may be multiple x runs in between.

Hmm.

Alternative idea: For each run i, check the previous and next non-x runs for each x.

But again, this is O(nk) time.

Another Idea:

For each x, the same_pairs is the number of times the pattern g, x+, g occurs in the runs list, where g is not x.

So, for each x, we can count the number of sequences where a run of genre g (g != x) is followed by one or more runs of x, followed by a run of g.

Each such sequence contributes 1 to same_pairs for x.

Thus, the approach is:

1. Iterate through the runs list and for each run i:

   a. If the previous run is x, check if runs[i].genre is the same as the previous non-x run.

   b. But this would only find adjacent pairs. For example, x, g → but not x, x, g.

Another Idea: For each x, we can collect all the runs that are not x. Then, for each consecutive pair in this list, check if the genres are the same and the runs between them are all x.

But how to do this without iterating through the entire list for each x.

But perhaps, during the initial processing of the runs list, we can track for each run, the previous non-x run for any x.

But I'm not sure.

Alternative Idea: For each x, maintain a list of indices of non-x runs. Then, for each consecutive pair in this list, check if all runs between them are x.

But for each x, this list can be built in O(n) time, and for each consecutive pair in the list, checking if all runs between them are x is O(1) time by checking if the indices are consecutive (i+1, j-1, etc. ?)

Wait, for example, if the indices of non-x runs are stored in a list for x, say positions [p0, p1, p2, ... pm], then between p0 and p1, the runs in the original list are p0+1 to p1-1. If all these runs are x, then the pair p0 and p1 contributes to same_pairs if genres are same.

But how to check if all runs between p0 and p1 are x.

But the runs between p0 and p1 are runs from p0+1 to p1-1. So for example, if the runs list is of length 100, and the non-x runs are at positions 5 and 8, then between 5 and 8 are positions 6 and 7. For all these to be x, the genres of runs[6] and runs[7] must be x.

But how to check this efficiently.

The solution is to precompute a 2D array for each x, which is not feasible.

Alternative Idea: For each x, the runs between p0 and p1 are all x if the number of x runs in the original list between p0 and p1 is equal to the number of runs between p0 and p1.

But how to compute the number of x runs between p0 and p1.

But again, this requires O(1) range queries for x runs.

But we can precompute for each x, a prefix sum array of the number of x runs up to each position.

For example, for x, create an array cnt_x where cnt_x[i] is the number of runs up to and including index i that are x.

Then, for a pair of non-x runs at positions i and j (i < j), the number of x runs between i and j is cnt_x[j-1] - cnt_x[i].

If this equals (j - i - 1), then all runs between i and j are x.

Because between i and j, there are j - i - 1 runs, and if all are x, then the number of x runs in that interval is j - i -1.

Thus, for a pair of non-x runs i and j (i < j):

if (cnt_x[j-1] - cnt_x[i]) == (j - i -1), then all runs between i and j are x.

So for each x, we can precompute this cnt_x array, and for each consecutive pair in the non-x runs list for x, we can check if this condition holds.

If yes, then check if their genres are same.

So the steps are:

For each x:

1. Collect all the non-x runs in the runs list, stored in a list called non_x_runs.

2. Compute the cnt_x array, where cnt_x[i] is the number of x runs in the first i runs (up to index i).

3. Iterate through non_x_runs. For each consecutive pair (prev, curr) in non_x_runs:

   a. Get their positions in the runs list: i and j.

   b. The number of runs between i and j is j - i -1.

   c. The number of x runs between i and j is cnt_x[j-1] - cnt_x[i].

   d. If (cnt_x[j-1] - cnt_x[i] == j - i -1), then all runs between are x.

   e. If yes, and prev.genre == curr.genre, then increment same_pairs.

Thus, for each x, the same_pairs can be computed.

This approach is O(n) per x, which is O(nk) time. But for n=1e5 and k=1e5, this is O(1e10), which is way too slow.

So this is not feasible.

Alternative Idea: Find all possible x for which there exists at least one pair (i,j) where genres are same and between them are all x runs. For each such x, increment same_pairs[x] by the number of such pairs.

But how to find these pairs.

Another Idea: Iterate through the runs list and for each possible pair of runs that could form a same_pairs pair, determine which x's they contribute to.

For example, if there is a run i of genre g, followed by a run i+1 of genre x, followed by run j of genre g. Then, this contributes to same_pairs[x] if all runs between i and j are x.

But this is only a pair where j = i+2.

But what if there are multiple x runs between i and j?

For example, i is g, then x runs (i+1, i+2, ..., j-1), then j is g.

Then, this pair contributes to same_pairs[x] by 1.

So, the problem is to find all such sequences of g, followed by one or more x runs, followed by g.

Each such sequence contributes 1 to same_pairs[x].

So, for each such sequence, we can determine the x (the genre of the middle runs) and increment same_pairs[x] by 1.

But how to find all such sequences.

This approach would require iterating through the runs list and checking for such sequences.

Let's see:

Iterate through the runs list from left to right. For each run i, look ahead to see if there's a run j > i such that:

- runs[i].genre == runs[j].genre,

- all runs between i and j are the same genre x,

- x != runs[i].genre.

For each such j, increment same_pairs[x] by 1.

But how to do this efficiently.

This would involve for each run i, looking ahead until a run j is found that matches the genre. If the runs between are all the same x, then increment same_pairs[x] by 1.

But again, this could be O(n^2) in worst cases.

But perhaps, given that the runs list is such that consecutive runs are different, we can find all possible sequences where between two runs of genre g, all runs are the same x.

For example, consider the runs list:

g, x, x, x, g.

This contributes 1 to same_pairs[x].

g, x, y, x, g → between g and g, there are x and y runs. So this doesn't contribute to any x.

g, x, x, y, g → between g and g, there are x, x, y runs. So this also doesn't contribute to any x.

Thus, only sequences where between two g runs, all are x runs (and x is a single genre) contribute to same_pairs[x].

So, for each pair of g runs in the runs list, check if the runs between them are all the same x genre.

If yes, then same_pairs[x] +=1.

But how to find such pairs.

An efficient way would be to, for each genre g, collect the indices of all runs with genre g. Then, for each consecutive pair of indices (i,j) in this list, check if all runs between i and j are of the same genre x.

If yes, then same_pairs[x] +=1.

But for each g, this is O(m^2) where m is the number of runs of genre g. Which could be O(n^2) in total.

Thus, this is not feasible.

Alternative Idea: For each run i, look at the next run i+1. If the next run i+1 is x, then check if there's a run j after i+1 with genre equal to i's genre, and all runs between i+1 and j are x.

But this would only find pairs where there's one x run between i and j.

Not helpful.

Alternative Idea: For each run i of genre g, look for the next run j of genre g such that the runs between i and j are all of the same genre x.

This can be done by:

- For each run i of genre g, we iterate j from i+1 onwards until we find a run of genre g.

- For each such j, check if all runs between i and j are of the same genre x.

If yes, increment same_pairs[x] by 1.

But this is again O(n^2) time in the worst case.

But perhaps in practice, for many cases, this would be manageable.

But for n=1e5, this is not feasible.

Thus, I'm stuck. I need to find a way to compute same_pairs[x] for all x efficiently.

Perhaps I should think of the problem differently.

Another approach: The number of same_pairs for x is the number of times two runs of the same genre are separated by one or more x runs. So for each x, we can precompute this count.

To compute this, for each x, we can maintain a dictionary that tracks the last occurrence of each genre g before x runs.

For example, as we iterate through the runs list:

- When we encounter a run of genre x, we skip.

- When we encounter a run of genre g (not x), we check if the previous non-x run was of genre g. If yes, then same_pairs[x] +=1.

But this only captures consecutive non-x runs in the S list.

Wait, no. Because between the previous non-x run and current run, there could be x runs. So if previous non-x run is g and current is g, then same_pairs[x] +=1.

But how to track the previous non-x run for each x.

This approach would require, for each x, to track the last non-x run genre. But with x varying up to 1e5, this is not feasible in terms of memory.

Thus, this approach is not feasible.

Another Idea: For each x, same_pairs can be computed by iterating through the runs list once and counting the number of times two non-x runs of the same genre are separated by x runs.

But for each x, this would take O(n) time. For k=1e5, this is O(nk) time.

But n can be 1e5, so 1e5 * 1e5 = 1e10 operations. This is way too slow.

Thus, this approach is not feasible.

At this point, I'm stuck and need to think of a different way to model the problem.

Let's return to the initial problem. The stress count after removing x is len(S') -1 - same_pairs. But len(S') is the number of runs in the filtered list after merging.

But the same_pairs is the number of consecutive pairs in the filtered list that are same.

But how to compute len(S').

len(S') is the number of merged runs in the filtered list.

For example, after filtering x, the S list is the runs not x. Then, consecutive runs in S that are same are merged. So the merged runs list S' is formed by grouping consecutive same genres in S.

Thus, len(S') is equal to the number of groups of consecutive same genres in S.

For example, S is [A, B, B, A]. Merged runs are [A, B, A]. len(S') is 3.

The number of transitions is len(S')-1 = 2.

So, the problem is to compute for each x, the number of merged runs in the filtered list.

But how to compute this.

The number of merged runs in S' is equal to the number of transitions between different genres in the S list plus 1.

For example, S list has genres A, B, B, A. Transitions are A→B and B→A. So number of merged runs is 2 transitions + 1 =3.

Thus, the number of merged runs is (number of transitions in S list) + 1.

The number of transitions in S list is the number of consecutive pairs in S list with different genres.

But in the original runs list, consecutive runs are already different. So when we remove x runs, consecutive runs in S list can be same or different.

For example, original runs list has genres A, B, X, A. After removing X, S list is [A, B, A]. The transitions are A→B and B→A. So two transitions. Thus, merged runs count is 3.

But in the original runs list, the S list is [A, B, A], which are consecutive in the original list. But B and A are different, so transitions are two.

Thus, the merged runs count is 3.

Thus, the merged runs count is equal to the number of transitions in S list plus 1.

But the transitions in S list are the number of consecutive pairs in S list (non-x runs) with different genres.

But in the original runs list, consecutive runs are different genres. So when two non-x runs are consecutive in the original list, their genres are different. Thus, consecutive pairs in the S list that are consecutive in the original list will have different genres and contribute to transitions.

But when two non-x runs are not consecutive in the original list (i.e., separated by x runs), their genres may be same or different.

Thus, the transitions in the S list are:

- For each consecutive pair in S list that are consecutive in the original list: their genres are different, so contribute 1.

- For each consecutive pair in S list that are not consecutive in the original list: their genres may be same or different.

So the total transitions is:

(number of consecutive pairs in S list that are consecutive in the original list) → each contributes 1.

Plus the number of consecutive pairs in S list that are not consecutive in the original list, but have different genres.

But this seems complicated.

But perhaps the number of transitions in S list can be expressed as (number of transitions in the original list) - transitions that involve x runs + transitions introduced by merging x runs.

But this is not clear.

Alternative Idea:

The transitions in the original list is (m-1), where m is the number of runs.

When we remove x's runs, the transitions in the S list is:

(number of transitions between non-x runs in the original list) + transitions introduced by merging.

Wait, no.

For example, original transitions are between all consecutive runs. When we remove x's runs, the transitions between non-x runs are preserved if they were consecutive in the original list. Otherwise, new transitions are added between non-x runs that are now consecutive in S list.

But this seems difficult to model.

At this point, I'm stuck and think I need to look for an alternative approach.

Let's think of the problem from the perspective of the merged runs after removing x.

The merged runs after removing x can be formed by:

1. Remove all x runs from the original runs list.

2. Merge consecutive runs of the same genre in the resulting list.

The number of merged runs is then the number of transitions in the filtered list plus 1.

Thus, the stress count is (merged_runs_count - 1).

But how to compute merged_runs_count.

The merged_runs_count is equal to the number of times the genre changes in the filtered list.

For example, if the filtered list is [A, B, B, A], the merged runs are [A, B, A], so merged_runs_count is 3, stress count is 2.

Thus, merged_runs_count is the number of genre changes in the filtered list plus 1.

But how to compute this.

The genre changes in the filtered list can be computed as the number of pairs of consecutive elements in the filtered list that are different.

But the filtered list is formed by removing x's from the original list.

But the original list is a list of runs. So the filtered list is a list of runs (non-x) in order. Consecutive runs in the filtered list may have the same genre (if they were separated by x runs in the original list).

Thus, the genre changes in the filtered list is the number of consecutive pairs in the filtered list that are different.

But how to compute this.

But for each x, the filtered list is the original list with x runs removed. So the filtered list is a list of runs (non-x) in order. Consecutive runs in this list may have the same or different genres.

Thus, the number of genre changes in the filtered list is the number of consecutive pairs in the filtered list that are different.

So, the merged_runs_count is (genre_changes_in_filtered_list + 1).

Thus, the stress count is (genre_changes_in_filtered_list + 1 - 1) = genre_changes_in_filtered_list.

Thus, the stress count for x is equal to the number of genre changes in the filtered list.

But how to compute this.

The filtered list is formed by the non-x runs in the original runs list. So the genre changes in the filtered list is:

(number of consecutive pairs in the filtered list) - number of consecutive pairs in the filtered list that have the same genre.

The number of consecutive pairs in the filtered list is (number of non-x runs - 1).

Thus, genre_changes = (number of non-x runs - 1) - same_pairs.

But same_pairs is the number of consecutive pairs in the filtered list with the same genre.

Thus, stress_count = (number of non-x runs - 1) - same_pairs.

But how to compute this.

But number of non-x runs is (total_runs - count_runs[x]).

So stress_count = (total_runs - count_runs[x] -1) - same_pairs.

But to compute same_pairs, which is the number of consecutive pairs in the filtered list with same genre.

But how to compute same_pairs.

This brings us back to the same problem.

Thus, the crux of the problem is to compute same_pairs for each x efficiently.

At this point, I think the only feasible approach is to precompute for each x the same_pairs as follows:

For each x:

1. Collect all the non-x runs in order.

2. Iterate through this list and count the number of consecutive pairs with same genre.

This would take O(m) time per x, where m is the number of non-x runs.

But for k=1e5, this is O(nk) time, which is not feasible.

Thus, this approach is not feasible.

But given the time constraints of the problem (2 seconds), perhaps we can find a way to represent the data in a way that allows for O(n) or O(n log n) time.

Alternative Idea: Realize that for x to be a candidate, it must be present in the runs list.

But each x is present at least once.

So for each x in the runs list (which is O(n) x's), we can process them.

But if k is up to 1e5, but the runs list contains O(n) x's, then for n=1e5, this is O(n) x's.

But this is not necessarily the case. For example, if x is a genre that appears multiple times in the runs list.

But the problem says that each genre from 1 to k is present at least once.

But the runs list is a list of genres with consecutive runs different. So each genre appears at least once in the runs list.

So the number of x's to process is exactly k, which can be up to 1e5.

Thus, even if we process each x in the runs list, it's O(k) x's.

Thus, the time complexity is O(k * m), where m is the average number of non-x runs.

But for k=1e5 and m=1e5, this is 1e10 operations, which is too slow.

Thus, I need to find a way to compute the same_pairs for all x in O(n) time.

Another Idea:

For each pair of consecutive runs in the original list, if they are both not x, then they contribute 1 to the transitions in the filtered list.

But consecutive runs in the original list are of different genres. So, if two consecutive runs are both not x, then their genres are different, so they contribute 1 to the transitions.

For pairs of non-x runs that are not consecutive in the original list but are consecutive in the filtered list, their genres may be same or different.

Thus, the stress count for x can be computed as:

stress_count[x] = (number of consecutive non-x pairs in the original list) + (number of non-consecutive pairs in the filtered list that are different) - (number of non-consecutive pairs in the filtered list that are same).

But this is not helpful.

Alternatively, the stress count is:

stress_count[x] = (number of transitions in the original list) - (number of transitions involving x) + (number of new transitions created by removing x runs).

But I'm not sure.

Another Idea: Let's precompute for each x the number of transitions in the original list that involve x. Then, when we remove x, these transitions are removed. But new transitions may be added between non-x runs that were separated by x.

The number of new transitions is equal to the number of pairs of non-x runs (i,j) that are now consecutive in the filtered list, and their genres are different.

Thus, stress_count[x] = (original_transitions - transitions_involving_x) + new_transitions.

But how to compute this.

Original_transitions is (m-1), where m is the number of runs.

transitions_involving_x is the number of transitions in the original list where at least one of the two runs is x.

For example, if the original list has a transition from x to y, then this transition is removed when x is excluded.

Thus, transitions_involving_x = number of transitions where either run is x.

This can be computed by iterating through the transitions and counting those involving x.

Then, new_transitions is the number of pairs of non-x runs (i,j) that are consecutive in the filtered list and have different genres.

These pairs were not consecutive in the original list.

For example, if the original list has runs A, X, B, then in the filtered list, A and B are consecutive. If A and B are different, then this contributes 1 to new_transitions.

But A and B are different, so this is a new transition.

Thus, new_transitions is the number of pairs of non-x runs (i,j) that are consecutive in the filtered list and have different genres.

But how to compute new_transitions.

The number of such pairs is equal to the number of pairs of non-x runs that are consecutive in the filtered list and have different genres.

But how to compute this.

The number of consecutive pairs in the filtered list is (s -1), where s is the number of non-x runs.

The number of consecutive pairs with same genre is same_pairs.

Thus, new_transitions = (s - 1) - same_pairs - original_consecutive_pairs_not_x.

Where original_consecutive_pairs_not_x is the number of consecutive pairs in the original list that are both not x (they are counted in the original transitions).

But this is getting complicated.

Let's think again:

original_transitions = m - 1.

When x is removed, transitions_involving_x is the number of transitions in the original list where either run is x.

new_transitions is the number of pairs of non-x runs (i,j) that are consecutive in the filtered list and have different genres, and were not consecutive in the original list.

Thus:

stress_count[x] = (original_transitions - transitions_involving_x) + new_transitions.

But how to compute new_transitions.

The filtered list's transitions is (original transitions not involving x) + new_transitions.

But original transitions not involving x are the transitions between two non-x runs that are consecutive in the original list. These transitions are preserved in the filtered list.

Thus:

original_transitions_not_involving_x = (number of consecutive pairs of non-x runs in the original list).

Because each such pair contributes a transition in the original list, and after removing x, they remain consecutive and their transition is preserved.

So:

stress_count[x] = original_transitions_not_involving_x + new_transitions.

But original_transitions_not_involving_x is the number of consecutive pairs in the original list that are both not x.

Thus, original_transitions_not_involving_x can be computed by iterating through the original transitions and counting those where both runs are not x.

new_transitions is the number of consecutive pairs in the filtered list that are not consecutive in the original list and have different genres.

But how to compute new_transitions.

The new_transitions can be computed as the number of consecutive pairs in the filtered list minus the original_consecutive_pairs_not_x minus the number of same_pairs.

Because:

consecutive_pairs_in_filtered_list = s-1.

original_consecutive_pairs_not_x = number of consecutive pairs in original list that are both not x.

Thus, new_consecutive_pairs_in_filtered_list = (s-1) - original_consecutive_pairs_not_x.

Each of these new pairs contributes a transition if their genres are different.

Thus:

new_transitions = new_consecutive_pairs_in_filtered_list - same_pairs.

But new_consecutive_pairs_in_filtered_list is (s-1) - original_consecutive_pairs_not_x.

Thus:

stress_count[x] = original_transitions_not_involving_x + ( (s-1 - original_consecutive_pairs_not_x) - same_pairs )

But original_transitions_not_involving_x = original_consecutive_pairs_not_x.

Because each consecutive pair in the original list that are both not x contributes a transition.

Thus:

stress_count[x] = original_consecutive_pairs_not_x + ( (s-1 - original_consecutive_pairs_not_x) - same_pairs )

Simplify:

stress_count[x] = original_consecutive_pairs_not_x + (s-1 - original_consecutive_pairs_not_x) - same_pairs

= (s-1) - same_pairs.

Which brings us back to the original formula: stress_count[x] = (s-1) - same_pairs.

Thus, we are back to the same problem of needing to compute same_pairs for x.

But this doesn't help.

At this point, I'm stuck and think that the only feasible way to proceed is to find a way to compute same_pairs for all x in O(n) time.

Another Idea: same_pairs for x is the number of times two non-x runs are consecutive in the filtered list and have the same genre.

But since the original runs are consecutive with different genres, two non-x runs that are consecutive in the original list must have different genres. Thus, same_pairs can only come from pairs of non-x runs that are not consecutive in the original list.

Thus, same_pairs is the number of pairs of non-x runs (i,j) that are consecutive in the filtered list (i.e., separated by x runs in the original list) and have the same genre.

Thus, for each x, same_pairs is the number of pairs of non-x runs (i,j) such that:

1. All runs between i and j are x.

2. i's genre == j's genre.

Thus, the same_pairs for x is the number of such pairs.

Now, how to compute this for all x efficiently.

Perhaps the solution is to iterate through all possible pairs of non-x runs and track for which x they contribute.

But with n up to 1e5, this is O(n^2), which is not feasible.

But perhaps we can find a way to count for each x the number of pairs of non-x runs that are separated by x and have the same genre.

An alternative Idea: For each run i, track the next run j where runs[j] is the same as runs[i], and all runs between i and j are x. For each such j, increment same_pairs[x] by 1.

But how to find such j's.

But this again requires O(n^2) time.

At this point, I think that the problem requires an approach that I'm not seeing, and perhaps the correct solution is to process each x in O(1) time after some preprocessing.

Another Idea: For each x, the same_pairs is equal to the number of times x appears in between two runs of the same genre.

But how.

For example, if we have a run of genre g, followed by one or more x runs, followed by a run of genre g, then x is in between, and this contributes 1 to same_pairs[x].

Thus, the same_pairs[x] is the number of such patterns.

Thus, the approach is to count for each x, the number of times x runs appear between two runs of the same genre.

So, for each x, iterate through the runs list and count the number of times a run of x is between two runs of the same genre.

But how.

For example, if we have runs: g, x, x, g → this contributes 2 to same_pairs[x] (since x appears between the two g's).

But the same_pairs[x] is 1 in this case because the two g's are consecutive in the filtered list and contribute 1 same_pair.

Wait, no. The same_pairs[x] is 1 in this example.

But according to this approach, each x run between two g's contributes 1. But this is not correct.

Thus, this approach is incorrect.

But perhaps, the number of times x runs are between two g runs is not the same as same_pairs[x], but the presence of any x runs between two g runs contributes 1 to same_pairs[x], regardless of how many x runs are there.

Thus, same_pairs[x] is the number of pairs of g runs (for any g) that are separated by x runs.

But this is the same as the previous idea.

Thus, for each x, we need to count the number of pairs of runs of the same genre g (g != x) such that between them are only x runs.

So, for each x, same_pairs[x] is the number of such pairs.

Thus, the approach is:

- For each x, same_pairs[x] is the number of pairs of runs (i, j) where i < j, runs[i].genre == runs[j].genre != x, and all runs between i and j are x.

The challenge is to find all such pairs efficiently.

Thus, the solution is to precompute for each genre g, the list of indices where g occurs. Then, for each pair of consecutive indices in this list, check if all runs between them are x for some x. If yes, then increment same_pairs[x] by 1.

But this is O(m) per genre g, where m is the number of runs of g.

But with genres up to k=1e5, this is O(n) time in total.

For example, for each g, process all pairs of consecutive runs of g and check if the runs between are x.

But how.

Let's see:

For each genre g, collect the list of positions where it occurs in the runs list. Let's call this list pos_g.

For each pair of consecutive positions i and j in pos_g:

- Check if all runs between i and j are of the same genre x.

- If yes, then increment same_pairs[x] by 1.

This is O(m) for each g, and summing over all g, O(n) time in total.

Because each run belongs to exactly one genre, and each pair of consecutive positions is processed once.

Thus, this is feasible.

Let's see why:

For example, if a pair of consecutive runs of g is separated by x runs, then this pair contributes 1 to same_pairs[x].

For example, pos_g is [0, 3, 5]. For i=0 and j=3, check if runs 1 and 2 are x. If runs 1 and 2 are x, then x is the genre of those runs. So for this pair, x is determined as the genre of runs 1 and 2. If they are all x, then same_pairs[x] +=1.

But if between i and j there are runs of different genres, then this pair does not contribute to any x.

Thus, for each pair of consecutive runs of g, we can check if all runs between them are the same genre x (and x != g). If yes, then same_pairs[x] +=1.

This can be done by checking if the set of genres between i and j is a singleton and not g.

Thus, the steps are:

For each genre g in 1..k:

   pos_g = list of indices in runs list where genre is g.

   for i from 0 to len(pos_g)-2:

       j = i+1

       start = pos_g[i] + 1

       end = pos_g[j] - 1

       if start > end:

           continue  # no runs between them

       # check if all runs from start to end are of the same genre x, and x != g

       first_genre = runs[start].genre

       if first_genre == g:

           continue

       # check if all other runs between start and end have genre first_genre

       valid = True

       for k in start+1 to end:

           if runs[k].genre != first_genre:

               valid = False

               break

       if valid:

           x = first_genre

           same_pairs[x] +=1

This approach iterates over each pair of consecutive runs of g and checks if the runs between are all x.

This is O(n) time in total because for each run, it's part of a genre g and has a certain number of consecutive pairs. The total number of pairs across all genres is O(n), since for a genre with m runs, there are m-1 consecutive pairs.

For each pair, we check the runs between them. However, checking the runs between can take O(1) time if we can quickly find the genre of the first run between them and check if all others are the same.

Wait, no. If there are m runs between i and j, this check is O(m) time, which can be O(n) in the worst case. For example, if two runs of g are at positions 0 and n-1, and the runs between are all x, then this would take O(n) time for that pair.

Thus, this approach is O(n^2) in the worst case.

But this is not feasible.

Alternative Idea: For each pair of consecutive runs of g, check if the runs between them are all the same genre x. This can be done by checking if the first run between them is x, and the last run between them is x, and the first run between is x.

But this is not sufficient.

Another Idea: For a pair of consecutive runs of g at positions i and j (i < j), the runs between are from i+1 to j-1.

If there are no runs between i and j (i+1 == j), then there's nothing to do.

Otherwise, check if all runs between i and j have the same genre x. To do this quickly, we can check if the first run between is x and the last run between is x, and all other runs between are x.

But this is not sufficient.

But in the runs list, consecutive runs are different genres. So if there are multiple runs between i and j, they must alternate between different genres.

Wait, no. The runs between i and j can have any genres, as long as consecutive runs are different.

So between i and j, the runs can be a sequence like x, y, x, y, x.

But this would not be all x.

Thus, the only way for all runs between i and j to be x is if there is a single run of x between them, or multiple runs of x with no other genres.

But since consecutive runs are different, multiple runs of x would alternate with other genres, so it's impossible to have multiple runs of x between i and j.

Wait, no. Because consecutive runs are different genres. So if between i and j there are multiple runs of x, that's impossible. Because consecutive runs are different.

Thus, between i and j, all runs must be x if and only if there is a single run of x between them.

Because if there were two runs between i and j, they would be different genres, and thus one of them is not x.

Thus, for two runs of g to be separated by x runs, there must be exactly one run of x between them.

Thus, the pair of consecutive g runs must be separated by a single x run.

Thus, same_pairs[x] is the number of pairs of consecutive g runs separated by a single x run.

Thus, the problem reduces to counting for each x, the number of pairs of consecutive g runs (for any g) that are separated by a single x run.

Thus, the solution is to iterate through all consecutive pairs of runs in the original list. For each pair (i, i+1), check if the previous run is g and the next run is g, and the current run is x.

For example:

If runs[i] is x, and runs[i-1] is g, runs[i+1] is g, then this contributes 1 to same_pairs[x].

Thus, the approach is:

- Iterate through the runs list from index 1 to m-2 (where m is the number of runs).

   For each run i:

       if runs[i-1].genre == runs[i+1].genre and runs[i].genre == x, then:

           same_pairs[x] +=1

This way, for each run i of x that is between two runs of g, we increment same_pairs[x] by 1.

This is O(m) time.

Thus, this is the solution.

Thus, the steps are:

1. Preprocess the runs list.

2. For each x, initialize same_pairs[x] to 0.

3. Iterate through the runs list from index 1 to m-2:

   a. If runs[i-1].genre == runs[i+1].genre and runs[i].genre == x, then:

       same_pairs[x] +=1

4. For each x, compute stress_count[x] = (s -1) - same_pairs[x], where s is the number of non-x runs.

5. Find the x with minimum stress_count. If tie, choose the smallest x.

This is O(m) time, which is O(n) since m is up to n.

This is the key insight.

Let's test this with the first example:

Example 1:

Input:

10 3

1 1 2 3 2 3 3 1 1 3

The runs list is:

[1, 2, 3, 2, 3, 1, 3]

So the runs list has indices 0 to 6.

Iterate from i=1 to 5:

i=1: runs[0]=1, runs[1]=2, runs[2]=3 → runs[i-1] is 1, runs[i+1] is 3 → genres 1 and 3 are different. So no.

i=2: runs[1]=2, runs[2]=3, runs[3]=2. → runs[i-1] is 2, runs[i+1] is 2. So runs[i] is 3 (x=3). So same_pairs[3] +=1.

i=3: runs[2]=3, runs[3]=2, runs[4]=3. → runs[i-1] is 3, runs[i+1] is 3. So runs[i] is 2 (x=2). same_pairs[2] +=1.

i=4: runs[3]=2, runs[4]=3, runs[5]=1. → genres 2 and 1 different. No.

i=5: runs[4]=3, runs[5]=1, runs[6]=3. → genres 3 and 3 are same. runs[i] is 1. So x=1. same_pairs[1] +=1.

So after processing:

same_pairs[3] =1, same_pairs[2] =1, same_pairs[1]=1.

For x=1:

s = number of non-1 runs: in runs list, the runs not 1 are 2,3,2,3,3 → count is 5. So s=5.

stress_count[1] = (5-1) - 1 =4-1=3.

For x=2:

s = number of non-2 runs: 1,3,3,1,3 → count is5. stress_count[2] =5-1 -1=4-1=3.

For x=3:

s is the number of non-3 runs: runs are 1,2,2,1 → count is4. stress_count[3] =4-1 -1=3-1=2.

Which matches the first example's output.

Thus, this approach is correct.

Thus, the steps are:

- Create the runs list.

- For each run between 1 and m-2, check if it is a single x run between two same genres.

- Compute same_pairs[x] for each x.

- For each x, compute s = total_runs - count_runs[x], and stress_count = (s-1) - same_pairs[x].

- Find the x with the minimum stress_count, and the smallest x if tied.

Thus, the code can be implemented as follows:

Read n and k.

Read the array a.

Generate the runs list.

Compute total_runs = len(runs).

Compute count_runs: a dictionary where count_runs[x] is the number of times x appears in the runs list.

Initialize same_pairs = defaultdict(int).

Iterate from i=1 to len(runs)-2:

   if runs[i-1] == runs[i+1] and runs[i-1] != runs[i]:

       x = runs[i]

       same_pairs[x] +=1

For each x in 1..k:

   s = total_runs - count_runs.get(x,0)

   if s ==0:

       # but since each x is present at least once, s can't be zero.

   stress_count = (s-1) - same_pairs.get(x, 0)

   track the minimum stress_count and x.

Choose the x with the minimum stress_count. If tie, pick the smallest.

Thus, this is O(n) time.

Now, the code.

First, generate the runs list.

Then, compute count_runs.

Then, compute same_pairs.

Then, iterate over all x from 1 to k.

So the code:

Read n, k.

a = list(map(int, input().split())).

Generate runs list.

prev = a[0]

runs = [prev]

for num in a[1:]:

   if num != prev:

       runs.append(num)

       prev = num

Then, count_runs can be a dictionary.

count_runs = {}

for num in runs:

   count_runs[num] = count_runs.get(num,0) +1

Then, same_pairs:

same_pairs = defaultdict(int)

for i in range(1, len(runs)-1):

   if runs[i-1] == runs[i+1] and runs[i-1] != runs[i]:

       x = runs[i]

       same_pairs[x] +=1

Then, for each x in 1..k:

s = len(runs) - count_runs.get(x,0)

stress = (s-1) - same_pairs.get(x,0)

track the x with minimal stress, and smallest in case of ties.

Thus, the code is manageable.

Testing against sample input 1.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))
    
    # Generate runs list
    runs = []
    prev = a[0]
    runs.append(prev)
    for num in a[1:]:
        if num != prev:
            runs.append(num)
            prev = num
    
    m = len(runs)
    count_runs = defaultdict(int)
    for num in runs:
        count_runs[num] += 1
    
    same_pairs = defaultdict(int)
    for i in range(1, m - 1):
        if runs[i - 1] == runs[i + 1] and runs[i] != runs[i - 1]:
            x = runs[i]
            same_pairs[x] += 1
    
    min_stress = float('inf')
    best_x = k + 1  # start with a value higher than possible
    
    for x in range(1, k + 1):
        s = m - count_runs[x]
        if s == 0:
            # This x cannot be chosen since each genre appears at least once, but s=0 would mean all runs are x
            continue  # but the problem states each x is present at least once, so s >=1
        stress = (s - 1) - same_pairs.get(x, 0)
        if stress < min_stress or (stress == min_stress and x < best_x):
            min_stress = stress
            best_x = x
    
    print(best_x, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 3
3 1 3 2 3 1 2
""",
            "output": \
"""\
1
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Thus, this approach is correct and efficient.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    # Generate runs list
    runs = []
    prev = a[0]
    runs.append(prev)
    for num in a[1:]:
        if num != prev:
            runs.append(num)
            prev = num
    
    m = len(runs)
    count_runs = defaultdict(int)
    for num in runs:
        count_runs[num] += 1
    
    same_pairs = defaultdict(int)
    for i in range(1, m - 1):
        if runs[i - 1] == runs[i + 1] and runs[i] != runs[i - 1]:
            x = runs[i]
            same_pairs[x] += 1
    
    min_stress = float('inf')
    best_x = k + 1  # start with a value higher than possible
    
    for x in range(1, k + 1):
        s = m - count_runs[x]
        if s == 0:
            # This x cannot be chosen since each genre appears at least once, but s=0 would mean all runs are x
            continue  # but the problem states each x is present at least once, so s >=1
        stress = (s - 1) - same_pairs.get(x, 0)
        if stress < min_stress or (stress == min_stress and x < best_x):
            min_stress = stress
            best_x = x
    
    print(best_x)

if __name__ == "__main__":
    main()
```
