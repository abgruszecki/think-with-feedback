<think>
Okay, let's see. We need to find the minimum number of operations to get at least k equal numbers in the array by dividing elements by two (flooring them). Each operation is a division by two, and we can choose any element any number of times.

Hmm. The idea is to track for each possible number, how many steps it would take to get other elements to reach that number. Then, for each possible number, collect the steps required from enough elements (at least k) and take the sum of the smallest k steps. The minimum among all such sums is the answer.

So the steps are as follows:

1. For each element in the array, generate all possible values it can take by dividing by two repeatedly, along with the number of steps taken to reach each value. For example, if the element is 5, the values would be 5 (0 steps), 2 (1 step), 1 (2 steps), 0 (3 steps), etc.

2. For each of these values, store the steps required in a dictionary or a list. Then, for each value, if there are at least k elements that can reach it, sum the k smallest steps and track the minimum such sum.

The challenge is to efficiently compute this for all possible values without exceeding time or memory limits, given that n can be up to 2e5.

Wait, how do we handle this efficiently? For each element, generating all possible values it can take would be O(log a_i) steps per element. Since a_i can be up to 2e5, log2(2e5) is around 18, so per element it's manageable. So for 2e5 elements, that's about 3.6e6 operations, which should be okay.

Once all possible values and their steps are generated, we can use a hash map (like a defaultdict(list)) where the key is the possible value, and the value is a list of steps needed for elements to reach that value. Then, for each key in the map, if the list's length is at least k, we sort the list, take the first k elements' sum, and keep track of the minimum such sum.

So the steps would be:

- Initialize a defaultdict(list) called counts.

- For each number in the array:
   - Initialize steps as 0.
   - While the current value is >=0:
      - Add steps to counts[value].
      - If current value is 0, break (since next division would still be 0, but steps would keep increasing, but adding those would be unnecessary as 0 can't be divided further).
      - Otherwise, divide by 2, steps +=1.

Wait, but when the value is 0, we can't divide anymore. So for each element, we generate all the values until we reach 0, but once it's 0, we stop. Because after that, each division would keep it at 0 but steps would increase, but those steps are unnecessary. So for example, if an element is 3, the steps would be:

3 (0 steps), 1 (1 step), 0 (2 steps). Then we stop. Because if we keep dividing 0 by 2, it's 0, but each step adds a step. So adding those steps would not be helpful, as 0 can be achieved in 2 steps. Any further steps would be more steps than necessary, so including them in the list for 0 would be adding higher steps, which are worse options. So, to avoid those, once we reach 0, we add it once (with the current step count) and break.

Wait, but for example, if the element is 0 initially (though according to the input constraints, a_i is at least 1?), the initial input has a_i >=1. Oh, right, the problem statement says that the input array elements are between 1 and 2e5. So the initial elements are all >=1. So in processing each element, we can generate all possible values until 0, but once it's 0, we add it once and break.

So for each element a_i:

current = a_i
steps = 0
while True:
   add (current, steps) to the map
   if current ==0:
       break
   current = current //2
   steps +=1

So this loop will process all possible values the element can take. For example, if a_i is 5:

5 (0 steps) → 2 (1) → 1 (2) → 0 (3 steps). Then stop.

So for each element, the loop runs log2(a_i) +1 times. For a_i up to 2e5, that's about 18 steps per element.

So total steps are O(n log a_i), which for n=2e5 is acceptable.

Once all these steps are stored in the map, for each key (possible target value) in the map, we check if the list of steps has at least k elements. If so, we sort that list, take the first k elements (smallest steps), sum them, and keep track of the minimum sum across all such keys.

The key part here is that for each possible target value, we need to collect all the steps that elements take to reach it, then sum the k smallest steps. The minimal sum across all possible target values is our answer.

Yes. That makes sense.

So the steps are:

1. Preprocess each element to generate all possible (value, steps) pairs.

2. For each possible value, collect all steps in a list.

3. For each value's list that has length >=k, compute the sum of the first k entries (sorted) and track the minimum.

So the time complexity is:

- O(n log a) for preprocessing.

- Then, for each possible value, sorting the list of steps. The number of possible values is O(n log a), but each steps list is of length O(n) in the worst case (if all elements generate the same value). But for each such list, sorting would take O(m log m) time, where m is the size of the list.

But considering that for n=2e5 and each element contributing up to 18 steps, the total number of entries in the map is O(n log a), which is about 3.6e6. Then, for each entry in the map, if the list has m elements, sorting m elements takes O(m log m) time. But for the worst case, if a value is generated by all elements (like 0), then m is 2e5. So sorting that would take O(m log m) = 2e5 * 18 ≈ 3.6e6 operations, which is acceptable. But for all other values, m is smaller.

So the total time for sorting is O(total entries log m), but perhaps it's manageable. The worst case would be if all elements have the same path towards 0, but that's unlikely. But even then, the total steps would be O(n log a) + O(n log n), which for 2e5 is acceptable.

But wait, the sum for each value's list is the sum of the first k elements. So for each list of steps, we can keep track of the steps as we add them, perhaps in a sorted manner. But since we add steps from each element in arbitrary order, it's easier to collect all steps for a value and then sort them when needed.

So the plan is:

- Use a dictionary to collect for each possible value the list of steps required to reach it.

- Once all elements are processed, iterate through each key in the dictionary.

- For each key, if the list's length is >=k, sort the list, sum the first k elements, and update the minimum.

So in Python, the code would look like:

from collections import defaultdict
import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

counts = defaultdict(list)

for num in a:
    current = num
    steps = 0
    while True:
        counts[current].append(steps)
        if current == 0:
            break
        current = current // 2
        steps += 1

min_ops = float('inf')

for key in counts:
    lst = counts[key]
    if len(lst) >= k:
        lst.sort()
        sum_ops = sum(lst[:k])
        if sum_ops < min_ops:
            min_ops = sum_ops

print(min_ops)

But wait, let's test this code against the examples.

First example:

Input:
5 3
1 2 2 4 5

Processing each number:

1:

current=1, steps=0 → add to 1: 0 steps. Then current becomes 0, steps=1 → add to 0: 1 step.

Wait no. Let's re-examine the code:

For num=1:

current starts at 1.

Loop:

add (1, 0) → counts[1].append(0)

current is 1, not zero. So current = 0 (1//2=0), steps becomes 1.

Next iteration:

add (0, 1) to counts[0], then check if current is 0 → break.

So for 1, the counts entries are 1: [0], 0: [1].

Similarly, let's process all numbers.

But perhaps the code is correct.

In the first example, the answer is 1.

Looking for the key that has at least 3 elements.

In the first example:

Looking for 2. Let's see:

The elements that can reach 2:

Original 2's can reach 2 in 0 steps. The 4 can reach 2 in one step (4 → 2). The 5 can reach 2 via 5 →2 (steps=1). Wait, 5//2 is 2, but steps would be 1. So the elements 2,2,4,5 would generate 2 with steps 0,0,1,1.

But how?

For the first two 2's in the array, each contributes steps 0 when generating 2. The 4 is divided once (4→2, steps=1). The 5 is divided once (5→2, steps=1). So counts[2] would have [0, 0, 1, 1]. Then when k=3, the sum of the first three (sorted) is 0+0+1=1. Hence the answer.

But in the code, when processing 2 in the array, current is 2, steps 0. Then 2//2=1, steps 1. Then 1//2=0, steps 2. So for the first 2:

counts[2].append(0)
current becomes 1, steps 1 → counts[1].append(1)
current becomes 0, steps 2 → counts[0].append(2)
then break.

Wait, no. The code for processing each number:

For example, num=2:

Loop:

current = 2, steps=0 → add to counts[2] → [0]

current is not 0, so divide by 2 → 1, steps becomes 1.

Next loop: add 1 with steps 1 to counts[1].

current is 1, divide by 2 → 0, steps 2.

Add 0 with steps 2 → counts[0].append(2).

Then break.

So for the two 2s in the input, each would generate 2 in 0 steps, but also 1 in 1 step, and 0 in 2 steps.

So the counts for 2 would have entries from the two 2s. Each 2 contributes to counts[2] as 0 steps. So counts[2] would have two 0 steps from the two 2s. The 4 in the input would be processed as:

4 → steps 0 (counts[4].append(0)), then 2 (steps 1 → counts[2].append(1)), then 1 (steps 2 → counts[1].append(2)), then 0 (steps 3 → counts[0].append(3)).

The 5 would be processed as:

5 → steps 0 (counts[5].append(0)), then 2 (steps 1 → counts[2].append(1)), then 1 (steps 2 → counts[1].append(2)), then 0 (steps 3 → counts[0].append(3)).

So for the key 2 in the counts, the steps list would be [0 (from first 2), 0 (from second 2), 1 (from 4), 1 (from 5)]. So len(lst) is 4 >=3. Sorting gives [0,0,1,1]. Sum first 3: 0+0+1=1. Which matches the first example's output.

So the code works here.

Another example:

Second input:

5 3

1 2 3 4 5

Looking for which numbers can have at least 3 elements contributing steps.

Looking at the counts:

Let's see for 1:

Each element can reach 1 through division.

For 1 → steps 0.

2 → steps 1 (2→1).

3 → steps 1 (3→1).

4 → steps 2 (4→2→1).

5 → steps 2 (5→2→1).

So steps list for 1 is [0,1,1,2,2]. Sum of first 3 is 0+1+1=2. Which is the answer.

So in the code, the sum for key 1 is 2, which is the correct answer.

So the code works for this case.

Third example:

5 3

1 2 3 3 3

The answer is 0, because there are three 3s already. So counts[3] would have three 0 steps. Sum is 0.

Yes.

So the code works.

Now, considering the constraints. For n=2e5, and each element generating up to 18 entries in the counts dictionary, the total number of entries is about 3.6e6. Then, for each of these entries, when processing, we may have to sort the list. The worst case is for a key that has 2e5 entries (like 0), which would take O(m log m) time. For m=2e5, this is 2e5 * 18 ≈ 3.6e6 operations, which is acceptable.

But in Python, sorting a list of 2e5 elements can take some time, but given that in practice, the per-test-case time is acceptable.

Now, for the code, using a defaultdict(list) is the right approach.

But in Python, appending to the list is O(1) (amortized), so the initial processing is manageable.

But for the lists, perhaps pre-sorting is better. But in the code, we sort the list each time when we check for a key. But for a key that's processed multiple times, like 0, we may process it once. So the code is correct.

Potential optimizations:

- When building the counts, for each element, generate all possible values and steps. Then, for each key in counts, sort the list once and then compute the sum.

Yes. For example, when building the counts, for each key, the steps list is unsorted. Then, when processing each key, we check if the list's length is >=k. If so, sort it, take the first k elements' sum.

But this can be optimized by pre-sorting each list once. However, since for a given key, the list is built by appending steps from multiple elements, which may not be in order. So we need to sort each list once.

In Python, the code as written is correct. But to handle large inputs efficiently, perhaps we can pre-sort each list as we build them. But that's not feasible, because steps are added for each element in the order of processing.

Another possible optimization is to keep the lists sorted as we insert elements. For example, using a priority queue or inserting in the right position. But for each insertion, that would be O(n) time, which is not feasible. So it's better to collect all steps and then sort once.

So the code as written is correct and efficient.

Testing edge cases.

Edge case 1: n=1, k=1. The answer is 0. The code would process the element, generate all possible steps, then for the key (the element itself) the sum is 0.

Edge case 2: All elements are 1. Then, counts[1] has n entries, all 0 steps. Sum is 0.

Edge case 3: k=3, elements 8, 8, 8. So steps for 8 is 0, so sum is 0.

Another case where elements can reach a value in varying steps.

But the code handles all these.

Now, about the time constraints. Let's calculate for n=2e5, each element generating 18 steps. So counts will have 3.6e6 entries in total. Then, for each entry, if the list's length is >=k, we sort it. The worst case is a key with 2e5 elements. Sorting that list takes O(2e5 log 2e5) steps, which is about 2e5 * 18 = 3.6e6 operations, which is acceptable. Then, for all keys, this would sum up to O(3.6e6 log m) steps. But since each list is sorted once, and the average list size is perhaps small (like log n), the total time is manageable.

In Python, the sort function is optimized, so even with 2e5 elements, it's acceptable.

Now, in Python, lists can handle 2e5 elements without issue. Memory-wise, each list stores integers. For 3.6e6 elements in total, each list's entries are integers. So 3.6e6 integers is about 28MB (since each int is 28 bytes in Python), but considering that for 2e5 elements, each with 18 steps, it's 3.6e6 entries. 3.6e6 * 28 bytes is about 100MB, which is within the memory limits (256MB). So the code is memory efficient.

Another possible optimization is that, when building the counts, for each number, we can collect the steps in reverse order, but that's not necessary.

In conclusion, the code is correct and efficient.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    counts = defaultdict(list)
    
    for num in a:
        current = num
        steps = 0
        while True:
            counts[current].append(steps)
            if current == 0:
                break
            current //= 2
            steps += 1
    
    min_ops = float('inf')
    
    for key in counts:
        lst = counts[key]
        if len(lst) >= k:
            lst.sort()
            current_sum = sum(lst[:k])
            if current_sum < min_ops:
                min_ops = current_sum
    
    print(min_ops)

if __name__ == "__main__":
    main()
```