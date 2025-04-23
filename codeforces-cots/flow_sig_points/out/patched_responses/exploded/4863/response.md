<think>
Okay, let's see. We need to find the minimum possible cost of a subsequence of size k. The cost is the minimum between the maximum of the elements at odd positions and the maximum at even positions in the subsequence. Hmm.

First, let's understand what the cost represents. For a given subsequence s of length k, we split the elements into two groups: those at odd indices (1,3,5...) and even indices (2,4,6...). The maximum of each group is taken, and the cost is the smaller of these two maxima.

Our goal is to choose a subsequence such that this cost is as small as possible. So, we need to minimize the minimum of the two maxima. But how?

Wait, the minimum of two values is as small as possible when at least one of the two values is small. So, we want either the maximum of the odd positions or the maximum of the even positions to be as small as possible. But since we take the minimum of the two, the overall cost is determined by whichever of the two is smaller. So, the optimal solution would have one of the maxima being as small as possible, and the other can be larger, but the cost is the smaller one.

Hmm. So maybe the problem can be approached by trying to find a value x such that there exists a subsequence where either the maximum of the odd positions is <=x, or the maximum of the even positions is <=x. Then, the minimal x for which this is possible would be our answer. This sounds like a binary search problem.

Yes! Binary search on the possible values of x. For each candidate x, check if there exists a subsequence of length k such that either the maximum of the odd positions in the subsequence is <=x, or the maximum of the even positions is <=x. Then, the minimal x where either condition holds would be the answer.

So, the steps would be:

1. Binary search on x (the possible values of the answer).
2. For each x, check if it's possible to select a subsequence of length k where either the odd positions' max is <=x, or the even's is <=x.
3. The minimal x for which this is possible is the answer.

But how do we check these conditions efficiently?

Let's think about each condition separately. For each x, we need to check two possibilities:

A) There exists a subsequence of length k where all elements in odd positions are <=x, and the maximum of these is <=x. The even positions can have elements larger than x, but their maximum would be considered. Wait, no. Wait, the problem says the cost is the minimum between the two maxima. So, for the cost to be <=x, either the maximum of the odd positions is <=x (so the cost is min(odd_max, even_max) <=x) OR the maximum of the even positions is <=x (so same logic). So, if either of the two maxima is <=x, the cost will be <=x. Therefore, the binary search condition is: can we form a subsequence where either the odd positions' max is <=x OR the even positions' max is <=x. Then, the minimal x for which either of these is possible is our answer.

Wait, no. Because the cost is the minimum of the two maxima. So, the cost can be at most the minimum of the two. So, to have the cost <=x, we need that either the odd maximum is <=x, or the even maximum is <=x. Because if both are larger than x, then the minimum would be larger than x. So, the minimal x where either condition holds is the answer. Because that x would be the minimal possible cost. So yes, the binary search approach is feasible.

So, the plan is to binary search on x. For each x, check if there's a way to choose a k-length subsequence where either the max of the odd positions is <=x, or the max of the even positions is <=x. The minimal x where this is possible is the answer.

So, how to check each condition?

For the first condition (check if there exists a subsequence where the odd positions are all <=x, and the subsequence length is k):

In the subsequence s, the elements at positions 1,3,5... must be <=x. The elements at even positions can be anything, but when we take the max of the even positions, it's possible that the cost is determined by the even positions. But for the binary search condition, we just need that either the max of the odd positions is <=x OR the max of the even positions is <=x. So, in the check for x, we can split the problem into two separate checks: can we form a subsequence of length k where the maximum in the odd indices is <=x, or can we form one where the maximum in the even indices is <=x. If either is possible, then x is a candidate.

So, for each x in the binary search, we need to check both possibilities.

Wait, but how do these checks work?

Let's first think about the first case: can we form a subsequence where the odd positions are all <=x. Let's model how to select such a subsequence.

The subsequence s is built by selecting elements from a in order. The first element (position 1) must be <=x. The third element (position 3) must be <=x. Similarly, the fifth, etc. The even positions can be any elements (could be >x). The goal is to select a subsequence of length k where all elements in the odd positions (1,3,5...) are <=x.

Similarly for the second case: can we form a subsequence where even positions are all <=x. Then, the elements in even indices (2,4,6...) must be <=x, and the odd positions can be anything.

So, for each of these two scenarios, we can model the selection process and check if it's possible to get a subsequence of length k.

So, the approach is as follows:

For a given x:

Check for case 1: possible to select a subsequence of length k where elements in odd positions are <=x.

Check for case 2: possible to select a subsequence of length k where elements in even positions are <=x.

If either case is possible, then x is a candidate, and we can try to find a smaller x. Otherwise, we need to increase x.

Now, the question is how to efficiently check these two cases.

Let's think about case 1: selecting a subsequence where the elements in the odd positions are <=x.

The subsequence s will have elements s_1, s_2, s_3, ..., s_k.

s_1 must be <=x.

s_3 must be <=x.

s_5 must be <=x.

And so on. The even positions (s_2, s_4, etc.) can be any elements from a, as long as they are in order.

We need to find a way to model the selection of such a subsequence.

So, for case 1, the algorithm to check if it's possible is as follows:

We need to select elements from the array, in order, such that every element in an odd position of the subsequence is <=x. We need to select exactly k elements.

Let's model this as a greedy selection process.

The first element must be <=x. Then, the second element can be any (but needs to come after the first in the array). The third element must be <=x (and come after the second), and so on.

The idea is to greedily pick elements that satisfy the constraints for their positions, as early as possible to allow more elements for the rest.

So, for case 1:

We can iterate through the array and track the positions in the subsequence. Let's have a variable pos that starts at 1 (the position in the subsequence we are trying to fill). For each element in a:

- If pos is odd: we can take this element only if it's <=x. If we take it, pos increments by 1.

- If pos is even: we can take this element regardless of its value. Taking it increments pos by 1.

We need to collect as many elements as possible, following this rule, and see if we can reach pos = k+1 (meaning we have selected k elements).

But how to model this optimally?

Alternatively, we can model the process as follows:

We need to select some elements for the subsequence. The positions in the subsequence are 1-based. For each position in the subsequence, if it's odd, the element must be <=x. Even positions can be any.

We can model this as a state machine where for each step in the array, we track the current position in the subsequence. The key is to find the maximum possible length of the subsequence we can form under these constraints.

So, here's an approach:

Initialize count = 0 (number of elements selected so far).

for element in a:

    if count is even (since positions are 1-based, count+1 is the next position):

        then the next position is count+1, which is odd.

        So, to select this element for position count+1, it must be <=x.

        If it is, we select it, count +=1.

    else:

        the next position is even, so we can select it regardless.

        count +=1.

But wait, perhaps this is not optimal. Because in some cases, selecting an element even when the position is even might not be the best choice. For example, if skipping a current element allows us to take more elements later. But given that the array is processed in order, and we need the subsequence to be in the same order as the array, the greedy approach of taking elements as soon as possible might be optimal.

Wait, let's think. For case 1, when the position is even, we can take any element, so taking it as early as possible allows us to proceed to the next position, which may require a <=x element. So, the greedy approach would be to take elements for even positions as soon as possible, but for odd positions, we can only take elements <=x.

But to maximize the subsequence length, the optimal way is to greedily take elements when possible.

For example:

Suppose we have a sequence like x is 3, and the array is [5,1,5,2]. For case 1:

Positions 1 (odd) must be <=3. So first, look for elements <=3. The first element is 5 which is >3, so can't take. Next is 1 (<=3) so take it. Now count is 1 (pos 1 filled). Next, pos 2 (even): take the next element (5) as it's allowed. Now count is 2. Then pos 3 (odd): next element is 5 >3. Can't take. Next element is 2 (<=3). Take it. Now count is 3. So total of 3 elements. So if k is 3, this is possible.

Thus, the greedy approach of taking elements when possible gives the correct count.

So for case 1, the algorithm is:

Initialize count = 0.

for element in a:

    if count is even (so next position is count+1, which is odd):

        if element <=x:

            count +=1

    else:

        count +=1

    if count >=k:

        return True

So, this would process the array, greedily taking elements for even positions and taking elements <=x for odd positions.

Similarly for case 2, where even positions must be <=x. So the positions 2,4,6... must be <=x, and the others can be anything.

The algorithm for case 2 is similar but with the conditions flipped for even positions:

Initialize count = 0.

for element in a:

    if count %2 ==1 (since count+1 is even):

        if element <=x:

            count +=1

    else:

        count +=1

    if count >=k:

        return True

Wait, let's see. For case 2, even positions must be <=x. So, when building the subsequence:

pos 1: can be any.

pos 2: must be <=x.

pos 3: can be any.

pos 4: must be <=x.

etc.

So, when the current count is even (since count starts at 0), the next position is count+1 = 1 (odd, no constraint). Then, when count is 1 (next position is 2, even), we need to select an element <=x.

So, in the algorithm for case 2:

for each element in a:

    if count is odd (since next pos is count+1, which is even):

        if element <=x:

            count +=1

    else:

        count +=1

    if count >=k: return True

So, the code for case 2 is:

count =0

for num in a:

    if count %2 ==1: # next pos is even (count+1 is even when count is odd)

        if num <=x:

            count +=1

    else:

        count +=1

    if count >=k:

        break

return count >=k

So, for each x, we can check both case1 and case2. If either returns True, then x is possible.

Thus, the binary search approach works as follows:

- The minimal possible answer is the minimal x where either case1 or case2 is possible.

Now, what's the range for binary search?

The possible x can be between the minimal element in the array and the maximum element, but perhaps even lower than that. Wait, no. Because the elements in the subsequence are from the array. So, the minimal possible x is the minimal element in the array (if there's a subsequence where all odd or even positions are covered by elements <= that min). But maybe not. Wait, for example, if the array is [5,1], k=2. Then, the subsequence is [5,1]. The cost is min(5,1) =1, which is the minimal possible. So x can be 1.

So, the binary search can start from low=min(a) to high=max(a). But perhaps we can start lower? Well, the answer can't be lower than the minimal possible value in the array. Because the elements in the subsequence are elements from the array. So, the minimal x possible is the minimal element in the array. Because if you can select a subsequence where the even or odd positions are all <= some x, then x must be at least the minimal element of the subsequence's even or odd positions. So, the answer can't be lower than the minimal element in the array.

Wait, but for example, if the array is [3,1,2], and k=3. The subsequence is [3,1,2]. The odd positions are 3 and 2. Their max is 3. Even position is 1. The cost is min(3,1)=1. So x can be 1, which is present in the array.

So, the minimal x is the minimal element in the array. Wait, but in the first example of the problem:

Input:

4 2

1 2 3 4

Output is 1.

Which is the minimal element.

Another example: in the second test case (n=4, k=3), the output is 2, which is present in the array.

So, the answer is indeed the minimal x in the array such that either case1 or case2 holds.

Thus, the binary search can be done on the sorted elements of the array, but perhaps it's easier to collect all possible candidates (sorted) and then binary search through them. But for efficiency, perhaps we can collect the elements and sort them, then binary search through that sorted list. But given the constraints (n=2e5), sorting is acceptable.

Wait, but binary search can be done even if the elements are not sorted. The standard binary search approach for finding the minimal x in a range [low, high] that satisfies a certain condition.

So, here's the plan:

- Find the minimal x such that either case1 or case2 is possible.

- Binary search between low = min(a) and high = max(a).

For each mid value, check if either case1 or case2 is possible. If yes, set high=mid. Else, set low=mid+1.

Wait, but the elements could have duplicates, and the answer could be an element not in the array. Wait no. Because x is the maximum of a subset of elements in the array (for case1: the max of the odd elements in the subsequence must be <=x. So, since the elements in the subsequence's odd positions are elements from the array, their maximum can't be lower than the minimal element. So, x can be any value, but the minimal possible x is the minimal possible maximum of the odd or even positions in a valid subsequence.

Wait, but the answer is the cost, which is the minimum between two maxima, each of which is the maximum of elements in the array. So, the answer must be equal to one of the elements in the array. Because the maximum of a subset of elements is an element in the subset, which is part of the array. So the cost is the minimum of two such maxima. Therefore, the answer is the minimum of two elements from the array. But in some cases, it's possible that the answer is not present in the array. Wait, for example: suppose the array is [3, 5, 1, 4], k=3. The subsequence could be [3,5,1]. The odd positions' max is 3 and 1: max is 3. Even position is 5. Cost is min(3,5)=3. But if there's another subsequence like [5,1,4]. The odd positions are 5 and 4 (max 5), even is 1. Cost is min(5,1) =1. So, the answer is 1, which is present in the array. Hmm. So perhaps the answer must be one of the elements in the array.

Wait, let's think: the cost is min(max_odd, max_even). Both max_odd and max_even are maxima of elements in the array. So, each is an element of the array. The cost is the minimum of two such elements. Therefore, the answer must be an element of the array. Because it's the minimum of two elements, each of which is in the array. So, the answer is an element of the array. Therefore, the binary search can be done on the sorted unique elements of the array. This would reduce the number of steps in the binary search.

Alternatively, even if not, binary searching between the minimal and maximal values would work, and for each mid, we can check the conditions.

So, the steps are:

1. Sort the unique elements in the array, and perform binary search on this sorted list. Or, binary search in the full range from min(a) to max(a). Since the answer is in the array, the binary search can find the minimal x.

Now, the code outline:

Read n and k.

Read array a.

Compute the initial low and high as the minimal and maximal elements in a.

Initialize answer to high.

While low <= high:

    mid = (low + high) // 2

    check if case1 or case2 is possible with x=mid.

    if possible:

        answer = mid

        high = mid -1

    else:

        low = mid +1

At the end, output the answer.

Now, the critical part is implementing the check for case1 and case2 efficiently.

Each check for case1 and case2 is O(n), which for n=2e5 and log2(1e9) steps (about 30) would be 2*2e5*30 = 1.2e7 operations, which is acceptable for the time constraints (Python can handle 1e8 operations per second, but this is way below that).

But let's confirm. For each binary search step, we perform two O(n) checks. So, for 30 steps, 30 * 2 * 2e5 = 12e6 operations. Python can handle that within 2 seconds.

Yes, because 1e8 operations take about a second. So 12e6 is manageable.

Now, coding the check functions.

For case1: subsequence can be formed where all elements in odd positions are <=x.

The code for case1 is:

def check_case1(x):

    count = 0

    for num in a:

        if count %2 ==0:  # next position is odd (count is even)

            if num <=x:

                count +=1

        else:  # even position, can take any

            count +=1

        if count >=k:

            return True

    return count >=k

Similarly, case2:

def check_case2(x):

    count =0

    for num in a:

        if count %2 ==1:  # next position is even (count is odd)

            if num <=x:

                count +=1

        else:  # can take any

            count +=1

        if count >=k:

            return True

    return count >=k

Then, for a given x, if either check_case1 or check_case2 returns True, then x is a possible candidate.

So, combining all this, the code would:

Read n and k.

Read a.

Compute the low and high as min(a) and max(a).

Initialize answer to high.

While low <=high:

    mid = (low + high)//2

    if check_case1(mid) or check_case2(mid):

        answer = mid

        high = mid -1

    else:

        low = mid +1

Output answer.

But wait, in the first example:

Input:

4 2

1 2 3 4

The minimal x is 1. Let's see how the binary search works.

The min(a) is 1, max(a) is4.

Mid is (1+4)//2=2.

Check if any case holds for x=2.

Case1: check if we can form a subsequence where odd positions are <=2.

Processing the array:

count starts at 0.

First element is 1 <=2: count becomes 1.

Next position is even (count=1): take 2 (any). count becomes 2. Now count >=k=2. So case1 returns True. So x=2 is possible. So we set high=mid-1=1.

Now, low=1, high=1.

Mid is 1.

Check case1: can we take two elements.

Processing:

count=0, next is odd. Take 1. count=1. Next is even, take 2 (or any). count=2. So case1 returns True. So x=1 is possible. Set high=0. Loop ends. Answer is 1.

Which matches the first example.

Another example: second input:

4 3

1 2 3 4.

The answer is 2.

min(a)=1, max=4.

Binary search steps:

low=1, high=4.

mid=2.5 (but since we are using integer division, mid= (1+4)//2=2.

Check x=2.

Case1: check for case1.

We need to form a subsequence of 3 elements where the odd positions (1 and 3) are <=2.

Let's process the array:

elements are 1,2,3,4.

count starts at 0.

First element is 1<=2: count becomes 1.

Next is even: take 2. count=2.

Next position is odd (count=2, next is 3). 3>2: can't take. Next element is 4>2: can't take. So total count is 2 <3. So case1 is False.

Case2: check if even positions are <=2. So even positions (2 and 4 in a 3-length subsequence? Wait, the length is 3. The even positions are 2. So in a 3-length subsequence, even positions are 2.

So case2 requires that the even positions (position 2) is <=2.

So, for case2:

Processing the array.

count starts at 0.

position 1 (count=0 is even? No. count=0: next is position 1, which is odd (case2's even positions are even in the subsequence). Wait, in case2, even positions must be <=x. So in the subsequence:

position 1 can be any.

position 2 must be <=x.

position 3 can be any.

So, for case2, when building the subsequence:

elements are taken as follows:

for each element in a:

if count is even (next position is odd, no constraint) → take it, count +=1.

if count is odd (next position is even, must be <=x):

if element <=x → take, count +=1.

Else, skip.

So, for x=2 and case2.

Processing the array [1,2,3,4].

count starts at 0.

element 1: count is 0 (even). next position is 1 (odd, case2's even positions are 2,4...). So, take it. count becomes 1.

element 2: count is 1 (odd). next position is 2 (even). So, need to take elements <=2. element 2 is <=2: take. count becomes 2.

element3: count is 2 (even). next position is 3 (odd). take it. count becomes3 → which is >=3. So case2 returns True.

Thus, x=2 is possible. So, in the binary search, when x=2 is mid, the check returns True. So high becomes mid-1=1.

Now, low is 1, high is1.

mid is1.

Check case1 and case2 for x=1.

case1: can we form a subsequence of 3 elements where odd positions are <=1.

elements are 1,2,3,4.

count=0 (even) → next position is 1 (must be <=1). Take 1. count=1.

even position: take 2. count=2.

next position is3 (odd, must be <=1). The next elements are3,4, which are >1. So can't take. So count=2 <3. case1 fails.

case2: check if even positions (position 2) are <=1.

Processing:

count=0 (even, next is 1 → can take any. Take 1. count=1.

next position 2 (even) must be <=1. Next element is2>1. Can't take. So skip.

element3: count is1. Next element is3. Check if it's <=1? No. So can't take. So skip.

element4: same. So count remains 1. So total is 1 <3. case2 fails.

So x=1 is not possible.

Thus, the answer is 2.

So the binary search logic works.

Thus, the code seems correct.

Now, the code in Python:

But to handle large inputs, we need to read the input efficiently.

So, in Python:

Read n, k from input.

a = list(map(int, input().split())).

Then proceed with the binary search.

Now, the code.

But the code needs to be efficient. Let's make sure that the check functions are as efficient as possible, perhaps by using loops and avoiding function calls. But in Python, function calls are not that expensive. However, for each binary search step, we need to check both case1 and case2, which can be done in a single pass through the array for both cases. Wait, but perhaps it's more efficient to process the array once and check for both case1 and case2 in the same loop. However, since case1 and case2 are separate conditions, perhaps it's better to handle them as separate checks.

Wait, no. Because each check requires processing the array in a different way. So, for case1 and case2, the way the elements are selected is different. So, each check must be done separately.

But given that for each x, we have to check both case1 and case2, each with O(n) time, perhaps combining the two checks into a single pass is possible. For example, during the same iteration through the array, track the counts for both cases. However, in practice, the two cases are independent and can't be tracked together, so it's better to process them separately.

Thus, the code would be structured as follows:

Read n and k.

Read the array.

Compute low and high.

Binary search between low and high.

For each mid, check case1 and case2.

Now, let's code this.

Sample code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    low = min(a)

    high = max(a)

    ans = high

    def check_case1(x):

        count =0

        for num in a:

            if count %2 ==0:  # next is odd

                if num <=x:

                    count +=1

            else:  # next is even, take any

                count +=1

            if count >=k:

                return True

        return count >=k

    def check_case2(x):

        count =0

        for num in a:

            if count %2 ==1:  # next is even

                if num <=x:

                    count +=1

            else:  # next is odd, take any

                count +=1

            if count >=k:

                return True

        return count >=k

    while low <= high:

        mid = (low + high) //2

        if check_case1(mid) or check_case2(mid):

            ans = mid

            high = mid -1

        else:

            low = mid +1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3
1 2 3 4
""",
            "output": \
"""\
2
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

Testing against sample inputs 2, 3.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    low = min(a)

    high = max(a)

    ans = high

    def check_case1(x):

        count =0

        for num in a:

            if count %2 ==0:  # next is odd

                if num <=x:

                    count +=1

            else:  # next is even, take any

                count +=1

            if count >=k:

                return True

        return count >=k

    def check_case2(x):

        count =0

        for num in a:

            if count %2 ==1:  # next is even

                if num <=x:

                    count +=1

            else:  # next is odd, take any

                count +=1

            if count >=k:

                return True

        return count >=k

    while low <= high:

        mid = (low + high) //2

        if check_case1(mid) or check_case2(mid):

            ans = mid

            high = mid -1

        else:

            low = mid +1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
5 3 4 2 6
""",
            "output": \
"""\
2
""",
        }, 
        {
            "input": \
"""\
6 4
5 3 50 2 4 5
""",
            "output": \
"""\
3
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

Case1: can we form a subsequence of 3 elements where odd positions are <=2.

The array is [5,3,4,2,6].

Processing:

count starts at0 (even → next is odd).

5>2: can't take. So proceed.

3>2: can't take.

4>2: can't take.

2<=2: take. count becomes1.

next is even: take next element (6). count becomes2. Now need one more. next is odd. next element is 6. But no elements left. So count is 2 <3. case1 fails.

case2: check if even positions are <=2.

Processing:

count starts at0 (even → next is odd (position1), can take any.

Take 5. count becomes1.

next even (position2) must be <=2. next element is3>2. Can't take.

Next element is4>2. Can't take.

next element is2<=2: take. count becomes2.

next element is6. count is even (2%2=0 → next position is3, can take any. take 6. count becomes3. So case2 returns True. Thus, x=2 is possible. So the code would find that.

But what's the answer for this case?

The example says output is 2.

So the code would return 2, which is correct.

Another test case:

6 4

5 3 50 2 4 5 → output3.

We can see that the code would check x=3.

case1: can we select a 4-length subsequence with odd positions <=3.

Processing the array [5,3,50,2,4,5].

count starts at0 (even → next is odd, must be <=3).

5>3: can't take. next is3 <=3. count becomes1.

even position: take 50. count=2.

next odd: must be <=3. next elements are50>3, 2<=3. take 2. count=3.

even: take 4. count=4. which is >=4. So case1 returns True.

So x=3 is possible, and the code would set ans=3.

Thus, the code works.

Thus, the code seems correct.

Now, considering the time constraints: for n=2e5, each check is O(n). Binary search steps are about 30. 2*2e5*30=12e6 operations. Which is acceptable.

But in Python, even 1e8 operations may take around 10 seconds. So 12e6 is about 0.12 seconds, which is fine.

Now, code optimizations.

In Python, function calls are relatively slow, so perhaps it's better to inline the checks. But in this case, since each check is a loop, the overhead is minimal.

Another optimization: in the check_case1 and check_case2 functions, once count >=k, we can break the loop early, which is already implemented.

Thus, the code should be efficient enough.

Therefore, the final code is as written.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))

low = min(a)
high = max(a)
ans = high

def check_case1(x):
    count = 0
    for num in a:
        if count % 2 == 0:
            if num <= x:
                count += 1
        else:
            count += 1
        if count >= k:
            return True
    return count >= k

def check_case2(x):
    count = 0
    for num in a:
        if count % 2 == 1:
            if num <= x:
                count += 1
        else:
            count += 1
        if count >= k:
            return True
    return count >= k

while low <= high:
    mid = (low + high) // 2
    if check_case1(mid) or check_case2(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)
```
