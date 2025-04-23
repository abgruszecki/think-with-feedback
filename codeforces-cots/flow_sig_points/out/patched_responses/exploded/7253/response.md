<think>
Okay, let's tackle this problem. The goal is to arrange the paintings in such a way that the number of times a visitor becomes happy (i.e., each time the next painting is more beautiful than the current) is maximized. So, we need to find the maximum possible number of adjacent pairs where the next element is larger than the previous one.

Hmm. Let's think about the problem. Let's take some examples. For the first sample input, all elements are unique and sorted in increasing order. That gives 4 pairs, which is the maximum possible since each consecutive pair is increasing. But in the second example, there are duplicates. The optimal arrangement is 100, 200, 100, 200. Here, the pairs are 100<200 (increase), 200>100 (no), 100<200 (increase). So two increases. So even with duplicates, there's a way to maximize.

So the key here is to arrange the elements such that as many consecutive increases as possible. How do we do that when there are duplicates?

Let me think about the structure of the optimal arrangement. Let's say we have a frequency count of each beauty value. For example, if some beauty value appears multiple times, like two 100s and two 200s. How to arrange them?

One approach that comes to mind is the greedy approach. Arrange the elements in a way that alternates as much as possible between increasing and then using a lower value. Like, arranging the elements in such a way that after a high value, we take a lower one if possible to create another possible increase.

Wait, maybe the maximum number of increases is determined by the number of duplicates. Let's think about the maximum possible increases.

Suppose all elements are the same. Then there can be zero increases. If all elements are unique and sorted, the maximum is n-1. But when there are duplicates, the maximum possible increases might be (total elements - maximum frequency) + (max_frequency -1). Wait, that formula might not be correct.

Wait, let's think of the problem in terms of arranging the elements such that as many increases as possible. The optimal arrangement would be to place elements in such a way that each element (except possibly some) is followed by a larger one. How can duplicates affect this?

Another approach is to model this as a problem of arranging the elements so that after each peak (a high value), you place a lower value so that you can have an increase again. For example, in the second sample: 100, 200, 100, 200. The 200 is followed by 100 (no increase), but then 100 is followed by 200 (increase). So here, the two 200s and two 100s are arranged in a way that creates two increases.

So perhaps the maximum number of increases is (total elements - the maximum frequency of any element) + (max_freq - 1). Let's see. For example, in the second sample: total elements is 4, max frequency is 2 (for 100 and 200 each). Wait, wait, the frequencies are 2 for 100 and 2 for 200. So the maximum frequency is 2. Then (4-2) + (2-1) = 2 +1 =3. But the correct answer is 2. Hmm, that doesn't match. So maybe my initial hypothesis is wrong.

Wait, what's the formula here. Let's take another example. Suppose there's a case where one element occurs m times, and others are unique. For instance, n=5, elements [1,2,3,3,3]. Max frequency is 3. Then (5-3) + (3-1) = 2 + 2 =4. Let's see what's possible. The optimal arrangement could be 1,3,2,3,3. Then the increases are 1<3 (yes), 3>2 (no), 2<3 (yes), 3=3 (no). So two increases. But according to the formula, it would give 4. So that's not correct. So the formula isn't working here.

Hmm. So perhaps that approach isn't correct. Let me think again.

Another idea: the maximum number of increases possible is (n - k) where k is the maximum frequency. Because when elements are arranged in a way that the maximum frequency elements are spaced out. For example, in the second sample, maximum frequency is 2. So 4-2 =2. Which matches the answer. In the first sample, maximum frequency is 1, so 5-1=4. Which matches. Let's test with the earlier example. For [1,2,3,3,3], maximum frequency is 3. n=5. So 5-3=2. But the optimal arrangement would be 3,1,3,2,3. Then the increases are 1<3 (yes), 3>2 (no), 2<3 (yes). So two increases. Which matches the formula. So maybe the maximum possible increases is (n - max_freq). Wait, but wait.

Another example: n=3, elements [1,1,2]. Max frequency is 2. So according to formula, 3-2=1. The arrangement could be 1,2,1. Then 1<2 (yes), 2>1 (no). So one increase. Correct. Or 1,1,2: 1=1 (no), 1<2 (yes). Also one. So formula holds.

Another example: n=6, elements [a, a, a, b, c, d]. Max frequency is 3. So 6-3=3. How to arrange? Possible arrangement: a b a c a d. Then increases: a < b (yes), b > a (no), a < c (yes), c >a (no), a < d (yes). So three increases. Which matches.

So the formula seems to hold. So the maximum possible number of increases is (n - max_freq), provided that the maximum frequency is <= (n+1)/2. Wait, no. Wait, when the maximum frequency is m, then the arrangement is possible if m-1 <= (n - (m)) +1. Because the maximum allowed for m is (n+1)/2. For example, if m is 3, and n=5. Then 3 <= (5+1)/2 =3, which is okay. If m exceeds (n+1)/2, then it's impossible to arrange all elements such that no two same elements are adjacent, but in our problem, same elements adjacent do not contribute to increases, but we are trying to maximize the number of increases.

Wait, but in the problem, the arrangement can have same elements adjacent. For example, if the maximum frequency is more than (n+1)/2, then the maximum possible increases would be (n - m) if possible. Wait, but perhaps the formula is (n - k), where k is the maximum frequency. So the maximum possible increases is (n-1) - (k-1) = n -k. Wait, why?

Because when you have a frequency k for the maximum occurring element, you can arrange it such that each occurrence of that element (except possibly the first) is preceded by a different element. But perhaps this is not directly applicable.

Alternatively, the maximum possible increases is min( (sum of all frequencies except max) * 2 - 1, n-1 ). Hmm. Not sure.

But according to the examples and the formula (n - max_freq), it seems to hold. So the answer is the maximum between (sum of all other frequencies) and (max_freq -1). Or perhaps the answer is (n - max_freq) if the max_freq <= sum_others +1, otherwise (2*sum_others) +1.

Wait, perhaps the maximum number of increases is (n-1) - (max_freq -1 - (sum_others))). No, that's not clear.

Alternatively, the problem is similar to arranging the elements such that as many adjacent pairs as possible have increasing values. The maximum possible is when the elements are arranged in such a way that every possible transition that can be increasing is done.

Wait, but how?

Let me think differently. Let's count the number of duplicates. For example, the maximum number of increases is (n-1) minus the number of duplicates that cannot be placed to avoid a non-increase.

But this is vague.

Alternatively, here's the approach: the maximum number of increases is (n - 1) - (max_freq -1). Because, in the best case, the maximum frequency element can be arranged in such a way that between every two of them, there is another element. For example, if the max frequency is m, then you need at least (m-1) other elements to interleave. So, if (m-1) <= (sum_others), then the maximum number of increases is (sum_others) + (m-1) -1 = sum_others + m-2. Wait, not sure.

Alternatively, the optimal arrangement is possible when the elements are arranged in a way that each occurrence of the maximum frequency element (except the first) is placed after a different element. Then, between each pair of such elements, there's a different element. So, the number of increases would be (sum_others) + (m-1) - 1 + ... ?

Wait, perhaps I'm overcomplicating this.

Looking back to the examples. Let's see:

In the first example, n=5, all elements are unique. So the maximum increases is 4 (n-1). Which is (n-1).

In the second example, n=4. The frequencies are 2 for 100 and 2 for 200. So max_freq is 2. The answer is 2. Which is (4-2) = 2. So matches the formula.

Another example: n=3, elements [1,1,1]. Then max_freq is 3. So answer is 0. Which is 3-3=0. Correct.

Another example: n=6, elements [1,1,1,2,3,4]. Max_freq is 3. So answer would be 6-3=3. How to arrange: 1,2,1,3,1,4. The increases are 1<2 (yes), 2>1 (no), 1<3 (yes), 3>1 (no), 1<4 (yes). So 3 increases. Correct.

So the formula seems to hold. So the maximum possible is (n - max_freq). So the algorithm is: count the frequency of each element, find the maximum frequency. The answer is min( (n - max_freq) * 2 -1, n-1 ). Wait, no. Wait, in the first example, (n - max_freq) is 4, which is the correct answer. So why would it be min( (5-1) * 2 -1, 4 )? No, that's not the case.

Wait, perhaps the answer is simply (n - k), where k is the maximum frequency, but only if that is possible. Wait, no. For example, let's say the frequencies are such that k is 3 and the sum of others is 2. Then according to the formula, the answer is (3+2) -3 =2. But how?

Let's take n=5, elements [a,a,a,b,c]. Max_freq is 3. The answer according to the formula is 5-3=2. Let's arrange: a b a c a. The increases are a < b (yes), b > a (no), a < c (yes), c >a (no). So 2 increases. Which matches the formula. So yes.

But what if the sum of other elements is more than (k-1). For example, k=2, sum_others=3. Then (n -k) =3. The maximum possible increases is 3, which would be achieved by arranging in a way that each a is followed by a higher element, but perhaps there are more.

Wait, another example: elements [a,a,b,c,d]. Max_freq is 2. Sum_others is 3. So n=5. Answer is 5-2=3. Let's arrange as a b a c d. Then increases are a <b (yes), b>a (no), a <c (yes), c <d (yes). So 3 increases. Correct. Alternatively, a b c a d: increases are a <b, b <c, c> a (no), a <d. So 3 increases. So yes.

So it seems that the formula holds regardless of the sum of other elements. So the maximum possible is (n -k), where k is the maximum frequency.

Wait, but what if the sum of other elements is less than (k-1). For example, k=4, sum_others=2. Then n=6. Then according to formula, 6-4=2. Let's see. Arrange a b a c a a. Wait, but that's four a's. Let's arrange a b a c a. Then the arrangement has a followed by b (increase), then a (decrease), then c (increase), then a (decrease). So two increases. Which matches the formula.

But in this case, the sum_others is 2 (b and c) and k-1 is 3. So sum_others <k-1. So the formula works even in this case.

So the conclusion is that the maximum possible number of increases is (n - maximum frequency) if maximum frequency is <= sum_others +1. Wait, no. But according to the previous examples, even when sum_others is less than (k-1), the formula still holds.

So the correct answer is (n - max_frequency).

Wait, but in the second example of the problem, the sum_others is 2 (two 200s and two 100s: no, sum_others is 2 for 200, but the maximum frequency is 2. So (n - max_freq) is 4-2=2, which is correct.

So the answer is (n - maximum frequency of any element).

So the steps to solve the problem are:

1. Count the frequency of each element in the array.
2. Find the maximum frequency among them.
3. The answer is (n - max_frequency).

Wait, but let me check another case. For example, the input is [1,1,2,2,3,3]. So n=6. Each element has frequency 2. So the maximum frequency is 2. The answer would be 6-2=4. How to arrange? Let's see: 1,2,1,3,2,3. Then the pairs are 1<2 (yes), 2>1 (no), 1<3 (yes), 3>2 (no), 2<3 (yes). So 3 increases. But according to the formula, the answer should be 4. Hmm, this contradicts the formula.

Wait, in this case, what's the maximum possible?

Wait, perhaps a better arrangement is possible. Let's see: 1,2,3,1,2,3. The pairs are 1<2 (yes), 2<3 (yes), 3>1 (no), 1<2 (yes), 2<3 (yes). So 4 increases. Oh right! So the answer here is 4, which matches the formula. So the arrangement is possible. So the formula holds.

So in that case, the formula is correct. So the approach is correct.

So the problem reduces to counting the frequency of each element, finding the maximum frequency, and subtracting that from n. That gives the maximum possible number of increases.

Wait, but why? Because the maximum possible increases is when the elements are arranged in a way that the most frequent elements are spread out as much as possible, allowing for as many increases as possible. So the formula is (n - max_freq).

But why is that? Let's think.

The maximum possible increases is the number of elements that can be placed between the maximum frequency elements. Each of those can be part of an increase. For example, if the maximum frequency is k, then we can arrange the elements as x1, m, x2, m, x3, m, ... where m is the maximum frequency element. Each x is placed between two m's. Then, the increases are x1 < m (yes), m >x2 (no), x2 < m (yes), etc. But this gives (k-1) increases (each x_i < m). But the x's can also form their own increases. Wait, but how?

Alternatively, the arrangement can be made as follows: arrange the elements in a way that each occurrence of the maximum frequency element is followed by a different element, which is higher. For example, if the maximum element is m and there are other elements higher than m. But this depends on the actual elements.

Wait, perhaps the key insight is that the maximum number of increases possible is (n - max_freq) because, regardless of the arrangement, the maximum frequency elements can create at most (max_freq -1) non-increases. Thus, the total possible increases is (n-1) - (max_freq -1) ) = n - max_freq.

But that's an alternative way to see it. Because, in the best case, each occurrence of the maximum frequency element (except the first) creates a non-increase. So, the number of non-increases is (max_freq-1). Then, the total increases is (n-1) - (max_freq-1) = n - max_freq.

So this is the reasoning. So regardless of how you arrange the elements, the maximum possible increases is (n - max_freq). Because each time you have a maximum frequency element after another, you can't have an increase. But in the best arrangement, you can minimize the number of non-increases to (max_freq -1). Thus, the total increases is (n-1) - (max_freq -1) = n - max_freq.

So the problem is solved by this approach.

So the steps are:

- Count the frequency of each element.

- Find the maximum frequency.

- The answer is (n - maximum frequency).

So the code will be straightforward.

Let's test this with the sample inputs.

Sample 1:

5 elements, all unique. max_freq is 1. 5-1=4. Correct.

Sample 2:

4 elements, two 200s and two 100s. max_freq is 2. 4-2=2. Correct.

Another test case: [1,1,2,2,3,3]. max_freq is 2. 6-2=4. Correct.

Another test case: [1,1,1]. n=3. answer 0. Correct.

Another test case: [1,2,3,3,3]. max_freq=3. n=5. answer 5-3=2. Let's arrange: 3,1,3,2,3. increases are 1<3 (yes), 3>2 (no), 2<3 (yes). So 2 increases. Correct.

So the code can be written as follows:

Read n, read the list of a. Count the frequency of each element. Find the maximum frequency. Compute n - max_freq. Output that.

But wait, is that correct in all cases?

Another example: [1,1,2]. n=3. max_freq=2. 3-2=1. Which is correct, as possible arrangement is 1,2,1: one increase.

Another example: [1,1,1,2,3]. n=5. max_freq=3. 5-3=2. Arrange as 1,2,1,3,1. Increases are 1<2, 2>1 (no), 1<3, 3>1 (no). So two increases. Correct.

So the code should be:

Count the frequencies, take the maximum, subtract from n.

Thus, the code is straightforward.

Now, let's code this.

We can use a frequency dictionary. For Python, we can use collections.Counter.

So code steps:

Read n.

Read the list of a.

Create a Counter of a.

Find the maximum frequency in the Counter.values().

Output n - max_frequency.

But wait, what if there are multiple elements with the same maximum frequency?

For example, in the second sample, both 100 and 200 have frequency 2. Then the maximum frequency is 2. The code would output 4-2=2. Correct.

So the code will handle that correctly.

Thus, the code is simple.

Now, let's code this.

Test case 1:

Input:

5

20 30 10 50 40

The frequencies are all 1. Max is 1. 5-1=4. Correct.

Test case 2:

4

200 100 100 200

Count is 200:2, 100:2. Max is 2. 4-2=2. Correct.

Another test case where n=1: input is 1 and a single element. Output is 0, which is correct.

So the code handles all cases.

Thus, the solution is correct.
</think>

```python
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
if n <= 1:
    print(0)
else:
    freq = Counter(a)
    max_freq = max(freq.values())
    print(n - max_freq)
```