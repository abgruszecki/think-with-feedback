<think>
Okay, I need to solve this problem where Alice and Bob have to choose books such that each likes at least k books in the chosen set. The goal is to minimize the total time. Let's think through this.

First, let's understand the problem. Each book can be in four categories based on a_i and b_i:

1. Both like it (a=1, b=1)
2. Only Alice likes it (a=1, b=0)
3. Only Bob likes it (a=0, b=1)
4. Neither likes it (a=0, b=0)

But books in category 4 don't contribute to either's count. So, including them only increases the time without helping. So we can ignore them unless absolutely necessary. Wait, no. Because if a book is in category 4, adding it doesn't help either Alice or Bob. So including it would only add to the time. So the optimal solution will not include any category 4 books. So we can ignore them when considering the problem.

Wait, but what if the required counts are already met by other books, but adding a category 4 book could allow for some other optimization? Like, maybe if a category 4 book has a very small time, but that's impossible. Because adding it would just add time. So no, the optimal solution will not include any category 4 books. So we can filter those out first.

So first, let's split the books into the four categories, then process each category.

Now, the key is to select a subset of books such that the sum of a_i is >=k and sum of b_i >=k. And the sum of t_i is minimized.

So the approach could be:

We need to collect enough books that contribute to Alice's count, Bob's count, and possibly some that contribute to both.

Let's think about the books that are both liked (type 1). These are the most efficient because they count towards both. Then, for the remaining required counts, we take the minimal time books from each of Alice's and Bob's individual lists (types 2 and 3).

So, here's the plan:

1. Separate the books into the three categories (since type 4 is ignored). Let's call them:

- Both: books where a=1 and b=1
- Alice: a=1, b=0
- Bob: a=0, b=1

2. For each possible number of type 1 books we can take, we can compute how much we need from the other categories.

For example, suppose we take x books from type 1. Then, these x books contribute x to both Alice and Bob's counts. The remaining required for Alice is max(k - x, 0), and similarly for Bob. But we need to take enough from the other categories to cover those.

But how do we model this? Maybe the optimal solution is to take a certain number of type 1 books, then take the required from type 2 and type 3.

But how to find the optimal x?

Let me think. Let's say the total number of type 1 books is m. The possible x can be from 0 up to min(m, required). Wait, but x can be up to m, but since each x contributes to both Alice and Bob's counts, taking x of them could allow us to take less from the other categories.

So for each possible x (number of type 1 books we take), the required from Alice's own category (type 2) is max(k - x, 0), and same for Bob's (type 3). But in order to have enough books in type 2 and 3 to cover these.

But how do we choose x to minimize the total time?

The steps could be:

- Pre-sort each category (type1, type2, type3) in ascending order of time, to compute prefix sums.

Then, for each possible x (from 0 up to the maximum possible, which is the minimum between the number of type1 books and the required for either Alice or Bob), we can calculate:

sum_time = sum of x smallest type1 books + sum of (k - x) smallest type2 books (if needed) + sum of (k - x) smallest type3 books (if needed)

But x can't exceed the minimum of the required k for both. Wait, no. For example, if x is 5, and k is 4. Then, after taking 5 type1 books, Alice and Bob each have 5 counts, which meets the required 4. So, for x >=k, then we don't need any type2 or type3 books. But if x is less than k, then for each, we need (k -x) from their respective categories.

Wait, but if x is the number of type1 books we take, then Alice's total is x (from type1) plus the number of type2 books taken. Similarly, Bob's is x plus the number of type3 books taken.

But to meet the conditions, Alice's total must be >=k, so the number of type2 books taken must be >= max(k -x, 0). Similarly for Bob and type3.

But to minimize the total time, for each x, the minimal sum would be the sum of the first x type1 books (sorted by time), plus the sum of first (k -x) type2 books (if possible), plus the sum of first (k -x) type3 books (if possible). But we need to ensure that there are enough books in type2 and type3 to cover (k -x).

But x can range from 0 to the maximum possible value. The maximum possible x is the minimum of:

- the number of type1 books available (since you can't take more than that)
- something else. Wait, for x to be possible, after taking x type1, the required from type2 is (k -x), and from type3 is (k -x). So the type2 and type3 must have at least (k -x) books each.

So for a given x, the required conditions are:

x <= number of type1 books (m1)
type2 count (m2) >= (k -x) if (k -x) >0
type3 count (m3) >= (k -x) if (k -x) >0

So the possible x can range from 0 to the maximum x where:

max(0, k - m2, k -m3) ) <= x <= min(m1, k * 2 - (k - m2) - (k - m3)) ... Hmm, maybe not. Let's think again.

Wait, for x to be a valid candidate, the following must hold:

(k - x) <= m2 --> x >= k - m2 (if k -x >=0)
Similarly, (k -x) <= m3 --> x >=k -m3 (if k -x >=0)
But if x >=k, then (k -x) is <=0, so no need for type2 or type3.

So x can be in the range:

x_min = max(0, k - m2, k - m3)

x_max = min(m1, k) 

Wait, but if x_max is up to m1. Because taking more than k type1 books would not require any type2 or type3. For example, if x is 5, and k is 4. Then x >=k. So (k -x) is -1, which is <=0. So no need for type2 or type3. So in this case, if there are m1 >=k, then x can be up to m1, but if we take x >=k, then the sum would be sum of x type1 books (but since we need only k counts, perhaps taking x >=k may not be optimal. Wait, no. Because each type1 book contributes to both. If x is greater than k, but the sum of x type1 books may be higher than taking x=k and then some type2 and type3. So we need to consider all possible x where x is in the valid range.

Wait, perhaps the optimal x is the minimal possible x that allows the sum of x type1 plus the required (k -x) type2 and type3. But x can't be less than max(0, k - m2, k -m3), because otherwise, type2 or type3 don't have enough books.

Alternatively, x can be any value from 0 up to the maximum possible, but for each x, we can check whether the required (k -x) for both type2 and type3 can be satisfied.

So the approach is:

- Pre-sort the three categories (type1, type2, type3) in ascending order of time.

- Compute prefix sums for each category.

- For type2, the prefix sum array will allow us to quickly get the sum of the first s elements. Similarly for type3 and type1.

Then, for each possible x in the possible x values, compute the total time as follows:

total = prefix1[x] + prefix2[s2] + prefix3[s3], where s2 = max(k - x, 0), s3 = max(k - x, 0)

But we need to check if there are enough type2 and type3 books for s2 and s3.

So for x to be a valid candidate:

If s2 > 0, then the number of type2 books must be >= s2.

If s3 >0, the number of type3 books must be >= s3.

So the valid x must satisfy:

if s2 >0: type2_count >= s2 --> x >= k - s2_available --> x >= k - type2_count (since s2 = k -x)

Wait, s2 is k -x. So if s2 >0, then k -x >0 --> x <k. So in this case, type2_count must be >= (k -x). So x >=k - type2_count.

Similarly, for type3: x >=k - type3_count.

So the x must be >= max( (k - type2_count), (k - type3_count), 0 )

But x can't be larger than the minimum between the type1 count and the possible maximum (like when x >=k).

So the valid x range is x_min <= x <= x_max, where:

x_min = max(0, k - type2_count, k - type3_count)

x_max = min( type1_count, k + ... wait, no. Because x can be up to type1_count, but even if x is larger than k, that's allowed. Because taking x type1 books, which contribute x to both counts, which are >=k if x >=k. So for x >=k, s2 and s3 are zero. So no need for type2 or type3 books. So in that case, the total is prefix1[x].

But if x is larger than k, but type1_count >=x, then that's allowed. But to reach x >=k, but then the sum is sum of x type1 books. But maybe taking x =k is better. Because taking x=5 when k=4 would sum 5 type1 books, but maybe taking x=4 (sum 4) plus some type2 and type3 books (if needed) could be cheaper. So no, for x >=k, the sum is the sum of x type1 books, but if x is larger than k, that's possible. So we need to consider all x in the valid x_min to x_max, where x_max is min( type1_count, any possible x where x >=x_min )

Wait, but when x >=k, then the required for Alice and Bob are met (since x >=k, so Alice's count is x >=k, Bob's is x >=k). So in that case, the sum is just the sum of x type1 books. But x can be any value >=k, but not exceeding the type1_count. So the minimal sum in this case would be the sum of the first k type1 books (since any more would add unnecessary time). Wait, no. For example, if type1 books are sorted in ascending order, the sum of x books is sum of first x. So if x is larger than k, the sum would be sum of first x books, which is larger than sum of first k books. So taking x=k in this case is better than x>k.

Ah, right. So in the case where x >=k, the minimal sum is the sum of the first k books, but we can take more, but that would only add more time. Therefore, for x >=k, the minimal sum is sum of first k type1 books, plus any sum from type2 and type3. Wait, no. Because when x >=k, then the required is already met. So the sum is the sum of x type1 books. So to minimize, x should be exactly k. But wait, if x is k, then sum is sum of first k type1 books. If x is k+1, sum is sum of first k+1, which is larger. So for x >=k, the minimal possible sum is when x is exactly k. So in that case, the sum is sum of first k type1 books, but only if there are at least k type1 books. Otherwise, even if x exceeds k, but you can't take enough.

Wait, no. Suppose type1 has m1 books. If m1 >=k, then taking x =k would be the minimal sum for the x >=k case. Taking x larger than k would require sum of more books, which is larger. So for x >=k, the minimal possible sum is sum of first k type1 books (since x can be k). So in that case, when considering x >=k, the best option is x =k.

But wait, maybe even when x >=k, but type1 has more than k books, perhaps taking some combination of type1 and other books could be better. For example, if after taking k type1 books, some other type1 books have smaller times than the sum of the other required books. Wait, but in the x >=k case, we don't need any type2 or type3 books. So the total sum is the sum of x type1 books. So if x is exactly k, the sum is sum of first k type1. If x is larger, sum increases. So the minimal sum for x >=k is sum of first k type1 books.

Therefore, when considering x >=k, the minimal sum is sum of first k type1 books, provided that m1 >=k. So in that case, the minimal sum for x >=k is sum1[k], where sum1 is the prefix sum of type1.

So combining all possibilities, the algorithm can be:

Compute all possible x values where:

Either:

x is in [x_min, min(m1, k-1)] (so x <k, and need to take (k-x) from type2 and type3)

OR

x is >=k, and then sum is sum1[k] (but only if m1 >=k)

So the steps are:

1. Collect all type1, type2, type3 books.

2. Sort each of the three lists by t_i in ascending order.

3. Compute prefix sums for each list.

4. Compute the possible x values:

   a. x can be in the range [x_min, x_max], where x_min is max(0, k - m2, k -m3), and x_max is min(m1, k-1). For these x, we take x type1, (k-x) type2, (k-x) type3. But for each x, we need m2 >= (k-x) and m3 >= (k-x).

   b. Also check the case where x >=k. For that, we can take x =k type1 books (if m1 >=k), and no type2 or type3. So sum is sum1[k].

Additionally, there's another possible case where we take some books from type1, and then combine with type2 and type3. But maybe the minimal sum is when you take some type1 books plus as many as possible from type2 and type3, but that's already considered in the x range.

So the approach is:

- For each possible x in the x_min to x_max range, compute the sum of x type1, (k-x) type2, (k-x) type3.

- Also compute the case where x =k (if m1 >=k).

Then, among all these possible sums, pick the minimal one.

But how to compute x_min and x_max.

x_min is the maximum of 0, (k - m2), (k - m3). Because:

For type2 to have (k -x) books available, m2 >= (k -x) --> x >=k - m2.

Similarly, for type3: x >=k -m3.

So x must be >= max( k -m2, k -m3, 0 )

x_max is the minimum between m1 and (k-1). Because when x >=k, that's handled separately.

Wait, no. Because if x_max is the maximum x that is less than k. Because when x is >=k, the (k -x) would be <=0, but in that case, the required for Alice and Bob is already met. So for x >=k, the sum is sum1[x], but to minimize, x should be exactly k, and sum1[k], provided that m1 >=k.

So in the first part (x <k), x can be up to m1 (but must be <=k-1). So x_max is min(m1, k-1). But wait, if m1 is larger than k-1, then x_max is k-1.

Wait, for example, if m1 is 10 and k is 4. Then x can be up to 3 (since x <k) for the first part.

So for x in 0 to 3 (provided x >= x_min), we compute the sum as x type1 + (4-x) type2 + (4-x) type3.

Then, check the case where x =4 (if m1 >=4), which would require sum1[4], but only if m1 >=4.

So the steps:

Compute all possible x in x_min to x_max (x_max is min(m1, k-1)), and for each x where m2 >= (k-x) and m3 >= (k-x), compute the sum.

Also, compute the sum when x >=k (if possible) which is sum1[k].

Then, the minimal sum among all these possibilities is the answer.

But how to compute x_min and x_max.

x_min = max(0, k - m2, k -m3)

x_max = min(m1, k-1)

If x_min > x_max, then no valid x in this range, so the only possible candidate is the x >=k case.

Now, to compute the sum for each x in x_min to x_max:

For each x, if (k -x) <= m2 and (k -x) <= m3.

Wait, but x_min is already set as the maximum of (k -m2, k -m3, 0), which ensures that (k -x) <= m2 and (k -x) <= m3.

Because x >=k -m2 --> k -x <= m2.

Similarly, x >=k -m3 --> k -x <=m3.

So for x >=x_min, (k -x) <= m2 and (k -x) <= m3.

So in that case, for each x in x_min ... x_max, the sum is sum1[x] + sum2[k -x] + sum3[k -x].

But we need to check whether x <=m1 (sum1[x] exists), and (k -x) <=m2 and <=m3.

But x_min is already set to ensure that (k -x) <= m2 and m3.

So for each x in x_min to x_max (inclusive), the sum is valid.

So the code can proceed as follows.

Now, the problem is that the x can range up to 2e5, and for each x in this range, we need to compute the sum. But if the x_min is 0 and x_max is 2e5, iterating each x in O(1) is acceptable.

But given that n is up to 2e5, and x can be up to 2e5, but the code can handle this in O(1) per x in the range.

Wait, but in practice, for each x in x_min to x_max, the sum is prefix1[x] + prefix2[k-x] + prefix3[k-x], which can be computed in O(1) if the prefix arrays are precomputed.

But the problem is that the x_min and x_max can be up to 2e5. So for the worst case, the loop would run 2e5 times. But 2e5 operations are acceptable for Python, as each is O(1), so total O(2e5) steps.

So the plan is:

1. Separate books into type1, type2, type3.

2. Sort each list and compute prefix sums. The prefix sums for each list will be a list where prefix[i] is the sum of the first i books.

3. Compute m1, m2, m3: the count of each type.

4. Compute the possible x_min and x_max.

   x_min = max(0, k - m2, k - m3)

   x_max = min(m1, k-1)

5. Check if x_min > x_max: if yes, then no solution in this case. Else, compute the minimal sum for x in x_min to x_max.

6. Also check the case where x >=k: this is possible only if m1 >=k and (m2 >=0 and m3 >=0). Wait, no. Because in this case, x is k, and sum is sum1[k]. But m1 must be >=k.

So the sum for this case is sum1[k] if m1 >=k.

So compute that sum if possible.

7. Among all possible sums, pick the minimal one.

If there are no possible sums (i.e., all possible cases are invalid), then output -1.

Now, let's handle edge cases.

For example, if m2 or m3 is 0. Then, for x to be valid, x must be >=k -m2, which if m2 is zero, then x >=k. But x can't be >=k unless m1 >=k and then x is >=k. But in that case, we would have to take x >=k, but in the x >=k case, which is sum1[k] if possible.

But if m2 is zero, then when x <k, (k -x) would have to be <=m2, which is zero. So x >=k. So the only possible sum is sum1[k], but only if m1 >=k and (sum of m2 and m3 can be zero). Wait, no. When x >=k, then (k -x) is <=0. So no need for type2 or type3. So the sum is sum1[x], but we have to take x >=k. But since x can be up to m1, but the minimal sum is sum1[k].

But sum1[k] is the sum of the first k type1 books, which is possible if m1 >=k.

So in this case, if m2 is zero and m3 is zero, but m1 >=k, then the sum is sum1[k].

Otherwise, impossible.

Another example: if k=0. But according to constraints, k >=1. So no problem.

Now, let's see the sample input:

Sample 1:

8 4

Books:

7 1 1 --> type1

2 1 1 --> type1

4 0 1 --> type3 (a=0, b=1)

8 1 1 --> type1

1 0 1 --> type3

1 1 1 --> type1

1 0 1 --> type3

3 0 0 --> type4 (ignored)

So type1 books are: [7,2,8,1], sorted to [1,2,7,8]. Wait, no. Wait, sorted by time.

Wait, for type1, the books are:

t_i:7, 2,8,1,1 (the fifth book is 1 1 1?)

Wait, the fifth book is 1 0 1, which is type3 (a=0, b=1). So in the sample input:

Looking at the books:

First book:7,1,1 → type1.

Second:2,1,1 → type1.

Third:4,0,1 → type3.

Fourth:8,1,1 → type1.

Fifth:1,0,1 → type3.

Sixth:1,1,1 → type1.

Seventh:1,0,1 → type3.

Eighth:3,0,0 → type4.

So type1 books are 7, 2,8,1,1 (books 1,2,4,6). Wait, no: let's list all books:

Looking at each of the 8 books:

1:7,1,1 → type1.

2:2,1,1 → type1.

3:4,0,1 → type3.

4:8,1,1 → type1.

5:1,0,1 → type3.

6:1,1,1 → type1.

7:1,0,1 → type3.

8:3,0,0 → type4.

So type1 books are books 1,2,4,6. Their t values:7,2,8,1.

Sorting them in ascending order gives:1 (book6), 2 (book2),7 (book1),8 (book4). So sum1[4] is 1+2+7+8 =18.

Type2 is empty (since no books where a=1 and b=0).

Type3 books are books3,5,7. t values 4,1,1. Sorted as 1,1,4. Sum3[3] is 1+1+4=6.

m1=4 (type1 count), m2=0 (type2 count), m3=3 (type3 count).

x_min = max(0, 4 -0, 4-3) → max(0,4,1) →4.

x_max = min(4, 4-1) → min(4,3) →3.

So x_min is 4, x_max is3. So no x in this range. So the only possible case is x >=k (4). So sum1[4] =1+2+7+8=18. Which is the sample output.

So the code should compute this.

Another sample:

Sample 2:

5 2

Books:

6 0 0 → type4 (ignored)

9 0 0 → type4 (ignored)

1 0 1 → type3.

2 1 1 → type1.

5 1 0 → type2.

So type1: [2] (t=2).

type2: [5] (t=5).

type3: [1] (t=1).

m1=1, m2=1, m3=1.

x_min = max(0, 2-1, 2-1) → max(0,1,1) →1.

x_max = min(1, 2-1) →1.

So x can be 1.

sum1[1] =2.

sum2[k -x] =2-1=1 → sum2[1]=5.

sum3[k-x] =2-1=1 → sum3[1]=1.

Total sum is 2+5+1=8.

Also check if x >=k (2). But m1 is 1, which is less than 2. So that's not possible.

So the answer is 8.

So code works.

Sample3:

5 3

Books:

3 0 0 → type4.

2 1 0 → type2.

3 1 0 → type2.

5 0 1 → type3.

3 0 1 → type3.

type1: none. m1=0.

type2: [2,3], sorted →2,3. sum2[0]=0, sum2[1]=2, sum2[2]=5.

type3: [5,3], sorted →3,5. sum3[0]=0, sum3[1]=3, sum3[2]=8.

k=3.

x can be in [x_min, x_max].

x_min = max(0, 3-2 (m2=2), 3-2 (m3=2)) →max(0,1,1) →1.

x_max = min(0 (m1=0), 3-1=2) →0.

So x_min=1, x_max=0 → invalid. So no solution in this range.

Then check x >=3. But m1=0, so no. So total impossible. Output -1.

So code returns -1.

So the approach works.

Now, code steps:

Read n and k.

Read each book, categorize into type1, type2, type3. Ignore type4.

Sort each type in ascending order of t_i.

Compute prefix sums for each type.

Compute m1 = len(type1), m2= len(type2), m3= len(type3).

Compute x_min = max(0, k - m2, k -m3)

x_max = min(m1, k-1)

possible_sums = empty list.

If x_min <=x_max:

   for x in x_min ...x_max:

       s2 = k -x

       s3 =k -x

       sum_total = prefix1[x] + (prefix2[s2] if s2 >0 else 0) + (prefix3[s3] if s3>0 else 0)

       possible_sums.append(sum_total)

Also, check the case where x >=k.

If m1 >=k:

   s = prefix1[k]

   possible_sums.append(s)

If possible_sums is empty → output -1.

Else, output the minimum possible sum.

But wait, when x >=k, the sum is prefix1[x], but x can be up to m1. But the minimal sum is when x=k, because taking more than k would add more time.

So we only consider x=k, not higher.

So in code:

if m1 >=k:

   sum_candidate = prefix1[k]

   possible_sums.append(sum_candidate)

So, that's correct.

Now, edge case when k=0. But according to constraints, k>=1.

Another edge case: if x_min is 0, but m2 and m3 are zero. Then, x must be >=0, but (k-x) must be <=0. So x >=k. So if m1 >=k, then sum1[k] is possible.

Now, code:

Implement the steps.

Now, handling the prefix sums:

For each type, after sorting, compute the prefix sum. The prefix sum starts at 0 (sum of 0 elements is 0), then sum up each element.

For example, type1 sorted as [1,2,7,8]. Prefix sum is [0, 1, 3, 10, 18].

So for x=2, sum1[2] is 3 (sum of first 2 elements:1+2=3).

So code:

type1_sorted = sorted(type1)

prefix1 = [0]

sum_so_far =0

for t in type1_sorted:

    sum_so_far +=t

    prefix1.append(sum_so_far)

Same for type2 and type3.

Now, code:

Read n, k.

type1 = []

type2 = []

type3 = []

for _ in range(n):

    t, a, b = map(int, input().split())

    if a ==1 and b ==1:

        type1.append(t)

    elif a ==1 and b ==0:

        type2.append(t)

    elif a ==0 and b ==1:

        type3.append(t)

    # else: ignore type4.

Sort the three lists.

Compute prefix1, prefix2, prefix3.

Compute m1, m2, m3.

x_min = max(0, k - m2, k - m3)

x_max = min(m1, k-1)

possible = []

if x_min <= x_max:

    # precompute the prefix sums for type2 and type3 up to k -x_min and k -x_max?

    for x in range(x_min, x_max +1):

        s2 = k -x

        s3 =k -x

        sum1 = prefix1[x]

        sum2 = 0

        if s2 >0:

            if s2 > m2:

                # not possible, but x_min is supposed to ensure that s2 <=m2.

                # because x >= k -m2 → s2 =k -x <=m2.

                # so this should not happen.

                pass

            else:

                sum2 = prefix2[s2]

        sum3 =0

        if s3>0:

            if s3>m3:

                pass

            else:

                sum3 = prefix3[s3]

        possible.append(sum1 + sum2 + sum3)

# Check the x >=k case.

if m1 >=k:

    sum_total = prefix1[k]

    possible.append(sum_total)

if not possible:

    print(-1)

else:

    print(min(possible))

But how to handle the cases where s2 or s3 are 0?

In code, when s2 is 0, sum2 is 0 (since s2 <=0, so no need for type2 books). So sum2 is 0.

So the code for sum2 and sum3 is:

sum2 = prefix2[s2] if s2 >0 else 0

sum3 = prefix3[s3] if s3>0 else 0

But in the code above, when s2 <=0, sum2 is 0.

But in the code:

sum2 = 0

if s2>0:

    sum2 = prefix2[s2]

But how to get prefix2[s2]?

Wait, prefix2 is a list where prefix2[i] is the sum of first i books.

So for s2=2, sum is prefix2[2], which is sum of first 2 books.

So code:

s2 = k -x

sum2 = prefix2[s2] if s2 <= len(prefix2)-1 else ... ?

Wait, no. Because the prefix2 is built as:

prefix2 starts with 0, then adds each element. So for example, if type2 has 3 books, prefix2 will have 4 elements (0, t0, t0+t1, t0+t1+t2).

So if s2 is 2, and m2 >=2, then prefix2[2] is sum of first 2 books.

But in code, when we compute s2 =k -x, but x >=k -m2 (due to x_min).

Because x >=k -m2 → s2 =k -x <=m2.

Thus, in the code, s2 is <=m2. And since prefix2 has length m2 +1, prefix2[s2] is valid.

So the code is correct.

Now, code.

Testing sample1:

type1 books sorted: [1,2,7,8], prefix1 is [0,1,3,10,18].

type2 is empty → prefix2 is [0].

type3 sorted: [1,1,4], prefix3 is [0,1,2,6].

m1=4, m2=0, m3=3.

x_min = max(0, 4-0=4, 4-3=1) →4.

x_max = min(4, 4-1=3) →3.

So x_min (4) >x_max (3) → no solution in this case.

Check the x >=k case. k=4. m1=4 >=4 → sum1[4] =18. So possible is [18]. Output 18.

Sample2:

type1: [2], prefix1 [0,2].

type2: [5], prefix2 [0,5].

type3: [1], prefix3 [0,1].

x_min= max(0, 2-1, 2-1)=1.

x_max= min(1, 2-1)=1.

So x=1.

s2=2-1=1 → sum2=5.

s3=1 → sum3=1.

sum1[1]=2. total 2+5+1=8.

Also check x>=2 (k=2). m1=1 <2 → no. So possible is [8]. Output 8.

Sample3:

type1 is empty. m1=0.

type2 has 2 books (2,3), prefix2 [0,2,5].

type3 has 2 books (3,5), prefix3 [0,3,8].

x_min= max(0, 3-2, 3-2)=1.

x_max= min(0, 3-1=2) →0.

No solution in x_min to x_max.

Check x>=3: m1=0 <3. So possible is empty. Output -1.

Thus code works.

Now, code in Python.

But for handling the prefix sums, note that when type2 or type3 is empty, their prefix sum is [0], so when s2=0, sum is 0.

But when s2>0 and type2 is empty, it's impossible, but x_min ensures that x >=k -m2. So if m2 is 0, then x >=k -0 →x >=k. So in that case, s2 =k -x <=0. So sum2=0.

Thus code is correct.

So the code will handle all cases.

Now, code:

Read n and k.

Then, for each of n books, categorize.

Sort the type lists.

Compute prefix sums.

Then compute possible sums.

Now, code.
</think>

```python
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    type1 = []
    type2 = []
    type3 = []
    for _ in range(n):
        t, a, b = map(int, sys.stdin.readline().split())
        if a == 1 and b == 1:
            type1.append(t)
        elif a == 1 and b == 0:
            type2.append(t)
        elif a == 0 and b == 1:
            type3.append(t)
    # Sort each type and compute prefix sums
    type1.sort()
    type2.sort()
    type3.sort()
    # Prefix sums
    prefix1 = [0]
    for t in type1:
        prefix1.append(prefix1[-1] + t)
    prefix2 = [0]
    for t in type2:
        prefix2.append(prefix2[-1] + t)
    prefix3 = [0]
    for t in type3:
        prefix3.append(prefix3[-1] + t)
    m1, m2, m3 = len(type1), len(type2), len(type3)
    possible = []
    x_min = max(0, k - m2, k - m3)
    x_max = min(m1, k-1)
    if x_min <= x_max:
        for x in range(x_min, x_max + 1):
            s2 = k - x
            s3 = k - x
            sum_total = prefix1[x]
            if s2 > 0:
                sum_total += prefix2[s2]
            if s3 > 0:
                sum_total += prefix3[s3]
            possible.append(sum_total)
    # Check case where x >= k
    if m1 >= k:
        possible.append(prefix1[k])
    if not possible:
        print(-1)
    else:
        print(min(possible))
        
if __name__ == "__main__":
    main()
```