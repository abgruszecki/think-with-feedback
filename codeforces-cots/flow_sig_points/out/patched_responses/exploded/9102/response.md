<think>
Okay, so I need to solve this problem where I have to count the number of pairs of clients with opposite t values. Let's see the problem statement again to make sure I understand it correctly.

The problem says that two clients form an opposite couple if their t values are opposites. For example, if one is 3 and the other is -3. Also, 0 is considered opposite to itself. The order of the pair doesn't matter, so (a,b) is the same as (b,a) and should be counted once. Also, a client can't pair with themselves, but they can pair multiple times if there are multiple occurrences. Oh right, but the problem states that each couple is exactly two clients, but the same client can be in multiple couples. Like in the second example, three 0s give three pairs (0C2 combinations).

So the approach here is to count for each number x how many times -x appears, and multiply those counts, but we have to avoid double-counting. Wait, but how?

Wait, the problem says that the couples are considered the same if they differ in order. So for x and -x, each occurrence of x can pair with each occurrence of -x. But if x is the same as -x (like 0), then we need to count the combinations of choosing two distinct elements from the count of x. Because each pair (i,j) where i and j are different indices counts as one pair.

So here's the plan:

1. Create a frequency map (like a dictionary) that counts the occurrences of each t value.

2. For each key x in the frequency map:
   a. If x is 0, then the number of pairs is the combination of count(x) taken 2 at a time. Because 0's opposite is 0, and each pair of different indices is valid once.
   b. Otherwise, if x is positive, check if -x exists in the map. For each such pair, the total pairs are the product of count(x) and count(-x). But since x and -x are different, we can process each pair once (like x and -x). However, if we process both x and -x, we might double count. So we need to handle this by only considering pairs where x is less than -x or something like that. Wait, no. For example, if x is 3 and -3, then when x is 3, we multiply count(3) * count(-3). Then when x is -3, we would multiply count(-3) * count(3), which would add the same product again, leading to double counting. So we need to make sure that each pair is only counted once.

So the correct way is to iterate through each x once, and process pairs where x is less than -x, but wait, maybe not. Let's think.

Suppose we have x and y such that y = -x. For example, x is 3 and y is -3. So when processing x, we can multiply count[x] * count[y], and then when processing y, we might do the same. To avoid this, perhaps we should process pairs where x is positive and y is negative, but only for x > 0, and then y is -x. But how?

Alternatively, we can iterate through all unique x in the frequency map, and for each x where x < 0, we check if -x is present. Wait, but maybe it's easier to iterate through all x in the frequency map, and for each x, if x is not zero, check if -x is present. But to avoid double-counting, perhaps process x and -x only once. For example, when x is positive, process x and -x. When x is negative, skip. But how to determine that.

Alternatively, for each x in the frequency map, if x is positive and -x exists, then the product is count[x] * count[-x]. But for x and -x, we will process x=3 and x=-3, leading to adding the same product twice. So to prevent that, we can process x only when x is positive. So for x > 0, we check if -x exists. Then the total pairs for this pair is count[x] * count[-x]. For x=0, handle separately with combinations.

So steps:

- Create a frequency dictionary.

- Initialize total pairs to 0.

- For each key in the frequency dict:

   if key is 0:

      add (count * (count -1)) // 2 to total

   else if key is positive:

      if -key is in the frequency dict:

          total += count[key] * count[-key]

So this way, for each pair (3, -3), when key is 3, it's positive, we process. When key is -3, since it's negative, we don't process it. So this avoids double counting.

Yes, that's correct.

So that's the approach.

Now, considering the constraints. The input size can be up to 1e5, which is manageable. The time complexity is O(n), since we process each element once, then iterate through the frequency keys, which is O(k) where k is the number of unique t values. Since t ranges from -10 to 10, the frequency map will have at most 21 keys (from -10 to 10), so this part is negligible.

So the steps are:

Read n.

Read the list of t's.

Build a frequency dictionary using a Counter.

Initialize total = 0.

Handle the 0 case: if 0 is in the counter, compute c = count[0], add c*(c-1)//2 to total.

For each key in the counter:

   if key is positive and (-key) exists in the counter:

       total += count[key] * count[-key]

Return total.

Wait, that's exactly the case.

Let's check the examples.

First example:

Input:

5

-3 3 0 0 3

The frequencies are:

-3:1

3:3

0:2

So for key 0: 2*(2-1)/2 = 1.

Then for keys:

-3: it's negative, so skipped.

3: check if -3 exists. Yes, count[3] is 3, count[-3] is 1. So 3*1=3 added. 0's contribution is 1. So total is 1+3=4. Wait, but the sample output is 3. Wait, what's wrong here?

Wait the sample input's output is 3, but according to this calculation:

The 0's contribution is (2*1)/2=1. Then 3's contribution is 3 (since 3*1). Then total is 1+3=4. But the correct answer is 3. Oh wait, this is a problem.

Wait the first sample's correct answer is 3. So what's wrong here.

Wait the first sample input:

-3, 3, 0, 0, 3. So the pairs are (1,2), (1,5), (3,4). So three pairs.

But according to the code's approach:

The 0s contribute 1 pair (3,4).

The 3 and -3 count is 3*1=3 pairs. So total 1+3=4. But sample output is 3.

Wait that's a contradiction. So there's a mistake in the approach.

Wait, why? What's wrong here?

Ah! Oh wait, the first sample's input is -3,3,0,0,3.

So the elements are: indices 1: -3, 2:3, 3:0,4:0,5:3.

Opposite pairs are:

Between -3 and 3:

The first element (-3) can pair with the 3s (indices 2,5). So 2 pairs.

The third and fourth 0s: one pair.

So total is 2+1=3. But according to the code's approach, for the 3 and -3 case, the product is 3 (since count[3] is 3 and count[-3] is 1). But the code's approach would multiply 3 * 1 =3, but in reality, it's 1*-3 element (the first one) paired with 3's elements (the 3's are at positions 2,3,5). So 3 elements of 3, and 1 element of -3. So 3*1=3 pairs. Which would add 3 to the total. Plus the 0's 1 pair. So 4. But sample output is 3.

Wait this is a discrepancy. So why?

Ah, wait the first sample's output is 3. So according to the code's approach, the code would output 3+1=4, which is wrong. So there's a problem here.

So why is the sample's correct answer 3? Let's look at the note. The note says that in the first sample, the pairs are (1,2), (1,5), (3,4). So three pairs. So why does the code's approach give 4?

Because according to the code:

The 0's pair is (3,4) → 1.

The 3 and -3 pairs are 3 *1 =3 → three pairs. So total 1+3=4. But the correct answer is 3.

Wait this is a problem. So where is the error?

Ah! Oh right, because the code's approach counts the pairs between 3 and -3. But the sample's input includes -3 once and 3 three times. So according to the code, the product is 3 *1=3, which is 3 pairs. But in the sample, there are two such pairs: (1,2) and (1,5). The third pair from this product would be (the -3 with the third 3, which is position 5. Wait, but the -3 is position 1, and the 3's are positions 2,5, and another 3 (position 3? No, wait in the input, the sequence is -3,3,0,0,3. So the elements are:

index 1: -3

index 2:3

index3:0

index4:0

index5:3.

So the 3's are indices 2,5. So the count of 3's is 2? Wait no, the input is -3,3,0,0,3 → the third element is 0, the fifth is 3. So the list is:

t = [-3, 3, 0, 0, 3]

So the count for 3 is 2 (indices 2 and 5). So in the code's approach, the code would have count[3] as 2, count[-3] as 1. So product is 2 *1=2. So then total would be 1 (from 0s) + 2 (from 3 and -3) → 3. Which matches the sample.

But why did I earlier think that the code's approach would compute 3*1? Because I thought the count[3] was 3. But in the first sample input, the 3's are at positions 2 and 5. So the count of 3's is 2. So the product is 2*1=2. Which is correct.

Ah! So the code is correct. The problem was in my initial analysis. So why did I make a mistake here? Because in the sample input, the user wrote 5 numbers: -3,3,0,0,3. So how many 3's are there? Let's count:

The list is -3, 3, 0, 0, 3. So the 3's are the second and fifth elements. So count(3) is 2, count(-3) is 1. So code's approach would compute 2*1=2 for that pair, plus 1 from 0's. So 3 total, which matches the sample.

So why did I think that the code would output 4? Because I made a mistake in the sample input.

So the code is correct.

Another example: the second sample input is 3 0s. The code would compute count[0] =3. So the pairs are 3 choose 2, which is 3, which is correct.

So the code's approach is correct.

So the steps are:

- For each number, count frequencies.

- For 0: add combinations of count[0] choose 2.

- For each positive number x, if -x is present, add count[x] * count[-x].

Thus, the code should be:

Read n.

Read the list of t's.

Use a Counter to count frequencies.

Initialize total to 0.

Check if 0 is present. If so, compute c = count[0], add c*(c-1)//2 to total.

Then, for each x in the Counter:

   if x >0 and -x in counter:

       total += count[x] * count[-x]

Return total.

Yes, that should work.

Now, implementing this in Python.

But what about when x is negative? For example, x is -3. Then, in the code, x >0 is false, so it's skipped. So for x=3, if present, it's processed once.

So code is correct.

So the code would be:

Read n.

t = list(map(int, input().split()))

from collections import Counter

counts = Counter(t)

total = 0

# Handle 0 case

if 0 in counts:

    c = counts[0]

    total += c * (c -1) // 2

# Handle other pairs

for x in counts:

    if x >0:

        if -x in counts:

            total += counts[x] * counts[-x]

print(total)

Yes.

Let's test the first sample.

Sample 1:

Input:

5

-3 3 0 0 3

counts = { -3:1, 3:2, 0:2 }

0's contribution is 2*1//2 =1.

Then for x in counts:

x = -3: not x>0 → skip.

x=3: x>0, check -3 is present. counts[3] * counts[-3] = 2*1=2. Add to total → total becomes 1+2=3.

Then x=0: x>0 is false. So total is 3. Correct.

Sample 2:

Input:

3

0 0 0

counts[0] is 3. Contribution is 3*2//2=3. No other x>0. So total is 3. Correct.

Another test case where x and -x are both present multiple times.

For example, input 2 1 and 1. Then counts[1] is 3, counts[-1] is 2. Then the contribution would be 3*2=6. So for each 1 and -1 pair, 3*2=6 pairs.

Yes.

So the code is correct.
</think>

```python
import sys
from collections import Counter

def main():
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    counts = Counter(t)
    total = 0
    
    # Handle zero case
    zero_count = counts.get(0, 0)
    total += zero_count * (zero_count - 1) // 2
    
    # Handle other pairs
    for x in counts:
        if x > 0 and -x in counts:
            total += counts[x] * counts[-x]
    
    print(total)

if __name__ == "__main__":
    main()
```