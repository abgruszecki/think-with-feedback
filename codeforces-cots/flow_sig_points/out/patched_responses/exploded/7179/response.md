<think>
Okay, let's tackle this problem. So the task is to determine the winner of a photo contest based on likes. The winner is the photo with the most likes, and if there's a tie, the one that reached that maximum count first. 

Hmm, the input is a list of photo IDs representing the order of likes. For each photo, I need to track both the total number of likes and the earliest time (or step) when they reached their maximum count. Because if two photos have the same total likes, we look at when each achieved their final count. Wait, no. Wait, the problem says: if multiple photos have the most likes, the winner is the one that got this maximum number first. Wait, example 1: two photos have two likes each. The first photo (id 1) got its second like at position 5, and the second photo (id 2) got its second like at position 4. So the winner is 2 because it reached two likes earlier. So the key is, for each photo, we need to track the time when it reached its final count (the last occurrence?), no. Wait, no. Because the maximum count for each photo is their total. So for each photo, when did they reach their maximum count (i.e., the last like that contributed to their total). Because the total is fixed. So the idea is: the photo with the highest count. If there's a tie, the photo that achieved their maximum count earliest. 

Wait, the problem statement says: the winner is the photo that got the maximum number of likes first. So if two photos have the same maximum count, the one that first reached that count (in the order of likes) is the winner. 

For example, suppose photo A gets likes at steps 1,3,5 (total 3), and photo B at steps 2,4,6 (also 3). Then photo A reached 3 likes at step5, B at step6. So A is the winner because their maximum count was achieved first (earlier step). 

So the plan is:

1. For each photo, track two things: the total number of likes (count), and the last step (position) when a like was added to it. Because the last step is when it achieved its final count. So for example, a photo with count 3, last step is step5. So when comparing two photos with the same count, the one with the earliest last step (smallest step number) is the winner.

Wait, no. Let's see. The problem says that in case of a tie in the total likes, the photo that reached the maximum first (the earliest) is the winner. So the maximum for each photo is their count. For example, if two photos have counts 3 and 3. For each, when did they reach that count? For photo X, the last like was at step 5. For Y, at step 6. So X's count was achieved earlier (step5) than Y's (step6), so X is the winner. So the correct approach is to track for each photo, the count and the last step when a like was added. Then, among the photos with maximum count, we choose the one with the smallest last step. Because their maximum was achieved earlier. Wait, no. Because the last step is when their count was incremented to the maximum. So the photo whose last step is earliest, meaning they reached their maximum earlier. Because once they reach the maximum count, all subsequent likes for others might not affect their own maximum. 

So the steps are:

- Iterate through each like in the input list, tracking for each photo ID:

   a. The count of likes (increment each time it's encountered)

   b. The last occurrence (position) where it was liked.

- Then, find the maximum count among all photos.

- Among all photos with that count, select the one with the earliest last occurrence. Wait, no, wait. Wait, for a photo, the last occurrence is the step when it received its last like (thereby achieving its final count). So among the photos with maximum count, the one that achieved their final count earliest (smallest last occurrence index) is the winner. Because in the example where two photos have counts 2, but one achieved it at step4 and another at step5, the first one (step4) is the winner.

So the steps are:

1. For each photo ID, compute count and last occurrence index (starting from 1 to n).

2. Find the maximum count.

3. Among all photos with that count, find the one with the smallest last occurrence index.

4. Output that photo's ID.

Wait, but in example 1:

Input is 1,3,2,2,1. The counts are:

1: 2 (last occurrence at step5)

3: 1 (step2)

2: 2 (step4)

The maximum count is 2. The two photos (1 and 2) have counts 2. The last occurrence of photo1 is step5, photo2 is step4. So photo2 has the earlier last occurrence, so it's the winner. Which matches the example.

Yes. So that approach works.

So how to implement this.

In Python, we can use a dictionary to track for each photo ID, its count and last occurrence.

We can loop through the list of likes, keeping track of the index (starting from 1 to n). For each ai in the list:

- For ai, increment its count (starting from 0 to +1 each occurrence)

- Update the last occurrence to the current index.

So after processing all elements, for each photo, we have (count, last_occurrence).

Then, among all the entries, find the one with the highest count. If multiple, choose the one with the smallest last_occurrence.

So the steps:

Read n.

Read the list a.

Initialize a dictionary, say, photo_info, where keys are the photo IDs, and values are tuples (count, last_occurrence).

Loop through each index i (from 0 to n-1) and value in a:

   current_photo = a[i]

   index is i+1 (since likes are 1-based for the step)

   if current_photo not in photo_info:

       photo_info[current_photo] = (1, index)

   else:

       photo_info[current_photo] = (photo_info[current_photo][0] + 1, index)

Once this is done, process the photo_info to find the winner.

We need to find the photo with maximum count. Among those, the one with the smallest last_occurrence.

So, first, find the maximum count.

max_count = max(v[0] for v in photo_info.values())

Then, collect all photos that have this count.

candidates = [ (id, info[1]) for id, info in photo_info.items() if info[0] == max_count ]

Then, among these candidates, select the one with the smallest last_occurrence. The ID of that candidate is the answer.

If there are multiple candidates with same smallest last_occurrence, which one do we pick? But since the last_occurrence is unique for each photo (as per how the problem is structured?), but in any case, among them, the first occurrence (smallest ID?) No, the problem statement says that if two photos have the same maximum count and their last_occurrence is the same (which can't happen, since each like is processed in order, so two different photos can't have the same last_occurrence). Wait, because each like is added to one photo. So for two different photos, their last_occurrence could be the same only if the same index is processed. But the index is unique. So each photo's last_occurrence is unique. So the candidates will have distinct last_occurrence values. So among the candidates, the one with the smallest last_occurrence is the answer.

So the code steps.

Now, considering the constraints:

n can be up to 1000. So even O(n) is acceptable. So the approach is efficient enough.

So for Python code:

Read n.

Then read the second line as a list of integers.

Initialize a dictionary.

Loop through each element in the list, track count and last_occurrence.

Then compute the max count, then the candidates, then find the candidate with the smallest last_occurrence, then output the ID.

Possible optimizations: Since n is small (1000), even using a list of tuples would work, but a dictionary is more efficient for lookups.

Edge Cases:

- All likes are to the same photo. Then it's the winner.

- All likes are to different photos. Then each has count 1. The one that was liked first (since all have same count, and the last_occurrence is their position. So the earliest last_occurrence is the first photo in the list, which is the first occurrence. For example, input 3: 1 2 3. Then counts are 1 each. Last_occurrence for 1 is 1, 2 is 2, 3 is3. So the earliest is 1. So output 1.

Another example:

Input is 9:

100, 200, 300, 200, 100, 300, 300, 100, 200

The counts are:

100: appears at indices 1,5,8? Wait, let's index from 0 to 8 (Python list is 0-based). Wait, the code uses i+1 as the step. So for the input list [100, 200, 300, 200, 100, 300, 300, 100, 200], the indexes (i) are 0 to 8. So steps (i+1) are 1 to 9.

Processing each:

100: count becomes 3. Last_occurrence is step8 (i=7) +1? Wait, let's see:

Wait, for each element in the list, index i runs from 0 to n-1. The step is i+1.

So the first element (i=0) is step1.

Yes.

In the example, the steps for each like:

Indices (0-based):

0:100 → step1

1:200 → step2

2:300 → step3

3:200 → step4 (count for 200 is now 2, last_occurrence 4)

4:100 → step5 (count for 100 is 2, last_occurrence 5)

5:300 → step6 (count for 300 is 2, last_occurrence6)

6:300 → step7 (count3, last_occurrence7)

7:100 → step8 (count3, last_occurrence8)

8:200 → step9 (count3 for 200, last_occurrence9)

So counts:

100:3 (steps1,5,8 → step8 is last)

200:3 (steps2,4,9 → step9)

300:3 (steps3,6,7 → step7)

So the candidates are all three with count3. Their last_occurrences are 8,9,7. So the smallest last_occurrence is 7 (300). So output is 300, which matches the sample.

So the approach works.

Now, code in Python.

Read n.

Then read the list as a = list(map(int, input().split())).

Initialize photo_info as a dict.

Loop over each index and value in a.

Then process.

Then compute max_count.

Then collect candidates.

Then select the candidate with min last_occurrence.

In code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    photo_info = {}
    for idx, photo in enumerate(a):
        step = idx + 1
        if photo in photo_info:
            count, last = photo_info[photo]
            count +=1
            photo_info[photo] = (count, step)
        else:
            photo_info[photo] = (1, step)
    max_count = max(v[0] for v in photo_info.values())
    candidates = []
    for pid, (cnt, last) in photo_info.items():
        if cnt == max_count:
            candidates.append( (last, pid) )
    # The candidate with the smallest last occurrence (smallest 'last'), so min in the first element.
    candidates.sort()
    print(candidates[0][1], file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9
100 200 300 200 100 300 300 100 200
""",
            "output": \
"""\
300
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

Another case: two photos with same counts and same last step? Not possible. Because each step is a like to a photo. So two different photos can't have the same last step.

So code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
photo_info = {}
for idx, photo in enumerate(a):
    step = idx + 1
    if photo in photo_info:
        count, last = photo_info[photo]
        photo_info[photo] = (count + 1, step)
    else:
        photo_info[photo] = (1, step)
max_count = max(v[0] for v in photo_info.values())
candidates = []
for pid, info in photo_info.items():
    cnt, last = info
    if cnt == max_count:
        candidates.append((last, pid))
candidates.sort()
print(candidates[0][1])
```
