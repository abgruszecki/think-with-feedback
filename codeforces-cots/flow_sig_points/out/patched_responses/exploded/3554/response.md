<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So the problem is about a spinning arrow pointing to a sector, and we need to find which sector's question will be chosen next. The rules are: if the arrow points to a sector that hasn't been asked (ai=1), then that's the chosen one. Otherwise, we need to check the next sectors in clockwise order until we find one that's unanswered. The sectors are arranged in a circle, so after the nth comes the first again.

The input gives the list of sectors, their statuses (0 or 1), and the initial sector k. Wait, but wait: the problem statement says "number of the sector where the arrow is pointing." But sectors are numbered from 1 to n. So the first input is n and k (the sector the arrow points to). The second line is a list of a_1 to a_n, where a_i is 0 or 1.

The output is the number of the sector that will be selected. So the task is to find the first sector starting from k, then k+1, ..., n, then 1, 2, etc., that has a_i=1.

So for example, the first sample input is:

5 5
0 1 0 1 0

The sectors are 1 to 5. The arrow points to sector 5. Check if a_5 is 1. It's 0, so move to next. The next is 1 (since after 5 comes 1). a_1 is 0. Next is 2. a_2 is 1, so output 2.

Another example: input is 2 1, with both sectors being 1. So arrow points to 1, which is unasked. So output 1.

So the approach is to iterate through the sectors starting from k, moving clockwise (i.e., increasing index, wrapping around), and return the first index where a_i is 1.

But the sectors are 1-based. So how to handle the indices? Let's see: the input is given as a list where the second line is a_1 to a_n. So for the initial position k (1-based), we need to check the elements in the order k, k+1, ..., n, 1, 2, etc.

Wait, but the array is 0-based in Python. So if k is given as 5, the index is 4 (since 0-based). Then, starting from index 4, check each element. If the element is 1, return its 1-based index. Otherwise, proceed to next, wrapping around.

So the algorithm is:

Loop from the starting index (k-1) to the end, then from 0 to k-2, and check if a[i] is 1. The first such i is the answer, converted to 1-based.

But how to loop in the order of k, k+1, ..., n, 1, 2, ...?

In terms of indices (0-based), the starting index is (k-1). Then, the next index is (k) mod n, then (k+1 mod n), etc. So for example, if k is 5 (1-based) in a 5-element array, the starting index is 4. Then indices 4, 0, 1, 2, 3, 4, etc.

Wait, no. Wait, the sectors are arranged in a circle. So when you start at k, and move clockwise, the next sector is k+1, but after n comes 1. So in 0-based terms, the indices go: start at s = k-1. Then next is (s + 1) % n, then (s+2) %n, etc., until we loop back to s.

But in code, how to do this? Because we need to check each index starting from s, then s+1 mod n, etc., until we find a 1.

So the code can loop from offset 0 to n-1. For each i in 0..n-1, compute (s + i) % n. Check a at that index. The first one that is 1 is the answer.

Yes. Because starting from s, the next is s+1 mod n, etc. So for i from 0 to n-1, the position is (s + i) mod n. For example:

s is 4 (k=5 in 5 elements), i ranges 0 to 4:

i=0: 4+0=4 mod5=4 → check a[4] → 0.

i=1: 4+1=5 mod5=0 → check a[0] → 0.

i=2: 4+2=6 mod5=1 → check a[1] →1. So return 1+1=2 (1-based).

So that's correct.

So the code steps:

1. Read n and k. Then read the list of a's.

2. Convert k to 0-based index: s = k-1.

3. For i in 0 to n-1:

   a. pos = (s + i) % n

   b. if a[pos] is 1 → return pos+1 (converted to 1-based)

Because the problem guarantees that there's at least one 1, so we don't need to handle the case where all are 0.

So the code in Python would be:

Read n and k from input. Then read the list of a's (as integers). Then loop i from 0 to n-1, compute (s + i) mod n, check a[pos]. When found, print pos+1.

This approach is O(n) time, which is acceptable for n up to 1000. Since 1000 is very small, even O(n^2) would be okay, but O(n) is optimal.

Now, the code:

Read the input:

First line: n and k.

Second line: list of n integers.

But in Python, the second line can be read as a list via list(map(int, input().split())).

So the code:

n, k = map(int, input().split())
a = list(map(int, input().split()))
s = k -1  # 0-based start index

for i in range(n):
    pos = (s + i) % n
    if a[pos] == 1:
        print(pos +1)
        exit()

But since the problem says the answer exists, we don't need to handle the case where nothing is found.

Testing first sample:

Sample 1:

n=5, k=5 → s=4.

a = [0,1,0,1,0]

Loop i from 0 to 4:

i=0: pos=4 → a[4] is 0 → no.

i=1: pos=5 mod5=0 → a[0] is 0 → no.

i=2: 4+2=6 mod5=1 → a[1] is 1 → output 2.

Which matches the sample.

Second sample:

n=2, k=1 → s=0.

a = [1,1]

i=0: pos=0 → a[0] is 1 → output 1.

Which is correct.

Another test case: n=3, k=2. a = [0,0,1]. Then s=1. i=0 → pos1 (a[1]=0), i=1 → pos2 (a[2]=1 → output 3.

So code seems correct.

Now, code needs to read input correctly and output.

So the code is straightforward.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
start = k - 1
for i in range(n):
    pos = (start + i) % n
    if a[pos] == 1:
        print(pos + 1)
        break
```