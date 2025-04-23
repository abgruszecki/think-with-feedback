<think>
Okay, I need to solve this problem where I have to determine each student's position based on their ratings. Let's read the problem carefully again.

The problem says that each student's position is 1 plus the number of students with strictly higher ratings. So if a student has a certain rating, their position is determined by how many students have a higher rating than them. And if two students have the same rating, they share the same position. For example, if two students are the highest, they both get position 1, and the next gets 3 if there are two higher than him.

Let me think about how to compute this efficiently.

The input constraints are up to 2000 students. So for each student, I need to count how many students have a strictly higher rating. Then add 1 to that count to get their position.

Wait, yes. For a given student i, their position is 1 + (number of students j where a_j > a_i). Because that's how many are strictly higher. For example, if three students have ratings 5, 5, 3. Then the first two have 0 higher students, so position 1. The third has two higher, so position 3.

So the straightforward approach would be: for each ai in the list, count how many elements in the list are strictly greater than ai, then add 1. That gives the position.

But with n up to 2000, doing this naively (for each element, iterate through the entire list and count) would result in O(n^2) time. Let's calculate: 2000^2 is 4 million operations. Which in Python is acceptable for 2 seconds, but maybe there's a better way.

Alternatively, we can pre-process the list to find the frequencies of each rating. Then for each ai, the count is the sum of frequencies of all ratings higher than ai.

So first, we can sort the unique elements in descending order. Then for each ai, find the sum of all elements that are strictly higher. This can be done by first creating a frequency map, then for each ai, iterate through the sorted unique list and sum the frequencies until we hit a value <= ai.

But how to do that efficiently.

Let me think. For example, for the list [3,5,3,4,5], the unique sorted in descending order is [5,4,3]. The frequencies are 5:2, 4:1, 3:2. So for each student's ai, the count is the sum of frequencies of elements higher than ai. Then add 1.

So for ai=5, higher elements sum to 0 → position 1. For ai=4, higher elements sum to 2 → position 3 (2+1=3). For ai=3, higher elements sum to 2+1=3 → position 4.

Yes. So the steps would be:

1. Create a frequency dictionary where keys are the ratings, and values are the counts.

2. Sort the unique ratings in descending order.

3. For each ai in the original list, iterate through the sorted unique ratings until we find the first one <= ai. Sum all the frequencies before that point (i.e., all higher ratings).

But even this approach could be optimized. For example, if the sorted unique list is in descending order, then for each ai, we can accumulate the sum of frequencies until we find a rating <= ai.

Wait, but how do we know when to stop? For example, in the sorted list [5,4,3], for ai=4, we take the first element (5 is higher than 4?), no. Wait, ai=4: higher elements are those greater than 4. So 5 is higher. So sum is 2. Then the next element is 4, which is equal, so we stop. So sum is 2.

So the sum of all elements in the sorted list that are greater than ai.

Thus, for each ai, the sum is the sum of frequencies where key > ai.

So the steps for each ai would be:

sum = 0

for rating in sorted_unique_ratings:

    if rating > ai:

        sum += freq[rating]

    else:

        break

Then, position is sum +1.

This way, once we hit a rating <= ai, we can break out of the loop since the rest are lower or equal.

So the question is, how to efficiently compute this sum for all ai in the original list.

Given that the maximum possible unique ratings is up to 2000 (since each ai can be up to 2000), the sorted unique list could be up to 2000 elements. For each ai, in the worst case, we iterate through all elements until we find one that's <= ai. But in the worst case (ai is the minimum), we iterate through all unique ratings. However, with 2000 unique ratings, each of the 2000 students would take 2000 steps. So 2000*2000=4 million steps, which is manageable.

But maybe there's a way to precompute a structure that allows for O(1) lookup for each ai.

Alternatively, we can precompute a prefix sum array.

Wait, the sorted unique list is in descending order. For example, sorted_ratings = [5,4,3], and frequencies [2,1,2].

We can precompute a prefix sum array where prefix_sum[i] is the sum of the first i elements (sum of frequencies of the first i unique ratings, which are in descending order). So for the example, prefix_sum would be [2, 3,5].

Then for a given ai, we need to find the largest index i where sorted_ratings[i] > ai. The sum is the prefix_sum up to that index.

But how to find that index quickly. For example, in the sorted list, which is in descending order, for a given ai, the elements greater than ai are the first k elements where sorted_ratings[k] > ai, and sorted_ratings[k+1] <= ai.

So we can perform a binary search to find the largest index where the rating is greater than ai.

Wait, since the sorted list is in descending order, the binary search would look for the rightmost element that is greater than ai.

For example, in the sorted list [5,4,3], if ai is 4, we are looking for elements greater than 4. The first element (5) is greater, but then the next elements (4) is equal. So the rightmost element greater than ai is 5. So the sum is the frequency of 5.

Another example: ai is 3. All elements 5 and 4 are greater. So sum is 2+1=3.

So to find the number of elements in the sorted_ratings list that are strictly greater than ai, we can perform a binary search to find the first element in the sorted list that is <= ai, and take the index before that.

Wait, since the list is sorted in descending order, all elements before that index are > ai.

So for example, in the list [5,4,3], ai is 3. We look for the first element <= 3, which is the third element (3). So the index is 2. The elements before that (indices 0 and 1) are 5 and 4, which are greater. So the sum is sum of frequencies up to index 1 (i=1).

Wait, perhaps the binary search can find the position where the elements are > ai, and then sum the prefix up to that point.

Yes, so here's the plan:

1. Create a list of unique ratings, sorted in descending order.

2. Create a prefix sum array, where each element is the sum of frequencies up to that point. So prefix_sum[i] = sum of frequencies[0..i] in the sorted_ratings list.

3. For each ai in the original list, perform a binary search on the sorted_ratings list to find the largest index where the rating is > ai. The sum is the prefix_sum up to that index.

Then, the position is sum + 1.

This approach reduces the per-ai computation from O(k) (k being the number of unique elements) to O(log k) time.

So the steps are:

- Preprocess the frequencies, sort the unique ratings in descending order.

- Create a prefix sum array.

- For each ai in the input list, compute the sum of frequencies of ratings > ai by finding the rightmost element in the sorted_ratings list that is > ai, then take the prefix sum up to that index.

This would be O(n log k) time, where k is the number of unique ratings (up to 2000). For n=2000, log k is about 11 (since 2^11=2048), so 2000 * 11 = 22000 operations. That's very efficient.

So how to implement this in Python.

First, process the input:

n = int(input())

a = list(map(int, input().split()))

Then, create a frequency dictionary:

from collections import defaultdict

freq = defaultdict(int)

for num in a:

    freq[num] +=1

Then, sort the unique ratings in descending order:

sorted_ratings = sorted(freq.keys(), reverse=True)

Then create a prefix sum array:

prefix_sum = []

current_sum = 0

for rating in sorted_ratings:

    current_sum += freq[rating]

    prefix_sum.append(current_sum)

Now, for each ai in a, we need to find the number of ratings higher than ai. So we can perform a binary search on the sorted_ratings list to find the rightmost index where the rating is > ai. Then, the sum is the prefix_sum up to that index.

Wait, but the prefix_sum array is cumulative. For example, sorted_ratings is [5,4,3], and prefix_sum is [2,3,5]. So if the index is 0 (rating=5), sum is 2. If index is 1 (4), sum is 3, which is 2+1. So if ai is 4, we want the sum of ratings >4, which is 5's frequency (2). So in this case, the index would be 0 (since 5>4), and the sum is prefix_sum[0] = 2.

But how to find the index.

We can use the bisect module. Since the list is sorted in descending order, the bisect functions can be adjusted. For example, to find the first element <= ai, we can use bisect_left.

Wait, let's think: sorted_ratings is in descending order. For a given ai, the elements greater than ai are the first k elements. We can find the insertion point of ai into the sorted list, maintaining the order, which would be the first element <= ai. So the index of that insertion point is the first position where elements are <= ai. So all elements before that index are > ai.

For example, in the sorted list [5,4,3], for ai=4, the insertion point would be 1, because 4 is present at index 1. Wait, but bisect functions work with ascending order. So perhaps we need to reverse the logic.

Alternatively, perhaps we can use a key to make the bisect function work. But perhaps the easiest way is to invert the comparison.

Wait, since the list is sorted in reverse (descending order), the bisect functions will not work directly. Let's think about how to find the rightmost index where the rating is greater than ai.

The bisect module in Python has bisect_right and bisect_left. For a list sorted in ascending order, bisect_left returns the first position where the element is >= target. But here, our list is in descending order.

Hmm. Let's think of it this way: we want to find the index where the elements are greater than ai. So for example, in a list [5,4,3], ai=3. All elements are greater. So the insertion point (for ai in ascending order) would be 0 if the list is sorted in reverse.

Wait, perhaps this is getting complicated. Let's consider using the bisect module with a custom key. Alternatively, we can use the bisect_right function.

Wait, here's an approach. Since the list is sorted in descending order, for a given ai, we can use bisect_right to find the first index where the element is <= ai. For example:

In sorted_ratings = [5,4,3], for ai=4:

bisect_right finds the insertion point where ai would be inserted to maintain the order. Since the list is sorted in reverse, bisect_right(ai) in this list would return the index after the elements > ai. Wait, perhaps not. Let's see.

Wait, bisect_right works for lists in ascending order. So for a list in descending order, we need to reverse the comparison. So for example, for ai=4 in a list [5,4,3], in ascending order, bisect_right would return 2 (since in a sorted list [3,4,5], the insertion point for 4 would be 2). But in the reversed list, we need to find where to insert ai so that the list remains in descending order.

Alternatively, perhaps we can use the key parameter. But the bisect module does not support a key parameter. So perhaps another approach is needed.

Another idea: For the list sorted in descending order, to find the number of elements greater than ai, we can find the index where the elements are <= ai. All elements before that index are > ai.

So for example, in [5,4,3], ai=4. The elements > ai are [5], which is index 0. The elements <= ai are starting from index 1 (4,3). So the first index where the element is <= ai is 1. The sum is the sum of elements up to index 0.

Thus, the number of elements > ai is the index of the first element <= ai.

So the code for finding this index can be done via a binary search:

left = 0

right = len(sorted_ratings) - 1

res = len(sorted_ratings)  # if all elements are <= ai, then 0.

But how?

Alternatively, let's think of the list in reverse. But perhaps not. Let's think about how to find the first element that is <= ai.

Since the list is sorted in descending order, all elements before that are > ai.

So the steps for binary search:

Initialize left = 0, right = len(sorted_ratings) - 1.

Initialize pos = 0.

We are looking for the first position where sorted_ratings[pos] <= ai.

But since the list is in descending order, the elements are in order from high to low.

So for example, if the list is [5,4,3], ai=4:

We want to find the first index where the element is <=4. The first element is 5 (which is >4), then 4 (equal). So the first element <=4 is at index 1.

If ai=3, then the first element <=3 is index 2.

If ai=5, then all elements are >=5. So the first element <=5 is index 0. Wait, because sorted_ratings[0] is 5 which is equal to ai. So in that case, elements >ai are 0.

Hmm, so the code would need to find the first index where sorted_ratings[i] <= ai.

So how to perform this binary search.

The binary search can be written as follows:

low = 0

high = len(sorted_ratings) - 1

ans = len(sorted_ratings)

while low <= high:

    mid = (low + high) //2

    if sorted_ratings[mid] <= ai:

        ans = mid

        high = mid -1  # because we are looking for the first occurrence, so move left.

    else:

        low = mid +1

At the end, ans is the first index where sorted_ratings[mid] <= ai. All elements before ans are > ai.

So the sum is the prefix_sum up to ans-1. Because elements 0 to ans-1 are > ai.

If ans is 0, then no elements are > ai. Sum is 0.

Wait, let's test this logic.

Case 1: ai=3, sorted_ratings = [5,4,3].

Initial low=0, high=2.

mid=1 (4>3), so we go to else: low=2.

mid=2 (3<=3). ans=2, high=1.

Loop ends. ans=2.

sum is prefix_sum[1] (since ans-1 =1). prefix_sum[1] is 3 (sum of 5 and 4's frequencies). So sum is 3, which is correct.

Another test case: ai=4.

sorted_ratings = [5,4,3].

Looking for first index where element <=4.

mid=1 (4<=4), so set ans=1, high=0.

mid=0 (5>4), so low=1.

Loop ends. ans=1.

sum is prefix_sum[0] (1-1=0). sum is 2. Correct.

Another case: ai=5.

Looking for first index where element <=5. sorted_ratings[0] is 5 <=5. So ans=0. sum is prefix_sum[0-1] which is prefix_sum[-1], but that's invalid. So we need to handle ans=0 as sum 0.

Wait, sum is the sum of elements >ai. For ai=5, all elements in sorted_ratings are 5, so none are >5. So sum is 0.

Yes. So when ans is 0, ans-1 is -1, so sum is 0.

So the code for sum would be:

if ans == 0:

    sum =0

else:

    sum = prefix_sum[ans-1]

Thus, the code would be:

for each ai in a:

    perform binary search to find ans.

    if ans ==0:

        sum =0

    else:

        sum = prefix_sum[ans-1]

    position = sum +1

So integrating this into the code.

So in Python, the code would look like:

sorted_ratings = sorted(freq.keys(), reverse=True)

prefix_sum = []
current_sum =0
for r in sorted_ratings:
    current_sum += freq[r]
    prefix_sum.append(current_sum)

Then, for each ai in the original list:

left =0

right = len(sorted_ratings)-1

ans = len(sorted_ratings)

while left <= right:

    mid = (left + right) //2

    if sorted_ratings[mid] <= ai:

        ans = mid

        right = mid -1

    else:

        left = mid +1

if ans ==0:

    total =0

else:

    if ans-1 >=0:

        total = prefix_sum[ans-1]

    else:

        total =0

position = total +1

So that's the plan.

Now, putting this all together.

But wait, the code for the binary search can be written as a function, but in Python, for efficiency, perhaps inlining it is better. However, with n up to 2000, even if each binary search takes 10 steps, it's manageable.

Alternatively, can we precompute a map that for each possible ai (since ai can be up to 2000), precompute the sum?

Since ai can be up to 2000, and sorted_ratings is sorted, perhaps precomputing a dictionary where key is ai and value is the sum.

But in practice, for each unique ai, compute the sum once, then use it for all occurrences. Since the frequency can be up to 2000, but the unique ai's can also be up to 2000. So precomputing for all possible ai's (even those not present) would take O(2000) time.

Wait, but for example, if there are multiple students with the same ai, like the first sample input [1,3,3], the ai=3 will be processed twice. So precomputing for each unique ai would save some time.

But given that n is 2000, even if all are unique, the per-element binary search is manageable.

But perhaps precomputing a dictionary for all possible a is better. Let's think.

But the possible a's can be up to 2000. So for each possible a in 1..2000, compute the sum of frequencies of elements greater than a. Then for each student's ai, look up this sum and add 1.

This approach would take O(2000 * log k) time for precomputing, then O(n) time for the output.

But with k up to 2000 (since unique ratings can be up to 2000), 2000 * log(2000) is about 2000 *11=22000 steps. Which is negligible.

Thus, precomputing for all possible a from 1 to 2000, and then for each ai in the input list, just use the precomputed value.

But wait, what about a_i that are not in the list of possible unique ratings. For example, if the students have ratings 5, but the problem allows a_i up to 2000. So even if a certain value isn't present in the input, but could be present, the code would need to handle it.

But in the problem statement, the input a_i can be any integer from 1 to 2000. So for all possible a in 1..2000, compute the sum of frequencies of elements greater than a.

But how do we precompute that.

The same way as before. For each a in 1 to 2000, compute the sum using the binary search approach.

This way, for all a_i in the input, we can just look up the precomputed value.

So steps:

1. Read the input list a.

2. Compute the frequency map.

3. Sort the unique ratings in descending order.

4. Precompute a dictionary, sum_higher, where sum_higher[x] is the sum of frequencies of elements greater than x.

   For each x from 1 to 2000:

       perform binary search on sorted_ratings to find the sum of frequencies of elements >x.

5. Then, for each a_i in the original list, the position is sum_higher[a_i] +1.

But this approach would require 2000 binary searches, which is manageable.

Alternatively, since the sorted_ratings list is sorted, and for x in 1 to 2000, the sum can be computed by finding the first element <=x and summing all elements before that.

But what if x is not present in the sorted_ratings list?

No, the code is the same. For example, if x is 2, and the sorted_ratings list is [5,4,3], then all elements >2 are 5,4,3. So the sum is 2+1+2=5 (if frequencies are 2 for 5, 1 for 4, 2 for 3). So sum is 5. Then position is 6.

But the code for binary search would work for any x.

So precomputing sum_higher for all possible x from 1 to 2000 would be feasible.

But in practice, the maximum x is 2000, but in the input, the a_i can be up to 2000. So precomputing for all x in 1..2000.

But how to generate all possible x's.

But in Python, we can loop x from 1 to 2000 and precompute sum_higher[x] for each.

But perhaps it's better to compute sum_higher as a dictionary, even if some x's are not present in the input.

But the code can proceed as follows:

sum_higher = {}

for x in range(1, 2001):

    # perform binary search for x in sorted_ratings

    left =0

    right = len(sorted_ratings)-1

    ans = len(sorted_ratings)

    while left <= right:

        mid = (left + right)//2

        if sorted_ratings[mid] <=x:

            ans = mid

            right = mid -1

        else:

            left = mid +1

    if ans ==0:

        sum_h =0

    else:

        sum_h = prefix_sum[ans-1]

    sum_higher[x] = sum_h

Then, for each a_i in the original list, the position is sum_higher[a_i] +1.

This way, even if a_i is not present in the original list, the sum is correctly calculated.

But wait, the sorted_ratings list includes all the possible ratings in the input. So for example, if the input has no 2000, but x is 2000, the code will process it correctly.

But why? Because the code checks for all x in 1..2000.

Yes. So this approach is correct.

But the code may take some time to precompute sum_higher for 2000 values, but it's manageable.

So for the sample input 3, with a = [1,3,3], the sum_higher would be:

for x=1, sum_higher[1] is sum of all elements >1. The sorted_ratings would be [3,1]. Wait, no. Wait, in the first sample input, the list is [1,3,3], so unique sorted in descending order is [3,1]. So for x=3:

binary search for x=3 in [3,1]. We are looking for the first element <=3.

mid=0: sorted_ratings[0] =3 <=3 → ans=0. So sum_h is 0. Then sum_h is prefix_sum[ans-1] → ans-1 is -1. So sum_h is 0.

Wait, no. Wait, the sum of elements greater than x=3. Since sorted_ratings is [3,1], which are all elements. So elements greater than 3 are none. So sum_h is 0.

But according to the sample input 3, the first student (ai=1) has position 3. For ai=3, sum_h is 0 (since there are no elements >3), position is 0+1=1. Which matches the sample.

But for x=1:

binary search for x=1 in [3,1]. The first element <=1 is index 1 (since 3>1, then 1<=1).

ans=1. So sum_h is prefix_sum[ans-1] = prefix_sum[0] which is the sum of the first element (3's frequency, which is 2). So sum_h=2. So position is 3 (2+1). Correct.

So this approach works.

Another test case: third sample input:

5

3 5 3 4 5

unique sorted_ratings: [5,4,3]. frequencies: 5:2,4:1,3:2.

prefix_sum is [2,3,5].

sum_higher for x=5: binary search for 5 in [5,4,3]. The first element <=5 is index 0 (since 5<=5). So ans=0. sum_h=0. So position is 1.

For x=4: binary search for 4 in [5,4,3]. The first element <=4 is index 1 (4<=4). ans=1. sum_h is prefix_sum[0] (5's frequency, 2). sum_h=2. position is 3.

For x=3: binary search for 3 in [5,4,3]. sorted_ratings[2] is 3 <=3. ans=2. sum_h is prefix_sum[1] (sum of 5 and 4's frequencies: 2+1=3). position is 4.

Which matches the sample's output.

So this approach is correct.

Now, implementing this code.

First, code steps:

Read n and the list a.

Compute frequency dict.

Sort the unique elements in descending order.

Compute prefix_sum array.

Precompute sum_higher for all x from 1 to 2000.

Then, output for each a_i in a, sum_higher[a_i] +1.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    from collections import defaultdict

    freq = defaultdict(int)
    for num in a:
        freq[num] +=1

    sorted_ratings = sorted(freq.keys(), reverse=True)
    prefix_sum = []
    current_sum =0
    for r in sorted_ratings:
        current_sum += freq[r]
        prefix_sum.append(current_sum)

    sum_higher = {}
    max_rating = 2000
    for x in range(1, max_rating +1):
        left =0
        right = len(sorted_ratings)-1
        ans = len(sorted_ratings)  # default to all elements <=x
        while left <= right:
            mid = (left + right) //2
            if sorted_ratings[mid] <=x:
                ans = mid
                right = mid -1
            else:
                left = mid +1
        if ans ==0:
            total =0
        else:
            total = prefix_sum[ans-1] if ans-1 >=0 else 0
        sum_higher[x] = total

    # Now generate the output
    output = [sum_higher[num] +1 for num in a]
    print(' '.join(map(str, output)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
1
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

Sample input 3:

5

3 5 3 4 5

sum_higher for 3: sum of 5 and 4 → 2+1=3 → 3+1=4.

sum_higher[5] is 0 → 1.

sum_higher[4] is sum of 5 →2 → 3.

So output positions are 4,1,4,3,1. Correct.

Yes, this code should work.

Now, edge cases. Like when all students have the same rating. For example, n=2000, all a_i=5. Then sorted_ratings is [5], and sum_higher for 5 is 0. So each position is 1.

Another edge case: n=2000, a_i all distinct from 1 to 2000. Then sorted_ratings is [2000, 1999, ..., 1]. For x=2000, sum_higher is 0. For x=1999, sum_higher is 1 (frequency of 2000). So position is 2, etc.

But the code would handle that.

Now, considering the memory constraints. For sum_higher, it's a dictionary with 2000 entries, which is manageable.

The time for precomputing sum_higher is 2000 * O(log k), where k is the number of unique elements. For k=2000, log2(2000) is ~11. So 2000 * 11 = 22000 steps, which is acceptable.

Thus, the code should work efficiently within the constraints.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)
for num in a:
    freq[num] += 1

sorted_ratings = sorted(freq.keys(), reverse=True)
prefix_sum = []
current_sum = 0
for r in sorted_ratings:
    current_sum += freq[r]
    prefix_sum.append(current_sum)

sum_higher = {}
max_rating = 2000
for x in range(1, max_rating + 1):
    left = 0
    right = len(sorted_ratings) - 1
    ans = len(sorted_ratings)  # Default to all elements <= x
    while left <= right:
        mid = (left + right) // 2
        if sorted_ratings[mid] <= x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    total = 0
    if ans > 0:
        total = prefix_sum[ans - 1] if (ans - 1) < len(prefix_sum) else 0
    sum_higher[x] = total

output = [sum_higher[num] + 1 for num in a]
print(' '.join(map(str, output)))
```
