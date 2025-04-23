<think>
Okay, let's see. The problem is to find the maximum number of rows that can be made completely clean by sweeping some columns. Each sweep on a column flips all its bits (clean becomes dirty and vice versa). So the goal is to choose which columns to flip such that as many rows as possible end up all clean (all '1's after the flips).

Hmm. Let's think about how to approach this. The key observation here is that for a row to be all clean after flipping certain columns, its pattern must match the flip pattern. Like, for each row, after flipping the columns we choose, all elements in that row must be 1. So if a row's original state is, say, "0101", then flipping columns 0 and 2 (assuming 0-based index) would change each element in those columns. Let's see: original row is 0,1,0,1. If we flip column 0 and 2, then the row becomes 1,1,1,1. So that row becomes all 1s. 

But how do we find which rows can be turned into all 1s by flipping some subset of columns, and which subset would maximize the number of such rows?

Wait, but flipping a column affects all rows. So whatever set of columns we flip, it's applied to all rows. Then, after flipping those columns, each row must be all 1s. So the problem reduces to: find a subset of columns to flip such that as many rows as possible, after flipping those columns, become all 1s.

So the approach is to find for each possible row pattern, how many rows would match that pattern if you flip the columns where the original row has 0 in that position. Wait, maybe not exactly, but let's think differently. For a particular row, the columns that need to be flipped are exactly those where the row has 0s. Because flipping those would turn the 0s into 1s. Wait, no. Let's think: If a row has some 0s and 1s. Suppose we flip the columns where the original row has 0s. Then after flipping, those positions become 1, and the 1s become 0. So the entire row would become all 1s only if all the original 1s are not in columns that we flip. Wait, no. Wait, let's take an example. Suppose a row is "0101". To turn all into 1s, we need to flip columns where the original value is 0. So columns 0, 2 in 0-based. Because flipping those would turn 0s into 1s, and 1s into 0s. Wait, but in this case, original row is 0,1,0,1. Flipping columns 0 and 2: the row becomes 1 (0 flipped), 1 (unchanged), 1 (0 flipped), 0 (1 flipped). So that's 1,1,1,0. Which isn't all 1s. Oh right, because the 1s in columns that are flipped become 0. So that approach would not work. So my initial thought was wrong.

So the correct approach is: for a given row, the set of columns to flip must be such that, after flipping, all elements in the row are 1. Let's model this. Let's say the original row is a string s. For each column j, if we flip it, then the j-th character of the row is flipped. So after flipping a set of columns F, the row becomes s' where s'_j = 1 - s_j if j is in F, else s_j. We need s'_j to be 1 for all j. So for each j in F: 1 - s_j == 1 → s_j must be 0. For j not in F: s_j must be 1. Wait, that's not possible. Wait, let's think again. The condition is that after flipping, all elements are 1. So for each j in the row:

If we flip column j: s_j must be 0 (because flipping 0 gives 1). 

If we don't flip column j: s_j must be 1. 

So the set F of columns to flip must be exactly those j where s_j is 0. Wait, but that's only if the row is supposed to be all 1s after flipping. Wait, no. Let's see:

For the row to be all 1s after flipping columns F, for each j:

If j is in F → s_j was 0 (because flipping 0 gives 1).

If j is not in F → s_j is 1 (since it remains as 1).

So the set F must be exactly the set of columns where s_j is 0. But that's only for that particular row. Because then, flipping those columns would turn all their 0s into 1s, and leave the 1s as 1s (since they are not flipped). Wait, no. Wait, if a row is 0101, then the columns with 0 are 0 and 2. So F is {0,2}. Flipping those would turn 0 into 1, 1 into 0, etc. Wait, let's see:

Original row is 0 (j=0), 1 (j=1), 0 (j=2), 1 (j=3).

After flipping columns 0 and 2:

j=0: 0 → 1.

j=1: remains 1.

j=2: 0 →1.

j=3: remains 1.

So the row becomes 1,1,1,1. So that works. Oh right! So in this case, the set F is exactly the columns where the original row has 0s. Then, after flipping those columns, the row becomes all 1s.

So, for a row to be all 1s after flipping, the set F must be exactly the set of columns where the original row has 0s. So if we choose F as that set, then that row becomes all 1s. But what about other rows? For other rows, if their columns in F are the same as their 0 positions, then those rows would also become all 1s. Wait no. For example, another row. Let's say another row is 0110. The original columns with 0 are 0 and 3. So the set F would be {0,3} for the first row, but if that's the case, then for this second row, flipping F would turn j=0 (0→1), j=3 (0→1), but j=1 and j=2 are 1 and 1. So after flipping, those become 0 and 0. So the row would become 1, 0, 0, 1. Which is not all 1s. So that row would not be part of the solution.

So the key idea is: For each row, the set of columns that need to be flipped to make it all 1s is exactly the set of 0s in that row. If we choose that set, then that row becomes all 1s. Then, the number of rows that can be made all 1s is the number of rows that have exactly the same pattern of 0s and 1s as the chosen row.

Wait, no. Because if two rows have the same pattern of 0s and 1s, then flipping F (the 0s in the first row) would also turn the second row into all 1s, since their 0s are in the same positions. So the maximum number of rows that can be made all 1s is equal to the maximum frequency of any row's 0/1 pattern.

Wait, let me clarify. For any row, the required set of columns to flip is the set of positions where that row has 0. Then, any other row that has 0s in exactly those same positions would, after flipping, have all 1s. Because their 0s are exactly the columns being flipped. So, if two rows have the same pattern (i.e., the same set of 0 positions), then flipping F for one of them would make both rows all 1s.

Therefore, the maximum number of rows that can be made all 1s is the maximum number of rows that have the same pattern. Because flipping the columns where those rows have 0s would turn all of them into 1s. So the solution is to find the pattern (row) that occurs most frequently. The count of that pattern is the answer.

Wait, but what about rows that, after flipping the columns, could be all 1s even if their pattern is different? For example, suppose a row has 0s in some positions. When you flip those columns, maybe other rows' 0s and 1s are arranged such that their flipped columns also result in all 1s. But how?

Wait, let's take an example. Suppose row A is 0101, which requires flipping columns 0 and 2. Another row B is 1010. After flipping columns 0 and 2, row B becomes 0010. Which is not all 1s. So that row B would not be part of the solution.

Another example: row C is 0000. Flipping all columns (since all are 0s) would turn this into 1111. Any other row that is 0000 would also become 1111. But any row that has 1s in all positions would, after flipping all columns, become 0000. So that's not part of the solution. Wait, but in this case, the maximum possible would be the count of rows that are all 0s, because flipping all columns would turn those into all 1s, but the other rows (all 1s) would become all 0s. So in that scenario, the answer is the number of all 0s rows. So the approach of taking the maximum frequency of any pattern would work here.

Wait, let's see. Suppose we have rows with various patterns. For each row, the required flips are the 0s in that row. Then, other rows would need to have exactly 0s in the same positions to be all 1s after flipping. So the answer is the maximum frequency of any row's pattern. Because when you choose to flip the 0s of that pattern, all rows with that same pattern will be all 1s. Any other row that doesn't have the same pattern would have some 1 in a flipped column (which would become 0) or a 0 in a non-flipped column (which remains 0). So those other rows would not be all 1s.

So the approach is to count the frequency of each row's pattern and take the maximum frequency. Because that's the maximum number of rows that can be made all 1s by flipping their required columns.

So the steps are:

1. Read all the rows.

2. For each row, determine its pattern. Because flipping a row's 0 columns would make it all 1s. So the pattern is the original row's 0/1 string. Wait, no. Wait, the pattern is the same as the original row. Because if two rows are identical, then their 0s are in the same positions. So flipping those columns would turn both into all 1s.

Wait, no. For example, consider two rows that are identical. Suppose row A is "0101", row B is "0101". Flipping columns 0 and 2 would turn both into all 1s. So the count for this pattern would be 2. But in the first sample input, the first sample input has two rows "0101" (rows 1 and 4). So their frequency is 2, which is the output. Which matches the sample.

So the approach is to count the frequency of each row's pattern. The maximum frequency is the answer.

But wait, another possibility: perhaps flipping some other set of columns can lead to more rows being all 1s. For example, if there's a pattern that, when flipped, some rows not having that pattern also become all 1s. But according to the earlier reasoning, that's not possible. Because for a row to be all 1s after flipping a set F, F must be exactly the columns where the original row has 0s. So when you choose F as the set of 0s for a particular row, only other rows that have 0s exactly in F (i.e., the same pattern) will become all 1s. So the maximum possible is indeed the maximum frequency of any row's pattern.

But wait, let's take an example. Suppose a row is "1111". The required F is the empty set. So flipping nothing. Then, all rows that are "1111" would remain as 1s. But also, any other row that has 1s in all positions would become 1s. So if there's a row that's "1111", then the frequency of this pattern is the number of rows that are all 1s, and that would be the maximum possible. So in the second sample input, all rows are "111", so the answer is 3.

So the approach is correct.

Another example: suppose a row is "1000". Flipping the columns where it has 0s (columns 1,2,3). Then, any row that also has 0s in columns 1,2,3 would become all 1s. So if there are two such rows, the answer would be 2.

So the algorithm is:

- Read all the rows.

- For each row, count how many times that row appears in the input.

- The maximum count is the answer.

Because for each row, if we choose to flip the columns where it has 0s, then all rows equal to it will become all 1s. And no other rows can be converted unless they have the same pattern.

So this is the correct approach.

So the solution is to count the frequency of each row and return the maximum frequency.

Wait, that seems too simple. Let's check the first sample input.

First sample input:

4

0101

1000

1111

0101

The rows are "0101", "1000", "1111", "0101". The frequencies are:

"0101" → 2

"1000" → 1

"1111" →1

So maximum is 2, which matches the sample output.

Second sample input:

3

111

111

111

All rows are same. So frequency is 3. Output is 3. Correct.

Another test case: if a row is all 0s. Then, flipping all columns (since all are 0s) would turn all those rows into 1s. So the count is the number of all 0 rows.

But what if there are rows of different patterns that when their F is applied, some other rows are also turned into all 1s?

For example:

n=2

Rows:

00 → flip columns 0 and 1. Then, after flipping, the row becomes 11. Suppose another row is 11. Then, flipping those columns would turn 11 into 00. So this other row would not be part of the solution. So the answer is 1.

So in this case, the maximum frequency is 1 (for the first row). But the other row is "11", which when flipped (F is empty), then the count is 1. So the maximum is 1. Correct.

So the approach works.

Therefore, the optimal solution is to count the frequency of each row's pattern and return the maximum frequency.

Now, how to implement this in Python?

We can read all the rows, store them in a list, and then use a dictionary to count the occurrences of each row. Then, the maximum value in the dictionary is the answer.

The time complexity is O(n^2) since for each of n rows (each of length n), we process them. For n up to 100, n^2 is 10,000, which is acceptable.

Space is O(n^2) since we store all the rows and the counts. But again, for n=100, that's 100 rows of 100 characters, which is 10,000 characters. The counts would take O(k) where k is the number of distinct rows, which is up to 100. So no problem with memory.

Thus, the code is straightforward.

So the steps are:

1. Read n.

2. Read n lines, each line is a string.

3. Count the frequency of each string.

4. The maximum frequency is the answer.

So the code would be something like:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    from collections import defaultdict
    counts = defaultdict(int)
    for _ in range(n):
        s = input_stream.readline().rstrip("\n").strip()
        counts[s] += 1
    print(max(counts.values()), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
111
111
111
""",
            "output": \
"""\
3
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

3

111

111

111 → counts {'111':3}. Max is 3. Correct.

Another test case: when all rows are 00. Then answer is 3. Correct.

Another case where some rows have same pattern, others different. So code works.

So this is the optimal solution. Time and space are within constraints.
</think>

```python
n = int(input())
from collections import defaultdict
count = defaultdict(int)
for _ in range(n):
    row = input().strip()
    count[row] += 1
print(max(count.values()))
```
