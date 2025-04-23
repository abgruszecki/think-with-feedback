<think>
Okay, so I have this programming problem to solve. Let's read through the problem carefully.

The task is to determine if six given sticks can form a bear, an elephant, or neither. The rules are:

For a bear:
- Exactly four sticks must be of the same length (legs).
- The remaining two sticks (head and body) must satisfy head < body.

For an elephant:
- Exactly four sticks must be the same length (legs).
- The remaining two sticks must be equal in length (head and body are same).

If neither condition is met, output 'Alien'.

Hmm. Also, the input is such that you can't have both possibilities. So we don't have to handle that case.

The constraints are that each stick's length is between 1 and 9. So the input is six integers.

First, I need to figure out how to check for the four legs and then the remaining two for the head and body.

Let me think about the steps.

First, count the frequencies of each length. For example, if there's a length that appears exactly four times, then that's the legs. The remaining two can be checked for the head and body.

Alternatively, maybe there's a length that appears five times. Then four of them are legs, and the remaining one plus another could be the other two. But wait, how would that work? For example, if there's a length that appears five times, then the four legs can be four of those. The fifth and the sixth (another length) would form the head and body. Or if the fifth is part of the legs, but then there's another occurrence elsewhere. Hmm.

Wait, maybe the four legs can be made from a length that appears exactly four times, or if a length appears more than four, like five or six. But then we need to check if after taking four, the remaining two meet the criteria.

Alternatively, perhaps the four legs can be made from any set of four sticks. But that's not possible. Because the legs have to be four of the same length. So the first step is to check if there exists at least four sticks of the same length. Otherwise, it's impossible.

So, the first step is to check for the presence of at least four sticks of the same length.

So, let's proceed step by step.

Step 1: Check if there are four sticks of the same length. If not, output 'Alien'.

If there are four sticks of the same length, then:

The remaining two sticks can be either (head and body). For elephant, they must be equal. For bear, they must be in increasing order.

But wait, the problem says that for the bear, the head is shorter than the body. So the two sticks must be two different lengths where one is less than the other. However, if the two remaining sticks are the same, then that can't be a bear, but could be an elephant if the legs are four of another length. But wait, no. Wait, if the four legs are of length A, then the remaining two must be checked. For example, if the remaining two are of length B and B (and B can be anything, including A), then it's an elephant. But if the four legs are made of a length that occurs five times, then the remaining two would be one of that same length plus another. Wait, maybe I need to consider all possibilities.

Wait, maybe the legs are four of a certain length. Then the remaining two are the head and body. But those two can be from any other lengths (or same as legs, but the head and body can be same or different).

Wait, the problem says that the legs must be four sticks of the same length. The other two can be anything, but for elephant, they must be same, for bear, the first (head) must be shorter than the body.

So, the steps are:

1. Check if there are four sticks of the same length. If not, output 'Alien'.

   But how to check that? Because the same length could appear 4,5,6 times. So for example, if a length appears 5 times, we can choose any four of them as legs, and then the fifth plus another as the remaining two. But the fifth might be part of the legs, but the remaining two would be fifth and the sixth.

   Wait, no. The legs are four sticks. So regardless of whether a length appears more than four times, we need to check if it's possible to have four of the same length. So the approach is:

   For each possible length in the list, check if there are at least four sticks of that length. Then, for each such possible length, see if the remaining two sticks can form the head and body for either bear or elephant.

So the algorithm would be:

- Count the frequency of each length.

- For each length l where count >=4:

   - Then, the remaining two sticks are the ones not part of the four legs. But how to get those?

   - Wait, perhaps when a length occurs 4 times, the remaining two are the other two elements.

   - If the length occurs 5 times, then after taking four, the fifth is part of the remaining two. So the remaining two would be the fifth and the sixth element (if the sixth is different), or two of the same.

   - If the length occurs 6 times, then the remaining two are two of the same, which would satisfy elephant.

But this is getting complicated. Alternatively, perhaps we can generate all possible combinations of four sticks of the same length, and then check the remaining two.

But for six sticks, the possible candidates for the four legs could be:

Case 1: exactly four sticks of length A. Then the other two can be anything.

Case 2: five sticks of length A. Then, the four legs can be four of them, leaving one A and the sixth stick (B).

Case 3: six sticks of length A. Then, four legs, leaving two A's. Which would form an elephant.

So, perhaps the approach is:

Sort the array. Then, check the possible groupings.

Wait, perhaps sorting the array would help. Let's see.

After sorting, the sticks are in non-decreasing order.

For example:

In the first sample input:

4 2 5 4 4 4 → sorted is [2,4,4,4,4,5]. The four 4's are legs, and the remaining two are 2 and 5. For bear, 2 <5 → valid.

In the second sample:

4 4 5 4 4 5 → sorted [4,4,4,4,5,5]. Four 4's as legs, remaining 5 and 5 → elephant.

Third sample: 1,2,3,4,5,6. Sorted. No four same elements → Alien.

Another example: six 5's. Sorted → five 5's. So four legs (5's), remaining two 5's → elephant.

Another example: five 3's and one 4. After sorting: [3,3,3,3,3,4]. Four legs (3's), remaining are 3 and 4. So 3 <4 → bear.

Another example: five 3's and one 2. After four 3's, remaining 3 and 2. Then sorted, the remaining two are 2 and 3 → 2 <3 → bear.

But wait, in this case, when the remaining two are 3 and 2, but after sorting the entire array, the remaining two would be 2 and 3 (sorted), so we can check if they are in order.

So the approach is to:

Sort the array. Then, check possible positions where four consecutive same numbers exist.

Wait, perhaps sorting helps in grouping the same numbers.

So after sorting, the array is in order. Then, possible scenarios for four legs:

Case 1: The first four elements are the same. Then, the remaining two are the fifth and sixth.

Case 2: The middle four (positions 1-4, but indices 0-based maybe) are same. Wait, perhaps not. For example, after sorting, the array could be [a, a, a, a, x, y], which is four a's. Or [x, a, a, a, a, y], where x and y are different.

Alternatively, maybe after sorting, the four legs could be in positions 0-3, 1-4, or 2-5. Because if there's a group of four same numbers, they would be consecutive in the sorted array.

Wait, no. For example, if there are five a's and one b. Sorted array is [a,a,a,a,a,b]. So four a's could be the first four, the middle four (indices 0-3, 1-4, etc.), but after grouping, the four a's can be taken as any four of the five. So when sorted, the four legs can be four of the a's, and the remaining two would be a and b.

But how to model that in code.

Alternative approach: after sorting, check for possible positions where four same elements exist. For example:

Check if the first four elements are the same. Then, the remaining two are elements 4 and 5.

Check if elements 1-4 (i.e., positions 1,2,3,4) are the same. Then, the remaining two are elements 0 and 5.

Check if elements 2-5 are the same. Then, the remaining two are 0 and 1.

But is that sufficient? Let's see.

For example, if there are five a's. Then, the sorted array is a,a,a,a,a,b (assuming the sixth is b). Then, the four a's can be in positions 0-3 (remaining a and b), or 1-4 (remaining a and a and b?), wait, no. Wait, in this case, the array would have five a's and one b.

So sorted array is [a,a,a,a,a,b]. So four legs can be any four a's. Then, the remaining two are a and b.

But when checking for possible positions, in the sorted array, the first four a's (indices 0-3) would have the remaining two as a (index 4) and b (index5). So the remaining two are a and b. So for bear, the head would be a, body b? No, because a is the same as the legs. So in this case, the head is a and body is b. But since a <b, that would make it a bear.

So, the code would need to check for any possible four a's (if present) and then see the remaining two.

But how to represent this in code.

Another approach: After sorting the array, for each possible way to choose four elements of the same value, collect the remaining two elements and check if they meet the bear or elephant condition.

But how to find all possible four elements.

But given that the array is sorted, perhaps the four same elements must form a contiguous block in the sorted array.

For example, if there are four same elements, after sorting, they will be consecutive. But if there are five, then there are multiple possibilities.

Wait, but if you have five a's in the array, when sorted, they will be consecutive. So the first five elements are a's, for example. So the four legs can be the first four a's, leaving the fifth a and the sixth element (which could be a or something else).

But perhaps we can check the possible four positions where the four a's are consecutive. Because in a sorted array, duplicates are consecutive.

So in code:

Sort the array.

Check the following possibilities:

1. The first four elements are the same. Then, the remaining two are elements[4] and elements[5].

2. The middle four elements (elements[1-4], i.e., indices 1,2,3,4) are the same. Then, the remaining two are elements[0] and elements[5].

3. The last four elements (indices 2,3,4,5) are the same. Then, the remaining two are elements[0] and elements[1].

Each of these checks if there's a group of four same elements. If any of these is true, then the remaining two can be checked.

But what about cases where a length appears five or six times? For example, if all six are same: then all four possibilities (like the first four, middle four, last four) are same, but the remaining two would be two same elements. So elephant.

Another example: five a's and one a. Then, all six are a's. So four legs, remaining two a's → elephant.

So this approach should handle those cases.

Once we find a group of four same elements, then the remaining two are the other two elements.

So once a group is found, extract the remaining two, and check if they satisfy bear or elephant.

If any of the groups (first four, middle four, last four) are same, then proceed to check.

If multiple groups are possible (for example, if there are five a's), then all possible groups (like first four, middle four) would be considered. But since the problem says that the input cannot form both animals, the code can process each possible group and check if any of them allows a valid animal. Once one is found, return the appropriate result.

Wait, but what if there are two possible groups leading to different animals? But the problem states that the input is such that this is not possible. So the code can process all possible groups and see if any of them can form an animal. If none can, output 'Alien'. If any of the groups can form an animal (bear or elephant), then output that.

So the code can process each possible group (if any) and check the conditions.

So, the steps for code:

Sort the array.

Check for each of the three possible four-length groups:

- group1: first four elements.

- group2: elements 1-4 (indices 1,2,3,4).

- group3: last four elements.

For each group, check if all four elements are the same.

If any group is found:

   Take the remaining two elements (the ones not in the group) and check:

   For elephant: if the remaining two are same.

   For bear: if the two are different, and the first is less than the second.

   If either condition is met, return the corresponding animal.

But wait, in the case where the group is the first four elements (a,a,a,a), and the remaining two are (a, b), then the remaining two are a and b. Then, the head and body would be a and b. For bear, a must be less than b. But if a is the same as the legs (the group is a's), then the head and body can be a and b. So in this case, if a <b → bear.

But in code, how to extract the remaining two elements?

For example, group1 is elements[0-3]. The remaining elements are 4 and 5. So elements[4] and elements[5].

Group2 is elements[1-4]. The remaining elements are 0 and 5.

Group3 is elements[2-5]. The remaining elements are 0 and 1.

So for each group, collect the two elements outside the group.

Once we have those two elements, check if they form elephant or bear.

But if any of the groups leads to a valid animal, then output the appropriate result.

Once a group is found and the remaining two meet the conditions, output the result.

But in the case where there are multiple groups (e.g., five a's), the code may check group1 (four a's, remaining a and b), then group2 (four a's, remaining a and 0-th element, which could be a as well). But in any case, the first group that allows for a valid animal is considered. However, the problem says that the input is guaranteed to not allow both animals. So even if multiple groups are possible, they would all lead to the same conclusion.

So code steps:

Sort the array.

Check group1: elements[0], elements[1], elements[2], elements[3] → are they all the same?

If yes, then the remaining elements are elements[4] and elements[5].

Check if those two are equal → elephant.

Else, check if the first is less than the second → bear.

If either condition, output accordingly.

If not, proceed to check next groups.

If any group (group1, group2, group3) has the same four elements, and the remaining two meet either elephant or bear condition, then output the result.

Else, check other groups.

If none of the groups leads to a valid animal, then output 'Alien'.

Wait, but what if a group exists (four same elements), but the remaining two do not meet the conditions? For example, group1 is four same, remaining two are same (elephant), but group2 is also four same, but remaining two are in a different order. But the problem states that the input is such that this can't happen. So the code can process all possible groups and check each one. If any group leads to a valid animal, return it. Otherwise, after checking all possible groups, return 'Alien'.

But how to check all possible groups.

Let me see:

For example, suppose the array is [a,a,a,a,a,b]. So group1 (0-3) are a's. Remaining two are a and b. Check if a ==b → no. a <b → bear.

Group2 (1-4) are a's. Remaining two are elements[0] (a) and elements[5] (b). So same as before.

So, even though multiple groups are possible, they all result in the same remaining elements and same check. So it's redundant to check all groups, but the code can proceed to check each group and return as soon as a valid case is found.

So in code, once a group is found and the remaining two elements meet the conditions, we can immediately return the result.

So code steps:

Sort the array.

For each possible group (group1, group2, group3):

   if the group has four same elements:

      get the remaining two elements.

      check if they are equal → elephant.

      else if they are in increasing order → bear.

      else → invalid.

      if either elephant or bear is possible, output the result and exit.

If none of the groups are valid, output 'Alien'.

But how to check the remaining two elements.

Wait, after getting the remaining two elements, they are not necessarily in order. For example, group2's remaining elements are elements[0] and elements[5]. Since the array is sorted, elements[0] is the smallest, elements[5] is the largest. So elements[0] <= elements[5], but when group2 is the middle four elements (indices 1-4), elements[0] could be less than elements[5], but the remaining two could be elements[0] and elements[5], which are already in order.

But since the array is sorted, the two remaining elements are in non-decreasing order. Because the original array is sorted.

Because when we take four consecutive elements (group1, group2, or group3), the remaining elements are the ones before and after the group (for group2, elements 0 and 5, which are the first and last in the sorted array. So in the sorted array, elements[0] <= elements[5], so the remaining two are already ordered. So for the bear condition, we can check if the first remaining is less than the second. If they are equal, it's elephant. If they are in order, then bear. Else, not possible.

Wait, but in the sorted array, the remaining two elements would always be in non-decreasing order. Because the entire array is sorted. So elements[0] <= elements[1] <= ... <= elements[5]. So if group is group2 (indices 1-4), then the remaining elements are elements[0] and elements[5]. elements[0] is the smallest, elements[5] the largest. So elements[0] <= elements[5]. So their order is correct. So for the bear, we need to check if elements[0] < elements[5]. If they are equal, it's elephant.

Wait, but the remaining two elements can be in any order?

No, because the entire array is sorted. So when you take a group of four elements, the remaining two are in the sorted order.

For example, if group1 is indices 0-3, then the remaining are 4 and 5, which are >= the group's elements (since the array is sorted). So elements[4] and elements[5] are in order.

If group3 is indices 2-5, the remaining two are 0 and 1, which are <= the group's elements. And they are in order.

So the remaining two elements are always in non-decreasing order. So for the bear condition, we just need to check if they are strictly increasing (x < y). If they are equal, it's elephant. If not, it's invalid.

So in code:

After getting the two remaining elements (a and b), since the array is sorted, a <= b.

If a == b → elephant.

Else, check if a < b → bear.

Else → impossible (since a <= b, the only possibility is a < b or a == b).

So the code can do:

if a == b: elephant.

else: bear.

Wait, but what if the two remaining elements are different but not in order? But no, the array is sorted. So the two remaining elements are in order.

So in code, for the remaining two elements, after group selection, since they are part of a sorted array, they are in non-decreasing order. So the only possibilities are a == b (elephant) or a <b (bear).

So in code:

If the group is found:

   rem = [the two remaining elements]

   if rem[0] == rem[1]: → elephant.

   else: → bear.

But wait, in the case where the four legs are taken, but the remaining two are the same as the legs. For example, all six elements are same. Then, the four legs, and the remaining two are same. So it's elephant.

Another example: five a's and one a. All a's. Then four legs, two a's. Elephant.

Another example: four a's and two a's. Then elephant.

So the code seems to handle that.

But let's test another case. Suppose the array is [4,4,4,4,5,5]. Then group1 is 4's. Remaining elements are 5 and5 → elephant.

Another example: [4,4,4,4,3,5]. After sorting, [3,4,4,4,4,5]. group1 is 4's. Remaining elements are 3 and5. 3 <5 → bear.

But in the group selection, the remaining elements are 3 and5, which are in order. So yes.

So the code would output bear.

So the code can proceed as follows:

Sort the array.

Check each possible group (three possibilities) for four same elements.

For each group found:

   get the remaining two elements.

   if they are equal → elephant.

   else → bear.

   then, return the answer.

If none of the groups have four same elements → output 'Alien'.

But wait, there's another scenario where the group is not four same elements, but there are five same elements. For example, the array is [a,a,a,a,a,b]. Then, group1 (0-3) is a's, group2 (1-4) is a's. So the code would check group1 first. The remaining elements are a and b. a <b → bear.

So code works.

Another case: [a,a,a,a,b,b]. Then, group1 is four a's. Remaining two are b and b → elephant.

So code returns elephant.

But what if there are four a's and two a's. Like [a,a,a,a,a,a]. Then group1 is four a's, remaining two are a and a → elephant.

So code returns elephant.

But what about when there are four a's and two different elements. For example, a,a,a,a,b,c. Then the code would check group1 (four a's), remaining two are b and c. So check if they are equal → no. So bear.

But if the two are in different order. Wait, after sorting, the array is a,a,a,a,b,c (sorted). So remaining two are b and c. So code checks if they are equal → no. So bear.

Yes.

But what if the two are in the other order? Like a,a,a,a,c,b. No, the array is sorted, so after sorting, the order would be a,a,a,a,b,c.

So code will see group1 as a's, remaining elements are b and c.

So code works.

So now, the code logic seems to handle all possible cases.

Now, let's think about possible code.

In Python:

First, read the six integers. Sort them.

Then, check the three possible groups.

For each group:

   if the first four elements are same:

       rem = [l[4], l[5]]

   elif the middle four elements (indices 1-4) are same:

       rem = [l[0], l[5]]

   elif the last four (indices 2-5) are same:

       rem = [l[0], l[1]]

Wait, but in code, how to check each group.

Wait, perhaps loop over the three possible group positions.

So in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    sticks = list(map(int, input_stream.readline().rstrip("\n").split()))
    sticks.sort()

    def check_group(sticks, start):
        # Check if four consecutive elements starting at 'start' are equal.
        # start can be 0, 1, or 2 (since groups are 0-3, 1-4, 2-5)
        # returns (is_group, remaining)
        if start + 3 >=6:
            return (False, [])
        # check if sticks[start] to sticks[start+3] are same
        val = sticks[start]
        for i in range(start, start+4):
            if sticks[i] != val:
                return (False, [])
        # group found. get remaining elements.
        # remaining elements are all elements not in the group.
        # since sorted, the group is start to start+3.
        # the remaining elements are all elements before start, and after start+3.
        # but since it's a sorted list, the group is a contiguous block.
        # For example, if group is start=0, then the remaining elements are 4,5.
        # if group is start=1, remaining are 0,5.
        # if group is start=2, remaining are 0,1.

        # collect the remaining elements.
        remaining = []
        for i in range(6):
            if i < start or i >= start +4:
                remaining.append(sticks[i])
        # since the array is sorted, the remaining elements are sorted.
        # but when group is start=1, remaining are 0,5. which are sorted.
        # So the remaining list is [sticks[0], sticks[5]] when start=1.

        return (True, remaining)

    groups_to_check = [0, 1, 2]

    found = False
    for start in groups_to_check:
        is_group, remaining = check_group(sticks, start)
        if is_group:
            # check the remaining two elements
            a, b = remaining[0], remaining[1]
            if a == b:
                print("Elephant", file=output_stream)
                found = True
                break
            else:
                # since the array is sorted, a <= b. So a < b.
                print("Bear", file=output_stream)
                found = True
                break

    if not found:
        print("Alien", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4 5 4 4 5
""",
            "output": \
"""\
Elephant
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
    sticks = list(map(int, input_stream.readline().rstrip("\n").split()))
    sticks.sort()

    def check_group(sticks, start):
        # Check if four consecutive elements starting at 'start' are equal.
        # start can be 0, 1, or 2 (since groups are 0-3, 1-4, 2-5)
        # returns (is_group, remaining)
        if start + 3 >=6:
            return (False, [])
        # check if sticks[start] to sticks[start+3] are same
        val = sticks[start]
        for i in range(start, start+4):
            if sticks[i] != val:
                return (False, [])
        # group found. get remaining elements.
        # remaining elements are all elements not in the group.
        # since sorted, the group is start to start+3.
        # the remaining elements are all elements before start, and after start+3.
        # but since it's a sorted list, the group is a contiguous block.
        # For example, if group is start=0, then the remaining elements are 4,5.
        # if group is start=1, remaining are 0,5.
        # if group is start=2, remaining are 0,1.

        # collect the remaining elements.
        remaining = []
        for i in range(6):
            if i < start or i >= start +4:
                remaining.append(sticks[i])
        # since the array is sorted, the remaining elements are sorted.
        # but when group is start=1, remaining are 0,5. which are sorted.
        # So the remaining list is [sticks[0], sticks[5]] when start=1.

        return (True, remaining)

    groups_to_check = [0, 1, 2]

    found = False
    for start in groups_to_check:
        is_group, remaining = check_group(sticks, start)
        if is_group:
            # check the remaining two elements
            a, b = remaining[0], remaining[1]
            if a == b:
                print("Elephant", file=output_stream)
                found = True
                break
            else:
                # since the array is sorted, a <= b. So a < b.
                print("Bear", file=output_stream)
                found = True
                break

    if not found:
        print("Alien", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2 3 4 5 6
""",
            "output": \
"""\
Alien
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

Sample 3:

Input:1 2 3 4 5 6 → sorted. Check all starts. No group of four. So output Alien.

Another test case: [5,5,5,5,5,5]. Sorted. Check start=0: group of four. Remaining 5 and5 → elephant.

Another test case: [5,5,5,5,6,6]. Start 0: group of four. Remaining 6 and6 → elephant.

Another test case: [5,5,5,5,6,7]. Start 0: group of four. Remaining 6 and7 → bear.

Another test case: [3,3,3,3,3,4]. Sorted → [3,3,3,3,3,4]. Check start=0: group of four (0-3). Remaining 3 and4 → 3 <4 → bear.

Another test case: [3,3,3,3,4,4]. Start=0: group of four. Remaining 4 and4 → elephant.

Another test case: [3,3,4,4,4,4]. Start=2: group of four (elements 2-5:4's). Remaining elements 3 and3. So elephant.

So code correctly outputs elephant.

So the code seems to handle all cases.

Now, code optimizations:

The code as written is O(1) because the input is fixed size. So even checking all three groups is O(1) time.

The code sorts the array, which is O(6 log6) time. Then checks three possibilities.

So code is acceptable.

But perhaps there's a way to avoid checking all three groups. For example, if all elements are the same, then the code can return elephant. But the code as written handles that.

But for the code to work, it's sufficient to proceed as written.

So the code should be correct.
</think>

```python
sticks = list(map(int, input().split()))
sticks.sort()

def check_group(start):
    if start + 3 > 5:
        return False, []
    val = sticks[start]
    for i in range(start, start + 4):
        if sticks[i] != val:
            return False, []
    remaining = []
    for i in range(6):
        if not (start <= i < start + 4):
            remaining.append(sticks[i])
    return True, remaining

for start in [0, 1, 2]:
    valid, rem = check_group(start)
    if valid:
        if rem[0] == rem[1]:
            print("Elephant")
        else:
            print("Bear")
        exit()
print("Alien")
```
