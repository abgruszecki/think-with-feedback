<think>
Okay, let's see. The problem is about finding all the percentages from 0 to 100 that appear simultaneously on both progress bars at some point during the copying of files. The files are copied sequentially, and after each byte copied, both bars update. We need to track when the two percentages are the same.

Hmm. The key here is to model when the two progress bars display the same percentage. Let's think about each byte being copied in order and check the percentages. But given that the a_i can be up to 1e10, iterating each byte is impossible. So we need a smarter approach.

So for each file i, we have to find all x (from 1 to a_i) such that floor(100x / a_i) = floor(100 * (sum_prev + x) / total), where sum_prev is the sum of all previous files. These x are the positions in the current file where the two percentages match.

But how do we compute this efficiently without checking each x?

Let's denote s_prev as the sum of a_1 to a_{i-1}, and total = sum of all a_i. Then for the current file i, x ranges from 1 to a_i.

For each x in this range, the first percentage is p1 = (100 * x) // a_i. The second is p2 = (100 * (s_prev + x)) // total. We need p1 == p2.

But how can we find all x where p1 equals p2, considering the ranges and the floor operations?

Alternatively, for each possible percentage value k (0 to 100), check if there exists an x in any file such that both p1 and p2 equal k. Then collect all such k.

So the approach could be:

1. Precompute the total sum of all a_i to get 'total'.
2. For each file i, compute the sum_prev (sum of a_1 to a_{i-1}).
3. For this file, find all k where there exists an x in [1, a_i] such that:
   - k = floor(100x / a_i)
   - k = floor(100*(sum_prev + x)/total)
4. Collect all such k across all files and output the unique ones sorted.

The challenge is efficiently finding these k values for each file without iterating each x.

Let's think about for a given file i and possible k, find x such that:

k <= (100x)/a_i < k+1
and
k <= (100(s_prev + x))/total < k+1

Which can be rewritten as:

x is in [ceil(k * a_i / 100), floor((k+1) * a_i -1)/100)]  (since 100x >= k a_i => x >= k a_i /100, but since x is integer, we take ceiling. Similarly upper bound.)

Similarly for the second condition:

100(s_prev + x) >= k * total
s_prev + x >= k * total / 100

and

100(s_prev + x) < (k+1)* total
s_prev + x < (k+1) total /100

So combining these inequalities:

s_prev + x >= ceil(k * total / 100)
s_prev + x <= floor( ( (k+1)* total -1 ) / 100 )

But x is between 1 and a_i.

So x must satisfy:

x >= max( ceil( k a_i / 100 ), ceil( k total /100 - s_prev ) )

and

x <= min( floor( ( (k+1) a_i -1 ) /100 ), floor( ( (k+1) total -1 ) /100 - s_prev ) )

If the lower bound is <= upper bound, then there exists an x in this range. For such x, both percentages are k. So for this k, there is at least one x in some file.

So the plan is:

For each file i:

   sum_prev = sum of a_1 to a_{i-1}
   a_i is the current file's size.
   For each k in 0..100:
       compute the x ranges for p1 and p2 being k.
       find the overlap between these ranges.
       if the overlap exists and x is between 1 and a_i, then k is possible.

But how to do this efficiently?

Wait, but for each k (0-100), check if there's any x in any file that satisfies both conditions.

So the steps would be:

1. Precompute the total sum.
2. For each k from 0 to 100:
   Check if there exists any x in any file where:
      x satisfies the two inequalities for p1 and p2 being k.
3. Collect all such k where at least one x exists.

So for each k, we need to check all files to see if for that file, there's an x that satisfies both ranges.

So for each k, loop through all the files and see if in any of them, the overlapping x range for that k is non-empty and within [1, a_i].

If yes, then k is part of the answer.

So the key is to, for each k, iterate through all the files and check if for that file, the intersection of the x ranges (from p1 and p2) is non-empty and within x's possible values.

Now, let's formalize the ranges:

For a file i and k, the x must satisfy:

x >= lower1 = ceil( (k * a_i) / 100 )
x >= lower2 = ceil( (k * total / 100) - s_prev )

so the lower is max(lower1, lower2)

x <= upper1 = floor( ( (k+1)*a_i -1 ) / 100 )
x <= upper2 = floor( ( (k+1)*total -1 ) / 100 ) - s_prev

so the upper is min(upper1, upper2)

Additionally, x must be <= a_i and >=1.

So the effective x range for the current file and k is:

x_start = max( lower1, lower2, 1 )

x_end = min( upper1, upper2, a_i )

if x_start <= x_end, then there are x's in this range, so k is valid.

Thus, for each k from 0 to 100, we check each file to see if in any of them, this x_start <= x_end. If so, add k to the answer set.

So the steps are:

Compute total = sum(a_i)

For each k in 0..100:

   found = False

   for each file i in 1..n:

       s_prev = sum of a_1 to a_{i-1}

       ai = a_i

       # compute lower1 and lower2

       lower1 = ceil( (k * ai) / 100 )

       lower2 = ceil( (k * total) / 100 - s_prev )

       x_lower = max( lower1, lower2, 1 )

       # compute upper1 and upper2

       upper1 = ( (k+1) * ai -1 ) // 100

       upper2 = ( (k+1)*total -1 ) // 100 - s_prev

       x_upper = min( upper1, upper2, ai )

       if x_lower <= x_upper and x_upper >= 1:

           found = True

           break

   if found:

       add k to the answer.

So this approach iterates over 101 k's and for each k, over n files (up to 100), and for each, computes some ranges and checks if they overlap. Since n is small (<=100), and k is 101, this is manageable.

Now, how to compute the ceiling and floor divisions correctly. Since in Python, dividing with integers is done with //, but when dealing with fractions, we need to be precise.

For example, lower1 is the smallest x where 100x >= k * a_i → x >= k * a_i /100. Since x must be an integer, lower1 is ceil(k * a_i /100). How to compute this?

But since k and a_i can be up to 1e10 * 100, we need to compute this accurately. However, in Python, integer arithmetic is precise.

Wait, ceil(a / b) can be written as (a + b -1) // b when a and b are positive integers.

So for lower1:

ceil( (k * a_i) /100 ) is equal to (k * a_i + 99) // 100. Because for example, if k*a_i is exactly divisible by 100, then it's (k*a_i)/100. Otherwise, it's integer division plus 1.

Wait, no. Let's see. Let's say a = k * ai, then ceil(a/100) is (a + 99) // 100.

For example, a=150 → 150/100=1.5 → ceil is 2. (150+99)=249 → 249//100=2.

Yes. So lower1 is (k * ai + 99) // 100.

Similarly, lower2 is ceil( (k * total)/100 - s_prev ). But wait, that's (k * total) /100 - s_prev. So to compute the x, which is >= that value. But since x is an integer, ceil( (k * total /100) - s_prev ) is equivalent to x >= ... so x must be >= the smallest integer greater than or equal to (k*total/100 - s_prev).

But (k * total) /100 could be a fractional value. So to compute lower2:

lower2 = ceil( (k * total) / 100 - s_prev )

But how to compute this? Let's compute (k * total) as a number. Then (k * total) /100 is a possibly fractional value, subtract s_prev, then take the ceiling.

But since total can be up to 1e10 * 100 (since n is up to 100 and each a_i is up to 1e10), k*total can be up to 1e12. But Python can handle that as integers.

Wait, but (k * total) can be up to 100 * (100 * 1e10) ) = 1e12 + something. So (k * total) is an integer. Then (k * total) /100 could be an integer or have .0, .01, etc.?

No, because k and total are integers. So (k * total) is an integer, divided by 100. So (k * total) /100 can be written as a float, but in integer terms, (k * total) divided by 100 is equal to (k * total) // 100 + ( (k * total) % 100 ) /100. So when you subtract s_prev from that, which is an integer, the fractional part is ( (k * total) % 100 ) /100. So the value (k * total)/100 - s_prev can be written as ( (k * total - s_prev * 100 ) ) /100. Let's see:

Let me see:

(k * total /100 ) - s_prev = (k * total - 100 s_prev ) / 100.

So the value is ( (k * total - 100 s_prev ) ) / 100.

So ceil( (k * total /100 - s_prev ) ) = ceil( (k * total - 100 s_prev ) / 100 )

Which can be computed as ( (k * total - 100 s_prev ) + 99 ) // 100.

Because again, to compute the ceiling of a division of a by b, it's (a + b -1) // b.

So in this case, a is (k * total - 100 s_prev ), and b is 100. So:

lower2 = ceil( (k * total - 100 s_prev ) / 100 ) = ( (k * total - 100 s_prev ) + 99 ) // 100

But wait, the value (k * total - 100 s_prev) could be negative, which would affect the ceiling. Let's make sure.

But since s_prev is the sum of previous files. For the current file, when x is being considered, the sum_prev is the sum of a_1 to a_{i-1}, and x is in 1..a_i. So sum_prev +x is part of the total.

But for the second progress bar, when we compute (sum_prev + x)/total *100, the sum_prev can be up to total - a_i. So (sum_prev +x) can be up to total. So for the k being considered, the (sum_prev +x) can be up to total.

So (k * total) /100 can be up to 100 * total /100 = total. So (sum_prev +x) can be up to total. So (sum_prev +x) >= k * total /100 → sum_prev >= k * total /100 -x.

But x can be up to a_i. So sum_prev can be up to total - a_i.

But perhaps for some k, (k * total) /100 - sum_prev could be negative. For example, when sum_prev is large and k is small.

In that case, lower2 would be negative. But x must be >=1, so the max(lower1, lower2,1) would take 1.

So in code, for lower2:

lower2 = ( (k * total - 100 * s_prev ) + 99 ) // 100

But if (k * total - 100 * s_prev) is negative, adding 99 and dividing by 100 can result in a negative number.

For example, if k=0, then (0 - 100 s_prev ) could be negative. Then (0 -100 s_prev +99) = ( -100 s_prev +99 ). Then dividing by 100 gives a negative value. For example, if s_prev is 100, then (0 - 100*100) = -10000. Adding 99 gives -9901. Divided by 100 is -99.01 → integer division in Python is towards negative infinity, so -99.01 becomes -100. So lower2 would be -100.

But x can't be negative, so when we take the max of lower1, lower2, and 1, it will be 1.

So the code can handle that.

Now, upper1 and upper2:

upper1 is ( (k+1)*a_i -1 ) // 100. Because the condition is 100x < (k+1)*a_i → x < (k+1)*a_i /100. But since x is integer, x can be at most floor( ( (k+1)*a_i -1 ) / 100 )

Similarly, upper2 is ( (k+1)*total -1 ) // 100 - s_prev.

Because sum_prev +x < (k+1)*total /100 → x < (k+1)*total/100 - s_prev. Since x is integer, x <= floor( ( (k+1)*total -1 ) /100 - s_prev )

So upper2 is ( (k+1)*total -1 ) // 100 - s_prev.

But ( (k+1)*total -1 ) //100 is the floor of ( (k+1)*total -1 ) /100, which is the same as floor( ( (k+1)*total -1 ) /100 )

So for upper2, subtract s_prev from that value.

Now, x_upper is the minimum of upper1, upper2, and a_i.

Once x_lower and x_upper are computed, we check if x_lower <= x_upper and x_upper >=1 (since x can't be 0, as per the problem statement: after copying each byte, which starts from x=1). Wait, no: in the problem statement, x is the number of bytes copied so far in the current file. So x ranges from 1 to a_i. So x must be at least 1. Wait, no. Wait, the first byte copied is x=1. For example, the first example: input is 6 bytes. The percentages after each byte (x=1, 2, 3,4,5,6).

So x starts from 1 to a_i.

Therefore, the x must be >=1 and <=a_i.

So when computing x_lower, we take the max of lower1, lower2, and 1. Because x can't be less than 1.

Similarly, x_upper is min(upper1, upper2, a_i). Because x can't be larger than a_i.

So in code:

For each file i:

   sum_prev = sum of a_1 to a_{i-1}

   a_i = current file's size

   for each k in 0..100:

       lower1 = (k * a_i + 99) // 100

       lower2 = (k * total - 100 * sum_prev + 99) // 100

       x_lower = max(lower1, lower2, 1)

       upper1 = ((k+1)*a_i -1) // 100

       upper2 = ((k+1)*total -1) // 100 - sum_prev

       x_upper = min(upper1, upper2, a_i)

       if x_lower <= x_upper and x_upper >=1:

           return True for this k.

So, for each k, if any file has x_lower <=x_upper and x_upper >=1, then k is in the answer.

Now, the code can proceed as follows:

Read n, then a list.

Compute total = sum(a)

Precompute the prefix sums s_prev for each file.

Then, for each k from 0 to 100:

   for each file i in 0..n-1:

       s_prev = prefix_sum[i]

       ai = a[i]

       compute lower1, lower2, x_lower

       compute upper1, upper2, x_upper

       check if x_lower <=x_upper and x_upper >=1.

       if yes, then k is valid, break.

So, in code, the steps are:

Read input.

Compute prefix sums.

For each k in 0-100:

   check all files for possible x.

If any file has x in the required range, add k to the answer.

Finally, output the sorted list.

Now, let's test this approach against the examples.

First example:

Input: 1 6 → total=6.

For k=0:

file 0: sum_prev=0, ai=6.

lower1 = (0*6 +99)//100 → 0//100=0.

lower2 = (0*6 -100*0 +99)//100 → 0 → 0//100=0.

x_lower = max(0,0,1) →1.

upper1 = (1*6 -1)//100 →5//100=0.

upper2 = (1*6 -1)//100 -0 →5//100=0 -0=0.

x_upper = min(0,0,6) →0.

x_lower=1 > x_upper=0 → no.

So k=0 is not found here. Wait, but the sample output includes 0. Wait, but the problem statement says that initially, both progress bars are 0. That is, before any copying. But according to the problem statement, after copying each byte, the percentages are updated. So initially (before any copying), they are 0. Then, after the first byte, they start to change.

Wait, but according to the problem statement, the initial state (0%) is when no bytes have been copied. So perhaps we need to include 0% as a possible value only if there exists a moment when both are 0, which is the start. But the problem says "найдите все целые числа от 0 до 100 включительно, что существует момент времени, в который оба прогресс-бара одновременно показывают это число."

The initial moment (before any copying) is time zero, and both are 0. So 0 is always included in the answer. Wait, but according to the problem's examples, in the first sample, 0 is present, but according to our code's calculation for k=0, in the first file, x_lower=1 and x_upper=0, which doesn't satisfy.

Wait, this suggests that the initial state (0 bytes copied) is considered. So for the code, we need to check if there exists a moment (including before any bytes are copied) where both are 0.

But according to the problem statement, the progress bars start at 0% and are updated after each byte. So the initial state (before any bytes are copied) is 0% for both. So 0 is always in the answer.

Wait, looking at the first sample input:

Sample 1:

input 1 6 → output includes 0,16, etc. But according to the code as written, the code would not find k=0 because for the first file, the x starts at 1. So the code would not check the initial state. So the code is missing the initial 0% case.

Ah, this is a problem. So in the code, we need to add 0% as a possible candidate if there exists any time where both are 0. But according to the problem statement, the initial state (0 bytes copied) is when both are 0. So 0 is always present in the answer. Wait, no.

Wait, consider the case where the first file has a size of 0. But the problem states that a_i >=1. So in all cases, the initial state is 0% for both. So 0% is always included. So the answer must include 0% unless there is no moment where both are 0% except the initial state. Wait, but the problem says that the initial state is considered. For example, in the first sample, the initial state is 0%, and after each byte, the percentages change. So the output includes 0.

But according to the code's current approach, the code would not capture this, because it checks x starting from 1.

So the code is missing the initial state. So how to handle this.

Hmm. So in the problem statement, the progress bars start at 0% and after each byte copied, they update. So the initial 0% is present, and the code's current approach would miss it. So for example, the code would not find k=0 in the first sample.

Wait, let's see:

In the first sample, after 0 bytes copied (before any copying), both are 0. Then, after the first byte (x=1), the percentages are 1*100/6 = 16 (floor(16.666)), and total percentage is 1*100/(6) =16.666→16.

So the initial state (x=0) is when both are 0. But in our code, the x ranges for each file start at 1, so the code would not check x=0. So the code would not find k=0 in the first file, leading to the code not including 0 in the answer. But the sample includes 0.

This indicates that the code must include the initial state (x=0 for all files) as a possible candidate.

But how?

Alternatively, perhaps the code can check for the initial state (before any files are copied) where sum_prev=0, and x=0 (since no file is being copied yet?), but that's not part of any file.

Alternatively, perhaps the code should treat the initial state as a separate case.

So how to model the initial state.

At the initial state, before any bytes are copied, sum_prev is 0 (no files copied yet), and x=0 (no bytes copied in the current file). But the current file is the first file, but x=0 would not be considered as the code's x ranges start at 1.

Wait, perhaps the initial state is when sum_prev=0, and all files are not yet started. So for all files, x is 0. But this is a special case.

So the code needs to check if the initial state (sum_prev=0, x=0 for all files) is a case where both percentages are 0. Which it is.

But according to the code's current approach, x must be >=1, so the code would not find this. So 0% is not considered.

Thus, the code's approach is missing the initial state. So we need to handle this case.

Thus, to include 0% in the answer, the code must check if there's a moment when both percentages are 0. The initial state is such a moment, so 0% is always present. Wait, no. What if the first file is 0 bytes? But the problem states that a_i >=1.

So in all test cases, the initial state is 0% for both. So 0% is always part of the answer. So the code should include 0% regardless of the checks. But according to the sample input 2, the output includes 0. So 0 is always part of the answer.

Wait, no. Looking at sample input 2:

Input: 2 100 500 → output includes 0,95,96,...100.

But in the initial state, both are 0. So why is 0 in the output? Because the code's approach would include 0% only if the code checks the initial state. So the code must account for the initial state.

Thus, the code must include 0 in the answer, but according to the current approach, it's not.

So, this suggests that the code is missing this case. Therefore, the code should add 0 to the answer set if it's possible, which is the case for the initial state.

But how to model this. Because the initial state is not part of any file's x. So perhaps the code should check if 0 is a possible value by considering x=0 for the first file. But according to the problem statement, x starts at 1. So the initial state is a separate case.

Therefore, the code must check the initial state (0 bytes copied) and add 0% to the answer.

So the initial state is when all files are not yet copied. sum_prev = 0 (all files), and x=0 for the current file (which is the first file). So:

sum_prev = 0

x=0 (but the current file is the first one, but x=0 is not part of the copying steps).

But according to the problem statement, the initial state is considered. So 0% is present in the answer.

So the code should add 0 to the answer set regardless of other conditions. But is that always the case?

No. Wait, suppose there is no other moment where both are 0. For example, after the initial state, there might be another moment where both are 0 again. For example, if after some bytes, both percentages drop back to 0. But given that the percentages are non-decreasing, except when switching files, this is not possible.

Wait, but when a new file starts, the first progress bar resets to 0. For example, after copying file 1, when starting file 2, the first progress bar is 0%, while the second is sum_prev / total. So for example, if sum_prev is 100 bytes, and total is 600, then sum_prev / total is 16.666...% → 16. So the second bar would be 16%, and the first bar would be 0% as the new file starts. Then, as bytes are copied, the first bar increases. So in this case, there is a moment where the first bar is 0% (when x=0 for the new file), but the second bar is 16%.

But according to the problem statement, the progress bars are updated after each byte. So when you start the new file, x is 0 (since you have not copied any bytes yet in that file), but according to the problem statement, the progress bars are updated after each byte. So the initial x=0 for a new file is not considered. Because you start copying the first byte, and after that, x becomes 1.

Wait, no. Let's think: the first file is copied first. After copying all a_1 bytes, the next file starts. The first byte of the next file is copied. After that, x becomes 1, so the first progress bar is 1 *100 / a_i. So when the next file starts, x starts at 0 until the first byte is copied. But according to the problem statement, the progress bars are updated after each byte is copied. So the initial state for a new file (x=0) is not present except for the very first moment before any bytes are copied.

Thus, the only time when both bars are 0% is at the very beginning. So 0% is in the answer if and only if the initial state is considered. But according to the problem statement, the initial state is a moment when both are 0. So 0% is always present in the answer.

But in the code's current approach, 0% is not considered. So the code must handle this separately.

Therefore, the code should add 0% to the answer set, but also check if there are other moments where both are 0%.

Wait, but in the initial state, there's no file being copied. Wait, no: the first file is being copied, but x is 0. But according to the problem statement, after each byte copied, the bars are updated. So the initial state is before any bytes are copied. So x=0, sum_prev=0.

So in that case, both percentages are 0. So the code must add 0% to the answer set.

But according to the code's current approach, the code only checks x >=1. So the initial x=0 is not considered. Therefore, to handle this, the code must explicitly add 0% to the answer.

But wait, in the sample input 2, the output includes 0. So even though the first file is 100 bytes, after the first byte, the first bar is 1% and the second is 0.1% (1/600 *100 = 0.166... → 0). So the second bar is 0% for the first 5 bytes (since 5 bytes /600 → 0.83% → 0). But the first bar, for the first file, after 5 bytes is 5% (5/100=0.05 → 5). So during these steps, the second bar is 0. So there are times when the first bar is 5% and the second is 0. But these percentages are not equal. But the initial state is the only time both are 0.

So the code's approach would need to check the initial state separately.

Therefore, the code should add 0% to the answer set, and then check for other percentages from 1 to 100.

But how to handle this.

So, to modify the code:

- The initial state (before any bytes are copied) is 0% for both. So 0% is always included in the answer.

But wait, let's look at the sample input 3:

Input:4

10000000000 2 2 9999999998

Output: 0 50 99 100.

So 0 is present.

But according to the code's current approach, 0% would not be considered because x starts at 1. So the code must include 0% in the answer.

Thus, the code must explicitly add 0% to the answer set.

But wait, what about cases where the initial state is the only time when 0% appears?

For example, if the first file's first byte makes the first bar 1% and the second bar 0% (sum_prev +x is 1, total is 100. 1/100 *100 =1% → no. Wait, no. Let's see: sum_prev is 0, x is 1. So sum_prev +x is 1. total is 100. So (1 /100)*100=1% → floor is 1. So the second bar is 1% after the first byte. So in this case, the initial state is 0%, and after the first byte, the second bar is 1%. So 0% is present only in the initial state.

But according to the code's current approach, the code would include 0% only if the code's checks for x=0 in some file, but x=0 is not considered. So the code would miss the 0% in the initial state.

Therefore, the code must include 0% as part of the answer regardless of other conditions.

But this is not the case. For example, if there are no files (n=0), but the problem states that n >=1.

But according to the problem constraints, n is at least 1.

So in all cases, the initial state exists. So 0% is always part of the answer.

Wait, but the problem says to output all numbers from 0 to 100 inclusive that appear at least once.

So 0% is always present because it's the initial state.

Wait, but what about the case when the first file's first byte causes both percentages to be 0%?

But sum_prev is 0, x=1.

So first bar is (1*100)/a_i.

Second bar is (0+1)/total *100 → floor.

If a_i is 100 bytes, total is 100. Then x=1: first bar is 1% (1*100/100=1), second is 1%. So no.

Alternatively, if a_i is 101, and x=1. Then first bar is 0 (1*100//101 = 0). Second bar is 1 /101 *100 = 0.99 → 0. So both are 0.

So in this case, after x=1, both are 0. So 0% is present in the initial state (x=0) and after x=1 (first byte copied). So the answer would include 0% twice.

But according to the code's current approach, the code would find k=0 for the first file, x=1, and thus include 0% even without considering the initial state.

So in this case, the code would include 0% as per the code's checks.

But in other cases where the initial state is the only time when both are 0, the code would miss it.

Thus, to correctly handle all cases, the code must check the initial state and add 0% to the answer.

But how?

So the code can add 0% to the answer set unconditionally, then proceed to check other k's.

But wait, what if the initial state is the only time when both are 0%?

For example, if n=1, a_1=1. Then the initial state is 0%, but after the first byte (x=1), first bar is 100% and second is 100%. So the answer would include 0, 100. So 0 is present.

But according to the code's current approach, for k=0, the code would check for x in a_1=1. Let's see:

sum_prev=0, ai=1, total=1.

lower1 = (0*1 +99)/100 →99//100=0.

lower2 = (0*1 -100*0 +99)/100 →99//100=0.

x_lower = max(0,0,1) →1.

upper1 = (1*1 -1)//100 →0//100=0.

upper2 = (1*1-1)//100 -0 →0//100=0.

x_upper = min(0,0,1) →0.

So x_lower=1 and x_upper=0 → no. So the code would not include k=0. But the initial state is present. So the code would miss it.

Therefore, the code must include 0% in the answer set, regardless of the checks.

So the solution is to add 0 to the answer set, then check for other k from 1 to 100.

But wait, there might be other times when both bars are 0%. For example, when after some bytes, both bars return to 0% (but this is unlikely since the total progress can't decrease). But in reality, once bytes are copied, the sum_prev increases, so the second bar can't go back. However, when a new file starts, the first bar resets to 0%, but the second bar may be higher. For example, if you have a large file followed by a small one. When the small one starts, the second bar is already high, so the first bar is 0% (during copying of first byte of the new file), but the second bar is higher. So the only time both are 0% is the initial state.

Thus, the initial state is the only time when both are 0%.

Therefore, the code can simply add 0% to the answer set, and then proceed to check for k from 1 to 100.

But wait, in the first example, after copying 0 bytes, it's 0%, but after copying 6 bytes, it's 100% in both bars. So 0% is present once.

But according to the code's approach, the code will miss 0% unless it's added manually.

Thus, the code must add 0% to the answer set, and then check for other k's from 1 to 100.

So the revised plan is:

Initialize the answer set with 0.

Then, for each k from 1 to 100:

   check if there's any file i where x exists (1 <=x <=a_i) such that floor(100x/a_i) = k and floor(100*(sum_prev +x)/total) =k.

If so, add k to the answer.

So the code would:

- read input.

- compute total.

- compute prefix sums.

- initialize a set with 0.

- for k in 1..100:

   for each file i:

      sum_prev = prefix_sum[i]

      ai = a[i]

      compute lower1, lower2, x_lower.

      compute upper1, upper2, x_upper.

      if x_lower <=x_upper and x_upper >=1:

          add k to the set.

- finally, output sorted list of the set.

This way, 0 is always in the answer.

But let's test this.

Sample input 1:

n=1, a=6.

The code adds 0 to the set. Then checks for k=1 to 100.

For k=16:

In the first file (i=0):

sum_prev=0, ai=6.

lower1 = (16 *6 +99 )//100 → (96+99)=195 →195//100=1.

lower2 = (16*6 -0*100 +99)//100 →96 +99=195 →195//100=1.

x_lower = max(1,1,1) →1.

upper1 = (17*6-1)//100 →101//100=1.

upper2 = (17*6-1)//100 -0 →101//100=1 →1-0=1.

x_upper = min(1,1,6) →1.

x_lower=1 <=x_upper=1 → yes.

So k=16 is added.

Similarly for other k's in the sample output.

Thus, the code would generate the correct answer.

But what about the initial 0%?

Yes. So the code would add 0% to the answer.

Thus, the code should work.

Another test case: sample input 2.

Input is 2 files: 100 and 500. Total=600.

The initial 0% is added.

Then, for k=95:

Check if any file has x such that both percentages are 95.

For example, file 2 (sum_prev=100, ai=500).

sum_prev=100, total=600.

For k=95:

lower1 = (95 *500 +99)//100 → (47500+99)=47599//100=475.99 →475.

lower2 = (95*600 -100*100 +99)//100 → (57000 -10000) +99=47099 →47099//100=470.99 →470.99 →470.

x_lower = max(475,470,1) →475.

upper1 = (96*500-1)//100 →47999//100=479.

upper2 = (96*600-1)//100 -100 → (57599)//100=575.99 →575 -100=475.

x_upper = min(479,475,500) →475.

x_lower=475 <=x_upper=475. So x=475.

Check if x is between 1 and 500: yes.

So k=95 is added.

Thus, the code would include 95, etc., and the sample output is correct.

So the code must be modified to add 0 to the answer set, then process k from 1 to 100.

Thus, the code's steps are:

Read input.

Compute total.

Compute prefix sums.

ans = {0}

for k in 1..100:

   for each file i in 0..n-1:

       sum_prev = prefix_sum[i]

       ai = a[i]

       lower1 = (k * ai +99) // 100

       lower2 = (k * total - 100 * sum_prev +99) // 100

       x_lower = max(lower1, lower2, 1)

       upper1 = ((k+1)*ai -1) //100

       upper2 = ((k+1)*total -1) //100 - sum_prev

       x_upper = min(upper1, upper2, ai)

       if x_lower <=x_upper and x_upper >=1:

           ans.add(k)

           break

sort ans and print.

Now, this should handle all cases.

Now, let's code this in Python.

The code:

Read n.

Read a list of integers.

Compute total = sum(a).

Compute prefix_sum:

prefix_sum = [0]*(n)

prefix_sum[0] = 0

for i in 1..n-1:

   prefix_sum[i] = prefix_sum[i-1] + a[i-1]

Wait, no. Wait, prefix_sum[i] should be the sum of a_0 to a_{i-1}.

Yes.

For example, for i=0, sum_prev is prefix_sum[0] = 0.

for file 0 (the first file), sum_prev is prefix_sum[0] =0.

So prefix_sum can be computed as follows:

prefix_sum = [0]*(n+1) ?

No, for i in 0..n-1:

prefix_sum[i] is sum of a_0..a_{i-1}.

So:

prefix_sum[0] =0.

prefix_sum[1] = a[0]

prefix_sum[2] = a[0]+a[1]

and so on.

So in code:

prefix = [0] * (n+1)

for i in range(n):

   prefix[i+1] = prefix[i] + a[i]

Then, for the i-th file (0-based), sum_prev is prefix[i], and a[i] is the file's size.

So in code:

prefix = [0]

for num in a:

   prefix.append( prefix[-1] + num )

total = prefix[-1]

Then, for each file i in 0..n-1:

sum_prev = prefix[i]

ai = a[i]

Thus, the code can proceed.

Thus, the code:

n = int(input())

a = list(map(int, input().split()))

prefix = [0]

for num in a:

    prefix.append(prefix[-1] + num)

total = prefix[-1]

ans = {0}

for k in range(1, 101):

    found = False

    for i in range(n):

        sum_prev = prefix[i]

        ai = a[i]

        # compute lower1, lower2, x_lower

        lower1 = (k * ai + 99) // 100

        numerator = k * total - 100 * sum_prev

        lower2 = (numerator + 99) // 100

        x_lower = max(lower1, lower2, 1)

        # compute upper1 and upper2

        upper1 = ((k+1) * ai - 1) // 100

        upper2_numerator = (k+1)*total -1

        upper2 = (upper2_numerator // 100) - sum_prev

        x_upper = min(upper1, upper2, ai)

        if x_lower <= x_upper and x_upper >= 1:

            found = True

            break

    if found:

        ans.add(k)

ans = sorted(ans)

print('\n'.join(map(str, ans)))

Let's test this code against the first sample input:

Sample 1:

Input:

1

6

prefix is [0,6]

total is6.

For k=16:

i=0:

sum_prev=0, ai=6.

lower1 = (16 *6 +99)/100 → (96 +99)=195 →195//100=1.

lower2 = (16*6*1 (total is6) -100*0 +99) → 96 +99=195 →195//100=1.

x_lower=1.

upper1 = (17*6-1)/100 →101//100=1.

upper2 = (17*6-1)//100 -0 →101//100=1 →1-0=1.

x_upper=1.

So x_lower=1 <=x_upper=1 → found. So k=16 is added.

Similarly, other k's in the sample are added.

So the code should work.

Another sample input:

Sample 2:

input:

2

100 500

total=600.

k=95:

For file 1 (i=1):

sum_prev=100, ai=500.

lower1 = (95*500 +99)//100 → (47500 +99)=47599//100=475.99 →475.

lower2 = (95*600 -100*100 +99) → 57000 -10000=47000 →47000+99=47099 →47099//100=470.99 →470.

x_lower= max(475,470,1) →475.

upper1 = (96 *500 -1) //100 →47999//100=479.

upper2 = (96*600-1) →57599 →57599//100=575 →575 - sum_prev=100 →475.

x_upper= min(479,475,500) →475.

x_lower=475 <= x_upper=475 → yes.

Thus, k=95 is added.

This matches the sample.

Sample 3:

input:

4

10000000000 2 2 9999999998

total is 10000000000 +2+2+9999999998 = (1e10 + 1e10) → 2e10.

For k=50:

Check files.

File 0: sum_prev=0, ai=1e10.

lower1 = (50 *1e10 +99)/100 → (5e11 +99)/100 →5e9 + 0.99 →5e9.

lower2 = (50*2e10 - 100*0 +99 ) → (1e12 +99) →1e12//100 + 0.99 →1e10 →10000000000.

x_lower = max(5e9,1e10,1) →1e10.

But ai is 1e10 → x must be <=1e10.

upper1 = (51*1e10 -1)/100 →5100000000-1 →5099999999//100 →50999999.99 →50999999.

upper2 = (51*2e10 -1 )//100 -0 → (1.02e12 -1 )//100 →10200000000-1=10199999999 →10199999999//100=101999999.99 →101999999 →101999999 -0=101999999.

x_upper = min(50999999, 101999999, 1e10) →50999999.

x_lower=1e10 > x_upper=50999999 → no.

So not in file 0.

File 1: sum_prev=1e10, ai=2.

k=50:

lower1 = (50 *2 +99)/100 →199//100=1.

lower2 = (50 *2e10 -100*1e10 +99) → (1e12 -1e12 +99) →99 →99//100=0.99 →0.

x_lower = max(1,0,1) →1.

upper1 = (51*2 -1)/100 →101//100=1.

upper2 = (51*2e10 -1 )//100 -1e10 → (1.02e12 -1 )//100 →10200000000 -1 →10199999999//100=101999999.99 →101999999 →101999999 -1e10=1e10 +1999999 → but sum_prev is 1e10. So upper2 = 101999999 -1e10 → which would be negative. So x_upper is min(1, negative, 2) →negative →x_upper=1.

So x_lower=1 <=x_upper=1 → yes.

So k=50 is added.

Thus, sample 3's output includes 50.

Thus, the code works.

Thus, the code should correctly handle all cases.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
prefix = [0]
for num in a:
    prefix.append(prefix[-1] + num)
total = prefix[-1]

result = {0}

for k in range(1, 101):
    found = False
    for i in range(n):
        sum_prev = prefix[i]
        ai = a[i]
        if ai == 0:
            continue  # According to problem constraints, a_i >=1, so this is redundant
        
        lower1 = (k * ai + 99) // 100
        numerator = k * total - 100 * sum_prev
        lower2 = (numerator + 99) // 100
        x_lower = max(lower1, lower2, 1)
        
        upper1 = ((k + 1) * ai - 1) // 100
        upper2_numerator = (k + 1) * total - 1
        upper2 = (upper2_numerator // 100) - sum_prev
        x_upper = min(upper1, upper2, ai)
        
        if x_lower <= x_upper and x_upper >= 1:
            found = True
            break
    if found:
        result.add(k)

print('\n'.join(map(str, sorted(result))))
```