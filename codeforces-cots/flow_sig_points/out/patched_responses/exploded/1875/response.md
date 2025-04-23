<think>
Okay, let's see. So the problem is about Tommy and Banban's lanterns. Tommy wants to hide one of his lanterns such that when Banban picks the best possible pair (from the remaining Tommy's lanterns and his own), the product is as small as possible. But Banban, on the other hand, will pick the pair that maximizes the product. We need to find the final product after both choose optimally.

Hmm. So the approach here is to simulate Tommy's choice of hiding a lantern, and for each possible hidden lantern, compute the maximum product Banban can get. Then Tommy will choose the scenario where this maximum is minimized. So the answer is the minimum of these maximums.

Let me think. So for each i in Tommy's lanterns (a_i), if Tommy hides a_i, then Banban will choose the maximum between all possible pairs (a_j, b_k) where j is not i. But wait, Banban has to choose one lantern from Tommy's remaining and one from his own. So the pair is (a_j, b_k) where j is not the hidden one, and k is any of his own. Then the product is a_j * b_k, and Banban picks the maximum possible product.

So for each possible hidden lantern (each a_i), we need to compute the maximum product possible after excluding that a_i. Then Tommy will choose the hidden lantern which results in the smallest such maximum. The answer is that smallest maximum.

So the steps are:

1. Iterate through each possible lantern in Tommy's list (a) to consider hiding it.
2. For each such scenario, create a list of Tommy's remaining lanterns (excluding the hidden one).
3. For these remaining a's, compute all possible products with each of Banban's b's. Find the maximum product in this case.
4. Among all the maximum products from each possible hiding choice, select the smallest one. That's the answer.

But how to compute this efficiently?

Let's think about the possible a's after hiding one. For each a_i being hidden, we have a list of a's without a_i. Then for each of these lists, we need to find the maximum a_j in the list (if possible) multiplied by the maximum b_k, but wait—it's not necessarily the case. Because the maximum product could be either (max_a * max_b), (max_a * min_b) if min_b is negative, (min_a * max_b) if min_a is negative, etc. So the maximum product depends on the combination of a's and b's.

Wait, right. The maximum product of two arrays can be found by checking the maximum and minimum of each array and considering their products. For example, the maximum product could be the maximum of (max_a * max_b, max_a * min_b, min_a * max_b, min_a * min_b). So for each remaining a's array (after hiding one a_i), we need to compute the max and min of that array, then combine with max and min of Banban's array (since that's fixed) to find the maximum possible product.

So for each remaining a array (after hiding a_i), the possible candidates for the maximum product are the four combinations of the a's max/min and b's max/min. So we can precompute Banban's max and min, and for each remaining a array, compute the max and min of the a's, then compute those four products and take the maximum. That's the maximum product for that scenario.

This approach would be O(n) per a_i. Let's see:

Original a array: n elements. For each a_i, the remaining array has n-1 elements. So for each of the n possible a_i to hide:

- Find the max and min of the remaining a's array. Then compute the four possible products with Banban's max and min.

The maximum of these four is the maximum product Banban can get. Then we take the minimum of all these maximums.

So for each i in a's array:

1. Remove a[i] from the array (but actually, to avoid modifying the array, maybe we can compute the max and min of the array without a[i] each time).

But how to compute the max and min of the array after excluding a[i] efficiently?

Wait, the array a can be up to 50 elements. So for each i, iterating through the array to find max and min excluding a[i] is O(n) per i. Since n is up to 50, this is acceptable. So total steps for all i would be O(n^2), which is 50*50=2500 operations. That's totally manageable.

Similarly for Banban's array, precompute the max and min once.

So the steps are:

- Precompute Banban's max_b and min_b.

- For each a_i in Tommy's array:

   a. Compute the list of a's excluding a_i.

   b. Find the max_a_excl and min_a_excl of this list.

   c. Compute the four possible products: max_a_excl * max_b, max_a_excl * min_b, min_a_excl * max_b, min_a_excl * min_b.

   d. The maximum of these four is the best product Banban can get in this scenario.

- Collect all such maximums for each a_i, and choose the smallest one among them. That's the answer.

Yes, this should work.

Now, how to implement this in Python.

First, read the input: n and m, then the a array, then the b array.

Compute max_b = max(b), min_b = min(b).

Then for each element in a:

   create a list without that element.

   compute max_a_excl and min_a_excl.

   compute the four products.

   take the maximum of those four.

Collect all these maximums, then output the minimum.

But creating a new list each time by excluding a_i can be done by list comprehensions.

But for efficiency, perhaps just loop through the a array each time, skipping the i-th element.

Like for each i in range(n):

   current_max_a = -infinity

   current_min_a = +infinity

   for j in range(n):

       if j != i:

           if a[j] > current_max_a:

               current_max_a = a[j]

           if a[j] < current_min_a:

               current_min_a = a[j]

   Then compute the four products.

This would avoid creating new lists and just iterate through the array each time. For n up to 50, this is acceptable.

Yes. So in code:

Read n, m.

Read a as a list of integers.

Read b as a list of integers.

max_b = max(b)

min_b = min(b)

result = infinity

for i in range(n):

   current_max_a = -inf

   current_min_a = inf

   for j in range(n):

       if j == i:

           continue

       num = a[j]

       if num > current_max_a:

           current_max_a = num

       if num < current_min_a:

           current_min_a = num

   # compute four products

   option1 = current_max_a * max_b

   option2 = current_max_a * min_b

   option3 = current_min_a * max_b

   option4 = current_min_a * min_b

   current_max = max(option1, option2, option3, option4)

   if current_max < result:

       result = current_max

print(result)

Yes. That should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))
    max_b = max(b)
    min_b = min(b)
    result = float('inf')

    for i in range(n):
        current_max = -float('inf')
        current_min = float('inf')
        for j in range(n):
            if j != i:
                num = a[j]
                if num > current_max:
                    current_max = num
                if num < current_min:
                    current_min = num
        option1 = current_max * max_b
        option2 = current_max * min_b
        option3 = current_min * max_b
        option4 = current_min * min_b
        max_option = max(option1, option2, option3, option4)
        if max_option < result:
            result = max_option

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
-1 0 1 2 3
-1 0 1
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

Second example:

n=5, m=3

a: [-1,0,1,2,3]

b: [-1,0,1]

max_b is 1, min_b is -1.

We need to find for each i in 0..4 (hiding each element), compute the max after exclusion.

For example, when Tommy hides 3 (index 4), the remaining a is [-1,0,1,2].

max_a_excl is 2, min_a_excl is -1.

Four options:

2*1=2, 2*(-1)=-2, (-1)*1=-1, (-1)*(-1)=1.

The max of these is 2. Which is the answer.

So the code works here.

Another test case: when a contains negatives and positives.

For example, if a has elements like 3, -4, 5 and b has elements like -2, 6.

max_b is 6, min_b is -2.

If after hiding 5, the a array is [3,-4].

max_a_excl is 3, min is -4.

products: 3*6=18, 3*(-2) =-6, (-4)*6=-24, (-4)*(-2)=8. Max is 18.

But if hiding 3, then a array is [-4,5]. max 5, min -4.

products:5*6=30, 5*-2=-10, -4*6=-24, -4*-2=8. Max is 30.

But the code would take the minimum of all possible maxes.

So this logic should handle all cases correctly.

Therefore, the code should be correct.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_b = max(b)
min_b = min(b)
result = float('inf')

for i in range(n):
    current_max = -float('inf')
    current_min = float('inf')
    for j in range(n):
        if j != i:
            num = a[j]
            if num > current_max:
                current_max = num
            if num < current_min:
                current_min = num
    option1 = current_max * max_b
    option2 = current_max * min_b
    option3 = current_min * max_b
    option4 = current_min * min_b
    max_option = max(option1, option2, option3, option4)
    if max_option < result:
        result = max_option

print(result)
```
