<think>
Okay, let's tackle this problem. Hmm, the problem says that Jury has to touch the strips every second when a square appears. Each strip has a certain calorie cost. We need to calculate the total calories he uses based on the string input that shows which strips are active each second.

So the input is four integers a1 to a4, representing the calories for each strip. Then the string s consists of characters '1' to '4' indicating which strip was active each second.

The approach here is straightforward. For each character in the string s, we look up the corresponding a value and sum them all up. For example, if a character is '2', we add a2 to the total. That's the basic idea.

Wait, but how do we map the characters to the indices? Let's see. The characters are '1' to '4', which correspond to the first, second, third, and fourth a values. So, for each character in s, we convert it to an integer, subtract 1 to get the index (since Python uses 0-based), and then get the a's value.

But wait, the input a's are given in order a1, a2, a3, a4. So if we have a list or a tuple that's [a1, a2, a3, a4], then the index for '1' is 0, '2' is 1, etc. So for each character c in the string, we take int(c) -1 to get the index and sum the corresponding a's.

So the steps are:

1. Read the four a values from the first line.
2. Read the string s from the second line.
3. For each character in s, convert to integer, subtract 1 to get index, add the corresponding a's value to total.
4. Output the total.

Now, considering the constraints. The string can be up to 1e5 characters long. So looping through each character is O(n), which should be acceptable for Python even for 1e5 elements. Because 1e5 operations are manageable in under a second.

In terms of data structures, we can store the a values in a list, say, a = [a1, a2, a3, a4]. Then for each character in s, we take int(c) -1 as index and sum.

But wait, how about the initial input reading? The first line is four space-separated integers. So in Python, we can read them using input().split() and then convert each to integer, then put into a list.

So code outline:

a = list(map(int, input().split()))
s = input().strip()
total = 0
for c in s:
    index = int(c) -1
    total += a[index]
print(total)

That's the core part. But what about possible edge cases? Let's see. What if the string is empty? But according to the problem statement, the length is at least 1. So no problem. Also, the a values can be zero. For example, if a strip's calorie is zero, then touching it doesn't add anything, but we still need to count it if it's in the string.

Wait, the problem says that each second a square appears on some of the strips. So the string s tells which strip to touch each second. So even if the a's value is zero, we have to add it. So the code correctly handles that.

Testing the first example:

Input:
1 2 3 4
123214

The string is '1','2','3','2','1','4'. So the sum is 1+2+3+2+1+4= 13. Which matches the sample output.

Another sample input:

1 5 3 2
11221

The string is '1','1','2','2','1' → sum 1+1+5+5+1 = 13.

So code works.

Now, considering the data size. The string can be 1e5 characters. Each iteration is O(1). So in Python, even for 1e5 iterations, it's acceptable.

In terms of memory, storing the a list as four integers is negligible. The string is read as a single string, which is okay. Python can handle 1e5 characters in a string.

So the code is optimal. There's no way to optimize further. It's O(n) time and O(1) extra space (other than the input storage). Because we process each character once, and sum as we go.

Thus, this approach is correct and efficient.
</think>

```python
a = list(map(int, input().split()))
s = input().strip()
total = 0
for c in s:
    total += a[int(c) - 1]
print(total)
```