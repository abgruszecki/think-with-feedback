<think>
Okay, let's see. I need to solve this problem where for each sliding window of size k in the array, I have to find the maximum element that occurs exactly once in that window. If there are no such elements, output "Nothing". 

First, I need to figure out how to efficiently track the elements in each window, count their occurrences, and then find the maximum among those with a count of exactly one. The constraints are up to 1e5 elements, so any O(nk) approach would be too slow. So we need an O(n) or O(n log k) solution.

Hmm. Let's think about data structures. For each window, we need to know the frequency of each element. A sliding window approach with a hashmap (like a frequency dictionary) could work. But maintaining the frequency counts as the window slides, adding the next element and removing the leftmost one. Then, for each window, we need to find the maximum element that has a frequency of 1.

The problem is that for each window, checking all elements to find those with frequency 1 and then taking the maximum would be O(k) per window, which would lead to O(nk) time overall. That's not feasible for n=1e5.

So, we need a way to track the maximum efficiently. Let's think: perhaps we can maintain a max-heap or a TreeSet (like in Java) of elements with frequency exactly 1. But maintaining such a structure as elements are added and removed from the window is tricky.

Alternatively, for each element in the current window, when its frequency changes to 1, we add it to some structure, and when it's no longer 1, we remove it. Then, the maximum in that structure is our candidate. But how to do this efficiently.

Let's outline the steps:

1. Use a sliding window of size k. Maintain a frequency dictionary (counts) of elements in the current window.

2. Also, maintain a data structure that keeps track of elements with count exactly 1. For each such element, we can quickly find the maximum.

The key is maintaining that data structure efficiently as the window slides.

So, when a new element is added to the window (right end):

- Increment its count in the frequency dict.

- If the count becomes 1, add it to the structure. If before adding it was 2, remove it from the structure (since now it's 1 again, but maybe after being 2 before? Wait, when adding a new element, if it's already in the window, then the count increments. So for example, when adding an element, if its previous count was 0: adding makes it 1 → add to structure. If previous count was 1: then after increment, it's 2 → need to remove from structure. If previous count was 2: after increment, it's 3 → no change in the structure (since it wasn't in the structure anymore).

Wait, let's think:

When the count for an element x changes from 0 → 1: add x to the structure.

If x was in the structure (count was 1) and we add another x (count becomes 2), then we need to remove x from the structure.

Similarly, when removing an element from the left of the window:

- Decrement its count.

- If the count was 2, then after decrement, it's 1 → add to the structure.

If the count was 1, then after decrement, it's 0 → remove from the structure.

So, for each element addition and removal, we can track whether their count transitions into or out of 1, and update the structure accordingly.

Now, the structure that holds elements with count exactly 1 must support:

- Adding elements.

- Removing elements.

- Quickly finding the maximum.

A max-heap could work, but the problem is that when elements are added and removed, the heap might contain elements that are no longer in the valid set (because their count is not 1). So, if we just use a heap, we could have stale entries. So, when trying to get the maximum, we need to check if the current top of the heap is actually in the structure (i.e., its count is 1). If not, we pop it and check the next.

But this could lead to O(1) for insertion and O(1) (amortized) for getting the maximum. Because each element is pushed and popped at most once.

So the approach would be:

- Maintain a max-heap (priority queue) that contains all elements which are candidates (count is 1), but may have some elements that are no longer valid (count not 1 anymore).

- Also maintain a frequency dictionary.

- When querying the maximum for the current window, we check the top of the heap. If the top element has a count of exactly 1 in the frequency dict, then that's the maximum. Otherwise, we pop it from the heap and continue until we find a valid element or the heap is empty.

This way, each element is pushed into the heap once, and popped once. So over all operations, this is O(n log n) time for the heap operations.

But how to track the current count when checking the heap's top. Because the frequency dict is maintained correctly as the window slides.

So for each window, when we need to find the maximum:

- While the heap is not empty and the top element's count is not 1, pop it.

- The top element now is the maximum (if any).

But since the same element can be pushed into the heap multiple times (if it's added again after its count returns to 1), we need to handle that.

Wait, no. For example, suppose the element x is in the window, count is 1. So it's in the heap. Then another x is added, count becomes 2. So we remove x from the heap. Then, when the first x is removed (window slides), count becomes 1 again. So we add x to the heap again. So in this case, the heap would have x twice. But when we check the top, the first occurrence (the one from the previous addition) is invalid because after sliding, x's count is 1 again, but the heap has another entry. Hmm. So this approach could lead to multiple entries of the same element in the heap, but when checking, we verify the current count.

So when we process the top of the heap, if the count is 1, then we take it. Otherwise, we pop it. This way, even if there are multiple entries for the same element in the heap, only the valid ones are considered.

But when an element's count becomes 1 again, we need to push it back into the heap. So every time an element's count transitions to 1, it's pushed into the heap. So the heap can have duplicates, but when checking, we verify the current count.

This approach might work, but for each window, when we check the maximum, we might have to pop some elements from the heap until we find a valid one.

In the worst case, for each window, you have to pop O(n) elements, but over all windows, each element is pushed and popped once. So the amortized time per window would be O(1) for the heap operations.

But I'm not sure. Let's see.

Each element can be pushed to the heap every time its count transitions to 1. So for example, an element that enters the window, is added to the heap (count 1), then another occurrence is added (count 2, removed from heap). Then, when that occurrence leaves the window, the count becomes 1 again, so it's pushed again. So in this case, the same element is pushed twice into the heap. So when processing the heap, even if there are duplicates, as long as the count is valid, the first occurrence is taken. The other entries would be invalid (because when the element is pushed again, it's after the count becomes 1 again).

Wait, perhaps the first occurrence in the heap (the one pushed earlier) would have a count that's now 2, but the second occurrence is pushed later and the count is 1. So during the processing for a window, when we pop the top, if it's not valid, we proceed to the next. Once we find a valid element, that's the maximum.

So even with multiple entries, this approach works.

So the steps would be:

Initialize a frequency dictionary (counts), a max-heap (max_heap), and a variable left=0.

For each right in 0 to n-1:

    add the current element to the window.

    update counts: counts[arr[right]] +=1

    if the new count is 1:

        push arr[right] to max_heap

    elif the new count is 2:

        if arr[right] was in the heap (but how?), perhaps we need to mark it as invalid. But this approach doesn't track that.

Wait, the problem is that when the count increases to 2, the element should no longer be considered. But since the heap can have multiple entries of this element (from previous times it was added when count was 1), when processing the heap, we need to check if the current count is 1. So even if the element was pushed to the heap when count was 1, but now the count is 2, those entries are invalid and should be ignored.

But how do we track the current count? Because the counts dictionary is updated as the window slides. So when we check the top element of the heap, we can look up its count in the current counts dict, which is accurate for the current window.

So the approach is:

For each window, after updating the counts for the elements in the window, we process the max_heap as follows:

    while the max_heap is not empty and counts[top_element] != 1:

        pop the top_element

    if the heap is not empty:

        output the top_element

    else:

        output "Nothing"

But wait, the window is of size k, and as we move the window, the left element is removed. So the code has to manage the sliding window correctly. Let me outline the steps again.

The window starts at index i=0, and ends at i+k-1. For each window, we process the elements from left to right.

But in terms of code:

We can use a sliding window approach where for each new element added to the right (right pointer), when the window's size exceeds k, we remove the leftmost element (left pointer).

So the process is:

Initialize left =0, right=0.

For each right from 0 to n-1:

    add arr[right] to the window.

    update counts: counts[arr[right]] +=1

    if counts[arr[right]] ==1:

        heappush(max_heap, -arr[right])  # since Python's heapq is a min-heap, using negatives for max-heap

    elif counts[arr[right]] ==2:

        # no action, but in the heap, existing entries of this element will be invalid

    # Now, if right >= k-1, we need to process the window.

    if right >= k-1:

        # process the current window [left, right]

        # first, check if the left element is outside the window now (window size is k)

        # so, after adding the right element, the window size is right - left +1.

        # Wait, no. We need to manage the window to have exactly k elements.

        # So when right reaches k-1 (i.e., the first window is when right=0, left=0, if k=1). Wait, perhaps better to adjust the loop.

Wait, perhaps the correct approach is to have the window from left to right, and when the window size (right - left +1) exceeds k, we increment left.

Wait, but how to process the window when right is increasing from 0 to n-1. For each right, when the window is larger than k, we increment left until the window is size k.

But for example, when the window is exactly size k, then we can process it. So the code would be:

for right in range(n):

    add arr[right] to the window (update counts)

    while left <= right and (right - left +1) >k:

        remove arr[left] from counts (decrement count)

        if counts[arr[left]] ==1:

            heappush(max_heap, -arr[left])

        elif counts[arr[left]] ==0:

            # remove from counts?

            pass

        left +=1

    # then process the window if size is k

    if right >=k-1:

        # Now, process the current window

        # Process the heap

        while max_heap and counts[-max_heap[0]] !=1:

            heappop(max_heap)

        if max_heap:

            print(-max_heap[0])

        else:

            print("Nothing")

But this approach may have a problem. When you remove elements from the left (left pointer increment), you decrement their counts, and if their count drops to 1, you push them into the heap again. But when you push them into the heap, they are now candidates for future windows. However, in the current window (after left has been incremented), maybe those elements are not in the window anymore.

Wait, for example: when you remove arr[left] from the window (since the window is moving), you decrement its count. If the count becomes 1, then that element (arr[left]) was present once in the previous window but after being removed, but now its count is 1 again (meaning it's present once in the current window? No. Because the current window is from left+1 to right. So when arr[left] is removed, its count is decremented. So if after decrementing, count becomes 1, that means that in the current window, arr[left] is present once. But arr[left] is outside the current window (since left was incremented). So the count for arr[left] is 1, but it's not part of the current window. So pushing it into the heap is incorrect.

Ah, that's a problem. Because the counts dictionary tracks the frequency of elements in the current window. So when you remove arr[left], you decrement its count. If the count becomes 1, that means the current window (after left has been incremented) has one occurrence of that element. But in reality, the element was part of the previous window and is now removed, so the count should not be 1 if it's not in the current window.

Wait, no. Let's think: the counts dictionary should represent the elements in the current window (left to right, inclusive). So when we remove arr[left], we decrement counts[arr[left]], and if it hits zero, we can delete it from the counts. But if it's 1, that means the current window (after left is incremented) has one occurrence of that element. So the element is present in the current window.

Wait, no. Because when we remove arr[left], the current window is left+1 to right. So the counts dictionary must represent elements in left+1 to right. Therefore, if after decrementing arr[left], the count becomes 1, that means that in the new window (left+1 to right), there's one occurrence of arr[left]?

No. Because arr[left] is being removed from the window. The count for arr[left] in the window (left+1 to right) is counts[arr[left]] after decrement. So if the count is 1, that implies that there is one occurrence of arr[left] in the new window (left+1 to right). But that can't be, since the element was removed. So this suggests that the counts dictionary is not being maintained correctly.

Ah! That's a critical mistake. The counts dictionary must track the elements in the current window. So when you remove an element from the window (left pointer moves), you need to decrement its count. But after decrementing, if the count is zero, you should remove it from the counts.

So the code when removing an element from the left would be:

element = arr[left]

counts[element] -=1

if counts[element] ==0:

    del counts[element]

else:

    # if the count is now 1, then this element is present once in the current window (left+1 to right)

    # so we need to add it to the heap

    if counts[element] ==1:

        heappush(max_heap, -element)

So when we remove arr[left], if after decrementing, the count is 1, then the element is present once in the current window. So adding it to the heap is correct.

For example:

Original window: [a, a, b], counts: a:2, b:1. Then, when left increments (window becomes [a, b]), the count of a is decremented to 1, so we add a to the heap. Now, the current window has a once, so a is a candidate. So the heap now has a, and when processing the window, the maximum would be a or b (if b's count is 1).

Yes, that makes sense.

So the code steps are:

For each element added to the window (right pointer):

- Increment its count. If the new count is 1, add to the heap. If the new count is 2, remove from the heap (but since the heap is a max-heap and elements are added when count is 1, but existing entries may have count 2 now, which are checked during processing).

Wait, no. When adding a new element, if the count was 0 → becomes 1: add to heap.

If the count was 1 → becomes 2: remove from the heap (but since we can't remove from a heap in O(1), we just leave it and when processing, check if the count is 1. So the heap may contain elements that are now invalid (count !=1), but during processing, they are popped.

So the key is that when you process the heap for the current window, you check each top element's count. If it's 1, it's valid. Otherwise, it's popped.

Thus, the code can proceed as follows:

Initialize:

counts = defaultdict(int)

max_heap = []

left =0

for right in range(n):

    num = arr[right]

    counts[num] +=1

    if counts[num] ==1:

        heapq.heappush(max_heap, -num)

    elif counts[num] ==2:

        # Any existing entries of num in the heap are invalid now, but they are handled when processing

        pass

    # Now, check if the window exceeds k

    while (right - left +1) >k:

        left_num = arr[left]

        counts[left_num] -=1

        if counts[left_num] ==0:

            del counts[left_num]

        else:

            if counts[left_num] ==1:

                heapq.heappush(max_heap, -left_num)

        left +=1

    # Now, if window is k, process

    if right >=k-1:

        # Now, find the maximum element in the heap with count 1

        while max_heap:

            current = -max_heap[0]

            if current in counts and counts[current] ==1:

                break

            heapq.heappop(max_heap)

        if max_heap:

            print(current)

        else:

            print("Nothing")

But this code may have some issues. For example, when counts[left_num] is decremented to 1, which could be part of the current window. So adding it to the heap is correct.

But how to handle the elements that are popped from the heap when processing. For example, after pushing left_num to the heap (because its count became 1), when processing, the code checks if counts[current] is 1. Which it is. So the code works.

Another thing to note: the heap may contain elements that are no longer in the counts (i.e., their count is 0). So when checking, we need to see if current is in counts (i.e., count >0) and count is 1. So in the processing loop, we first check if current is in counts. If not, then it's not part of the current window, so we pop it. Otherwise, check if count is 1.

This should handle all cases.

Now, let's test this approach against the sample inputs.

First sample input:

5 3

1

2

2

3

3

The array is [1,2,2,3,3]

The windows are:

[1,2,2] → elements with count 1: 1. Max is 1.

[2,2,3] → elements with count 1: 3. Max is 3.

[2,3,3] → elements with count 1: 2. Max is 2.

Sample output is as given.

Let's see how the code would process this.

First, when right=0 (num=1):

counts[1] =1 → push -1 to heap.

window size is 1 (since k=3). So no processing.

right=1 (num=2):

counts[2] becomes 1 → push -2.

window size is 2. Still <3.

right=2 (num=2):

counts[2] becomes 2. So no push.

window size is 3. Now process.

Check the heap. The top is -1 (current=1). Check counts[1] → 1. So output 1.

Then, the next window. The code increments left to 1 after processing.

Now, for right=3 (num=3):

Add to counts. counts[3] =1 → push -3.

window size is 3 (left=1, right=3). Process.

Check heap. The top is -3 (current=3). counts is 1? No, the window is [2,2,3]. counts is 2:2, 3:1. So 3 has count 1. So output 3.

Then right=4 (num=3):

counts[3] becomes 2. No push.

window size is 3 (left=2, right=4 → elements [2,3,3]).

Process:

Check the heap. The top is -2 (current=2). counts[2] is 1? Let's see:

The window is [2,3,3]. counts[2] is 1 (since left=2, right=4. The element at index 2 is 2. So the current window is indices 2,3,4: elements 2,3,3. So counts[2] is 1 (since left was 2, which was incremented from 1, but when left was 1, the code removed the left_num (arr[1] =2) → counts[2] was decremented from 2 to 1. Then, after pushing -2 into the heap.

So when processing the third window (indices 2,3,4):

The heap has elements like -3 (from when right=3), -2 (from when left=1 was incremented, counts[2] became 1 again). So when the code processes this window, the top of the heap is the smallest (since we store negatives). The max-heap is implemented with a min-heap using negatives. So the first element is -3 (current=3), but counts[3] is 2 (since in this window, 3 occurs twice). So code pops it. Then next element is -2 (current=2). Check counts[2] is 1 → yes. So output 2.

Which matches the sample.

Another sample:

6 4

3

3

3

4

4

2

The array is [3,3,3,4,4,2].

The windows are:

[3,3,3,4] → elements with count 1:4. Output 4.

[3,3,4,4] → no elements with count 1. Output Nothing.

[3,4,4,2] → elements with count 1:3,2. Max is 3.

Sample output is 4, Nothing,3.

Let's see how code processes this.

First window (indices 0-3):

elements: 3,3,3,4. counts: 3:3,4:1. So 4 is in heap. Output 4.

Second window (indices 1-4): 3,3,4,4. counts:3:2,4:2. So no elements with count 1. Output Nothing.

Third window (indices 2-5):3,4,4,2. counts:3:1,4:2,2:1. So elements 3 and 2. Max is 3.

Code steps:

When processing the second window, after removing left=0 (3), counts[3] becomes 2. Then when adding elements up to right=3 (4), but the code pushes 4. Then when the window is 1-4 (right=4 is 4), counts for 4 becomes 2. The heap after processing would have 4 (pushed when added), but then when counts becomes 2, the entries are invalid.

Processing this window:

Heap starts with elements like -4, etc. Check top. 4's count is 2 → pop. Then other elements? Let's see:

After the first window (0-3), the heap has -4. Then when processing the next window (left=1, right=4):

The elements are 3,3,4,4. counts[3]=2, counts[4]=2. So when processing, the heap is popped until empty. So output Nothing.

Then for the third window (left=2, right=5):

The code adds 2 (right=5, element=2. counts[2] becomes 1 → push into heap. The heap now has -2, and possibly other elements.

When processing the window, the code checks the heap. The top is -3 (if it was pushed when the counts became 1). Let's see:

When left was incremented to 2, the code removed left=1 (3). counts[3] was decremented from 3 to 2 (since in the previous window, counts[3] was 3, then after decrementing to 2. So counts[3] was not 1, so no push. Then when left increments to 2, and the window becomes [3,4,4,2], the code adds 2, which has count 1 → push into heap.

But in the third window, counts[3] is 1 (since left was 2, which was part of the window after removing left=1. Wait, the third window is left=2 (element=3), right=5 (element=2). The elements are 3,4,4,2. So counts[3] is 1 (since there's one occurrence of 3 in this window). So when the code processed the left increments (after right=4, left was 1. Then, after adding right=5 (element 2), the code checks the window size. The window is from left=2 to right=5 (size 4). So during the processing of left increments when adding right=5, the code removes elements until window is 4. But in this case, the window is already 4 (right=5 - left=2 +1 =4, which is k=4). So no left increments. So for the third window, counts[3] is 1 (since in the window [3,4,4,2], there's one 3. So when the code processes this window, the heap may have elements like -3 (pushed when counts became 1) and -2 (pushed when counts became 1).

So during processing, the heap's top is -3. Check counts[3] → 1. So output 3.

Yes, which matches the sample.

So the code seems to handle the sample cases correctly.

Now, the code needs to be implemented in Python.

But in Python, the heapq is a min-heap, so to implement a max-heap, we push the negative values. Also, when we process the heap, the top element is the smallest negative, which corresponds to the largest original value.

Another consideration is the efficiency. For each element, when it's added to the heap, it's O(log m), where m is the current size of the heap. But in the worst case, the heap can have O(n) elements, leading to O(n log n) time for all heap operations. For n=1e5, this is acceptable.

But what about the processing loop (the while loop that pops elements from the heap until a valid one is found)? Each element is pushed once and popped once. So overall, the processing of the heap is O(n log n) time.

The other steps (updating counts, moving left and right pointers) are O(n) time.

So the total time complexity is O(n log n), which should be acceptable for n=1e5.

Now, the code:

But in the code, when left_num is removed from the window (left pointer increments), if after decrementing the count, it's 1, then we push it into the heap. That's correct because the element is now present once in the current window.

Now, code steps:

Read n and k.

Read the array. Since each element is on a separate line, read n lines and collect into a list.

Then process as outlined.

But in Python, the input is read via input(). For n up to 1e5, using a list comprehension would be efficient.

So:

n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

Then, code as outlined.

Now, the code:

But when we process the heap for each window, the code may have to process multiple elements. However, over all windows, each element is pushed once and popped once, leading to O(n) heap operations, each O(log n). So the time is manageable.

But the code may have a problem when the same element is pushed multiple times into the heap. For example, if an element's count transitions to 1 multiple times. But since the processing step checks the current count, the code will handle it correctly.

Another possible optimization is to use a Counter or a default dictionary for the counts. But for speed, perhaps a regular dictionary is better, but in Python, defaultdict is efficient.

So in code:

Testing against sample input 1.

```python
from heapq import heappush, heappop
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())

    arr = [int(input_stream.readline()) for _ in range(n)]

    counts = defaultdict(int)

    max_heap = []

    left =0

    for right in range(n):

        num = arr[right]

        counts[num] +=1

        if counts[num] ==1:

            heappush(max_heap, -num)

        # No action needed when counts[num] becomes 2

        # Maintain window size <=k

        while (right - left +1) >k:

            left_num = arr[left]

            counts[left_num] -=1

            if counts[left_num] ==0:

                del counts[left_num]

            else:

                if counts[left_num] ==1:

                    heappush(max_heap, -left_num)

            left +=1

        # Process when window is exactly k

        if right >= k-1:

            # Find the maximum element with count 1

            valid_max = None

            while max_heap:

                current = -max_heap[0]

                if current in counts and counts[current] ==1:

                    valid_max = current

                    break

                else:

                    heappop(max_heap)

            if valid_max is not None:

                print(valid_max, file=output_stream)

            else:

                print("Nothing", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 4
3
3
3
4
4
2
""",
            "output": \
"""\
4
Nothing
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

Sample 2:

Input:

6 4

3

3

3

4

4

2

Output:

4

Nothing

3

First window (indices 0-3):

elements 3,3,3,4 → counts:3:3,4:1. Heap has -4. Output 4.

Second window (indices 1-4):

elements 3,3,4,4 → counts:3:2,4:2. Heap has elements like -4 (from before) and others, but when processing, they are popped. So output Nothing.

Third window (indices 2-5):

elements 3,4,4,2 → counts:3:1,4:2,2:1. Heap has -3 (pushed when left=2, counts[3] becomes 1) and -2 (pushed when right=5). Processing the heap, the top is -3 (current 3), which is valid. So output 3.

Thus, the code works.

Now, possible edge cases.

Test case where all elements are the same and k=1. For example, n=3, k=1, elements 5,5,5. Each window is a single element. Since each element is in the window once, the maximum is 5 each time. But since each occurs once, so output 5 three times.

Another case: n=1, k=1. Output the element.

Test case with k=1: each window is a single element, so all elements must be output as long as they are unique (which they are, since each is in the window once). So output each element.

Another case: all elements are distinct. Then, each window of size k will have all elements unique. So the maximum is the maximum in each window.

But how does the code handle this? For each window, the heap will contain all elements, but when processing, the code checks if the count is 1. Since all counts are 1, the maximum is taken from the heap.

The code should handle this correctly.

Potential issues:

- Elements with negative values. But since the heap stores negative values, comparing them works correctly.

For example, if an element is -5, stored as 5 in the heap (since pushed as -(-5) =5). But when checking counts, the current value is -5, which is correct.

Wait, no. Because in the code:

when we push into the heap, we do heappush(max_heap, -num). So for num=-5, the stored value is 5, which in the min-heap will come before smaller numbers. So when the code pops the smallest stored value (5), which represents the original -5. But when the heap has 5 and 3 (stored values), the min-heap will pop 3 first. So the code treats stored values as the max-heap of the original numbers.

Yes. For example, numbers 5 and 3: stored as -5 and -3. The min-heap has -5, -3. The smallest is -5, so popped first. So current is 5 (since -(-5) is 5). Which is the max.

If the numbers are -5 and -3: stored as 5 and 3. The min-heap will have 3 (from -3) and 5 (from -5). So when popped, the smallest is 3 → current is -3, which is the max between -3 and -5.

Yes. So the code correctly handles negative numbers.

Another test case: n=3, k=2, elements 5,5,5.

Windows: [5,5] → no elements with count 1. Output Nothing. [5,5] → same. So two outputs: Nothing, Nothing.

Thus, the code should handle that.

Another case: n=2, k=2, elements [1,2]. Output 2 (since both occur once, max is 2).

Thus, the code should output 2.

Thus, the code handles all these cases.

So, the code should be correct.
</think>

```python
from heapq import heappush, heappop
import sys
from collections import defaultdict

def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    counts = defaultdict(int)
    max_heap = []
    left = 0

    for right in range(n):
        num = arr[right]
        counts[num] += 1
        if counts[num] == 1:
            heappush(max_heap, -num)

        while (right - left + 1) > k:
            left_num = arr[left]
            counts[left_num] -= 1
            if counts[left_num] == 0:
                del counts[left_num]
            else:
                if counts[left_num] == 1:
                    heappush(max_heap, -left_num)
            left += 1

        if right >= k - 1:
            valid_max = None
            while max_heap:
                current = -max_heap[0]
                if current in counts and counts[current] == 1:
                    valid_max = current
                    break
                else:
                    heappop(max_heap)
            print(valid_max if valid_max is not None else "Nothing")

if __name__ == "__main__":
    main()
```
