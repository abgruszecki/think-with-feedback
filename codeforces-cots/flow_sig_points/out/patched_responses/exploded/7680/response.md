<think>
Okay, let's see. The problem is to find the minimum number of operations to turn all elements of an array into 1. Each operation allows replacing one of two adjacent elements with their GCD. Hmm.

First, I need to check if it's even possible. If there's at least one 1 in the array, then the answer is possible because we can spread that 1 to the entire array. But if there are no 1s, then we need to find a subarray where the GCD of all elements is 1. Because only then can we create a 1 through operations, and then spread it. If the overall GCD of the entire array isn't 1, then it's impossible. So the first step is to compute the GCD of the entire array. If it's not 1, return -1.

If there's already a 1 in the array, then the number of operations is (n - count_ones) * 1. Because each non-1 element can be turned into 1 by replacing it with an adjacent 1 in one step. Wait, but maybe that's not exactly accurate. Because the existing 1s can help. For example, if there are k 1s, then each non-1 element needs to be adjacent to a 1. So the total steps would be the total number of elements not 1, but the way they are arranged might require more steps. Wait, no. Wait, the initial array may have some 1s. For each 0 in the array (but no, the problem says the elements are >=1). Wait, the initial array can have 1s. So, for each element that's not 1, we can turn it into 1 by applying an operation with a neighboring 1. Each such element takes exactly one operation. But how?

Wait, let's say the array is [1, x]. Then in one operation, we can replace x with GCD(1, x) = 1. So that's one step. Similarly, if the array is [x, 1], same. For an array like [1, a, b], we can first turn a into 1 (using the first 1), which takes 1 step, then turn b into 1 using the new 1 (another step). So the total steps for n elements with k existing 1s is (n -k) steps. But wait, the existing 1s might not be contiguous. For example, if the array is [1, 2, 1, 3], then the two 1s are already present. The 2 can be replaced in one step (using the left 1), and the 3 can be replaced in one step (using the right 1). So total steps are 2. Which is (4-2) = 2. So that formula works.

But the problem is how to get the first 1. If there are no existing 1s, then we need to find the smallest window (subarray) where the GCD is 1. Because once we can create a 1 in that window, then the steps required to spread that 1 to the entire array would be the length of the window minus 1 (since each operation in the window reduces the elements until we get a 1), plus (n - 1) steps to spread the 1 to the entire array. Wait, maybe not exactly. Let's think.

Suppose we have a window of length L where the GCD is 1. The minimum number of operations to create a single 1 in that window is (L-1) operations. Because to compute the GCD of the entire window, you need to iteratively compute GCDs of adjacent pairs, but I'm not sure how the operations work. Let me think.

Each operation replaces one of two adjacent elements with their GCD. So, to compute the GCD of a window, you can perform operations that gradually reduce the elements. For example, for a window of three elements a, b, c:

First compute GCD(a, b) = g1. Then compute GCD(g1, c) = g2. If g2 is 1, then we can do that in two steps. But how exactly?

Wait, maybe the minimum number of steps to get a 1 in a subarray is the length of the subarray minus 1. For example, if there's a subarray of length m where the GCD is 1, then you need m-1 operations to create a 1. Because each step reduces the elements by replacing adjacent pairs with their GCD. So for a subarray of length m, you can compute the GCD in m-1 steps. Wait, perhaps not. Let's take an example.

Take the sample input 1: [2,2,3,4,6]. The overall GCD is 1, and there's a subarray (positions 1-2) which has GCD 2. But that's not helpful. Wait, the sample input's solution uses a subarray where they create a 1 in two steps. Let me see:

Original array: 2,2,3,4,6. The first operation is choosing the two 2s. Replace one of them with GCD(2,2)=2. Wait, that doesn't help. Oh wait, the first sample's note shows that they first replace the two 2s (positions 1 and 2) with 1. How does that happen? Because the GCD of 2 and 2 is 2. Wait, that doesn't add up. Wait, the first step in the note's explanation replaces the two 2s (elements 1 and 2) with GCD(2,2) = 2? Wait, no. Oh no, in the note, the first step is [2, 2, 3, 4, 6] → [2, 1, 3, 4, 6]. So how did they get a 1 from 2 and 2? Because GCD(2,2) is 2, not 1. Hmm, that suggests that perhaps the sample input's array was different. Wait, let me check the first sample input again.

Ah, the first sample input is:

5

2 2 3 4 6

Wait, the first two elements are 2 and 2. Their GCD is 2. But in the note, they turn them into 2 and 1. How? That doesn't make sense. Wait, perhaps the operation allows replacing either of the two elements with their GCD. Wait, the problem says: choose two adjacent elements x and y, and replace one of them with GCD(x, y). So for two elements x and y, after the operation, one of them is replaced by GCD(x,y). The other remains as before. So in the first step of the sample, replacing the two 2s (positions 1 and 2), which are 2 and 2. Replacing one of them (say the second) with GCD(2,2)=2. That doesn't help. So perhaps the note is wrong? Or maybe I'm misunderstanding the problem. Oh wait, maybe the note's initial array is different.

Wait the note's steps are:

Original array: [2, 2, 3, 4, 6]

After first step: [2, 1, 3, 4, 6]. So the two 2s are replaced with 2 and 1. How? GCD(2,2) is 2. Unless the note has a typo. Wait this suggests that perhaps the initial array is different. Maybe the first two elements are 2 and something else. Let me check the first sample input again. Oh no, the sample input is 5 elements: 2, 2, 3,4,6. So the first two elements are 2 and 2. Then the first operation is to replace them with 2 and 1. How is that possible? Because GCD(2,2) is 2. So there's a mistake here. So perhaps the note is illustrative and the actual steps are different. But regardless, the problem statement is as given.

Wait maybe I'm misunderstanding the operation. The operation is: choose two adjacent elements x and y. Then replace one of them with their GCD. So for example, if x=2 and y=2, then you can replace either x or y with GCD(2,2)=2. So that's not helpful. But in the note, they get a 1. So perhaps the note's example isn't accurate. Or maybe I'm missing something. Wait perhaps the first step in the note is not the first step. Let me look again. Oh no, the note's first step is the original array, then after 5 moves, it becomes all 1s. So the steps must be correct.

Wait, perhaps the first step in the note is not using the first two elements. Let me think. Let's see the steps:

Original array: 2,2,3,4,6.

After first move: [2,1,3,4,6]. So how? So perhaps the two elements selected are the second and third elements? Wait 2 (index 2?) or perhaps the first two elements are replaced, but how?

Wait perhaps the first step is replacing the 2 (first element) and 2 (second element) by replacing the second with GCD(2,2) = 2. But that doesn't create a 1. So there's a mistake here. Wait perhaps the sample input is incorrect, but according to the problem statement, the note's explanation is correct. So perhaps there's a misunderstanding of the problem.

Alternatively, maybe the initial array has elements that allow creating a 1. Wait, the array in the first sample is 2,2,3,4,6. The GCD of all elements is 1. So there exists a subarray whose GCD is 1. Let's compute the GCD of elements 2,3,4,6. Let's see:

GCD(2,3) is 1. So the subarray [2,3] has a GCD of 1. Wait, no. Wait, the GCD of 2 and 3 is 1. So a subarray of length 2. So the minimal steps would be (2-1) = 1 operations to get a 1 here. Then, the number of operations would be (1) + (n -1) steps to spread the 1. Wait, maybe the steps are:

First, create a 1 in the array. Let's say the minimal window where GCD is 1 is of length L. The number of steps needed to create a 1 is (L-1) steps. Then, the total steps would be (L-1) + (n-1). Because after creating the 1, you have to spread it to the entire array. But how?

For example, in the first sample, the minimal window is of length 2 (elements 2 and 3, GCD 1). So steps to create 1: 2-1=1. Then spread to all elements. The array after creating a 1 would have that 1 somewhere. Then, each element not 1 can be turned into 1 in one step each. But how many steps are needed to spread?

Wait, when you have a 1 in the array, each adjacent element can be turned into 1 in one operation. So for example, if the array is [..., 1, x, ...], you can replace x with GCD(1, x) = 1 in one step. So each element to the left and right can be converted one by one. So the total steps after creating a 1 would be (number of elements not 1) * 1 steps. But that's only if the 1 is in a contiguous block. Wait, perhaps the spreading requires that the 1 is adjacent to the elements. So for example, if the 1 is at position i, then to turn all elements to the left into 1, each requires one step (since you can pair each element with the 1 next to it). Similarly for the right.

But in that case, the total steps after creating the 1 would be (n-1) steps, because each of the other n-1 elements can be converted in one step. So the total steps would be (L-1) + (n-1). But in the first sample, the answer is 5. Let's see:

If the minimal window length L is 2 (steps needed 1), then total steps would be 1 + 4 =5. Which matches the sample. So that's correct. So the algorithm would be:

1. If the array already contains at least one 1, then the answer is (n - number_of_ones). Because each non-1 can be converted in one step.

2. Else, compute the minimal length L of a subarray where GCD is 1. If no such subarray exists (i.e., the overall array GCD is not 1), return -1.

   Then, the minimal steps is (L-1) + (n-1). Because (L-1) steps to create the first 1, then (n-1) steps to spread it.

So the problem reduces to finding the minimal L for which there exists a subarray of length L with GCD 1.

So the steps for solving the problem:

- Check if there's at least one 1 in the array. If yes, return (n - count_ones).

- Else, compute the GCD of the entire array. If it's not 1, return -1.

- Else, find the smallest L such that there's a subarray of length L with GCD 1. Then, the answer is (L-1) + (n-1).

So now, the challenge is to find the smallest L where a subarray of length L has GCD 1.

How to compute this efficiently?

Constraints: n can be up to 2000. So O(n^2) is acceptable, but anything higher may be a problem.

An approach to compute the minimal L is to iterate over all possible starting positions and compute the GCD of subarrays starting at that position and extending as far as possible. For each starting index i, we can keep track of all possible GCDs and their lengths.

For example, for each i from 0 to n-1:

- current_gcds is a dictionary {gcd_value: minimal_length}.

- For j from i to n-1:

   compute the current GCD as gcd(current_gcd, a[j]).

   if current_gcd is 1, then update the minimal L if (j - i +1) is smaller than the current minimal.

   We can break early if the GCD becomes 1, because adding more elements will only keep the GCD as 1 or smaller, but since we are looking for minimal L, once we find a GCD 1 at j, we can note the length (j-i+1) and proceed to the next i.

But how to manage this efficiently?

Let's think. For each starting index i, we can track the current GCDs as we expand the subarray to the right. For example:

Start at i=0. j starts at i, and for each step, we compute the GCD of the current subarray from i to j.

We can track a set of possible GCDs for each j. For example, for j=0, the GCD is a[0]. For j=1, the possible GCDs are GCD(a[0], a[1]). For j=2, the possible GCDs are GCD(gcd_prev, a[2]). Wait, but since the GCD is computed incrementally, each step j adds a new element and the new GCD is the GCD of the previous GCD and the new element.

So for each i, we can track the current GCD as we extend j from i to the right. At each step j, compute the GCD of a[i..j]. If at any j, this GCD becomes 1, then the length is j-i+1. We can keep track of the minimal length found across all i and j.

So for each i, we start with current_gcd = a[i]. If it's 1, then the minimal L is 1. Otherwise, we proceed to j=i+1, compute GCD(current_gcd, a[j]). If it's 1, then L is 2. Otherwise, proceed to j=i+2, etc.

But this approach would be O(n^2) in the worst case, which for n=2000 is 4 million operations. That's acceptable.

So the algorithm is:

Initialize min_len to a large value.

For each i from 0 to n-1:

   current_gcd = a[i]

   if current_gcd is 1:

       min_len = 1

       break all loops

   for j from i+1 to n-1:

       current_gcd = gcd(current_gcd, a[j])

       if current_gcd == 1:

           current_length = j - i + 1

           if current_length < min_len:

               min_len = current_length

           break  # since adding more elements won't reduce the length

So, for each i, we compute the GCD of the subarray starting at i and extending as far as possible. If at any point the GCD becomes 1, we record the length and break, since any longer subarrays starting at i will have a GCD of 1 but longer length, which is worse.

So this approach is O(n^2) in time, which should work for n=2000.

Once we find the minimal L, the answer is (L-1) + (n-1).

So putting it all together:

Read the array.

Check if any element is 1. If yes, the answer is (n - count_ones).

Else, compute the overall GCD. If it's not 1, output -1.

Else, compute the minimal L as described. Then, answer is (L-1) + (n-1).

So now, code.

Let's see the sample input 3:

3

2 6 9

The array has no 1s. Overall GCD is GCD(2,6,9). Let's compute:

GCD(2,6) is 2. GCD(2,9) is 1. So the overall GCD is 1.

Find minimal L. The possible subarrays:

Check i=0:

current_gcd=2. Not 1.

j=1: gcd(2,6)=2. Not 1.

j=2: gcd(2,9)=1. So L is 3 (0-2). So min_len is 3.

i=1:

current_gcd=6. Not 1.

j=2: gcd(6,9)=3. Not 1. So no.

i=2:

current_gcd=9. Not 1.

So minimal L is 3. So steps (3-1) + (3-1) = 2+2=4, which matches the sample.

Another sample input 2:

4

2 4 6 8

No 1s. Overall GCD is 2. So output is -1.

Sample input 1:

n=5, array 2 2 3 4 6.

No 1s. Overall GCD is 1. Find minimal L.

Check i=0:

current_gcd=2.

j=1: GCD(2,2)=2.

j=2: GCD(2,3)=1. So L=3. So current min is 3.

i=1:

current_gcd=2.

j=2: GCD(2,3)=1. L=3-1+1=3? Wait, j=2, i=1: length is 2 (i=1, j=2: elements 2 and 3). So length is 2. Oh right, because j increments from i+1. Wait, in the code, for i=1:

current_gcd = a[1] = 2.

j starts at i+1=2:

compute GCD(2,3) = 1. So the subarray is from i=1 to j=2, length 2. So min_len is 2.

Then the answer is (2-1) + (5-1) = 1 +4=5, which matches the sample.

Ah, right. So the code needs to find the minimal L. So in the first sample, the minimal L is 2, but in the code, when i=1, j=2, the current_gcd is 1. So the length is j -i +1 = 2.

So the code would find L=2 as the minimal.

So the code would output (2-1)+(5-1) =1+4=5, which matches the sample.

So the code logic is correct.

Now, code.

First, read n and array.

Check for existing 1s:

count_ones = sum(1 for x in array if x ==1)

if count_ones >0: print(n - count_ones)

else:

   compute overall GCD of the array. if not 1, print -1.

   else, find minimal L.

       min_len = infinity

       for i in 0...n-1:

           current_gcd = array[i]

           if current_gcd ==1:

               min_len =1

               break

           for j in i+1 ...n-1:

               current_gcd = gcd(current_gcd, array[j])

               if current_gcd ==1:

                   length = j -i +1

                   if length < min_len:

                       min_len = length

                   break  # since further elements won't reduce the length

       answer is (min_len -1) + (n-1)

       print(answer)

Now, how to compute the overall GCD.

We can compute the overall GCD by iterating through the array.

Similarly, for each i, compute the cumulative GCD.

So code in Python:

Implementing the steps.

Edge cases:

n=1. If the array is [1], output 0. Else, if the element is not 1, check if it's possible. For n=1, if the element is 1, answer 0. Else, if the array's GCD is 1 (only possible if element is 1). So n=1, array [x], if x is 1, output 0. Else, if x is not 1, check if overall GCD is 1. Which is only possible if x is 1. So output -1.

So code handles this.

Another edge case: all elements are 1. Then output 0.

Now, code.

But in Python, for GCD, we can use math.gcd, but note that math.gcd returns 0 if both inputs are 0, but in our problem, all elements are >=1. So for two elements a and b, their GCD can be computed as math.gcd(a, b), but since in Python's math.gcd, the function returns the absolute value, and since inputs are positive, it's okay. However, when the inputs are 0, but our problem states that elements are >=1, so no problem.

Wait, the problem says 1<= ai <=1e9. So all elements are at least 1. So no issues.

But for multiple elements, we need to compute the GCD step by step.

So for the overall GCD:

overall_gcd = a[0]

for x in a[1:]:

    overall_gcd = math.gcd(overall_gcd, x)

    if overall_gcd ==1:

        break

So that's efficient.

Now, code:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    count_ones = a.count(1)

    if count_ones >0:

        print(n - count_ones, file=output_stream)

    else:

        # compute overall GCD

        overall_gcd = a[0]

        for num in a[1:]:

            overall_gcd = math.gcd(overall_gcd, num)

            if overall_gcd ==1:

                break

        if overall_gcd !=1:

            print(-1, file=output_stream)

        else:

            # find minimal L

            min_len = float('inf')

            for i in range(n):

                current_gcd = a[i]

                if current_gcd ==1:

                    min_len =1

                    break

                for j in range(i+1, n):

                    current_gcd = math.gcd(current_gcd, a[j])

                    if current_gcd ==1:

                        current_length = j -i +1

                        if current_length < min_len:

                            min_len = current_length

                        break  # since adding more elements won't help

                if min_len ==1:

                    break

            res = (min_len -1) + (n-1)

            print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
2 4 6 8
""",
            "output": \
"""\
-1
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

Sample 3:

3

2 6 9.

No ones. Overall GCD is 1.

Looking for minimal L:

i=0:

current_gcd=2. j=1: gcd(2,6)=2. j=2: gcd(2,9)=1. So current_length is 3. min_len=3.

i=1:

current_gcd=6. j=2: gcd(6,9)=3. No.

i=2:

current_gcd=9. No.

So minimal L is 3. res=3-1 + 3-1 =2+2=4.

Which matches.

Another test case where the minimal L is found early.

Test case where the array is [3, 4]. The overall GCD is 1. Minimal L is 2. So steps (2-1)+(2-1)=1+1=2. How?

The steps would be:

First, create a 1. Subarray [3,4] has GCD 1. So two elements, 1 step to create 1. Then spread to the other element.

So the array after creating 1 could be [1,4], which takes 2 steps: first step to replace 3 and4 with GCD(3,4)=1 (maybe replacing the first element, then replace 4 with GCD(1,4)=1. So two steps. Which matches the formula.

So code works.

Another case: array [4, 3]. Minimal L is 2. So steps 1 + (2-1) =2.

Yes.

So code is correct.
</think>

```python
import math

n = int(input())
a = list(map(int, input().split()))
count_ones = a.count(1)

if count_ones > 0:
    print(n - count_ones)
else:
    overall_gcd = a[0]
    for num in a[1:]:
        overall_gcd = math.gcd(overall_gcd, num)
        if overall_gcd == 1:
            break
    if overall_gcd != 1:
        print(-1)
    else:
        min_len = float('inf')
        for i in range(n):
            current_gcd = a[i]
            if current_gcd == 1:
                min_len = 1
                break
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, a[j])
                if current_gcd == 1:
                    current_length = j - i + 1
                    if current_length < min_len:
                        min_len = current_length
                    break
            if min_len == 1:
                break
        res = (min_len - 1) + (n - 1)
        print(res)
```
