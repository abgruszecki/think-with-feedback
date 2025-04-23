<think>
Okay, so I need to solve this problem where I have to select up to k songs from a playlist to maximize the pleasure. The pleasure is calculated as the sum of the lengths multiplied by the minimum beauty in the selected set. Hmm, let's think about how to approach this.

First, let's understand the problem. For any subset of songs we choose (with size up to k), the key factors are the sum of their t_i's and the minimum b_i among them. So the total is (sum t) * (min b). We need to maximize this value.

The constraints are n up to 3e5, which is 300,000. So any O(n^2) approach is out of the question. We need an O(n log n) or O(n) solution.

Let me think about possible approaches. Since the minimum beauty is a critical part here, maybe we can fix the minimum beauty and then find the best possible sum of t's given that the beauty is at least that value. Then for each possible minimum, we can compute the maximum sum of t's from songs with beauty >= that minimum, choosing up to k songs. Then take the maximum over all these possibilities.

But how do we efficiently compute for each possible minimum b_i the maximum sum of t's from songs with b_i >= current b, up to k elements?

Alternatively, perhaps we can sort the songs in descending order of beauty. Then, for each position i in the sorted list, consider the songs up to i (since they have higher or equal beauty to song i's b) and select the top (up to k) t's from those songs, including song i. The minimum beauty would be song i's b, and the sum would be the sum of the largest (k) t's in the first i songs (including the i-th).

Wait, that's an interesting idea. Let's think through this. If we sort all songs in decreasing order of beauty, then when we process the i-th song, all songs from 0 to i have a beauty >= b_i. So the minimum beauty in any subset selected from these songs could be b_i. But if we take the current song (i) and any others from the first i songs, the minimum beauty is at least b_i. However, to have the minimum exactly b_i, we need to include at least one song with beauty exactly b_i. But if the i-th song has the lowest beauty in the subset, then including it ensures that the minimum is b_i. So by considering each i in the sorted list, we can compute the sum of the top (k-1) t's from the first i songs plus the t_i of the current song, multiplied by b_i. Or maybe just the top k t's up to i, and multiply by the current b_i. Wait, because when we process the i-th song, which is sorted in descending order, the first i songs have beauty >= b_i. So the minimum in any subset chosen from them (including the i-th) can be >= b_i. But if we include the i-th song, then the minimum is at most b_i, but since all others in the subset are from the first i songs (including the i-th), their beauty is >= b_i. So the minimum is exactly b_i. So for each i, if we select a subset that includes the i-th song (which has beauty b_i) and any other songs from the first i songs (which have beauty >= b_i), then the minimum beauty is b_i. Therefore, the pleasure is (sum of t's of selected songs) * b_i.

So the approach would be:

1. Sort all songs in descending order of b_i.

2. For each i in 0..n-1:

   a. Collect the first i+1 songs (since they are sorted, all have b >= b_i).

   b. Among these, select up to k songs (including song i) with the largest t's.

   c. Sum their t's and multiply by b_i. Keep track of the maximum such value.

The maximum over all i would be the answer.

Wait, but why include song i? Because if we don't include it, then the subset's minimum could be higher than b_i. But in that case, that subset would have been considered when processing an earlier i (since the songs are sorted). So by considering each i as the minimum in the subset, we cover all possible cases where the subset's minimum is exactly b_i. Then the maximum among all these would be the answer.

So the key is to process each song in the sorted order, and for each i, compute the maximum possible sum of up to k t's from the first i+1 songs (including song i), multiply by b_i, and track the maximum.

But how to efficiently compute the sum of the top m t's (where m is up to k) from the first i+1 songs?

We need a data structure that allows us to keep track of the top t's as we process each song. Since the songs are sorted by beauty, we can process them in order. For each song, we add its t to a priority queue (or a heap), but a min-heap that keeps the largest k elements. Wait, here's the idea:

We maintain a min-heap that holds the largest k t's so far. For each song i (sorted in descending order of b_i), we add its t to the heap. If the heap's size exceeds k, we remove the smallest t in the heap. Then, the sum of the elements in the heap (if any) is the maximum sum possible for up to k elements. Then, when considering song i, the sum is the sum of the heap elements (since we have up to k elements with largest t's from the first i+1 songs), multiplied by b_i. Since the current song's b is the minimum of the subset (as the subset is chosen from the first i+1 songs, which have b >= current b_i, and the current song's b is the smallest so far in the subset).

Wait, but the current song is part of the first i+1 songs. So when we process the i-th song (0-based?), we add it to the heap. Then, the heap contains the largest possible t's up to k elements. Then, the sum of the heap elements multiplied by the current song's b_i gives a candidate value for the maximum. We can track the maximum over all these candidates.

Wait, let's think with an example. Let's say we have songs sorted in decreasing order of beauty. The first song has the highest beauty. When we process it, the heap contains its t (assuming k >=1). Sum is t1 * b1. Then, the next song has lower beauty. When we add its t to the heap. If k is 2, then we take both. Sum is (t1 + t2) * b2 (since the minimum beauty is b2). But maybe there's a case where taking just the first song again (but with k=1), the sum would be t1 * b1, which is better. But since we are tracking the maximum at each step, including when we processed the first song, the maximum will be considered.

So, by processing each song in order, and maintaining a heap that keeps the top m t's (m up to k), we can compute for each song the maximum possible sum of up to k elements from the first i+1 songs, multiplied by the current song's b_i. Then, the maximum of all these is the answer.

Yes, this seems correct. Because for each song i in the sorted list, the subset of songs we are considering includes the song i (since it's part of the first i+1 songs), and all other songs in the subset have b >= b_i. So the minimum is b_i. The sum is the sum of the largest up to k t's from the first i+1 songs, which is exactly what the heap is maintaining.

So the algorithm steps are:

1. Sort the songs in descending order of beauty.

2. Initialize a min-heap to keep track of the top t's. Also, maintain a sum variable that holds the sum of the elements in the heap.

3. For each song in the sorted list:

   a. Add its t to the heap. If the heap size exceeds k, pop the smallest element and subtract it from the sum. Then add the new t (but wait, need to handle the sum correctly).

   b. The sum of the heap elements is the sum of the top m t's (m is min(k, i+1)).

   c. Multiply this sum by the current song's b. Compare with the current maximum, update if needed.

But how to maintain the sum efficiently. Because every time we add a new t, we need to see if the heap's size is over k. If it is, we remove the smallest element (since it's a min-heap, the top is the smallest). So we can track the sum as we go.

Yes. Here's the process:

Initialize sum = 0 and a min-heap.

For each song in sorted list:

   add t_i to the heap. sum += t_i.

   if the heap size exceeds k:

       popped = heappop(heap)

       sum -= popped

   current_pleasure = sum * b_i

   max_pleasure = max(max_pleasure, current_pleasure)

This way, for each song, we have the sum of the top k t's (if there are more than k) from the first i+1 songs. If there are less than k, we take all. Then, multiplying by b_i gives the pleasure for choosing those songs (with min beauty = b_i).

This seems correct. Let's test with the first example.

First example input:

4 3

Songs:

4 7

15 1

3 6

6 8

Sorted by b in descending order:

6 8 (b=8)

4 7 (b=7)

3 6 (b=6)

15 1 (b=1)

k=3.

Processing each song:

First song (t=6, b=8):

heap is empty. Add 6. sum =6. heap size 1 <=3.

current_pleasure =6 *8=48. max is 48.

Second song (t=4, b=7):

Add 4. sum=10. heap size 2.

current_pleasure=10*7=70. max is 70.

Third song (t=3, b=6):

Add 3. sum=13. heap size 3.

current_pleasure=13*6=78. max is 78.

Fourth song (t=15, b=1):

Add 15. sum=28. heap size 4>3. Pop smallest (3). sum=25.

current_pleasure=25*1=25. Max remains 78.

So the output is 78, which matches the example.

Second example:

5 3

Songs:

12 31

112 4

100 100

13 55

55 50

Sorted by b in descending order:

100 100 (b=100)

55 50 (b=50)

13 55 (b=55? Wait, wait the original input is:

Wait, the input lines are:

12 31

112 4

100 100

13 55

55 50

So the fifth line is 55 50 (b=50).

Wait, the third song is 100 100 (b=100).

The fourth song is 13 55 (b=55).

Fifth is 55 50 (b=50).

So when sorted by b in descending order:

100 (b=100) comes first.

Then 55 (song with b=55) is next (13 55).

Then 55 50 (b=50) and 12 31 (b=31), then 112 4 (b=4).

So the sorted list is:

100 100 (b=100)

13 55 (b=55)

55 50 (b=50)

12 31 (b=31)

112 4 (b=4)

k=3.

Processing each:

First song (t=100, b=100):

sum=100. heap size 1. 100*100=10000. max is 10000.

Second song (t=13, b=55):

sum=113. heap size 2. 113 *55=6215. which is less than 10000. So max remains.

Third song (t=55, b=50):

sum=113+55=168. heap size 3. 168*50=8400. Still less than 10000.

Fourth song (t=12, b=31):

sum would be 168+12=180. heap size 4>3. Pop smallest, which is 13. sum=180-13=167.

167 *31=5177. Less than 10000.

Fifth song (t=112, b=4):

sum=167+112=279. heap size 4>3. Pop 12 (since heap is a min-heap and after adding 112, the heap has elements 55,100,112, which are the largest? Wait, no. Wait, the heap is a min-heap. Let's think: the first three elements are 100,13,55. Wait, no. Wait, when you add elements to the heap, the heap maintains the smallest at the top, but the structure allows for the min to be popped.

Wait, let's track the heap step by step.

First song: add 100. heap is [100]. sum=100.

Second song: add 13. heap becomes [13,100], but since it's a min-heap, the smallest is at the top. Then, since size is 2 <=3, sum is 113. When the third song is added (55), the heap has 13,100,55. The sum is 113+55=168. Then, when processing the fourth song (t=12), sum becomes 168+12=180. Heap size is 4, so we pop the smallest element (12?), wait wait. Wait, when we add 12, the heap now has 13,100,55,12. But the heap structure is a min-heap. The heap will now have 12 as the root. So when we pop, we remove 12. sum becomes 180-12=168. The heap now contains 13,55,100. Sum is 168. Then multiply by 31 gives 168*31=5208.

Wait, but in the example, the correct answer is 10000, which is achieved by taking just the third song (100 100). So in this approach, when processing the first song, the sum is 100 *100=10000, which is the maximum. So the code works here.

So this approach seems to handle both examples correctly.

Now, the algorithm's time complexity: sorting the n songs is O(n log n). Then, for each song, we perform heap operations (heappush and possibly heappop). Each of these operations is O(log k), and since we have n elements, the total heap operations are O(n log k). So overall time complexity is O(n log n + n log k), which for n up to 3e5 is acceptable.

Now, how to implement this in Python.

But wait, Python's heapq is a min-heap. So when we add elements, the smallest is popped when the heap exceeds size k. This way, the heap always contains the largest k elements so far.

Wait, because when you have a min-heap, the smallest element is at the top. So, if the heap's size is k, adding a new element and then popping the top (smallest) would keep the k largest elements.

For example, suppose we have elements [5, 3, 7] and k=3. The heap would be [3,5,7]. If we add 2, the heap becomes [2,3,5,7]. Then, since size is 4, we pop 2. So the heap becomes [3,5,7], which are the three largest elements. Then, adding a 6, the heap becomes [3,5,6,7]. Pop 3, so the heap is [5,6,7], which are the three largest.

Wait, no. Wait, the min-heap's structure doesn't keep the elements in sorted order. The only guarantee is that the parent is less than or equal to children. So the root is the smallest. When you add elements, the heap structure is maintained. So when you have a min-heap, when you push elements, the heap's root is the smallest. So when you add a new element, the heap will adjust to have the new element in the correct place.

But the logic is that the heap contains the largest k elements, but stored in a min-heap. So the smallest of those k elements is at the top. So when a new element is added, if it's larger than the smallest in the heap, then the smallest is popped, and the new element is added, maintaining the size k. If it's smaller, then the heap remains the same. This way, the sum is the sum of the largest k elements.

Wait, yes. For example, the current heap has the k largest elements. When a new element comes in, if it's larger than the smallest in the heap (the root), then adding it to the heap and then popping the root (the previous smallest) keeps the sum of the k largest. If the new element is smaller than the root, then adding it to the heap would make it have k+1 elements, but when we pop the root (the smallest), the new element is part of the heap. Wait, no. Wait, if the heap has size k and contains elements a1 (smallest), a2, ..., ak (all larger than a1). When adding a new element x. If x < a1, then after adding, the heap has k+1 elements. The root is a1. Then, we pop a1, and the new heap's root is the next smallest, which could be x. So the sum would have included x, but that's wrong. Because x is smaller than a1. So in that case, the sum would be (sum of the previous elements) - a1 + x, which is worse. Wait, but that's not what we want. We want to keep the largest k elements. So in that case, adding x (which is smaller than all elements in the heap) and then popping the root (which is a1, the previous smallest) would leave the heap with x and the other elements. But x is smaller than a1, so that's incorrect.

Wait, that's a problem. Oh wait, no. Wait, the heap is storing the largest elements. For example, the current heap has the k largest elements. When a new element comes in, if it's larger than the smallest in the heap (a1), then we add it, and remove a1, keeping the k largest. If it's smaller than a1, then the k elements in the heap are all larger than x, so adding x and then removing a1 would leave x in the heap, but x is smaller than a1. So that's a problem.

Ah, right! So this approach would not work as intended. Because the min-heap is supposed to keep the largest k elements. However, when a new element is smaller than the current minimum of the heap, adding it and then popping the minimum would replace the current minimum (which is a1) with x (which is smaller), leading to a smaller sum. Which is not desired.

So this approach is incorrect. Oh no! So what's wrong here?

Wait, let's think of an example. Suppose k is 3. Current heap has elements [5, 6, 7], which sum to 18. The next element is 4, which is smaller than the current minimum (5). If we add 4 to the heap, making [4,5,6,7], then pop the minimum (4), the heap becomes [5,6,7], sum is 18. Which is correct. But if the next element is 3, adding it would result in sum 18 again. So that's okay.

Wait, perhaps the approach is correct. Because if the new element is smaller than the current minimum of the heap, then the heap after adding and popping would remain the same. Because when you add the new element, the heap's size becomes k+1, so you pop the smallest, which is the new element. So sum remains the same.

Wait, that's possible. Let's see:

Heap has [5,6,7]. Sum is 18.

Add 4. Heap becomes [4,5,6,7]. Pop 4. Sum is 5+6+7=18. So sum remains the same. Correct.

Add 3: heap is [3,5,6,7]. Pop 3. Sum remains 18.

So in this case, even if the new element is smaller than all elements in the heap, adding it and then popping the new element (since the heap size is k+1) leaves the heap as before, sum unchanged. So the sum remains the sum of the largest k elements.

Ah! So the approach is correct. Because whenever we add a new element to the heap, if the heap's size exceeds k, we pop the smallest element (the root). So the heap after processing each element will always contain the largest k elements (so far), with the smallest of those elements at the root.

Thus, even when adding elements smaller than the current root, they are added to the heap, but then immediately popped (since the size becomes k+1), so the heap remains as before. Thus, the sum is maintained correctly as the sum of the largest k elements.

So the approach is correct. Therefore, the code is as follows:

Sort the songs in descending order of beauty.

Initialize a min-heap, and a sum variable.

Initialize max_pleasure to 0.

For each song in the sorted list:

   add t_i to the heap.

   sum += t_i

   if len(heap) > k:

       popped = heappop(heap)

       sum -= popped

   current_pleasure = sum * b_i

   if current_pleasure > max_pleasure:

       max_pleasure = current_pleasure

At the end, output max_pleasure.

Yes. So this code works.

Now, in Python, using heapq.

But note that in Python, the heapq module only provides a min-heap. So when adding elements, the heap will maintain the smallest element at the front.

So, the code should be:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    songs = []
    for _ in range(n):
        t, b = map(int, input_stream.readline().rstrip("\n").split())
        songs.append( (-b, t) )  # sort in descending order of b, so store as -b for min-heap

    songs.sort()

    max_pleasure = 0
    heap = []
    sum_t = 0

    for neg_b, t in songs:
        b = -neg_b
        heapq.heappush(heap, t)
        sum_t += t
        if len(heap) > k:
            popped = heapq.heappop(heap)
            sum_t -= popped
        current_pleasure = sum_t * b
        if current_pleasure > max_pleasure:
            max_pleasure = current_pleasure

    print(max_pleasure, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
12 31
112 4
100 100
13 55
55 50
""",
            "output": \
"""\
10000
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

Second example:

Sorted list after sorting by -b:

(-100,100), (-55,13), (-50,55), (-31,12), (-4, 112)

Processing each:

First song: t=100, b=100. heap [100], sum=100. pleasure 100*100=10000. max is 10000.

Second song: t=13, b=55. add to heap. heap [13,100], sum 113. 113*55=6215. max remains.

Third song: t=55, b=50. sum becomes 113+55=168. heap size 3. sum*50=8400. less than 10000.

Fourth song: t=12, b=31. add to heap. sum 180. heap size 4. pop 12 (min of [12,13,55,100]). sum 168. current_pleasure=168*31=5208. max still 10000.

Fifth song: t=112, b=4. add to heap. sum 168+112=280. heap size 4+1=5? Wait, after adding 112 to heap, which has elements [12 (popped before?), 13,55,100]? Or perhaps the heap after the fourth song is [13,55,100], sum 168. Then adding 112: sum becomes 168+112=280. heap size 4>3. Pop 13. sum becomes 280-13=267. current_pleasure=267*4=1068. So max remains 10000.

So the code returns 10000, which is correct.

So this code should work.

Now, for handling the data, we need to read n and k, then n lines of t and b. We sort the songs by -b, and then process each as described.

In Python, the code would be as written.

But need to be cautious with the data types. The t and b can be up to 1e6, and multiplied by k (up to 3e5), sum could be 3e11. So in Python, integers can handle that.

So the code should work correctly.
</think>

```python
import heapq

n, k = map(int, input().split())
songs = []
for _ in range(n):
    t, b = map(int, input().split())
    songs.append((-b, t))  # Sort by descending beauty

songs.sort()

max_pleasure = 0
heap = []
sum_t = 0

for neg_b, t in songs:
    b = -neg_b
    heapq.heappush(heap, t)
    sum_t += t
    if len(heap) > k:
        removed = heapq.heappop(heap)
        sum_t -= removed
    current = sum_t * b
    if current > max_pleasure:
        max_pleasure = current

print(max_pleasure)
```
