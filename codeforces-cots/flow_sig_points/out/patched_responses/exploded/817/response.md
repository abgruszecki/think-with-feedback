<think>
Okay, let's try to figure out this problem. The goal is to find the minimum time required to combine all the initial chains into a single chain, following the allowed operations. The operations are either nesting two outer dolls (costing 1 second) or extracting a doll from its immediate container (also 1 second). So, we need to model the steps needed and find the optimal way.

First, let's understand the initial and desired states. The initial state has k chains. The desired state is a single chain 1→2→3→…→n. So each doll must be nested such that each subsequent doll is the container of the previous. 

Hmm. Let's think about each existing chain. For each chain in the initial configuration, if it's already part of the desired sequence, then maybe we can save some steps. For example, if there's a chain that's a consecutive sequence starting from 1, like 1→2→3, then we can use that as a base and add the remaining dolls around it. Otherwise, we might have to break down the chain.

Wait, the problem statement says that in the initial configuration, each chain's dolls are in ascending order. So each chain is a sequence like a1 < a2 < ... < am. But in the desired configuration, it's the entire sequence from 1 to n. So, the desired chain is the maximum possible chain.

So the key idea here is to find the longest consecutive sequence in the initial chains. Because that part can be kept as is, and we only need to break the other parts. Let me explain.

Suppose there's a chain that is a consecutive subsequence in the desired order. For example, in the first sample input, the chain is 1→2. The desired final chain is 1→2→3. So the existing 1→2 can stay as a part of the final chain. Then, we only need to nest the 3 chain into the 1→2 chain. That takes 1 operation (nesting the 1→2 into 3, but wait, no— wait, the 1→2 is already a chain, and 3 is a single doll. So to nest 1→2 into 3, which is allowed if 3 is not nested. So in this case, since 3 is not part of any other chain, the first operation is to put 1→2 (as a single unit, but since they are already nested) into 3. Wait, but the first operation allows nesting a into b, where a is a chain and b is another chain. But in this case, 3 is a single doll. So putting 1→2 into 3 would take 1 second.

But how does that work? Because 1→2 is already a chain, and 3 is a single doll. So you can take the outermost doll of the 1→2 chain (which is 2) and the 3, and since 2 can be nested into 3 (since 2 <3), you can perform the operation. But wait, the initial chain is 1→2. So the 2 is the outermost. So to nest into 3, you can do that in one step, which combines both chains into 1→2→3. That's why the first sample's output is 1.

So the key insight here is that if there exists a consecutive sequence in the initial chains that forms a prefix of the desired chain, then we can save some steps. The maximum such sequence is called the "maximal existing chain" and the length of this chain minus 1 (since each consecutive pair in the chain requires no extraction) determines how many operations we can avoid.

Wait, perhaps the steps required are calculated as follows:

The total steps required to disassemble all chains into individual dolls plus the steps to assemble them into the desired chain. But when there's an existing consecutive chain that is part of the desired chain, we don't have to disassemble that part. So the steps saved would be the number of operations needed to disassemble and reassemble that part.

Wait, let's think differently. Let's model each chain in the initial configuration. For each chain, if it has a consecutive sequence starting from 1, like 1,2,3, then each of those consecutive elements can be part of the final chain. The longer this consecutive sequence, the fewer steps we need.

The total number of steps needed is: the sum for each chain of (the number of elements in the chain -1) [because each chain of m elements requires m-1 extract operations to disassemble into individual dolls], plus (n-1) steps to assemble all into the desired chain. But if there is a consecutive sequence of length L (like 1,2,...,L), then the initial chains that form parts of this sequence can contribute to saving steps. For example, if there's a chain that starts with 1, then the consecutive elements in that chain up to some L would form a base, and those elements don't need to be disassembled. So the steps saved would be (L-1) for disassembly (since they are already in the correct nested order) and (L-1) for the assembly steps. So the total steps saved would be 2*(L-1). 

But how to calculate L? L is the length of the longest consecutive sequence starting at 1 that is present in some initial chain. For example, in the first sample, the chain is 1→2. L is 2. So steps saved would be 2*(2-1) = 2. So original steps would be (sum of (mi-1) for all chains) + (n-1) = (1 (from first chain) + 0 (second chain)) ) + 2 = 1 + 2 =3. Then subtract 2*(2-1) = 2. 3-2=1, which matches the sample.

Wait, let's see. The sum of (mi-1) is (2-1) + (1-1) =1+0=1. Then add (n-1) =3-1=2. Total steps would be 1+2=3. Then subtract 2*(L-1) where L=2. So 2*(1) =2. 3-2=1. So that's the answer.

So the formula would be:

Total steps = (sum (mi-1 for all chains) ) + (n-1) - 2*(L-1)

Where L is the maximum length of the consecutive sequence starting at 1 in any of the chains.

So how to compute L? For each chain, check if the chain contains a sequence 1,2,...,x. Then the maximum x is L.

For example, in the first sample, the first chain is 1,2. So L is 2.

In the second sample, let's look at the input:

7 3

3 1 3 7

2 2 5

2 4 6

So the chains are:

1 →3→7

2→5

4→6

So in the first chain, the first element is 1. The next is 3, which is not consecutive. So the consecutive sequence here is just 1. Then, in the second chain, the first element is 2. But there's no 1 before it. So the consecutive sequences in the chains are:

First chain: 1 (since next is 3 which is not 2)

Second chain: 2 (since next is 5, which is not 3)

Third chain: 4 (since next is 6, but no 5 before it)

So the maximum L here is 1. So the formula gives:

sum (mi-1) for each chain is (3-1)+(2-1)+(2-1) = 2+1+1=4.

Add n-1 =6. Total steps before saving: 4+6=10. Then subtract 2*(1-1) =0. So 10, which matches the sample.

So the algorithm is:

1. Find L, which is the maximum length of the consecutive sequence starting at 1 in the initial chains. For example, if a chain has elements 1,2,3, then L is 3. If a chain has 1,3, then L is 1.

2. The total steps is (sum of (mi-1) for all chains) + (n-1) - 2*(L-1).

So how to compute L?

We can process each chain. For each chain, iterate through the elements and check if they form consecutive numbers starting from 1.

Wait, no. Because the chain could start with 1, followed by 2, etc. So for each chain, we can check if the first element is 1. If not, ignore this chain. If it is, then we check how long the consecutive sequence starting at 1 is.

For example, chain 1,2,3,5: the consecutive sequence is 1,2,3. So L would be 3.

Another example, chain 1,3,4: consecutive sequence starts at 1 but next is 3, so L is 1.

So, for each chain that starts with 1, we can check the consecutive sequence in the chain. The maximum L across all such chains is the value we need.

So the steps are:

- For each chain, check if the first element is 1. If not, skip.

- If it is 1, then iterate through the chain's elements to see the maximum consecutive sequence starting at 1. For example, chain [1,2,3,4], then the consecutive sequence is 4. So L is 4.

- Among all chains, find the maximum L.

Once we have L, compute the formula.

Now, the sum of (mi-1) is the number of extraction steps needed to break down all chains into individual dolls. Because for each chain of length m, you need m-1 extractions to get all dolls out. For example, a chain of 3 dolls a→b→c: to extract a, you need to take out a from b (operation 2), then take out b from c (operation 2 again). So two steps for a chain of 3. Which is m-1.

Then, once all dolls are individual, you need to assemble them into the target chain, which takes n-1 steps (each step nests a doll into the next).

But if there's a consecutive sequence of L in the initial chains, then during the assembly process, those L dolls are already in order. So the steps saved are:

- For the L dolls: you don't have to break them down (saving L-1 steps) and you don't have to assemble them (saving L-1 steps). So total saved steps are 2*(L-1).

Hence the formula.

So the main steps are:

1. Read all the chains.

2. For each chain, check if it starts with 1. If yes, compute the maximum consecutive sequence starting from 1.

3. Find the maximum L among all chains.

4. Compute the sum of (mi-1) for all chains.

5. The answer is sum + (n-1) - 2*(L-1).

Yes, that makes sense.

Now, the problem is to implement this efficiently.

Constraints: n up to 1e5, k up to 1e5.

Each chain's elements are in ascending order. So the elements in a chain are given as a sequence where each is larger than the previous.

So, for a chain starting with 1, we can check the consecutive elements. Let's say the elements are [a1, a2, ..., am]. For consecutive sequence starting at 1, we need a1=1, a2=2, a3=3, etc. So for each element in the chain after the first, if it's exactly one more than the previous, then the sequence continues.

For example:

Chain [1,2,3,5]. The consecutive sequence is 3 elements (1,2,3). So L=3.

Chain [1,3,4,5]. L is 1, since after 1 comes 3, which is not 2.

So, for a given chain, the code to compute L would be:

current_max = 1 (since the first element is 1)

for i from 1 to len(chain)-1:

    if chain[i] == chain[i-1] +1:

        current_max +=1

    else:

        break

So, for that chain, the current_max is the L.

We need to find the maximum L across all chains.

Once that is found, proceed.

Now, in terms of code:

Read n and k.

sum_mi_minus_1 = 0

max_L = 0

for each of k chains:

    read mi and the list of ai's.

    sum_mi_minus_1 += (mi -1)

    if the first element is 1:

        current_L =1

        for j in 1 to mi-1:

            if ai[j] == ai[j-1] +1:

                current_L +=1

            else:

                break

        if current_L > max_L:

            max_L = current_L

So, after processing all chains, compute:

answer = sum_mi_minus_1 + (n-1) - 2*(max_L -1)

If there's no chain starting with 1, then max_L is 0, but according to the formula, that term is 2*(0-1) = -2, which would add 2 to the answer. But that's not possible. Wait, no.

Wait, if there's no chain starting with 1, then max_L is 0 (since no chain starts with 1). But according to the formula:

sum_mi_minus_1 + (n-1) - 2*(0-1) = sum + (n-1) + 2. But that would be wrong. Wait, but in reality, if there's no chain starting with 1, then the initial chains must all be broken down, and the final assembly is from scratch, which is sum_mi_minus_1 (all disassembled) plus n-1 steps for assembly. But in this case, max_L is 0, so the formula gives sum + (n-1) - 2*(-1) = sum + (n-1) +2. Which is incorrect. So there's a mistake here.

Wait, perhaps my initial reasoning was wrong. Let's think again.

Ah! Oh right. The L represents the length of the maximal consecutive sequence starting at 1. So, if there's no chain starting with 1, then L is 0. Because the consecutive sequence can't start. Wait no, the consecutive sequence starts at 1, but if 1 is not present in any chain, then L is 0. But according to the problem statement, all chains have distinct numbers, so 1 must be present in exactly one chain.

Wait, the problem says that the sum of mi is n and all numbers are distinct. So 1 must be in exactly one chain.

So if 1 is in a chain, then L can be at least 1. So in the code, max_L is initialized as 0, but after processing all chains, one of them will have 1 as the first element. So max_L will be at least 1.

Wait, no. For example, if 1 is the second element in a chain, then that chain starts with a higher number, so when processing that chain, we don't check for consecutive sequence. But according to the problem statement, the chains are given in ascending order. So the chain that contains 1 must start with 1, right? Because the chain is a nested sequence where each subsequent number is larger than the previous. So the chain must be in strictly increasing order. So the chain that contains 1 must start with 1, then 2, etc. Because the problem says, "in each chain the numbers of matryoshkas follow in the ascending order". So the elements in the chain are in ascending order, but not necessarily consecutive.

So for example, a chain could be [1,3,4], but then the next elements are larger than previous. So if 1 is in a chain, then the first element of that chain is 1.

Ah, right! Because the chains are stored in ascending order. So the first element is the innermost doll, and each next is nested inside it. So the order in the chain is a1 → a2 → ... → am, where a1 < a2 < ... < am. So the chain is in strictly increasing order, but not necessarily consecutive. But in order for 1 to be in a chain, it must be the first element of that chain, because all elements in the chain are increasing. So the chain that contains 1 must start with 1. Otherwise, if 1 is somewhere in the middle, then the elements before it would have to be less than 1, which is impossible. Therefore, the chain containing 1 must start with 1.

So, the code can safely check for the chains where the first element is 1. Because 1 can only be the first element of a chain.

Therefore, the code will process that chain to find the maximum consecutive sequence.

So in all cases, the chain containing 1 has 1 as the first element, and thus, the code will process it and set max_L to at least 1.

Therefore, the formula will be correct.

So, in code:

We read the k chains. For each, check if the first element is 1. If yes, then compute the consecutive sequence starting at 1.

Then sum (mi-1) for all chains. Then calculate the answer.

Now, code-wise, how to process the chains efficiently.

In Python, for each chain, the code can read the list of elements, check if the first is 1, then iterate through the list to see how many consecutive numbers starting from 1 are present.

But for chains that are large (up to 1e5 elements in total across all chains), this could take O(n) time, which is acceptable since n is 1e5.

So the code is manageable.

Now, let's test the examples.

First example:

Input:

3 2

2 1 2

1 3

Processing the first chain: starts with 1. The elements are [1,2]. Check consecutive:

2 is 1+1, so consecutive. So current_L is 2. So max_L is 2.

Second chain: starts with 3. Ignore.

sum_mi_minus_1 is (2-1)+(1-1) =1 +0=1.

Answer: 1 + (3-1) - 2*(2-1) =1+2 -2=1. Correct.

Second example:

Input:

7 3

3 1 3 7

2 2 5

2 4 6

Chains:

First chain: 1,3,7. Starts with 1. Check consecutive. Next element is 3, which is not 2. So current_L is 1.

Second chain: starts with 2. Ignore.

Third chain: starts with4. Ignore.

sum_mi_minus_1: (3-1)+(2-1)+(2-1) =2+1+1=4.

n-1=6.

answer:4+6 -2*(1-1) =10-0=10. Correct.

Another test case: if a chain starts with 1,2,3,4. Then L=4. The sum would be sum(mi-1) for this chain (4-1=3) plus others. Then answer is sum + n-1 - 2*(4-1) =3+ others sum + (n-1) -6.

Which would save 6 steps.

Thus, the code seems correct.

So the code can be written as:

Read n and k.

sum_mi_minus_1 =0

max_L=0

for each of the k chains:

    read mi and the list of a_i's.

    sum_mi_minus_1 += mi-1

    if a_i's[0] ==1:

        current_L=1

        for j in range(1, mi):

            if a_i[j] == a_i[j-1]+1:

                current_L +=1

            else:

                break

        if current_L > max_L:

            max_L = current_L

answer = sum_mi_minus_1 + (n-1) - 2*(max_L -1)

print(answer)

Yes. Now, implement this in Python.

But we need to read the chains efficiently.

In Python, reading the input as:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())

    sum_mi_minus_1 = 0

    max_L =0

    for _ in range(k):

        parts = list(map(int, input_stream.readline().split()))

        mi = parts[0]

        a = parts[1:]

        sum_mi_minus_1 += mi -1

        if a[0] ==1:

            current_L =1

            for j in range(1, mi):

                if a[j] == a[j-1] +1:

                    current_L +=1

                else:

                    break

            if current_L > max_L:

                max_L = current_L

    answer = sum_mi_minus_1 + (n-1) - 2*(max_L -1)

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 3
3 1 3 7
2 2 5
2 4 6
""",
            "output": \
"""\
10
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

Second sample:

7 3

3 1 3 7 → mi=3. sum_mi_minus_1 +=2. a[0] is 1. Check 3 ==2? No. So current_L=1.

sum_mi_minus_1 is 2.

next chain: 2 2 5 → mi=2. sum +=1. a[0] is 2, ignored.

sum becomes 3.

next chain:2 4 6 → sum +=1. sum is 4.

max_L is 1.

answer:4 +6 -0 =10.

Yes.

Another test case where a chain has 1,2,3,4. Let's say n=4, k=1. Then sum_mi_minus_1 is 3. max_L=4. answer is 3 +3 -2*3=6-6=0? Wait, but that's impossible. Wait, the formula:

sum (mi-1) is 3 (since mi=4). n-1=3. So 3+3=6. Subtract 2*(4-1)=6. So 6-6=0. But how?

Because the chain is already the desired 1→2→3→4. So no steps are needed. So yes, answer is 0. Correct.

Another test case where the chain is 1,3,4. Then max_L is1. sum is 2 (mi=3, 3-1=2). n-1=3. answer is 2+3 -0=5.

Which would correspond to breaking the chain into 3 parts (taking 2 steps), then assembling into 1→2→3→4 (but 2 is missing). Wait, no. Wait, the problem says that the initial configuration may not have all the dolls. Wait, no, the input must have all the dolls. Because sum of mi is n. So in this example, perhaps n=4, k=2. The chain 1,3,4 and another chain 2.

So sum_mi_minus_1 is 2 (3-1=2) +0 (1-1=0) =2.

max_L is 1 (chain 1,3,4 starts with 1, but consecutive only up to 1).

n=4.

answer is 2+3 - 0 =5.

Which would be:

Break down the first chain: 3 elements → 2 steps. The second chain is already a single doll. So sum is 2+0=2.

Assemble into 1→2→3→4. To assemble, you need to nest 1 into 2 (1 step), then 2 into 3 (1 step), then 3 into4 (1 step). Wait, no. Wait, the dolls are initially all separate. To assemble:

1 is separate. 2 is separate. 3 is separate. 4 is separate.

So step 1: nest 1 into 2. (1 step)

step 2: nest 2 (with 1 inside) into 3. (another step)

step 3: nest 3 (with 2 and 1) into4. (third step).

Total 3 steps.

But according to the formula, sum_mi_minus_1 is 2 (from first chain) +0 (second chain) =2. n-1=3. So total steps 2+3=5. Which matches the formula. So the answer is 5.

But according to the problem's allowed operations, when assembling, each nesting takes one step. So yes, that's correct.

So the code works.

Thus, the code is correct.
</think>

```python
import sys

n, k = map(int, sys.stdin.readline().split())
sum_mi_minus_1 = 0
max_L = 0

for _ in range(k):
    parts = list(map(int, sys.stdin.readline().split()))
    mi = parts[0]
    a = parts[1:]
    sum_mi_minus_1 += mi - 1
    if a[0] == 1:
        current_L = 1
        for j in range(1, mi):
            if a[j] == a[j-1] + 1:
                current_L += 1
            else:
                break
        if current_L > max_L:
            max_L = current_L

answer = sum_mi_minus_1 + (n - 1) - 2 * (max_L - 1)
print(answer)
```
