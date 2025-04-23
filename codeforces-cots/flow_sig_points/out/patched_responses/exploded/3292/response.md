<think>
Okay, let's tackle this problem. So, the problem is about scheduling video recompression on servers. We have n videos arriving at different times, each needing m seconds of processing (since each minute is a second, so m minutes becomes m seconds). The servers are all the same, and each can handle one video at a time. The goal is to find for each video when it finishes processing.

Hmm. Let's think about how to model this. The key points here are that the videos are processed in the order they arrive. So even if a video arrives at time s, if all servers are busy, it has to wait until a server becomes available. And once a server is free, it picks up the next video in the queue.

Wait, but the servers are all the same. So the way to model this is to track when each server becomes available. For example, if we have k servers, each starts available at time 0. When a new video comes in, we check which server is available the earliest. But since the videos are processed in order, each video is assigned to the earliest available server at the moment when it's processed.

Wait no. Because the servers could be busy when the video arrives. So for each video, the processing starts at the maximum between its arrival time and the earliest available server time. Then, the server's next available time is start_time + m_i (since m_i is in minutes, but each minute takes 1 second to process). Wait, no: the problem statement says that each server takes m seconds to recompress a m minute video. So a video of m minutes requires m seconds of processing time. So the processing time is m seconds.

So for each video, the start time is the maximum between the time when the video arrives (s_i) and the earliest available server time. Then, the server's available time is updated to start_time + m_i.

But how to efficiently manage the servers' availability? Since the number of servers can be up to 5e5, but the number of videos is also up to 5e5. So we need an efficient way to track which server is available the earliest.

Wait, but the servers can be modeled using a priority queue (min-heap). The heap would contain the next available times of each server. For each video, we check the earliest available server. If the earliest time is less than or equal to s_i, then the server is available at s_i. So the start time is s_i. Otherwise, the server is busy, so the start time is the server's available time.

Wait, but the servers are processed in the order of their availability. So for each video, we can check the smallest available time from the heap. If that time is <= s_i, then this server can start processing the video at s_i. Otherwise, the server's available time is later than s_i, which means the video has to wait until that server is free. But since the servers are ordered in the heap, the earliest available server is always the one that can process the video first.

Wait, but when a new video arrives, we need to assign it to the earliest possible server. So the approach would be:

- Maintain a min-heap that keeps track of the available times of the servers.
- For each video in order:
   - Pop the server with the earliest available time.
   - The start time for this video is max(s_i, server's available time).
   - The end time is start_time + m_i.
   - Record this end time as the answer for the video.
   - Push the new available time (end time) back into the heap.

This works because each time we assign the video to the server that becomes available the earliest. Since the videos are processed in the order they arrive, this approach ensures that each video is handled as early as possible.

But what if the number of servers k is larger than the number of videos? Then, each video is handled immediately when they arrive, since there are enough servers. So the start time is s_i, end is s_i + m_i.

The problem with this approach is the time complexity. For each of the n videos, we perform two heap operations (pop and push). Since each heap operation is O(log k) time, the total time is O(n log k). With n up to 5e5, this would be acceptable as 5e5 * 20 (approx log2(5e5) is about 19) is around 1e7 operations, which should fit within the 3-second time limit.

So the plan is:

1. Initialize a min-heap with k zeros (each server's available time starts at 0).
2. For each video in order:
   a. Pop the smallest available time from the heap.
   b. Compute the start time as max(s_i, available_time).
   c. The end time is start_time + m_i.
   d. Push the end time back into the heap.
   e. Record end time as the answer for this video.

This should work. Let's test it against the examples.

First example:

3 2

1 5 → s=1, m=5. The heap has [0,0]. Pop 0. start_time is max(1,0)=1. end is 6. Push 6. Answer is 6.

Second video: s=2. Heap now has [0,6]. Pop 0. start is max(2,0)=2. end 7. Push 7. Answer is 7.

Third video: s=3. Heap has [6,7]. Pop 6. start is max(3,6) →6. end 6+5=11. Push 11. So answers are 6,7,11. Which matches the sample.

Another example:

6 1. So heap starts with [0].

First video: s=1, m=1e9. Pop 0. start max(1,0)=1. end 1+1e9 = 1e9+1. Push that. Answer is 1e9+1.

Second video: s=2. Heap has [1e9+1]. Pop it. start is 1e9+1. end is 1e9+1 +1e9 = 2e9+1. Answer. Then push.

Third: s=3. Heap has [2e9+1]. Pop, start is 2e9+1. end 3e9+1. Etc. Each subsequent adds 1e9. The sixth video is s=6, m=3. When it arrives, the server is available at 5e9+1 (from the fifth video). So start is 5e9+1. End is 5e9+1 +3 =5e9+4. Which matches the sample.

So this approach works for the examples.

Now, implementing this in Python.

But wait, for k up to 5e5, initializing the heap with k zeros could be a problem. Because in Python, the heapify function is O(k), but with k up to 5e5, that's acceptable. Wait, 5e5 is manageable. Heapify is O(n), so 5e5 elements would take O(5e5) time. Then, for each of the n elements, two heap operations (each O(log k)), which is O(n log k) time.

So the steps are:

Read n and k.

Then read n lines, each with si and mi. But the input is given in the order of increasing si, so no need to sort.

We need to process each video in order, so we can read them one by one.

But for the initial heap, if k is larger than n? Like, if there are 1e5 servers and 5e5 videos, but wait, n and k are up to 5e5 each. So even if k is 5e5, initializing the heap with k elements is O(k), which is 5e5 steps.

But in Python, using a heap with 5e5 elements is manageable, but inserting all of them might take some time. Wait, in Python, the heap is a list. So for k elements, we can create a list of zeros and then heapify it. But heapify is O(k), which for 5e5 is okay.

So code steps:

Read n and k.

Then, create a heap with k elements, all 0. Then heapify.

Then for each video, do:

current_s, current_m = read the pair.

available_time = heappop(heap)

start = max(current_s, available_time)

end = start + current_m

print(end)

heappush(heap, end)

But wait, the order in which the videos are processed is correct. Because each video is handled in the order they appear, which is given in the input. So we process each video one by one, in the input order.

Yes.

Now, the problem is that for large k (like k=5e5), the initial heap is 5e5 elements. In Python, creating a list of 5e5 elements and heapifying it is feasible. But in practice, when k is large and n is small (like n=1, k=5e5), we need to pop the first element (0), then push back end, but the rest of the heap remains with 5e5-1 elements, which are all 0. So in that case, the next pop would take O(1) time (since the heap is a min-heap and the next element is 0 again). But the heap operations would be O(log k), which for k=5e5, log2(5e5) is around 19, which is manageable.

Another thing to note is that the initial heap contains k elements. Each video is processed by taking the smallest available time. So when the number of servers is larger than the number of videos, each video can be processed as soon as it arrives. So for example, if we have 100 servers and 10 videos, each video is processed at s_i, since the available_time is 0 (from the initial heap), and s_i is >=0 (since all s_i are at least 1). So start is s_i, end is s_i + m_i.

This approach seems correct.

Now, considering the constraints. For n=5e5 and k=5e5, each heappop and heappush is O(log k) time. So total time is O(n log k) = 5e5 * 20 ≈ 1e7 operations, which is acceptable.

But in Python, for 1e7 operations, each being a heappop and heappush, which are O(1) per operation (but with the log factors), it's possible that it's tight. However, given that Python is efficient enough for such operations, this should be manageable.

Now, the code.

In Python, using heapq.

But the initial heap needs to be filled with k zeros. So:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    # Initialize the heap with k zeros
    heap = [0]*k
    heapq.heapify(heap)

    for _ in range(n):
        s, m = map(int, input_stream.readline().rstrip("\n").split())
        available = heapq.heappop(heap)
        start = max(s, available)
        end = start + m
        print(end, file=output_stream)
        heapq.heappush(heap, end)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 1
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000
6 3
""",
            "output": \
"""\
1000000001
2000000001
3000000001
4000000001
5000000001
5000000004
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

Another test case: when k is 1 and n is 6, as in the second sample.

The heap starts with [0].

First video: s=1, m=1e9.

available=0. start=1. end=1+1e9. print 1e9+1. Push.

Second video: s=2. available is 1e9+1. start is that. end= 1e9+1+1e9 = 2e9+1. etc.

So the code works.

Now, what about the case where k is 5e5 and n is 5e5. Then each video is assigned to a separate server. So the end time for each is s_i + m_i. Because when the server is popped (available time 0), s_i >=0, so start is s_i. So the code would output s_i + m_i for all.

Yes.

But what about the scenario where videos arrive when all servers are busy. For example, servers=2, and three videos arrive at time 0, 0,0. No, wait the input says that all s_i are distinct. So the code can rely on s_i being in increasing order. Wait, the problem statement says that the videos are given in order of increasing s_i. So the code can process them in the order given.

Thus, the code should handle all cases correctly.

Now, the code must read input efficiently. For n up to 5e5, using input() each time can be slow in Python. So it's better to read all input at once.

But how?

In Python, for large n, using sys.stdin.readline() is better. But even better is to read the entire input at once and split it.

So modifying the code:

import sys, heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr +=1
    k = int(input[ptr])
    ptr +=1

    heap = [0]*k
    heapq.heapify(heap)

    for _ in range(n):
        s = int(input[ptr])
        ptr +=1
        m = int(input[ptr])
        ptr +=1
        available = heapq.heappop(heap)
        start = max(s, available)
        end = start + m
        print(end)
        heapq.heappush(heap, end)

if __name__ == "__main__":
    main()

This way, all input is read at once, split into a list, and processed via pointers, which is faster than reading line by line. This is crucial for large n.

Yes, this should optimize the input reading.

Another optimization is to precompute the outputs into a list and then print them all at once with '\n'.join, but in this code, each end is printed as it's computed. However, for n=5e5, printing 5e5 lines can be slow. So it's better to collect the outputs into a list and then print them all at once.

So modifying the code to collect the outputs in a list and then print them with '\n'.join.

So:

import sys, heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr +=1
    k = int(input[ptr])
    ptr +=1

    heap = [0]*k
    heapq.heapify(heap)
    outputs = []

    for _ in range(n):
        s = int(input[ptr])
        ptr +=1
        m = int(input[ptr])
        ptr +=1
        available = heapq.heappop(heap)
        start = max(s, available)
        end = start + m
        outputs.append(str(end))
        heapq.heappush(heap, end)
    print('\n'.join(outputs))

if __name__ == "__main__":
    main()

This should be much faster for large n, as the print statement is done once instead of n times. Because for 5e5 lines, each print call is expensive. So collecting them into a list and then using a single print is better.

Yes. So this is the optimized code.

So the final code should be as above.
</think>

```python
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    k = int(data[ptr])
    ptr += 1

    heap = [0] * k
    heapq.heapify(heap)
    outputs = []

    for _ in range(n):
        s = int(data[ptr])
        ptr += 1
        m = int(data[ptr])
        ptr += 1
        available = heapq.heappop(heap)
        start = max(s, available)
        end = start + m
        outputs.append(str(end))
        heapq.heappush(heap, end)
    
    print('\n'.join(outputs))

if __name__ == "__main__":
    main()
```
