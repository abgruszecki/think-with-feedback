<think>
Okay, let's tackle this problem. So, the task is to divide n even numbers into groups (each with at least two numbers) such that the sum of the squares of the group sums is minimized. Hmm, how do we approach this?

Wait, the first thing I notice is that the optimal grouping probably depends on pairing larger numbers with smaller ones. Because when you have a large number paired with a small one, their sum's square is (a + b)^2 = a² + 2ab + b². But if you pair two large numbers together and two small ones, the sum of squares would be (a + c)^2 + (b + d)^2. Wait, maybe not. Let me think.

Actually, the sum of squares is minimized when the groups' sums are as balanced as possible. For example, if you have a very big number and a very small number in the same group, their sum's square might be better than pairing the big with another big and the small with another small. Wait, no. Wait, let's take an example. Suppose we have 8 and 5, 3 and 2. If we pair 8+5=13 and 3+2=5, sum of squares is 169 + 25 = 194. Alternatively, 8+2=10 and 5+3=8, sum is 100 +64=164. Which is better. So pairing the largest with the smallest gives a better result here. So the second example gives a lower sum. So perhaps the optimal approach is to sort the array, pair the largest with the smallest, then the second largest with the second smallest, and so on. That seems to be the case in the first sample.

So the strategy might be: sort the array in non-decreasing order. Then pair the largest with the smallest, the second largest with the second smallest, etc. Let's test this hypothesis against the examples.

In the first example, the sorted array is [2,3,5,8]. Pair 2 with 8 (sum 10) and 3 with 5 (sum 8). Which gives 10^2 +8^2=164. Correct.

In the second example, the sorted array is [1,1,1,2,2,2]. Pair 1 and 2, 1 and 2, 1 and 2. Each sum is 3. 3^2 *3 = 27. Which is correct.

So the approach seems to work for the examples. So the plan is:

1. Sort the array in ascending order.
2. Pair the first element with the last, the second with the second last, and so on.

But why is this optimal? Let's think about the mathematical reasoning.

Suppose we have two pairs (a, d) and (b, c), where a <= b <= c <= d. Let's compare the sum of squares when paired as (a+d)² + (b +c)² versus (a+c)² + (b+d)². Which is smaller?

Compute the difference between the two:

(a+d)^2 + (b + c)^2 - [ (a +c)^2 + (b +d)^2 ]

Expanding all terms:

= a² + 2ad + d² + b² + 2bc + c² - (a² + 2ac + c² + b² + 2bd + d²)
= 2ad + 2bc - 2ac - 2bd
= 2(ad + bc - ac - bd)
= 2( a(d -c) + b(c -d) )
= 2( (d -c)(a - b) )

Since a <= b and d >= c (since the array is sorted a <= b <= c <= d), d -c is >=0? Wait, no. Wait, in the original scenario, a is the first element, d the last. Then the next pair would be second and second last. So for the next pair, if the array is sorted, for example, if we have a sequence like a, b, c, d where a <= b <= c <= d. Then pairing a+d and b+c. So the difference between (a+d)² + (b +c)² and (a + c)² + (b +d)².

Wait, let's see: the difference is (a+d)^2 + (b+c)^2 - (a+c)^2 - (b+d)^2.

Expand each term:

(a^2 + 2ad + d^2) + (b² + 2bc + c²) 
- (a² + 2ac + c²) - (b² + 2bd + d²)

Simplify:

2ad + 2bc - 2ac - 2bd = 2(ad + bc - ac - bd)
Factor this: 2[ a(d -c) + b(c -d) ) ] = 2[ (d -c)(a - b) ]

Now, d >= c (since sorted), and a <= b (since sorted), so (d-c) is >=0, (a -b) is <=0. So the product is <=0. So the entire difference is 2*(negative or zero) <=0. So the original sum (a+d and b+c) is less than or equal to the other pairing. So the sum (a+d)^2 + (b+c)^2 is less than or equal to (a +c)^2 + (b +d)^2. So pairing a with d and b with c gives a better (smaller) sum.

Therefore, this suggests that pairing the smallest with the largest, then next smallest with next largest, etc., is the optimal way to minimize the sum of squares.

Therefore, the algorithm would be:

Sort the array in ascending order.

Then pair a[0] with a[-1], a[1] with a[-2], etc.

Each pair is a group. However, the problem allows groups to have more than two elements. Wait, the problem states that each group must have at least two elements. But in the examples, the optimal solution was groups of two. So maybe the optimal is to have all groups of exactly two elements. Because if you can have groups of two, but the problem allows larger groups, but perhaps grouping into pairs gives the minimal sum.

Wait, but why? Suppose you have three elements. Wait, but the problem says n is even, so the total number of elements is even. So all groups can be of two elements. So the optimal grouping is to pair into two-element groups, as any larger group would lead to higher sums. Because combining more numbers would increase their sum. For example, if you have a group of three elements, their sum is larger than the sum of individual pairs. So perhaps grouping into pairs is the way to go. So the optimal is to group all into pairs of two elements, and the way to pair them is sorted and paired smallest with largest.

So the approach is:

Sort the array.

Pair the first element with the last, second with second last, etc.

Then compute the sum of squares of each pair's sum.

So the steps are:

1. Sort the array in non-decreasing order.

2. Pair a[i] with a[n-1 -i] for i from 0 to n/2 -1.

3. For each pair, compute (a[i] + a[n-1 -i])² and sum all.

So for n=4: pairs are (0,3) and (1,2).

So how do we implement this efficiently?

Given that n can be up to 3e5, we need to process in O(n log n) time, which is acceptable.

So the code steps:

Read n.

Read list a.

Sort a.

Initialize sum = 0.

For i in 0 to (n//2 -1):

sum += (a[i] + a[n-1 -i]) **2

Output sum.

Wait, but let's check the second example:

Input is 6 numbers: [1,1,1,2,2,2]

After sorting: [1,1,1,2,2,2]

Pairings are (0,5), (1,4), (2,3).

So pairs are (1 and 2), (1 and 2), (1 and 2). Sum each pair is 3. Each squared is 9. Sum is 9*3=27. Which matches the example.

Another example: input 4 numbers 8 5 2 3. Sorted is [2,3,5,8]. Pairings are 2+8 and 3+5. Sum 10^2 +8^2= 100+64=164. Correct.

So the algorithm works for these examples.

So the code is straightforward: sort, pair, compute sum.

So now the code:

Read n.

Read list of a's.

Sort a.

sum =0

for i in range(n//2):

    sum += (a[i] + a[ n-1 -i ]) **2

print(sum)

Wait, but for n even, the number of pairs is n/2. Each pair is two elements, so the group count is n/2, each with two elements.

But the problem allows groups with more than two elements. So why is this the optimal? For example, if you have four numbers: 1,2,3,4. Pair them as (1+4) and (2+3) sum 5 and 5: sum squares 25+25=50. Alternatively, group (1,2,3) and 4. Then sum is 6+4=10, squares 36 +16=52>50. Or group all four into one group: sum 10, square 100>50. So grouping into pairs is better.

Another example: if we have 1,1,2,2. Pairing (1+2) and (1+2) sum 3 each: total 18. If grouped as (1+1+2) and 2, sum 4 and 2: squares 16+4=20>18.

So the minimal sum comes from grouping into pairs of two, with the pairing strategy of smallest and largest.

Therefore, the code is correct.

Now, for the implementation. Since n can be up to 3e5, the code needs to be efficient. Sorting 3e5 elements is O(n log n), which is acceptable. The sum is O(n), which is acceptable.

So the code is straightforward.

Testing on sample inputs:

Sample 1:

4

8 5 2 3 → sorted [2,3,5,8]. pairs (2+8)=10, (3+5)=8. sum 100+64=164.

Sample 2:

6

1 1 1 2 2 2 → sorted [1,1,1,2,2,2]. pairs 1+2, 1+2, 1+2. sum 9 each. total 27.

So the code works.

Thus, the correct solution is to sort the array and pair the i-th smallest with i-th largest, sum their squares.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(n // 2):
    total += (a[i] + a[-i-1]) ** 2
print(total)
```