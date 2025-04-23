<think>
Okay, let's see. The problem gives us n and k, and a list of numbers. We need to find the output which is one number. Hmm. Let's look at the examples to understand what's going on.

Looking at the first example: n=8, k=5, all ones. The output is 5. Oh right, maybe when you select 5 elements, the sum is 5. But wait, the second example: input is 10 numbers, k=3. The output is 7. Wait, the numbers are 16,8,2,4,512,256,32,128,64,1. Let's see, if you pick the three smallest elements: 1, 2, 4. Their sum is 7. Oh right, maybe the problem is to select k elements such that their sum is as small as possible, but then the output is that sum. But wait the third example: n=5, k=1. The output is 10. Which is the minimum of the list. So yes, the problem is to choose k elements with the smallest sum possible and output that sum.

Wait, but the fourth example: all 6s, k=6. Sum is 6*6=36. So that's the case when you take all elements. So the problem is indeed to select any k elements from the array and find the minimal possible sum of those k elements.

So the solution is straightforward: sort the array in non-decreasing order and take the first k elements' sum.

Wait, that's what the examples suggest. Let's check all examples:

First example: sorted is all ones. Take first 5, sum 5. Correct.

Second example: sorted array is [1, 2,4,8,16,32,64,128,256,512]. Take first 3: 1+2+4=7. Correct.

Third example: sorted array is [10,20,30,46,50]. Take first 1 (k=1) which is 10. Correct.

Fourth example: all 6s, sum 6*6=36. Correct.

Fifth example: same as fourth. So the solution is to sort the array and sum the first k elements.

So the steps are:

1. Sort the array in ascending order.
2. Sum the first k elements.

But wait, the constraints say n can be up to 2200. So even a O(n^2) algorithm is acceptable. But sorting in O(n log n) is definitely okay.

So the code is straightforward. Read n and k, read the list, sort it, sum first k elements, output.

But let's make sure that the input is read correctly. For example, when n is 2200, the list has 2200 numbers. The code needs to read them all.

In Python, reading input can sometimes be a bottleneck. So for handling large inputs, using sys.stdin is better. But for n up to 2200, even using input().split() is manageable. But to be safe, perhaps read via sys.stdin.

But let's check the problem statement. The input is given as two lines: first line n and k, second line the n numbers.

So the code would be:

Read n and k from first line.

Read the list of a_i.

Sort the list, sum first k.

Print the sum.

Yes. Let's code that.

In Python, the code would be:

n, k = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

print(sum(a[:k]))

Wait, but for the case where the list is not exactly n elements? But the problem says that the second line has exactly n elements. So as long as the input is correct, this code works.

Testing the examples:

First example:

8 5

1 1 ... (8 times). Sum 5.

Yes.

Second example: sorted list is as I thought, sum 7.

Third example: sum of first 1 element is 10.

Yes.

Fourth example: sum 6*6=36.

Yes.

So this code should work. But why the problem says to think about data structures and optimal approach? Because for n up to 2200, sorting is trivial. So this code is optimal.

So the answer is as simple as that. I think that's the correct approach.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(sum(a[:k]))
```