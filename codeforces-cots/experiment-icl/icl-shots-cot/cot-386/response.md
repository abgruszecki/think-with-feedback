<think>
Okay, let's see. The problem is about converting a cell number from a column-wise numbering to a row-wise numbering. So, given n rows and m columns, when the table is numbered by columns, each cell's number x needs to be converted to the corresponding number in the row-wise numbering.

First, I need to find the formula that connects these two numberings. Let's think about how the column-wise numbering works. In column-wise, the cells are filled column by column, top to bottom. For example, in a 3x5 grid, the first column is 1,2,3; the second column is 4,5,6, etc. So for any cell, the column number can be determined by x. Then, once we know the row and column in the column-wise system, we can convert that to the row-wise number.

Wait, no. Wait, the row-wise numbering is when the cells are filled row by row. So the cell's position (i,j) in the row-wise numbering is such that the number is (i-1)*m + j. But in the column-wise numbering, the position (i,j) would be (j-1)*n + i. Because each column has n cells, so the first column is 1..n, the second column starts at n+1, etc. So for column j, the starting number is (j-1)*n + 1. Then each row in that column increases by 1. So the cell (i,j) in column-wise numbering is (j-1)*n + i. 

But the problem says, given x (which is the column-wise number), find the row-wise number. So x is the column-wise number. So first, for x, we need to find the original (i,j) in the column-wise numbering, and then convert that (i,j) to the row-wise number.

So the steps would be:

1. Given x, compute which column it is in (in the column-wise system). Let's call that column c. Since each column has n cells, the column c can be found by (x-1) // n + 1. Because the first column has numbers 1 to n, so x-1 divided by n gives (0) for the first column, leading to c=1. Similarly, for x= n+1, (x-1) is n, divided by n gives 1, so c=2.

Wait, let's check. Suppose n=3, m=5. For x=7, which is in column 3. (7-1)=6 divided by 3 is 2, so c=2+1=3? Wait 6//3 is 2. So c=2+1=3. Which is correct, since column 3 starts at 3*2 +1=7? Wait, no. Wait column 1: 1-3, column 2:4-6, column 3:7-9, etc. So x=7 is in column 3. (7-1)=6, divided by 3 is 2. So 2+1=3. Yes. So column c = (x-1) // n + 1. Then the position in the column is (x-1) % n + 1. So row i in column-wise is (x-1) % n +1.

So the (i,j) in the column-wise system is ( (x-1) % n + 1, (x-1) // n + 1 ). Then, the row-wise number is (i-1)*m + j. Wait no. Wait, row-wise numbering is (i,j) in the same grid, but the number is (i-1)*m +j. Because the first row is 1..m, second row starts at m+1, etc. So yes.

Wait, the cell (i,j) in row-wise is (i-1)*m +j. So once we have the (i,j) of the cell in the column-wise system, which is the same as the actual grid's (i,j), then the row-wise number is (i-1)*m +j. Wait no. Wait, in column-wise numbering, the cell (i,j) in the grid (row i, column j) is numbered as (j-1)*n +i. So in this case, given x, which is the column-wise number, we can find j (column) and i (row) as j = (x-1) //n +1, i= (x-1) %n +1. Then, the row-wise number is (i-1)*m +j.

So putting this together: For x, compute j = (x-1) //n +1, i = (x-1) %n +1. Then the row-wise number is (i-1)*m +j.

Wait, but let's test this with the sample input.

Sample input 3:

3 5 11.

In the column-wise system, 11 is the cell in column (11-1)//3 +1 = 10//3=3, +1=4. So column 4. Wait no, 10//3 is 3 (since 3*3=9, 10-9=1). So (x-1)=10. 10//3=3, so column 3+1=4. Then the row is (10%3)+1=1+1=2. So i=2, j=4. Then row-wise number is (2-1)*5 +4= 5+4=9. Which matches the sample output. So that works.

Another sample: input 2 2 3. For x=3 in 2x2. Column is (3-1)//2 +1= 2//2=1, +1=2. Row is (3-1)%2 +1= 2%2=0 +1=1. So i=1, j=2. Row-wise number is (1-1)*2 +2= 2. Which matches the sample output.

Another sample: 1000000 1000000 1e12. The row-wise number would be (i-1)*m +j. Let's see: x=1e12. For j=(x-1)//n +1. Since n=1e6, (1e12-1) is 999999999999. Divided by 1e6: 999999999999 // 1e6 is 999999. So j=999999+1=1e6. Then the row i is (x-1) %n +1. (1e12-1) mod 1e6 is 999999. So i=999999+1=1e6. So row-wise number is (1e6 -1)*1e6 +1e6 = (1e6 *1e6 -1e6) +1e6 = 1e12. Which is correct. So the sample output is 1e12.

So the formula seems to work.

Thus, the steps for each test case are:

- Given n, m, x.

Compute:

j = (x-1) // n +1

i = (x-1) % n +1

row_wise = (i-1)*m +j

But wait, what if j exceeds m? Because m is the total number of columns. Because x could be up to n*m. So j can be (x-1) //n +1. Let's see, maximum x is n*m. (x-1) is n*m-1. Divided by n is (n*m-1)//n. Which is (m-1) when (n*m-1) = n*(m-1) + (n-1). So (n*m-1)//n = m-1. So j = m-1 +1 = m. Which is valid. So j can't exceed m. So that's safe.

Similarly, i can't exceed n, since (x-1) mod n is between 0 and n-1. So i is between 1 and n. So that's okay.

So the code for each test case is straightforward. For each x, compute j and i, then compute the row-wise number.

Now, considering the constraints:

t is up to 1e4, and each test case can have n and m up to 1e6. But for each test case, the calculation is O(1) time, so total time is acceptable.

So the code in Python would read t test cases, and for each, compute j, i, then (i-1)*m +j.

But in Python, division is a bit tricky. However, for integer division, (x-1) //n is correct.

Wait, in Python, (x-1)//n is integer division. So for example, (3-1)//2 is 1, which is correct. So that's okay.

So the code would be:

Read t.

For each t times:

Read n, m, x.

Compute column_j = (x-1) // n + 1

row_i = (x-1) % n +1

result = (row_i -1)*m + column_j

Print(result)

Testing this against the sample inputs:

Sample 3:

3 5 11 → x=11.

(x-1) is 10.

10//3=3, so column_j=4. 10%3=1 → row_i=2. (2-1)*5 +4 =5+4=9. Correct.

Sample 2:

2 2 3 → (3-1)=2 → 2//2=1 → column_j=2. 2%2=0 → row_i=1. (1-1)*2 +2=2. Correct.

Sample 5:

n=1e6, m=1e6, x=1e12.

(x-1) is 999999999999.

Divided by 1e6 gives 999999 → 999999 +1=1e6 (column_j=1e6). (x-1) mod 1e6 is 999999 → row_i=1e6. (1e6-1)*1e6 +1e6 = (999999 *1e6) +1e6 = 1e6*(999999 +1) =1e12 → correct.

Another sample: input 100 100 7312. Let's compute:

x=7312, n=100.

x-1=7311.

7311//100=73.11 → floor is 73. So column_j=73+1=74.

row_i=7311%100 +1= 11 +1=12.

Row-wise number is (12-1)*100 +74 = 11*100 +74= 1100+74=1174. Which matches the sample.

Yes.

So this formula works.

Therefore, the code is straightforward. Now, considering possible edge cases:

Test case where n=1, m=1, x=1 → column_j=1, row_i=1. (1-1)*1 +1=1. Correct.

Another case: n=1, m=5, x=3. Here, the column-wise numbering is 1,2,3,4,5 (since it's a single row). So row-wise is same as column-wise. So output x. Let's see: j=(3-1)//1 +1=2+1=3. row_i= (3-1)%1 +1=0+1=1. (1-1)*5 +3=3. Correct.

Another case: m=1. For example, n=5, m=1, x=3. Column-wise numbering is 1,2,3,4,5 (since m=1, it's a single column). Row-wise numbering is same as column-wise. So output x. Let's compute: j=(3-1)//5 +1= 2//5=0 +1=1. row_i= (3-1)%5 +1=2+1=3. (3-1)*1 +1=3. Correct.

So the code handles all cases.

Now, considering data types. The problem says that x can be up to 1e12, which is within 64-bit integer range (Python's int is arbitrary precision, so no problem). The calculations (x-1) can be up to 1e12-1, but in Python, no issues.

Thus, the code is correct.
</think>

```python
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        x = int(data[idx+2])
        idx +=3
        col = (x-1) // n +1
        row = (x-1) % n +1
        res = (row-1)*m + col
        print(res)
        
if __name__ == "__main__":
    main()
```