<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So, the task is to find the number of ways to choose c prisoners that form a contiguous segment, and all of them have a crime severity not exceeding t. The answer is the count of such possible contiguous segments of exactly length c where each element in the segment is <= t.

Hmm. Let's think about the constraints. The input n can be up to 2e5, which is 200,000. So any O(n^2) approach is out of the question. The solution must be linear or O(n), maybe O(n) time with some sliding window technique.

The first thing that comes to mind is to find all possible sequences of consecutive elements of length c where all elements are <= t. So the problem reduces to finding all such windows.

Let me think of how to approach this. One way is to pre-process the array and find all the positions where the crime severity is greater than t. Then, these positions act as barriers. Any valid window cannot include any of these positions. So the valid segments are the regions between these barriers where the length is at least c.

For example, if between two barriers (positions i and j) there's a run of k consecutive elements all <= t, then the number of possible windows here is (k - c + 1) provided that k >= c.

So the plan is:

1. Iterate through the list and split it into runs of consecutive elements where all are <= t. These runs are separated by elements > t.
2. For each such run, calculate how many valid windows of length c exist within it. That is, for a run of length L, the count is max(0, L - c + 1).
3. Sum all these counts across all runs.

Yes, that makes sense. So the key steps are:

- Identify all the consecutive segments where elements are <= t.
- For each such segment of length L, add (L - c + 1) if L >= c.

This approach is O(n), which should be efficient enough for n up to 2e5.

Now, how to implement this.

First, split the array into the valid runs. Let's think of a way to track the current run length. We can iterate through each element, and whenever an element is <= t, we increment the current run length. If we hit an element > t, we process the current run (if any) by calculating the possible windows and add to the total, then reset the current run to 0. At the end of the loop, we also need to process the last run if it's valid.

Wait, yes. Let's see:

Initialize a current_run_length variable to 0. Also, total_ways to 0.

For each element in the array:
    if element <= t:
        current_run_length +=1
    else:
        # current run ends here. Calculate how many windows in this run.
        if current_run_length >= c:
            total_ways += (current_run_length - c +1)
        current_run_length =0

After processing all elements, we need to check if there's a current run that hasn't been processed. Because if the array ends with elements <=t, the loop would have added to current_run_length but not processed it. So after the loop ends, we need to do:

if current_run_length >=c:
    total_ways += (current_run_length - c +1)

Yes. That way, all possible runs are considered.

For example, take the first sample input:

4 3 3

Crime severities: 2,3,1,1.

All elements are <=3 except none. So the entire array is a run of length 4.

Then, the number of ways is 4-3 +1 = 2, which matches the sample output.

Another example: second input has a single element 2, which is >1, so the run is 0. So output is 0.

Third sample input: let's see the array. The runs are where elements <=4.

Looking at the array: 2,2,0,7,3,2,2,4,9,1,4.

The elements >4 are 7 (index 3), 9 (index8), etc. So the valid runs are:

First run: 2,2,0 (length 3) then 7 is invalid. Then 3,2,2,4 (length 4). Then 9 is invalid. Then 1,4 (length 2). So:

For the first run of 3: 3-2+1 =2.

Second run of 4: 4-2+1=3.

Third run of 2: can't have c=2, so 0.

Total 2+3=5? Wait the sample output is 6. Hmm. Wait maybe I made a mistake.

Wait the third sample input is:

Crime severities: 2 2 0 7 3 2 2 4 9 1 4

Looking at each element:

Indices 0-2: 2,2,0 (all <=4). Then index3 is7 (>4). Then 3,2,2,4 (indices4-7, 4 elements). Then index8 is9 (>4). Then indices9-10:1,4 (<=4). So the runs are:

Run 1: length 3. So 3-2+1=2.

Run 2: length4. 4-2+1=3. So 3.

Run3: length2. 0.

Total is 2+3=5. But sample output is6. Wait that's a problem. What's wrong here?

Wait the sample input's output is 6. So perhaps my approach is missing something.

Wait perhaps I made a mistake in processing the third sample. Let me re-examine.

Wait the third sample input is:

n=11, t=4, c=2.

The array is:

2 2 0 7 3 2 2 4 9 1 4.

Let's list each element and whether <=4:

Yes, yes, yes, no, yes, yes, yes, yes, no, yes, yes.

So the runs are:

0-2: length 3. Then after 3 (7 is no), run starts again at 4 (element 3) to 7 (element 4 is index4, then elements 3,2,2,4 are indices4-7 (elements 3,2,2,4). That's four elements. Then 9 is no, then 1 and4 are yes (indices9 and10). So run of 2.

So runs are:

3 elements, then 4 elements, then 2 elements.

Calculating for each:

First run: 3-2+1=2.

Second run:4-2+1=3.

Third run:2-2+1=1 (if c=2, then 2-2+1=1. Wait 2 elements. So 1 way. So total is 2+3+1=6. Which matches the sample output.

Ah! So the third run is 2 elements, so 2-2+1=1. So in the previous calculation, I forgot that. So the problem in my earlier analysis was that I thought the third run was 2 elements, but for c=2, the number of ways is 1.

So my initial approach is correct, but the mistake was in the example analysis. So the approach is correct.

So the algorithm is to track each run of elements <=t, compute (run_length - c +1) if run_length >=c, and sum all these.

Yes.

Now, coding this in Python.

The steps:

Read n, t, c from input.

Read the list of crime severities as a list of integers.

Initialize current_run_length to 0, total_ways to 0.

Iterate over each crime in the list:

   if crime <=t: current_run_length +=1

   else:

       if current_run_length >0:

           add (current_run_length -c +1) to total_ways if current_run_length >=c

           reset current_run_length to 0.

After processing all elements, check if current_run_length >0, and add the same as before.

Finally, print total_ways.

Yes.

Edge cases to consider:

- All elements are <=t. Then the total is (n -c +1) if n >=c.

For example, if n=5, c=3: 5-3+1=3.

- No elements are <=t: output 0.

- Some runs are shorter than c: ignore them.

Another example: if c is 1. Then each element <=t contributes 1, but in runs, for example, a run of 5 elements (each <=t) would have 5 ways. So the code correctly handles this.

So, let's code this.

Wait, but in code, the way to process the runs is as follows. Let's see.

Sample input 3:

After processing all elements, after the loop, the code will check the last run (run of 2), which is 2 >=c (c=2), so adds (2-2+1) =1. So total becomes 2+3+1=6.

Yes.

Another test case: the first sample input. After processing all elements, the code will process the run in the loop only if the next element is >t. But since there are no elements >t, the code will process the run after the loop. So that's correct.

So the code needs to, after the loop, check if there's a current run.

So code steps:

Read n, t, c.

Then the list of crimes.

current_run = 0

total =0

for crime in crimes:

    if crime <=t:

        current_run +=1

    else:

        # process current run if possible

        if current_run >=c:

            total += (current_run - c +1)

        elif current_run >0:  # but less than c, but maybe after reset?

            # no, because current_run <c, so (current_run -c +1) would be <=0. So no need.

            # So even if current_run is positive but less than c, adding (current_run -c +1) is zero or negative. So in code, can just add (current_run -c +1) but take max with 0.

        current_run =0

# after loop, process the last run

if current_run >=c:

    total += (current_run -c +1)

Wait, but in the code above, when we encounter a crime >t, we process the current_run (only if it's >=c) and reset. But what if current_run is less than c? Then adding (current_run -c +1) would be negative. So in code, when processing the current_run in the else block, should we compute max(0, current_run -c +1) ?

Yes. Because if current_run is 5 and c is 3: 5-3+1=3. If current_run is 2 and c is3: 2-3+1=0. So adding max(0, ...) is better.

So in code:

when processing the current run (either during the loop or at the end), we compute possible = max(0, current_run - c +1)

But in code, when in the loop, when we hit a crime >t:

we add possible = max(0, current_run - c +1) to the total.

Wait no: the code is:

current_run is the length of the current run. For example, if current_run is 2, and c is3: 2-3+1=0. So adding 0, which is correct.

So the code in the else block is:

if current_run >=c:

    total += (current_run -c +1)

But that's equivalent to adding max(0, current_run -c +1). Because if current_run <c, then current_run -c +1 <=0. So adding 0.

So in code:

when processing a run (either in the loop when hit a >t, or after loop ends), calculate:

ways = max(0, current_run - c +1)

and add that to the total.

Thus, in code:

In the loop:

when we encounter a crime >t:

ways = max(0, current_run - c +1)

total += ways

current_run =0

And after loop ends, same thing.

But in code, the code in the loop's else block (when crime>t) would be:

ways = max(0, current_run - c +1)

total += ways

current_run =0

Similarly, after the loop ends, we do the same.

Wait, but in the code as written earlier, during the loop's else block, when crime>t, the code checks if current_run >=c. But this is equivalent to adding max(0, ...). Because if current_run >=c, then current_run -c +1 is positive. Otherwise, zero.

So code can be written as:

current_run =0

total =0

for crime in crimes:

    if crime <=t:

        current_run +=1

    else:

        total += max(0, current_run - c +1)

        current_run =0

# process the last run

total += max(0, current_run - c +1)

print(total)

Yes, that's a simpler way. Because whenever a run ends (either because we hit a crime>t or because we reach the end of the array), we add the possible ways for that run.

This approach handles all possible cases.

So in code, each time a run ends (because of a crime>t or end of array), calculate the max(0, run_length -c +1) and add to total.

This code would handle all runs correctly.

Let's test this with sample input 3.

The runs are 3,4,2. c=2.

3-2+1=2.

4-2+1=3.

2-2+1=1.

Total 6.

Which matches the sample.

Another sample: the second input where the crime is 2>1. So current_run is 0. So after the loop, the code adds max(0,0-1+1) which is 0. So total is 0.

Yes.

Another test case: n=5, c=3. All crimes <=t. Then run_length is5. So 5-3+1=3. So total is3.

Yes.

Another test case: run length 3, c=3. Then 3-3+1=1.

Yes.

So the code should be correct.

Now, code in Python.

Read n, t, c from input.

Then read the list.

current_run =0

total=0

for crime in list:

    if crime <=t:

        current_run +=1

    else:

        total += max(0, current_run -c +1)

        current_run =0

After loop, add the last run.

total += max(0, current_run -c +1)

print(total)

Yes.

But wait, in Python, the input is read as a list of integers. So code:

n, t, c = map(int, input().split())

crimes = list(map(int, input().split()))

current_run =0

total =0

for crime in crimes:

    if crime <= t:

        current_run +=1

    else:

        total += max(0, current_run - c +1)

        current_run =0

total += max(0, current_run - c +1)

print(total)

Yes.

Testing sample 1:

Input:

4 3 3

2 3 1 1

Processing:

current_run starts at 0.

Each element is <=3.

current_run becomes 4.

Then, after loop, add 4-3+1=2. So total is 2.

Output is 2.

Sample 2:

1 1 1

2.

In loop: crime is 2>1. So current_run is 0. So adding max(0, 0-1+1)=0. Then current_run reset to 0.

After loop, add max(0,0-1+1)=0.

Total is 0+0=0.

Sample3:

The code correctly computes 6.

So this should handle all cases.

Now, what about cases where a run is split into multiple runs, like ... elements <=t, then >t, then again <=t. The code processes each run correctly.

Another test case: n=5, t=5, c=2. Crimes are [5,5,5,5,5]. All <=5.

Run is 5. So 5-2+1=4. So output is4.

Yes.

Another case: n=3, c=2. Elements [1,2,3], t=3. Then run is 3. 3-2+1=2. Output is2.

Yes.

So the code should work.

This approach is O(n) time and O(1) space (since we're not storing the entire array in memory, but in practice, in Python, we read the array as a list, which uses O(n) space, but that's unavoidable).

But according to the problem statement, the constraints for n are up to 2e5, which is manageable in Python.

Therefore, the code is correct and efficient.
</think>

```python
n, t, c = map(int, input().split())
crimes = list(map(int, input().split()))
current_run = 0
total = 0

for crime in crimes:
    if crime <= t:
        current_run += 1
    else:
        total += max(0, current_run - c + 1)
        current_run = 0

total += max(0, current_run - c + 1)
print(total)
```