<think>
Okay, let's tackle this problem. The goal is to find the minimal number of colors needed to paint the elements according to the given rules. So, each color's elements must be divisible by the minimal element in that color. And we want to minimize the number of colors. Hmm.

Let me think about the approach. So, the key here is to group elements into colors such that for each group, all elements are divisible by the group's minimum. To minimize the number of groups, we need to maximize the size of each group. But how?

Wait, maybe we can start by sorting the elements. Because if the elements are sorted, it might be easier to assign them to groups. Because once a group has a minimum, all elements in that group must be multiples of that minimum. So, the minimal elements in the groups should be divisors of all elements in their group.

Another thought: the minimal element of a group can't have any larger divisors in the sequence. Wait, maybe not. Because if there's a smaller element, then it can't be in the same group. Wait, no. Because if a group has a minimal element m, then all elements in the group must be divisible by m. If there's an element smaller than m in the group, that would contradict m being the minimal. So, the minimal element of each group is indeed the smallest in that group.

So, the elements in a group must be multiples of the group's minimal element, which is the smallest in the group. Therefore, when we assign elements to groups, the minimal element of each group must be a divisor of all elements in the group.

So, the problem reduces to selecting a set of minimal elements (each being a divisor of their group's elements), such that every element in the original array is in exactly one group, and the number of groups is minimized.

Wait, but how do we choose these minimal elements optimally?

Let's think of the elements in sorted order. Suppose we sort the array in increasing order. Then, for each element, we can decide whether to start a new group with it as the minimal, or assign it to an existing group if possible.

But how to model this. Let's see:

If we process elements in ascending order, then for each element, it can be the minimal of a new group. Alternatively, if there's an existing group whose minimal divides the current element, then we can add it to that group. But we want to choose the group that allows the maximum possible use of existing groups, to minimize the total count.

Wait, but this is a bit tricky. Because once we assign an element to a group, that group's minimal is fixed, and any subsequent elements must be divisible by their group's minimal.

Alternatively, perhaps the optimal way is to select the largest possible minimal elements first. Because a larger minimal element would allow fewer elements to be grouped under it, but perhaps that's offset by reducing the number of groups needed elsewhere.

Wait, let's take an example. Consider the sample input 3: [7,6,5,4,3,2,2,3]. Sorted, it's [2,2,3,3,4,5,6,7]. Let's see the optimal grouping. The output is 4.

In the note, the groups are:

- 4, 2, 2 (min 2)
Wait, wait the group's minimal is 2, but 4 is part of that group. Then 6 and 3 and 3 are in another group with min 3. Then 5 and 7 in their own groups, and 6's group has min 3. Hmm.

Wait, but how to decide the minimal elements.

Another idea: The minimal elements in the groups must form a set where each is a divisor of the elements in their group, and no two elements in the group are smaller than the minimal. So, the minimal elements must be in the sorted array, and each element in the group is >= the minimal and a multiple of it.

So, perhaps the way to minimize the number of groups is to select as many elements as possible into a group with the largest possible minimal. Because a larger minimal can't cover as many elements, but perhaps allows other groups to have larger minimals as well. Wait, not sure.

Alternatively, let's think of the problem as a graph. Each element can be a possible minimal for some group. Then, the problem is to select a set of elements (as minimals) such that every other element is a multiple of exactly one of these minimals, and the set is as small as possible.

But how do we find such a set?

This sounds like a problem where we need to find the minimal number of divisors that cover all elements, such that each element is covered by exactly one of these divisors, and the divisor is the minimal in its group. Wait, but the minimal in the group has to be the smallest element in the group. So, the divisors selected as minimal must not have any element smaller than them in the array, unless that element is part of a different group.

Wait, but the array is sorted. Let's say we process elements in sorted order. For each element, if it's not already covered by a previous group's minimal, then we have to create a new group with it as the minimal. Because otherwise, if we skip it and don't assign it to a group, then later when a larger element comes, we can't have a group that includes this element and the larger element (since the minimal would have to be this element, which is smaller than the larger element). But perhaps that's the right approach.

So here's an algorithm idea:

1. Sort the array in ascending order.

2. Iterate through each element in the sorted array. For each element, if it hasn't been assigned to a group yet, create a new group with it as the minimal. Then, mark all multiples of this element (that are present in the array and haven't been assigned yet) as part of this group.

Wait, but this might not work. Because, for example, if the array is [2,4,8], then the first element is 2. Assign it as minimal, and all multiples (4 and 8) are added to its group. So one group. Which is correct.

Another example: [2,3,4,5,6]. Sorted, [2,3,4,5,6]. The first element is 2. Assign 2 as minimal, then 4 and 6 are multiples. So group 1: 2,4,6. Remaining elements:3,5. Then next element is 3. Assign as minimal, and check if 6 is present (already assigned). So group 2:3. Then 5 is next. Assign as group 3. So total 3 groups. Which is correct.

Wait, but what if the array is [6,2,3,4,12] as in the first example? Sorted: [2,3,4,6,12]. The algorithm would process 2 first. Assign 2 and 4,6,12. Then 3 is next, not assigned. Assign to a new group. So groups are 2 (elements 2,4,6,12) and 3 (element 3). But wait, according to the example, the answer was 2, but this approach would give 2 as well. Wait, but in the example the answer is 2. So maybe this approach works.

Wait, the first example's input is [6,2,3,4,12]. Sorted is [2,3,4,6,12]. So the algorithm would process 2 first. Assign all elements that are multiples of 2 and not yet assigned. So 2,4,6,12 are assigned. Then, the next element is 3, which is unassigned. Create a new group. Assign 3, but 6 and 12 are already in group 1, which is correct. Then the group count is 2. Which matches the example. So this approach works here.

Another test case from the third example input: sorted array is [2,2,3,3,4,5,6,7]. Let's see. Process 2 first. Assign all multiples of 2 that are unassigned. So 2,2,4,6. Then next unassigned is 3. Assign multiples of 3. So 3,3,6 (but 6 is already assigned). So the group for 3 is 3,3. Then next is 4 (already assigned). Next is 5. Assign 5. Then 6 is assigned. Then 7. Assign 7. So total groups would be 2 (from 2), 3 (from 3), 5,7. That's 4 groups. Which matches the example. So this approach works here.

So the algorithm seems to work. The steps are:

Sort the array in ascending order. Then, for each element in order, if it hasn't been used as a group's minimal yet (i.e., not assigned to any group), create a new group with it as the minimal. Then, assign all elements in the array that are multiples of this minimal (and not yet assigned) to this group.

This way, each minimal is the smallest possible for the group, and we cover all elements. The number of groups created this way would be the minimal possible.

Because when we process the elements in order, and whenever we find an element that hasn't been assigned, we create a group with it as the minimal. Then, all elements that are multiples of this minimal (and not yet assigned) are grouped under it. This ensures that each group's minimal is as small as possible, allowing larger elements to be covered by their divisors.

So the steps are:

1. Sort the array in ascending order.

2. Initialize a visited array (or a set) to track which elements have been assigned to a group.

3. Iterate through each element in the sorted array:

   a. If the element is not marked as visited:

      i. Increment the color count.

      ii. Mark all elements in the array (from current position onwards) that are multiples of this element as visited.

This approach should work. Let's see how this can be implemented.

For example, for the input [2,2,3,3,4,5,6,7], sorted:

Indices 0:2, 1:2, 2:3, 3:3, 4:4, 5:5, 6:6, 7:7.

Processing index 0 (2, not visited):

Color count becomes 1.

Mark all multiples of 2 (2, 2, 4, 6) as visited.

Next, index 1 (2 is visited), index 2 (3 not visited):

Color count becomes 2.

Mark multiples of 3 (3,3,6 (already visited), 6? Wait, in the array, 3 is at index 2 and 3. So after processing 3, the elements 3 and 3 are marked. 6 is already in the previous group.

So color count is now 2. Then index 4 (4 is visited), index 5 (5 not visited):

Color count becomes 3.

Mark 5. Then index 6 (6 is visited), index 7 (7 not visited):

Color count becomes 4.

So total 4, which is correct.

So the algorithm works here.

Now, how to implement this.

In Python:

We can proceed as follows:

- Sort the array.

- Create a list of booleans to track visited elements.

- Initialize color count to 0.

- Iterate through each element in the sorted array. For each element:

   - If not visited:

      - Increment color count.

      - For all elements from current index onwards, check if they are multiples of current element. If yes and not visited, mark them as visited.

But how to handle duplicates. For example, multiple elements with the same value. If an element is unvisited, and we mark all multiples, including the same value elements, as visited.

Yes. Because when the current element is 2, and there are other 2's, those are also multiples of 2. So they will be marked as visited.

But in code, when the array is sorted, and we process elements in order, once a group is formed with the minimal element, all elements that are multiples of it (including itself) are marked.

So the code steps:

n = int(input())

a = list(map(int, input().split()))

a_sorted = sorted(a)

visited = [False] * n

count = 0

for i in range(n):

    if not visited[i]:

        count +=1

        # Mark all multiples of a_sorted[i] from i to end as visited

        current = a_sorted[i]

        for j in range(i, n):

            if a_sorted[j] % current == 0 and not visited[j]:

                visited[j] = True

return count

Wait, but in the sample input 6:

Input:
6
10 2 3 5 4 2

Sorted is [2,2,3,4,5,10]

Processing the first 2 (index 0):

current is 2. Mark all multiples of 2 in the array. The elements are 2,2,3,4,5,10.

So check each element from index 0:

j=0: 2%2==0 → mark.

j=1: 2%2==0 → mark.

j=2:3%2 !=0 → no.

j=3:4%2 ==0 → mark.

j=4:5%2 !=0 → no.

j=5:10%2==0 → mark.

So after this step, elements 0,1,3,5 are marked.

Next, index 1 is already marked.

Index 2 (3, not marked):

count becomes 2. Now mark all multiples of 3 from index 2 onwards.

Check elements:

j=2:3 → 3%3=0 → mark.

j=3:4 →4%3=1 → no.

j=4:5 → no.

j=5:10 →10%3=1 → no.

So only j=2 is marked.

Now, index 3 is marked. Index 4 (5, not marked):

count becomes 3. Mark multiples of 5:

j=4:5 → yes. Mark.

j=5:10 → yes. Mark.

So now, all elements are marked. Total count is 3, which matches the sample output.

So this code works for that case.

Another sample input:

4

100 100 100 100 → sorted [100,100,100,100]

Processing index 0: current is 100. All elements are multiples. Mark all. Count is 1. Correct.

Third sample:

Input is [7,6,5,4,3,2,2,3] sorted to [2,2,3,3,4,5,6,7]

Processing index 0 (2):

Mark multiples of 2. Which are 2,2,4,6. So indexes 0,1,4,6.

Count becomes 1.

Next, index 2 (3, unmarked):

Mark multiples of 3. Those are 3,3,6. 6 is index 6 (already marked). So indexes 2,3.

Count becomes 2.

Next index 4 (4, marked).

Index 5 (5, unmarked):

Count becomes 3. Mark 5 and 10 (but 10 is not there). So only 5 is marked.

Index 6 (marked).

Index7 (7, unmarked):

Count becomes 4. Mark 7.

So total 4, correct.

So this algorithm works for the samples.

Therefore, the optimal approach is to sort the array, then greedily assign groups starting from the smallest elements, marking all their multiples. This will ensure that each group uses the minimal possible number of colors.

Now, implementing this in Python.

The code needs to read n, then the list, sort it, then track visited elements.

In Python, the code would look like this:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    a.sort()
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            current = a[i]
            for j in range(i, n):
                if a[j] % current == 0:
                    visited[j] = True
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
100 100 100 100
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

Yes, the code works.

Another sample:

Third sample input:

8

7 6 5 4 3 2 2 3 → sorted [2,2,3,3,4,5,6,7]

Processing i=0 (2). Mark j where a[j] is multiple of 2. These are 2, 2,4,6 → indices 0,1,4,6.

count becomes 1.

i=1 is marked. i=2 (3 not marked). count becomes 2. Mark 3,3,6 (but 6 is index 6, which is already marked). So j=2 (3) → mark. j=3 (3) → mark. j=4 (4) is already marked. j=5 (5 → 5%3=2 → no. j=6 → 6%3=0 → but 6 is already marked. j=7 →7%3=1 → no. So after processing i=2, j=2 and 3 are marked.

count is 2.

Then i=3 is marked.

i=4 is marked.

i=5 (5, not marked). count becomes 3. Mark 5 and 10 (if any). j=5 (5) → mark. j=6 (6 is marked). j=7 (7 →7%5=2 → no. So only j=5 is marked.

i=6 is marked.

i=7 (7 not marked). count becomes 4. Mark 7. So total 4.

Thus, code works.

So the code is correct. The time complexity is O(n^2), which for n up to 100 is acceptable. The algorithm is optimal here, as for each element, in the worst case, we check all elements after it, leading to O(n^2) operations. But with n=100, this is 10^4 operations, which is very manageable.

The space is O(n) for the visited array, which is acceptable.

Therefore, this approach is correct and efficient.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
visited = [False] * n
count = 0
for i in range(n):
    if not visited[i]:
        count += 1
        current = a[i]
        for j in range(i, n):
            if a[j] % current == 0:
                visited[j] = True
print(count)
```
