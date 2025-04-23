<think>
Okay, I need to solve this problem where I have to find the next year after a given one that has all distinct digits. Let's see. The input is a year between 1000 and 9000. The output has to be the smallest year larger than the input with all digits different. And the answer is guaranteed to exist, so I don't have to handle impossible cases.

First, I should think about the approach. The straightforward way is to check each year starting from y+1 upwards, and for each year, check if all four digits are unique. The first one that satisfies this is the answer.

But wait, the constraints are up to 9000, and the next possible year could be as big as... well, the maximum possible after 9000 would be something like 9012, 9013, etc. So the loop might have to check a few numbers each time. For example, if the input is 8999, the next possible is 9012. So how efficient is this approach?

Let's calculate. For each year after y, check the digits. Since the maximum possible check is up to, say, 9876, which is the largest 4-digit number with all distinct digits, but wait, since the input is up to 9000, the maximum possible next year would be 9876. But even if the input is 9875, the next is 9876. But the problem says the answer exists, so maybe the input is such that the next year is within 9000-something. Anyway, the loop would run at most a few thousand iterations. For each iteration, checking 4 digits for uniqueness. That's O(1) per check. So overall, even in the worst case, it's O(1) time. Because 10,000 iterations would take negligible time. So this approach is feasible.

So the plan is:

1. Start from y+1.
2. For each number, check if all digits are unique.
3. The first such number is the answer.

So how to check if all digits are unique? Well, for a number, we can convert it to a string, then check if the length of the set of its characters is 4. For example, '1987' has 4 unique characters, so set('1987') would be of size 4. That's a simple check.

So the steps would be:

Read the input y. Then, loop starting at y+1. For each candidate in this loop, check if all digits are distinct. Once found, output it.

Now, thinking about possible optimizations. Well, since the input is up to 9000, the next valid year can't be more than, say, 9999 (but since the input is up to 9000, the answer is within 1000 to 9999). But even in the worst case, the maximum number of iterations is 9999 - y. But since y is at least 1000, the worst case would be y=8999, and the next is 9012. That's 13 iterations, which is nothing. So even the brute force approach is acceptable here.

So no need for any complex algorithm. Just check each year one by one.

So coding this in Python:

Read y as integer. Then for n in y+1 to... well, up to maybe y+10000 (though the loop will break once found). For each n, check if all digits are unique.

Let's test the sample input.

Sample 1: 1987. The next is 1988. Let's see:

1988: digits 1,9,8,8 → duplicates. So check each year:

1988: duplicate 8s → no.
1989: digits 1,9,8,9 → duplicates. No.
...
2013: digits 2,0,1,3 → all unique. So output 2013.

Sample 2: 2013. Next is 2014. Check digits 2,0,1,4 → unique. So yes.

So the code would work.

Now, in Python, how to implement this.

Read the input as y = int(input()).

Then, loop from y+1 to infinity. For each number in this loop, check if the digits are all unique.

Wait, but in Python, for numbers, converting to a string, then checking if the length of the set is 4.

So:

def has_unique_digits(n):
    s = str(n)
    return len(set(s)) == 4

But the problem is that the number must have 4 digits. But since y is at least 1000, the next possible n is y+1 which is 1001. So all numbers considered are 4 digits. So no problem.

So code:

y = int(input())
n = y + 1
while True:
    if len(set(str(n))) == 4:
        print(n)
        break
    n += 1

This is straightforward and should work.

Testing this code with sample input 1987: it would start at 1988, check each until 2013. For 2013, set('2013') has 4 elements → output.

Another sample input 2013: next is 2014. Check digits: 2,0,1,4 → unique. So output 2014.

But wait, what if the next number is 2015, 2016, etc. For example, if the input is 2013, the code would check 2014. Which is correct.

Yes.

This code should handle all cases. Now, check for possible edge cases.

Edge case 1: input is 9999. But according to constraints, the input is up to 9000, so this is not allowed. The maximum input is 9000. The next possible year would be 9012.

Another edge case: input is 8999. The next year is 9012. Let's see:

n starts at 9000. Check 9000: digits 9,0,0,0 → duplicates. 9001: 9,0,0,1 → duplicates. ... 9012: 9,0,1,2 → all unique. So code would output 9012.

Another case: input 1111. Next would be 1112, but digits not unique. Continue until 1234, but wait, the next valid year after 1111 is 1203? Let's see. Wait, 1111+1=1112. All digits are 1,1,1,2 → duplicates. Then 1113, etc., until 1123. Then 1123's digits are 1,1,2,3 → duplicates. Then 1124 → duplicates. ... The first valid would be 1203? No. Wait, maybe 1023? But wait, 1111 is 4-digit. The next possible 4-digit number with distinct digits would be 1112, but no. So the code would loop until it finds the next one.

But regardless, the code will handle it. Since the code is correct for all possible inputs within the constraints.

Therefore, the code is correct and efficient. Even though it's brute-force, it's acceptable for the problem's constraints.
</think>

```python
y = int(input())
n = y + 1
while True:
    if len(set(str(n))) == 4:
        print(n)
        break
    n += 1
```