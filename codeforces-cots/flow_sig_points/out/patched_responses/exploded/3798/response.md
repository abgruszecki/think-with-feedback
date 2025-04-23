<think>
Okay, so I need to solve this problem where I have to rearrange students in a queue to minimize the total dissatisfaction. Let me think about how to approach this.

First, let's understand the problem. Each student's dissatisfaction is calculated based on their position. For a student i in position j, the formula is a_i*(j-1) + b_i*(n-j). The total is the sum of all these values. We need to arrange the students in such a way that this total is minimized.

Hmm, the key here is to find the optimal order of the students. How to model the effect of each student's a_i and b_i on their optimal position? Let's try to find a way to sort the students so that when placed in that order, the total is minimized.

Let me think about each student's contribution. Let's say a student is placed at position j. Then, the contribution to the total is a_i*(j-1) + b_i*(n-j). Let's simplify this equation. 

Expanding the terms: a_i j - a_i + b_i n - b_i j. Combine like terms: (a_i - b_i) j + (b_i n - a_i). So for each student, their contribution is (a_i - b_i)*j plus a constant term (b_i n -a_i). 

Wait, but when we sum over all students, the total would be sum((a_i -b_i)*j_i) + sum(b_i n -a_i) for all i. Since the second term is a constant (doesn't depend on the order of the students, because each student is included once), the problem reduces to minimizing the sum of (a_i -b_i)*j_i, where j_i is the position of student i in the arrangement. Because the other term is fixed once the set of students is given, regardless of their order. 

Wait, is that correct? Let me check. For each student i, their contribution has a term (b_i n -a_i). Summing over all i gives sum(b_i n -a_i) = n sum(b_i) - sum(a_i). Since all students are present, this sum is fixed. So yes, the only thing that depends on the order is the sum of (a_i - b_i)*j_i. Therefore, the problem reduces to arranging the students such that the sum of (a_i -b_i)*j_i is minimized. 

So now, the problem becomes: arrange the students in some order such that when each is assigned a position j (from 1 to n), the sum of (a_i -b_i)*j_i is as small as possible. 

But how do we arrange them to minimize this sum? Let's think about two students, say student A and student B. How should they be ordered relative to each other?

Suppose we have two students, A and B. We need to decide whether A comes before B or B comes before A. Let's model the difference in the sum for these two orderings.

Case 1: A is in position j, B is in position j+1.

The contribution from A and B would be (a_A - b_A)*j + (a_B - b_B)*(j+1).

Case 2: B is in position j, A is in position j+1.

The contribution would be (a_B - b_B)*j + (a_A - b_A)*(j+1).

The difference between these two cases is:

[ (a_A - b_A)*j + (a_B - b_B)*(j+1) ] - [ (a_B - b_B)*j + (a_A - b_A)*(j+1) ]

Simplifying:

= (a_A - b_A - a_B + b_B)*j + (a_B - b_B - a_A + b_A)*(j+1 - j) ?

Wait, perhaps better to subtract the two expressions:

Case1 - Case2 = (a_A - b_A)j + (a_B -b_B)(j+1) - [ (a_B -b_B)j + (a_A -b_A)(j+1) ]

Expand terms:

= a_A j - b_A j + a_B (j+1) - b_B (j+1) - a_B j + b_B j - a_A (j+1) + b_A (j+1)

Combine like terms:

a_A j - a_A (j+1) = a_A (j - j -1) = -a_A

Similarly, -b_A j + b_A (j+1) = b_A (1)

a_B (j+1) - a_B j = a_B (1)

- b_B (j+1) + b_B j = -b_B (1)

So overall:

= (-a_A + b_A + a_B - b_B) 

So the difference is (a_B - b_B) - (a_A - b_A). 

If Case1 is better than Case2, then the difference (Case1 - Case2) should be negative, which would mean (a_B -b_B) - (a_A - b_A) < 0 → a_B -b_B < a_A - b_A → (a_A - b_A) > (a_B -b_B). 

So when (a_A -b_A) > (a_B -b_B), then swapping A and B (placing A first) gives a lower sum. Therefore, to minimize the sum, when comparing two students, the one with higher (a_i -b_i) should come first. Wait, wait. Let me rephrase.

If (a_A - b_A) > (a_B -b_B), then when we place A before B, the difference is (a_B -b_B - a_A + b_A) which is ( -(a_A -b_A) + (a_B -b_B) ) → negative, which means Case1 (A before B) is better, because the difference (Case1 - Case2) is negative → Case1 gives a smaller sum than Case2. So in this scenario, when A has a higher (a_i -b_i) than B, putting A before B is better.

Therefore, the optimal order is to sort the students in decreasing order of (a_i - b_i). Because this way, for any two adjacent students, the one with higher (a_i -b_i) comes first, which gives the minimal possible sum for their arrangement.

Wait, but how does this work when we have multiple students? The pairwise comparison leads to a global optimal arrangement. So by sorting all students in decreasing order of (a_i - b_i), the sum of (a_i -b_i)*j_i will be minimized. Because higher (a_i -b_i) will be multiplied by smaller j (since j is 1-based). Wait, j increases as you go later in the order. So if a student has a higher (a_i -b_i) value, placing them earlier (smaller j) will contribute more (since (a_i -b_i) is positive and multiplied by a smaller j, but wait, maybe (a_i -b_i) could be negative. Hmm.

Wait, for example, if (a_i -b_i) is positive, then having a smaller j (earlier position) would reduce the product (a_i -b_i)*j, since j is smaller. But if (a_i -b_i) is negative, then placing them later (larger j) would make the product less negative (i.e., larger, but since we are summing, it's worse). Wait, but the sum is the sum of all (a_i -b_i)*j_i. So for each student, we want (a_i -b_i)*j_i to be as small as possible. So if (a_i -b_i) is positive, then placing the student in as low a j as possible (earlier positions) reduces their contribution. If (a_i -b_i) is negative, then placing them in as high a j as possible (later positions) reduces their contribution (since multiplying a negative by a larger j gives a smaller value, i.e., more negative).

So, to minimize the sum, we should arrange the students in such a way that those with higher (a_i -b_i) are placed first, and those with lower (a_i -b_i) (including negative) are placed later. This way, the higher values (including positive ones) are multiplied by smaller j's, and the lower values (possibly negative) are multiplied by larger j's, thus minimizing the sum.

Therefore, the correct approach is to sort the students in descending order of (a_i - b_i). Once sorted, the first student in the list will be in position 1, the next in position 2, etc. Then, the sum can be computed by iterating through the sorted list and adding (a_i -b_i) * j, and then adding the fixed sum of (b_i *n -a_i) for all i.

Wait, but the fixed sum is sum(b_i *n -a_i), which is separate. So the total dissatisfaction is sum( (a_i -b_i)*j_i ) + sum( b_i n -a_i ). So the sum that we need to minimize is the first term, as the second is fixed.

Therefore, the algorithm is:

1. Compute for each student the value (a_i - b_i).

2. Sort the students in descending order of this value. So the student with highest (a_i -b_i) comes first.

3. Assign positions j from 1 to n in this sorted order.

4. Compute the sum of (a_i -b_i)*j for each student, then add the fixed sum (sum(b_i *n -a_i)).

This should give the minimal total dissatisfaction.

Let me test this with the first example.

Sample Input 1:

3

4 2 → a_i -b_i = 4-2=2

2 3 → 2-3= -1

6 1 →6-1=5

So sorted in descending order: 5, 2, -1 → the third student (6,1), first (4,2), then second (2,3). Wait, original students are 3,1,2 in the sorted order.

Then their positions are 1, 2, 3.

Calculating the sum (a_i -b_i)*j:

For third student (i=3, a_i=6, b_i=1): 5 * 1 =5

First student (i=1, a=4, b=2): 2 *2=4

Second student (i=2, a=2, b=3): (-1)*3 =-3

Sum of these terms:5+4-3=6.

Then the fixed sum is sum(b_i *n -a_i) → n=3.

Each term:

b_i*3 -a_i:

For student 1: 2*3 -4=6-4=2

Student 2:3*3-2=9-2=7

Student3:1*3 -6=3-6= -3

Sum is 2+7-3=6.

Total sum is 6+6=12, which matches the example. So this approach works.

Another example: let's see. If a student has a negative (a_i -b_i), like the second student in the first example, which is placed in position 3. So (a_i -b_i) is -1, multiplied by 3. The term is -3, which is better than if it were placed in a lower position. Wait, but if we placed a student with (a_i -b_i) = -1 in position 3, the product is -3, which is the same as -1 *3. If they were placed in a higher position, say position 1, the product would be -1*1 =-1, which is better (smaller). Wait, but that's the opposite of what our approach suggests.

Wait, this seems conflicting. Oh wait, maybe I made a mistake in the reasoning. Let me re-examine.

If (a_i -b_i) is negative, then (a_i -b_i)*j is minimized when j is as large as possible. Because multiplying a negative number by a larger j makes the product smaller (more negative). For example, -1 *3 =-3 is better (smaller) than -1 *1 =-1.

Wait, but in the sum, we are trying to minimize the total of all (a_i -b_i)*j_i. So for a student with (a_i -b_i) negative, placing them in a higher j (later position) gives a smaller value (more negative) which reduces the total sum. That's exactly what we want. So in the first example, the student with (a_i -b_i)=-1 is placed in position 3, which contributes (-1)*3 =-3. If they were placed in position 1, that would contribute (-1)*1 =-1, which is higher (less negative) and thus worse for the sum. So our approach is correct.

So the sorted order is correct. Students with higher (a_i -b_i) are placed first. For those with lower (a_i -b_i) (including negative), they are placed later, so their (a_i -b_i) *j is as small as possible.

Thus, the approach is to sort in descending order of (a_i -b_i). Then compute the sum of (a_i -b_i)*j for j from 1 to n. Then add the fixed sum.

Now, to implement this in Python efficiently.

The steps:

Read n.

Then read n pairs of a_i and b_i.

Compute for each student (a_i, b_i) the value (a_i -b_i), and also compute the sum of (b_i *n -a_i).

Sort the list of students in descending order of (a_i -b_i).

Then, for each student in the sorted list, multiply (a_i -b_i) by their position (1-based index) and sum all these.

Add this sum to the fixed sum to get the total.

Now, the constraints: n can be up to 1e5, so sorting is O(n log n), which is acceptable.

In Python, for 1e5 elements, sorting is manageable.

So the code would be:

Read n.

sum_fixed = 0

students = []

for _ in range(n):

    a, b = map(int, input().split())

    students.append( (a - b, a, b) )

    sum_fixed += b * n - a

Then, sort the students in descending order of (a -b).

Then, iterate through the sorted list, for each student in position j (1-based), compute (a_i -b_i) *j and accumulate the sum.

sum_var = 0

for j in range(1, n+1):

    delta, a, b = students_sorted[j-1]  # assuming 0-based list

    sum_var += delta * j

total = sum_var + sum_fixed

print(total)

Wait, but in the code, how are we storing the students? For the sorted list, we need to sort based on (a_i -b_i) in descending order. So when we append (a -b, a, b) into the students list, then sort the list in reverse order (descending) based on the first element.

So the code would be:

students.sort(reverse=True, key=lambda x: x[0])

Wait, but in Python, the list.sort() method uses the key function. So for each student in the list, which is a tuple (delta, a, b), we can just sort in reverse order of delta.

So:

students.sort(reverse=True, key=lambda x: x[0])

Wait, but since the first element of the tuple is delta, which is a_i -b_i, we can sort the list in reverse order (descending) by delta.

So:

students.sort(reverse=True, key=lambda x: x[0])

But wait, the first element is delta, so the key can be omitted, as the default for tuples is to compare the first element, then the next, etc. So if we sort the list of tuples in reverse order, that's equivalent to sorting by delta in reverse.

So:

students.sort(reverse=True)

Yes, because each element in the students list is a tuple (delta, a, b). So when you sort the list, the default comparison is based on the first element, then the second, etc. So students.sort(reverse=True) will sort the tuples in descending order of delta.

So the code becomes:

students = []

sum_fixed = 0

for _ in range(n):

    a, b = map(int, input().split())

    delta = a - b

    students.append( (delta, a, b) )

    sum_fixed += b *n - a

students.sort(reverse=True)

sum_var = 0

for idx in range(n):

    delta, a, b = students[idx]

    sum_var += delta * (idx +1)

total = sum_var + sum_fixed

print(total)

Yes. Let's test this with the first sample input.

Sample input 1:

3

4 2 → delta 2

2 3 → delta -1

6 1 → delta 5

students list becomes [(5,6,1), (2,4,2), (-1,2,3)] ?

Wait, initial order is as read. Then after sorting in reverse, the order would be (5,6,1), (2,4,2), (-1,2,3). Then, their positions are 1,2,3.

sum_var is 5*1 +2*2 + (-1)*3 =5 +4 -3=6.

sum_fixed is sum(2*3-4=2, 3*3-2=7, 1*3-6=-3 → 2+7-3=6). Total 6+6=12.

Which matches the sample.

The code seems correct.

Now, considering the constraints. For n=1e5, the code needs to read 1e5 lines. Using sys.stdin.readline could be faster. But in Python, using input() may be too slow for 1e5 lines. So, perhaps it's better to read all input at once.

But in Python, the standard way is to read via sys.stdin for speed. So, the code should read:

import sys

n = int(sys.stdin.readline())

students = []

sum_fixed =0

for _ in range(n):

    a, b = map(int, sys.stdin.readline().split())

    delta = a -b

    students.append( (delta, a, b) )

    sum_fixed += b *n -a

students.sort(reverse=True)

sum_var =0

for i in range(n):

    sum_var += students[i][0] * (i+1)

print(sum_var + sum_fixed)

This should handle the inputs efficiently.

Testing with the second sample:

Input 4:

4

2 4 → delta -2

3 3 → delta 0

7 1 → delta 6

2 3 → delta -1

sum_fixed is sum(4*4 -2=14, 3*4-3=9, 1*4-7=-3, 3*4-2=10 → 14+9-3+10=30.

After sorting the students in reverse order of delta:

The deltas are -2,0,6,-1. So the sorted deltas in reverse are 6,0,-1,-2.

So the sorted list is:

6 (from 7,1), 0 (3,3), -1 (2,3), -2 (2,4).

sum_var is 6*1 +0*2 + (-1)*3 + (-2)*4 =6 +0 -3-8= -5.

Total is -5 +30=25, which matches sample 2.

So the code works for that case.

Thus, this approach is correct.

The time complexity is O(n log n), which for n=1e5 is acceptable. The memory is O(n), which is also acceptable.

Thus, the Python code should be as written above.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    students = []
    sum_fixed = 0
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        delta = a - b
        students.append((delta, a, b))
        sum_fixed += b * n - a
    students.sort(reverse=True)
    sum_var = 0
    for i in range(n):
        sum_var += students[i][0] * (i + 1)
    print(sum_var + sum_fixed)

if __name__ == "__main__":
    main()
```