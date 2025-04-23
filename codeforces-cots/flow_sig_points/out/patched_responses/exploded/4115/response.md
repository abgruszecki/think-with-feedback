<think>
Okay, let's see. The problem is to determine if there are three balls with distinct sizes such that the maximum difference between any two is at most 2. Hmm. So, the three numbers need to be such that they are all within a range of 2. But also, all three must be distinct. Wait, right. So, for example, if two are same and the third is different by 1, that's not allowed because two are the same. So, all three have to be different and within a window of 2.

So first, I need to check all possible triplets in the list. But since n can be up to 50, the number of triplets is 50 choose 3, which is 19600. That's manageable even with a brute-force approach, but maybe there's a smarter way.

Alternatively, we can process the list in a way that groups numbers by their values and then check for possible triplets in consecutive groups. Let's think about the steps.

First, maybe sorting the array would help. Once sorted, consecutive numbers are in order, and we can look for three distinct numbers in a window where the maximum minus the minimum is <=2. But even after sorting, there could be duplicates. For example, if we have [1,2,2,3], then 1,2,3 is a valid triplet. Wait, but the problem states that no two friends can have the same size. So all three must be distinct. So even if there's a triplet in the sorted list where the first is x, second is x, third is x+1, that's invalid because two are the same.

So, after sorting, we can consider each possible triplet in the sorted array, check if all three are distinct, and their maximum and min differ by <=2.

But how to do this efficiently?

Another approach: first, create a sorted list of unique elements. Then, for each possible triplet in this unique list (since duplicates can't be used), check if their max - min is <=2 and they are three distinct numbers. For example, if the unique list has elements like 3,4,5, then 3,4,5 is a valid triplet. Or, 4,5,6, but since 6-4=2, yes. Wait, 4,5,6: max is 6, min 4, difference 2. So allowed.

Wait, the problem says "differ by more than 2" is not allowed. So any two of the three can't differ by more than 2. But if the three are in a sorted order a, b, c, then the maximum difference between any two is c - a. So if c - a <=2, then all pairs will have difference <=2.

So, the approach would be: in the sorted unique list, check any triplet of consecutive elements (or any triplet) where the max and min are at most 2 apart, and there are three distinct elements.

Wait, but the unique list could have elements like 3,4,5,6. Then 3,4,5 is a valid triplet (max diff 2), 4,5,6 is also valid, etc. So the key is to find three distinct elements in the sorted unique list where the largest minus smallest is <=2.

But how to generate possible triplets from the sorted unique list. For example, if the unique list is [1,2,3,4], then possible triplets are (1,2,3), (2,3,4). Both have max - min <=2. So that's two possible triplets.

So, the plan is:

1. Sort the original list, then create a list of unique elements. Because duplicates can't be part of the triplet (since all three must be distinct). But even if there are duplicates in the original list, but the unique list has three elements within a window of 2, then the triplet exists.

Wait, no. Because the original list could have multiple elements, but the unique list's elements are sorted and duplicates removed. So, for example, in the first sample input:

4
18 55 16 17

After sorting: 16,17,18,55. Unique elements are the same. So the triplet 16,17,18 is in the unique list, and 18-16=2. So that's valid. So the answer is yes.

In the second sample:

6
40 41 43 44 44 44

After sorting and unique: 40,41,43,44. Now, check triplets:

40,41,43: max - min is 3 → invalid.

41,43,44: max - min is 3 → invalid.

Other possible triplets, but any triplet would have max-min >=3, so no.

So the answer is no.

In the third sample:

Original list sorted is [1,3,4,4,5,970,971,972]. Wait no, let's look at the input:

Input is 8

5 972 3 4 1 4 970 971

So sorted list would be 1,3,4,4,5,970,971,972. Unique elements are [1,3,4,5,970,971,972]. So possible triplets here could be 3,4,5 (max-min=2), which is valid. Also, 970,971,972 (max-min=2). So yes.

So the approach is:

- Sort the list and remove duplicates (since we need three distinct sizes). So the unique list must have at least three elements. If not, return no.

- Then, iterate through each possible triplet in the unique list. For each triplet, check if the maximum and minimum in the triplet differ by at most 2. If any triplet satisfies this, return yes.

But even in the unique list, the possible triplets could be in non-consecutive positions. For example, if the unique list is [1,2,4], then the max - min is 3, which is invalid. So the triplet is invalid.

But in the unique list, how many possible triplets are there? Let's say the unique list has m elements. Then the number of triplets is m choose 3. For m up to 1000 (since the original ti is up to 1000, but after duplicates, m can be up to 1000. But n is up to 50, so the unique list can be at most 50 elements. So m is up to 50. So 50 choose 3 is 19600, which is manageable.

But even that might be optimized. Because when sorted, the unique list is in increasing order. So for a triplet to have max - min <=2, the first and third elements must be no more than 2 apart. So for each element x in the unique list, we can check if there's x and x+1 and x+2 (but they may not exist), or x and x+1 and x+ something else. Wait, perhaps the optimal way is, for each x in the unique list, check if there exists x, y, z in the list such that x <= y <= z, z - x <=2, and all three are distinct.

But another way: since the list is sorted, for each position i in the unique list, we can look up to j such that the value at j is <= value at i + 2. Then, for that window from i to j, check if there are at least 3 elements. If yes, then there exists a triplet.

For example, in the unique sorted list, for each i, find the largest j where unique_list[j] <= unique_list[i] +2. Then, the number of elements from i to j is j - i +1. If that's >=3, then there's a triplet. Because in that window, any three consecutive elements would form a valid triplet.

Wait, but even if there are three elements in the window, but they are not consecutive. Like 1,3,4. Then 1,3,4: 4-1=3>2. So that's invalid. So this approach would not work.

Hmm. So perhaps the only valid triplets are consecutive elements in the unique list. Wait, no. For example, in the unique list [3,4,5], the triplet is valid. In [3,4,5,6], the triplet 4,5,6 is valid, but also 3,4,5 is valid. So, in that case, consecutive triplets are valid. But what about a unique list like [3,4,6]. Then the triplet 3,4,6: 6-3=3>2 → invalid. So consecutive elements in the list may not form a valid triplet.

Wait, but in this example, there's no valid triplet. Because the triplet must have all elements within 2. So, the only possible way to have a valid triplet is if three elements are such that they form a consecutive sequence where the max and min differ by at most 2.

So perhaps the correct approach is to check all possible triplets in the unique list and see if any has max - min <=2.

But how?

Alternatively, after sorting and deduping, iterate through the unique list and for each possible triplet (i, j, k) where i < j < k, check if unique_list[k] - unique_list[i] <= 2. If yes, then return YES.

Because if the max and min in the triplet are within 2, then all pairs are within 2. For example, triplet (a, b, c), a <= b <= c. Then c -a <=2 implies that b -a <=2 and c -b <=2. So all pairs are within 2.

So, the problem reduces to: does the sorted unique list have a triplet of elements where the maximum is at most 2 greater than the minimum.

So the steps are:

1. Sort the original list.

2. Deduplicate to get a list of unique elements in sorted order.

3. Check all possible triplets in this list. For each triplet, if the max - min is <=2, return YES.

If after checking all triplets none are found, return NO.

This approach is O(m^3), where m is the number of unique elements. Since m can be up to 50 (since n is up to 50), 50^3 is 125,000 operations. That's acceptable even for Python, as 1e5 operations are manageable in under 2 seconds.

But perhaps there's a smarter way. Let's think. Since the list is sorted, perhaps for each i, we can check the next two elements. For example, if for any i, unique_list[i+2] - unique_list[i] <=2, then the triplet i, i+1, i+2 is a valid one. Because in a sorted list, the next two elements are the smallest possible for the third element. So if the third element is more than i+2, then any other elements after that would be even larger, so the difference would be larger. So the minimal possible max for triplet starting at i is i+2.

So for example, if the list is [1,2,3], then i=0, the third element is 3. 3-1=2, which is allowed. So the triplet is valid.

If the list is [1,3,4], then i=0, unique_list[i+2] is 4. 4-1=3>2. So invalid.

So if in any triplet of consecutive elements in the unique list, the third element minus the first is <=2, then return yes. Otherwise, check if there are any triplets that are not consecutive but still meet the condition.

Wait, no. For example, consider the list [1,2,4,5]. The triplet (2,4,5) has max 5, min 2 → difference 3. So invalid. But the triplet (1,2,5) is invalid. However, the triplet (4,5,6) would be valid if it existed. But the point is, the consecutive triplet approach may miss some valid triplets. Wait no, how?

Wait, let's take the list [1,2,3,4]. The consecutive triplets are 1,2,3 (diff 2) → valid. 2,3,4 → diff 2 → valid. So all valid triplets would be found by consecutive triplets.

But what about a list where the unique sorted list is [1,2,3,5]. Then the triplet (1,2,3) is valid. However, the triplet (2,3,5) has a diff of 3. So no. But what if the list is [1,2,4,5]. Then there are no consecutive triplets. But maybe there's a triplet (2,4,5) but their difference is 3. So no. So in this case, there's no valid triplet.

Another example: [1,3,4,5]. The consecutive triplets are 3,4,5 (diff 2 → valid). So even if the first element is 1, the triplet 3,4,5 is valid. So the consecutive triplet approach would find it.

Wait, but in the list [3,4,5], the consecutive triplet is (3,4,5). Their difference is 2, which is valid.

Another example: [1,2,3,5,6]. The triplet (1,2,3) is valid. The triplet (5,6, ...) but there's no third element. So yes.

What about the list [2,3,5,6]. No triplet here. Because the possible triplets are (2,3,5) (diff 3 → invalid), (3,5,6) → diff 3 → invalid. So no.

But if there's a triplet (3,4,5), which is consecutive in the unique list, then it's valid.

So, the conclusion is that in the sorted unique list, if there exists any three elements (not necessarily consecutive) where the max and min differ by <=2, then there exists at least one triplet of consecutive elements in the unique list that also satisfies this condition.

Wait, no. Let's see. Suppose the unique list is [1,2,4,5]. The triplet (2,4,5) has a max - min of 3, which is invalid. So the only possible triplet is (1,2,4), which is invalid. So no triplet. But if the unique list is [1,2,3,5], then the triplet (1,2,3) is valid. So consecutive elements.

Another example: [1,3,4,5]. The triplet (3,4,5) is valid. So consecutive.

So perhaps, in the sorted unique list, if there exists a triplet of elements where the max and min differ by <=2, then there must be a triplet of consecutive elements in the list where the same holds. Because the list is sorted, any triplet with elements in between would have a max and min that is >= the consecutive triplet. Wait, maybe not. Let me think. Suppose the list is [1,2,3,5]. The triplet (1,2,3) is consecutive and valid. Suppose the list is [1,3,4,5]. The triplet (3,4,5) is consecutive and valid.

Another example: list [1,2,4,5]. The triplet (2,4,5) is not consecutive. Max - min is 3, invalid. So no valid triplet.

Another example: list [1,2,5,6]. No triplet. So consecutive approach works.

So the conclusion is that if there exists a triplet in the unique list where the max - min <=2, then there exists a triplet of three consecutive elements in the unique list where the max - min <=2.

Is that true? Let's think of a case where non-consecutive elements form a valid triplet but no consecutive elements do.

Suppose the unique list is [1,3,4,5]. The triplet (3,4,5) is consecutive and valid. So yes.

Another example: list [2,3,5]. The triplet (2,3,5) has max - min =3 → invalid. So no.

Another example: list [1,3,4,6]. Triplet (3,4,6) has max - min 3 → invalid. Triplet (1,3,4) → 3 → invalid. No valid triplet.

But what if the list is [1,2,3,4]. The triplet (1,2,4) → max - min 3 → invalid. But the consecutive triplet (1,2,3) is valid. So even if some non-consecutive triplets are invalid, the consecutive ones are valid.

So the idea is that in the sorted unique list, the only possible valid triplets are those where the elements are consecutive in the list. Because if there's a triplet a, b, c (a < b < c) where c - a <=2, then there must be elements between a and c (since the list is sorted and unique). But perhaps the triplet is formed by a, b, c where they are consecutive elements. For example, if a and c are two elements apart, then the elements in between would form a consecutive triplet.

Wait, perhaps not. Let's say the unique list is [1,2,4,5]. The triplet (2,4,5) has c - a =3 → invalid. So no. So perhaps, the only possible valid triplets are consecutive triplets in the unique list.

So the optimized approach is: after sorting and deduping, check all consecutive triplets (i, i+1, i+2) in the unique list, and see if the max (which is the third element) minus the first is <=2. If any such triplet exists, return YES. Otherwise, return NO.

Because if there exists any valid triplet, there must be such a consecutive triplet. Because the list is sorted and unique. Let's see.

Suppose there exists a triplet a, b, c (a < b < c) where c - a <=2. Since the list is sorted and unique, the elements between a and c must be consecutive. So a, a+1, a+2 (if the triplet is a, a+1, a+2). Or, there could be elements like a, a+1, a+1 (but that's not allowed as they have to be unique). Wait, but the unique list has all distinct elements. So in the unique list, a, b, c are distinct and in order. So for a, b, c to have c -a <=2, then the elements must be such that a < b < c and c <= a+2. So the possible scenarios are:

Case 1: c = a+2. Then the elements could be a, a+1, a+2. These are consecutive numbers. So in the unique list, they would be consecutive elements. So the triplet is (i, i+1, i+2) in the unique list.

Case 2: c = a+1. Then the elements are a, a+1, and another element between a and a+1, which can't exist. Wait, but in the unique list, all elements are in order. So if c = a+1, then the elements must be a, a+1, and another element in between, but since the list is sorted and unique, that's not possible. So if c = a+1, then the third element must be a or a+1, which can't be. So the only possible way for three elements to have c =a+1 is if the three elements are a, a, a+1. But since the list is unique, this is not allowed.

Wait, perhaps I'm getting confused here. Let's think again.

In the unique sorted list, all elements are strictly increasing. So for three elements a, b, c (i < j < k in the list), we have a < b < c. So c - a must be >=2 (since a < b < c, and they are integers). Wait, no. If a and c are consecutive integers, like a=3, c=4, then c-a=1. So for example, triplet (3,4,5) would have c=5, a=3 → difference 2. That's allowed. Wait, 5-3 is 2, which is allowed. So the triplet (3,4,5) is valid.

But in the unique sorted list, these three elements are consecutive entries, so in the list, their indices are i, i+1, i+2.

So if there's a triplet a, b, c where c -a <=2, then the maximum possible a, b, c in the unique list must be consecutive. Because if they are not consecutive, then there's a gap between a and c. For example, if the unique list is [1,3,4,5], then the triplet (3,4,5) is consecutive and valid. But if there was a triplet (3,5, something else), then 5-3=2, but if the elements are 3,4,5, then the triplet (3,4,5) is consecutive. So in this case, the consecutive triplet is valid.

So in general, the only way to have three elements with a difference of at most 2 is that they form consecutive elements in the unique sorted list, and their values are consecutive or have a difference of 2. So the only possible valid triplets are consecutive triplets in the unique list.

Wait, let's think of a counterexample. Suppose unique list is [1,2,4,5]. The triplet (1,2,4) has max - min 3, which is invalid. The triplet (2,4,5) has max - min 3. The triplet (1,4,5) has max - min 4. So all invalid. So there's no valid triplet. Now, if the unique list is [1,2,3,5], the triplet (1,2,3) is consecutive and valid. So yes.

Another example: unique list [2,3,5,6]. The triplet (3,5,6) → max - min 3. So invalid. But if the list is [3,4,5], then triplet is valid.

So the conclusion is that if there exists a valid triplet (three distinct elements with max - min <=2), then there exists a triplet of three consecutive elements in the unique list that satisfies this condition. Therefore, we can optimize the solution by only checking consecutive triplets in the unique list.

So the steps would be:

1. Sort the original list and deduplicate to get a unique list.

2. Iterate through each possible triplet of consecutive elements (i, i+1, i+2) in the unique list. For each, check if the third element minus the first is <=2.

3. If any such triplet exists, return YES. Otherwise, return NO.

This approach reduces the number of triplets checked from O(m^3) to O(m), which is more efficient, especially for larger m.

So, let's code this.

First, read n and the list. Then sort and deduplicate.

Deduplicating can be done by converting the sorted list into a set and then back to a sorted list. Or, we can iterate through the sorted list and add elements only if they are different from the previous.

Once we have the unique list, check if its length is less than 3. If so, return NO.

Otherwise, for each i in range(len(unique_list) -2), check if unique_list[i+2] - unique_list[i] <=2. If any such i exists, return YES. Else, NO.

For example:

First sample input after deduping is [16,17,18,55]. Check i=0: 18-16=2 → yes. So return YES.

Second sample after deduping is [40,41,43,44]. Check i=0: 43-40=3>2. i=1:44-41=3>2. i=2: no. So returns NO.

Third sample after deduping is [1,3,4,5,970,971,972]. i=0: 4-1=3>2. i=1:5-3=2 → yes. So returns YES.

Another example: input [5,972,3,4,1,4,970,971]. sorted is [1,3,4,4,5,970,971,972]. deduplicated is [1,3,4,5,970,971,972]. So i=0: 4-1=3. i=1:5-3=2 → yes.

Another example: input [3,3,4,5]. Deduplicated is [3,4,5]. i=0:5-3=2 → yes.

Another example: [1,2,4,5]. Deduplicated is [1,2,4,5]. Check i=0: 4-1=3 → no. i=1:5-2=3 → no. So no.

So the code would work.

Now, let's code this.

Read n: n = int(input())

Read the list: t = list(map(int, input().split()))

Sort the list: t_sorted = sorted(t)

Deduplicate:

unique = []
prev = None
for num in t_sorted:
    if num != prev:
        unique.append(num)
        prev = num

If len(unique) <3: print("NO")

Else:

for i in range(len(unique) -2):
    if unique[i+2] - unique[i] <=2:
        print("YES")
        exit()
print("NO")

Wait, but in the case where the triplet is not consecutive in the unique list, but there are three elements where the max and min are <=2 apart. For example, if unique list is [1,2,3,4], then i=0: 3-1=2 → yes.

But if the unique list is [1,2,4,5,6], then i=0: 4-1=3 → no. i=1:5-2=3 → no. i=2:6-4=2 → yes. So triplet 4,5,6.

But the code would check i=2: unique[i+2] is 6. i is 2, i+2 is 4? Wait, len(unique) is 5. So range(len(unique)-2) is 0,1,2. For i=2, i+2 is 4, but unique has indexes 0-4.

So for i=2, unique[i] is 4, unique[i+2] is 6. 6-4=2 → yes.

So the code would correctly find this.

So the code would work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    t = list(map(int, input_stream.readline().rstrip("\n").split()))
    t_sorted = sorted(t)
    unique = []
    prev = None
    for num in t_sorted:
        if num != prev:
            unique.append(num)
            prev = num
    if len(unique) < 3:
        print("NO", file=output_stream)
    else:
        for i in range(len(unique) - 2):
            if unique[i+2] - unique[i] <= 2:
                print("YES", file=output_stream)
                return
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
40 41 43 44 44 44
""",
            "output": \
"""\
NO
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    t = list(map(int, input_stream.readline().rstrip("\n").split()))
    t_sorted = sorted(t)
    unique = []
    prev = None
    for num in t_sorted:
        if num != prev:
            unique.append(num)
            prev = num
    if len(unique) < 3:
        print("NO", file=output_stream)
    else:
        for i in range(len(unique) - 2):
            if unique[i+2] - unique[i] <= 2:
                print("YES", file=output_stream)
                return
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
5 972 3 4 1 4 970 971
""",
            "output": \
"""\
YES
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

Third sample:

8

5 972 3 4 1 4 970 971 → sorted is [1,3,4,4,5,970,971,972]. deduped is [1,3,4,5,970,971,972]. len is 7. For i in 0 to 5-2 =5. i=1: 5-3=2 → yes. So output YES.

All samples pass.

Another test case: [1,2,3,4]. unique is [1,2,3,4]. i=0: 3-1=2 → yes.

Another test case: [2,3,5,6]. unique is [2,3,5,6]. len is 4. i can be 0 and 1. i=0:5-2=3>2. i=1:6-3=3>2. So output NO.

Another test case: [3,4,5]. len is 3. i=0:5-3=2 → yes.

So the code works.

Thus, the optimal approach is to check consecutive triplets in the sorted unique list. Time complexity is O(n log n) for sorting, which is acceptable. Even for n=50, this is trivial.
</think>

```python
n = int(input())
t = list(map(int, input().split()))
t_sorted = sorted(t)
unique = []
prev = None
for num in t_sorted:
    if num != prev:
        unique.append(num)
        prev = num
if len(unique) < 3:
    print("NO")
else:
    for i in range(len(unique) - 2):
        if unique[i+2] - unique[i] <= 2:
            print("YES")
            exit()
    print("NO")
```
