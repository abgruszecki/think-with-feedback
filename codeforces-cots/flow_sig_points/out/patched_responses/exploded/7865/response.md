<think>
Okay, let's see. The problem is to find the number of subrectangles in a matrix c that have area exactly k and consist entirely of ones. The matrix c is formed by multiplying each element of array a (which is 0 or 1) with each element of array b. So each cell c_ij is a_i * b_j. 

First, I need to think about how the matrix c looks. Since c_ij is 1 only when both a_i and b_j are 1. So the matrix will have 1s only in rows where a_i is 1 and columns where b_j is 1. So the 1s in c form a grid where the rows correspond to the 1s in a and the columns correspond to the 1s in b. 

But how to count the subrectangles of area k that are all ones. Since all the 1s in the matrix are contiguous in some way. Wait, no. Because the matrix is the product of a and b, the 1s in c form a grid where the rows with a_i=1 contribute to entire rows of 1s in the corresponding columns where b_j=1. Wait, for example, if a has 1s in positions 0, 2, 3 and b has 1s in positions 1,2, then the c matrix will have 1s in those rows (where a is 1) and those columns (where b is 1). So the 1s in c form a grid where the rows are the positions where a has 1s and the columns are where b has 1s. So the 1s are in a rectangle of size (number of 1s in a) × (number of 1s in b). But the problem is to find all possible subrectangles of c that have area exactly k and all 1s. 

But any subrectangle in c that is all 1s must be entirely contained within this block of 1s. Because outside of that, the cells are 0. So the problem reduces to finding all possible rectangles of area k within a grid that is a contiguous block of 1s. Wait, no. Because the 1s in c are in the form where for each row i in a that is 1, and each column j in b that is 1, the cell is 1. But the rows in a that are 1 might not be consecutive. Similarly for the columns in b. For example, a could be [1,0,1], so the rows where a is 1 are row 0 and row 2. Then, in matrix c, the rows that are 1s (from a's perspective) are rows 0 and 2, but not 1. So the 1s in c are in those rows and the columns where b is 1. So the structure of c's 1s is a grid where the rows are the 1s in a (possibly non-consecutive) and the columns are the 1s in b (also possibly non-consecutive). 

But for a subrectangle to be all 1s in c, it's necessary that all the rows in that subrectangle have a_i=1 and all the columns in that subrectangle have b_j=1. Because if any row in the subrectangle has a_i=0, then all the cells in that row would be 0. Similarly for columns. So the problem reduces to: find all pairs of a range of rows in a where all a_i are 1, and a range of columns in b where all b_j are 1, such that the product of the number of rows and columns (the area) is exactly k.

Wait, no. Because a subrectangle in c is determined by selecting consecutive rows of the original matrix and consecutive columns. So even if the rows in the original a are not consecutive 1s, but in the matrix c, those rows are not consecutive. For example, a is [1,0,1], so the rows in c are rows 0 and 2 (assuming 0-based or 1-based? The problem uses 1-based, like x_1 and x_2). So when you select a subrectangle in c that spans rows x1 to x2, those rows in the original matrix may not be consecutive. But in the matrix c, those rows may or may not be consecutive. But in order for all the cells in that subrectangle to be 1s, all the rows in x1..x2 must have a_i=1, and all the columns in y1..y2 must have b_j=1. Because if any a_i in x1..x2 is 0, then all the cells in that row of c would be 0. So the entire subrectangle must be in a region where all the selected rows in a are 1 and all the selected columns in b are 1. 

Therefore, the problem can be broken down into:

The number of possible subrectangles of area k in c that are all 1s is equal to the sum over all possible pairs (h, w) where h * w = k, of (the number of consecutive sequences of h rows in a that are all 1s) multiplied by (the number of consecutive sequences of w columns in b that are all 1s). 

So the approach is to:

1. For array a, compute all possible lengths of consecutive 1s. For example, in a = [1,1,0,1], the consecutive 1s sequences are of lengths 2 and 1. Then, for each possible length l, count how many possible sequences of h consecutive 1s are contained in all sequences of consecutive 1s. For example, a consecutive run of 3 1s contributes (3 - h + 1) sequences for h ≤3. 

2. Do the same for array b. 

Then, for each possible pair (h, w) where h * w = k, multiply the count of h-length sequences in a by the count of w-length sequences in b, and sum all these products. 

So the key steps are:

- For a and b, precompute the counts of all possible consecutive runs of 1s, and for each possible h, compute how many possible h-length sequences there are. 

So the plan is:

- Process array a to find all runs of consecutive 1s. For each run of length l, add (l - h + 1) to the count for h, for each possible h <= l. 

Similarly for array b. 

Then, for all factors (h, w) of k where h * w =k, compute the product of the counts from a and b for h and w respectively, and sum all these products. 

So the steps:

1. Precompute for a the frequency array cnt_a, where cnt_a[h] is the total number of consecutive sequences of h 1s in a. 

2. Precompute for b the frequency array cnt_b, where cnt_b[w] is the total number of consecutive sequences of w 1s in b. 

3. For all pairs (h, w) such that h * w =k, add cnt_a[h] * cnt_b[w] to the result. 

Now, the problem is to compute cnt_a and cnt_b efficiently, given that n and m can be up to 4e4, which is manageable. 

So how to compute cnt_a:

Loop through array a, track the current length of consecutive 1s. For each element, if it's 1, increment the current length. Otherwise, process the current run. For each run length l, for each possible h from 1 to l, we add (l - h +1) to cnt_a[h]. But if l is large (like up to 4e4), and we have to loop from 1 to l for each run, this would be O(total runs * l). But for a run of length l, the sum for h from 1 to l is (l*(l+1))/2. However, if l is up to 4e4 and there are 4e4 runs, this would be O(4e8) operations, which is way too slow. 

So that approach is not feasible. Therefore, we need a smarter way to compute cnt_a and cnt_b. 

Alternative approach: For each run of length l, the contribution to cnt_a is for h from 1 to l: (l - h +1) = sum_{h=1}^l (l -h +1) = sum_{x=1}^l x} = l*(l+1)/2. But we need to count for each possible h, how many times h appears. So for a run of length l, the number of times h appears is (l - h +1) for h <= l. So for each h in 1..l, add (l-h+1) to cnt_a[h]. 

But if l can be up to 4e4, and the number of runs is O(4e4), then the total operations would be O(4e4 * 4e4) = 1.6e9, which is way too slow. 

So we need a way to compute this more efficiently. 

An optimized way is to note that for a run of length l, the contribution to h=1 is l, to h=2 is l-1, ..., to h=l is 1. So for each h from 1 to l, we add (l -h +1) to cnt_a[h]. 

But how to compute this efficiently for all possible h. 

Alternatively, for each run of length l, we can increment a frequency array for each possible h in 1..l by (l -h +1). But this is O(l) per run, which is not feasible for large l. 

So we need a mathematical approach. 

Let's consider the total contribution for all h in 1..l. For each run of l, the number of times h occurs as a possible sub-run is (l - h + 1). So for all h ≤ l, (l - h +1) is added. 

But how can we compute this in O(1) per run? 

We can model this as for each run of length l, we can compute for each h from 1 to l, the term (l -h +1) and add it to cnt_a[h]. 

But this is O(l) per run, which is not feasible. 

Alternative idea: precompute for all possible h, the number of runs that are >=h. Then, for each h, the total contribution from all runs is sum over all runs of max(0, run_length - h +1). 

So for example, if a run is of length l, then for h in 1..l, it contributes (l -h +1) to cnt_a[h]. 

So the total cnt_a[h] is sum over all runs (max(0, l_i - h +1)), where l_i is the length of the i-th run. 

So if we can find for each h, the sum of (l_i -h +1) for all runs where l_i >=h. 

But how to compute this efficiently for all h? 

The problem is that h can be up to 4e4 (since n is up to 4e4). 

So for h in 1 to max_l (max_l being the maximum run length in a), we need to compute sum (l_i -h +1) for all l_i >=h. 

But even for h up to 4e4, this can be done by first collecting all run lengths, then for each h, iterate through all runs and sum (l_i -h +1) if l_i >=h. But this is O( (number of runs) * max_h ), which again is not feasible for large runs. 

Alternative approach: 

Let’s collect all the run lengths in a list for a and b. Then, for each possible h, compute the sum for all runs in a where run_length >=h of (run_length - h +1). Similarly for b. 

But even with runs stored as a list, the time to compute this sum for all h is O(R) per h, where R is the number of runs. Since h can be up to 4e4, this is O(R*4e4) which is up to 4e4 *4e4=1.6e9 operations. That's way too slow. 

We need a way to compute for each possible h, the sum over all runs of (max(0, l_i - h +1)). 

An efficient way is to sort the run lengths and then for each h, compute the sum using prefix sums and binary search. 

Let's think. Suppose we have all the run lengths sorted in non-decreasing order. For a given h, we can find the first index where l_i >=h. All runs from that index onwards have l_i >=h. For each such l_i, the contribution is (l_i -h +1). 

So for the sorted list, we can compute for each h the sum as:

sum_{i=index}^{n_runs-1} (l_i -h +1) = sum_{i=index}^{n_runs-1} (l_i +1 -h) = (sum (l_i +1) for i >=index) - h * (number of runs from index onwards). 

So if we have the runs sorted, and have a prefix sum array for (l_i +1) and a prefix count array, we can compute this sum for each h in O(log n_runs) time. 

So here's the plan:

For array a:

1. Collect all runs of consecutive 1s. Let's call this list runs_a. Similarly for runs_b. 

2. Sort runs_a in non-decreasing order. 

3. Compute a prefix sum array for (l_i +1), sorted in ascending order. 

Wait, no. For runs sorted in ascending order, the prefix sum of (l_i +1) from the end. Wait, since the runs are sorted in non-decreasing order, when we find the first index where l_i >=h, all the runs after that index (including) will have l_i >=h. So the sum of (l_i - h +1) for these runs is sum(l_i - h +1) = sum(l_i +1) - h * count. 

But if the runs are sorted, for a given h, the sum of (l_i +1) for runs >=h is sum(l_i +1 for l_i >=h), and the count is the number of such runs. 

So the steps for a:

- Collect runs_a, the list of lengths of consecutive 1s. 

- Sort runs_a in non-decreasing order. 

- Compute a list sorted_runs_a. 

- Precompute a suffix sum array for (l_i +1), and a suffix count array. 

For example, sorted_runs_a is sorted. Then, for each possible h, we can find the first index in sorted_runs_a where l_i >=h. Then, the sum is suffix_sum[index] - h * suffix_count[index], where suffix_sum is the sum of (l_i +1) from index to end, and suffix_count is the number of elements from index to end. 

So precompute for the sorted runs the suffix_sum and suffix_count arrays. 

How to compute these:

sorted_runs = sorted(runs)

suffix_sum = [0]*(len(sorted_runs) + 1)
suffix_count = [0]*(len(sorted_runs) +1)

for i in reversed(range(len(sorted_runs))):
    suffix_sum[i] = suffix_sum[i+1] + (sorted_runs[i] +1)
    suffix_count[i] = suffix_count[i+1] + 1

Then, for a given h, using binary search, find the first index where sorted_runs[i] >=h. Then, sum_contrib = suffix_sum[index] - h * suffix_count[index]

This sum_contrib is the total contribution of all runs in a for that h. 

This approach would allow us to compute cnt_a[h] in O(log R) time, where R is the number of runs. 

Similarly for array b. 

So the steps to compute cnt_a and cnt_b:

For a:

Process the array to get runs of 1s. Sort them. Compute suffix sums and counts. Then, for any h, use binary search to find the index and calculate the sum. 

Similarly for b. 

Once we have these structures, the problem reduces to iterating over all possible pairs (h, w) where h * w =k, and sum the product of the counts from a and b for h and w. 

So the overall steps are:

1. Process a and b to get runs. 

2. Sort the runs. 

3. Precompute suffix sums and counts for the sorted runs. 

4. For each h that divides k, compute w = k/h. 

   For each (h, w) pair where h*w =k, compute the count_a for h and count_b for w, multiply them, and add to the result. 

But how to handle all possible factors (h, w) where h *w =k. 

Note that h can be any divisor of k. So first, we need to find all possible pairs (h, w) where h *w =k, and h <=max_possible_h (which is the maximum run length in a), and w <=max_possible_w (max run length in b). 

But even if h exceeds the max run length in a, then the count_a for h is zero, so that pair contributes nothing. 

So the algorithm is:

Initialize result to 0. 

For each h in the divisors of k:

   w = k / h

   compute count_a for h (using the suffix sum and count arrays for a's runs)

   compute count_b for w (using the suffix sum and count arrays for b's runs)

   add count_a * count_b to result

But to generate all possible divisors h of k:

We need to iterate h from 1 to sqrt(k), and for each h that divides k, add both (h, k/h) and (k/h, h) pairs. But also avoid duplicates when h and k/h are the same. 

So first, generate all possible pairs (h, w) where h*w =k. 

So the steps to generate these pairs:

Initialize a list of pairs. 

For i in 1 to sqrt(k):

   if k % i ==0:

      add (i, k//i)

      if i != k//i:

          add (k//i, i)

So this gives all possible pairs (h, w) such that h*w =k. 

Then, for each pair (h, w), compute the count for h in a and the count for w in b, multiply them and add to the result. 

But for each pair, h can be up to k (if k is a large prime, then h=1 and w=k). 

So for h, we need to check if there are runs in a of at least h, and similarly for w in b. 

But how? The count_a for h is the sum of (l_i -h +1) for all runs l_i >=h. 

But using the precomputed suffix arrays, we can compute this quickly. 

So putting it all together:

The code steps are:

Read n, m, k.

Read array a (as a list of integers).

Read array b (as a list of integers).

Process a to find all runs of 1s. 

Process b to find all runs of 1s. 

Sort the runs of a and compute suffix_sum and suffix_count. 

Same for runs of b. 

Generate all divisors (h, w) pairs where h *w =k. 

For each such pair:

   compute count_a for h: 

      using binary search on sorted_runs_a to find first index >=h. 

      sum_contrib_a = suffix_sum_a[index] - h * suffix_count_a[index]

   compute count_b for w:

      similar, using sorted_runs_b. 

   result += sum_contrib_a * sum_contrib_b

Return result. 

Now, the key steps are:

Processing the runs for a and b. 

Implementing the binary search and suffix sum arrays. 

Generating all divisors of k. 

Edge Cases:

- If k is 0: but according to the problem statement, k can be up to n*m. But in the input constraints, k is >=1, so this is not possible. 

Wait, input constraints for k: 1<=k <=n*m. So k=0 is not possible. 

Another edge case: when there are no 1s in a or b. Then the matrix c is all zeros, so the answer is zero. 

Another case: when k is larger than the maximum possible area (product of the number of 1s in a and 1s in b). For example, if a has 3 1s and b has 4, the maximum area is 12. If k is 13, the answer is zero. 

But the code should handle all these cases automatically. 

Now, the code steps in Python:

First, process the runs. 

To process the runs of 1s in a list:

For example, for a = [1,0,1,1,0,1], the runs are [1, 2, 1]. 

So code for processing runs:

def get_runs(arr):

    runs = []

    current = 0

    for num in arr:

        if num == 1:

            current +=1

        else:

            if current >0:

                runs.append(current)

                current =0

    if current >0:

        runs.append(current)

    return runs

Yes. 

Then, sort the runs. 

Then, compute the suffix sums and counts. 

But in Python, how to handle the suffix sums. 

Once the runs are sorted, for the sorted list:

sorted_runs = sorted(runs)

Then, compute the suffix sums and counts. 

We can create a list of sorted_runs, then for each position i in sorted_runs, compute the sum from i to end of (run +1) and the count. 

But in Python, we can precompute a reversed list and compute the prefix sums. 

Alternatively, iterate from the end. 

For example:

sorted_runs = sorted(runs_a)

n = len(sorted_runs)

suffix_sum = [0]*(n+1)

suffix_count = [0]*(n+1)

for i in reversed(range(n)):

    suffix_sum[i] = suffix_sum[i+1] + (sorted_runs[i] + 1)

    suffix_count[i] = suffix_count[i+1] + 1

Then, for a given h, find the first index in sorted_runs where the run >=h. 

This can be done with bisect_left. For example:

import bisect

index = bisect.bisect_left(sorted_runs, h)

Then, sum_contrib = suffix_sum[index] - h * suffix_count[index]

Similarly for b. 

Now, generate all possible pairs (h, w) where h *w =k. 

To generate all divisors of k:

def get_divisors(k):

    divisors = set()

    for i in range(1, int(k**0.5) +1):

        if k %i ==0:

            divisors.add(i)

            divisors.add(k//i)

    return divisors

But then, for each divisor h, we can generate the pair (h, w) where w =k//h. 

But the set includes all possible h. 

Wait, no. For example, if k=6, the set would be {1,6,2,3}. Then, the possible pairs are (1,6), (6,1), (2,3), (3,2). 

So when generating the pairs, for each h in the set, compute w=k//h, and add the pair (h, w). But this would generate duplicates. For example, h=2, w=3 and h=3, w=2. 

But in the code, when we process all possible h in the set of divisors, and for each h, compute w=k/h, then check if h and w are valid. 

Wait, but the code may process (h, w) and (w, h) as two separate pairs, which is correct. 

Wait, for example, for k=6, the pairs are (1,6), (6,1), (2,3), (3,2). So the code would process each pair, but in each case, h is a divisor. 

But when we generate all possible divisors, each pair (h, w) is considered once, where h is a divisor. But then, the code will generate both (h, w) and (w, h), but only if both h and w are divisors. 

Wait, no. Because if h is a divisor of k, then w =k/h is also a divisor. Because h * w =k, so w must divide k. 

So the set of divisors includes all possible h and their corresponding w. 

But the code as written (using a set) may not generate all possible pairs. Because for each divisor h, the pair (h, w) is considered once, but when processing h and w as separate entries. 

Wait, perhaps the code should generate all possible pairs (h, w) where h*w =k, and h can be any positive integer, and w any positive integer. 

But the set of divisors is exactly all possible h and w. So the code can generate all possible pairs (h, w) by iterating through all divisors h of k and compute w =k//h, but then process each pair once. 

Wait, but for h in the set of divisors, and w =k//h, each pair (h, w) is unique. For example, in k=6, the divisors are 1,2,3,6. So for h=1, w=6; h=6, w=1; h=2, w=3; h=3, w=2. 

So in this case, when the code iterates through all h in divisors, and for each h, compute w=k//h, then all four pairs are considered. 

But the set of divisors is {1,2,3,6}, so for each h in the set, the code would compute w=6/h, which is 6,3,2,1. 

So for h=1, pair (1,6); h=2: (2,3); h=3: (3,2); h=6: (6,1). So all possible pairs are generated. 

So the code can process all possible (h, w) pairs by iterating through all divisors of k. 

But then, the code needs to generate all pairs (h, w) where h and w are positive integers and h *w =k. 

So the code can get all the possible (h, w) pairs by iterating over all h in the set of divisors of k, and for each h, set w=k//h. 

Thus, the code can proceed as follows:

divisors = get_divisors(k)

for h in divisors:

    w = k // h

    compute count_a for h, count_b for w

    add to result

    compute count_a for w, count_b for h

    add to result?

No, wait. Because when h is a divisor, and w is k//h, then (h, w) and (w, h) are two different pairs only when h !=w. But in the set of divisors, when h and w are different, both h and w are present. 

Wait, no. For example, if k=6, the divisors are 1,2,3,6. So when h=1, w=6. But when h=6, w=1. So the code would process both (1,6) and (6,1) pairs. 

But in this case, when we iterate through all divisors h, and for each h, compute w=k//h, then each pair is considered once. 

For example, h=1: (1,6)

h=2: (2,3)

h=3: (3,2)

h=6: (6,1)

But this would process each pair (h,w) once. So the code would process (h, w) and (w, h) as separate pairs. 

But wait, h is in the set of divisors, and for each h, the code processes (h, w). So the code would process all possible pairs. 

Wait, for example, for h=2, the pair is (2,3). For h=3, the pair is (3,2). Both are processed. 

But in that case, the code would add count_a[2] * count_b[3] and count_a[3] * count_b[2]. 

But in reality, these are two distinct pairs and should be considered. 

So the code is correct. 

But in the code, when we generate the set of divisors, we have all possible h, and for each h in the set, we process (h, w), where w =k//h. 

But for example, when k is a square, like k=4, the divisors are 1,2,4. So for h=2, w=2, and this is processed once. 

So this approach correctly generates all possible (h, w) pairs. 

Thus, the code can proceed by iterating over each h in the set of divisors of k, and for each h, process (h, k//h). 

But then, in the code, when h is 2 and w is 3, the code would process (2,3) and when h is 3, it would process (3,2). 

But in the code, the code is adding count_a[h] * count_b[w] for each h and w. 

Thus, the code should generate all possible pairs. 

Wait, but if the code iterates through all h in the divisors and for each h, processes (h, k//h), then when h is 1 and k//h is 6, and when h is 6 and k//h is 1, the code would process both. 

Thus, the code would correctly calculate both (h, w) and (w, h) pairs. 

But when the code is iterating through all divisors, which includes 1,2,3,6, and for each h in that set, it's considering (h, w) where w=k//h. 

So the code is correct. 

Now, code steps:

Implement the get_runs function. 

Implement the code for processing a and b. 

Now, the code in Python:

But the code must read input from stdin, process, and output the result. 

Let's write the code:

Read n, m, k from input.

Read a as a list of integers.

Read b as a list of integers.

Compute runs_a and runs_b. 

Sort the runs and compute the suffix sums and counts. 

Generate the divisors of k. 

For each h in divisors:

   w = k//h

   compute sum_contrib_a for h. 

   compute sum_contrib_b for w. 

   add sum_contrib_a * sum_contrib_b to the result. 

   if h !=w: 

       compute sum_contrib_a for w. 

       compute sum_contrib_b for h. 

       add sum_contrib_a * sum_contrib_b to the result. 

Wait, no. Because for example, in the case where h and w are different, processing (h, w) and (w, h) as separate pairs. 

Wait, but in the code, if we process all h in the set of divisors, then for each h, (h, w) is processed once. However, the code would also process (w, h) when w is in the divisor set, which it is. 

But in this case, when h is processed, and then w is processed, but in that case, the code would process both (h, w) and (w, h). 

But this would lead to double-counting. 

Wait, for example, if k=6, the divisors are 1, 2, 3, 6. 

So for h=1, w=6: the code adds count_a[1] * count_b[6]

For h=6, w=1: code adds count_a[6] * count_b[1]

Which are two separate terms. 

But in reality, (h, w) is (1,6) and (6,1). Are these both valid? 

Yes. Because the code is to find all possible pairs (h, w) where h*w=k. 

But when h=1 and w=6, the code counts the number of runs in a of length >=1 (sum_contrib_a for h=1) multiplied by sum_contrib_b for w=6. 

But sum_contrib_b for w=6 is the number of consecutive runs of 6 in b. 

Similarly, when h=6 and w=1, it's the sum_contrib_a for h=6 multiplied by sum_contrib_b for w=1. 

These are two different terms. 

Thus, the code must process all possible pairs (h, w) where h *w=k, and h and w are positive integers. 

But how to generate all possible pairs (h, w) without duplicates. 

The correct approach is to generate all pairs (h, w) where h <= w, and multiply the count for both (h, w) and (w, h) unless h ==w. 

But perhaps the code as written (processing each divisor h and pair (h, w)) would process each pair twice. 

Because for example, when k=6, the pairs (1,6), (6,1), (2,3), (3,2) are all processed. But in reality, the code would process all of them, leading to correct counts. 

But wait, in the code, when the code iterates through all divisors h, including 1,2,3,6, and for each h, process (h, w) once, then the code will process all four pairs. 

But this would lead to adding count_a[1] * count_b[6] + count_a[6] * count_b[1] + count_a[2] * count_b[3] + count_a[3] * count_b[2]. 

But the correct answer should include all pairs. 

Yes. For example, if h=2 and w=3, it's possible that a has h=2 and b has w=3. But also, a could have w=3 and b have h=2. 

So both terms are needed and are separate. 

Thus, the code should process all possible pairs (h, w) where h *w=k, regardless of order. 

Thus, the code should iterate through all divisors of k, and for each h in the divisors, compute w =k//h and process (h, w). 

But since the set of divisors includes all possible h, then for each (h, w) pair, the code will process each once. 

Thus, the code can be written as follows:

Initialize the result to 0.

Generate all the divisors of k.

For each h in divisors:

    w = k // h

    compute the count for a's runs for h: count_a

    compute the count for b's runs for w: count_b

    result += count_a * count_b

But this would process each pair (h, w) once. For example, for k=6, the divisors are 1,2,3,6. The code would process (1,6), (2,3), (3,2), (6,1). 

Wait, no. Because the divisors are 1,2,3,6. For each h in this list, w =k//h. So:

h=1 → w=6 → (1,6)

h=2 → w=3 → (2,3)

h=3 → w=2 → (3,2)

h=6 → w=1 → (6,1)

Thus, all four pairs are processed, and the code adds count_a[1] * count_b[6] + count_a[2] * count_b[3] + count_a[3] * count_b[2] + count_a[6] * count_b[1]

But this counts all four pairs. So the code is correct. 

Thus, the code should process all divisors, and for each h in the divisors, compute w =k//h and add the product of the counts. 

But how to generate all possible pairs (h, w) where h *w =k. 

The answer is to generate all divisors h of k, and for each h, compute w =k//h, and process the pair (h, w). 

Thus, the code is correct. 

Thus, the code can proceed as follows:

divisors = get_divisors(k)

result =0 

for h in divisors:

    w = k // h 

    # compute count_a for h

    idx_a = bisect.bisect_left(sorted_runs_a, h)

    sum_a = suffix_sum_a[idx_a] - h * suffix_count_a[idx_a]

    # compute count_b for w 

    idx_b = bisect.bisect_left(sorted_runs_b, w)

    sum_b = suffix_sum_b[idx_b] - w * suffix_count_b[idx_b]

    result += sum_a * sum_b 

But this would process each pair (h, w) once, including (h, w) and (w, h) when they are different. 

But wait, in the example of k=6, the code would process h=1 and w=6, then h=2 and w=3, then h=3 and w=2, then h=6 and w=1. 

Which is four separate terms. 

Thus, the code would correctly add all four terms. 

But in reality, the code will generate all possible pairs (h, w) where h *w =k, and for each, add the product of count_a and count_b. 

Thus, the code is correct. 

Now, handling the case where there are no runs in a or b. 

For example, if a is all zeros, then runs_a is empty. So sorted_runs_a is empty. 

In that case, for any h, bisect_left returns 0, suffix_sum_a[0] is 0, and sum_a =0 -h *0 =0. 

Thus, the contribution for that h is zero. 

Similarly for b. 

Thus, the code correctly handles cases where there are no runs. 

Now, code implementation:

The code will need to import bisect. 

But in Python, for bisect_left, we need to import the bisect module. 

Putting it all together:

The code:

import bisect

def get_runs(arr):

    runs = []

    current = 0

    for num in arr:

        if num ==1:

            current +=1

        else:

            if current >0:

                runs.append(current)

                current =0

    if current >0:

        runs.append(current)

    return runs

def compute_suffixes(sorted_runs):

    n = len(sorted_runs)

    suffix_sum = [0]*(n+1)

    suffix_count = [0]*(n+1)

    for i in reversed(range(n)):

        suffix_sum[i] = suffix_sum[i+1] + (sorted_runs[i] +1)

        suffix_count[i] = suffix_count[i+1] +1

    return suffix_sum, suffix_count

def get_divisors(k):

    divisors = set()

    for i in range(1, int(k**0.5)+1):

        if k %i ==0:

            divisors.add(i)

            divisors.add(k//i)

    return divisors

n, m, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

runs_a = get_runs(a)

runs_b = get_runs(b)

sorted_runs_a = sorted(runs_a)

sorted_runs_b = sorted(runs_b)

suffix_sum_a, suffix_count_a = compute_suffixes(sorted_runs_a)

suffix_sum_b, suffix_count_b = compute_suffixes(sorted_runs_b)

divisors = get_divisors(k)

result =0 

for h in divisors:

    w = k // h 

    # compute count_a for h

    idx_a = bisect.bisect_left(sorted_runs_a, h)

    sum_a = suffix_sum_a[idx_a] - h * suffix_count_a[idx_a]

    # compute count_b for w 

    idx_b = bisect.bisect_left(sorted_runs_b, w)

    sum_b = suffix_sum_b[idx_b] - w * suffix_count_b[idx_b]

    result += sum_a * sum_b 

print(result)

Wait, but this code will process each pair (h, w) once. For example, for k=6, the code will process h=1, w=6, and then h=6, w=1. 

But in this case, when h=6, the code will check the runs in a for h=6 and sum_a is computed as the sum of (l_i -6 +1) for all runs in a >=6. sum_b is computed as (l_j -1 +1) for runs in b >=1. 

Thus, the code correctly counts all possible pairs. 

But what about when k is a square? For example, k=4. Then, the divisors are 1,2,4. 

Processing h=1, w=4: sum_a for h=1 and sum_b for w=4. 

Processing h=2, w=2: sum_a for h=2 and sum_b for w=2. 

Processing h=4, w=1: sum_a for h=4 and sum_b for w=1. 

So the code adds all three possibilities. 

But for h=2 and w=2, it's processed once, which is correct. 

Thus, the code should be correct. 

Testing the first sample input:

Sample input 1:

3 3 2

1 0 1

1 1 1

So array a is [1,0,1], which has two runs of 1: lengths 1 and 1. 

Thus, runs_a = [1,1]. sorted_runs_a is [1,1]. 

So for h=1, sum_a is:

For each run >=1: both runs. 

Each contributes (1-1+1)=1. So total sum_a =1 +1=2. 

For h=2: runs >=2: none. sum_a=0. 

For array b, the runs are [3]. sorted_runs_b is [3]. 

For w=2 (since k=2, divisors are 1,2. So for h=1, w=2:

sum_a for h=1 is 2. sum_b for w=2 is (3-2 +1) =2. So 2*2=4. 

For h=2, w=1:

sum_a for h=2 is 0. sum_b for w=1 is (3-1 +1) =3. 0*3=0. 

So total result is 4. Which matches the sample output. 

Thus, the code works for this case. 

The second sample input:

3 5 4

a is [1,1,1], so runs_a is [3]. 

sorted_runs_a is [3]. 

b is [1,1,1,1,1], runs_b is [5]. sorted_runs_b is [5]. 

k=4. 

Divisors are 1,2,4. 

For each h in divisors:

h=1, w=4:

sum_a for h=1 is (3-1+1) =3. sum_b for w=4: 5-4+1=2. So 3*2=6.

h=2, w=2:

sum_a for h=2: 3-2+1=2. sum_b for w=2:5-2+1=4. 2*4=8.

h=4, w=1:

sum_a for h=4: 3-4+1=0. sum_b for w=1:5-1+1=5. 0*5=0.

So total result is 6 +8 +0 =14, which matches the sample. 

Thus, the code is correct. 

Therefore, this should be the correct implementation.
</think>

```python
import bisect

def get_runs(arr):
    runs = []
    current = 0
    for num in arr:
        if num == 1:
            current += 1
        else:
            if current > 0:
                runs.append(current)
                current = 0
    if current > 0:
        runs.append(current)
    return runs

def compute_suffixes(sorted_runs):
    n = len(sorted_runs)
    suffix_sum = [0] * (n + 1)
    suffix_count = [0] * (n + 1)
    for i in reversed(range(n)):
        suffix_sum[i] = suffix_sum[i+1] + (sorted_runs[i] + 1)
        suffix_count[i] = suffix_count[i+1] + 1
    return suffix_sum, suffix_count

def get_divisors(k):
    divisors = set()
    for i in range(1, int(k**0.5) + 1):
        if k % i == 0:
            divisors.add(i)
            divisors.add(k // i)
    return divisors

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

runs_a = get_runs(a)
runs_b = get_runs(b)

sorted_runs_a = sorted(runs_a)
sorted_runs_b = sorted(runs_b)

suffix_sum_a, suffix_count_a = compute_suffixes(sorted_runs_a)
suffix_sum_b, suffix_count_b = compute_suffixes(sorted_runs_b)

divisors = get_divisors(k)

result = 0
for h in divisors:
    w = k // h
    idx_a = bisect.bisect_left(sorted_runs_a, h)
    sum_a = suffix_sum_a[idx_a] - h * suffix_count_a[idx_a]
    idx_b = bisect.bisect_left(sorted_runs_b, w)
    sum_b = suffix_sum_b[idx_b] - w * suffix_count_b[idx_b]
    result += sum_a * sum_b

print(result)
```