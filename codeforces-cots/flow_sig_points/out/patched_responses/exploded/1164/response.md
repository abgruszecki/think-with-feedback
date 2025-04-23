<think>
Okay, let's see. The problem is to find the rank of Thomas Smith, whose ID is 1. The rank is determined by the sum of his four scores compared to others. Students are sorted by their total sum in descending order, and if two have the same sum, the one with the smaller ID comes first. So, Thomas's rank depends on how many students have a higher sum than him, plus those with the same sum but lower ID (but wait, no, because when sorted in descending order, same sum students are ordered by increasing ID. So, in the list sorted first by sum (desc) then ID (asc), Thomas's position is his rank.

So the steps I need to do:

1. Read all students' data.
2. For each student, calculate the sum of their four scores.
3. Sort the students in such a way that higher sums come first. If sums are equal, the student with the smaller ID comes first.
4. Find the position of Thomas (ID 1) in this sorted list. That position +1 is his rank.

Wait, no. Wait, positions are 1-based. Like, if he's first in the sorted list, rank 1. So, after sorting, iterate through the list and find where Thomas is. The index (starting from 0) plus 1 is his rank.

So the steps are:

- Read n.
- Read n lines, each line has four integers. For each line, compute the sum, and store the id (i-th line, id is i) along with the sum.
- Create a list of tuples (sum, id) for all students. But Thomas is the first student (since the input is given in order of increasing IDs, so the first line after n is id 1, second line id 2, etc. Wait, no. The problem says: "the students are given in order of increasing of their ids." So the first line is id 1, second line id 2, etc. So the i-th line (0-based) corresponds to id i+1.

Wait, the problem says: "the next n lines contains the grades of the i-th student on... The id of the i-th student is equal to i." Wait, no. Wait the input description says: "the i-th student's grades are a_i, b_i, etc. The id is i." Wait, the problem says: "the students are given in order of increasing of their ids." So for each of the next n lines, the first line is student with id 1, then 2, etc. So for each line, the student's id is the line's position (if we start from 1). So the first line after n is student 1 (Thomas), then student 2, etc.

So, for each line, the student's id is (i+1) where i is the 0-based index of the line in the next n lines. Wait no. Wait, the problem says: "the i-th student's id is equal to i." So the first line (after n) is id 1, the second line id 2, etc. So when we read the first line after n, that's id 1.

So, for each of the n students, their id is their 1-based index in the list. So the first line (after n) is id 1 (Thomas), the second line is id 2, etc.

So, for each student, we can store their id (starting from 1) and their sum.

Then, we need to sort the students in such a way that:

- Higher sum comes first.
- If sums are equal, the student with the smaller id comes first (since in the problem statement, when two students have the same sum, they are sorted by increasing id. So in the sorted list, the one with lower id comes first. So when sorted in descending order by sum, but for same sum, ascending by id.

Wait, the problem says: "sorted by decreasing the sum of their scores. If two or more students have the same sum, these students will be sorted by increasing their ids."

So the primary key for sorting is sum (descending), then id (ascending). So the sort order is:

student A comes before student B if:

A's sum > B's sum, or

A's sum == B's sum and A's id < B's id.

So when we sort the list of students, we need to sort them in such a way.

So in Python, we can create a list of tuples for each student: (-sum, id). Then when sorted in ascending order, since Python's sort is stable. Wait, because a higher sum should come first. So for two students, if student A has sum 400 and student B has sum 398, then A comes first. So when sorted in descending order of sum, but for the same sum, ascending order of id.

But in Python, the way to do a custom sort is to use a key. So the key for each student would be (-sum, id), so that when sorted in ascending order, the students are ordered by sum (descending) and then id (ascending). Because when you sort the list of tuples, tuples are compared element-wise. For example, (-sum_a, id_a) < (-sum_b, id_b) if sum_a > sum_b (because -sum_a is smaller than -sum_b when sum_a is larger), or if sums are equal and id_a is smaller.

So sorting the list of (-sum, id) in ascending order will give the correct order.

So the steps are:

1. Read n.

2. Read n lines. For each line, split into four integers, compute sum, store sum and id.

3. For each student, create a tuple (-sum, id).

4. Sort the list of these tuples.

5. After sorting, find the index of the tuple where id is 1. That index +1 is the rank.

So, how to find the index? For example, in the first sample input:

After processing, the tuples would be:

For Thomas (sum 398, id 1): (-398, 1)

Others:

sum 400 (id 2) → (-400, 2)

sum 398 (id 3) → (-398, 3)

sum 379 (id 4) → (-379,4)

sum 357 (id5) → (-357,5)

Wait wait wait, the first sample input's students are:

Wait first line (after n=5) is Thomas's grades: 100,98,100,100 → sum 100+98=198 + 200 → 398. So sum is 398. Then the second line is 100,100,100,100 → sum 400. Third line is 100+100+99+99 → 398. Fourth line sum 90+99+90+100 = 379. Fifth line 100+98+60+99= 357.

So their tuples when stored are:

(-398, 1), (-400, 2), (-398,3), (-379,4), (-357,5).

Wait no. Wait the sum for id2 is 400, so -400. So when we sort the list of tuples, the order would be sorted in ascending order of the first element (since sorted in ascending order), then the second element.

So let's list all the tuples:

For the first sample:

[ (-398,1), (-400,2), (-398,3), (-379,4), (-357,5) ]

Wait no, wait the sum for id2 is 400, so the tuple is (-400, 2). Similarly, id3 sum 398 → (-398,3).

So when we sort the list of tuples, the order would be sorted by the first element in ascending order. But since the first element is negative sum, this is equivalent to sorting the sum in descending order.

So sorted list would be:

- The tuple with the smallest first element (i.e., the most negative) comes first. So (-400,2) is the first element. Then comes (-398,1), then (-398,3), then -379,4, then -357,5.

So the sorted list is [ (-400,2), (-398,1), (-398,3), (-379,4), (-357,5) ]

Wait wait, no. Let's see: when sorted in ascending order of the tuple (-sum, id), the tuples are compared first by the first element. So (-400,2) is less than (-398,1), because -400 < -398. So in the sorted list, (-400,2) comes first, then (-398,1), then (-398,3) (since their first elements are equal, then compare the id. 1 <3, so (-398,1) comes before (-398,3)).

So the sorted list would be ordered as:

[ (-400,2), (-398,1), (-398,3), (-379,4), (-357,5) ]

So in the sorted list, the students are ordered as 2, 1, 3,4,5.

But wait, the sum for student 2 is 400, which is higher than Thomas's 398. So Thomas is in second place. So in the sorted list, the first element is student 2 (sum 400), then Thomas (sum 398), then student 3 (sum 398). So the rank of Thomas is 2, which matches the sample output.

So when we sort the list of tuples, the index of Thomas's tuple (id 1) is index 1 (since the list is 0-based). So rank is index+1 → 2.

So the approach is correct.

So now, in code:

Read n.

Then, read n lines. For each line, compute the sum. For each student, create a tuple of (-sum, id). The id starts at 1 and increments by 1 for each line.

Wait, the first line after n is id 1, second line id 2, etc. So for each line in the n lines, the id is 1-based. So in code:

students = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    s = a + b + c + d
    students.append( (-s, i+1) )  # because i starts from 0, so i+1 is the id.

Then, sort the students list.

Then, iterate through the sorted list to find the index where the id is 1.

But how to do that efficiently?

Once sorted, we can loop through the list and check each element's id. Once found, the index is the position.

But since n can be up to 1000, this is acceptable.

Alternatively, we can collect all the (sum, id) in a list, sort them, then loop through the sorted list to find Thomas's position.

So code steps:

Read n.

Read n lines, compute sum and id for each, create a list of (-sum, id).

Sort this list.

Then, loop through the sorted list, check for each element's id. When the id is 1, the index +1 is the rank.

But how to handle this in code.

For example:

sorted_students = sorted(students)

for index in range(len(sorted_students)):
    if sorted_students[index][1] == 1:
        print(index + 1)
        exit()

But since the list is sorted, we need to find the first occurrence of id 1? Wait no. Because the list is sorted by (-sum, id). So if two students have the same sum, the one with smaller id comes first. So in the list, Thomas's tuple is (-sum, 1). So in the sorted list, the first occurrence of Thomas's sum will have his id. So the loop will find him in the correct position.

Yes.

So code in Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    students = []
    for i in range(n):
        a, b, c, d = map(int, input_stream.readline().rstrip("\n").split())
        s = a + b + c + d
        students.append( (-s, i+1) )

    students.sort()

    for idx in range(len(students)):
        if students[idx][1] == 1:
            print(idx + 1, file=output_stream)
            break



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
100 80 90 99
60 60 60 60
90 60 100 60
60 100 60 80
100 100 0 100
0 0 0 0
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

Sample 2:

Input:

6

100 80 90 99 → sum 100+80=180, 90+99=189 → 369 → id1 → (-369,1)

60 60 60 60 → sum 240 → id2 → (-240, 2)

90 60 100 60 → sum 90+60=150, 100+60=160 → 310 → id3 → (-310,3)

60 100 60 80 → 60+100=160, 60+80=140 → 300 → id4 → (-300,4)

100 100 0 100 → sum 300 → id5 → (-300,5)

0 0 0 0 → sum 0 → id6 → (0,6)

So students list before sorting:

[ (-369,1), (-240,2), (-310,3), (-300,4), (-300,5), (0,6) ]

After sorting:

The sorted list will arrange the tuples in ascending order.

First, the smallest first elements:

The first element is (-369,1) → first element is -369.

Wait, no. Wait the list after appending all students is:

[ (-369,1), (-240,2), (-310,3), (-300,4), (-300,5), (0,6) ]

Wait no, the first line after n is 6 is Thomas's line. Sum is 100+80+90+99= 369. So the tuple is (-369, 1).

Then the next lines:

Second student's sum is 60+60+60+60=240 → tuple (-240,2).

Third line: 90+60+100+60= 310 → tuple (-310,3).

Fourth line: 60+100+60+80= 300 → tuple (-300,4).

Fifth line: 100+100+0+100= 300 → tuple (-300,5).

Sixth line: 0 → tuple (0,6).

Now, when we sort the list of these tuples:

The first elements are -369, -240, -310, -300, -300, 0.

Wait, but when sorted in ascending order, the order of first elements will be from smallest to largest. So -369 is the smallest (since -369 < -310 < -300 < -240 < 0). Wait wait:

Wait -369 is less than -310 → yes, because -369 is to the left of -310 on the number line. So when sorted, the tuples are ordered based on their first elements in ascending order.

So the sorted list would be ordered as:

(-369,1), (-310,3), (-300,4), (-300,5), (-240,2), (0,6). Wait no, wait the first elements are:

-369, -310, -300, -300, -240, 0. So the sorted list of tuples is ordered as:

[-369, -310, -300, -300, -240, 0]

So the tuples are:

(-369,1), (-310,3), (-300,4), (-300,5), (-240,2), (0,6).

Wait, but when comparing the first elements, -369 is the smallest, then -310, then -300 (twice), then -240, then 0.

So the sorted list starts with (-369,1), then (-310,3), then (-300,4), (-300,5), etc.

So the id 1 is in the first position (index 0), so rank is 0+1=1. Which matches the sample.

So code works.

Now, considering possible edge cases.

Edge case 1: All students have same sum except Thomas. For example, Thomas has sum 400, others have sum 400. Then since Thomas's id is 1, he is first in the sorted list. So rank 1.

Another edge case: Thomas has sum 400, another student has sum 400. But that student's id is 0? No, no. All ids start from 1. So if Thomas and another student (id 2) have same sum. Then Thomas (id1) comes first. So the code would find Thomas at index 0.

Another edge case: Thomas is the only student. Then his rank is 1.

So the code handles all these cases.

Now, for performance, n is up to 1000. Sorting a list of 1000 elements is O(n log n), which is acceptable. Even for n=1e5, it would be okay, but n is 1e3 here. So the code is efficient.

Memory-wise, we are storing a list of tuples, each with two integers. For 1000 elements, that's negligible. So the code is efficient.

So the approach is correct. The code is straightforward.

Now, write the Python code as per the problem's instructions.

The code must read input from stdin, compute, and output the correct answer.

So the code:

Reads n, then n lines. For each line, compute the sum, store the tuple (-sum, id). Sort the list. Then iterate through the sorted list to find the index where id is 1. Output index+1.

Yes.
</think>

```python
n = int(input())
students = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    total = a + b + c + d
    students.append((-total, i + 1))
students.sort()
for idx, (_, student_id) in enumerate(students):
    if student_id == 1:
        print(idx + 1)
        break
```
