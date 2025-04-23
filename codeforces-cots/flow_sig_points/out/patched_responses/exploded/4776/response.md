<think>
Okay, let's see. I need to solve this problem where for each element in an array, I have to output the sum of itself and the previous element. But for the first element, it's the sum of the first and last elements. Hmm.

So the input is a list where the first number is n, followed by n integers. The output should be a new array where each position i (starting from 0 maybe?) is the sum of a[i] and a[i-1]. Except for the first element, which is a[0] + a[-1] (the last element).

Let me think about the steps. Let's take the first example: input is 4 1 2 3 4. So n is 4, array is [1,2,3,4]. The output is 5 (1+4), 3 (2+1), 5 (3+2), 7 (4+3). So the first element's sum is with the last, then each subsequent element is added with the previous.

So for each index i in 0 to n-1:

if i is 0, sum is array[0] + array[-1]

else, sum is array[i] + array[i-1]

So the algorithm is straightforward. For each element in the array, calculate the sum as described. Then collect all those sums and output them separated by spaces.

But how do I handle the array? Let's see. Let's parse the input. The input line is split into integers. The first is n, then the next n are the array elements.

So in code:

Read the input line, split into parts. The first element is n. The array is the next elements.

Then create a result list. For each i in 0 to n-1:

if i is 0: res[i] = a[0] + a[-1]

else: res[i] = a[i] + a[i-1]

Wait, but the array indices: the first element is at 0, the last at n-1. So yes.

So for the first element (i=0), sum with a[-1], which is the last element.

Then for i from 1 to n-1, sum a[i] and a[i-1].

So the code would be something like:

n, *rest = map(int, input().split())

array = rest[:n]

result = []

for i in range(n):

    if i == 0:

        sum_val = array[0] + array[-1]

    else:

        sum_val = array[i] + array[i-1]

    result.append(str(sum_val))

print(' '.join(result))

Wait, but in Python, the array is zero-based, so yes. Let's test this with the first example.

Sample input 4 1 2 3 4. array is [1,2,3,4]. For i=0: 1 +4 =5. Then i=1: 2+1=3, i=2:3+2=5, i=3:4+3=7. So output 5 3 5 7. Which matches the sample. So that's correct.

Another sample: input 5 5 46 372 81 9. Array is [5,46,372,81,9]. The first element is 5 +9=14. Then 46+5=51, 372+46=418, 81+372=453, 9+81=90. So output is 14 51 418 453 90. Which matches the sample.

So this approach should work.

Now, what about the constraints? The n is up to 50. So even if n is 50, the algorithm is O(n), which is trivial. So no performance issues here.

So the code is straightforward. Now, in terms of code optimization, perhaps we can precompute the first element and then loop from 1 to n-1. But the code as written is simple and efficient enough.

What about memory? The array is small, up to 50 elements. So no problem.

So the code should be:

Read the input line, split into integers.

The first integer is n. The rest are the array elements. So we take the first n elements of the rest.

Then compute the result as described.

So code in Python:

n, *rest = map(int, input().split())

arr = rest[:n]

res = [arr[0] + arr[-1]]

for i in range(1, n):

    res.append(arr[i] + arr[i-1])

print(' '.join(map(str, res)))

Wait, that's even better. For the first element, compute it, then loop from 1 to n-1. So the code is a bit more optimized, but same O(n) time.

Yes. So this should work.

Testing the first sample: arr is [1,2,3,4]. res starts as 1+4=5. Then for i=1: 2+1=3 added. i=2:3+2=5. i=3:4+3=7. So [5,3,5,7], joined as '5 3 5 7'.

Another sample: [5,46,372,81,9]. res starts with 5+9=14. Then i=1:46+5=51. i=2:372+46=418. i=3:81+372=453. i=4:9+81=90. So [14,51,418,453,90], which is correct.

So this code should work.

Now, make sure that the input is read correctly. The input is a single line of space-separated integers, with the first being n. So the code n, *rest = map(int, ...) will correctly split into n and the rest. Then arr is the first n elements of rest, which is correct.

Edge cases: n=2. For example, input 2 10 20. Output would be 10+20=30, 20+10=30. So output '30 30'.

Another edge case: all elements same, e.g., 3 5 5 5. Output is 5+5=10, 5+5=10, 5+5=10. So '10 10 10'.

So code handles that.

So the code seems correct.
</think>

```python
n, *rest = map(int, input().split())
arr = rest[:n]
result = [arr[0] + arr[-1]]
for i in range(1, n):
    result.append(arr[i] + arr[i-1])
print(' '.join(map(str, result)))
```