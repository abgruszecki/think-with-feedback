<think>
Okay, let's tackle this problem. The task is to handle user registrations such that if a name already exists, we append the smallest possible integer starting from 1. So each time a name is reused, the next number in sequence is added. For example, the first occurrence is OK, the second becomes name1, then name2, etc.

First, the input size is up to 1e5. So whatever data structure we use, it needs to handle that efficiently. Using a hash map (like a Python dictionary) seems obvious here. The key is the original name, and the value could be the count of how many times it's been used. But wait, wait. Because when a user registers with a name, the next number is the smallest available. So if the name is added again, we check the current count and assign that number, then increment the count. For example, for the first name 'first', the count is 0. Then the first occurrence is OK (count becomes 1). The next 'first' becomes first1 (count is now 2). Then the third 'first' would be first2, and so on. Wait, no. Wait, the first time 'first' is added, the count is 1. When it comes again, we append 1 (since the current count is 1), then increment the count to 2. Then next time, append 2, increment to 3. So the count for each name represents how many times it's been used, and the next suffix is the current count. Because for the first duplicate, the count is 1, so the name becomes name1. Then the count increments by 1 each time.

So the approach is: maintain a dictionary where each key is the username, and the value is the next number to append. When a user submits a name, check if it's in the dict. If not, output OK and add it to the dict with value 1. If it is in the dict, output the name followed by the current value, then increment the value in the dict by 1.

Wait, yes. Because the first occurrence is OK, and the dict stores the next suffix. So for the first occurrence, it's not present, output OK, then set the value to 1. The second occurrence (same name) will output name1 and increment to 2. The third occurrence outputs name2 and increments to 3. That's correct.

So the data structure is a simple dictionary. Each entry tracks the next number to use for that name.

Now, considering the constraints. For n up to 1e5, a dictionary in Python can handle that. Each insertion and lookup is O(1) on average, which is acceptable. So the algorithm is O(n), which should work within 5 seconds.

Testing with the examples:

First example input:

4
abacaba
acaba
abacaba
acab

Processing:

- abacaba: not in the dict. Output OK. dict becomes {'abacaba': 1}
- acaba: not present. Output OK. dict now {'abacaba':1, 'acaba':1}
- abacaba: exists. Output abacaba1 (current value 1). Then increment to 2.
- acab: not present. Output OK. dict adds 'acab' with 1.

Which matches the sample output.

Another example:

6 entries, the first is 'first', which becomes OK and stored as 1. Next 'first' outputs first1 and increments to 2. Then 'second' is OK. Next 'second' becomes second1. Then 'third' OK, then third1. So the output matches.

Now, the code structure would be:

Read n.

Initialize a dictionary, say, name_counts.

Loop n times:

   Read the name.

   If the name is not in the dict:

      print OK

      add it to the dict with value 1.

   else:

      current = name_counts[name]

      print(name + str(current))

      increment name_counts[name] by 1.

But wait, in the first case, after adding the name, the next occurrence will have the count 1, which is correct. So the code should work.

But let's think about possible issues. What about when the name already has numbers in it? Like if someone registers 'name1' as a new name. But according to the problem statement, the system appends the numbers only when the original name is already present. So 'name1' is treated as a different name. So the code doesn't need to check if the generated name is already in the database. Because the problem states that the system's generated names (like name1, name2) are generated such that they don't exist in the database. Wait, but according to the problem description, the system's generated names are inserted into the database. So for example, when a user registers 'name' again, the system generates name1, adds that to the database. So the next time, if the user registers 'name' again, the system will generate name2, and so on.

Wait, but what if someone tries to register 'name1' as a new name? Then that's allowed. So the code as written would handle it. For example:

Suppose:

n=3

Input:

name

name

name1

Processing:

First name: OK. dict has 'name' :1.

Second name: name1 is output, dict becomes 'name' :2.

Third input is name1: it's not in the dict. So output OK, and dict adds 'name1' :1.

So the output would be:

OK

name1

OK

Which is correct.

So the code as written correctly handles such cases.

Therefore, the approach is correct.

Now, implementing in Python. But considering the input size (n=1e5), we need to read the input efficiently. Using input() in a loop can be slow if we have 1e5 lines. So in Python, it's better to read all lines at once. For example:

import sys

n = int(sys.stdin.readline())

for _ in range(n):

   name = sys.stdin.readline().strip()

   ...

But even better, read all the lines at once. But in practice, using a loop with sys.stdin.readline() for each line is acceptable. Because 1e5 is manageable, but in Python, sometimes for very large data, it's better to read the entire input first. Let's see.

But for this problem, using sys.stdin.readline() in a loop is okay. Because each line is read as it's processed, and the code is O(n) time.

So the code would be:

import sys

def main():

    import sys

    n = int(sys.stdin.readline())

    counts = {}

    for _ in range(n):

        name = sys.stdin.readline().strip()

        if name in counts:

            cnt = counts[name]

            print(f"{name}{cnt}")

            counts[name] += 1

        else:

            print("OK")

            counts[name] = 1

But wait, here the generated name (name + cnt) is added to the database? Wait, no. According to the problem statement, the system's generated name is inserted into the database. Wait, the original problem says: when a name is taken, the system generates a new name (like name1), inserts it into the database, and returns it as a prompt.

But according to the current code, when you process a name that's already in the database (say, 'name'), you generate name1, but the code does not add 'name1' to the counts. Wait, this is a problem. Because the code's logic is only tracking the original name's count, not the generated names.

Wait, this is a critical mistake here. Let me re-read the problem statement.

Problem statement:

Each time a new user wants to register, he sends to the system a request with his name. If such a name does not exist in the system database, it is inserted into the database, and the user gets the response OK. If the name already exists, the system makes up a new user name (namei), sends it as a prompt, and also inserts the prompt into the database.

Wait, so the generated name (like name1) must also be added to the database. Otherwise, if the user tries to register name1 again, it would be allowed. But according to the problem's example, the generated names are part of the database.

For example, in the first sample input:

4

abacaba

acaba

abacaba

acab

The third input is abacaba again. The output is abacaba1, and this name is inserted into the database. So when processing the fourth input (acab), it's a new name. But if another abacaba1 is sent, then the system would generate abacaba11 (if the count for abacaba1 is 1). Or wait, no. Let's think.

The database starts empty.

First 'abacaba' is added. Output OK. Database has 'abacaba'.

Second 'acaba' is added. Output OK. Database has 'abacaba', 'acaba'.

Third 'abacaba' exists. So generate abacaba1. Output abacaba1. Add abacaba1 to the database.

Fourth 'acab' is added. Output OK. Database has 'abacaba', 'acaba', 'abacaba1', 'acab'.

So, if someone then sends 'abacaba1', the first time, it's not in the database, so output OK. But according to our current code, the counts dictionary only tracks the original names, not the generated ones. So the code as written would not handle this case correctly.

So the current approach is wrong. Oh, this is a big mistake. The code above only tracks the original names, but the generated names need to be stored in the database as well.

So, the initial approach is incorrect. We need to track all names (original and generated) in the database.

So the problem requires that when a generated name is added, it's part of the database. So, for example, if a user tries to register 'name1' as a new name (not generated by the system), but the system has a 'name1' already generated, then that would conflict.

Wait, no. Let's clarify:

The system's database is a collection of all names that have been either registered as original or generated. So each generated name (like name1) is part of the database, and subsequent requests for name1 would have to generate name11, name12, etc.

Therefore, the code's current approach is incorrect. Because it only tracks the count for the original name, not for the generated names. For example:

Suppose:

Input lines:

name

name

name1

name1

Processing:

First line: name is not in the database. Output OK. Add name to the database (counts['name'] = 1).

Second line: name exists. Generate name1. Output name1. Add name1 to the database (counts['name1'] = 1).

Third line: name1 is now in the database. So generate name11. Output name11. Add name11 to the database (counts['name11'] = 1).

Fourth line: name1 exists. Generate name12. Output name12. Add name12 to the database.

But according to the code as written earlier, the third line (name1) is considered a new name. Because the code's counts dictionary only tracks the original name. So in the code:

Third line is 'name1' which is not in counts. So output OK. Add counts['name1'] = 1.

But according to the problem statement, the generated name (name1 from the second line) was added to the database. So when the third line is 'name1', the system should check if 'name1' is present. Since it is (from the second line's generated name), the system should generate name11.

But the code as written does not track the generated names in the counts. So the code would incorrectly allow 'name1' to be added as a new name, leading to a wrong answer.

So the initial approach is wrong. Therefore, the code must track all names that have been inserted into the database, whether they are original or generated.

This changes everything. So the problem is more complex than initially thought.

So how do we handle this?

Each generated name is part of the database. So every time a name is generated, it's added to the database, just like the original names.

Therefore, the counts dictionary must track all the names that are in the database, including the generated ones.

But how to track the counts for each possible base name? Because the generated names can have numbers appended, which complicates the counting.

Wait, but the problem is that when a user submits a name, whether it's original or generated, the system must check if that name is already in the database. If it is, then generate the next available name for that submitted name.

Wait, no. Wait, the problem says:

Each time a new user sends a request with their desired name. The system checks if that name is in the database. If not, add it. If yes, generate the next available name (appending the smallest possible i) and add that generated name to the database.

So the system treats each submitted name as a base name. For example:

If the user submits 'name', the system checks if 'name' is in the database. If yes, generate 'name1', add it to the database, and return 'name1'.

If another user submits 'name1', the system checks if 'name1' is in the database. If yes, generate 'name11', add it to the database, and return 'name11'.

But according to the initial approach, the code doesn't track generated names. So in this case, the code would allow 'name1' to be added as a new name, which is wrong.

Thus, the initial approach is incorrect. The problem requires that all generated names are stored in the database, so that subsequent submissions of those names (as user requests) are checked against the entire database.

So the solution must track all names that have been added to the database (original and generated) and for each submitted name, check if it's in the database. If not, add it and output OK. If it is in the database, generate the next available suffix for that submitted name.

Wait, but how to track the count for each submitted name? For example, if a user submits 'name', and it's already present, the system appends 1, which becomes name1. Then, if the same user submits 'name' again, the next count is 2, so name2. But if another user submits 'name1', and it's in the database (because of the previous generated name), then the system must generate name11.

So the counts need to be tracked per submitted name, not per original name.

Wait, no. The counts are per the base name that the user is submitting. Each time a user submits a name, the system checks if that name is present. So, for example:

Submitted name is 'name' → check if 'name' is in the database. If so, generate name1, add to the database. The count for 'name' is incremented.

Another submission of 'name' → check again if 'name' is present (it is), so generate name2, add to the database, count becomes 3.

A submission of 'name1' → check if 'name1' is present. If it's present (from previous generation), generate name11, add to the database, count for 'name1' becomes 2.

So each name (original or generated) has its own count. So the counts must track for each possible base name (which can be any string), how many times it has been used. So the data structure is a dictionary where the keys are all possible names (original and generated) and the value is the current count for that name.

Wait, but that's impossible. Because when a name is generated (like name1), it's added to the database, and if a user submits name1 again, it's treated as a new base name, which must be checked. So the dictionary needs to track for each possible name (whether generated or original) how many times it has been used.

But then, the code would look like this:

When a user submits a name X:

If X is not in the database:

   add X to the database with count 1. Output OK.

Else:

   find the smallest i (starting from 1) such that X + i is not in the database.

   output X + i.

   add X + i to the database with count 1.

   Also, increment the count for X (the original name) so that next time, we can start from the next number.

Wait, but this approach is wrong. Because the count for X represents the number of times X has been registered. So for example, after the first X is added (count 1), the next X would generate X1 (count becomes 2). The third X would generate X2 (count becomes 3). So in this case, the count for X is the number of times it's been used, and the generated name is X followed by (count-1).

But then, if X is 'name1' and it's in the database, then the count for 'name1' is 1, so the next submission of 'name1' would generate 'name11', increment count to 2.

But the problem is that when the user submits a name, the system checks if that name exists. If it does, then the system generates the next possible name for that specific name, not the original. So the count is per submitted name.

Therefore, the correct approach is to track for each possible name (including generated ones) how many times it has been used. So the dictionary maps each possible name to the number of times it has been used, which determines the next suffix.

But this can't be right. Because when you generate a name like X1, then X1 is added to the database, and if someone submits X1 again, the system should generate X11, X12, etc.

So the initial approach where the dictionary tracks the count for each possible name (even generated ones) is necessary. But how can we track that?

In the initial code approach, the code only tracks the count for the original name, not the generated ones. So when a generated name is added to the database, it's not tracked, leading to errors.

So, the problem requires that all names (original and generated) are tracked. So, each time a generated name is added to the database, it's treated as a new entry in the dictionary. But that's not feasible, because each generated name can be up to 32 characters, and there's no limit on the number of generated names. For example, if a user submits 'a' 1e5 times, each time the generated name is a1, a2, etc. Then, each of these generated names (a1, a2, a3, etc) would need to be tracked in the dictionary. But that's O(n) entries, which for n up to 1e5 is manageable. But in Python, the dictionary would have O(n) entries, which for 1e5 is acceptable.

But then, how to handle the counts for each generated name?

Wait, no. Let's think again. Let's take the first example.

Sample Input 2:

6

first

first

second

second

third

third

Sample Output:

OK

first1

OK

second1

OK

third1

Processing steps:

1. 'first' → not in the dict. Add 'first' → count=1. Output OK.

2. 'first' → exists. Generate first1. Add 'first1' → count=1. Also, increment 'first' count to 2. Output first1.

3. 'second' → not in the dict. Add, output OK. 'second' count=1.

4. 'second' → exists. Generate second1. Add 'second1' → count=1. Increment 'second' count to 2. Output second1.

5. 'third' → not in the dict. Add, output OK.

6. 'third' → exists. Generate third1. Add 'third1' → count=1. Output third1.

In this case, the code's initial approach (only tracking the original names' counts) would work. Because when the 'first' is submitted the second time, it's in the dict with count 2. So the generated name is first1 (count-1). Then, when 'first1' is added, it's part of the dict. So the next time someone submits 'first1', it's present, and the code would generate first11.

But according to the initial code approach, the 'first1' is not tracked in the counts. So in the code, when the third input is 'second', it's added to the dict. But if someone submits 'first1' in the next input, the code would output OK, since it's not in the dict. But according to the problem statement, 'first1' was added to the database, so it should generate first11.

Thus, the code's approach is wrong. So the initial approach is incorrect. We need to track all generated names in the database.

But how?

The correct approach is: each generated name is added to the database. So the counts dictionary must track all names that have been added, including the generated ones.

But how to handle the counts for each name, whether original or generated?

The problem is that each time a user submits a name (original or generated), the system must check if that name is in the database. If it is, generate the next available suffix for that name and add it to the database.

So for example:

User submits 'name' → added as OK. counts['name'] = 1.

User submits 'name' again → generate name1. Add counts['name'] = 2, and also add counts['name1'] = 1.

User submits 'name1' → check if it's in counts. It is. So generate name11. Add counts['name1'] = 2, and add counts['name11'] = 1.

Thus, the counts dictionary tracks all names, original and generated. The count for a name is the number of times it has been used as a base name.

But this leads to a problem. Because each generated name (like 'name1') is added to the database. So when a user submits 'name1', the system must generate the next available name for 'name1' (i.e., name11, name12, etc.).

Thus, the correct approach is to track for every possible name (original and generated) how many times it has been used. So the counts dictionary must include all such names.

But how to implement this?

In the initial code approach, when a name is generated, the code outputs it but does not add it to the counts. So the code is wrong. To fix this, the generated names must be added to the counts.

So, the correct code would be:

For each name in the input:

   if the name is not in counts:

       output OK

       add name to counts with value 1

   else:

       generate the new name as name + count, where count is counts[name]

       output the new name

       add the new name to counts with value 1

       increment counts[name] by 1

But wait, no. Because when you generate name + count (e.g., name1), this generated name must be added to the counts. So the next time someone submits name1, it's in the counts, and the system will generate name11.

So the code should:

When a name is found in the counts, the new name is generated as name + str(count), which is then added to the counts. Also, the original name's count is incremented by 1.

But this approach would work. Let's see.

Example:

Processing the second sample input:

6 entries.

First 'first' is added to counts. counts = {'first':1}.

Second 'first' is in counts. Generate 'first1', output it. Add 'first1' to counts with value 1. Increment 'first' to 2. counts is {'first':2, 'first1':1}.

Third 'second' is added. counts now includes 'second':1.

Fourth 'second' is present. Generate 'second1', add to counts, increment 'second' to 2. counts has 'second1':1.

Fifth 'third' added.

Sixth 'third' is present. Generate 'third1', add to counts, increment 'third' to 2.

Which matches the sample output.

But what about when the generated name is processed again?

For example, input:

3

name

name

name1

Processing:

1. name → added. counts: {'name':1}

2. name → present. generate name1. Add name1 to counts. counts: {'name':2, 'name1':1}

3. name1 → present. generate name11. add name11 to counts. counts: {'name1':2, 'name11':1}

Output for third input is name11.

But according to the problem statement, when the user submits name1 (the third input), the system checks if name1 is in the database. It is (added in step 2). So generate name11.

So the code would handle this correctly.

Thus, the code needs to:

- For each input name:

   if name not in counts: output OK and add to counts with 1.

   else:

       new_name = name + str(counts[name])

       output new_name

       add new_name to counts with 1.

       increment counts[name] by 1.

But wait, in this code, when a name is found in counts, the new name is generated, added to counts (so subsequent submissions of this new name will be handled), and the original name's count is incremented.

This approach should work.

But let's test with the example where a generated name is submitted again.

Test case:

Input:

3

name

name

name1

The code's processing:

Line 1: 'name' not in counts. Output OK. counts = {'name':1}

Line 2: 'name' is in counts. Generate name1. Output name1. Add 'name1' to counts with 1. Increment 'name' to 2. counts now {'name':2, 'name1':1}

Line 3: 'name1' is in counts. Generate name11. Output name11. Add 'name11' to counts with 1. Increment 'name1' to 2.

Thus, outputs are:

OK

name1

name11.

Which is correct.

Thus, this approach seems correct.

But what about memory? For each generated name, we add an entry in the counts dictionary. For n=1e5, the worst case is when each name is unique. Then the dictionary has 1e5 entries. But if the names are all the same, like n=1e5 submissions of 'name', then the first submission adds 'name' →1. The second generates 'name1', adds to counts. Third generates 'name2', adds to counts. And so on. So for 1e5 submissions of 'name', the dictionary would have 'name' and 'name1', 'name2', ... 'name99999'. Thus, 1e5 entries. Which is manageable.

But in Python, each string is stored as a separate key in the dictionary. For 1e5 keys, each up to 32 characters, it's acceptable.

Thus, the code would be:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    import sys

    counts = {}

    n = int(input_stream.readline())

    for _ in range(n):

        name = input_stream.readline().strip()

        if name in counts:

            # Generate new name

            new_name = f"{name}{counts[name]}"

            print(new_name, file=output_stream)

            # Add the new_name to counts with 1 (since it's now in the database)

            counts[new_name] = 1

            # Increment the original name's count

            counts[name] += 1

        else:

            print("OK", file=output_stream)

            counts[name] = 1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
first
first
second
second
third
third
""",
            "output": \
"""\
OK
first1
OK
second1
OK
third1
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

Sample input:

6

first

first

second

second

third

third

Processing:

Line 1: 'first' added. Output OK. counts {'first':1}.

Line 2: 'first' exists. Generate first1. Output. Add first1 to counts. counts['first'] becomes 2. counts['first1']=1.

Line 3: 'second' added. Output OK.

Line 4: 'second' exists. Generate second1. Add to counts. counts['second']=2, counts['second1']=1.

Line 5: 'third' added.

Line 6: 'third' exists. Generate third1. Add to counts.

So output is as expected.

Another test case where a generated name is used again:

Input:

3

a

a

a1

Processing:

Line 1: a added. Output OK.

Line 2: a exists. Generate a1. Add to counts. counts['a']=2, counts['a1']=1.

Line 3: a1 exists. Generate a11. Output a11. Add to counts. counts['a1']=2.

Thus, the output is OK, a1, a11.

This is correct.

Thus, this code should handle all cases correctly.

Now, considering the constraints. For n=1e5, each iteration is O(1) on average (dictionary lookups and insertions), which is acceptable. The total time is O(n).

In Python, using a dictionary and strings should be efficient enough. However, for very large n, the code must be optimized. But given that Python's dictionaries are hash tables with average O(1) operations, this should be manageable.

In terms of memory, each entry in the dictionary is a string (up to 32 characters plus the suffix). For n=1e5, each key is a string, so the memory usage would be around 1e5 * (average string size) bytes. Assuming each string is about 32 characters, it's 3.2 million bytes, which is around 3MB, which is well within the 64MB limit.

Therefore, the code should work.
</think>

```python
import sys

def main():
    counts = {}
    n = int(sys.stdin.readline())
    for _ in range(n):
        name = sys.stdin.readline().strip()
        if name in counts:
            cnt = counts[name]
            new_name = f"{name}{cnt}"
            print(new_name)
            counts[new_name] = 1
            counts[name] += 1
        else:
            print("OK")
            counts[name] = 1

if __name__ == "__main__":
    main()
```
