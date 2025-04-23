<think>
Okay, so I have this programming problem to solve. Let's read the problem carefully.

The problem is about counting how many times a page is turned each day when writing names into the Death Note. Each day, you write a certain number of names, and each page can hold exactly m names. You start writing on the current page, and whenever you fill it up, you turn the page. The question is, for each day, how many page turns happen during that day.

Hmm. Let's think about how to model this. Let's see the example.

In the first example, n=3, m=5, a is [3,7,9]. The output is 0 2 1. Let's see why. 

On day 1, you write 3 names. The current page starts empty, and after writing 3, it has 3. Since 3 is less than 5, no page turn. So t1 is 0.

On day 2, you add 7 names. Let's see: the current page was filled to 3. Adding 7 gives a total of 10. Wait, wait. How does this work?

Wait, no. Wait, during each day, you write all the names for that day. So during day 2, you start on whatever page you were on after day 1. The initial state after day 1: the current page is page 1 (since you wrote 3 names, not filling the page, so you don't turn it). So during day 2, you have to write 7 names. Let's see:

Start on page 1, which has 3 names. The remaining capacity is 2 (since 3+2=5). So you write 2 names here, filling the page. Then you turn the page (that's a page turn). Now you're on page 2. You have 7-2=5 names left. So you write all 5 into page 2, which fills it. Then you turn again. So after writing the 7, you turned the page twice. So t2 is 2.

Then day3: you start on page3. 9 names. The first page (page3) is empty. You write 5 names, fill it, turn (count 1). Then 4 left. Next page (page4) takes 4, which doesn't fill. So total page turns during day3 is 1.

So the key is tracking the current position in terms of how much of the current page is filled after each day. But wait, each day, the a_i names are written in sequence, and whenever the current page is filled, you turn. But how to compute for each day the number of page turns.

Let me model the process:

We need to track the current position: the number of names written on the current page before the day starts. Let's call this variable 'current'.

For each day i:

- The total names written during the day is a_i.

- The total after writing is current + a_i.

- The number of pages turned is equal to how many times the cumulative sum crosses multiples of m. But wait, perhaps we can model it as:

Compute how many full pages are filled during this day, which is (current + a_i) // m, then subtract the number of full pages before the day started (current // m). The difference gives the number of page turns during the day.

Wait, no. Because current is the number of names on the current page before the day starts. So before the day starts, the current page could be partially filled. So during the day, we add a_i names. The way it's filled is:

The current page can take some of the a_i. Once it's filled, a page is turned, then the next page is filled, and so on until all a_i names are written.

The number of page turns during the day is equal to the number of times the cumulative sum (current + sum of a_i up to the current day) // m minus the cumulative sum (current) // m. Wait, maybe that's the case.

Wait, let's think about cumulative sum.

Let's track the total number of names written up to day i. Let total = sum_{k=1 to i} a_k.

The total number of pages used after day i is (total) // m, but considering that each page is exactly filled. Wait, but when you fill a page, you turn it. So for example, if you have 5 per page and write 5 names, you turn the page. So the total pages used after writing a_i is (total + m -1 ) // m ?

Wait, maybe not. Let's see: for example, if total is 5, that's exactly one page. But according to the problem statement, you turn the page when you finish the current page. So after writing 5 names, you are on a new page. So the number of pages turned is 1 (since you started on page 1, filled it, turned to page 2, but page 2 is empty). So the number of pages used is 1, but the number of page turns is 1 (but that's not the case. Let me recheck.

Wait, the initial state is that you start on page 1. When you write the first 5 names, you fill page 1, then turn to page 2. So after day 1, the total pages turned is 1. But if m=5 and a_i=5, then the page turns during that day is 1. Because during that day, you started on page 1 (empty), wrote 5 names, filled it, turned the page. So the page turns for that day is 1.

But according to the example 1:

The first day's a_i is 3. m=5. So the current after day1 is 3. The total is 3. So (3 + m -1 ) // m = (3+4)/5 = 7//5=1. So total pages used is 1. Which is correct, because you didn't turn the page. Wait, but (3) // 5 is 0. So the number of pages used is 0? No, no. You start on page 1, write 3 names. So page 1 is partially filled. So the number of pages used is 1. So perhaps the correct formula is (sum + m -1 ) // m.

Yes. Because sum=3: 3 names take up 1 page. sum=5: 5 names take 1 page. Wait, no. sum=5 names is exactly one page. Then you turn to the next page. So the number of pages used is 1, but the current page is page 2 (empty). So the total pages used is 1 (page 1), and the current page is page 2. So when sum is 5, the pages used is 1, but the current page is 2. So perhaps the formula (sum) // m gives the number of pages turned.

Wait, sum=5, m=5: 5//5=1. Which is the number of page turns. Because after writing 5 names, you turned the page once. So for each day, the number of page turns is the difference between the cumulative sum divided by m after the day and before the day.

Wait, let's model the cumulative sum:

After day i, the cumulative sum is S_i = sum_{k=1 to i} a_k.

The number of pages turned after all days up to i is S_i // m.

But that's not correct. Because when you write 5 names, you turn the page once. So S_i//m is 1. But after writing 5 names, the page is turned once, which is the number of times.

But for the first example:

Day1: sum 3. pages turned: 0.

Day2: sum 10. 10//5 = 2. So total pages turned up to day2 is 2. The difference from day1 (0) is 2, which is the number of page turns during day2. Which matches the example.

Day3: sum 19. 19//5=3. So difference from day2 (2) is 1, which is the page turns during day3. So yes, this seems to work.

So the approach is:

Compute the cumulative sum after each day. The number of page turns during day i is (current_cumulative_sum // m) minus (previous_cumulative_sum // m).

Yes! Because for each day i, the cumulative sum after i days is S_i. The previous sum was S_{i-1}. The number of pages turned during day i is (S_i // m) - (S_{i-1} // m).

This is a brilliant insight. So the key is to compute the prefix sums and for each i, compute (sum_i // m) - (sum_{i-1} // m).

This approach is O(n) time, which is acceptable for n up to 2e5. Because 2e5 operations are manageable.

So the steps are:

1. Read n and m.

2. Read the array a.

3. Compute the prefix sums. But since a_i can be up to 1e9, and n up to 2e5, the sum can be up to 2e5 * 1e9 = 2e14. So in Python, that's manageable as integers.

4. For each i in 0 to n-1, compute sum_i = sum of a[0..i], then t_i = (sum_i // m) - (sum_{i-1} // m). But note that sum_{i-1} is the sum up to a[0..i-1], so when i=0, sum_{-1} is 0.

Wait, the indices in the code: let's say the input array is a list with 0-based index. For each element a[i], which is the (i+1)th day.

Wait, in the problem statement, the days are 1-based. But the code can process them as 0-based.

Wait, let's say:

sum_prev starts at 0.

For each i from 0 to n-1:

sum_current += a[i]

t_i = (sum_current // m) - (sum_prev // m)

sum_prev = sum_current

So for each day, the sum_prev before the day is the sum of the previous days. Then sum_current is sum_prev + a[i].

So this approach works.

Yes, this should correctly compute the number of page turns during each day.

Now let's test this with the first example:

Sample Input 1:

3 5

3 7 9

Day 1 (i=0):

sum_prev = 0.

sum_current = 3.

sum_current //5 = 0.

sum_prev //5 is 0.

t0 = 0-0=0.

sum_prev becomes 3.

Day 2 (i=1):

sum_current = 3+7=10.

sum_current//5 = 2.

sum_prev//5=0.

t1=2-0=2.

sum_prev becomes 10.

Day3 (i=2):

sum_current=19.

sum_current//5=3.

sum_prev//5=2.

t2=3-2=1.

Which matches the output.

Another sample input:

Sample Input 2:

4 20

10 9 19 2

sum_prev starts at 0.

Day1: sum_current=10. 10//20=0. t0=0-0=0. sum_prev=10.

Day2: sum_current=19. 19//20=0. t1=0-0=0. sum_prev=19.

Day3: sum_current=38. 38//20=1. previous sum_prev//20=0. t2=1-0=1. sum_prev=38.

Day4: sum_current=40. 40//20=2. previous sum_prev//20=1. t3=2-1=1. So output is 0 0 1 1. Which matches.

Third sample:

n=1, m=100, a=99.

sum_prev=0.

sum_current=99. 99//100=0. t0=0-0=0. Correct.

So this approach works.

Therefore, the code can be written as follows.

We need to read the array, compute the prefix sum, and for each element, compute (current_sum // m) - (prev_sum // m).

In Python, to handle large numbers, but since integers can be big, no problem.

Now, considering that n can be up to 2e5, the code should read the input efficiently.

In Python, reading the input with split may be slow for large n. So using sys.stdin to read the input.

But the code must read from input(), but for large n, it's better to read via sys.stdin.

Wait, but the problem statement says "Your solution must read input from standard input (input()), write output to standard output (print())."

But for large inputs, using input() can be slow. However, in practice, for Python, the best way to read a line of integers is to read via sys.stdin, split, and map to integers.

But the problem says that the code should use input(). So perhaps, but perhaps the code can read via input().split().

But let's think: for n up to 2e5, the second line has 2e5 numbers, which when split into a list can be handled, but the input() function in Python may read the entire line, which is possible.

Alternatively, for the second line, using sys.stdin.read() and split accordingly.

Wait, perhaps the code can be written as:

import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

But this is better for handling large input sizes.

But in Python, the problem is that when you have a line with 2e5 numbers, using input().split() may take time, but using sys.stdin.readline is faster.

So the code should use sys.stdin for speed.

Once the array is read, the code can compute the sum progressively.

Initialize sum_prev = 0.

Then, for each number in a:

sum_current += a[i]

t_i = (sum_current // m) - (sum_prev // m)

sum_prev becomes sum_current.

Append t_i to the result list.

But since the a can be up to 1e9 and n up to 2e5, the sum can be up to 2e14 * 1e9 = 2e23, but Python can handle big integers, so no problem.

So the code would be:

Read n and m.

Read the list a.

Compute the prefix sum step by step, keeping track of the previous sum.

For each element in a:

current_sum += a[i]

t_i = (current_sum // m) - (prev_sum // m)

Store t_i in a list.

prev_sum = current_sum

Then print the list as space-separated integers.

Yes.

Now, edge cases:

Test case where sum is exactly m. For example, m=5, a_i=5. Then sum_prev was 0. sum_current is 5. 5//5=1. prev_sum//5=0. So t_i=1.

Another case: a_i=5, m=5. Then during that day, the page is filled once, so page turns during that day is 1.

Yes.

Another case: m=1. Then each name causes a page turn. For example, a_i=3. sum_prev is 0. sum_current is 3. 3//1=3. prev_sum//1=0. So t_i=3.

Which is correct. Because on day i, you write 3 names. Each name fills a page. So after each name, you turn the page. But according to the problem statement: "you turn the page when it ends". So writing 3 names on a page with m=1 would require turning the page 3 times. Because the first name fills the page (turn), the second name fills a new page (turn), the third fills a new page (turn again). Wait, no. Wait, during the day, you start with the current page. If m=1, and you write 3 names, each name takes a full page. So:

After the first name: page is filled, turn once. So during the day, after writing the first name, you turn. Then the second name is written on the next page, which is filled, turn again. Third name, same. So total 3 turns. So yes, the code would output 3.

Yes.

Another test case: m=1, a_i=0. But the problem says a_i is at least 1. So no need to handle that.

So the code is correct.

Now, code.

In Python, the code would be:

Read n and m.

Read a as a list.

Initialize sum_prev = 0, current_sum=0.

Then for each num in a:

current_sum += num

t_i = (current_sum // m) - (sum_prev // m)

append t_i to result.

sum_prev = current_sum

Finally, print the result as space-separated.

So code:

Read the inputs:

n, m = map(int, input().split())

a = list(map(int, input().split()))

But for n up to 2e5, this could be a problem if the input is read via input(), but in practice, in Python, it's okay.

But to optimize, perhaps using sys.stdin.

But the problem statement says to use input(), so perhaps the code should use that.

But perhaps in the actual code, using sys.stdin would be better. Let me check.

In Python, when the input line is very long (like 2e5 numbers), using input().split() may be slow. Because the default split() function splits on all whitespace, including multiple spaces, but the built-in split in Python is efficient. So perhaps the code can use sys.stdin.read() and split once.

But in code submission, sometimes using sys.stdin is faster. Let's code that way.

So the code:

import sys

def main():

    data = sys.stdin.read().split()

    n = int(data[0])

    m = int(data[1])

    a = list(map(int, data[2:2+n]))

    sum_prev = 0

    current_sum = 0

    res = []

    for num in a:

        current_sum += num

        t = (current_sum // m) - (sum_prev // m)

        res.append(str(t))

        sum_prev = current_sum

    print(' '.join(res))

if __name__ == '__main__':

    main()

This code reads all data at once, splits into a list, and processes. This is faster for large input.

But according to the problem statement, the code must read via input(), but that's not the case. The problem states: "Your solution must read input from standard input (input()), write output to standard output (print())."

But in Python, the code can read via sys.stdin and still be considered as reading from standard input. The input() function is a higher-level way to read from stdin.

But using sys.stdin.read() is allowed. So the code is okay.

This code should handle all cases correctly.

Testing the first sample:

Input:

3 5

3 7 9

The data list will be ['3', '5', '3', '7', '9']

n=3, m=5.

a = [3,7,9].

sum_prev starts at 0.

current_sum after each step:

3: 3//5=0. t=0-0=0. res is [0].

sum_prev becomes 3.

current_sum becomes 3+7=10. 10//5=2. sum_prev//5=3//5=0. t=2-0=2. res [0,2].

sum_prev becomes 10.

current_sum 19. 19//5=3. sum_prev//5=2. t=3-2=1. res [0,2,1].

Output is 0 2 1.

Which is correct.

Another sample:

Sample input 2:

4 20

10 9 19 2

data list is ['4', '20', '10', '9', '19', '2'].

sum_prev=0.

current_sum=10: 10//20=0. t=0-0=0. res [0].

sum_prev=10.

current_sum=19: 19//20=0. t=0-0=0. res [0,0].

sum_prev=19.

current_sum=38: 38//20=1. t=1 - 0=1. res [0,0,1].

sum_prev=38.

current_sum 40: 40//20=2. 38//20=1. t=2-1=1. res [0,0,1,1].

Which matches.

Thus, the code should work.
</think>

```python
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    sum_prev = 0
    current_sum = 0
    result = []
    
    for num in a:
        current_sum += num
        turns = (current_sum // m) - (sum_prev // m)
        result.append(str(turns))
        sum_prev = current_sum
    
    print(' '.join(result))

if __name__ == "__main__":
    main()
```