<think>
Okay, let's tackle this problem. The task is to find, for each element in the array, the distance to the nearest zero. The constraints are tight: n can be up to 2e5, so any O(n^2) approach is definitely out of the question. We need something linear or O(n) time.

Hmm. So how to approach this? Let's think. For each element, we need to know the closest zero to the left and the closest zero to the right, then take the minimum of those two distances.

Wait, right. Because the nearest zero could be on either side. For example, in the third sample input, the element at index 3 (value 1) has a zero two steps to the left and no zero to the right until after. Wait, no, in that case, the nearest zero is the one at index 2 (distance 1). Then for the element at index 4 (value -2), the closest zero is at index 2 (distance 2), and so on.

So the idea is to track the last zero encountered from the left, then track the next zero from the right, and for each position, compute the minimum distance between the two.

But how to do this efficiently?

One common approach for such problems is a two-pass method. Here's how it works:

1. First pass: left to right. For each element, keep track of the last zero's position. The distance is current index - last_zero_index. If we haven't encountered any zero yet, we can set the distance to a large value (since we don't have any zeros to the left yet). However, since the problem states that there's at least one zero, maybe during the first pass, the initial large values will be overwritten in the second pass.

2. Second pass: right to left. Similarly, track the last zero encountered and compute the distance as last_zero_index - current index. Then, take the minimum of the two passes for each position.

Wait, but how to handle the initial state where there's no previous zero? For example, for elements before the first zero in the array. In the first pass (left to right), when moving left to right, until the first zero is found, all those elements would have their left distance as infinity. But the nearest zero could be to the right (the first zero). Then, when we do the right pass, for elements after a zero, we track the next zero. So combining these two passes, each position's distance is the minimum of the left pass and right pass.

Yes. Let's work through an example. Take the input 5: 0 1 2 3 4. The left pass would have first zero at index 0, so for each position i, left distance is i - 0. So left distances are 0,1,2,3,4. Then the right pass would track zeros from the right. The first zero from the right is at index 0. So for each position i, the right distance is 0 - i (but since i is left of 0, that's negative, but that's not possible. Wait, no. Wait, in the right pass, we track the last zero as we move from right to left. So for example:

In the right pass, we start from the end. For the array 0 1 2 3 4:

Right pass:

Initialize last_zero = -infinity (or some value indicating that we haven't seen a zero yet). Then, we start at index 4 (element 4). Since there's no zero after it (since we are moving right to left, but the current element is 4, not zero). So the right distance for index 4 is infinity. Then index 3 (element 3) same. ... until index 0 (element 0). Here, we update last_zero to 0. Then, for elements to the right of index 0 (which are indices 1-4), when we process them in the right pass, the last_zero is 0. So the right distance for index 1 would be 0 (since last_zero is 0, 0 - 1 is negative, but we take absolute value? Wait, no. Wait, the right pass is moving from right to left, but the distance would be the next zero to the right (from the original array's perspective). So when moving right to left, the next zero in the original array's right would be tracked.

Wait, perhaps the right pass is a bit more confusing. Let's think again.

Let me think of the right pass as follows: for each position i, the distance to the next zero that is to the right of i. Wait, but if we process from the end to the start, then for each i, the next zero to the right (in the original array) is the last_zero encountered so far (since we're moving from right to left).

Wait, maybe I need to rephrase.

In the left to right pass:

We keep track of the previous zero. For each element at i, the distance from the previous zero (left side).

In the right to left pass:

We keep track of the next zero (right side). For each element at i, the distance from the next zero (right side).

So during the right pass, we start from the end and move left, keeping track of the last zero encountered. For each i, the next zero is the last one we've seen so far. Then, for the current i, the right distance is (last_zero - i) if last_zero is not set. But wait, when moving right to left, the next zero for i would be the first zero encountered when moving towards the right (i.e., to the right in the array). So for example, for the array [5,6,0,1,-2,3,4], the third sample input.

The right pass would track zeros as we move from the end to the start. Let's see:

Original array indexes 0-6:

5,6,0,1,-2,3,4

Right pass:

Start at i=6 (element 4). No zeros seen yet, so right distance is infinity.

i=5 (3), no zeros, distance infinity.

i=4 (-2), no zeros.

i=3 (1), no zeros.

i=2 (0). Now, we set last_zero to 2. The distance here is 0 (since it's a zero). Then, for i=1 (6), the right distance is 2-1 =1. For i=0 (5), the right distance is 2-0=2.

So the right distances would be [2,1,0, ... ] for the first few elements.

So combining left and right passes:

Left pass:

Initialize last_zero to -infinity. Then:

For each i from 0 to n-1:

if a[i] is 0, then last_zero = i, and distance[i] =0.

else:

if last_zero is -infinity (no zeros seen yet), then distance_left[i] = some large number.

else, distance_left[i] = i - last_zero.

Then, right pass:

Initialize next_zero to +infinity.

For each i from n-1 downto 0:

if a[i] is 0, then next_zero = i, distance_right[i] =0.

else:

if next_zero is +infinity, then distance_right[i] = some large number.

else, distance_right[i] = next_zero -i.

Wait, no. Wait, during the right pass, the next_zero is the index of the zero encountered to the right (from the current position). So, when moving from right to left, for each position i, if a[i] is zero, then next_zero becomes i. For non-zero elements, the distance from the next zero (to the right) is next_zero - i.

But wait, in the right pass, when moving from right to left, the next zero for i is the next_zero that is to the right of i. So for example, for i=3 in the third sample input (element 1), the next_zero is 2 (which is to the left of i in terms of indexes, but in the array, it's to the left, not the right). Wait, this seems conflicting.

Wait, maybe I have the directions confused. Let's think again.

The right pass is supposed to find the distance to the next zero that is to the right of the current element. So for each element i, we need the distance to the first zero that occurs after i (i.e., to the right). So when processing from right to left, whenever we hit a zero, we update next_zero to i. For each element before that (to the left of it), their distance to the next zero is next_zero - i (since next_zero is the first zero to their right). But if there is no such zero (i.e., next_zero hasn't been updated yet), then the distance is considered as infinity.

Wait, for example, in the third sample input:

Original array: indexes 0-6.

Elements: 5,6,0,1,-2,3,4.

The right pass starts at i=6 (element 4). Since it's not zero, and next_zero is infinity (initially), so distance_right[6] is infinity. Then i=5 (3): same. i=4 (-2): same. i=3 (1): same. i=2 (0): set next_zero to 2. distance_right[2] =0. Then i=1 (6): next_zero is 2, so distance is 2-1=1. i=0 (5): next_zero is 2, so distance 2-0=2.

So for the third sample, the right pass gives:

distance_right = [2,1,0,1,2,3, infinity]. Wait, but wait the array is 5,6,0,1,-2,3,4. So for i=3 (element 1), next_zero is 2 (the first zero to the right of i=3 is the same as i=2, but in the array, i=2 is to the left of i=3. So this suggests that the right pass is actually considering the next_zero as the first zero to the left (when moving from right to left). That can't be right. So perhaps I have the direction mixed up.

Wait, perhaps the right pass is supposed to capture the nearest zero to the right (i.e., after the current element), but when moving from right to left, the next_zero would be the first zero encountered when moving to the left (i.e., to the left of the current element). So that approach would not capture zeros to the right. Wait, this is confusing.

Let me think of the array [5,6,0,1,2,0,4]. For element at index 3 (value 1), the nearest zero is index 2 (distance 1). The next zero to the right is index 5 (distance 2). So the minimum is 1. So the right pass for this element would be 2 (5-3=2), left pass would be 3-2=1. So the minimum is 1. But how does the right pass get the distance from the right zero?

Alternatively, perhaps the right pass should be tracking the next zero that is to the right of the current element. So when moving from right to left, we can track the next zero's position. For example, in the array [5,6,0,1,2,0,4], moving from the end (index 6) to the left:

At index 6 (element 4), not zero. So next_zero is undefined (infinity). Distance right is infinity.

At index 5 (element 0): next_zero is set to 5. Distance is 0.

At index 4 (element 2): next_zero is 5. So distance is 5-4=1.

At index 3 (element 1): next_zero is 5. Distance is 5-3=2.

At index 2 (element 0): next_zero is set to 2. Distance is 0.

At index 1 (element 6): next_zero is 2. Distance is 2-1=1.

At index 0 (element 5): next_zero is 2. Distance is 2-0=2.

So in this case, the right pass for index 3 is 2, and the left pass would have the previous zero at index 2. So left pass is 3-2=1. So the minimum is 1.

Ah, I see. So the right pass gives the distance to the next zero to the right (i.e., after the current index), but when moving from right to left, whenever we find a zero, we update the next_zero variable. Then, for elements to the left of that zero (i.e., with smaller indices), their distance to the next_zero (which is the first zero encountered to the right of them) is next_zero - current index.

Wait, yes. Because when moving from right to left, when you hit a zero at position j, any position i < j (to the left of j) will have their next_zero as j, until another zero is found. So, for each i < j, their next_zero is j. So the distance is j - i.

So in the example above, for i=3 (element 1), the next_zero is 5. So the right distance is 5-3=2, but the left distance is 3-2=1, so the minimum is 1.

So combining the two passes, the correct answer is the minimum of left and right distances for each position.

Now, the problem requires us to compute this for each element.

So the approach is:

1. Initialize a result array with the same length as the input array.

2. First pass (left to right):

   - Track the last_zero index. Initially, set to -infinity (indicating no zero encountered yet).

   - For each i from 0 to n-1:

      - if a[i] is zero:

          - set last_zero to i.

          - result[i] = 0.

      - else:

          - if last_zero is not -infinity:

              - result[i] = i - last_zero.

          - else:

              - result[i] = infinity (since no zeros have been encountered yet).

3. Second pass (right to left):

   - Track next_zero index. Initially, set to +infinity (indicating no zero encountered yet).

   - For each i from n-1 downto 0:

      - if a[i] is zero:

          - set next_zero to i.

          - current_min = 0 (since this is a zero).

      - else:

          - current_right_distance = next_zero - i (if next_zero is not +infinity).

          - current_min = min(result[i], current_right_distance).

      - set result[i] to current_min.

4. The final result array is the answer.

Wait, but during the right pass, for elements where next_zero is +infinity (i.e., no zeros to the right), then the current_right_distance would be invalid. But the problem says that there's at least one zero in the array, so during the left pass, for elements before the first zero, the left distance is infinity (but the right pass will have the first zero's distance from the right. For example, in the second sample input:

Input 5: 0 1 2 3 4.

Left pass:

For i=0, it's a zero, so result[0] = 0.

For i=1, last_zero is 0. result[1] = 1-0=1.

For i=2: last_zero is 0. result[2] =2-0=2.

Similarly, up to i=4, result[4] =4.

Then, during the right pass:

Start from i=4 (element4). next_zero is +infinity. current_right_distance is infinity. So the current_min is min(4, infinity) →4. So result remains 4.

i=3: element3. next_zero is +infinity. So current_right_distance is infinity. result[3] is 3 (from left pass), min(3, inf) →3.

i=2: element2. next_zero is +infinity. So same, result[2] remains 2.

i=1: next_zero is +infinity. result[1] remains 1.

i=0: a[i] is zero. So next_zero is set to 0. So result[0] is 0.

Wait, but the right pass for elements before the first zero (if any) will have next_zero as the first zero. But in the left pass, those elements have their left distance as infinity, but during the right pass, their right distance is next_zero - i (the first zero to the right, which is the first zero in the array). So for example, in the first sample input:

Original array: 2 1 0 3 0 0 3 2 4

Left pass:

The first zero is at index 2.

For indices 0 and 1: during left pass, last_zero is -infinity, so their left distance is infinity. Then, during the right pass, for index 0 and 1, next_zero is the first zero (index2). So their right distance is 2 -0=2 and 2-1=1. So the min between left (infinity) and right (2,1) is 2 and 1. Which is correct.

So the algorithm works.

So the steps are:

- Left pass: compute the distance to the previous zero (left side).

- Right pass: compute the distance to the next zero (right side), and take the minimum of left and right.

Now, in code, how to implement this efficiently?

We need to process the array in two passes. For each pass, we can keep track of the last zero's position.

In Python, we can initialize an array of the same length as the input. Then, in the first pass, for each element, compute the left distance, and store it. Then, during the right pass, compute the right distance and compare with the existing value, taking the minimum.

But for Python, handling n=2e5 is manageable. Let's see:

First, read the input. The input is n, then the list of a's.

In Python, for n=2e5, using list comprehensions is efficient.

Now, code steps:

Read n, then the array.

Initialize a result array with the same length as a.

First pass (left to right):

last_zero = -infinity (we can represent this as -infinity, but in Python, perhaps using a variable that is initially set to a value indicating that no zero has been found yet. For example, set last_zero to -infinity. Then, during the first pass:

for i in range(n):

    if a[i] == 0:

        result[i] = 0

        last_zero = i

    else:

        if last_zero == -infinity:

            # no zeros to the left, so left distance is infinity.

            # but since the problem states there's at least one zero, during the right pass, this will be updated.

            result[i] = float('inf')

        else:

            result[i] = i - last_zero

Wait, but when we do the right pass, the next_zero starts as +infinity, and during the right pass, the code would compute next_zero - i, but if next_zero is +infinity, that's not possible. So in the right pass, for elements where next_zero is still +infinity (no zeros to the right), the current_right_distance is next_zero - i (which would be +infinity minus i). But in Python, that's handled as infinity. Then, the min between the left distance (which could be infinity) and the right distance (infinity) would be incorrect. But according to the problem statement, there is at least one zero, so this should not happen. Because during the right pass, once a zero is encountered, next_zero is set. For example, in the left pass, the elements after the last zero would have their left distance set to their position minus last_zero. But during the right pass, when moving from the end, the next_zero would be set to the last zero encountered. So in the right pass, after processing the last zero (which is the first in the right pass), the next_zero would be set, and all elements to the left of it (i.e., higher indices in the array) would have their right distance computed correctly.

Wait, perhaps the right pass should start with next_zero as +infinity, and during processing, when a zero is found, update next_zero to i. For each non-zero element, the right distance is next_zero - i. But in the case where next_zero is +infinity, this would be a very large number, which would be larger than the left distance (if any). So during the right pass, for elements that have no zero to their right (which can't happen according to the problem statement), the code would use the left distance.

But since the problem states that there's at least one zero, then during the right pass, for elements before (to the left of) the first zero encountered in the right pass (which is the last zero in the array), their right distance would be set to next_zero - i (since next_zero is the last zero in the array). But if the element is after all zeros, then their right distance would be computed correctly.

Wait, perhaps the code will work correctly because in the left pass, for elements after the last zero in the array, their left distance is (i - last_zero) which is the distance to the last zero. Then during the right pass, their right distance is infinity (since there's no zero to the right), but the min is taken between left distance and infinity. So the correct distance is left distance.

But wait, in that case, the right pass's next_zero would have been set to the last zero in the array. So for elements after that zero (which is the last zero in the array), during the right pass, moving from the end, the next_zero would be set to the last zero. So, for example, for the array [0, 1, 2, 3, 4], the right pass would process elements 4,3,2,1,0. For element 0 (index 0), next_zero is 0. For element 1 (index1), next_zero is 0 (since during right pass, moving from left to right, no, wait, the code is processing from right to left. Wait, in the array [0,1,2,3,4], during the right pass, i starts at 4 (element4), then 3 (element3), etc. For each, since they are not zero, next_zero remains +infinity. So their right distance is next_zero - i (which is infinity - i, but in practice, we can't compute that. So, during the right pass, when next_zero is infinity, the right distance would be a very large number. But during the left pass, for these elements (1,2,3,4), their left distance was set to i (since the last_zero was 0). So during the right pass, when next_zero is infinity, the code would take the minimum between left distance (i) and a very large number (infinity). So the result would be i. Which is correct, because in this case, the nearest zero is the first one (index 0). So for element 4 (index4), the distance is 4 (left pass), and right distance is infinity. So the min is 4.

But during the right pass, after processing index0 (element0), next_zero is set to0. Then, during processing index1, next_zero is0. The right distance is 0 -1 = -1, but that's a negative number. Wait, this can't be right. Wait, the code in the right pass is:

for i in range(n-1, -1, -1):

    if a[i] ==0:

        next_zero =i

        current_right =0

    else:

        if next_zero != infinity:

            current_right = next_zero -i

        else:

            current_right = infinity

    result[i] = min(result[i], current_right)

Wait, but next_zero -i would be the distance from i to next_zero. For example, next_zero is 0, i is 1. Then next_zero -i = -1. Which is incorrect. So there's a mistake here.

Oh, right! Because during the right pass, we're moving from right to left. The next_zero is the index of the zero that is to the right of the current element. So for example, when processing index1, next_zero is the index of a zero that is to the right (i.e., with a higher index) than index1. But if the code is moving from the end towards the start, then when a zero is found at index j, all elements to the left of j (i < j) would have next_zero =j. So the distance from i to j is j - i, which is correct.

Wait, yes. For example, in the array [0,1,2,3,4], during the right pass, when processing i=4 (element4), next_zero is infinity (no zeros found yet). So the right distance is infinity. Then i=3 (element3), same. Then i=2 (element2), same. Then i=1 (element1), same. Then i=0 (element0), which is a zero. So next_zero is set to0. Then, for elements to the left of 0 (which there are none). Wait, in the right pass, after processing i=0, when the code processes i=1 (which is not possible here, since the loop is from n-1 downto 0, and the array has 5 elements (indices 0-4). So, in this example, during the right pass, the code would set next_zero to0. Then, the elements to the right of 0 (indices 1-4) have already been processed. So their right distances would have been set to infinity. So during the right pass, the code for these elements (indices1-4) would have next_zero as infinity, so current_right is infinity. Then, their result[i] is min(left distance, infinity), which is left distance, which is correct.

But for elements that are to the left of a zero (but processed earlier in the right pass), the next_zero would not have been updated yet. For example, in the array [5,6,0,1,2,0,4], during the right pass, when processing i=5 (element0), next_zero is set to5. Then, when processing i=4 (element2), the next_zero is5. current_right is5-4=1. The left distance for i=4 is4-2=2. So the min is1, which is correct.

So the code for the right pass should calculate the current_right as next_zero -i, but only when next_zero is not infinity.

But what about when next_zero is to the left of i? For example, if next_zero is 2 and i is3. Then next_zero -i is -1. But this is impossible, because next_zero is supposed to be a zero to the right of i. So this indicates a mistake in the code.

Ah, here's the problem. The right pass is supposed to compute the distance to the nearest zero to the right (i.e., higher index) of the current element. But when we process elements from right to left, the next_zero is the most recently encountered zero (which has a lower index than the current element being processed). So this is incorrect.

Wait, no. Wait, when processing from right to left, the next_zero is the index of a zero that is to the right of the current element. Because when processing from right to left, once we encounter a zero, that zero is to the left (smaller index) than the current element. For example, in the array [5,0,3,0], the zeros are at indices1 and3. When processing from right to left:

i=3 (element0) → next_zero=3.

i=2 (element3): current_right is3-2=1.

i=1 (element0): set next_zero=1.

i=0 (element5): current_right is1-0=1.

So the right distances are [1,0,1,0]. But the nearest zero to the right of i=0 is at1. The distance is1-0=1, which is correct.

But in this case, during the right pass, the code correctly computes the distance to the next zero to the right.

Wait, but when processing i=2 (element3), next_zero is3. So the distance is3-2=1. Which is correct, since the next zero to the right of i=2 is at3.

But when processing i=1 (element0), next_zero is set to1. Then, when processing i=0 (element5), the next_zero is1. The distance is1-0=1, which is correct.

So even though during the right pass, the code processes elements from right to left, the next_zero is updated whenever a zero is found. So the code correctly computes the distance to the next zero to the right.

So the code is correct.

So the code should:

In the right pass, for each element i:

if the element is zero, then next_zero is set to i.

the distance to the next zero to the right is next_zero -i (if next_zero is not infinity).

But for example, in the array [0,1,2,3,4], during the right pass:

i=4 → no zero, next_zero is infinity. So current_right is infinity. result[i] is min(4, inf) →4.

i=3 → same, current_right is infinity. result[i] is3.

i=2 → result[i] is2.

i=1 → result[i] is1.

i=0 → zero, set next_zero to0. current_right is0. result[0] is0.

So the output is [0,1,2,3,4], which is correct.

So the code is correct.

Thus, the code steps are:

Initialize result array.

Left pass:

Track last_zero. Initialize to -infinity.

For each i in 0..n-1:

if a[i] is zero:

    last_zero =i

    result[i] =0

else:

    if last_zero == -infinity:

        result[i] =inf

    else:

        result[i] =i - last_zero

Right pass:

Track next_zero. Initialize to +infinity.

for i from n-1 downto 0:

    if a[i] is zero:

        next_zero =i

        current_right =0

    else:

        current_right = (next_zero -i) if next_zero != inf else inf

    result[i] = min(result[i], current_right)

But wait, in Python, handling the 'inf' as a float could be problematic. For example, for n=2e5, but since the elements can be up to 1e9 in distance, using a large value (like n) would be sufficient. Because the maximum possible distance is n-1. So we can represent 'infinity' as n+1 or similar.

Alternatively, in Python, use a very large number like 1e18.

But in the problem statement, the array has at least one zero, so during the right pass, every element will have a valid next_zero, except for those that are after the last zero. But wait, no. For example, in the array [0,1,2,3], during the right pass:

The last zero is at index0. So during the right pass, when processing elements 3,2,1,0:

i=3 (element3) → next_zero is infinity. current_right is infinity. result[i] was set to3 in the left pass. So min(3, inf) is3.

i=2 (element2) → same. result[i] is2.

i=1 → same. result[i] is1.

i=0 → zero. next_zero set to0. current_right is0. result[i] is0.

So for elements after the last zero (the first zero in this case), their right distance is infinity, but their left distance is correct.

So during the right pass, the code correctly takes the minimum between the left and right distances.

But in this case, the code for the right pass will correctly compute the distance.

Thus, the code can proceed with using 'inf' as a placeholder.

In Python, using float('inf') is possible, but for integer operations, perhaps using a very large number like 10^18 is better. But for the purposes of this problem, using float('inf') is acceptable.

So now, implement this in Python.

Read n, then a list of integers.

Initialize the result list.

Then the left pass:

last_zero = -infinity (initially set to -1e18, but in code, perhaps -infinity).

Wait, in Python, we can set last_zero = -infinity initially. But how?

Wait, no. Because in Python, the initial last_zero is not found. So perhaps, for the left pass, we can initialize last_zero to -infinity, but in Python, it's better to use a variable and set it to None. Or, since indices are 0-based, we can set last_zero to -infinity (using a very large negative number).

Alternatively, use a variable that starts as None. Then, during the left pass:

for i in range(n):

    if a[i] ==0:

        last_zero =i

        result[i] =0

    else:

        if last_zero is None:

            result[i] = float('inf')

        else:

            result[i] =i - last_zero

Similarly for the right pass:

next_zero = None

for i in range(n-1, -1, -1):

    if a[i] ==0:

        next_zero =i

        current_right =0

    else:

        if next_zero is not None:

            current_right = next_zero -i

        else:

            current_right = float('inf')

    result[i] = min(result[i], current_right)

Wait, but in the right pass, next_zero is initially None. So during the first iteration (processing i from n-1 downto 0), if a[i] is not zero, then next_zero is None. So current_right is infinity. But the min with the left pass's result[i] (which could be infinity, but during the left pass, for elements after the last zero, the left distance is their index - last_zero (which is the last zero's index). But in cases where all zeros are before the current element, the right pass's current_right would be infinity, so the min would be the left distance.

But according to the problem statement, there is at least one zero, so eventually, next_zero will be set during the right pass.

For example, if the array has zeros, then during the right pass, processing from the end, once a zero is encountered, next_zero is set, and all previous elements (those with lower indices) will have their current_right computed as next_zero -i.

So the code is correct.

Testing this code with the sample inputs.

First sample input:

9

2 1 0 3 0 0 3 2 4

Left pass:

For indices 0,1:

a[i] is not zero. last_zero is None. So result[0] = inf, result[1] = inf.

At i=2, a[i] is zero. result[2]=0. last_zero=2.

i=3: result[i] =3-2=1.

i=4: zero → result[4]=0. last_zero=4.

i=5: zero → result[5]=0. last_zero=5.

i=6: result[6]=6-5=1.

i=7:7-5=2.

i=8:8-5=3.

So after left pass, result is [inf, inf,0,1,0,0,1,2,3].

Right pass:

Start from i=8.

a[8] is4 → next_zero is None → current_right is inf. result[i] is3. min(3, inf) →3.

i=7: a[i] is2 → next_zero is None → current_right inf. min(2, inf) →2.

i=6: a[i] is3 → next_zero is None → current_right inf. min(1, inf) →1.

i=5: a[i] is0 → next_zero=5. current_right 0. result[i] is0. min(0,0) →0.

i=4: a[i] is0 → next_zero=4. result[i] 0.

i=3: a[i] is3 → next_zero=4. current_right=4-3=1. min(1,1) →1.

i=2: a[i] is0 → next_zero=2. current_right 0. result[i] 0.

i=1: a[i] is1 → next_zero=2. current_right=2-1=1. min(inf,1) →1.

i=0: a[i] is2 → next_zero=2. current_right=2-0=2. min(inf,2) →2.

So the final result is [2,1,0,1,0,0,1,2,3], which matches the sample.

Second sample input:

5

0 1 2 3 4.

Left pass:

result after left pass: [0,1,2,3,4].

Right pass:

processing from 4 downto 0.

i=4: a[i] is4 → next_zero is None → current_right inf. min(4, inf) →4.

i=3: a[i] is3 → next_zero None → current_right inf. min(3, inf) →3.

i=2: a[i] is2 → next_zero None → current_right inf. min(2, inf) →2.

i=1: a[i] is1 → next_zero None → current_right inf. min(1, inf) →1.

i=0: a[i] is0 → next_zero=0. current_right 0. min(0,0) →0.

So the result is [0,1,2,3,4], which is correct.

Third sample input:

7

5 6 0 1 -2 3 4.

Left pass:

indices0 and1: inf.

index2: zero →0.

index3:3-2=1.

index4:4-2=2.

index5:5-2=3.

index6:6-2=4.

So left pass result is [inf, inf,0,1,2,3,4].

Right pass:

i=6 (4) → next_zero is None → current_right inf. min(4, inf) →4.

i=5 (3) → same →3.

i=4 (-2) → same →2.

i=3 (1) → same →1.

i=2 (0) → set next_zero=2. current_right 0. min(0,0) →0.

i=1 (6) → next_zero=2. current_right=2-1=1. min(inf,1) →1.

i=0 (5) → next_zero=2. current_right=2-0=2. min(inf,2) →2.

So the result is [2,1,0,1,2,3,4], which matches the sample.

Thus, the code works.

Now, in Python, implementing this.

But for the first pass, in Python, for the left pass, we need to handle 'inf' correctly.

In Python, 'infinity' can be represented with float('inf').

So the code steps are:

Read n.

Read the array a as a list of integers.

Initialize the result list with the same length as a, filled with zeros.

Left pass:

last_zero = None

for i in range(n):

    if a[i] ==0:

        result[i] =0

        last_zero =i

    else:

        if last_zero is None:

            result[i] = float('inf')

        else:

            result[i] =i - last_zero

Right pass:

next_zero = None

for i in range(n-1, -1, -1):

    if a[i] ==0:

        next_zero =i

        current_right =0

    else:

        if next_zero is not None:

            current_right = next_zero -i

        else:

            current_right = float('inf')

    result[i] = min(result[i], current_right)

Print the result as space-separated integers.

But wait, in the right pass, when a[i] is zero, we set current_right to0. But in the code above, even if a[i] is zero, the code does:

result[i] = min(result[i], current_right)

But current_right is0. Since the left pass would have already set result[i] to0, the min is0, so no problem.

Testing this code in the samples.

But in Python, when you print float('inf'), it becomes 'inf' which is not acceptable. So using float('inf') could be a problem for elements that have no zeros to one side. But according to the problem statement, there's at least one zero in the array, so the code should not have any inf in the final result. But during the left pass, for elements before the first zero, the left distance is inf. But during the right pass, their right distance is the distance to the first zero (which is encountered in the right pass).

Wait, but for example, in the first sample input, the first two elements (2 and1) have left distance inf. But during the right pass, their current_right is computed as next_zero (which is2) -i. So for i=0:2-0=2, i=1:2-1=1. So during the right pass, their result[i] is min(inf, 2) →2, and min(inf,1) →1.

So in Python, using float('inf') is okay, as min(inf, x) returns x if x is finite.

Thus, the code is correct.

But when printing, the float values like 2.0 would be printed as 2.0, but the problem requires integer outputs. So converting the result elements to integers.

But in the code, during the left and right passes, the distances are integers. For example, i - last_zero is integer, and next_zero -i is integer.

But in Python, when you assign to result[i] = i - last_zero, it's integer. But if you assign float('inf'), then that's a float.

So to ensure that all elements are integers, perhaps the code should use a very large integer instead of float('inf').

But for n up to 2e5, the maximum possible distance is 2e5-1. So using a value like 1e9 as 'infinity' would suffice.

So modifying the code:

In the left pass:

if last_zero is None:

    result[i] = 1e18  # a large number larger than any possible distance.

Similarly in the right pass:

if next_zero is None:

    current_right =1e18

But how to choose this value?

The maximum possible distance between two elements is n-1. So using n as the 'infinity' is sufficient. Because for n up to 2e5, the maximum distance is 2e5-1. So using 2e5+1 would be larger than any possible distance. So in code:

INF = n + 1

Then, during the left pass:

if last_zero is None:

    result[i] = INF

Similarly, in the right pass:

current_right = INF if next_zero is None else (next_zero -i)

This would avoid using float('inf'), ensuring that all values are integers.

But how to set INF?

After reading n, set INF = n + 1.

So in code:

n = int(input())

a = list(map(int, input().split()))

INF = n +1

result = [0]*n

# Left pass

last_zero = None

for i in range(n):

    if a[i] ==0:

        result[i] =0

        last_zero =i

    else:

        if last_zero is None:

            result[i] = INF

        else:

            result[i] = i - last_zero

# Right pass

next_zero = None

for i in range(n-1, -1, -1):

    if a[i] ==0:

        next_zero =i

        current_right =0

    else:

        if next_zero is not None:

            current_right = next_zero -i

        else:

            current_right = INF

    result[i] = min(result[i], current_right)

# Print the result as space-separated integers.

print(' '.join(map(str, result)))

This code uses integer values, and for cases where the left or right distance is not present, uses INF. But since the problem states that there's at least one zero, in the final result, all entries will have a valid distance (i.e., min of left and right is finite).

Testing this with the first sample:

n=9, INF=10.

Left pass:

Indices0 and1: result is10.

Then, during the right pass:

For i=0, next_zero is2. current_right=2-0=2. min(10,2) →2.

Similarly for i=1: current_right=1. min(10,1) →1.

Thus, the output is correct.

Thus, the code should work correctly.

The time complexity is O(n) for two passes, which is acceptable for n=2e5.

Space complexity is O(n) for the result array, which is acceptable for 256MB (each entry is a 4-byte integer, so 2e5 *4 bytes is 800KB, which is well within the limit).

Thus, this code should pass all test cases.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
INF = n + 1
result = [0] * n

# Left pass
last_zero = None
for i in range(n):
    if a[i] == 0:
        result[i] = 0
        last_zero = i
    else:
        if last_zero is not None:
            result[i] = i - last_zero
        else:
            result[i] = INF

# Right pass
next_zero = None
for i in range(n-1, -1, -1):
    if a[i] == 0:
        next_zero = i
        current_right = 0
    else:
        if next_zero is not None:
            current_right = next_zero - i
        else:
            current_right = INF
    result[i] = min(result[i], current_right)

print(' '.join(map(str, result)))
```