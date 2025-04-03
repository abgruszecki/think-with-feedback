<think>
Okay, let's tackle this problem. So, the task is to find the maximum length of a strictly increasing sequence by taking elements from either the left or right end of the array each time. And then output the sequence of moves (L or R) that achieves this.

First, I need to understand the approach. Since each element is distinct and all are from 1 to n, perhaps there's a pattern here. Wait, the array is a permutation of 1..n. That's important.

The key is that the sequence we take must be strictly increasing. So each next element we take must be larger than the last. Let's think about how to model this.

Let me think about possible approaches. One common approach for such two-pointer problems is to greedily choose the smaller possible next element. But wait, no. Wait, because we need the sequence to be strictly increasing, so each next element must be larger than the previous. So the first element is the smallest possible. Then, each subsequent element must be the next possible in the sequence.

Wait, maybe not. Because the sequence must be as long as possible. So we need to choose elements in such a way that each next step picks the smallest possible element that's larger than the last, but considering that we can take from either end.

Alternatively, perhaps the problem can be viewed as finding the longest possible path where each step is choosing left or right such that the selected element is larger than the previous. The optimal path here would be the one that allows the maximum length.

But how do we model this? The brute force approach would be to consider all possible choices at each step, but with n up to 2e5, that's impossible. So we need a smarter approach.

Let me think. Since the array is a permutation of 1 to n, each number is unique and the sequence must form a strictly increasing sequence. The maximum possible length is n, which is possible only if the array is already sorted in increasing order. For example, if the array is 1,2,3,4,5, then taking all left (LLL) gives the sequence 1,2,3,4,5, which is strictly increasing.

But when the array is not sorted, the maximum length depends on the possible paths we can take. Let's think about how to model this.

Another idea: the problem is similar to finding the longest increasing subsequence (LIS), but with the constraints that the elements must be taken from the ends. So the LIS approach won't directly work here.

Wait, but the LIS approach uses dynamic programming. Maybe here we can model the problem using a two-pointer approach with some dynamic programming. Let's see.

Suppose we have two pointers, left and right, at the current ends of the remaining array. At each step, we can choose either left or right, but the chosen element must be larger than the last one taken.

But how do we track the last element taken and the possible left and right pointers? This seems like a problem that could be O(n) time, but we need to find a way to model it.

Let's think about the possible cases. Let's denote that the last element taken was 'last'. The next element must be larger than 'last'. The possible choices are the leftmost or the rightmost element of the current array.

So the problem reduces to choosing between left and right such that the chosen element is larger than 'last', and the resulting path is the longest possible.

But how to compute this efficiently?

An alternative approach: since the elements are a permutation of 1..n, the maximum possible sequence would be 1,2,3,...,k, where each next element is the next number. Wait, no. Because the order in the array may not allow that. But perhaps the sequence is determined by the order of the numbers in the array.

Wait, perhaps the optimal sequence starts with the minimal possible element. Because once you take a higher element, you can't take any smaller elements after that. So maybe the optimal strategy is to start with the minimal possible, then the next minimal possible in the remaining elements that can be taken from either end.

But how to find the longest possible sequence.

Another idea: the problem is similar to the greedy approach for LIS where you build the sequence by taking the smallest possible next element.

Wait, here's an example from the first sample input: [2,1,5,4,3]. The optimal sequence is 2,3,4,5. The next elements after 2 could be 1 (but 1 is smaller) or 3 (from the right). So the choice is to take 3. Then from the remaining elements [1,5,4], the next element can be 4 (right) then 5 (right). So the sequence is built by taking the next possible element that's larger than the last, and allows the longest possible continuation.

But how to model this decision process.

Let me think about the algorithm. Let's try to model the possible choices at each step, but in a way that can be computed efficiently.

Here's an approach:

Initialize two pointers, left=0 and right=n-1. The current sequence is empty. The last value is -infinity.

We need to choose either a[left] or a[right], whichever is larger than last, and allows the maximum possible sequence length. Then, proceed recursively.

But this approach would be O(2^n), which is not feasible. So we need a way to compute this in linear time.

Alternative approach: since the elements are a permutation, perhaps the optimal sequence is a consecutive sequence of numbers starting from some x, and increasing by 1 each step. But not sure.

Wait, perhaps the optimal sequence can be formed by taking elements from either end such that each next element is the smallest possible possible value that is larger than the last. This way, we allow more choices for future steps.

For example, if after taking the current element, the next possible elements are 3 and 5. Taking 3 allows the next step to take 4 if available, whereas taking 5 would not allow any elements between 5 and 5 (since all are unique). So taking the smaller possible next element (3) would allow a longer sequence.

This suggests a greedy approach where, at each step, we choose the smaller of the two possible options (left and right) that is larger than the last, as long as that choice allows a longer sequence.

But how to implement this.

Wait, here's an idea inspired by the two-pointer approach:

We can greedily choose the smaller possible element between left and right, provided that it's larger than the last. Then proceed. The idea is that by taking the smaller possible next element, we can maximize the remaining options for subsequent steps.

So the steps would be:

Initialize left = 0, right = n-1.

current_last = 0 (or the initial element's value minus 1)

result = []

While left <= right:

    if a[left] > current_last and a[right] > current_last:

        choose the smaller of the two, append the direction (L or R), update current_last and the pointer.

    elif a[left] > current_last:

        take left, append L, current_last = a[left], left +=1

    elif a[right] > current_last:

        take right, append R, current_last = a[right], right -=1

    else:

        break.

But does this work? Let's see the first sample input:

Sample 1: [2,1,5,4,3]

Initial left=0 (2), right=4 (3). current_last is 0.

a[left] is 2 >0, a[right] is 3>0. So we choose the smaller one, which is 2. Append L. current_last becomes 2. left becomes 1 (value 1). Now, in next step, left is 1, right is4. a[left] is 1 (<=2), a[right] is3>2. So take R. append R. current_last is3. right becomes3 (4). Now, left is1 (1), right is3 (4). a[left] is1 <=3, a[right]4>3. So take R. append R. current_last is4. right becomes2 (5). Now, left is1 (1), right is2 (5). both 1 and5 are >4. take the smaller one, 5 is not smaller than 5? Wait, wait, 5 is larger than current_last (4). So choose the smaller between a[left] and a[right] which are 1 and5. Wait, a[left] is1, which is less than current_last 4? So only a[right] is 5>4. So in this step, the code would take 5 (right). append R. So the sequence becomes LRRR. Which is the correct sample output. Then, after taking 5, current_last is5. Now left is1, right is2. The remaining elements are [1,5]. But both are 1 (left) and5 (right). Both are <=5. So we stop. So the sequence is 4 elements. Which matches the sample.

Hmm, but wait in the sample, the code would proceed to take 3,4,5. Wait, the sample's output is 2,3,4,5. So how does that happen?

Wait, the sample input is [2,1,5,4,3]. Let's walk through:

After taking 2 (L), the array becomes [1,5,4,3]. Then take right (3) (R). current_last is3. Then take right (4) (R). current_last is4. Then take right (5) (R). current_last is5. So the sequence is 2,3,4,5. Which is correct.

But according to the code I thought of earlier, after taking 3 (R), the next options are [1,5,4]. The left is 1 (a[left] is1, which is <=3. So the code would take the right, which is4. Then current_last is4. The next elements are [5]. So take R (5). So sequence is LRRR, which is correct.

So the code seems to work for that case.

Another sample input: the third sample is [1,2,3], output LLL. So the code would take left (1), then left (2), then left (3). Correct.

Another sample input: 1 2 4 3. Output is 4, LLRL. Let's see:

Initial array: [1,2,4,3]. The code would take left (1), then left (2), then right (3) would be invalid (since current_last is2. 4 is larger, so take left (4), append L. Then right is3, which is larger than4. So take R. So the sequence is 1,2,4,3. Wait but that's not increasing. Oh wait no. Wait the sample output is LLRL. Let's see the actual steps:

Wait, the correct output for input 4 is 4 elements, LLRL. So the sequence is 1,2,4,3. But that's not strictly increasing. Wait that can't be. Oh no, I must have made a mistake. Wait the sample input is [1,2,4,3], and the output is 4. So how is that possible?

Wait the sample input is 4: [1,2,4,3]. The output is LLRL, which would take elements as follows: L (1), L (2), R (3), then L (4)? Wait no. Wait the array is [1,2,4,3]. Let's see the steps:

First L: take 1. Remaining array [2,4,3]. Then L: take 2. Remaining array [4,3]. Then R: take 3. Next, the remaining array is [4]. So take L (4). So the sequence is 1,2,3,4. Wait that's strictly increasing. So the steps are LLLR. Wait but the sample output is LLRL. Wait maybe there's another way. Hmm.

Wait the sample output is 4, LLRL. Let's see:

First L:1. Remaining [2,4,3]. Then L:2. Remaining [4,3]. Then R:3. But 3 is larger than 2, yes. Then take L (4). So the sequence is 1,2,3,4. So the moves are L, L, R, L → "LLRL". Oh right. Because after taking 3 (from the right), the remaining array is [4]. So the next move is L (take 4). So the sequence is indeed 1,2,3,4. So the code's approach would work here.

So in this case, the code's approach would proceed as follows:

Initial left=0 (1), right=3 (3). current_last=0. Both 1 and3 are >0. Take the smaller one (1, left). Now current_last=1, left=1.

Next left=1 (2), right=3 (3). Both 2 and3 >1. Take the smaller (2, left). current_last=2. left=2. Now, left=2 (4), right=3 (3). a[left]=4>2, a[right]=3>2. So choose the smaller between 4 and3. The smaller is3. So take right (R). Append R. current_last=3. right=2. Now left=2, right=2. a[left] is4>3. Take L. Append L. So the sequence is L L R L. Which matches the sample.

So this suggests that the greedy approach of taking the smaller of the two possible options (when both are available) works correctly.

But how to implement this. Let's think.

The algorithm is:

Initialize left and right pointers.

current_last starts at 0 (or -infinity, as long as it's smaller than any possible element).

result is an empty list.

loop:

if left > right: break.

Check if the left and right elements are larger than current_last.

If both are larger:

   choose the one with the smaller value (since taking the smaller allows more options in the future). Because if you take the larger one, then the next step may have no options left. For example, if left is 3 and right is4, and current_last is2. Taking 3 allows next steps to take 4, but taking4 would leave 3, which can't be used.

So choosing the smaller one is better.

So append 'L' if left element is smaller, else 'R'.

Update current_last to that element's value. Move the pointer accordingly.

If only one is larger than current_last:

   take that element, append direction, move pointer.

else:

   break.

So the code would look something like:

left = 0

right = n-1

last = -infinity

result = []

while left <= right:

    if a[left] > last and a[right] > last:

        if a[left] < a[right]:

            result.append('L')

            last = a[left]

            left +=1

        else:

            result.append('R')

            last = a[right]

            right -=1

    elif a[left] > last:

        result.append('L')

        last = a[left]

        left +=1

    elif a[right] > last:

        result.append('R')

        last = a[right]

        right -=1

    else:

        break

return the length of result and the string.

But wait, let's test this code against the sample inputs.

Sample 4: [1,2,4,3]

Steps:

left=0, right=3, last=-inf. Both 1 and3 > last. a[left]=1 is smaller than a[right]=3. So append L, last=1. left becomes1.

Now, left=1 (2), right=3 (3). Both 2 and3>1. a[left] is2 <3. Append L. last=2. left=2.

Now left=2 (4), right=3 (3). Both 4 and3>2. a[left] (4) is larger than a[right] (3). So append R. last=3. right=2.

Now left=2 and right=2 (4). a[left]=4>3. So append L. last=4. left=3. Now left>right. Loop ends.

Result is 'LLRL', which matches the sample.

Another sample: input 7

Sample input 7: [1,3,5,6,7,4,2]

The output is 7, LRLRLLL.

Wait according to the code, how would this proceed.

The array is [1,3,5,6,7,4,2]. Let's walk through.

Initialize left=0, right=6. last is -inf.

Take left (1), append L. left=1. last=1.

Next, left=1 (3), right=6 (2). Both 3 and2 are larger than 1. So compare 3 and2. Take the smaller, which is2. Append R. right=5. last=2.

Now, left=1 (3), right=5 (4). Both 3 and4>2. Take 3 (append L). last=3. left=2.

Now, left=2 (5), right=5 (4). 5>3,4>3. take smaller (4). But wait, wait, a[right] is4. So take R. append R. last=4. right=4.

Now, left=2 (5), right=4 (7). 5>4,7>4. take the smaller (5). append L. left=3. last=5.

Now, left=3 (6), right=4 (7). both larger than5. take the smaller (6). append L. left=4. last=6.

Now, left=4 (7), right=4 (7). take L. append L. left=5. last=7. Now, left=5 is4, but 4<7. So check if any elements are left. left is5 (4), right=4. left>right. loop ends.

Wait, but according to the sample output, the sequence is 7 elements. So the code's approach would collect 1,2,3,4,5,6,7. How?

Wait, maybe I made a mistake in the code's logic.

Wait sample input 7's output is LRLRLLL. Let's see the steps according to that:

1. L: take 1.

2. R: take 2 (from the right end).

3. L: take 3.

4. R: take 4 (from the right end after 3 is taken? Or wait, the array after taking 3 (left) would be [5,6,7,4,2]. Then R would take 2 again? Wait, maybe I need to re-examine.

Alternatively, perhaps the code's approach isn't sufficient for all cases. Let's see.

The sample input 7's array is [1,3,5,6,7,4,2]. The optimal sequence is all 7 elements, which implies that the entire array can be taken in a strictly increasing sequence. So the sequence is 1,3,5,6,7,4,2. But that's not possible as that's not increasing. So perhaps the correct sequence is 1,2,3,4,5,6,7. But how is that possible given the array.

Wait, the sample output's sequence is LRLRLLL, which implies:

L (take 1), R (take 2), L (take3), R (take4), L (take5), L (take6), L (take7). So the sequence is 1,2,3,4,5,6,7. But how does that work with the array.

Let's see the steps:

Original array: [1,3,5,6,7,4,2]

Step 1: L → 1. Remaining array [3,5,6,7,4,2].

Step 2: R → 2. Now, the remaining array is [3,5,6,7,4]. But 2 is larger than 1. Then next step: take L (3) which is larger than 2. Then R (4) which is larger than3. Then L (5), which is larger than4. Then L (6), then L (7). So the sequence is 1,2,3,4,5,6,7. So the moves are L, R, L, R, L, L, L. Which is LRLRLLL. Which matches the sample.

But according to the code's approach, how would this be handled.

Let's see:

After step 1: left=0 (1), right=6 (2). both are >-inf. Take L, code proceeds.

Now, left=1 (3), right=6 (2). current_last=1. a[left] is3>1, a[right] is2>1. Both are larger. The code would take the smaller of 3 and2, which is2. So append R. current_last=2. right=5 (4). So the code's approach would take R here.

Now, left=1 (3), right=5 (4). Both 3 and4>2. Take the smaller (3). Append L. left=2 (5). current_last=3.

Next step: left=2 (5), right=5 (4). 5>3,4>3. take the smaller (4). Append R. current_last=4. right=4 (7).

Next step: left=2 (5), right=4 (7). 5>4,7>4. take 5 (append L). current_last=5. left=3 (6).

Next step: left=3 (6), right=4 (7). 6>5,7>5. take 6 (append L). current_last=6. left=4 (7).

Next step: left=4 (7), right=4 (7). take L. append L. current_last=7. left=5.

Now, left=5 is beyond right=4. loop ends. So the code's approach would have 6 steps: L, R, L, R, L, L, L? No, wait the code would have steps:

1. L (1) → len=1.

2. R (2) → len=2.

3. L (3) → len=3.

4. R (4) → len=4.

5. L (5) → len=5.

6. L (6) → len=6.

7. L (7) → len=7.

So the code's approach would collect all 7 elements, and the string would be L R L R L L L. Which is LRLRLLL. Which matches the sample. So the code works here.

So it seems that the code's approach works for the samples. So perhaps this is the correct approach.

But why does this approach work? Let's think about the correctness.

The key idea is that whenever both ends are possible (i.e., both are larger than the last taken element), we choose the smaller one. This allows the next step to have as small a value as possible to take next, thereby maximizing the possible remaining choices.

For example, if you have a choice between 3 and 4, taking 3 allows you to take 4 later (if available), but taking 4 would not allow you to take 3. Hence, taking the smaller one gives more options in the future.

This is a classic greedy approach where choosing the locally optimal choice (smallest possible next element) leads to a globally optimal solution.

Thus, the algorithm is correct.

Now, let's consider the implementation. The code should be straightforward, using two pointers and a loop.

But since n can be up to 2e5, the code must run in O(n) time. The code as described runs in O(n) time, as each step either moves left to the right or right to the left, and each is processed once.

Now, let's code this in Python.

Read n, read the array. Then left=0, right=n-1. last is initialized to a value smaller than all possible elements (like 0). Then, the loop as described.

Now, for handling the output, we can collect the 'L' and 'R's in a list, then output the length and the joined string.

Testing edge cases:

Test case when the array is sorted in increasing order. Then all left moves. For example, input 3: [1,2,3]. Code takes L, L, L. Correct.

Test case when the array is sorted in decreasing order. For example, n=3, [3,2,1]. Then first take left (3). Then next elements (2 and1) are smaller than 3. So sequence length is 1. But wait, but if we take right (1) first. Wait, the code would start with comparing left (3) and right (1). Both >0. Take the smaller (1). So append R. current_last=1. Then left=0 (3), right=1 (2). Both 3 and2>1. Take the smaller (2). Append R. current_last=2. Then left=0 (3). Take L. current_last=3. So sequence is RRL, length 3. So the code would output 3, RRL.

But wait, the array is [3,2,1]. How can you take 3 elements? Because 1>2>3 is not increasing. Wait no. The sequence would be 1, 2,3? But how? Because after taking 1 (right), the array becomes [3,2]. Then taking 2 (right), array becomes [3]. Then take 3 (left). The sequence is 1,2,3. Which is increasing. So the code's approach works here.

So the code works even if the array is in reverse order.

Another edge case: n=1. Output is 1, L.

Another case: n=2, [2,1]. The code takes left (2) and then right (1) is invalid. So sequence is length 1. But if you take right (1), then left (2) is invalid. So maximum is 1. But wait, no. Wait, the array is [2,1]. The possible sequences are taking 2 (L) → sequence [2], or taking 1 (R) → [1]. So maximum length is 1. But according to the code, initial step: left=0 (2), right=1 (1). Both >0. Take the smaller (1). Append R. current_last=1. Then left=0 (2) is larger than 1. So take L. current_last=2. So sequence is RL, which is 1,2. So length 2. Wait, but how?

Wait, in the array [2,1], the code would proceed as:

left=0 (2), right=1 (1). Both are >0. Take the smaller (1). Append R. current_last=1. Then left=0 (2) which is >1. Take L. append L. So the sequence is RL. The elements taken are 1 and2. Which is increasing. So the code would output 2, RL. Which is correct. So in this case, the code produces the optimal solution.

So the code works for this case.

Hence, the code seems to handle all cases correctly.

Now, let's write the code.

Read n.

Read the array as a list.

left=0, right= n-1.

current_last=0.

result = []

while left <= right:

    if a[left] > current_last and a[right] > current_last:

        if a[left] < a[right]:

            result.append('L')

            current_last = a[left]

            left +=1

        else:

            result.append('R')

            current_last = a[right]

            right -=1

    elif a[left] > current_last:

        result.append('L')

        current_last = a[left]

        left +=1

    elif a[right] > current_last:

        result.append('R')

        current_last = a[right]

        right -=1

    else:

        break

Then, print the length of result, followed by the string.

Let's confirm with a testable snippet.

```python
def test_program(input_stream, output_stream):
  n = int(input_stream.readline())
  a = list(map(int, input_stream.readline().split()))
  left = 0
  right = n - 1
  last = 0
  res = []
  while left <= right:
      if a[left] > last and a[right] > last:
          if a[left] < a[right]:
              res.append("L")
              last = a[left]
              left += 1
          else:
              res.append("R")
              last = a[right]
              right -= 1
      elif a[left] > last:
          res.append("L")
          last = a[left]
          left += 1
      elif a[right] > last:
          res.append("R")
          last = a[right]
          right -= 1
      else:
          break
  print(len(res), file=output_stream)
  print("".join(res), file=output_stream)

import io

TEST_CASES = [{
    "input": """\
5
2 1 5 4 3\
""",
    "output": """\
4
LRRR\
""",
}, {
    "input": """\
7
1 3 5 6 7 4 2\
""",
    "output": """\
7
LRLRLLL\
""",
}, {
    "input": """\
3
1 2 3\
""",
    "output": """\
3
LLL\
""",
}, {
    "input": """\
4
1 2 4 3\
""",
    "output": """\
4
LLRL\
""",
}, ]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    test_program(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, \
        f"Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}"

print("Tests passed!")
```

RUN_SNIPPET
```text
Traceback (most recent call last):
  File "<stdin>", line 109, in <module>
AssertionError: Test case 1 failed.
Expected: '7\nLRLRLLL'
Got: '7\nLRLRLLR'
```

Wait, the second test case failed.