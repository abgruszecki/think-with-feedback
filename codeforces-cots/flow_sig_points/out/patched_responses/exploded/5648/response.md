<think>
Okay, let's tackle this problem. So, the task is to process a sequence of integers and answer multiple queries about the number of subarrays whose GCD equals a given value. Hmm, I remember that GCD problems can be tricky, especially with large constraints. Let's think about the approach here.

First, the constraints are tight. The array can be up to 1e5 elements, and there are up to 3e5 queries. So, any O(n^2) approach is definitely out of the question. We need something more efficient.

Let me recall some similar problems. Oh right, there's a method for finding all possible GCDs of subarrays ending at each position. The idea is that for each element in the array, we track all possible GCD values of subarrays ending at that position. Since GCDs can only decrease or stay the same as we add elements, this can be done efficiently by maintaining a map of current GCDs and their counts.

Wait, here's the plan: for each index i in the array, keep a dictionary (like a hash map) that stores the GCD values of all subarrays ending at i, along with the number of times each GCD occurs. For example, when processing the i-th element, we take the previous GCDs (from i-1) and compute their GCD with a[i]. Then, we merge these with a[i] itself (as a subarray of length 1). This way, for each position, we track all possible GCDs and their counts. As we process each element, we can accumulate these counts into a global frequency map. Once we have this global map, answering queries is just a matter of looking up the frequency for each query x.

Let's break it down. For each element a[i], we have a current map. For the previous element's map, each entry is a GCD value g and the count of subarrays ending at i-1 with that GCD. When we take a[i], the new possible GCDs for subarrays ending at i are the GCD of g and a[i] for each g in the previous map, plus a[i] itself. So, for each step, the current map is built by taking all entries from the previous map, computing their GCD with a[i], and grouping duplicates by summing their counts. Then, we add a new entry for a[i] as a subarray of length 1.

By doing this for all elements, and keeping a global frequency dictionary that accumulates the counts of each GCD value across all possible subarrays, we can build up the answer for all possible GCDs. Then, each query is just a lookup into this frequency map.

But wait, how efficient is this? Let's see. For each element, the number of different GCDs in the current map is O(log a[i]), because each time you take GCDs, the value can decrease by at least a factor of 1/2 each step. So, over the entire array, the total number of GCD operations is O(n log a), which is acceptable for n up to 1e5.

Yes, this seems feasible. The time complexity should be O(n log max_a) for building the frequency map, and then O(q) for answering the queries. Since q can be up to 3e5, the total time is acceptable.

So the steps are:

1. Initialize a global frequency dictionary (defaultdict or a normal dict) to count occurrences of each GCD.
2. For each element in the array:
   a. Create a new temporary dictionary for the current element's possible GCDs.
   b. Take the previous element's GCD map, compute GCD with current a[i], and update the temporary dictionary.
   c. Also add the current a[i] as a new GCD (subarray of length 1).
   d. Merge the temporary dictionary into the current element's GCD map, combining counts for the same GCD.
   e. Update the global frequency map by adding the counts from the current element's GCD map.
3. After processing all elements, for each query x, output the value from the global frequency map, or 0 if x is not present.

Now, some edge cases to consider. For example, if a subarray has a GCD that's a divisor of x, but not exactly x. So, the global frequency map should only count exact matches. Also, if a query x is larger than any element in the array, then the answer is 0. For instance, in the first example, the query for 6 is answered with 1, which comes from the subarray [6] (since the third element is 3, so the subarray [6,3] has GCD 3, and the first element is 2, but the subarray [2,6] has GCD 2).

So the key is to correctly accumulate all possible GCDs of all possible subarrays. The approach of tracking GCDs ending at each position seems correct.

Now, let's think about implementing this in Python. Since n is up to 1e5, and for each element we process O(log a) GCDs, the total operations are manageable. However, Python's dictionaries can be a bit slow if not handled carefully, so we need to optimize.

Possible optimizations:

- Use a list of tuples instead of a dictionary for the current GCDs. Since the number of entries is small, appending and iterating through a list might be faster than using a dictionary. But for merging, a dictionary is easier. Hmm. Let's see. For each step, the previous GCDs are in a list of (g, count) pairs. Then for each (g, count), compute new_gcd = gcd(g, a[i]). Then, for all new_gcd values, sum the counts. Then add a new entry for a[i]. So, perhaps using a dictionary for the current state is better, as it allows O(1) lookups when merging.

Wait, here's the process:

For each element a[i], the current GCD map is built as follows:

- Take the previous map (from i-1), which is a dictionary of GCD values and counts.
- For each (g, cnt) in the previous map:
   compute new_gcd = gcd(g, a[i])
   add new_gcd to a temporary dictionary, accumulating counts.
- Also, add a new entry for a[i] itself with count 1.
- Then, the current map is this temporary dictionary.

So for each element, the current map is a new dictionary. But in Python, creating new dictionaries for each element may be slow if n is 1e5. So perhaps we can reuse variables. Let's think. We can have a previous_dict and current_dict. For each i, current_dict starts empty. We process the previous_dict's entries, compute new_gcd, and update current_dict. Then add a[i] to current_dict (if not already present, add 1; else, add 1). Then, previous_dict becomes current_dict for the next iteration.

Wait, no. Because current_dict is built from the previous_dict. Then, after processing, we need to add all entries in current_dict to the global frequency map. Then, previous_dict is replaced by current_dict for the next step.

Wait, perhaps in code:

prev_gcds = {}
global_freq = defaultdict(int)
for num in array:
    curr_gcds = defaultdict(int)
    # Process previous GCDs
    for g in prev_gcds:
        new_g = gcd(g, num)
        curr_gcds[new_g] += prev_gcds[g]
    # Add the current number as a subarray of length 1
    curr_gcds[num] += 1
    # Update the global frequency
    for g in curr_gcds:
        global_freq[g] += curr_gcds[g]
    # Set prev_gcds for next iteration
    prev_gcds = curr_gcds

But wait, in Python, dictionaries are mutable, so prev_gcds = curr_gcds would make prev_gcds reference the same dictionary. But in each iteration, curr_gcds is a new defaultdict. So this approach should work. But using defaultdict may have some overhead. Alternatively, we can use a regular dictionary and check for existence.

Alternatively, for each step, create a new empty dictionary for curr_gcds, process the previous GCDs, then add the current number. Then, accumulate into global_freq. That's manageable.

But how about the time? For each element, the inner loops run for O(number of GCDs in prev_gcds) steps. The number of GCDs per step is logarithmic in the maximum possible value. So, for n=1e5 and each step processing 5-20 entries, the total is 1e6 operations, which is acceptable.

Now, let's think about the GCD computation. In Python, math.gcd returns the positive GCD, but the elements can be zero? Wait, the problem states that each a_i is at least 1. So no problem. Also, note that math.gcd in Python 3 handles positive integers correctly. But we need to make sure that when a number is added, the GCD is computed correctly. For example, if the previous GCD is 6 and the current number is 3, the new GCD is 3.

Yes, that's correct.

Another point: when a new_gcd is computed, multiple previous GCDs may lead to the same new_gcd. For example, suppose prev_gcds has entries 6 (count 2) and 3 (count 3). Then, when adding a new number 3, the new_gcd would be 3 for both. So curr_gcds[3] would be 2 + 3 =5, plus 1 for the new subarray [3] (but wait, the code above adds 1 for the new subarray. Wait, no: the code adds the current number as a subarray of length 1. But when processing the previous GCDs, the code computes new_gcds and then adds the current number as a new entry. So in the example, after processing the previous GCDs, we have curr_gcds[3] = 5 (from previous GCDs). Then, adding num=3, which is done via curr_gcds[num] +=1. But wait, that's part of the same step. So, in the code:

curr_gcds is initially empty. Then, for each g in prev_gcds, compute new_g and add to curr_gcds. Then, add num to curr_gcds. So in the case where num is 3, and prev_gcds has entries that lead to new_g 3, then curr_gcds[3] is the sum of those entries. Then, adding num (3) as a new entry (subarray of length 1) would increment curr_gcds[3] by 1. So the total is the sum of the previous entries' contributions plus 1. But that's incorrect. Oh wait, no: the code as written first processes the previous GCDs, then adds the current number as a subarray of length 1. So the new_gcds from the previous GCDs are added, and then the current number is added as a new subarray. So for example, if the previous GCDs, when combined with the current num, produce a new GCD of g, and the current num itself is g, then the count for g is the sum of those contributions plus 1. But that's wrong. Because the current number's subarray (length 1) is a separate case. Wait, no. The previous step's GCDs are for subarrays ending at i-1. When you take those and combine with a[i], you get subarrays that start at some l <= i-1 and end at i. The current number's subarray is just [i], which is a separate case. So the code correctly adds that.

Wait, for example, if the previous GCDs (from i-1) are for subarrays ending at i-1. When you process the current a[i], the new GCDs are those subarrays that start at any l <= i-1 and end at i. So for each of those, the GCD is gcd(g, a[i]), where g is the GCD of the subarray from l to i-1. Then, the subarray [i] (starting and ending at i) is a separate case, which has GCD a[i]. So the code's approach is correct.

So the code for each step is:

For the current element a[i], create a new dictionary curr_gcds.

For each (g, cnt) in prev_gcds:

   new_g = gcd(g, a[i])

   curr_gcds[new_g] += cnt

Then, add a[i] to curr_gcds (count +=1).

Then, for each entry in curr_gcds, add to the global frequency.

Yes, that's correct.

So in Python, this can be implemented with dictionaries or defaultdicts.

Now, considering that in Python, using defaultdict(int) may be slightly slower than a regular dictionary, but for code simplicity, it's manageable. Alternatively, we can use regular dictionaries and check for the existence of keys. Let's see.

Another optimization: since the GCDs can be up to 1e9, but the number of possible GCDs per step is small, using a dictionary is efficient in terms of space.

Now, the code structure would be:

Read n.

Read the array a as a list of integers.

Read q, then read the queries into a list.

Process the array to compute the global frequency map.

Then, for each query x in the queries, output the corresponding value from the global frequency map, defaulting to 0 if x is not present.

So the code would look something like this:

import sys
import math
from collections import defaultdict

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
queries = [int(sys.stdin.readline()) for _ in range(q)]

global_freq = defaultdict(int)
prev_gcds = {}

for num in a:
    curr_gcds = defaultdict(int)
    # Process previous GCDs
    for g in prev_gcds:
        new_g = math.gcd(g, num)
        curr_gcds[new_g] += prev_gcds[g]
    # Add the current number as a subarray of length 1
    curr_gcds[num] += 1
    # Update global frequency
    for g, cnt in curr_gcds.items():
        global_freq[g] += cnt
    # Update prev_gcds for next iteration
    prev_gcds = curr_gcds

# Answer queries
for x in queries:
    print(global_freq.get(x, 0))

Wait, but in Python, dictionaries can't be directly assigned like prev_gcds = curr_gcds because curr_gcds is a defaultdict. But for the next iteration, prev_gcds would be a defaultdict. However, in the next iteration, when we iterate over 'prev_gcds', which is a defaultdict, but in the next loop, when we process it as for g in prev_gcds, it's okay because defaultdict's keys are the same as a regular dict's when entries are accessed. Wait, no. A defaultdict has entries for keys that are accessed and not present, but in this code, we are only processing the keys that are actually present in prev_gcds. Because, in the loop, for g in prev_gcds: ... So prev_gcds is a dictionary (either defaultdict or regular) and the loop iterates over its keys, which are only those that were added in the previous step.

Wait, but in the code above, prev_gcds is assigned to curr_gcds, which is a defaultdict. Then, in the next iteration, the loop is for g in prev_gcds: ... which iterates over all keys in prev_gcds. So even if curr_gcds is a defaultdict, the keys are only those that were added during the processing. So that's correct.

But in Python, when you assign prev_gcds = curr_gcds, you are just making a reference. So when curr_gcds is modified in the next iteration, prev_gcds would change? No, because in each iteration, curr_gcds is a new defaultdict. For example, in the first iteration, curr_gcds is a new defaultdict. Then prev_gcds is assigned to it. In the next iteration, curr_gcds is a new defaultdict again. So prev_gcds in the next iteration is the previous curr_gcds.

Wait, no. The code in each loop iteration:

prev_gcds starts as whatever it was from the previous step.

Then curr_gcds is created as a new defaultdict(int).

Then, process the prev_gcds, which is the previous step's curr_gcds.

So each step, prev_gcds is a regular dict (if curr_gcds is a regular dict). But in the code above, curr_gcds is a defaultdict. So prev_gcds will be a defaultdict. But when iterating over it (for g in prev_gcds), it's fine because the keys are the ones that were added.

So the code should work correctly.

Now, testing against the sample input.

First sample:

3
2 6 3
5 queries: 1,2,3,4,6.

Processing the array:

First element is 2.

prev_gcds is empty (first iteration).

curr_gcds is built by processing prev_gcds (nothing), then add 2. So curr_gcds is {2:1}.

global_freq[2] +=1.

prev_gcds is now {2:1}.

Second element:6.

Process prev_gcds (2:1). new_gcd(2,6) is 2. So curr_gcds[2] +=1.

Then add 6:1. So curr_gcds is {2:1, 6:1}.

global_freq adds 2 and 6 each with count 1 (so global_freq[2] is 1+1=2, 6 is 1).

Third element:3.

prev_gcds is {2:1, 6:1}.

For each g in prev_gcds:

g=2: new_gcd(2,3) is 1. curr_gcds[1] +=1.

g=6: new_gcd(6,3) is 3. curr_gcds[3] +=1.

Add 3 to curr_gcds: now 3:1.

So curr_gcds is {1:1, 3:1+1=2? Wait, no.

Wait, after processing the previous GCDs:

curr_gcds starts empty.

Processing g=2 from prev_gcds (count is 1):

new_g = gcd(2,3) = 1. curr_gcds[1] +=1.

Then processing g=6 (count 1):

new_g = gcd(6,3) =3. curr_gcds[3] +=1.

Then add 3 to curr_gcds: curr_gcds[3] +=1. So now curr_gcds[3] is 1 (from adding) plus 1 (from the previous step), so 2?

Wait, no. Let's see:

After processing the previous GCDs:

curr_gcds is:

1:1 (from g=2, count 1).

3:1 (from g=6, count 1).

Then add the current num (3) as a subarray of length 1. So curr_gcds[3] +=1. So 3 becomes 1+1=2?

No. Wait, the code does:

curr_gcds = defaultdict(int).

For each g in prev_gcds (2 and 6):

g=2: new_gcd(2,3) is 1. curr_gcds[1] += prev_gcds[g] (which is 1).

So curr_gcds[1] becomes 1.

g=6: new_gcd(6,3) is 3. curr_gcds[3] += prev_gcds[g] (1). So curr_gcds[3] is 1.

Then, add the current num (3) as a new entry: curr_gcds[3] +=1. So curr_gcds[3] becomes 1+1=2.

So curr_gcds is {1:1, 3:2}.

Then, global_freq is updated:

global_freq[1] +=1.

global_freq[3] +=2.

So after processing the third element, global_freq is:

2: 2 (from first and second elements)

6:1 (from second element)

1:1 (from third)

3:2 (from third)

Wait, but the first element's global_freq after step 1 is 2:1.

Second element's step adds 2 (from the new GCD 2 in curr_gcds) and 6 (count 1). So global_freq[2] is 1 (from first step) +1 (second step) = 2. global_freq[6] is 1.

Third step adds 1 and 3. global_freq[1] is 1, global_freq[3] is 2.

But then, the curr_gcds after third step is {1:1, 3:2}.

So when added to global_freq, global_freq[1] +=1 (total 1), global_freq[3] +=2 (total 2), and existing values like 2 and 6 are not modified here.

Wait no. The code adds all entries from curr_gcds to the global_freq in each step. So in the first step, curr_gcds is {2:1}, global_freq[2] +=1 → global_freq[2] is 1.

Second step, curr_gcds is {2:1, 6:1}. So global_freq[2] +=1 (now 2), and global_freq[6] +=1.

Third step, curr_gcds is {1:1, 3:2}. So global_freq[1] +=1, and global_freq[3] +=2.

So overall, global_freq is:

2: 2 (from steps 1 and 2)

6:1 (from step 2)

1:1 (from step3)

3:2 (from step3)

But in the first sample input, the queries are 1, 2, 3,4,6.

The answers are 1,2,2,0,1.

Wait, according to the first sample's output, query 2 returns 2. Let's see:

How many subarrays have GCD 2?

Looking at the array [2,6,3].

Possible subarrays:

[2] → GCD 2 → yes.

[2,6] → GCD 2 → yes.

[6] → GCD6.

[6,3] → GCD3.

[2,6,3] → GCD1.

[3] →3.

So the subarrays with GCD 2 are [2] and [2,6]. So count is 2. But according to the first sample's output, the query for 2 is 2. Which matches the code's calculation. Because global_freq[2] is 2.

So the code's global_freq for 2 is 2, which is correct.

But the third element's processing: when the third element is 3, the current GCDs are {1:1, 3:2}.

So during that step, the code adds 1 (count 1) and 3 (count 2) to the global frequency. So after all steps:

global_freq is:

2: 2 (from steps 1 and 2)

6:1 (from step 2)

1:1 (from step3)

3:2 (from step3)

Additionally, in step3, what about the subarrays that contribute to 3? The subarrays ending at the third element (3) are:

- [3] → GCD3 → count 1 (from adding the current num).

- [6,3] → GCD3 → count 1 (from previous GCD 6, which when combined with 3 gives 3).

So total 2 entries for 3 in curr_gcds. So during step3, the code adds 2 to the global_freq[3]. But before that, in step2, the subarray [6] contributes to 6's count.

So the code's approach seems to count all possible subarrays correctly.

But in the first sample, the query for 1 has output 1, which corresponds to the subarray [2,6,3] (GCD1). The code's global_freq[1] is 1, which is correct.

So the code works for the first sample.

Another example: the second sample input.

But the code should handle it.

Now, in terms of performance, what's the maximum possible time for this code? For n=1e5, each step processing O(log a) entries. Since each a is up to 1e9, log2(1e9) is about 30. So per step, 30 operations. So 1e5 * 30 = 3e6 operations. For q=3e5, lookups are O(1) per query. So the code should run within the time limits.

But in Python, dictionaries can be slow for very large numbers of entries. So perhaps using a regular dictionary and avoiding defaultdict could be more efficient. Let's test.

Modifying the code to use regular dictionaries:

prev_gcds = {}

for num in a:

    curr_gcds = {}

    # Process previous GCDs

    for g in list(prev_gcds.keys()):

        cnt = prev_gcds[g]

        new_g = math.gcd(g, num)

        if new_g in curr_gcds:

            curr_gcds[new_g] += cnt

        else:

            curr_gcds[new_g] = cnt

    # Add the current number as a subarray of length 1

    if num in curr_gcds:

        curr_gcds[num] +=1

    else:

        curr_gcds[num] =1

    # Update global_freq

    for g in curr_gcds:

        global_freq[g] = global_freq.get(g,0) + curr_gcds[g]

    # Set prev_gcds for next iteration

    prev_gcds = curr_gcds

This uses regular dictionaries, which may be faster. Because defaultdict's __missing__ method can add some overhead. For example, when checking for a key that's not present, a regular dict would return None, but defaultdict would create it. However, in this code, when processing prev_gcds (which is a regular dict), the for loop iterates over its keys, so no KeyError. Similarly, when adding to curr_gcds, we check if the key exists.

So using regular dictionaries may save some time. Let's see.

Another optimization: using a list to store the current GCDs as tuples (g, cnt), and then merging them. But not sure if that's better.

Another thing: the global_freq can be a defaultdict(int), which is okay. But when answering queries, if x is not present in the global_freq, output 0.

In Python, for the code as written, using the regular dict for curr_gcds may be more efficient than defaultdict, because the code explicitly checks for the keys. But the code's performance depends on how often these checks are done. For example, when adding new_g to curr_gcds, the code checks if new_g is present. But for each step, the number of checks is O(number of GCDs), which is small.

So, given that, perhaps using regular dicts is better. Let's adjust the code accordingly.

So, the code would look like:

Testing against sample input 1.

```python
import sys
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    q = int(input_stream.readline())
    queries = [int(input_stream.readline()) for _ in range(q)]

    global_freq = {}
    prev_gcds = {}

    for num in a:
        curr_gcds = {}
        # Process previous GCDs
        for g in list(prev_gcds.keys()):
            cnt = prev_gcds[g]
            new_g = math.gcd(g, num)
            if new_g in curr_gcds:
                curr_gcds[new_g] += cnt
            else:
                curr_gcds[new_g] = cnt
        # Add current number as a subarray of length 1
        if num in curr_gcds:
            curr_gcds[num] += 1
        else:
            curr_gcds[num] = 1
        # Update global frequency
        for g, cnt in curr_gcds.items():
            if g in global_freq:
                global_freq[g] += cnt
            else:
                global_freq[g] = cnt
        # Update prev_gcds
        prev_gcds = curr_gcds

    # Answer queries
    for x in queries:
        print(global_freq.get(x, 0), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
10 20 3 15 1000 60 16
10
1
2
3
4
5
6
10
20
60
1000
""",
            "output": \
"""\
14
0
2
2
2
0
2
2
1
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

</think>

```python
import sys
import math

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline())
    queries = [int(sys.stdin.readline()) for _ in range(q)]
    
    global_freq = {}
    prev_gcds = {}
    
    for num in a:
        curr_gcds = {}
        # Process previous GCDs
        for g in list(prev_gcds.keys()):
            cnt = prev_gcds[g]
            new_g = math.gcd(g, num)
            if new_g in curr_gcds:
                curr_gcds[new_g] += cnt
            else:
                curr_gcds[new_g] = cnt
        # Add current number as a subarray of length 1
        if num in curr_gcds:
            curr_gcds[num] += 1
        else:
            curr_gcds[num] = 1
        # Update global frequency
        for g, cnt in curr_gcds.items():
            if g in global_freq:
                global_freq[g] += cnt
            else:
                global_freq[g] = cnt
        prev_gcds = curr_gcds
    
    for x in queries:
        print(global_freq.get(x, 0))

if __name__ == "__main__":
    main()
```
