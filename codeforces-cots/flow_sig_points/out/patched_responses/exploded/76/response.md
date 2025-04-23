<think>
Okay, I need to solve this programming problem. Let's read the problem statement carefully.

The problem is about finding suggested friends for each user in a social network. The suggested friends are those non-friends who are friends with at least k% of the user's friends. So, for each user x, we have to look at all their current friends, find the users y who are not friends with x but are friends with at least k% of x's friends. Then output those y in sorted order.

First, let's understand the input. The input is m pairs of friends. Each pair is given once. So, if a and b are friends, the pair (a, b) appears once, and we can assume the friendship is mutual. The output requires that for all mentioned users (those that appear in the input), sorted by their ID, we list their suggested friends.

So, the first step is to process all the input pairs and build a data structure that maps each user to their set of friends. Because the friends are mutual, each time a pair (a, b) is read, we add b to a's friends and a to b's friends.

Once the friend lists are built, for each user x, we need to compute for every possible y (not in x's friends and not x) the number of x's friends that are friends with y. Then, check if that count is >= (k * len(friends_of_x)) / 100. Since k can be 100, which is exact, we need to use integer division with proper handling of fractions.

But wait, the problem statement says "не менее, чем для k% друзей x". So, the required number of friends is the ceiling of (k% of the friends of x). Wait, no. Let's compute it as a percentage.

For example, if x has N friends, then the required number of mutual friends for y is at least (k * N) / 100. But division here could be fractional. So, we need to use ceiling or exact? For example, if k is 51, and N is 3 friends, then 3 * 51% = 1.53 → so y needs to be friends with at least 2 of x's friends.

Wait, the problem statement says "не менее, чем для k% друзей x". So, the threshold is (k% of the number of friends x has). Since you can't have a fraction of a friend, this needs to be computed as the ceiling of k% when necessary. However, how to handle this precisely.

Wait, mathematical formula: required = ceil( (k / 100) * len(friends_x) )? Or is it floor?

For example, in the first sample input:

Sample Input 1:
5 51
10 23
23 42
39 42
10 39
39 58

Let's look at user 58. His friends are 39. So friends_x has size 1. k is 51. So 51% of 1 is 0.51. So y needs to be friends with at least 1 (0.51 → ceiling is 1) of 58's friends. So for any y not friend of 58 (which is 39's friends are 10, 42, 58. So 58's friends is 39. So non-friends would be all users except 39 and 58. Wait, but in the sample output, 58's suggested friends are 10 and 42. Let's see.

Wait, 58's friends are only 39. So for a user y to be suggested, they must not be friends with 58 (so y != 39 and y !=58) and have at least 51% of 58's friends. Since len(friends) is 1, 51% of 1 is 0.51, so required is at least 1. So y must be friends with at least 1 of 58's friends (which is 39). So y must be a friend of 39. The friends of 39 are 10, 42, 58. So y can't be 39 (since x is 58), and can't be 58. So possible y's are 10 and 42. Both are friends of 39. So 58's suggested friends are 10 and 42.

So in this case, 1 friend of x, and required is 1. So the calculation is ceil(k% * friends_count). But how to handle it precisely.

So, the formula would be required = ceil( (k * friends_count) / 100 ). However, since in some programming languages division is integer, perhaps we can compute it as:

required = (k * friends_count + 99) // 100

Wait, let's think. For example, if k=51, friends_count=3 → 51*3=153 → 153/100=1.53 → ceil(1.53)=2. So (153 +99) = 252 → 252//100=2.52 → but integer division would be 2. So yes, (k * friends_count + 99) // 100 gives the ceiling.

Yes. Because (a + b - 1) // b is the way to compute the ceiling of a/b.

So, required = ceil( (k * friends_count) / 100 ) → which can be written as (k * friends_count + 99) // 100.

But we have to make sure that when (k * friends_count) is exactly divisible by 100, it's not over-incremented. For example, k=50, friends_count=2 → 50*2=100 → 100/100=1 → required is 1. (50 * 2 +99) //100 = (199)//100=1.99 → integer division is 1, which is correct.

Yes, that formula works.

So, for each user x:

- Collect all friends of x (friends_x). friends_x is a set.

- For all possible users y that are not x and not in friends_x, check if the number of friends of x that are friends with y is >= required.

But how do we collect all possible users y? Since the input may have up to m=100 pairs, but each pair can be up to 1e9 in ID, we can't iterate through all possible IDs. So, the possible y's are those users that are friends of friends of x. Because only friends of x's friends can be friends with some of x's friends.

Wait, but y could be someone who is friends with a friend of x but is not a friend of x. So, for x's friends, their friends are possible candidates for y. Because y must have at least one friend (a friend of x) to be considered.

But how do we collect all such y's?

Alternative approach:

For each x, the candidates y must be in the union of the friends of x's friends, but not in x's friends, and not x itself.

But building this set for each x could be expensive if x has many friends, each with many friends. However, since m is up to 100, the total number of friends per x is up to m. Because each pair is unique. So for example, a user x can have up to m friends if all pairs involve x. But m is 100, so friends_x can be up to 100 elements.

Then, for each friend in friends_x, collect their friends. Then take the union of all those friends, subtract x's friends and x. So the candidates for y are the union of friends of friends of x, minus x's friends and x.

Once we have the candidate y's for x, we need to check for each y how many friends of x are friends with y. Then compare that count with the required threshold.

But even this approach could be manageable. Let's think through the steps.

First, build a friends dictionary: for each user, a set of their friends.

Then, for each x in the list of all users (all mentioned in the input):

- Get the friends of x, friends_x. The size is n = len(friends_x).

- If n is 0, then there can be no suggested friends (since 0 friends, so k% of 0 is 0, but there are no friends to check). So output 0.

- Else, compute required = (k * n + 99) // 100.

- Collect all candidates y:

   For each friend in friends_x, add all their friends to a set. Then subtract friends_x and x from this set.

   So candidates = (union of friends of friends_x) - friends_x - {x}

- For each candidate y in candidates:

   count = 0

   for each friend in friends_x:

       if y is in friends of friend, increment count.

   if count >= required, then add y to the suggested list.

- Sort the suggested list and output.

But how efficient is this?

For each x:

- Collecting candidates: For each friend in friends_x (up to 100), for each friend's friend (up to 100 per friend), so up to 100*100=10,000 entries. But since the friends are stored in sets, the union can be built efficiently by adding all elements and then converting to a set.

But even 10,000 entries per x is manageable for m up to 100.

Then, for each candidate y (say, 10,000 per x), for each x's friend (100), check if y is a friend. So 100 checks per candidate. For 10,000 candidates, that's 1,000,000 operations per x.

But for m up to 100, the total number of users mentioned could be up to 200 (since each pair is two users). So 200 x's. Each with 1e6 operations → 2e8 operations. That's probably too slow for Python, which can handle about 1e8 operations per second. But 2e8 is 200 million, which is over the time limit.

Wait, but in reality, the friends per x could be lower. Let's think. For example, if x has 100 friends, and each friend has 100 friends, the union could be 100*100=10,000. But each of those friends' friends could have overlaps, so the actual number of unique candidates is much less.

But even if it's 10,000 candidates per x, and 100 x's (since m=100, possible users are up to 200), then 100 x 10,000 x 100 = 1e8 operations. That's 100 million, which in Python may be tight for a 2-second time limit. But perhaps with optimizations.

So, how to optimize this.

Alternative approach: precompute for each user, the set of their friends.

Then, for each x, collect all friends of friends (excluding x and x's friends) and for each such y, precompute how many of x's friends are friends with y.

But how?

Another idea: For each x, for all possible y that are candidates (friends of friends), compute the count by taking the intersection of x's friends and y's friends, then the size of that intersection.

But how to compute that efficiently.

But for x's friends, which are stored as a set, and for y's friends stored as a set, the intersection can be computed as the size of the intersection of friends_x and friends_y.

Wait, but friends_x is a set, and friends_y is a set. The intersection is friends_x & friends_y. The length is len(friends_x & friends_y). So for each candidate y, the number of mutual friends between x's friends and y is the number of friends of x that are also friends of y.

So for a candidate y, the count is the size of the intersection between friends_x and friends_y.

Thus, for each candidate y, the count is len( friends_x & friends_y ).

But in Python, set intersections are O(min(len(a), len(b))). So if friends_x is 100 elements and friends_y is 100 elements, each intersection is O(100) per check.

So for each candidate y, this is O(100) time. For 10,000 candidates per x, that's 1e6 per x. For 200 x's, 2e8 operations. Which is too slow.

Alternative idea: Precompute for each possible pair (y, friend) a count of how many friends of x are in friends_y.

Wait, maybe we can precompute for each user a set of their friends, and then for each x, collect all the friends of friends (candidates y), and for each y, count how many friends of x are in y's friends. That's exactly what we need.

But how?

Yes. So for a candidate y, the count is the number of friends of x that are in y's friends.

So, for each x:

   friends_x = set of friends of x.

   candidates_y = (union of friends of friends_x) - friends_x - {x}

   for each y in candidates_y:

       count = len( friends_x & friends_of_y )

       if count >= required:

           add to suggested.

So, the problem is that for each y, friends_of_y is a set, and the len of the intersection between friends_x and friends_of_y is the count.

But friends_x can be up to 100 elements, and for each y, friends_of_y can be up to 100 elements. So each intersection is up to 100 elements. But even for 100 elements, checking each element in friends_x if it's present in friends_of_y's set is O(1) per element, because sets have O(1) membership check.

Wait, but for the len(friends_x & friends_of_y) operation, it's equivalent to sum(1 for friend in friends_x if friend in friends_of_y).

Which is O(len(friends_x)) time.

So for each y, it's O(len(friends_x)) time to compute the count.

So for a friends_x of size 100, and 10,000 candidates, that's 1e6 operations per x. For 200 x's, that's 2e8 operations. Which may be too slow for Python.

So we need a way to optimize this.

Alternative approach: For each x, precompute a set of friends_x. Then, for each candidate y, the count is the number of friends of x that are present in friends_of_y. Since friends_of_y is a set, checking for each friend in friends_x whether it's in friends_of_y is O(1) per check.

So the count can be computed as sum(1 for friend in friends_x if friend in friends_of_y).

But even this is O(len(friends_x)) per candidate y.

Wait, but if we can precompute for each x, a dictionary that maps user IDs to their friends, then for each candidate y, friends_of_y is retrieved from the dictionary, and then for each friend in friends_x, we check if they are in friends_of_y. So sum the count.

But again, this is O(len(friends_x)) per y.

So the key is to find a way to compute this count more efficiently.

Alternative idea: For each x, precompute a set of friends_x. Then, for each candidate y, the count is the size of the intersection between friends_x and friends_of_y. The size can be computed as the sum of 1 for each element in friends_x that is present in friends_of_y's set.

But how else can this be computed?

Wait, perhaps for each x, we can represent friends_x as a set. Then, for a candidate y, the count is the number of elements in friends_x that are present in the friends_of_y's set.

But this is the same as the len of friends_x & friends_of_y.

So no way around that. So, perhaps this is the best approach.

Now, considering that m is up to 100, and the total number of users is up to 200, and each friends list is up to 100, perhaps this approach is manageable.

But let's compute.

Suppose for each x:

friends_x has 100 elements.

candidates_y has 100 * 100 = 10,000 elements (if each friend has 100 friends), but after removing x's friends and x, maybe 9,900.

For each candidate y, 100 checks (if friend in friends_of_y).

So per x, 100 * 10,000 = 1,000,000 operations.

For 200 x's, 200 million operations. Python can handle about 1e8 operations per second, so 200 million would take 2 seconds. Which is tight but possible if optimized.

But perhaps in practice, the numbers are lower. For example, if each x has 50 friends, and each friend has 50 friends, the candidates are 50*50 = 2500 per x. Then 50*2500 = 125,000 per x. For 200 x's, 25 million operations, which is manageable.

But the worst case is m=100 pairs, all connected to a single user x. Then x has 100 friends. Each of those friends has 100 friends (possibly overlapping). So the candidates could be up to (100 * 100) - 100 (subtract x's friends) and minus x. Suppose each friend's friends are distinct. So 100*100=10,000, minus 100 (friends of x) → 9,900, minus x (if present) → 9,899. For each of these 9,899 candidates, 100 checks. So 989,900 operations per x. For 200 x's, 197,980,000 operations, which is around 2e8. Which would be about 2 seconds in Python.

But perhaps even this can be optimized.

Alternative idea: For each x, precompute a set of friends_x. Then, for each candidate y, instead of checking all friends in friends_x, precompute the friends_of_y once and then iterate through the smaller set. For example, if friends_x is larger than friends_of_y, iterate through friends_of_y and count how many are in friends_x. But this would not save time, as it's the same number of checks.

Hmm. Maybe not helpful.

Alternative approach: Precompute for each user, a set of their friends. Then, for a given x and candidate y, the count is the length of the intersection of friends_x and friends_of_y. To compute this quickly, can we represent friends_x as a set and friends_of_y as a set, then find the size of their intersection. In Python, the set intersection is O(min(len(a), len(b))). So if friends_x has 100 elements and friends_of_y has 100 elements, the intersection is 100 elements (worst case), but in Python, the time is O(100), same as checking each element.

So perhaps no gain.

Alternative idea: Precompute for each x's friends_x as a set. Then, for each candidate y, the count is the number of friends of x that are in the friends_of_y set.

But in Python, checking if an element is in a set is O(1). So for each friend in friends_x, check if it's in friends_of_y's set. Summing the count. Which is O(len(friends_x)) time.

So how to optimize this.

Wait, perhaps using bitmasking. But given that the user IDs can be up to 1e9, it's impossible to represent the friends as bits.

Alternative approach: For each x, friends_x is a set. For each candidate y, friends_of_y is a set. The intersection can be computed as len(friends_x & friends_of_y). But in Python, this is O(min(len(friends_x), len(friends_of_y))) time.

Wait, but perhaps using the built-in set intersection is more efficient than manually checking each element. For example:

count = len(friends_x.intersection(friends_of_y))

This is a single operation, and in Python, the set intersection is implemented efficiently in C, so even though the time complexity is O(n), the constant factors are much better than looping through each element in Python.

So this is a crucial optimization. Instead of looping through each element in friends_x and checking if it's in friends_of_y, we can compute the intersection size using the built-in set operation, which is much faster.

So for each candidate y, the count can be computed as:

count = len(friends_x & friends_of_y)

This is a single line in Python and is handled efficiently in C code, which is much faster than a Python for loop.

So this optimization can significantly reduce the runtime.

So the key steps are:

1. Read all the pairs and build a dictionary (friends) where each user's friends are stored as a set.

2. Collect all users mentioned in the input (all_users) and sort them.

3. For each user x in all_users in sorted order:

   a. Get friends_x = friends[x]

   b. n = len(friends_x)

   c. If n == 0:

       output x: 0

       continue

   d. required = (k * n + 99) // 100

   e. Collect all candidates y as follows:

       candidates = set()

       for friend in friends_x:

           candidates.update(friends[friend])

       candidates.difference_update(friends_x)

       candidates.discard(x)

   f. For each y in candidates:

       friends_of_y = friends[y]

       count = len(friends_x & friends_of_y)

       if count >= required:

           add y to suggested list

   g. Sort the suggested list and output.

Now, step 3e is building the candidates. For each friend of x, add all their friends (which includes x's friends and others). Then subtract x's friends and x.

But in Python, the set operations are efficient. So friends_x is a set. For each friend in friends_x, friends[friend] is a set. So candidates is the union of all friends[friend] for friend in friends_x. Then, subtract friends_x and x.

So for example:

Initially, candidates is empty. Then, for each friend in friends_x, add their friends. Then, remove friends_x and x.

Now, let's see for the first sample input.

Sample Input 1:

5 51

10 23

23 42

39 42

10 39

39 58

The friends dictionary after processing would be:

10: {23,39}

23: {10,42}

39: {10,42,58}

42: {23,39}

58: {39}

Now, for x=58:

friends_x = {39}

n = 1

required = (51 *1 +99)//100 = (51+99)/100=150//100=1.5 → 1.5 → integer division gives 1.

So required is 1.

Candidates are:

For friends of 58's friends (friend is 39):

friends of 39 are 10,42,58.

Then candidates is {10,42,58}.

Subtract friends_x (39 and 58 are not in friends_x, but friends_x is {39}?)

Wait, friends_x is {39}, so subtract {39} from the candidates.

Also subtract x=58.

So initial candidates after adding friends of 39 is {10,42,58}.

Then, subtract friends_x (39 is not in the candidates, so no change). Then subtract x=58. So candidates becomes {10,42}.

For each y in {10,42}:

Check len(friends_x (which is {39}) & friends_of_y.

For y=10: friends_of_10 is {23,39}. The intersection with {39} is {39} → length 1. So count is 1 >= 1 → yes. So add 10.

For y=42: friends_of_42 is {23,39}. Intersection is {39} → count 1 >=1 → add 42.

So suggested list is [10,42], sorted. Which matches the sample output.

So the approach works.

Now, the next optimization is to collect all candidates efficiently.

Now, the steps for each x are:

- Collect all friends of friends.

But in Python, the union can be done by creating a set and updating it with each friend's friends.

But for efficiency, perhaps using a set and repeatedly updating is the way to go.

Now, let's code this.

First, read m and k.

Then, read m pairs. For each pair a, b:

- Add b to a's friends set.

- Add a to b's friends set.

Also, collect all users in a set (all_users) to process them in sorted order.

After reading all pairs, process each user in sorted(all_users).

But the code structure in Python would be:

friends = defaultdict(set)

all_users = set()

for each pair:

   a, b = map(int, input().split())

   friends[a].add(b)

   friends[b].add(a)

   all_users.add(a)

   all_users.add(b)

Then, sorted_users = sorted(all_users)

Then, for each x in sorted_users:

   friends_x = friends[x]

   n = len(friends_x)

   if n ==0:

       print(f"{x}: 0")

       continue

   required = (k * n +99) // 100

   # build candidates

   candidates = set()

   for friend in friends_x:

       candidates.update(friends[friend])

   # remove x's friends and x

   candidates -= friends_x

   candidates.discard(x)

   # now process each candidate

   suggested = []

   for y in candidates:

       # friends_of_y is friends[y]

       count = len(friends_x & friends[y])

       if count >= required:

           suggested.append(y)

   suggested.sort()

   print(f"{x}: {len(suggested)} {' '.join(map(str, suggested))}" if suggested else f"{x}: 0")

But wait, the candidate set could be empty. So in that case, output 0.

But how about when x has no friends? Then required is (k*0 +99)/100 = 0. So required is 0. But since len(friends_x) is 0, the code skips the processing. So in this case, the output is 0, which is correct.

Now, possible edge cases:

Test case when k is 0. Then required is 0. So any candidate y with count >=0 (which is always true). So all candidates are suggested.

But in the code, required is (0 *n +99)/100. Wait, no: for example, n=5, k=0. required = (0*5 +99)/100 =99/100=0.99 → integer division in Python is 0. So required is 0. So even if n is 5, (0*5) is 0, (0*5 +99) //100 = 0. So required is 0. So any candidate y with count >=0 (all) are included.

But how?

For example, if x has friends, and k=0, required is 0. So all candidates are suggested, as long as they are not friends with x.

But if k is 0, then the required is zero, which is len >=0, which is always true. So all candidates are suggested.

But in code, for k=0 and n>0, required is (0 *n +99)//100. Let's compute for n=5:

(0*5 +99)/100 →99//100=0. So required is 0.

So yes, the code correctly captures that.

Another edge case: when k=100. Then required is (100 *n) /100 → exactly n. So a candidate must be friends with all friends of x.

So, the code correctly computes required as (100*n +99) //100 = (100n +99) //100. For example, if n=5 → 500+99=599//100=5.99 →5. So required is 5. So the candidate must be friends with all 5 friends.

But wait, if n=5, k=100, required is (100*5)/100 =5. So code is correct.

But (100*5 +99) //100 → 599//100=5.99 →5 in integer division. So yes.

But wait, 100*5 is 500. 500/100 =5. So required is 5. So code uses (100*5 +99) //100 = (599)//100=5.99→5? Wait, no. 599 divided by 100 is 5.99, but integer division in Python truncates towards negative infinity. So 599 //100 is 5. So the code computes required as 5. Which is correct.

So for k=100, required is exactly (k/100) *n, rounded up. Wait, no. For example, n=3, k=100 → required is (300 +99)/100 → 399//100=3. So required is 3. Which is exactly 100% of n.

But if n=1, k=51: (51 *1 +99)/100 →150//100=1. So required is 1. Which is 51% of 1 is 0.51, ceil is 1.

Yes.

So the code correctly calculates the required.

Now, let's test the second sample input:

Sample Input 2:

5 100

1 2

1 3

1 4

2 3

2 4

The output is:

1: 0

2: 0

3: 1 4

4: 1 3

Let's see.

friends after processing:

1's friends: 2,3,4.

2's friends: 1,3,4.

3's friends: 1,2.

4's friends: 1,2.

So for x=1:

n=3, required = (100*3 +99)/100 →399//100=3. So required is 3.

Candidates:

friends of friends are 2's friends (1,3,4), 3's friends (1,2), 4's friends (1,2). The union is {1,2,3,4}.

Subtract friends_x (2,3,4) and x=1. So candidates is empty. So suggested list is empty. So output 0.

For x=2:

n=3, required 3.

friends are 1,3,4.

Candidates: friends of 1 (2,3,4), friends of 3 (1,2), friends of 4 (1,2). Union is 2,3,4,1. Subtract friends_x (1,3,4) and x=2 → no candidates. So output 0.

For x=3:

friends are 1,2. n=2.

required = (100*2 +99)/100 →299//100=2. So required is 2.

Candidates: friends of 1 (2,3,4), friends of 2 (1,3,4). Union is 1,2,3,4. Subtract friends_x {1,2}, and x=3. Candidates are {4}.

Check y=4:

friends_of_4 is {1,2}.

The count is len( {1,2} & {1,2} ) → 2. 2 >=2 → yes. So suggested is [4].

So output 3: 1 4.

Similarly for x=4.

Thus, the code works.

Now, the code must read input, process, and output.

But the code must read m lines after the first line. For m up to 100, no problem.

In Python, using defaultdict(set) is efficient. Also, when building the candidates, using set operations is efficient.

Now, let's code this.

But note that in Python, when we read the inputs, the order of processing the pairs does not matter since each pair is added to both a and b's friends.

So the code will be:

import sys
from collections import defaultdict

m, k = map(int, sys.stdin.readline().split())
friends = defaultdict(set)
all_users = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].add(b)
    friends[b].add(a)
    all_users.add(a)
    all_users.add(b)

sorted_users = sorted(all_users)

for x in sorted_users:
    friends_x = friends[x]
    n = len(friends_x)
    if n == 0:
        print(f"{x}: 0")
        continue
    required = (k * n + 99) // 100
    candidates = set()
    for friend in friends_x:
        candidates.update(friends[friend])
    candidates -= friends_x
    candidates.discard(x)
    suggested = []
    for y in candidates:
        count = len(friends_x & friends[y])
        if count >= required:
            suggested.append(y)
    suggested.sort()
    print(f"{x}: {len(suggested)} {' '.join(map(str, suggested))}" if suggested else f"{x}: 0")

Wait, but in the output, even when len(suggested) is zero, it should print "x: 0". So the code uses a ternary operator to check if suggested is non-empty. If yes, format with the numbers, else output with 0.

This should work.

Testing the first sample input:

Sample Input 1 output:

10: 1 42

23: 1 39

39: 1 23

42: 1 10

58: 2 10 42

Which the code should produce.

Thus, the code should be correct.

Now, possible optimizations:

- Using sys.stdin.readline() for faster input reading. Which we already do.

- Pre-sorting the suggested list once, which the code does.

But for very large candidate lists, the sorting could take time. But the candidates are up to 1e4, sorted in Python is O(n log n), which for 1e4 is manageable.

Another optimization: precompute friends_of_y for each y. But it's already stored as friends[y], so no gain.

Thus, the code should work within time and memory constraints.
</think>

```python
import sys
from collections import defaultdict

def main():
    m, k = map(int, sys.stdin.readline().split())
    friends = defaultdict(set)
    all_users = set()

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        friends[a].add(b)
        friends[b].add(a)
        all_users.add(a)
        all_users.add(b)

    sorted_users = sorted(all_users)

    for x in sorted_users:
        friends_x = friends[x]
        n = len(friends_x)
        if n == 0:
            print(f"{x}: 0")
            continue
        required = (k * n + 99) // 100
        candidates = set()
        for friend in friends_x:
            candidates.update(friends[friend])
        candidates -= friends_x
        candidates.discard(x)
        suggested = []
        for y in candidates:
            if len(friends_x & friends[y]) >= required:
                suggested.append(y)
        suggested.sort()
        if suggested:
            print(f"{x}: {len(suggested)} {' '.join(map(str, suggested))}")
        else:
            print(f"{x}: 0")

if __name__ == "__main__":
    main()
```