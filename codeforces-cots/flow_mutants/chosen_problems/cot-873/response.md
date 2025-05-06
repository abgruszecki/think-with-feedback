<think>
Okay, let's see. The problem is to find the number of distinct letters in Anton's set. The input is a string formatted with curly braces, and inside are letters separated by commas and spaces. So the task is to parse that string and count the unique letters.

First, I need to read the input line. Then, process it to extract the individual letters. Let's think about the structure of the input. The line starts with '{' and ends with '}'. Between them are the elements. Each element is a single lowercase letter, and they're separated by ', ' (comma followed by a space). For example, the first sample input is "{a, b, c}", which splits into 'a', 'b', 'c'.

So, the approach would be:

1. Remove the braces from both ends. So, take the input string, strip the first and last characters. Wait, but what if the input is empty like the third example? Like "{}" becomes an empty string in the middle. Then, splitting that would result in zero elements.

2. Split the remaining string into parts using the ', ' as the delimiter. So, for the input "a, b, c", splitting by ', ' gives ["a", "b", "c"].

3. Each of these parts is a single character. So, we can collect all these into a set, and then the size of the set is the answer.

But wait, what if there are leading or trailing spaces in the elements? Like, if the input is "{a , b}"? But according to the problem statement, the input is such that the letters are separated by a comma followed by a space. So each element is a single letter, and the commas are followed by a space. So the elements should not have any extra spaces except the mandatory ones after the comma. So, when splitting by ', ', each element is a single letter. But perhaps in the code, after splitting, we should check each part, strip any whitespace (but according to the problem statement, there's exactly one space after the comma, so each element is a single letter preceded by a space? Or maybe not. Let's see the examples. The first sample input is "{a, b, c}". So after the comma, there's a space. So each element is "a", " b", " c" after splitting by commas? Wait, no. Wait, the entire line is split by ', ' (comma followed by space), right?

Wait, the input format says: "between them, small English letters are listed, separated by a comma. Each comma is followed by a space." So the separator is ', ' (comma plus space). So the splitting should be on ', '.

Wait, for example, in the first sample input, the inner part is "a, b, c". Split by ', ' gives ["a", "b", "c"], right? Because the first element is "a", then after that comes ", b", which is split into next elements. Wait, no. Let's see. The entire string between braces is "a, b, c". If I split this by ', ', then the first split is "a", then "b", then "c". Wait, no. Let's take the string "a, b, c". Split by ', ' gives ["a", "b", "c"], because the commas followed by space are the separators. So that's correct.

But in the case of the second example input, "{b, a, b, a}", the inner part is "b, a, b, a", splitting by ', ' gives ["b", "a", "b", "a"], which when put into a set would have size 2.

So the steps are:

- Take the input string, e.g., s = input().strip()
- Remove the first and last characters (assuming they are '{' and '}')?
Yes. Because the problem says the input starts with '{' and ends with '}'.

So, the code would be:

s = input().strip()
if len(s) == 2:  # case of "{}"
    print(0)
else:
    parts = s[1:-1].split(', ')
    unique = len(set(parts))
    print(unique)

Wait, but what if the input is empty between the braces (like "{}")? Then s[1:-1] is an empty string. So split(', ') would return [''], but in that case, len(parts) would be 1? But in the case of "{}", the code would first check len(s) == 2. Which it is, so print 0. Otherwise, split the inner part.

Wait, let's see. The third example's input is "{}", so s is "{}". s[1:-1] is an empty string. Then split(', ') on an empty string would give [''] if the string is empty. Wait no. Let's test in Python:

s = ""
parts = s.split(', ')
print(parts)  # outputs ['']

Wait, splitting an empty string with any separator would produce a list containing one element, which is the empty string. So in the case of "{}", after s[1:-1] is "", then split(', ') gives [""], which would have parts as [""], and then the set would have one element, which is the empty string, leading to a count of 1. But the correct answer is 0. So the code would have to handle that case.

Ah, right. So the code as written would fail for the third example. Because in the case of "{}", the code would proceed to split the empty string into [''], then the set would have one element (empty string), leading to len being 1, but the correct output is 0.

So the code's initial check for len(s) ==2 is correct. So, the code:

s = input().strip()
if len(s) == 2:
    print(0)
else:
    inner = s[1:-1]
    parts = inner.split(', ')
    # Now, parts could be [''] if inner is empty (but that's handled by len(s)==2)
    # So, for inner not empty, split into parts. Then check each part?
    # But according to the problem statement, each part is a single lowercase letter. So the code is correct?
Wait, but in the third example, the code would have len(s) ==2, so print 0. Which is correct.

So the code would work for the sample inputs.

But what if the input is "{a}"? Then s is "{a}". len(s) is 3. So code proceeds to split the inner part "a" into parts, which would split on ', ', but since there's no ', ' in "a", the split returns ["a"]. So the set has size 1. Which is correct.

Another test case: "{a, }". Then the inner part is "a, ", split into ["a", ""]. So the parts would include an empty string. But according to the problem statement, the line is guaranteed to have a valid format. So this case is invalid, and the problem says that each element is a small letter. So the input will not have such cases. So we can assume that all parts after splitting are single letters.

Therefore, the code is safe.

So the code would read the input, check if it's "{}" (length 2), print 0. Otherwise, split the inner part into elements, create a set, count the size.

So the code is straightforward.
</think>

```python
s = input().strip()
if len(s) == 2:
    print(0)
else:
    print(len(set(s[1:-1].split(', '))))
```