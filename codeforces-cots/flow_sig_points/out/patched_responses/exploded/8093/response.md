<think>
Okay, let's see. The problem is about forming teams of two students each, where each team must have equal skills. The goal is to find the minimal total number of problems they need to solve (i.e., the sum of increments in their skills) to form all the required teams.

Hmm, the first thing I need to do is figure out how to pair the students optimally. Because the way we pair them will affect the total number of problems required. For example, in the first sample input, the sorted array is [2,3,5,5,10,14]. The pairs chosen were (2,3), (5,5), and (10,14). Wait, no, wait. Wait, the sample explanation says the pairs are (3,4), (1,6), (2,5) based on indices. The original array is [5,10,2,3,14,5]. So the indices are 1-based. So student 3 has 2, student 4 has 3. So pair (2,3) in the sorted array. Then 5 and 5 (indices 1 and 6), and 10 and 14 (indices 2 and 5). Wait, but how does that lead to the sum of 1 +4?

Wait, for the third and fourth students (2 and 3 skills), to make them equal. The third has 2, the fourth has 3. So one of them needs to solve 1 problem. Either 2 becomes 3 (add 1) or 3 becomes 2 (add 1). Wait, no, wait. Wait, if student 3 is 2 and student 4 is 3, then to make them equal, student 3 can solve 1 problem (2+1=3), which adds 1. Or student 4 solves 0 (since 3-3=0, but that's not allowed because you can't decrease skills). So the minimal here is 1.

For the pair (5 and 14), the first student in the pair is 10 (student 2) and the second is 14 (student 5). Wait, no. Wait the pair (2,5) in the problem's explanation refers to indices 2 (10) and 5 (14). Oh right, so 10 and 14. So to make them equal, the 10 needs to become 14 (add 4) or 14 becomes 10 (but that's not allowed because you can't decrease skills). So the minimal here is 14-10=4. So total is 1+0+4=5.

So how did they pair them? The key seems to be that after sorting the array, you pair consecutive elements. Because in the first sample, when you sort the array [2,3,5,5,10,14], the pairs are (2,3), (5,5), (10,14). Wait, but that's not the case here. Wait the sorted array is 2,3,5,5,10,14. So pairing 2 with 3, then 5 and 5, then 10 and 14. Then for the first pair, 3-2=1. For the third pair, 14-10=4. So sum 1+0+4=5. Which matches the sample. So the approach is to sort the array, then pair each two consecutive elements. So the first pair is 0 and 1 (indices in zero-based), the next pair is 2 and 3, etc.

So the strategy is to sort the array, then pair each even index with the next odd index. For example, for n=6, indices 0,1 (first pair), 2,3 (second), 4,5 (third). Then for each pair, the required difference is (a[i+1] - a[i]) for i in even indices, since the second element is larger (since sorted in non-decreasing order). So the sum of all (a[i+1] - a[i]) for i even in the sorted array.

Wait, but in the first sample, the sum is (3-2) + (5-5) + (14-10) = 1+0+4=5. Exactly the sample output.

So the minimal sum is achieved by pairing consecutive elements in the sorted array, taking adjacent pairs, and then summing the differences between the two elements of each pair.

Ah! So the optimal approach is to sort the array, then pair the 1st and 2nd elements, 3rd and 4th, etc., and compute the sum of the differences between each pair.

Why is this the optimal way? Let's think. Suppose we have four elements sorted as a, b, c, d. If we pair a and c, then b and d. Then the sum is (c - a) + (d - b). Alternatively, if we pair a and b, c and d. Then the sum is (b -a) + (d -c). Which is smaller?

Let's compare:

Original approach (adjacent pairs) sum: (b-a) + (d -c) = (b +d) - (a + c).

Alternative pairing sum: (c -a) + (d -b) = (c +d) - (a +b). 

Which is better?

The original approach gives (b +d) - (a +c). Alternative gives (c +d) - (a +b). Let's subtract the two:

Original sum - alternative sum = (b +d - a -c) - (c +d - a -b) = b +d -a -c -c -d +a +b = 2b - 2c.

If the elements are sorted as a <= b <= c <= d, then b <= c. So 2b -2c <=0. So original sum is less than or equal to alternative sum. Therefore, the adjacent pairing is better.

So for four elements, pairing adjacent gives a better or equal sum. Similarly, for more elements, this approach of pairing adjacent after sorting gives the minimal possible sum.

So the algorithm is:

1. Sort the array in non-decreasing order.
2. Pair the elements as (0,1), (2,3), ..., (n-2, n-1).
3. For each pair, add the difference between the second and first (since the array is sorted, the second is larger or equal).
4. Sum all these differences to get the minimal total.

So the steps are straightforward. Now, the code is easy.

So the code will:

- Read n and the list of a_i.
- Sort the list.
- Iterate over even indices (0, 2, 4, etc.), and for each i, take a[i+1] - a[i], sum all these.

For example, in the second sample input: 2 elements [1, 100]. After sorting, they are [1,100]. The sum is 100-1=99, which matches the sample.

So the code is:

Read n.

Read list, sort.

sum =0

for i in range(0, n, 2):

    sum += a[i+1] - a[i]

print sum.

Yes, that's the code.

So the code in Python would be:

n = int(input())
a = list(map(int, input().split()))
a.sort()
res = 0
for i in range(0, n, 2):
    res += a[i+1] - a[i]
print(res)

That's all. It's O(n log n) due to the sorting step, which is acceptable for n up to 100.

Testing the first sample:

Input 6

5 10 2 3 14 5 → sorted becomes [2,3,5,5,10,14]

The pairs are 2-3 (1), 5-5 (0), 10-14 (4). Sum is 5. Correct.

Second sample: sum is 99. Correct.

Another test case: maybe n=4, a=[1,2,3,4]. Pairing (1,2) and (3,4). Sum is (2-1)+(4-3) =1+1=2. Alternatively, pairing (1,3) and (2,4) would be (3-1)+(4-2)=2+2=4. So the adjacent pairs are better.

Thus, the code works.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(0, n, 2):
    total += a[i+1] - a[i]
print(total)
```