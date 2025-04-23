<think>
Okay, let's see. The problem is about inserting numbers into a hash table and finding the first conflict. So, the task is to determine the first insertion that causes a conflict. If all insertions are without conflicts, output -1.

Hmm. The constraints are p and n up to 300. Wait, that's not very big. So even a simple approach would work here. But let's think about the optimal solution.

The approach would be to track which buckets have been filled. For each number in the input, compute its hash (mod p) and check if that bucket is already occupied. The first time a collision happens is the answer. If none, return -1.

So the steps are:

1. Read p and n.
2. Initialize a set or a list to keep track of occupied buckets.
3. For each of the n numbers:
   a. Compute the bucket (xi mod p).
   b. If the bucket is already in the set, return the current index (i+1, since it's 1-based? Wait, wait. The problem says, "the first conflict happens right after the i-th insertion". For example, the sample input had 5 insertions. The output was 4. Looking at the sample input:

Sample 1:
Inputs are 0,21,53,41,53. Let's compute their mod 10.

0 mod 10 is 0. Bucket 0 filled. No conflict.
21 mod10 is 1. New. Ok.
53 mod10 is 3. New. Ok.
41 mod10 is 1. Oh, bucket 1 is already filled. So this is the 4th insertion (since we start counting from 1?), so output 4. Yes, that's the sample output.

Wait, the first insertion is index 0 (0-based) or 1? The problem says "after the i-th insertion". So for the sample, the conflict happens after inserting the fourth element. So the answer is 4.

So the loop should start from 1 to n, and for each element, check if the bucket is already occupied. If yes, return the current index (i) and exit. Otherwise, add the bucket to the occupied set.

So the plan is:

- Create a set to track occupied buckets.
- Iterate over each of the n elements in order.
- For each element, compute mod p.
- Check if in the set. If yes, return the current index (i+1? Or 0-based? Wait, the problem's examples show that in the first sample, the fifth element is 53, which mod 10 is 3. But bucket 3 was filled by 53 before. Wait no, let's re-examine the first sample.

Sample input 1:

p=10, n=5.

The numbers are:

0 → 0 mod10 → 0. Added.

21 → 21 mod10 →1. Added.

53 →53 mod10 →3. Added.

41 mod10 is 1 → conflict. This is the fourth number. So the fourth insertion causes the first conflict. So the output is 4.

So the indices are 1-based. So for each element in the input (0-based in the code), when we process the ith element (0-based), we check if the bucket is in the set. If yes, then the answer is i+1 (since the first conflict is after the i-th insertion, where i starts at 1). Because the first element is i=0, but the first insertion is the 1st.

Wait, the first insertion is the first element. So for the i-th element (0-based in code, but the input is given in order as per the problem statement), the answer is i+1. Because the first element is the first insertion, and if a conflict happens, then the answer is 1.

Wait, let's clarify:

For each number in the order given (1 to n?), but the input is given as n lines. The code will read each line in order. So for the first line, it's the first insertion, the second line is the second insertion, etc.

So the code processes the numbers in the order given. For each number, compute the hash. If the bucket is already occupied, then the answer is the index (starting from 1) of this insertion. Otherwise, add the bucket to the occupied set.

So for the first sample, the fourth insertion (i=3 in 0-based) is the 41, which mod 10 is 1. So the answer is 4.

So the code needs to loop through each of the n elements, keeping track of the buckets, and return the first index (1-based) where a conflict occurs. If all are okay, return -1.

So the steps are:

Initialize a set.

For each i from 0 to n-1:

   read x_i.

   compute bucket = x_i mod p.

   if bucket is in the set: return i+1.

   else: add bucket to the set.

If all processed and no conflicts: return -1.

That's straightforward.

Now, considering the constraints: p and n up to 300. Even with n=300, the loop will run 300 times. So the time complexity is O(n), which is acceptable.

The data structure for tracking the occupied buckets can be a set, which gives O(1) lookups and inserts. So that's efficient.

In Python, using a set is the way to go.

Now, let's think about possible edge cases.

Edge case 1: p=2, n=2. Insert 0 and 2. 0 mod 2 is 0, 2 mod2 is 0. So conflict at second insertion. Output is 2.

Edge case 2: All insertions are unique. Then output -1.

Another edge case: p=1. Wait, but the problem states that p >=2. Because the input constraints say 2 ≤ p, n ≤ 300. So p is at least 2. So no problem here.

Another case: multiple x_i mod p being same, but not consecutive. For example, first x is 0, then some others, then another 0. So first conflict at that insertion.

So the code should handle all cases correctly.

Now, the code in Python:

Read p and n from input. Then read n lines of x_i.

So code outline:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    p, n = map(int, input_stream.readline().rstrip("\n").split())
    occupied = set()
    for i in range(n):
        x = int(input_stream.readline().rstrip("\n"))
        mod = x % p
        if mod in occupied:
            print(i+1, file=output_stream)
            return
        occupied.add(mod)
    print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 5
0
1
2
3
4
""",
            "output": \
"""\
-1
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

Sample 2:

5 5
0 →0 mod5=0.
1 mod5=1.
2 mod5=2.
3 mod5=3.
4 mod5=4. All added. No conflicts. Output -1.

Yes.

Another test case: when the first insertion causes a conflict. Like p=5 and inserting 5 (mod5=0), but the first insertion was 0 mod5=0. So the second insertion is 5, which mod5 is 0. So the answer is 2.

So code would print 2.

Yes.

So the code seems correct.
</think>

```python
p, n = map(int, input().split())
seen = set()
for i in range(n):
    x = int(input())
    mod = x % p
    if mod in seen:
        print(i + 1)
        exit()
    seen.add(mod)
print(-1)
```
