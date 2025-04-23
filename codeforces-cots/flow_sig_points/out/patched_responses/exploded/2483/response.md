<think>
Okay, let's tackle this problem. The task is to find the two errors that were fixed by B. The first error is the one missing from the second line compared to the first, and the second error is the one missing from the third line compared to the second.

Hmm. So the first step is to find the error that's present in the first list but not in the second. Then, from the second list, find the error that's not present in the third. But since the order can change each time, we can't just compare indices. We need to track the counts of each number in each list.

Wait, right. Because there might be duplicates. For example, if the first list has two 3s, the second list might have one 3. Then that's the one that's removed. So the approach should be to count the frequency of each element in each list and find the discrepancies.

So for the first missing error: compare the counts between the first and second lists. The element whose count in the first list is one more than in the second list would be the missing one. Similarly for the second missing error between the second and third lists.

But how do we efficiently compute this? Let's think about using dictionaries or hash maps to count the occurrences.

For the first list, we can create a frequency dictionary. Then for the second list, subtract counts. The key with a count difference of 1 is the first missing. Then do the same between the second and third lists for the second missing.

Wait, but for large n (up to 1e5), we need an efficient way. But using dictionaries should be O(n) time, which is acceptable.

Let's outline the steps:

1. Read the first list (a), second list (b), third list (c).
2. Create a frequency map for a, then subtract frequencies from b. The key remaining with a value of 1 is the first missing error.
3. Then create a frequency map for b, subtract frequencies from c. The key remaining with a value of 1 is the second missing error.
4. Output the two errors in order.

Wait, but when we subtract the frequencies from the next list, maybe we need to compute the difference between the two. For example, for the first step: the first error is the one that's in a but not in b. So for each element in a, count how many times it appears, then subtract the counts from b. The element in a with a count higher by 1 than in b is the missing one.

Alternatively, since the second list is exactly the first list minus one occurrence of one element, then the difference between the two lists is that element. Similarly between the third and second.

But how to handle duplicates? For example, if the first list has two 5s, and the second list has one 5. Then the missing is 5.

So the correct approach is to count the frequency of each element in the first and second lists. The element where the count in the first list is one more than in the second list is the first missing.

So let's implement this. For each element in a, count the occurrences. Then for each element in b, count the occurrences. For each key in a's count, check if a_count[key] - b_count.get(key, 0) is 1. That's the first missing.

Similarly for the second missing error between b and c.

But how to handle elements that are in a but not in b? For example, if a has a key that's not in b, then the difference is a_count[key], which would be the missing count.

So, steps:

First error:

- Create a frequency dictionary for a and b. For each key in a's dict, check if a's count is higher than b's. The key where the difference is 1 is the first error.

Similarly, second error:

- Create a frequency dict for b and c. The key in b with count higher by 1 than in c is the second error.

Yes.

But how to implement this efficiently?

In Python, we can use collections.defaultdict for counting.

Alternatively, for even better performance, since the elements can be up to 1e9, using a Counter would be suitable. But for handling large n, we need to make sure that the code is efficient.

Let's proceed step by step.

For the first part:

Read n.

Read a = list of integers.

Read b = list of integers (n-1 elements).

Read c = list of integers (n-2 elements).

Then:

Create a Counter for a, called count_a.

Create a Counter for b, called count_b.

The first error is the element where count_a[element] - count_b.get(element, 0) == 1.

But wait, in case the element is not present in count_b, then count_b[element] is 0, so the difference is count_a[element], which would be 1 only if count_a[element] is 1.

So for example, in the first sample input:

a is [1,5,8,123,7]

count_a would be {1:1,5:1,8:1,123:1,7:1}

b is [123,7,5,1]

count_b is {123:1,7:1,5:1,1:1}

So 8 is in a but not in b. So count_a[8] is 1, count_b[8] is 0. Difference is 1. So 8 is the first error.

Yes.

Then, for the second error:

count_b for the elements in b. Then count_c for c.

The element in count_b where count_b[element] - count_c.get(element, 0) == 1.

In the first sample:

b is [123,7,5,1], count_b is each has 1.

c is [5,1,7]. count_c: 5:1, 1:1,7:1.

So for 123, count_b[123] is 1, count_c has 0. So difference is 1. So 123 is the second error.

Which matches the sample.

Another example: second sample input.

a is [1,4,3,3,5,7]

count_a: 1:1,4:1,3:2,5:1,7:1.

b is [3,7,5,4,3] (n-1=5 elements). count_b: 3:2,7:1,5:1,4:1.

So compare a and b. For 1: count_a[1] is 1, count_b[1] is 0. Difference is 1. So first error is 1.

Then, c is [4,3,7,5]. count_c:4:1,3:1,7:1,5:1.

Compare count_b and count_c. For 3, count_b is 2, count_c is 1. Difference is 1. So second error is 3.

Which matches the sample.

So this approach works.

So the code steps would be:

1. Read n.

2. Read a, b, c.

3. Compute count_a = Counter(a)

4. Compute count_b = Counter(b)

5. For the first missing error (from a to b):

   Iterate through elements in a, check for each if count_a[element] > count_b.get(element,0). When the difference is 1, that's the first error.

Wait, but elements can appear multiple times. For example, in the second sample, the first error is 1, which is unique. But if there was an element that appears twice in a and once in b, then that would be the first error.

But how to find the first error? For example, when a has two 3's and b has one 3, then the first error is 3.

But how do we find that in code? Because when we iterate through a, the first element where count_a[e] - count_b[e] is 1 could be found by checking all elements.

But since the elements are in a list, perhaps the first occurrence of such an element would be the answer? Wait, no. Because the problem says that in the first correction, exactly one error is removed, which could be any occurrence. But the order in the output doesn't matter for the first error. So any occurrence of the element that has a count difference of 1 would be correct.

Wait, but the problem says that B fixed one mistake (so exactly one error is removed from a to get b). So for example, if a has two 3s and b has one 3, then the first error is one of the 3s. So the output for the first error is 3.

So the code needs to find which element in a has a count higher than in b by exactly one.

But how to find it? Since the elements can be in any order, we need to check all possible elements in a, but perhaps we can break once we find the element.

But in code, since we are using a Counter, which is a dictionary, the elements in a may not be unique. So for example, a list [3,3,5] would have a Counter {3:2,5:1}.

So when checking for the element where count_a[e] - count_b.get(e,0) == 1, we need to find that element. But when the same element occurs multiple times, how do we check?

Wait, the Counter approach counts the total occurrences, so regardless of the order. For example, in the second sample, the first error is 1. The count in a is 1, and in b, it's 0. So the difference is 1.

So the code can be written as:

For the first error, iterate through all elements in a's Counter and find the key where count_a[key] - count_b.get(key, 0) == 1.

But since a Counter is a dictionary, iterating through its keys will give each unique element once. So for example, in a list [3,3,5], the Counter's keys are 3 and 5. So for the first step, for each unique key in a, check if the count difference is 1.

But what if the element that's removed is one of multiple instances? For example, a has three 3s, and b has two. Then the count difference is 1. So the code would correctly identify 3 as the first error.

So the approach is:

For the first error, loop through all elements in the Counter of a, and check if their count in a is 1 more than in b. Once found, that's the first error.

But in Python, to get the first such element, since the order of the elements in the Counter is arbitrary (since it's a dictionary), but the code can just pick any of them, since the problem allows any order? Wait, no. The problem says to output the two errors in the order they were fixed. The first error is the one that was fixed first (so it's missing from the second line), and the second error is the one missing from the third line (so fixed after the first error).

Wait, the problem statement says that B fixed two mistakes. The first mistake is the one that's missing from the second line. The second mistake is the one missing from the third line.

So the order in the output is first the error removed in the first step, then the error removed in the second step.

So the code's approach for the first error is correct.

So for the first error, the code can iterate through the elements of a's Counter, and find the key with count difference 1.

Similarly for the second error, iterate through the elements of b's Counter, find the key with count difference 1 compared to c's Counter.

But how to find these keys efficiently?

Another approach is to compute the difference between the two Counters.

For example, for a and b:

diff = count_a - count_b.

But in Python, the subtraction of Counters works as follows: For each element, the count is the max of count_a[e] - count_b[e], 0. So if count_a[e] > count_b[e], then the difference is count_a[e] - count_b[e]. Otherwise, 0.

So in this case, after a - b, the resulting Counter should have exactly one element with count 1. So the key is the first error.

Similarly for b - c.

So in code:

first_error = (count_a - count_b).most_common(1)[0][0]

second_error = (count_b - count_c).most_common(1)[0][0]

But wait, let's test this.

In the first sample:

count_a is {1:1,5:1,8:1,123:1,7:1}

count_b is {123:1,7:1,5:1,1:1}

count_a - count_b: for each key in a:

1: 1-1=0 → not in result.

5: 1-1=0 → not.

8: 1-0=1 → included.

123:1-1=0 → no.

7:1-1=0 → no.

So the result is {8:1}. most_common(1) is (8,1). So first_error is 8.

Yes.

In the second sample:

count_a is {1:1,4:1,3:2,5:1,7:1}

count_b is {3:2,7:1,5:1,4:1}

count_a - count_b:

1:1-0=1 → included.

4:1-1=0 → no.

3:2-2=0 → no.

5:1-1=0 → no.

7:1-1=0 → no.

So the difference is {1:1} → first_error is 1.

Then, count_b is {3:2,7:1,5:1,4:1}

count_c is {4:1,3:1,7:1,5:1}

count_b - count_c:

3:2-1=1 → included.

others: 1-1=0.

So the difference is {3:1} → second_error is 3.

Yes.

So this approach works.

Thus, the code can be written as:

from collections import Counter

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

count_a = Counter(a)
count_b = Counter(b)
count_c = Counter(c)

first_error = (count_a - count_b).most_common(1)[0][0]
second_error = (count_b - count_c).most_common(1)[0][0]

print(first_error)
print(second_error)

Wait, but in Python, the Counter subtraction might return multiple elements if there are multiple differences. But according to the problem statement, there is exactly one element that's removed each time. So the difference Counter should have exactly one element with a count of 1.

So using most_common(1) will get that element.

This code should work and is efficient.

Testing the first sample:

Input:

5

1 5 8 123 7

123 7 5 1

5 1 7

count_a - count_b is {8:1}, so first_error is 8.

count_b - count_c: count_b is {123:1,7:1,5:1,1:1}, count_c is {5:1,1:1,7:1}.

count_b - count_c is {123:1}.

So second_error is 123. Correct.

Second sample:

6

1 4 3 3 5 7

3 7 5 4 3

4 3 7 5

count_a - count_b is {1:1} → first error 1.

count_b is {3:2,7:1,5:1,4:1}

count_c is {4:1,3:1,7:1,5:1}

count_b - count_c is {3:1} → second error 3.

Yes.

So this code works.

But what about elements that appear multiple times, like in the second sample's 3s. The code correctly identifies the first error as 1 and the second as 3.

Another test case: suppose a has [2,2,2], b has [2,2], and c has [2]. Then first error is 2 (since a has 3, b has 2, so difference is 1). Then, b has 2, c has 1 → difference 1. So code returns 2 and 2. Which is correct.

But in this case, the output is 2 followed by 2. Which is correct, because B first fixed one 2 (so three → two in b), then fixed another 2 (two → one in c).

So the code works.

Now, considering the constraints: n can be up to 1e5. The code reads the input as lists and uses Counters, which are O(n) time and space. For n=1e5, this is acceptable.

But in Python, using Counter's subtraction is O(k) where k is the number of keys. Since all keys are elements in a, which can be up to 1e5 unique elements, but the problem allows for 1e5 elements. However, the total time is acceptable.

So this approach is efficient and correct.
</think>

```python
from collections import Counter
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

count_a = Counter(a)
count_b = Counter(b)
count_c = Counter(c)

first_error = (count_a - count_b).most_common(1)[0][0]
second_error = (count_b - count_c).most_common(1)[0][0]

print(first_error)
print(second_error)
```