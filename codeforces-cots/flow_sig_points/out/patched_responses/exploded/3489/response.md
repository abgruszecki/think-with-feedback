<think>
Okay, I need to solve this problem where I have to determine if it's possible to make all elements of an array zero by repeatedly choosing two elements and decreasing each by one each time. Let's think about the conditions required for this to be possible.

First, let's consider the sum of all elements. Each operation reduces the total sum by 2 (since two elements are each decreased by 1). So the total sum must be even. If the sum is odd, it's impossible. But that's not the only condition. For example, even if the sum is even, there might be a case where one element is too large compared to the others.

Wait, right. Another condition is that no element is greater than the sum of all other elements. Because in each operation, you can only decrease two elements. Suppose there's an element a_i that is larger than the sum of the rest. Then, even if you pair this a_i with every other element in every possible step, the total possible decreases for a_i would be at most the sum of the others. So a_i would end up with a_i - (sum of others) >= 1 (since a_i was larger than sum of others), which can't be zero. So the maximum element must be <= sum of all other elements.

So putting these two conditions together: sum must be even, and the maximum element must not exceed the sum of the others.

Wait, but the sum of the others is (total sum - max_element). So the condition is max_element <= sum_rest, which is equivalent to sum_rest >= max_element. So sum_rest + max_element = total_sum. So if sum is even, and max_element <= sum_rest, then it's possible?

Yes. Because the sum being even ensures that the total can be divided into pairs, and the max_element condition ensures that the largest element can be "balanced" with the others.

Let's test this against the examples.

First example: 1,1,2,2. Sum is 6, which is even. Max element is 2. Sum of others is 1+1+2=4. 2 <=4. So yes.

Second example: sum is 1+2+3+4+5+6=21, which is odd. So even before checking the max element, it's impossible. So output is no.

Another test case: n=2, elements [3,3]. Sum is 6, even. Max is 3, sum of rest is 3. So 3 <=3. So possible. How? Each operation chooses both elements. After three operations, both become zero.

Another case: n=3, elements [3,3,3]. Sum is 9, which is odd. So impossible.

Another case: n=3, elements [5,5,5]. Sum is 15 (odd). Impossible.

Another case: sum is even but max is too big. Like [5,1,1,1]. Sum is 8 (even). Max is 5. Sum of others is 3. 5>3, so no.

So the two conditions are necessary and sufficient.

So the algorithm is:

1. Calculate the total sum of the array. If it's odd, return NO.

2. Find the maximum element. If the max element is greater than (sum - max_element), return NO.

Otherwise, return YES.

So the code steps:

Read n.

Read the array as list of integers.

Compute sum of the array.

If sum is odd: output NO.

Else:

Compute max_val = max(array).

sum_rest = sum - max_val.

if max_val > sum_rest: output NO.

Else: output YES.

This approach is O(n) time, which is acceptable for n up to 1e5.

Memory-wise, we only need to store the array once, which is manageable.

So the Python code would be straightforward.

Edge cases:

n=2: if both elements are equal and sum even, yes. Like [1,1] sum 2 even, max 1, sum_rest 1.

Another edge case where the max is exactly sum_rest. Like [3,3], sum 6, max 3, sum_rest 3. Which works.

So the code should handle all these cases.

So the code:

Read n.

a = list of integers.

s = sum(a)

if s % 2 !=0: print NO.

else:

max_a = max(a)

if max_a > (s - max_a): print NO else YES.

That's all.

Let's code this.

Test the first example:

sum is 1+1+2+2=6 even.

max is 2.

sum_rest=6-2=4. 2 <=4: yes.

Second example sum 21: odd. So no.

Another test case where sum is even but max exceeds sum_rest:

n=4, elements [5,1,1,1]. sum 8 even.

sum_rest = 3. 5>3: no.

So code should handle that.

So the code is simple. Let's write it.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total % 2 != 0:
    print("NO")
else:
    max_val = max(a)
    remaining = total - max_val
    if max_val > remaining:
        print("NO")
    else:
        print("YES")
```