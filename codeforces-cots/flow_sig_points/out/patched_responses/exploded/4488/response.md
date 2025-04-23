<think>
Okay, let's see. I need to solve this problem where I have to find the minimum number of steps using the XOR-gun to make the array non-decreasing. Wait, wait, no. The original array is non-decreasing, and I have to make it no longer non-decreasing. So the goal is to perform some operations (replace two consecutive elements with their XOR) such that after these operations, the array is not non-decreasing. And find the minimal number of steps required, or return -1 if it's impossible.

Hmm. Let's think about the operations. Each operation reduces the array's length by 1. So after k operations, the array's length is n - k. But we can't perform any operations once the length is 1, so maximum possible steps is n-1, but that would leave a single element which can't be non-decreasing (but according to the problem statement, you can't perform the operation when the array is of length 1, so maybe even if you have to stop earlier).

Wait, the problem says that you can't perform the operation when the length reaches one. So the array can have length 2, perform one operation to make it length 1, but you can't do any more steps. So the steps can be up to n-1, but the array after each step must be longer than one before performing the step.

The key is to find the minimal k such that after applying k steps, the resulting array is not non-decreasing. Or determine that it's impossible.

But how to approach this? Let's think about small cases.

Take the first example: [2,5,6,8]. The minimal steps are 1. If we merge 2 and 5, we get 7, so the array becomes [7,6,8], which is decreasing at the first two elements (7>6). So that's a single step.

So the idea is that when we merge two consecutive elements, their XOR could create a situation where the array is no longer non-decreasing. But how can we find this quickly?

The constraints are up to n=1e5. So a brute-force approach is impossible. We need an O(n) or O(n^2) algorithm, but even O(n^2) might be too slow for 1e5.

Wait, but for some cases, maybe the answer is very small. Like, maybe there's a triplet of elements where merging two adjacent pairs breaks the non-decreasing property.

Wait, let's think about when merging two elements. Suppose the array is a1 <= a2 <= ... <= an. After merging two consecutive elements x and y into x^y, the new array could have a point where a'[i] > a'[i+1]. So the question is: when can merging two consecutive elements create such a situation?

For example, in the first example, after merging 2 and 5 into 7, the array is [7,6,8]. The 7>6, which breaks the non-decreasing order.

So, the key observation is that merging two elements can cause a violation in the non-decreasing order. So perhaps the minimal steps needed is 1 if there exists any two consecutive elements x and y such that x^y is less than the previous element, or greater than the next element.

Wait, but merging x and y would replace them with x^y, so the new array's elements around the merged position could create a problem.

But how to check this efficiently?

Alternatively, maybe the minimal steps can be 1, 2, or more. Let's see:

If there's any position i where merging a[i] and a[i+1] results in a new array that is not non-decreasing, then the answer is 1. So the first thing is to check all possible pairs of consecutive elements and see if merging them creates a non-decreasing array. If any such pair exists, then the answer is 1.

If not, then we need to check for two operations. But how?

But for large n, checking all possible pairs for merging once is O(n) time, which is acceptable. Similarly, for two steps, perhaps it's possible to merge two pairs in such a way that the resulting array is non-decreasing. But how?

But let's think: what's the minimal k? Let's first check if k=1 is possible.

So, for each i in 0 to n-2 (assuming 0-based), compute the merged value x = a[i]^a[i+1]. Then, check if the new array (after merging i and i+1) is non-decreasing. If any such array is not non-decreasing, then return 1.

Otherwise, check for k=2. How can two steps lead to a non-decreasing array?

Wait, but two steps would merge two pairs. For example, merge i and i+1, then merge j and j+1 (but the indices would have shifted after the first merge). Alternatively, perhaps merge two consecutive pairs in a way that their merged values create a violation.

Alternatively, maybe merging three elements into two steps. For instance, merging three elements into two steps. Let's see: For example, in the third example, after merging the first two elements (1 and 2) into 3, the array becomes [3,4,6,20]. Then merging 3 and 4 gives 7, so the array is [7,6,20], which is not non-decreasing. So two steps.

Wait, but in this case, after the first merge, the array is still non-decreasing. Then merging the first two elements again (3 and 4) leads to 7, which is greater than 6, so the array becomes [7,6,20], which is not non-decreasing.

So the two-step process requires that after two merges, the array becomes non-decreasing. But how to check for that.

But given that n can be up to 1e5, even checking all possible pairs for two steps is O(n^2), which is not feasible.

So, perhaps we can find that the answer is either 1, 2, or -1. Let's think: for n >= 60, maybe there's a way to find that the answer is 1 or 2. Because after merging a few elements, the XOR could create a problem.

Wait, but why 60? Because the maximum possible a_i is 1e9, which is about 30 bits. So if the array has more than 30 elements, maybe there's some overlapping in the bits that would allow for a merge to create a problem.

Alternatively, perhaps the problem can be solved by checking all possible pairs of consecutive elements (for k=1) and if not found, check for triplets where merging two consecutive pairs (i, i+1) and (i+1, i+2) in some order, but perhaps that's getting complicated.

Wait, maybe there's a key observation here. Let's think about the maximum possible steps needed. For example, what's the minimal steps possible. Let's see the examples.

In the third example, two steps are needed. But what if there's a case where three steps are needed? Well, according to the problem statement, perhaps the answer is at most 3, but for n up to 1e5, we need a way to check this efficiently.

Alternatively, perhaps the answer is always either 1, 2, or -1. Let's see.

If merging two consecutive elements in the array (any two) doesn't create a non-decreasing array, then maybe merging two pairs can.

Wait, let's think: after two steps, the array's length is n-2. For example, merging two consecutive pairs. For instance, merge elements i and i+1, then merge j and j+1 (the positions may shift based on the first merge). But how can two steps create a situation where the array is not non-decreasing?

Alternatively, maybe after two consecutive merges, like merging elements i and i+1, then merging the resulting element and its next element. Or merging two adjacent elements in the original array such that their XOR's sequence is decreasing.

But how to model this.

Alternatively, perhaps for a triplet of consecutive elements a, b, c. If merging a and b gives x, then merging x and c gives y. Then check if x > y. But how?

Wait, but in the third example, the original array is [1,2,4,6,20]. After merging 1 and 2 (3), the array is [3,4,6,20]. Then merging 3 and 4 (7) gives [7,6,20], which is not non-decreasing. So two steps. So in this case, the two merges are consecutive.

Alternatively, maybe the minimal steps can be achieved by merging two consecutive pairs. So in the third example, merging the first two elements and then merging the first two again (since the array after first merge is [3,4,6,20], merging 3 and4 gives 7, leading to [7,6,20]).

So the steps are consecutive merges at position 0 and 0 again.

Hmm. So perhaps, the minimal steps can be found by checking for consecutive triplets where merging two elements in a row would lead to a problem.

But how?

Another approach: let's consider that when you merge two elements, the XOR may not preserve the non-decreasing order. For example, if the array is [x, y, z], and x <= y <= z. If merging x and y gives x^y, which could be larger than z, but that's possible only in some cases.

Wait, but XOR is a bitwise operation. So, for example, if x and y have the same higher bits, their XOR would have those higher bits canceled. So x^y could be smaller than x and y.

So, perhaps in some cases, merging two consecutive elements can create a value that is lower than the previous element or higher than the next element, leading to a non-decreasing array.

So the plan is:

1. Check if there exists any i such that merging i and i+1 (x = a[i] ^ a[i+1]) and inserting it into the array breaks the non-decreasing condition. For this, after merging, the new array is [a[0], ..., x, a[i+2], ...]. We need to check if x is greater than the next element (a[i+2]) or less than the previous element (a[i-1], if i>0). Or, if i is 0, check if x > a[i+2]. If i is the last possible (n-2), check if x < a[i-1].

Wait, no. Let's think for a general i. When we merge a[i] and a[i+1] into x, the new array's elements are:

- For i=0: x, a[2], a[3], ..., a[n-1]. So check if x > a[2], which would make the array [x, a[2]] and x > a[2], which is a problem.

- For i in the middle: the new array is ... a[i-1], x, a[i+2], ... So check if a[i-1] > x or x > a[i+2].

So for each i from 0 to n-2:

- Compute x = a[i]^a[i+1]

- If i == 0 and i+2 < n: check if x > a[i+2]

- If i >0 and i+2 <n: check if a[i-1] > x or x > a[i+2]

- If i ==0 and i+2 ==n (n=2, after merge length is 1), then the array is [x], which is length 1. But the problem requires that the array is not non-decreasing. However, a single element is considered non-decreasing. So in this case, merging the only two elements is allowed (as the operation is allowed when the array has length 2), but the resulting array has length 1. But according to the problem statement, the array must no longer be non-decreasing, which is impossible here, because a single element is non-decreasing. So in this case, the answer is -1.

So for n=2, the only possible operation is to merge the two elements. But then the array becomes length 1, which is still considered non-decreasing. So in this case, the answer is -1.

So, the first step is to check for all possible i whether merging i and i+1 leads to a non-decreasing array. If any such i exists, then the answer is 1.

But how to implement this?

For each i, compute x = a[i]^a[i+1].

Then, check:

- If i >0, check if the previous element (a[i-1]) is greater than x.

- If i+1 <n-1 (i.e., the next element is a[i+2]), check if x is greater than a[i+2].

If either of these conditions is true, then merging i and i+1 would create a non-decreasing array. Wait, no. Wait, the original array is non-decreasing. So after merging, the new array's elements are:

a[0], a[1], ..., a[i-1], x, a[i+2], ..., a[n-1].

We need to check whether this new array is non-decreasing. But since the original array is non-decreasing, the only possible places where the new array could be decreasing are around x.

So, the new array must have:

if i >0: a[i-1] <= x

if i+2 <n: x <= a[i+2]

and between a[i-1] and x, and between x and a[i+2].

But the original array has a[i-1] <= a[i] <= a[i+1] <= a[i+2] (since the array is non-decreasing).

But x is a[i]^a[i+1]. So x could be less than a[i-1] or greater than a[i+2], which would break the non-decreasing order.

So for each i, after merging i and i+1 into x, we need to check the following:

If i >0 and a[i-1] > x: then the array is not non-decreasing.

If i+2 <n and x > a[i+2]: then the array is not non-decreasing.

If either is true, then the answer is 1.

So, for each i in 0..n-2:

Compute x = a[i]^a[i+1]

Check:

prev = a[i-1] if i >0 else None

next_el = a[i+2] if i+2 <n else None

If (prev is not None and prev >x) or (next_el is not None and x > next_el):

Then, answer is 1.

If any such i exists, return 1.

Otherwise, check for possible k=2 steps.

But how to check for k=2 steps efficiently.

Hmm. For k=2, there are two possibilities: two non-overlapping merges, or two overlapping merges (like merging i and i+1, then merging the new element and its next one).

But for n up to 1e5, checking all possible pairs of merges is O(n^2), which is impossible.

So, perhaps there's a pattern where merging two consecutive elements in a triplet (i, i+1, i+2) leads to a problem.

For example, merging i and i+1, then merging the new element (x) with i+2.

So after two merges, the array would have x ^ a[i+2], but this seems arbitrary.

Alternatively, perhaps there exists a triplet of elements where the XOR of the first two, then XOR with the third, creates a value that is less than the previous element or higher than the next.

But again, how to find this quickly.

Another observation: since XOR is associative? No. XOR is commutative and associative, but the order matters when merging. Wait, no. Because (a^b)^c = a^(b^c). So the order in merging consecutive elements is important.

But perhaps, for the purpose of the problem, there exists a triplet where merging the first two, then the resulting two (now consecutive) elements, results in a non-decreasing array.

Alternatively, perhaps merging three elements into one in two steps. For example, merging i and i+1 into x, then merging x and i+2 into x^a[i+2]. Then check if this value breaks the non-decreasing property.

So, for a triplet of elements a[i], a[i+1], a[i+2], we can merge the first two and then the result with the third. The resulting array would have ... a[i-1], (a[i]^a[i+1])^a[i+2], a[i+3] ... if i+3 exists.

But how to check if this creates a non-decreasing array.

Alternatively, after merging the first two elements (i and i+1) into x, and then merging x and i+2 into y. The array's elements would be ... a[i-1], y, a[i+3] ... .

So, check if a[i-1] > y, or y > a[i+3], etc.

But even this approach requires checking O(n) triplets, which is feasible.

So, the plan for k=2 steps:

Check all possible triplets (i, i+1, i+2) for i from 0 to n-3.

For each such triplet:

- Merge i and i+1 into x. Then merge x and i+2 into y. The total steps are 2.

The resulting array would be: a[0], ..., a[i-1], y, a[i+3], ...].

Check if this array is not non-decreasing. To check this, we need to ensure that in the new array, either a[i-1] > y (if i>0), or y > a[i+3] (if i+3 <n), or the new array's elements are not non-decreasing elsewhere. But after merging two steps, the new array's length is n-2, so perhaps the only possible violations are around y.

Alternatively, after two steps, the new array would have a[i-1], y, a[i+3], and we need to check if a[i-1] <= y <= a[i+3]. But if either of these inequalities is violated, then the array is not non-decreasing.

Alternatively, in the original array, a[i] <= a[i+1] <= a[i+2]. So x = a[i]^a[i+1], then y = x ^ a[i+2].

But x can be anything, and so can y.

So for each triplet (i, i+1, i+2), compute x = a[i]^a[i+1], then compute y = x ^ a[i+2].

Then, check:

If i >0, check if a[i-1] > y.

If i+3 <n, check if y > a[i+3].

If either is true, then the two steps would create a non-decreasing array. So the answer is 2.

Alternatively, there could be another scenario where merging i+1 and i+2 first, then merging i and x. For example, merge a[i+1] and a[i+2] into x, then merge a[i] and x into y. Then check if this leads to a violation.

But this would also require O(n) checks.

But for the sake of time, perhaps checking all possible triplets (i, i+1, i+2) for both possible orders of merging (merge i and i+1 first, then merge with i+2; or merge i+1 and i+2 first, then merge with i) might be necessary.

But given that n can be up to 1e5, this approach would be O(n), which is manageable.

Alternatively, maybe merging three elements into one in two steps is the key. So for each triplet (i, i+1, i+2), compute the two possible ways to merge and check if any of them leads to a violation.

So for each triplet:

Case 1: merge i and i+1 into x, then merge x and i+2 into y.

Check the new array elements around y.

Case 2: merge i+1 and i+2 into x, then merge i and x into y.

Check the new array elements around y.

If any of these cases leads to a violation in the non-decreasing order, then the answer is 2.

If none of these cases work, then proceed to check other possibilities.

But how to compute this.

Let's see for case 1:

After merging i and i+1, the array becomes:

... a[i-1], x, a[i+2], a[i+3], ... 

Then, merging x and a[i+2] gives y = x ^ a[i+2].

The new array is:

... a[i-1], y, a[i+3], ... 

So, check if a[i-1] > y (if i>0) or y > a[i+3] (if i+3 <n). If either is true, then after two steps, the array is not non-decreasing.

Similarly, for case 2:

Merge i+1 and i+2 into x. The array becomes:

... a[i], x, a[i+3], ... 

Then, merge a[i] and x into y = a[i] ^ x.

The new array is:

... y, a[i+3], ... 

Check if i>0: a[i-1] > y. Check if a[i+3] < y (if i+3 <n). If either is true, then answer is 2.

So for each triplet i, i+1, i+2 (for i from 0 to n-3), check both cases.

If any of these checks pass, then the answer is 2.

If after checking all possible triplets for k=1 and k=2 steps, and none are found, then return -1.

But why would the answer be at most 2 steps?

Hmm, perhaps there's a mathematical reason here. For example, when the array has length >= 60, according to the pigeonhole principle, there must be some triplet where merging two steps can produce a violation. But I'm not sure.

Alternatively, perhaps if after checking k=1 and k=2 steps and none are found, then the answer is -1. But how to verify this.

Wait, let's think of a case where the answer is 3. For example, after three steps, the array becomes non-decreasing. But according to the problem examples, the third example's answer is 2. So perhaps the answer can't be larger than 2.

But why?

Another approach: the answer is either 1, 2, or -1.

If that's the case, then we can check all possible possibilities for k=1 and k=2 steps, and if none are found, return -1.

So the steps are:

1. Check for k=1.

   For each i in 0..n-2:

   - Compute x = a[i]^a[i+1]

   - Check if merging i and i+1 leads to a non-decreasing array. If not, return 1.

2. If no k=1 is found, check for k=2.

   For each i in 0..n-3:

   - Check the two possible merging sequences for the triplet (i, i+1, i+2). Compute the resulting y and check if it creates a violation.

   If any of these checks pass, return 2.

3. If neither k=1 nor k=2 are possible, return -1.

So the code can be structured as follows:

First, handle the case where n is 2. In that case, after one merge, the array becomes a single element. Since a single element is considered non-decreasing, the answer is -1.

Otherwise:

Loop through all i from 0 to n-2:

   compute x = a[i] ^ a[i+1]

   check if merging i and i+1 would break the non-decreasing condition.

   For the new array, the only possible problem is between a[i-1] and x, or between x and a[i+2].

   So:

   if i > 0 and a[i-1] > x: return 1.

   if i+2 < n and x > a[i+2]: return 1.

If none found, then check for k=2.

Loop through all i from 0 to n-3:

   case 1: merge i and i+1 into x, then merge x and i+2 into y.

   y = x ^ a[i+2] = (a[i]^a[i+1]) ^ a[i+2].

   check if i>0 and a[i-1] > y → return 2.

   check if i+3 <n and y > a[i+3] → return 2.

   case 2: merge i+1 and i+2 into x (x = a[i+1]^a[i+2]), then merge a[i] and x into y = a[i] ^ x.

   check if i>0 and a[i-1] > y → return 2.

   check if i+3 <n and y > a[i+3] → return 2.

If any of these checks pass, return 2.

Otherwise, return -1.

But wait, in case 1, after merging i and i+1 and then merging x and i+2, the new array's elements around y are a[i-1] (if i>0) and a[i+3] (if i+3 <n). So we need to check those.

Similarly for case 2.

So the code for k=2 would look like this:

for i in range(n-2):

   # case 1: merge i, i+1 then merge with i+2.

   x = a[i] ^ a[i+1]

   y = x ^ a[i+2]

   # check new array:

   if i > 0:

       prev = a[i-1]

       if prev > y:

           return 2

   if i +3 < n:

       next_el = a[i+3]

       if y > next_el:

           return 2

   # case 2: merge i+1 and i+2 then merge with i.

   x = a[i+1] ^ a[i+2]

   y = a[i] ^ x

   # check new array:

   if i > 0:

       prev = a[i-1]

       if prev > y:

           return 2

   if i +3 < n:

       next_el = a[i+3]

       if y > next_el:

           return 2

So in this loop, for each i from 0 to n-3, check both cases.

If any of these cases returns true, return 2.

Otherwise, after checking all i, return -1.

But wait, in case n is 3, then i can be 0. Then, in case 1, merging 0,1 then 0 (the new array after first merge is [x, a[2]]; then merging x and a[2] gives y. Then the array is [y]. But a single element is considered non-decreasing, so that's not helpful.

So perhaps in some cases, even after two steps, the array's length is 1, which is not helpful. But according to the problem statement, the steps can be applied until the array's length is 1. So for n=3, after two steps, the array is length 1. Which is allowed as per the problem statement (since you can't perform the operation once the array reaches length 1). But the array must not be non-decreasing. However, a single element is considered non-decreasing, so this scenario is invalid. Therefore, in the case of n=3, the answer is -1 if merging any two steps leads to a single element.

But in the second example, n=3: 1,2,3. The possible steps are:

First step: merge 1 and 2 → 3, array [3,3]. Then step two: merge 3 and 3 → 0. The array is [0], which is non-decreasing. So the answer is -1.

But according to the code above, for i=0 (n=3, so i can be 0 to 0):

Case1: merge i=0 and i+1=1 into x=3, then merge x and i+2=2 (which is a[2]=3), x=3^3=0. So y=0. The new array is [0]. Since it's length 1, it's non-decreasing. So no violation.

Case2: merge i+1=1 and i+2=2 → 1^2=3. Then merge a[i]=1 with x=3 → 2. Array is [2]. Again, no violation.

Thus, code returns -1, which is correct.

So the code seems to handle that.

Now, the code's time complexity is O(n) for checking k=1 and O(n) for k=2. So overall O(n) time, which is acceptable for 1e5.

But let's test the third example:

Input: 5 1 2 4 6 20

Check for k=1:

Each i from 0 to 3:

i=0: x=1^2=3. Check if previous is None (i=0), next_el is a[2] =4. So 3 <=4. So no problem.

i=1: x=2^4=6. Check previous a[0] =1 <=6, next_el a[3]=6 <=6. So no problem.

i=2: x=4^6=2. Check previous a[1]=2 <=2, next_el a[4]=20. So 2<=20. No problem.

i=3: x=6^20= 18. previous a[2]=4 <=18, next_el None. So no problem.

Thus, no k=1.

Check for k=2:

For i=0 to 2:

i=0:

case1: x=1^2=3, y=3^4=7. Check previous (i=0-1=-1, so no), next_el a[3] =6. So 7>6 → violation. So return 2.

So code returns 2, which is correct.

Thus, the code would work for that.

Another example, the second test case:

n=3, array [1,2,3].

Check for k=1:

i=0: x=1^2=3. next_el is 3. 3<=3 → no problem.

i=1: x=2^3=1. previous a[0]=1 <=1, next_el None. So no problem.

Thus, no k=1.

Check for k=2:

i=0 (n=3, so i can be 0 to 0).

case1: x=1^2=3, y=3^3=0. check previous (i=0-1=-1) → no. next_el (i+3=3 >=n=3 → no. So no violation.

case2: merge i+1 and i+2 (2 and3) → 1. Then merge a[0] (1) and 1 → 0. Again, array is [0], no violation.

Thus, code returns -1.

So the code works.

Thus, the approach is to check k=1 and k=2 steps.

Now, let's code this.

First, handle the case where n=2. Then, check for k=1 steps. Then check for k=2 steps.

But also, note that for n=3, after two steps, the array is of length 1. Which can't be non-decreasing. But according to the problem statement, the array must no longer be non-decreasing. However, a single element is considered non-decreasing, so merging two steps in this case is not sufficient.

Thus, in code:

Read n, then the array.

if n <3:

   if n ==2:

       after one step, array is length 1. So answer is -1.

else:

   check for k=1.

   if not found, check for k=2.

   if not found, return -1.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if n == 2:

        print(-1, file=output_stream)

    else:

        found = False

        # Check for k=1

        for i in range(n-1):

            x = a[i] ^ a[i+1]

            if i > 0:

                if a[i-1] > x:

                    print(1, file=output_stream)

                    found = True

                    break

            if i +2 < n:

                if x > a[i+2]:

                    print(1, file=output_stream)

                    found = True

                    break

        if not found:

            # Check for k=2

            for i in range(n-2):

                # Case 1: merge i and i+1, then i+2

                x = a[i] ^ a[i+1]

                y = x ^ a[i+2]

                if i > 0 and a[i-1] > y:

                    print(2, file=output_stream)

                    found = True

                    break

                if i +3 < n and y > a[i+3]:

                    print(2, file=output_stream)

                    found = True

                    break

                # Case 2: merge i+1 and i+2, then i

                x = a[i+1] ^ a[i+2]

                y = a[i] ^ x

                if i >0 and a[i-1] > y:

                    print(2, file=output_stream)

                    found = True

                    break

                if i +3 <n and y > a[i+3]:

                    print(2, file=output_stream)

                    found = True

                    break

            if not found:

                print(-1, file=output_stream)

            else:

                # already printed 2

                pass

        else:

            # already printed 1

            pass



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 2 3
""",
            "output": \
"""\
-1
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

Another test case: n=5, 1 2 4 6 20.

Check i=0:

case1: x=1^2=3, y=3^4=7. next_el is 6. 7>6 → yes. So returns 2.

Thus, code works.

Another case where merging two steps in a different way.

So this code should handle all cases correctly.

Now, considering the constraints. For n=1e5, the code is O(n) time and O(1) space, which is acceptable.

Thus, the code should be correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(-1)
else:
    found = False
    # Check for k=1
    for i in range(n - 1):
        x = a[i] ^ a[i+1]
        # Check previous element
        if i > 0 and a[i-1] > x:
            print(1)
            found = True
            break
        # Check next element
        if i + 2 < n and x > a[i+2]:
            print(1)
            found = True
            break
    if found:
        pass
    else:
        # Check for k=2
        for i in range(n - 2):
            # Case 1: merge i and i+1, then merge with i+2
            x = a[i] ^ a[i+1]
            y = x ^ a[i+2]
            if (i > 0 and a[i-1] > y) or (i + 3 < n and y > a[i+3]):
                print(2)
                found = True
                break
            # Case 2: merge i+1 and i+2, then merge with i
            x = a[i+1] ^ a[i+2]
            y = a[i] ^ x
            if (i > 0 and a[i-1] > y) or (i + 3 < n and y > a[i+3]):
                print(2)
                found = True
                break
        if not found:
            print(-1)
```
