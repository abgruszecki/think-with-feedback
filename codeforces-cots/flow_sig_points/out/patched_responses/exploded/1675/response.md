<think>
Okay, let's see. The problem is to find the number of ways Olga can steal exactly one bag so that the remaining sum is even. Hmm. So the main idea here is to calculate the total sum of all the cookies first, right? Because when we remove a bag, the new sum will be the original sum minus the cookies in that bag. And we need this new sum to be even.

Wait, so the original sum is S. Then, for each bag i with value a_i, when we remove it, the sum becomes S - a_i. We need S - a_i to be even. Which is equivalent to (S - a_i) mod 2 == 0. But that's the same as S mod 2 == a_i mod 2. Because (S - a_i) mod 2 = (S mod 2 - a_i mod 2) mod 2. So for the result to be even, S - a_i must be even, which means S and a_i must have the same parity. Oh right! So the sum after removing the bag will be even if and only if the parity of the original sum and the parity of the bag's cookies are the same.

Wait, let's think again. Let's say original sum S is even. Then, to have S - a_i even, a_i must be even. Because even minus even is even, even minus odd is odd. Wait no, S is even. So S - a_i is even if a_i is even. Because even minus even is even, even minus odd is odd. So yes. So if S is even, then we can only remove a bag with even number of cookies to get an even sum. Similarly, if S is odd, then we need to remove an odd number of cookies. Because S is odd, subtracting an odd number would make it even. So the parity of a_i must be the same as the parity of the sum S.

So the approach is:

1. Compute the total sum S of all the cookies.
2. For each cookie a_i in the list, check if (a_i % 2) == (S % 2). Because then, removing a_i would leave a sum that's even.
3. Count the number of such a_i's. Because each such a_i represents a valid way.

Wait, but wait. Because when you remove a_i, the sum is S - a_i, which is even if and only if S - a_i is even. Which is equivalent to S and a_i having the same parity. Because S and a_i have the same parity if S - a_i is even. So yes, the condition is (S % 2) == (a_i % 2). So the number of valid ways is the count of a_i's that have the same parity as the sum S.

Wait, that's a brilliant insight. So regardless of whether S is even or odd, we just need to count the number of elements in the list that have the same parity as S. Because removing such an element would leave S - a_i even.

So the steps are:

- Compute the sum S of all a_i.
- If S is even, count how many a_i are even.
- If S is odd, count how many a_i are odd.
- The answer is that count.

But wait, let's test this with the examples.

First example:

Input is 1 bag with 1 cookie. Sum S is 1, which is odd. So we need to count the number of a_i with parity same as S (odd). The a_i is 1, which is odd. So count is 1. Which matches the sample output.

Second example:

Input is 10 elements. Let's compute the sum. Let's see: the numbers are 1, 2,2,3,4,4,4,2,2,2.

Sum them up: 1 is odd, then 2+2 is 4 even. Adding 3 gives sum 1+4+3 = 8, then 4+4+4 is 12, so total so far 8+12=20. Then 2+2+2+2 = 8. So total sum is 20 + 8 = 28. 28 is even. So we need to count even numbers in the list. Let's look at each element:

1 is odd → no. 2,2 (even), 3 (odd), 4,4,4 (even), 2,2,2 (even). So the even numbers are: 2,2,4,4,4,2,2,2. That's 8 elements. Which matches the sample output of 8.

Third example: 11 elements. The first 10 are 2's (even) and last is 99 (odd). Sum is 2*10 +99 = 20+99=119 (odd). So S is odd. So we need to count the number of odd a_i. There's only one: 99. So answer is 1. Which matches the sample.

So this approach works for all the examples. So the code can be written as follows:

Read n.

Read the list of a_i.

Compute sum S.

Compute the parity of S: s_parity = S % 2.

Count the number of elements in a_i where a_i % 2 == s_parity.

That's the answer.

So this is O(n) time, which is acceptable for n up to 100. No problem with constraints.

So the code would be straightforward.

In Python, code:

n = int(input())
a = list(map(int, input().split()))
s = sum(a)
target_parity = s % 2
count = 0
for num in a:
    if num % 2 == target_parity:
        count +=1
print(count)

Testing this code:

First example:

Input 1 and 1 → sum is 1 (odd). Target parity is 1. Check 1 → yes. Output 1.

Second example:

Sum is 28 → even. So count all even numbers. Let's see the input array:

1 (odd) → no.

Then 2,2 (even → yes), 3 (odd → no), 4,4,4 (even → yes), 2,2,2 (yes). So total 2+2+3 (for the first 2,2; then 3 4's, then 3 2's?) Wait in the input, the list is [1,2,2,3,4,4,4,2,2,2] → that's 10 elements. Let's count even numbers:

Indices 1,2,4,5,6,7,8,9 (assuming 0-based). Wait no, wait the array is 1,2,2,3,4,4,4,2,2,2. So elements are:

Element 1: 1 → odd → no.

Elements 2 and 3 (0-based) are 2 and 2 → even.

Then 3 is 3 → no.

Elements 4,5,6 are 4,4,4 → even.

Elements 7,8,9 (0-based) are 2,2,2 → even.

So total even numbers: 2 (positions 1 and 2), 3 (positions 4,5,6), 3 (positions 7,8,9) → total 2+3+3 = 8. Which matches.

Third example: sum is 119 (odd). So count the number of odd elements. The array is 10 2's (even) and one 99 (odd). So count 1. Which is correct.

So code works. Now, is there any edge case? Like when sum is zero (even). So all even elements contribute. Or when all elements are even and sum is even. For example, n=2, elements [2,2]. Sum is 4 (even). So count how many even elements: 2. So answer is 2. Because removing either would leave sum 2, which is even.

Another edge case: n=1, a_i=2. Sum is even. Target parity is 0. So a_i is even → yes. So answer is 1. But if you remove the only bag, sum becomes zero, which is even. So correct.

Yes, this seems to handle all cases correctly.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
parity = total % 2
count = 0
for num in a:
    if num % 2 == parity:
        count += 1
print(count)
```