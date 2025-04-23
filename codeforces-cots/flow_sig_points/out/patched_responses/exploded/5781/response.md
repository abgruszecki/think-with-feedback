<think>
Okay, let's see. We have this problem where we need to process a functional graph and compute for each node the sum and the minimum of the weights along a path of length k starting from that node. The constraints are pretty tight: n can be up to 1e5 and k up to 1e10. So a naive approach where we simulate each step for each node would be way too slow. We need something smarter here.

Hmm. Functional graphs have the property that each node has exactly one outgoing edge. So the structure is made up of cycles and trees directed towards the cycles. For each node, after some steps, it will enter a cycle. So when k is larger than the steps needed to reach the cycle, the rest of the path loops around the cycle. This makes me think that binary lifting (or exponentiation) might be the way to go here. Because with binary lifting, we can precompute jumps of powers of two steps, allowing us to compute the sum and min for any number of steps efficiently.

Right. Binary lifting is a technique where we precompute for each node, the result of jumping 2^j steps ahead, along with aggregated information like sum and min. Then, when we need to compute a path of length k, we can break it down into a sum of powers of two, and combine the precomputed data.

So the plan is:

1. Precompute for each node and each power of two (up to log2(k)), the destination node after 2^j steps, the total sum of those steps, and the minimum weight along those steps.
2. For each starting node, decompose k into binary, and use the precomputed tables to accumulate the sum and min for the entire path.

Let's think about how to structure this. The binary lifting tables will need to store for each step j (like 1, 2, 4, 8, etc.) the next node, sum up to that step, and min. For example, for j=0 (1 step), each entry would be the direct next node, the weight, and the weight itself. For higher j, we can combine previous steps. Like, for j=1 (2 steps), the sum is the sum of the first step and the sum of the next step, and the min is the minimum of the two steps' mins.

Wait, but when combining two jumps of 2^j steps each, the sum is the sum of both parts, and the min is the minimum of both parts. So for example, if we have a jump of 2^j steps followed by another 2^j steps, the total sum is sum1 + sum2, and the total min is min(min1, min2). So the binary lifting tables for each node and each j should store the sum of 2^j steps and the minimum in those steps, as well as the node you end up at after those steps.

So the steps would be:

- Precompute a table for each node, for j from 0 to log2(k_max). Here, log2(k_max) is up to around 34 since k can be 1e10 (2^34 is about 1.7e10). So for each node, we need to store for each j up to 34, the destination, sum, and min.

Once this table is built, for a given k, we can process each bit in the binary representation of k. For each bit that is set, we apply that jump and accumulate the sum and min.

So for each node, starting from the initial node, we check each bit of k from the highest to the lowest. For each bit set, we take the corresponding jump (like 2^j steps), add the sum to the total sum, take the min between the current min and the min from the jump, and move the current node to the destination of the jump. This way, after processing all bits, we have the total sum and min after exactly k steps.

This approach would have a time complexity of O(n log k) for precomputing the tables, and O(n log k) for processing all nodes, which should be acceptable for n=1e5 and log k up to 34 (so total operations around 1e5 * 34 * 2 = 6.8e6, which is manageable).

Now, how to implement this in Python.

First, read the input: n and k, then the f array and the w array.

Then, precompute the binary lifting tables. Let's call them up, sum_table, min_table. Each is a list of lists, where up[j][i] is the node you get to after 2^j steps from i, sum_table[j][i] is the sum of those steps, and min_table[j][i] is the min weight in those steps.

Initialize the tables for j=0 (2^0 steps, which is 1 step):

- up[0][i] = f[i]
- sum_table[0][i] = w[i]
- min_table[0][i] = w[i]

Then, for each j from 1 to max_level (which is log2(k) rounded up), compute the tables for j based on j-1. So for each i:

up[j][i] = up[j-1][up[j-1][i]]
sum_table[j][i] = sum_table[j-1][i] + sum_table[j-1][up[j-1][i]]
min_table[j][i] = min(min_table[j-1][i], min_table[j-1][up[j-1][i]])

Once the tables are built, for each node i, we can process the k steps by breaking it into its binary components. For each bit in k's binary representation, if the bit is set, we take that jump and accumulate the sum and min.

But how to handle the binary decomposition of k? For each node, we can start with current_node = i, current_sum = 0, current_min = infinity. Then, for each bit position j from 0 to max_level, if (k & (1 << j)) is non-zero, then we add sum_table[j][current_node] to current_sum, take the min of current_min and min_table[j][current_node], and update current_node to up[j][current_node].

Wait, but the bits need to be processed from the highest to the lowest. Because each bit represents a power of two, and higher bits are larger. So we need to iterate j from highest to 0.

So first, precompute the maximum level needed. For example, find the highest j where 2^j <=k. Then, for each j starting from that level down to 0, check if the j-th bit is set in k.

Wait, but how to get the binary decomposition of k? We can loop through each bit of k, starting from the highest possible (like 60 bits for 1e10, which is 34 bits as 2^34 is 1.7e10). For each j in 0 to max_level, check if the j-th bit is set in k.

So the steps for each node i:

Initialize sum_total = 0, min_total = infinity, current_node = i.

For j from 0 to max_level:

Wait, no. Because the binary lifting tables represent steps of 2^j. So to build k steps, we need to process the bits of k from LSB to MSB? Or from MSB to LSB? Wait, the binary lifting approach uses that each bit in the binary representation of k represents a power of two, which can be combined. For example, to compute 5 steps (binary 101), we take the 4-step jump (if that bit is set), then the 1-step jump. So processing the bits from highest to lowest.

Wait, binary lifting is similar to exponentiation by squaring. So in this case, for each bit in the binary representation of k, starting from the highest to the lowest. So for example, if k is 5 (101), we first check the highest bit (which is 4, 2^2). Then the next bit (2^1, which is 0), then the last (2^0, which is 1). So we process 4 steps, then 1 step.

But to handle this correctly, we need to track the current position, and for each set bit, apply the corresponding jump.

So for each node i:

sum_total = 0

min_total = infinity

current_node = i

remaining = k

for j in reversed(range(max_level+1)):

    if (remaining >= (1 << j)):

        sum_total += sum_table[j][current_node]

        min_total = min(min_total, min_table[j][current_node])

        current_node = up[j][current_node]

        remaining -= (1 << j)

But since k can be up to 1e10, and the bits are up to 34, this loop would run 34 times per node.

But wait, how to precompute the sum and min for each possible 2^j step. So the tables are built up for each j, and then for each node, the jumps are combined based on the bits of k.

Yes.

So in code:

First, determine the maximum level needed. For k=0, no steps. But since k is at least 1, the maximum level can be calculated as the floor of log2(k), but perhaps it's easier to precompute up to 60 levels (since 2^60 is way bigger than 1e10). But in Python, for k up to 1e10, the maximum exponent needed is 34 (since 2^34 is ~1.7e10, which is larger than 1e10).

But to find the maximum level needed, we can compute the highest j where 2^j <=k. Let's say we compute it as bits = k.bit_length().

Wait, for example, k=3 is 11 in binary, so bits is 2. But 1<< (bits-1) is 2, and 1<<bits is 4. So the maximum level is bits-1.

So in code, max_level = 0. While (1 << (max_level+1)) <=k: max_level +=1.

Alternatively, in Python, max_level can be calculated as k.bit_length() -1 if k>0 else 0.

So in code, if k is 0, but the problem says k is >=1.

So for the code, first, precompute the binary lifting tables up to max_level.

Now, the problem is that for n=1e5 and max_level=34, each table (up, sum, min) will be of size 34*1e5. Which is 3.4e6 entries. For each entry, we store an integer, which in Python could be a list of lists. Each list for level j will have n elements.

But for Python, storing 34 lists each of 1e5 elements is manageable. Let's see: 34*1e5*3 (up, sum, min) = 1.02e7 elements. Each integer is 28 bytes (for small ints in Python), but even so, this is around 28*1e7 = 280MB, which may be acceptable given the memory limit of 512MB. But perhaps in Python, the way lists are stored can be a bit more efficient. Let's proceed.

So in code:

n, k = map(int, input().split())

f = list(map(int, input().split()))
w = list(map(int, input().split()))

max_level = 0
if k >0:
    max_level = k.bit_length() -1
    while (1 << max_level) >k:
        max_level -=1
    # Now 2^max_level is the highest power of 2 <=k.

But wait, in Python, the bit_length() returns the number of bits required to represent the integer in binary, excluding the sign and leading zeros. So for example, 3 (binary 11) has bit_length() of 2, 4 (100) has 3. So for k >=1, the maximum level is (k.bit_length() -1) if 2^(bit_length()-1) <=k. Wait, 2^(bit_length()-1) is the highest power of two <=k. Because for example, 5 (101) has bit_length 3. 2^(3-1) is 4, which is <=5.

So max_level can be computed as (k.bit_length() -1). But perhaps in code, to make sure, we can calculate it as (k.bit_length() -1) if k>0.

But perhaps even better: the maximum level needed is the highest j where (1 << j) <=k. So in code:

max_level = 0

while (1 << (max_level+1)) <=k:

    max_level +=1

But for k=0, but the problem says k is >=1. So code can handle that.

Once max_level is determined, we can precompute the tables.

Initialize up, sum_table, min_table.

up is a list of lists, where up[j] is the nodes after 2^j steps.

Similarly for sum_table and min_table.

In Python, for efficiency, perhaps use separate lists for each level. But given that in Python list comprehensions are efficient, perhaps preallocate.

But for n=1e5 and max_level up to 34, this is manageable.

So code:

up = []
sum_table = []
min_table = []

# Initialize level 0 (2^0 =1 steps)
up.append(f.copy())
sum_table.append(w.copy())
min_table.append(w.copy())

for j in range(1, max_level+1):
    prev_up = up[j-1]
    prev_sum = sum_table[j-1]
    prev_min = min_table[j-1]
    current_up = []
    current_sum = []
    current_min = []
    for i in range(n):
        mid = prev_up[i]  # after 2^(j-1) steps from i
        current_up.append(prev_up[mid])  # after another 2^(j-1) steps
        current_sum.append(prev_sum[i] + prev_sum[mid])
        current_min.append(min(prev_min[i], prev_min[mid]))
    up.append(current_up)
    sum_table.append(current_sum)
    min_table.append(current_min)

Wait, but for j=1, each entry is computed by combining two steps of 2^(j-1) =1 steps. So for each i, after 2 steps, the destination is prev_up[prev_up[i]], the sum is sum_table[j-1][i] + sum_table[j-1][prev_up[i]], and the min is the min of the two steps.

Yes. So for each j, building the next level based on the previous.

But for j from 1 to max_level, including max_level.

Once this is built, then for each node i, we need to process k steps by decomposing into binary.

But here's a possible problem: if k is larger than the sum of the maximum steps in the tables, but the tables are built up to the maximum required j. Wait, no: the tables are built up to j where 2^j is the largest power of two <=k. Then, the binary decomposition of k would require all bits up to that j.

Wait, but for example, if k is 5, which is 101 in binary, the highest j is 2 (since 2^2=4 <=5, and 2^3=8>5). Then, max_level=2. So when building up to j=2, the tables for j=0,1,2 are available.

So when processing each node, we loop through j from max_level down to 0. For each j, if the current remaining steps (initially k) has (1<<j) <= remaining, then take that step.

So in code:

for each i in 0..n-1:

    current_node = i

    s = 0

    m = infinity

    remaining = k

    for j in range(max_level, -1, -1):

        if remaining >= (1 << j):

            s += sum_table[j][current_node]

            m = min(m, min_table[j][current_node])

            current_node = up[j][current_node]

            remaining -= (1 << j)

    print(s, m)

But wait, how do we check if the j-th bit is set in k? Because the decomposition is in terms of the bits of k. For example, if k is 3, which is 11 in binary, then the bits at j=1 and j=0 are set. So in this approach, we process each j from highest to lowest, and subtract the 2^j when possible.

But this code would correctly accumulate the sum and min, regardless of the order, as long as the bits are processed in order. For example, in the code above, for j from max_level down to 0, and if the remaining steps is >= 2^j, then apply that step.

But why not process from the highest possible? Because the sum of the steps would correctly accumulate, and the current_node would be updated after each step.

Yes. For example, with k=5 (101), j=2 (4 steps) is first processed. Then remaining becomes 1. Then j=0 (1 step) is processed.

Thus, for each node, the code would process the steps in log2(k) time.

This seems correct.

But what about the case where k is 0? Well, according to the problem statement, k is at least 1, so we don't need to handle that.

Now, the code for building up the tables. But in Python, for n=1e5, and max_level=34, building the tables for j from 1 to 34 would take O(34 * n) time. Each iteration for j is O(n), which is acceptable.

But let's check for j=34, n=1e5: 34 * 1e5 = 3.4e6 operations, which is manageable.

Now, possible optimizations:

- Precompute the maximum level needed. For example, if k=0, but the problem says k >=1.

- Preallocate the tables. But in Python, list comprehensions and appending may be efficient enough.

Another possible optimization is to precompute all the required bits for k once, and then loop through them. But the code above does that implicitly by checking the remaining steps.

Now, let's test the code against the sample inputs.

First sample input:

7 3

f = [1,2,3,4,3,2,6]

w = [6,3,1,4,2,2,3]

For each node i, we need to compute the sum and min of the next 3 steps.

Let's take node 0:

Step 1: 0 ->1 (weight 6). sum=6, min=6.

Step 2: 1->2 (3). sum=9, min=3.

Step3: 2->3 (1). sum=10, min=1.

So output is 10 1, which matches the sample.

Another example: node 6.

Path: 6->6 (since f[6] is 6, so it's a cycle). Step 1: 6->6 (3). Step 2: same. Step3: same. So sum is 3*3=9. Min is 3. Which matches the sample.

Another sample input:

4 4

f = [0,1,2,3]

w = [0,1,2,3]

Each node i steps 4 times. For node 0: it's a cycle of 1. So each step is 0. So sum is 0*4=0, min 0. Which matches the sample.

Another sample input:

5 3

f = [1,2,3,4,0]

w = [4,1,2,14,3]

For node 0:

Path is 0->1->2->3. Weights are 4,1,2. Sum is 7. Min is 1.

Which matches the sample.

So the code seems to handle these cases.

Now, considering possible edge cases. For example, when a node is in a cycle of length l, and k is larger than l. The code would correctly sum the cycle steps, using binary lifting.

Another case is when k is exactly a power of two. The code would process it as a single jump.

So, the code should work.

Now, in Python, for handling 1e5 elements, and building up 34 levels, the code needs to be efficient. But in Python, list comprehensions and for loops can be a bit slow for 1e5 elements. But given that the time limit is 2 seconds, and the code is O(n log k), which is 1e5 * 34 = 3.4e6 operations, that's manageable.

But there's a possible issue with memory. For each of the 3 tables (up, sum_table, min_table), each level is a list of n integers. So for 34 levels, each of 1e5 elements, each table uses 34 * 1e5 * 4 bytes (if integers are stored as 4 bytes, but in Python, integers are objects, which take more memory). However, the memory limit is 512MB. But in practice, for 3 tables * 34 levels * 1e5 elements, each element is an integer. Let's estimate:

Each integer in Python can take up 28 bytes (for small integers). So 3 * 34 * 1e5 * 28 = 3 * 34 * 1e5 = 1.02e7 elements. 1.02e7 *28 = 28.56e7 bytes, which is 285.6MB. Plus the other variables, it's within the 512MB limit.

But in Python, using lists of lists might be manageable.

Another possible optimization is to precompute each level in a way that avoids creating a new list each time, but that's not critical.

Now, implement the code in Python.

But wait, when initializing up[0], sum_table[0], min_table[0], we need to copy f and w. But in Python, f is a list of integers, so up[0] = f.copy() (but f's elements are the next nodes). sum_table[0] is the w array.

Then, for each j from 1 to max_level, we compute each level based on the previous.

But in Python, when building up the tables, for each j, we can create a new list for each level.

But for n=1e5, each list for a level is 1e5 elements, and for 34 levels, this is 34 * 1e5 elements per table.

So the code should proceed as:

Read n and k.

Read f as a list of integers.

Read w as a list of integers.

Compute max_level.

Initialize up, sum_table, min_table.

For each j from 1 to max_level, build the tables.

Then, for each node i, process the bits of k.

Now, in Python, when building the up, sum_table, min_table for j levels, we can do:

But for j in 1 to max_level:

prev_up = up[j-1]

prev_sum = sum_table[j-1]

prev_min = min_table[j-1]

current_up = [prev_up[prev_up[i]] for i in range(n)]

current_sum = [prev_sum[i] + prev_sum[prev_up[i]] for i in range(n)]

current_min = [min(prev_min[i], prev_min[prev_up[i]]) for i in range(n)]

But for n=1e5, list comprehensions might be slow. Because for each j level, we have to iterate 1e5 elements.

But in Python, list comprehensions are faster than for loops. So perhaps using list comprehensions here is better.

But for j=34, each level would require 3 * 1e5 operations, which for 34 levels would be 1.02e7 operations. Which in Python should be manageable in 2 seconds.

But let's test with an example.

Wait, the first sample input:

max_level for k=3 is 1 (since 2^1=2 <=3, and 2^2=4>3). So j=1 is the highest. So the tables are built for j=0 and j=1.

For j=1, each entry is computed as follows: for node i, jump 2 steps.

For example, node 0:

j=0: up[0][0] is 1. sum is 6, min is6.

j=1: up[1][0] is up[0][up[0][0]] = up[0][1] =2. sum is 6+3=9. min is min(6,3)=3.

But in the code, for each j, the up, sum, min are built correctly.

Now, when processing k=3 (binary 11), the code would process j=1 (2 steps) and j=0 (1 step). For each node, sum and min are added.

So the code should work.

Another possible edge case is when k=1. Then max_level is 0, and for each node, we take j=0 once.

Another case is when k is 2^j -1, like 3=2^2-1, but the code would process the bits 2^1 (2 steps) and 2^0 (1 step) for a total of 3 steps.

So the code should handle that.

Thus, the code seems correct.

So the final code is as follows:
</think>

```python
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    f = list(map(int, sys.stdin.readline().split()))
    w = list(map(int, sys.stdin.readline().split()))
    
    if k == 0:
        for _ in range(n):
            print(0, 0)
        return
    
    max_level = 0
    if k > 0:
        max_level = k.bit_length() - 1
        while (1 << max_level) > k:
            max_level -= 1
    
    # Initialize tables for binary lifting
    up = [f.copy()]
    sum_table = [w.copy()]
    min_table = [w.copy()]
    
    for j in range(1, max_level + 1):
        prev_up = up[j-1]
        prev_sum = sum_table[j-1]
        prev_min = min_table[j-1]
        current_up = []
        current_sum = []
        current_min = []
        for i in range(n):
            mid = prev_up[i]
            current_up.append(prev_up[mid])
            current_sum.append(prev_sum[i] + prev_sum[mid])
            current_min.append(min(prev_min[i], prev_min[mid]))
        up.append(current_up)
        sum_table.append(current_sum)
        min_table.append(current_min)
    
    # Process each node
    for i in range(n):
        current = i
        total_sum = 0
        min_val = float('inf')
        remaining = k
        for j in range(max_level, -1, -1):
            if remaining >= (1 << j):
                total_sum += sum_table[j][current]
                if min_table[j][current] < min_val:
                    min_val = min_table[j][current]
                current = up[j][current]
                remaining -= (1 << j)
        print(total_sum, min_val)

if __name__ == "__main__":
    main()
```