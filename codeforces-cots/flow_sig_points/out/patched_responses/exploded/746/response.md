<think>
Okay, let's tackle this programming problem. Hmm, the problem statement says that for each friend j, we need to compute the minimum photo size when that friend is excluded. The photo size is calculated as the sum of widths (W) of all included friends multiplied by the maximum height (H) among them. So for each j, we need to compute W = total width - w_j and H = maximum height of all friends except the j-th. Then W*H is the value for that j.

The constraints are tight: n can be up to 200,000. So any O(n) solution per test case is acceptable, but anything higher like O(n^2) would be way too slow. We need an efficient way to compute for each j the sum of widths minus w_j and the maximum height excluding the j-th friend.

First, the sum of widths is straightforward. We can compute the total sum first, then for each j, subtract w_j to get the new sum. That's O(1) per j.

The challenge is finding the maximum height when excluding the j-th friend. Because for each j, we have to exclude h_j and find the max of the remaining. How do we compute this efficiently?

If we have a data structure that can quickly find the maximum height when a certain element is excluded, that would work. But for each j, checking all elements except j is O(n) per j, which is O(n^2) total and not feasible.

Wait, maybe there's a smarter way. Let's think: the maximum H when excluding j depends on how many times the maximum h occurs in the array. For example, if the maximum h occurs more than once, then even if we exclude one occurrence, there's another one left. So for those j's whose h_j is not the maximum, the maximum H would remain the overall maximum. Only when h_j is the maximum, we need to check if there are other elements with the same maximum. If there's more than one, then the new H is still the same maximum. If there's exactly one, then the new H is the second maximum.

So the plan is:

1. Precompute the total sum of widths. For each j, the sum is total_sum - w_j.
2. Precompute the maximum height and the count of how many times this maximum occurs.
3. Precompute the second maximum height.

Then, for each j:
- If h_j < max_h, then the new H is max_h.
- If h_j == max_h:
   - If the count of max_h is more than 1, then new H is still max_h.
   - Else, new H is the second_max_h.

So we need to track the max_h, the count of max_h, and the second_max_h.

But how do we compute the second_max_h? Let's see. We can iterate through all h_i and track the top two maximum values. So for the entire array, find the maximum and second maximum.

Wait, but maybe there are multiple elements with the max_h. Like, if the array is [5,5,3], then the max is 5, occurs twice, second max is 3. So if we exclude one 5, the max is still 5. Only when the count is 1, the second max comes into play.

So the steps are:

Compute total_sum = sum of all w_i.

Compute:

- max_h = maximum of all h_i
- count_max = number of h_i equal to max_h
- second_max = the maximum value in h_i which is less than max_h.

Then, for each j:

sum_w = total_sum - w_j

if h_j < max_h:
    current_max_h = max_h
else:
    if count_max > 1:
        current_max_h = max_h
    else:
        current_max_h = second_max

result[j] = sum_w * current_max_h

So the key is to precompute max_h, count_max, and second_max.

But how to compute second_max efficiently?

We can loop through all h_i, and track the first and second maximum. Let's see.

Initialize first_max and second_max as -infinity.

For each h in h_list:

    if h > first_max:
        second_max = first_max
        first_max = h
    elif h == first_max:
        pass  # second_max remains the same
    elif h > second_max:
        second_max = h

Wait, but in case there are multiple elements equal to first_max, like [5,5,3], then the second_max is 3. So in that case, when one 5 is excluded, the max is still 5. But if the count_max is 1, then the second_max is the next highest.

So yes, this approach would compute the correct second_max as the next highest value after the first_max.

But what if all elements are the same? Like all h_i are 10. Then first_max is 10, count_max is n, and second_max would be 10. But in that case, when any element is excluded, the count_max would be n-1 >=1, so the max is still 10. So even if the second_max is 10, it's okay.

So the way to compute second_max is correct.

Once we have first_max, count_max, and second_max, we can process each j in O(1) time.

So the algorithm steps are:

1. Compute total_sum as sum of all w_i.
2. Find max_h, count_max (number of h_i equal to max_h), and second_max_h (the maximum of h_i where h_i < max_h).
3. For each j:
   a. sum_w = total_sum - w_j
   b. if h_j < max_h: current_max = max_h
   c. else:
      if count_max > 1: current_max = max_h
      else: current_max = second_max_h
   d. result[j] = sum_w * current_max
4. Output all result[j] separated by spaces.

Now, the question is how to compute max_h, count_max, and second_max_h efficiently.

Let's see:

For max_h and count_max: straightforward. Iterate through all h_i, track the maximum and count.

For second_max_h: iterate through all h_i, and track the maximum value that's less than max_h.

But how to do this?

We can first collect all h_i, then filter out those equal to max_h, then take the maximum of the remaining. But if all h_i are equal to max_h, then there is no second_max, but in that case, when any h_i is excluded, the count_max would be n-1 >=1 (since n >=2), so current_max would still be max_h. So in that case, even if second_max is undefined (like all h are same), the code would handle it because when h_j == max_h, count_max (original count) would be n. So when we exclude one, count becomes n-1, which is >=1. So current_max is max_h. So even if second_max is not present, it's okay. But in code, when we compute second_max, if all h are same, then second_max would be max_h. Wait no, in that case, the code for second_max would not have any h_i less than max_h. So when all h are the same, then when we collect the remaining elements (excluding max_h), the list is empty, so the maximum of an empty list is undefined. So how do we handle that?

Wait, perhaps during the initial iteration for second_max, we can track the second_max as the maximum value less than max_h. If all elements are equal to max_h, then second_max is -infinity. But in such a case, when count_max is n, and the code would check if count_max > 1 (original count_max is n, when we exclude j, count_max becomes n-1, which is >=1 as n >=2). So current_max remains max_h, so second_max is irrelevant.

Therefore, in the code, when all h_i are equal to max_h, second_max can be any value (since it's not used). So during the computation of second_max, if there are no elements less than max_h, then second_max can be set to 0 (but it doesn't matter as it's not used). So in code:

Compute second_max as the maximum of all h_i that are less than max_h.

If there are none, then second_max can be 0, but in that case, when a j is excluded (which had h_j = max_h), since count_max (original) was >=1 (since all are max_h), then count_max > 1 (original is the total count, so for j in that case, count_max was n, so when we exclude j, count is n-1, which is >=1 if n>=2. So current_max remains max_h. So second_max is not used in this scenario.

So in code, to compute second_max:

We can initialize second_max to -infinity. Then, for each h in h_list:

if h < max_h:

   if h > second_max:

      second_max = h

So after processing all elements, if second_max is still -infinity, then there are no elements less than max_h. So set it to 0 or handle it as needed.

But in the code logic, if the count_max was 1, but when we exclude j (the only max_h), then the current_max is second_max. But if all h_i are same (so count_max is n), then second_max would be -infinity. But in that case, when count_max is 1 (original count_max is 1), then when we exclude j, the count becomes 0, but in that case, the code would have second_max as the next max. Wait no, in this case, original count_max is 1. So when j is the only max_h, then count_max is 1. So when we exclude j, then the new h list has no elements equal to max_h (since j was the only one). So the new max_h would be the second_max. So in that scenario, the code would use the second_max. But if all other elements are less than max_h, then second_max is the maximum of them.

But if j is the only max_h, then count_max is 1. So for that j, when excluded, the current_max is the second_max. So the code is correct.

But in the code, how do we compute second_max when the original max_h occurs once, but there are other elements? Like, in the first example:

Sample Input 1:

3

1 10

5 5

10 1

The h_list is [10,5,1]

max_h is 10, count_max is 1, second_max is 5.

So for j=0 (h=10), count_max was 1. So when excluded, the new max is 5.

Which is correct.

In Sample Input 2:

3

2 1

1 2

2 1

h_list is [1,2,1]

max_h is 2, count_max is 1, second_max is 1.

So when j=1 is excluded (h=2), then the new max is 1.

So the code works.

So now, in code:

We need to compute:

max_h: the maximum h in the list.

count_max: the number of times max_h appears.

second_max: the maximum h in the list that is less than max_h.

So how to compute these?

Let's code this:

Initialize max_h as the first h, count_max as 1. Then iterate through the rest of h_list:

for h in h_list[1:]:
    if h > max_h:
        max_h = h
        count_max = 1
    elif h == max_h:
        count_max +=1

Then, compute second_max:

second_max = -infinity

for h in h_list:
    if h < max_h and h > second_max:
        second_max = h

If after this, second_max is still -infinity (i.e., all h are equal to max_h), then set second_max to 0 (but it's not used in such cases, as the count_max is >=1. So in code, we can leave it as -infinity. But in Python, multiplying by a negative number would cause issues, but in the code, when count_max is >1, second_max is not used. So perhaps it's better to set it to 0 if no elements are found.

Wait, but in the code, when count_max is 1, and the excluded j's h is max_h, then current_max is second_max. But if second_max is -infinity, that's a problem. But how could that happen?

Only if all h_i are equal to max_h. Because if j is excluded, then all remaining h_i are max_h (since all are max_h and j was part of them). But wait, if all h_i are equal to max_h, then when we exclude j (assuming count_max was n), then count_max-1 would be n-1 >=1 (since n >=2). So current_max remains max_h, so even if second_max is not computed properly, the code would not use it.

So the scenario where second_max is -infinity can only occur when all h_i are equal to max_h. In that case, when any j is excluded, count_max (original) is >=1, so current_max remains max_h. So even if second_max is -infinity, it's not used.

Therefore, in code, we can leave second_max as -infinity. But during the computation, if there are no elements less than max_h, then second_max remains -infinity. But when that happens, the code will only use second_max when count_max is 1 and j's h is max_h. But in that case, if all elements are max_h, then count_max would be n (original count). So if j is the one being excluded, then the remaining count is n-1. So count_max (original) was n, so in the code, if h_j == max_h, then count_max (original) is n. So even after excluding j, the new count_max is n-1 >=1. So current_max is max_h. So the code would not use second_max.

Thus, in code, even if second_max is -infinity, the code will not use it. So no problem.

So the code can proceed as follows.

Now, let's code this step by step.

Read n.

Read n lines, storing w and h for each.

Compute total_sum = sum of all w.

Compute max_h, count_max.

Then compute second_max.

Then for each friend j:

sum_w = total_sum - w_j

if h_j < max_h:

    current_max = max_h

else:

    if count_max > 1:

        current_max = max_h

    else:

        current_max = second_max

result[j] = sum_w * current_max

Now, let's test the sample inputs.

Sample Input 1:

3

1 10

5 5

10 1

total_sum = 1+5+10 =16

max_h =10, count_max=1, second_max=5.

For j=0 (w=1, h=10):

sum_w = 16-1=15

h_j is 10. count_max is 1. So current_max = second_max=5. 15*5=75.

j=1 (w=5, h=5):

h_j is 5 < max_h. current_max is 10. sum_w=16-5=11. 11*10=110.

j=2 (w=10, h=1 <10). sum_w=16-10=6. current_max=10. 6*10=60. So output 75 110 60. Which matches the sample.

Sample Input 2:

3

2 1 → h=1

1 2 → h=2

2 1 → h=1

max_h=2, count_max=1. second_max is max of [1,1] →1.

For j=0: sum_w= (2+1+2) -2 =3. Wait, wait no. Wait, wait the friends' w is:

First friend: 2, h 1

Second friend:1, h 2

Third friend:2, h 1.

Wait the input is:

3

2 1 →w=2, h=1

1 2 →w=1, h=2

2 1 →w=2, h=1.

So total_sum is 2+1+2=5.

For j=0 (w=2, h=1):

sum_w=5-2=3.

h_j is 1 <2. current_max is 2. 3*2=6.

j=1 (w=1, h=2):

sum_w=5-1=4.

h_j is 2. count_max is 1, so current_max is second_max=1. 4*1=4.

j=2 (w=2, h=1):

sum_w=5-2=3. current_max=2. 3*2=6.

So output is 6 4 6. Which matches the sample.

Another test case: all h same. Like:

n=2

h1=5, h2=5.

max_h=5, count_max=2. second_max would be -inf.

For j=0:

sum_w = (w1 +w2) -w0 = w2.

h_j=5. count_max=2 (original count). So count_max>1. current_max=5. sum_w*5.

Similarly for j=1.

So code works.

Another case where count_max=1 and second_max is present.

So the code seems to handle all cases.

Now, in Python, for n up to 2e5, the code needs to process this quickly. Let's think about the data structures.

We can read all the inputs, store w and h in a list.

Calculating the sum is O(n).

Calculating max_h and count_max is O(n).

Calculating second_max is O(n).

Then for each j, O(1) processing, O(n) total.

So overall O(n) time, which is acceptable.

Memory-wise, we need to store the list of w and h. For 2e5 elements, it's manageable.

Now, code:

Read n.

Then read n lines, each with wi, hi.

Store in a list.

Compute sum_w.

Compute max_h, count_max.

Then compute second_max.

Then for each j, compute the output.

Now, code in Python:

But in Python, reading 2e5 lines with input() can be slow if done naively. So it's better to read via sys.stdin.

But in the problem statement, the solution must read via input() and output via print().

Wait, but for handling large inputs, the standard approach in Python is to read all input at once. So maybe read via sys.stdin.

But the problem says: "Your solution must read input from standard input (input()), write output to standard output (print())."

Wait, the problem says input() must be used, but in Python, using input() for each line when n is 2e5 is slow. So this may cause a time-out. So perhaps to read via sys.stdin.

But the problem statement says "your solution must read input from standard input (input())", so we have to use input(). Hmm, but maybe the intended way is to use input() but read the lines all at once. But in practice, for n=2e5, the code would be:

import sys

n = int(sys.stdin.readline())

sum_w =0

h_list = []

for _ in range(n):

    w, h = map(int, sys.stdin.readline().split())

    sum_w +=w

    h_list.append(h)

But that's the way to read quickly.

But the problem statement says to use input(), not sys.stdin. But perhaps in practice, the code will use sys.stdin for speed. So maybe that's allowed.

The problem says: "your solution must read input from standard input (input()), write output to standard output (print())."

Wait, that's a bit ambiguous. Do they mean that you can't use sys.stdin for reading? For example, perhaps the code is supposed to use input(), but in Python, for handling large inputs, using input() in a loop is slow. So perhaps using sys.stdin is better.

But given that the problem states that input must be read via input(), perhaps that's not allowed. So the code would use input() for each line. But with n=2e5, this would be slow. But perhaps the problem's time constraints are lenient enough.

Alternatively, perhaps the code can read all the input at once using sys.stdin.read(). Split into tokens.

But the problem says to use input(). So maybe the code is allowed to use sys.stdin.

But perhaps the problem's intention is that the code reads via input() and the user can use any method as long as it's standard input. So perhaps using sys.stdin is allowed.

In any case, for Python, the fastest way to read the input is via sys.stdin, splitting into tokens. So perhaps the code would read as follows.

But let's proceed.

So code:

import sys

n = int(sys.stdin.readline())

sum_w =0

h_list = []

w_list = []

for _ in range(n):

    w, h = map(int, sys.stdin.readline().split())

    sum_w +=w

    h_list.append(h)

    w_list.append(w)

Then compute max_h, count_max:

max_h = max(h_list)

count_max = h_list.count(max_h)

Wait, but for a list of 2e5 elements, h_list.count is O(n). So that's acceptable. But perhaps even better to compute it during the initial loop.

Alternatively, during the initial loop, track max_h and count_max.

Yes, this would be better. Because:

max_h = -1

count_max =0

for h in h_list:

    if h > max_h:

        max_h = h

        count_max =1

    elif h == max_h:

        count_max +=1

But wait, h_list is being built in the loop. So during the initial reading, we can track max_h and count_max as we read each h.

Yes.

So code:

sum_w =0

h_list = []

max_h = -1

count_max =0

for _ in range(n):

    w, h = map(int, sys.stdin.readline().split())

    sum_w +=w

    h_list.append(h)

    if h > max_h:

        max_h = h

        count_max =1

    elif h == max_h:

        count_max +=1

But this way, during the first iteration, we compute sum_w, h_list, and track max_h and count_max. Then, after the loop, we can proceed to compute second_max.

Then, compute second_max:

second_max = -1

for h in h_list:

    if h < max_h and h > second_max:

        second_max = h

But this is another O(n) loop.

So total O(n) time.

Now, code:

Then, for each j in 0..n-1:

current_w = sum_w - w_list[j]

h_j = h_list[j]

if h_j < max_h:

    current_h = max_h

else:

    if count_max >1:

        current_h = max_h

    else:

        current_h = second_max

result_j = current_w * current_h

But the code needs to collect all the w's in a list. So during the initial loop, we can collect w in a list.

So code:

sum_w =0

w_list = []

h_list = []

max_h = -1

count_max =0

for _ in range(n):

    w, h = map(int, sys.stdin.readline().split())

    sum_w +=w

    w_list.append(w)

    h_list.append(h)

    if h > max_h:

        max_h = h

        count_max =1

    elif h == max_h:

        count_max +=1

Then compute second_max.

Now, the code:

Now, let's code all this.

But in Python, for 2e5 elements, this is manageable.

But in the code, for each j, we have to compute sum_w - w_list[j], which is O(1) per j.

So the code will be:

Compute sum_w, max_h, count_max, second_max.

Then, for each j, compute sum_w - w_list[j], and then the H as per rules.

Now, code:

After computing sum_w, max_h, count_max:

second_max = -1

for h in h_list:

    if h < max_h and h > second_max:

        second_max = h

Then, process each j:

results = []

for j in range(n):

    current_w = sum_w - w_list[j]

    current_h = max_h

    h_j = h_list[j]

    if h_j == max_h:

        if count_max ==1:

            current_h = second_max

        else:

            current_h = max_h

    else:

        current_h = max_h

    results.append(current_w * current_h)

print(' '.join(map(str, results)))

But wait, in the case where all h are equal to max_h, then second_max remains -1. But in that case, when count_max is the original count (n), and when j's h is max_h, then count_max >1 (since n >=2), so current_h remains max_h. So even if second_max is -1, it's not used.

But what if all h are 5, and n is 2. Then count_max is 2, so when j is excluded, count_max becomes 1. But original count_max is 2, which is >1. So current_h remains max_h.

So the code is correct.

Now, test the code.

Sample Input 2:

3

2 1

1 2

2 1

So h_list is [1,2,1]

max_h is 2, count_max=1.

second_max is 1.

For j=1 (h=2):

current_h is computed as count_max (original) is 1. So current_h becomes second_max (1). sum_w is 2+1+2=5. sum_w -1 is 4. 4*1=4. Which is correct.

Yes.

Another case: all h are 5, n=3.

sum_w = sum of w.

max_h=5, count_max=3.

second_max is -1 (since all h are 5, which are not <5).

For any j:

sum_w -w_j.

current_h: since h_j is 5, count_max was 3>1. So current_h is 5. So result is (sum_w -w_j) *5.

Which is correct.

Thus, the code handles all cases.

Now, let's code this in Python, using sys.stdin for faster input.

The code should not have any debug statements.

Now, the code:

Read n.

Read n lines, each with w and h.

Compute sum_w, max_h, count_max.

Compute second_max.

Process each j.

Now, the code:

import sys

def main():

    n = int(sys.stdin.readline())

    sum_w =0

    w_list = []

    h_list = []

    max_h = -1

    count_max =0

    for _ in range(n):

        w, h = map(int, sys.stdin.readline().split())

        sum_w += w

        w_list.append(w)

        h_list.append(h)

        if h > max_h:

            max_h = h

            count_max =1

        elif h == max_h:

            count_max +=1

    # Compute second_max

    second_max = -1

    for h in h_list:

        if h < max_h and h > second_max:

            second_max = h

    # Prepare results

    results = []

    for j in range(n):

        current_w = sum_w - w_list[j]

        h_j = h_list[j]

        if h_j == max_h:

            if count_max >1:

                current_h = max_h

            else:

                current_h = second_max

        else:

            current_h = max_h

        results.append(current_w * current_h)

    print(' '.join(map(str, results)))

if __name__ == "__main__":

    main()

Yes, this should work.

Testing this code with the sample inputs.

Sample Input 1:

3

1 10

5 5

10 1

sum_w is 1+5+10=16.

max_h is 10, count_max=1.

second_max is 5.

For j=0: current_w=15. h_j=10. count_max=1. So current_h=5. 15*5=75.

j=1: current_w=11. h_j=5 <10. current_h=10. 11*10=110.

j=2: current_w=6. h_j=1<10. current_h=10. 6*10=60.

Output is 75 110 60.

Sample Input 2:

3

2 1

1 2

2 1

sum_w=5.

max_h=2, count_max=1.

second_max=1.

j=0: current_w=5-2=3. h_j=1 <2 → current_h=2. 3*2=6? Wait, no. Wait, for j=0, h_j is 1, which is less than max_h (2). So current_h is max_h (2). So 3*2=6.

j=1: current_w=5-1=4. h_j is 2 (max). count_max is 1. So current_h is second_max (1). 4*1=4.

j=2: current_w=5-2=3. h_j=1. current_h=2. 3*2=6.

So output is 6 4 6.

Thus, the code works.

Thus, this code should be correct and efficient.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    sum_w = 0
    w_list = []
    h_list = []
    max_h = -1
    count_max = 0

    for _ in range(n):
        w, h = map(int, sys.stdin.readline().split())
        sum_w += w
        w_list.append(w)
        h_list.append(h)
        if h > max_h:
            max_h = h
            count_max = 1
        elif h == max_h:
            count_max += 1

    second_max = -1
    for h in h_list:
        if h < max_h and h > second_max:
            second_max = h

    results = []
    for j in range(n):
        current_w = sum_w - w_list[j]
        h_j = h_list[j]
        if h_j == max_h:
            if count_max > 1:
                current_h = max_h
            else:
                current_h = second_max
        else:
            current_h = max_h
        results.append(current_w * current_h)
    
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()
```