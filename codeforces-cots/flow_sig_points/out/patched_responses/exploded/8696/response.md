<think>
Okay, let's see. The problem is to find the minimum number of insertions required so that no subsegment (contiguous elements) of the resulting array has a sum of zero. The original array can't have zeros, but after inserting elements, we have to make sure that any possible contiguous subarray in the modified array doesn't sum to zero.

Hmm. So the approach here is to find where the current array has subarrays with sum zero and then figure out how to break them with insertions. But wait, the original array might not have any such subarrays, like in the second example. Then the answer is zero.

But when there are such subarrays, inserting elements can split them into parts where their sums can't form a zero. So the key is to find all the subarrays in the original array that sum to zero and then determine how to insert the minimal number of elements to break all these possibilities.

But checking all possible subarrays is impossible because there are O(n^2) of them. So we need an efficient way to track the required insertions.

Let me think. The problem resembles the problem where we need to split the array into the maximum number of segments such that the sum of each is zero. But here, the goal is different. Wait, maybe we can model this using prefix sums.

The idea is that if two prefix sums are equal, then the subarray between those indices has a sum of zero. So, in the original array, any occurrence of a repeated prefix sum indicates a zero-sum subarray. To prevent any such subarrays in the modified array, we need to ensure that no two prefix sums in the modified array are the same. Because if any two are the same, the subarray between them sums to zero.

But inserting elements changes the prefix sums. So, the approach here is similar to making sure that all prefix sums are unique. But how does inserting elements affect this?

Wait, let's consider the original array. The prefix sums of the original array might have duplicates. Each duplicate pair corresponds to a zero subarray. To break all such possibilities, we need to insert elements in such a way that when we process the original array, whenever a prefix sum repeats, we insert a "barrier" to split the array into parts where the prefix sums are reset. 

Wait, perhaps the solution is to track the current prefix sum and whenever a duplicate is found, we insert a separator. Then, after inserting, the prefix sums are reset, so that in the new sections, the prefix sums don't have duplicates.

This sounds similar to the problem of splitting the array into as many parts as possible such that each part has no duplicate prefix sums, which would minimize the number of required insertions. Because each split requires inserting a single element (since insertions are between existing elements, each split corresponds to inserting one element).

So the minimal number of insertions is equal to the number of splits needed minus one. Or wait, each time we split, we need to insert one element. So if we split the array into k parts, then the number of insertions is (k-1). 

But how do we split the array into such parts where each part has unique prefix sums? 

The approach here is to use a greedy algorithm. We can track the prefix sums as we go, and whenever a duplicate is found, we split the array at this point. Then, reset the set of seen prefix sums, and continue. This would ensure that each split part has unique prefix sums, thus avoiding any zero subarrays.

So the algorithm would be:

1. Iterate through the array, keeping track of the prefix sum.
2. Maintain a set of seen prefix sums for the current segment.
3. For each element, add the current element to the prefix sum.
4. If the current prefix sum has been seen before in the current segment, or if the current sum is zero (since that implies the subarray from the start to here sums to zero), then we must split here. Increment the insertion count (since inserting one element here splits the array), reset the prefix sum and the seen set, and start a new segment.
5. Otherwise, add the current prefix sum to the seen set.

Wait, but the initial sum is zero before processing any elements. Hmm, perhaps the initial sum is zero. For example, when the first element is the sum of the entire segment (prefix sum after first element is a_1). So, if the first element is x, then the prefix sum after processing it is x. But if x is zero, but the original array doesn't contain zeros. So that's not a problem.

Wait, but the sum zero could be formed by a subarray starting from the first element. For example, if the prefix sum at index i is zero, then the subarray from start to i has sum zero. So we need to check for that as well.

So, the algorithm would check for each step whether the current prefix sum is zero (sum from start to current is zero) or if the prefix sum has been seen before. If either case is true, we split here.

Wait, but when you split here, you insert an element, which creates a new element. So after inserting, the next segment starts with the next element. But the split is done before the current element. Hmm, maybe I need to adjust the approach.

Alternatively, let's model the process of building the modified array. Each time we process elements, whenever adding the next element would cause a prefix sum that's already been seen in the current segment (or zero), we insert a separator (which can be any value, but the sum of the current segment up to that point plus the inserted element's value is such that no subarray in the new segments can sum to zero). But the key is that inserting a separator resets the prefix sums.

But how to model this. Let's think of it as after inserting a separator, the next elements form a new segment, and their prefix sums start from zero again. Wait, no. Because the separator is a new element. For example, suppose the original array is [a, b]. If we insert x between them, the new array is [a, x, b]. The prefix sums would be a, a+x, a+x+b. So the inserted element x affects the prefix sums of the subsequent elements.

But the problem allows us to insert any elements. So the optimal strategy is to insert elements in such a way that after each insertion, the new segments' prefix sums do not repeat and do not include zero. But how to model this with minimal insertions.

Alternatively, the minimal number of insertions is determined by the number of times we need to split the array into segments where each segment's prefix sums (starting from the beginning of the segment) are unique and not zero. Because in each such segment, any subarray sum cannot be zero. Because if a subarray in the segment has sum zero, that would imply that two prefix sums in that segment are equal (or the prefix sum is zero), which we prevent by splitting.

So the algorithm is as follows:

Initialize a set to keep track of the prefix sums in the current segment. Also, track the current prefix sum. For each element in the array:

- Add the current element to the current prefix sum.
- Check if the current prefix sum is zero (meaning the subarray from the start of the current segment to this point has sum zero) or if the sum is already present in the set.
- If either is true, then we must split here. Insert a separator (count += 1), reset the current prefix sum to zero (since after insertion, the next segment starts with zero prefix sum?), and clear the set. Also, add the current element's value to the prefix sum (since after inserting, the next element is part of the new segment). Wait, perhaps not.

Wait, after inserting a separator, the new segment starts processing the current element. Because the insertion is before the current element. So when we split after the previous element, the current element is part of the new segment. So the next step would be:

When a split is needed before the current element, we reset the prefix sum to zero and the set to {0} (since the new segment's initial prefix sum is zero). Then, add the current element's value to the prefix sum. Then check if this sum is zero or exists in the set (which now starts fresh for the new segment).

Wait, maybe I need to model the current segment's prefix sums. Let's think:

We process elements one by one. For the current segment, we track the prefix sums. The initial state is that the current sum is zero (before processing any elements in the segment). For each element in the array:

- Add the element to the current sum.
- Check if the current sum is zero (sum of this segment's elements up to now is zero) or if the sum was already present in the set.
- If yes, then we need to split before this element. So, insert a separator here (count += 1), reset the current sum to zero (because the new segment starts here), and reset the set to {0} (since the new segment's prefix sum starts at zero before adding this element).
- Then, process the current element as the first element of the new segment. So add it to the sum (sum becomes element's value), check if it's zero or in the new set. If not, add to the set. If yes, then this element alone is a problem (but since the original array has no zeros, that's impossible). Wait, but the original array elements are non-zero. So in the new segment, the sum after processing the first element is non-zero. So adding it to the set would not have a zero sum.

Wait, let's see with an example.

Suppose we have a segment that starts with element a. The prefix sum starts at zero. Then after adding a, the sum is a. Since a is non-zero, this sum is not zero. So we add it to the set. So for the first element of a new segment, the sum is a (non-zero), so it's safe. Then the next element is b. Sum becomes a + b. Check if this sum is zero or already in the set. If yes, split here.

So the algorithm would be:

Initialize:

count = 0
current_sum = 0
seen = set()
seen.add(0)  # because the initial sum before any elements is zero.

Wait, wait. For each new segment, the initial sum is zero (before processing any elements of the segment). So when processing the first element of the segment, the sum becomes a_i. Then, we need to check if this sum is zero (but a_i is non-zero, so that's not possible) or if it's in the seen set. But the seen set for the new segment includes 0 (initial sum) and then the sum after the first element.

Wait, no. Let me re-express:

For each segment, the processing starts with sum = 0 (before processing any elements in that segment). The set seen contains 0. Then, when we process each element in the segment:

sum += a_i

if sum is in seen or sum is zero (but sum can't be zero because the original elements are non-zero, but after inserting elements, the sum can't have any subarrays with sum zero. Wait, but the original array's elements are non-zero, but the inserted elements can be anything. But in our approach, we are trying to split the original array into segments where each segment's prefix sums (as processed) are unique and not zero. So the algorithm must ensure that within each segment, no two prefix sums are equal and none are zero. So for each segment, the initial sum is zero (before any elements), then we add elements one by one. For each element added, the new sum is checked against the seen set (which includes all previous prefix sums, including the initial zero). If the new sum is already in the set (which includes zero), then we have a problem. So we need to split before this element.

So here's the correct approach:

Initialize a variable count to 0. Also, a set seen that starts with 0 (the initial sum before any elements in the current segment). The current_sum is 0.

For each element in the array:

current_sum += element

if current_sum is in seen or current_sum == 0:
    count += 1
    # Insert a separator before this element. So the current element starts a new segment.
    # Reset the seen set and current_sum.
    seen = {0}
    current_sum = element  # because in the new segment, the sum starts at 0, then adding the element gives element as the sum.
    # Check if this new sum is already in the new seen (which contains 0 and element if added)
    # But since element is non-zero, the sum is element, which is not zero. But we need to check if it's in the new seen set (which now is {0}).
    # So after adding, current_sum is element. Check if it's in seen (0) or is zero. If it's not, add to seen.
    if current_sum in seen or current_sum == 0:
        # This can't happen because element is non-zero and seen is {0}, so current_sum (element) is not in seen and not zero.
        # So proceed.
    seen.add(current_sum)
else:
    seen.add(current_sum)

Wait, but after splitting, the current element becomes the first element of the new segment. So for example, after splitting, we reset the current_sum to 0, then add the current element. So the sum becomes the element's value. Then, check if that sum is in the new seen (which is {0}), which would be true only if the element is zero (but original elements are non-zero). So the new sum (element) is not in seen, so add it to the seen.

So the algorithm becomes:

count = 0
current_sum = 0
seen = set()
seen.add(0)

for num in array:
    current_sum += num
    if current_sum in seen or current_sum == 0:
        count +=1
        # split here, reset
        seen = {0}
        current_sum = num
        # now, current_sum is num, which is non-zero. Check if in seen (0)
        # if yes, but it's impossible because num is non-zero. So add to seen.
        seen.add(current_sum)
    else:
        seen.add(current_sum)

Wait, but when we split, the current element is part of the new segment. So after splitting, the new segment's prefix sum starts at 0 (before processing the current element), then adding the current element gives sum = num. So the new seen set is {0, num}.

But the code above, after splitting, adds the num to the seen. So that's correct.

Let's test this algorithm on the first example:

Example 1:
4
1 -5 3 2

The array is [1, -5, 3, 2].

Processing:

Initialize seen={0}, current_sum=0.

First element is 1:

current_sum = 0 +1 =1.

Check if 1 is in seen (no) and not zero. So add 1 to seen. Now seen is {0,1}.

Second element is -5:

current_sum =1 + (-5) = -4. Check if -4 is in seen (no) and not zero. Add to seen. Now seen {0,1,-4}.

Third element is 3:

current_sum =-4 +3 = -1. Check: not in seen. Add. Now seen {0,1,-4,-1}.

Fourth element is 2:

current_sum =-1 +2=1. Check if 1 is in seen (yes, exists). So need to split.

count becomes 1.

Reset seen to {0}, current_sum is set to 2 (since the current element is now part of the new segment. So after splitting before 2, the new segment starts with 2. So sum is 2. Check if 2 is in seen (no) and not zero. Add to seen. Now seen {0,2}.

Thus, the total count is 1. Which matches the example.

Another example: third input.

Input:

9
-1 1 -1 1 -1 1 1 -1 -1

The array is [-1, 1, -1, 1, -1, 1, 1, -1, -1].

Processing step by step:

Initialization: seen = {0}, current_sum=0.

Processing first element -1:

sum becomes -1. Not in seen, not zero. Add to seen. seen {0, -1}.

Second element 1: sum is 0. Oh, sum is zero. So we have to split here.

count becomes 1. Reset seen to {0}, current_sum =1 (since the split is after the first element, and the next element is 1). Check if sum is 1. Not in seen, add. seen {0,1}.

Third element -1: sum becomes 0. Again sum is zero. Split again. count becomes 2. Reset seen to {0}, current_sum =-1. Check if -1 is in seen (no), add to seen. seen {0,-1}.

Fourth element 1: sum is 0. Split again. count becomes 3. Reset seen to {0}, current_sum=1. Add to seen. seen {0,1}.

Fifth element -1: sum becomes 0. Split again. count 4. Reset seen. current_sum=-1. Add.

Sixth element 1: sum 0. Split again. count 5. Reset. current_sum=1. Add.

Seventh element 1: sum is 2. Not in seen, add. seen {0,1,2}.

Eighth element -1: sum 1. Not in seen, add. sum=1, seen now {0,1,2,1} → no, wait sum is 2 + (-1) =1. Check if 1 is in seen (yes, because seen is {0,1,2}).

So sum 1 is already present. So split here. count becomes 6. Reset seen to {0}, current_sum = -1. Add to seen.

Ninth element -1: sum becomes -2. Not in seen, add. So total count is 6. Which matches the example.

So the algorithm works here.

Another test case:

Second example:

5
4 -2 3 -9 2

Processing:

sum starts at 0. After adding 4: 4. Not in seen, add. Then -2: 2. Not in seen. Then 3: 5. Not in seen. Then -9: -4. Not in seen. Then 2: -2. Not in seen. So no splits. Count is 0. Correct.

Third example: the output is 6.

So the algorithm seems to work.

So the code needs to process each element in the array, track the current sum and the seen set. When a split is needed (sum in seen or sum zero), increment the count, reset the seen set and current sum.

Now, in Python, using a set for each segment is manageable, but with n up to 2e5, we need to make sure that the code is efficient. Using a hash set (Python's built-in set) should be O(1) per insertion and lookup on average.

But for each split, we create a new set. But in the worst case, splits could be O(n), leading to O(n) set operations, which is acceptable.

So the code will be:

Read n and the array.

Initialize count = 0, current_sum = 0, seen = {0}.

Loop through each number in the array:

current_sum += num

if current_sum in seen or current_sum == 0:

    count +=1

    seen = set()

    seen.add(0)

    current_sum = num

    if current_sum in seen or current_sum ==0:

        # impossible, since num is non-zero and seen is {0}

        # so add to seen

        seen.add(current_sum)

else:

    seen.add(current_sum)

Wait, but after splitting, the current_sum is set to num. Then, since seen is {0}, current_sum is added to the new seen.

So the code would be:

In Python:

n = int(input())
a = list(map(int, input().split()))

count = 0
current_sum = 0
seen = {0}

for num in a:
    current_sum += num
    if current_sum in seen or current_sum == 0:
        count +=1
        seen = {0}
        current_sum = num
        seen.add(current_sum)
    else:
        seen.add(current_sum)

print(count)

Wait, but in the case of splitting, after setting current_sum to num, we add it to the seen. Because after the split, the new segment starts with this num, and we need to track the prefix sum of the new segment.

Yes. For example, after splitting, the new segment starts with current_sum = num. The seen set is {0} (the initial sum), then adding num to the sum (since the initial sum is 0, the new sum is num). We check if num is in the seen (0), which it's not (since num is non-zero). So we add it to the seen. The next elements in the new segment will be processed with this seen set.

So this code should work.

Testing this code on the first example:

Processing the elements:

Initial seen is {0}, current_sum 0.

First num: 1. current_sum +=1 → 1. Check if 1 is in seen (no) and not zero. So add to seen. seen becomes {0,1}.

Second num: -5. current_sum becomes -4. Check: not in seen, not zero. Add to seen.

Third num:3. sum becomes -1. Add.

Fourth num:2. sum becomes 1. Check if in seen (yes, 1 is in seen). So count increments to 1. Reset seen to {0}, current_sum is 2. Add 2 to seen. Now seen is {0,2}.

No more elements. The code outputs 1. Correct.

Another test case: when the array starts with a zero sum. Wait, but the original array has no zeros. So sum can't be zero unless it's a subarray.

But the code checks for sum being zero. For example, if a segment's sum becomes zero (the sum from the start of the segment to current element is zero), then split. But this can happen even if the individual elements are non-zero. For example, if the array is [1, -1]. The sum after the first element is 1, which is not zero. After the second, sum is 0. So the code checks and splits here.

So the code seems correct.

Now, considering the third example. The code would split each time the sum is zero, leading to 6 splits.

Thus, the code should work.

But what about the fourth example:

Input:

8

16 -5 -11 -15 10 5 4 -4

Output is 3.

Let's see:

The array is [16, -5, -11, -15, 10,5,4,-4].

Processing:

current_sum starts at 0. seen = {0}.

Process 16:

sum is 16. Not in seen, add. seen {0,16}.

Process -5: sum 11. Add.

Process -11: sum 0. Split here. count becomes 1. Reset seen to {0}, current_sum =-11. Add to seen. seen {0,-11}.

Process -15: sum-11 + (-15) =-26. Not in seen. Add.

Process 10: sum-26 +10 =-16. Add.

Process5: sum-11. Add.

Process4: sum-7. Add.

Process-4: sum-11. Already in seen (sum -11 is in seen). Split. count becomes 2. Reset seen to {0}, current_sum =-4. Add. seen {0,-4}.

But now, after processing the split, the next elements are the remaining elements (none). So total count is 2?

Wait, but according to the sample input, the output is 3.

Hmm. So maybe this code isn't correct. Let me step through the fourth example step by step.

Original array: [16, -5, -11, -15, 10,5,4,-4]

Let's process each element:

Initialize count=0, current_sum=0, seen={0}.

Process 16:

sum +=16 →16. Check: 16 not in seen (0), sum not zero. Add to seen. seen={0,16}.

Process -5: sum 11. Check: not in seen. Add. seen {0,16,11}.

Process -11: sum 0. Oh, sum is zero. So split here. count +=1 (now 1). Reset seen to {0}, current_sum =-11. Add to seen. seen={0,-11}.

Process -15: sum -11 + (-15) =-26. Check: not in seen. Add. seen {0,-11, -26}.

Process 10: sum -26 +10 =-16. Add. seen {0,-11,-26,-16}.

Process5: sum -16 +5 =-11. Check: -11 is in seen. So split here. count becomes 2. Reset seen to {0}, current_sum=5. Add to seen. seen={0,5}.

Process4: sum 5+4=9. Not in seen. Add. seen {0,5,9}.

Process-4: sum 9 + (-4)=5. Check: 5 is in seen. Split. count becomes3. Reset seen to {0}, current_sum=-4. Add. seen={0,-4}.

Now all elements processed. The total count is 3. Which matches the sample output.

So why in the previous step-by-step processing of the code, when processing the elements, after the fifth element (5), the sum is -11 (current_sum =5?), no. Wait, perhaps I made a mistake in tracking the steps.

Let me re-do for the fourth example step by step:

Initialization:

count=0

current_sum=0

seen = {0}

Processing each element:

1. 16:

current_sum =0 +16=16.

Check if 16 is in seen (no) and sum is 16≠0. Add to seen. seen={0,16}.

2. -5:

sum=16-5=11. Not in seen. Add. seen {0,16,11}.

3. -11:

sum=11-11=0. sum is zero → split. count=1.

Reset seen to {0}, current_sum =-11.

Add -11 to seen. seen={0,-11}.

4. -15:

sum =-11 + (-15) =-26. Check: not in seen. Add. seen {0,-11,-26}.

5.10:

sum =-26 +10 =-16. Not in seen. Add. seen {0,-11,-26,-16}.

6.5:

sum =-16 +5 =-11. Check: -11 is in seen. So split. count=2.

Reset seen to {0}, current_sum=5. Add to seen. seen={0,5}.

7.4:

sum=5+4=9. Not in seen. Add. seen {0,5,9}.

8.-4:

sum=9-4=5. 5 is in seen. Split. count=3.

Reset seen to {0}, current_sum=-4. Add to seen. seen={0,-4}.

Total count is 3, which is correct.

So the code works for this case.

Thus, the code seems correct. But why, when processing the fifth element (5) in the fourth example, the sum is -11. Because after the previous split (after -15, 10, etc.), the current_sum was -26 +10 = -16, then 5 is added, sum is -11. So yes.

Thus, the code is correct.

So the code will read the array, track the current sum and seen set, and increment the count whenever a split is needed.

Now, to handle the time and memory constraints:

n is up to 2e5. For each element, we perform O(1) operations (hash set add and lookups). So the time is O(n), which is acceptable.

In Python, using a set for each split is manageable. Even if there are O(n) splits, each set is O(1) per element (each element is added to exactly one set). The total memory is O(n), which is acceptable.

Thus, the code should work correctly and efficiently.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

count = 0
current_sum = 0
seen = {0}

for num in a:
    current_sum += num
    if current_sum in seen or current_sum == 0:
        count += 1
        seen = {0}
        current_sum = num
    seen.add(current_sum)

print(count)
```