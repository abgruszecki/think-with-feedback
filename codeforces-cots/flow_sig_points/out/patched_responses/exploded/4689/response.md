<think>
Okay, let's see. The problem is that we have a list of badges with certain coolness factors, and we need to make all of them unique by increasing them (since we can't decrease, right?), and find the minimum cost. The cost is the sum of the increments. Hmm.

So the main idea here is to sort the array and then adjust each element to be at least one more than the previous. Because if we sort them in non-decreasing order, then each next element must be at least previous +1. That way, all elements are unique and in order. But how do we calculate the minimum cost efficiently?

Let me think of an example. Like the first sample input: 1,3,1,4. When sorted, it's 1,1,3,4. The first element is 1. The second must be at least 2. So we increase it by 1 (cost 1). Then third is 3, which is already higher than 2, so no change. Fourth is 4, higher than 3. Total cost is 1. That's correct.

Another example: 1,2,3,2,5. Sorted: 1,2,2,3,5. So first is 1. Second must be at least 2. It's already 2. Third needs to be at least 3. So increase by 1 (cost 1). Fourth must be at least 4. Current is 3, so increase by 1 (cost 1). Fifth is 5 which is okay. Total cost is 2. That matches the sample.

So the approach is:

1. Sort the array in non-decreasing order.
2. Iterate through the sorted array, and for each element starting from the second, if it's less than or equal to the previous element, set it to previous + 1. The difference between new value and original adds to the cost.

Wait, but what if there are multiple duplicates in a row? Like 2,2,2. The first stays 2. The second becomes 3 (cost +1). Third must be at least 4 (cost +2). Total cost 3. Which is correct.

So the algorithm seems straightforward: sort, then adjust each element to be max(current, previous +1), and accumulate the difference between new value and original.

But how to implement this efficiently?

Let's consider the steps:

- Sort the array. That's O(n log n) time, which is acceptable for n up to 3000. Since 3000 log 3000 is way less than even 1e5 operations, this is feasible.

Then, iterate through the sorted array, keeping track of the previous value.

Wait, but the sorted array is modified as we go. For example, after sorting, the array is [a0, a1, a2, ...], and we process each element in order. For each a[i], we set it to max(a[i], a[i-1] + 1). The difference (a[i] after - a[i] before) is added to the total cost.

Yes. So for each element i from 1 to n-1:

current = sorted_array[i]

prev = sorted_array[i-1]

if current <= prev:

   new_val = prev + 1

   cost += (new_val - current)

   sorted_array[i] = new_val

else:

   do nothing.

But how does this affect subsequent elements? Because after modifying a[i], the next a[i+1] has to be compared to the modified a[i]. So this has to be done in a sequential manner.

So the steps are:

Sort the array.

Initialize cost to 0.

prev = sorted_array[0]

for i from 1 to n-1:

   current = sorted_array[i]

   if current <= prev:

       new_val = prev + 1

       cost += (new_val - current)

       prev = new_val

   else:

       prev = current

   sorted_array[i] is updated to new_val or remains current.

So, for example, in the first iteration, after processing the second element (i=1), the prev is updated, and the next elements compare against that.

This should ensure that each element is at least one more than the previous.

So the approach is correct.

Now, the code.

In Python, we can sort the list, then iterate, keeping track of the previous element. For each element, compute the required new value.

Let's test the code with the sample inputs.

First sample input:

4

1 3 1 4

After sorting: [1,1,3,4]

i=1 (second element, 1):

prev is 1. current is 1. new_val is 2. cost += 1. prev becomes 2.

i=2 (third element, 3):

prev is 2. current 3 is greater, so no change. cost remains. prev becomes 3.

i=3 (fourth element,4): 4>3. No change. Cost total is 1.

Which matches the first sample.

Second sample input:

5

1 2 3 2 5 → sorted as [1,2,2,3,5]

i=1: current is 2. prev is 2 → new_val 3. cost +=1. prev 3.

i=2: current is 2. prev is 3 → new_val 4. cost += (4-2)=2. total 3? Wait wait sample output is 2.

Wait wait. Wait the sample input after sorting is 1, 2, 2, 3,5. Let's process:

i=0: prev =1.

i=1: current 2. prev is 1. So 2 is okay. prev becomes 2.

i=2: current 2. prev is 2. new_val 3. cost +=1. prev becomes 3.

i=3: current 3. prev is 3 → new_val 4. cost +=1 (4-3=1). Total cost 2.

i=4: current 5 >=4 → no change. So total cost 2. Which matches the sample. So the code works.

So the code logic is correct.

Thus, the code would be:

Read n.

Read the list as a.

Sort a.

if n is 1, output 0.

else:

cost =0

prev = a[0]

for i in range(1, n):

    current = a[i]

    if current <= prev:

        need = prev +1

        cost += need - current

        prev = need

    else:

        prev = current

return cost.

Yes.

Now, in code.

In Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    a.sort()

    cost = 0

    prev = a[0]

    for i in range(1, n):

        current = a[i]

        if current <= prev:

            need = prev +1

            cost += need - current

            prev = need

        else:

            prev = current

    print(cost, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2 3 2 5
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

Sample 2:

5 numbers sorted [1,2,2,3,5]. Processing:

i=1: 2 <=2 → need 3. cost +=1. prev 3.

i=2: current 2 (original) but after sorting, in the list, the third element is 2. But after i=1, prev is 3. So current is 2. 2 <=3 → need 4. cost +=4-2=2. prev becomes4.

i=3: current 3. <=4 → need 5. cost +=5-3=2. prev 5.

Wait wait. Then the code would output 1+2+2=5? But the sample output is 2.

Wait wait, what's wrong here. Wait the second sample input is 1,2,3,2,5. After sorting, it's 1,2,2,3,5.

Processing:

i=1 (element 2). prev is 1. current is 2. 2>1. So no cost. prev becomes2.

i=2: current 2. prev is 2. need 3. cost +=1. prev becomes3.

i=3: current 3. prev is3. need4. cost +=1. total 2.

i=4: current5>4. no cost. So total cost is 1+1=2. Which matches sample.

Ah right, the code for the second sample:

After sorting, the array is [1,2,2,3,5]

i=1 (element 2):

prev is 1. current is 2. 2>1 → prev becomes 2. cost 0.

i=2 (element 2):

current 2 <= prev 2. need 3. cost +=1. prev 3.

i=3 (element3):

current3 is <=3? No. prev is3. current3 is equal. So need4. cost +=4-3=1. total 2. prev4.

i=4: current5>4 → no cost. So total 2.

Yes. So the code works.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
cost = 0
prev = a[0]
for i in range(1, n):
    current = a[i]
    if current <= prev:
        need = prev + 1
        cost += need - current
        prev = need
    else:
        prev = current
print(cost)
```
