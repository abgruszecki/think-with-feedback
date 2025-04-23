<think>
Okay, let's see. The problem is to determine who won more games between Anton and Danik based on a string of 'A's and 'D's. The input is the number of games and then the string. The output depends on which has more counts.

First, I need to process the input. The constraints say that n can be up to 100,000. So the solution needs to handle strings of that length efficiently.

The straightforward approach is to count the number of 'A's and 'D's in the string. Then compare the two counts.

So, the steps would be:

1. Read n (though maybe not necessary to use it since the string's length is n).
2. Read the string s.
3. Count how many times 'A' occurs and 'D' occurs.
4. Compare the counts and output the result.

How to count efficiently? In Python, the string's count method is O(n), which should be acceptable for n=1e5. Since 1e5 operations are manageable in Python under 1 second. Because even 1e8 operations are around 10 seconds, but 1e5 is 0.1 milliseconds. So using s.count('A') and s.count('D') would be efficient.

Another way is to iterate through each character once and count. But the count method is likely optimized, so using that is better. Also, using count is O(n) time, which is optimal here.

Once we have the counts, compare them:

- If A > D: print Anton
- If D > A: print Danik
- Else: print Friendship.

Edge cases: when all are A or all D. Or when counts are equal.

So the code structure is:

Read n from input (though perhaps not needed, but maybe to check), then read the next line. Then compute a_count = s.count('A'), d_count = len(s) - a_count. Wait, but len(s) is n, which is given. But perhaps it's better to compute a_count and d_count as s.count('A') and s.count('D')? Because the problem says that the input string is exactly of length n, but maybe in the code, it's better to process the string as given. However, since the problem states that all characters are A or D, so len(s) should be equal to n. So using len(s) is okay. But maybe the second line is read as input().strip(), and then process that. So perhaps:

n = int(input())
s = input().strip()

a = s.count('A')
d = s.count('D')

Alternatively, since the problem states that the string consists of exactly n characters, perhaps we can just use len(s) as n. But the problem says the first line is n, so perhaps the code should read n even if it's redundant. Because maybe the second line could have a different length, but according to the problem statement, it's guaranteed. So the code can proceed as:

n = int(input())
s = input().strip()

But then, the code may proceed to count A and D.

Then, compare a and d.

So the code is straightforward.

What about memory? For a string of 1e5 characters, that's manageable in Python. Each character is stored as part of the string, which is acceptable. No issues here.

So the optimal approach is to use the built-in count method. This is O(n) time, which is the best possible, since we have to check all characters.

Yes, this should be the most efficient solution. There's no way to do better than O(n) time, since each character must be read and checked. So the approach is optimal.

Now, code.

Read n, then s. Then count A and D. Compare and print.

So the code would be:

n = int(input())
s = input().strip()

a = s.count('A')
d = s.count('D')

if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")

Wait, but what if the sum of a and d is not n? Like, if the string has other characters. But the problem statement says that the string consists of uppercase A and D only. So it's safe.

Yes, so this code should work.

Testing the examples:

First example:

6
ADAAAA

s = 'ADAAAA' → count A: 5, D:1 → Anton.

Second example:

7
DDDAADA → DDD (3) + AADA (3 A's? Let's see: 'DDDAADA' → D D D A A D A → A's are 3, D's are 4. So Danik.

Third example: 'DADADA' → A's are 3, D's 3 → Friendship.

So code works.

This should be the correct solution. And it's efficient as possible. The count method is O(n), but in Python, it's a C-level loop, which is very fast. So even for 1e5, it's acceptable.

The code reads the input correctly, and processes it. So this should pass all test cases.
</think>

```python
n = int(input())
s = input().strip()
a = s.count('A')
d = n - a  # Since s consists only of 'A' and 'D'
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
```