<think>
Okay, let's tackle this problem. So the problem is about selecting students from different subjects such that for each chosen subject, the number of students selected is the same. And we need to maximize the total sum of their skill levels. If all possible options result in a negative sum, we output 0.

Hmm, first, I need to understand the constraints. The maximum n is 1e5, and m is also up to 1e5. So any algorithm that is O(n^2) would be too slow. We need an efficient approach here.

Let me think about how to model this. For each subject, we can collect the list of students sorted in descending order of their skill levels. Then, for each possible k (the number of students per subject), we can calculate the sum of the top k students in each subject that has at least k students. Then, we select the subjects where taking k students gives a non-negative contribution. The total for that k is the sum of all such subject sums. The maximum over all possible k's is our answer.

Wait, right. Because for a given k, we can include any subset of subjects that have at least k students, and take exactly k top students from each. The sum of those would be the total for that k. Then, we need to check all possible k's (from 1 up to the maximum possible number of students in any subject) and find the maximum total.

So the steps would be:

1. For each subject, sort its students in descending order of r_i, and compute the prefix sums. For example, for subject s, the prefix sum array will have sum of top 1, top 2, ..., top t students, where t is the total students in that subject.

2. For each possible k, compute the sum of all prefix sums for each subject's k-th entry (if available and >=k). But we only include a subject's prefix sum for k if the sum is positive. Because including a subject where the sum for k is negative would decrease the total. So for each subject, if the prefix sum up to k is positive, we add it to the total for that k.

3. The answer is the maximum total across all possible k's and the sum for that k. If all possible sums are negative, output 0.

So how do we efficiently compute this?

First, we need to group all students by their subject. Then, for each subject, sort the list of r_i in descending order and compute the prefix sums. Then, for each possible k, we can collect the sum of all subjects' prefix sums for k, but only if that subject's prefix sum for k is non-negative.

But the problem is that k can be up to the maximum size of any subject. For example, if there's a subject with 1e5 students, then k could be up to 1e5. But checking each possible k from 1 to 1e5 and for each k, summing all the prefix sums of subjects that have at least k students and their k prefix sum is positive... that's O(m * max_k) time. But m can be 1e5 and max_k can be 1e5, which would result in 1e10 operations. That's way too slow.

So we need a smarter way.

Wait, but perhaps the maximum possible k is not 1e5. Let's see: for each subject, the maximum possible k is the number of students in that subject. But the sum of all the k's across all possible subjects is O(n). Because each student is part of a subject's list. So for each student in a subject, they are part of the prefix sums up to their position. So maybe the total possible k's across all subjects is O(n), but how to aggregate that.

Alternatively, for each subject, after computing the prefix sums, we can, for each possible k (1 to len(students)), compute the prefix sum up to k, and if it's positive, add it to a global list for that k. Then, for each k, the sum of all entries in the global list for k is a candidate. The maximum over all k's is the answer.

But how to do this efficiently.

So for each subject s, after sorting and computing the prefix sums, we iterate through each k (from 1 to the number of students in s), compute the sum up to k. If the sum is positive, we add it to a dictionary where the key is k, and the value accumulates the sum for all subjects that contribute to this k.

Once all subjects are processed, for each k in the dictionary, we have the sum of all s's prefix sums for k. Then, the maximum value in the dictionary is the answer. If the dictionary is empty, output 0.

Yes, this approach would work. Because for each subject, we process each possible k up to the number of students in it. The total number of k's across all subjects is O(n), since each student contributes to a k once. For example, a subject with t students will contribute t k's.

But processing O(n) k's is manageable because n is up to 1e5. So this should be feasible.

So the steps are:

1. Group all students by their subject. For each subject, collect all r_i's, sort them in descending order, compute prefix sums.

2. For each subject's prefix sums, iterate k from 1 to len(prefix_sums). For each k, if prefix_sum[k] is positive, add it to a global dictionary (like a frequency array) that keeps track of the sum for each k. For example, a defaultdict that for each k, accumulates the sum of all subjects' prefix_sum[k] where prefix_sum[k] is positive.

3. After processing all subjects, iterate through all keys in the dictionary. For each k, the value is the total sum if we choose k students from each subject that can contribute. The maximum among these values is the answer. If all are negative, output 0.

Yes, that's the plan.

Now, let's think about the details.

How to compute the prefix sums:

For a subject's list of students sorted in descending order, the prefix sum for k is sum of the first k elements. But if any of the first k elements is negative, including it could reduce the sum. Wait no: for example, the students are sorted in descending order. So if the next element is negative, adding it would decrease the sum. So the maximum prefix sum up to k for a subject may not be the sum of all first k. For example, if after adding some elements, the sum starts to decrease, but perhaps including those elements would be necessary for the k constraint. Wait, but the problem says that the delegation must have exactly k students per chosen subject. So even if some students have negative r_i, if the sum of the top k is positive, it's better to include them.

Wait, no. Because if a subject's sum for k is negative, then including that subject in the delegation when k is chosen would decrease the total sum. So for each subject, when considering k, we only include it if the sum of the first k students (sorted descendingly) is positive. Because adding a positive value increases the total, but adding a negative (sum) would decrease it. So the optimal choice is to include a subject for a particular k only if the sum of the top k students in that subject is non-negative.

So when building the prefix sums for a subject, for each k, if the sum is positive, add it to the global k's sum.

So for example, if a subject has prefix sums for k=1, 2, 3 as 5, 4, 3, then for k=1, sum is 5 (add to k=1), k=2 sum is 4 (add to k=2), k=3 sum is 3 (add to k=3). But if another subject has prefix sums 3, -1, then for k=1, add 3 to k=1, for k=2 sum is -1 (don't add).

Then, for each k in the global sum, the total is the sum of all the contributions from the subjects for that k. The maximum of these totals is the answer.

So the key is to precompute for each subject the prefix sums, and for each k, if the sum is positive, add to the global sum for k.

Now, how to implement this.

In Python:

We can use a dictionary, say, sums_for_k, which is a defaultdict(int). Then, for each subject:

- collect the students in that subject, sort in descending order of r_i.

- compute the prefix sums.

- for each k in 1..len(prefix_sums):

   sum_k = prefix_sum[k]

   if sum_k > 0:

       sums_for_k[k] += sum_k

Once all subjects are processed, iterate over all keys in sums_for_k and find the maximum value. If no keys (all possible sums are <=0), output 0. Else, output the maximum.

So the steps are:

Read n and m.

Create a dictionary (defaultdict(list)) to group students by their subject.

Then, for each student, add their r_i to the corresponding subject's list.

Then, for each subject in the dictionary:

   Sort the list in descending order.

   Compute the prefix sums.

   For each k from 1 to len(prefix_sums):

       sum_k = prefix_sum[k]

       if sum_k >0:

           sums_for_k[k] += sum_k

Once all subjects are processed, the maximum value in sums_for_k.values() is the answer. If that maximum is negative, output 0. Wait, but in the code, we only add sum_k if it's positive. So all entries in sums_for_k are sums of positive sum_k. So the maximum could be 0 only if there's no entries. Wait, no. Because if a subject's sum_k is positive, but after adding multiple such, the total could be positive. So the sums_for_k's values are all positive or the sum of positive terms.

Wait, no. For example, a subject's sum for k=2 is 5 (positive). Another subject's sum for k=2 is 3 (positive). So sum_for_k[2] is 8. If another subject's sum for k=2 is -2, but we don't add it, so sum_for_k[2] is 8.

Thus, all entries in sums_for_k are sums of positive contributions. So the maximum possible sum is non-negative. So if there is at least one entry in sums_for_k, the maximum will be at least 1 (if all contributions are 1, but given r_i can be as low as -1e4, but sum_k has to be positive). Wait, but sum_k can be any positive number. So if all sum_k's are positive but their total is positive. So if sums_for_k is not empty, the maximum is the maximum of those sums. So the answer is the maximum of those sums. If there are no entries, output 0.

So in code:

max_sum = max(sums_for_k.values(), default=0)

print(max_sum if max_sum >0 else 0)

But since all entries in sums_for_k are sums of positive sum_k, the max_sum will be >= the maximum individual sum_k. So if any sum in sums_for_k is positive, then max_sum is positive. Thus, if sums_for_k is non-empty, the answer is the maximum of its values. Otherwise, output 0.

So in code:

if not sums_for_k:

    print(0)

else:

    print(max(sums_for_k.values()))

But wait, what if all entries in sums_for_k are zero? Because sum_k can be zero. But according to the problem statement, if a delegation's sum is non-positive, we output 0. But the problem says, "every valid non-empty delegation has negative sum". But in our code, a sum_k is added to the global sum only if it's positive. So if sum_k is zero, it's not added. So the code would not consider that. So in that case, the sum would not be included. So if a subject's sum_k is zero, it's not considered. Because sum_k must be positive to be added.

So for example, if a subject has sum_k=0 for some k, then it's not added to the sums_for_k[k]. So if all possible sum_k's are zero, then sums_for_k is empty. So the answer is zero.

So the code correctly handles that.

Now, the next thing is to compute the prefix sums efficiently.

For example, for a subject's list sorted in descending order, the prefix sum for k=1 is the first element, k=2 is sum of first two, etc. But for each k, if the cumulative sum is positive, we add it.

But when a prefix sum becomes negative, all larger k's for that subject will also have sum less than or equal to the previous sum. Because adding another element (which could be negative) would reduce the sum. Wait, no. Because the list is sorted in descending order. So each subsequent element is <= previous ones. But if the elements are allowed to be negative, then the prefix sums can first increase, then decrease, but once they start decreasing, adding more elements may keep the sum decreasing.

Wait, for example:

Suppose a subject has students with r_i: [5, 3, -1, -2]. Sorted in descending order. The prefix sums are 5, 8, 7, 5. So for k=3, sum is 7, which is positive. For k=4, sum is 5, which is positive. So for each k, even if the next element is negative, the cumulative sum can still be positive. So even if the next element is negative, but the sum remains positive, we need to include it.

But the problem is, for a subject with a long list of students, the prefix sum may start high, then go lower but stay positive, then eventually turn negative. For example, sum up to k is 10, then 9, then 8, ... until k=10 where sum is 1, then k=11 sum is -5. In that case, for all k up to 10, sum is positive. So each of those k's (1 to 10) would contribute to the global sum_for_k.

Thus, for each subject, after sorting, we need to compute the prefix sums and check for each k whether the sum up to k is positive, and if so, add it to the global sum_for_k.

But how to compute this efficiently.

In Python, for each subject's list, sorted in descending order:

Compute the prefix sum array. Then, iterate through each possible k (from 1 to len(list)), check if the sum is positive. If yes, add to the global sum.

But for n up to 1e5, and each subject's processing being O(t) where t is the number of students in that subject, the total time is O(n) which is acceptable.

But how to compute the prefix sums efficiently.

Yes. For example:

students = sorted([r_i for s_i, r_i in ...], reverse=True)

prefix = [0]  # prefix[0] = 0, prefix[1] = students[0], etc.

current_sum = 0

for i in range(len(students)):

    current_sum += students[i]

    prefix.append(current_sum)

Then, for k in 1 to len(students):

sum_k = prefix[k]

if sum_k > 0: add to sums_for_k[k]

But this is O(t) per subject. So overall O(n) time.

Now, the problem is that for n=1e5, and m=1e5, this approach is feasible.

But in Python, using a defaultdict to collect the sums for each k might be a problem if the k's are up to 1e5. But considering that the total number of k's processed across all subjects is O(n), the defaultdict should handle that.

So the code steps:

Read n and m.

subjects = defaultdict(list)

for each of n lines:

    s_i, r_i = map(int, input().split())

    subjects[s_i-1].append(r_i)  # assuming s_i is 1-based, convert to 0-based.

sums_for_k = defaultdict(int)

for s in subjects:

    students = subjects[s]

    students.sort(reverse=True)

    current_sum = 0

    for i in range(len(students)):

        current_sum += students[i]

        k = i + 1  # since starting from 1

        if current_sum > 0:

            sums_for_k[k] += current_sum

Then, compute the maximum in sums_for_k.values(), or 0.

Yes.

Now, let's test this against the examples.

First example:

Input:

6 3

2 6 → s=1 (0-based?), no, original problem says s_i ranges from 1 to m. So in code, s_i-1 is used.

Wait, in code, the code uses s_i-1 as the key in the subjects dict. So for s_i=2, the subject index is 1.

So in the first example, the students are:

s=1 (subject 0) has one student with r=9.

s=2 (subject 1) has two students: 6 and 5 → sorted as 6,5. The prefix sums are 6 (k=1, sum 6), 11 (k=2, sum 11).

s=3 (subject 2) has three students: 6,5,1. Wait no, the input is:

The 6 lines are:

2 6 → subject 1 (0-based) → s=1.

3 6 → subject 2 (0-based) → s=2.

2 5 → subject 1.

3 5 → subject 2.

1 9 → subject 0.

3 1 → subject 2.

So subject 0 has one student (9), subject 1 has two (6,5), subject 2 has three (6,5,1, and 5,1? Wait no. Let's list all students for each subject:

Subject 1 (s=2 in input, which is s_i-1=1 in code):

students are 6 (from first line), 5 (third line). So sorted as [6,5]. prefix sums are 6 (k=1), 11 (k=2).

Subject 2 (s=3 in input, which is 2 in code):

students are 6 (second line),5 (fourth line),1 (sixth line). So sorted as [6,5,1]. Then prefix sums:

k=1:6, sum 6. k=2:6+5=11. k=3:12. So for each of these, sum is positive.

So the sums_for_k would have:

k=1: 6 (subject 1) + 6 (subject 2) +9 (subject 0) → wait no.

Wait no. Let's process each subject:

Subject 0 (s_i=1 in input, code's key 0):

students = [9]. sorted in reverse. sum for k=1 is 9>0. So sums_for_k[1] +=9.

Subject 1 (s_i=2 in input, code's key 1):

students [6,5]. sorted [6,5]. sum for k=1 is 6. sum for k=2 is 11. both positive. So sums_for_k[1] +=6, sums_for_k[2] +=11.

Subject 2 (s_i=3 in input, code's key 2):

students [6,5,1,5,1? Wait, original input:

Second line: s_i=3, r=6 → added to subject 2.

Fourth line: s_i=3, r=5 → added to subject 2.

Sixth line: s_i=3, r=1 → added to subject 2.

Wait, the first example input has 6 lines:

Line 1: 2 6 → subject 1.

Line 2: 3 6 → subject 2.

Line 3: 2 5 → subject 1.

Line 4:3 5 → subject 2.

Line 5:1 9 → subject 0.

Line 6:3 1 → subject 2.

So subject 2 has students [6,5,1,5,1? Wait no: lines 2,4,6 are:

s_i=3 (subject 2 in code):

Line 2: r=6.

Line4: r=5.

Line6: r=1.

So subject 2 has 3 students: 6,5,1.

Wait no: line 4 is s_i=3, r=5 → added to subject 2. Line6 is s_i=3, r=1 → added to subject 2.

So subject 2's list is [6,5,5,1]?

Wait no, wait:

Wait, the input has 6 lines. Let's list them:

1. 2 6 → s=2-1=1 (code's key is 1), r=6.

2. 3 6 → s=3-1=2, r=6.

3. 2 5 → s=2-1=1, r=5.

4.3 5 → s=3-1=2, r=5.

5.1 9 → s=1-1=0, r=9.

6.3 1 → s=3-1=2, r=1.

So subject 2 (code's key 2) has students with r_i 6,5,5,1? Because lines 2,4,6 are s_i=3. Wait line 2 is s_i=3 (subject 2), r=6. line4 is s_i=3, r=5. line6 is s_i=3, r=1. So three students, right? So subject 2 has three students: 6,5,1.

Wait, no. Wait, lines 2,4,6 are three entries for s_i=3. So three students: 6,5,1. So sorted in descending order: 6,5,1.

Prefix sums:

k=1:6 → sum 6>0. Add to sums_for_k[1].

k=2:6+5=11>0 → add to sums_for_k[2].

k=3:6+5+1=12 → add to sums_for_k[3].

So for each subject:

Subject 0: k=1, sum 9.

Subject 1: k=1 sum 6, k=2 sum 11.

Subject 2: k=1 sum6, k=2 sum11, k=3 sum12.

So the sums_for_k:

k=1: 9 (subject0) +6 (subject1) +6 (subject2) =21.

k=2: 11 (subject1) +11 (subject2) =22.

k=3:12 (subject2) →12.

So the maximum is 22, which matches the first example.

Yes. So the code would compute that.

Second example:

Input:

5 3

2 6 → subject 1.

3 6 → subject2.

2 5 → subject1.

3 5 → subject2.

1 11 → subject0.

So subject0 has one student (11). So k=1 sum 11.

Subject1 has two students (6,5). k=1 sum6, k=2 sum11.

Subject2 has two students (6,5). k=1 sum6, k=2 sum11.

So sums_for_k:

k=1:11+6+6=23.

k=2:11 (subject1) +11 (subject2) =22.

So maximum is 23.

Which matches the second example.

Third example:

All students have negative r_i. So for each subject, the sum for k=1 is sum of the top 1 (which is negative), so no entries in sums_for_k. So output 0.

Thus, the code works for these examples.

Now, let's think about possible edge cases.

Case where a subject has a student with r_i=0. Then the sum for k=1 is 0. Since 0 is not >0, so it's not added. So the subject is ignored for k=1.

Another case: a subject's sum for k=1 is positive, but for higher k's, the sum is lower but still positive. All those sums are added.

Another edge case: n=1. Then the subject has one student. If r_i is positive, then sum is r_i. So the maximum is r_i.

If r_i is negative, then no entries, output 0.

So the code handles that.

Now, considering the time and memory constraints.

In Python, for n=1e5, this approach is O(n) time. Because grouping by subject is O(n), sorting each subject's list is O(t log t) where t is the number of students per subject, and sum of t log t over all subjects is O(n log n), which is acceptable for n=1e5.

But in Python, for 1e5 elements, sorting is manageable.

But what if m=1e5 and each subject has one student? Then, for each subject, the list has one element. Sorting takes O(1) time per subject. So the total time is O(n) + O(m * 1), which is acceptable.

So the code is efficient.

Now, code implementation.

But how to handle the subjects in Python. Using a defaultdict(list) for subjects.

Now, code:

Read n and m.

Then read n lines, each line with s_i and r_i.

Group the students by s_i-1 (since s_i is 1-based in the input).

For each subject, sort in reverse order, compute prefix sums, and for each k, if sum is positive, add to sums_for_k.

Then, compute the maximum sum.

In Python:

But for handling large n, using sys.stdin.readline might be better. But according to the problem statement, input is read via input().

But in Python, for n=1e5, using input() in a loop is possible but may be slow. To speed up, we can read all input at once.

So in code:

Testing against sample input 1.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().split())

    subjects = defaultdict(list)

    for _ in range(n):

        s_i, r_i = map(int, input_stream.readline().split())

        subjects[s_i-1].append(r_i)

    sums_for_k = defaultdict(int)

    for s in subjects.values():

        s.sort(reverse=True)

        current_sum = 0

        for i in range(len(s)):

            current_sum += s[i]

            k = i +1

            if current_sum >0:

                sums_for_k[k] += current_sum

    if sums_for_k:

        print(max(sums_for_k.values()), file=output_stream)

    else:

        print(0, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
2 6
3 6
2 5
3 5
1 11
""",
            "output": \
"""\
23
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

Yes.

The code seems correct.

Another test case: the third example.

All r_i are negative.

Each subject's sum for any k is negative. So sums_for_k is empty. Output is 0.

Yes.

Another test case where a subject has sum for some k positive, others negative.

E.g., subject with students [5, -3]. Sorted as [5, -3].

prefix sums:

k=1:5>0 → added.

k=2:5-3=2>0 → added.

So for this subject, sums_for_k[1] +=5, sums_for_k[2] +=2.

But another subject with students [3, -5]. Sorted as [3, -5].

prefix sums:

k=1:3>0 → added.

k=2:3-5 =-2 → not added.

So for k=1, sum is 5+3=8. For k=2, sum is 2.

Maximum is 8.

Thus, code works.

Thus, the code should be correct.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    subjects = defaultdict(list)
    for _ in range(n):
        s_i, r_i = map(int, sys.stdin.readline().split())
        subjects[s_i - 1].append(r_i)
    
    sums_for_k = defaultdict(int)
    for s in subjects.values():
        s.sort(reverse=True)
        current_sum = 0
        for idx in range(len(s)):
            current_sum += s[idx]
            k = idx + 1
            if current_sum > 0:
                sums_for_k[k] += current_sum
    
    if sums_for_k:
        print(max(sums_for_k.values()))
    else:
        print(0)

if __name__ == "__main__":
    main()
```
