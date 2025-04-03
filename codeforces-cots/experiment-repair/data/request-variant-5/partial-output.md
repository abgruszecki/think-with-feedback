<think>
Okay, let's see. I need to solve this problem where I have to determine which friends have the most taxi numbers, pizza numbers, and girls' numbers in their phonebooks. Hmm. Let's break down the problem.

First, the problem says that taxi numbers are six identical digits. Like 22-22-22. So for each number, I need to check if all six digits are the same. So the steps here are: take each phone number, remove the hyphens, and check if all characters are the same.

Next, pizza numbers are decreasing sequences of six different digits. So, for example, 98-73-21. When concatenated, that's 987321. Each digit must be strictly decreasing, and all six must be different. So I need to check if each digit is less than the previous one. Also, all six must be unique. Wait, but the problem says "necessarily a decreasing sequence of six different digits". So yes, all six must be different and in a strictly decreasing order. So steps here: check if the digits form a strictly decreasing sequence, and all are unique.

Other numbers are considered girls' numbers. So any number that is not taxi or pizza falls into this category.

The input has n friends, each with a list of si numbers. For each friend, count how many taxi, pizza, and girls' numbers they have. Then, for each category, find the maximum count among all friends and list all friends who have that maximum count. The output has to be in the order they were input, separated by commas and ending with a period.

Now, the constraints: n is up to 100, each si can be up to 100. So total numbers are up to 100 * 100 = 10,000. That's manageable. So processing each number for each friend is feasible.

So, the plan is:

1. Read n friends.
2. For each friend, process their si numbers:
   a. For each number, check if it's a taxi, pizza, or girl.
   b. Count each type.
3. For each category (taxi, pizza, girls), collect the maximum count.
4. Find all friends with that count in each category, maintaining input order.
5. Output the results according to the specified format.

Now, the key steps are efficiently checking each number's type.

Let's think about the checking functions.

For taxi: the number, when hyphens removed, must be all same digits. So, for example, "22-22-22" becomes "222222". All characters must be equal. So we can take the first character and check that all others are equal to it. Alternatively, convert to a set and see if the length is 1. Either way is O(6) steps, which is trivial.

For pizza: the digits must be strictly decreasing and all unique. So, for the concatenated string (after removing hyphens), check that each digit is less than the previous one. Also, check that there are no duplicates. Wait, but if they are strictly decreasing, then duplicates can't exist. Because in a strictly decreasing sequence, each next digit is smaller than the previous. So if any two adjacent digits are equal, the sequence is invalid. So perhaps the check for strictly decreasing implies uniqueness. Wait, no. Wait, no. Suppose the digits are 4,3,3,2,1,0. Then the sequence is not strictly decreasing. So the check for strictly decreasing is sufficient to ensure that all digits are unique. Because if the digits are in strictly decreasing order, then each digit is smaller than the previous. Therefore, all digits must be distinct. So for pizza, we can just check that each digit is less than the previous. So the steps are: check that each digit is less than the previous. If yes, then it's a pizza. Otherwise, not.

So, for example, 987654 is valid. 98-76-54 is okay. 98-73-21 is 987321: 9>8>7>3>2>1, so yes. 22-22-22 is taxi. 99-99-98 is not pizza because the first two digits are same, so not strictly decreasing.

So for a pizza number, when the hyphens are removed, the sequence must be a strictly decreasing sequence. So, for each digit in the concatenated number (let's say d0, d1, d2, d3, d4, d5), check if d0 > d1 > d2 > d3 > d4 > d5. If yes, then it's a pizza. Otherwise, not.

So the check for pizza is straightforward.

Once the counts are done for each friend, we need to track the maximum counts for each category. Then collect all friends with those maximum counts in each category, in the input order.

Now, the data structures needed:

For each friend, store their name, and their counts for taxi, pizza, girls. So perhaps a list of dictionaries or objects. But in Python, perhaps a list of tuples: (name, taxi_count, pizza_count, girls_count).

Then, for each category, we need to find the maximum count among all friends, then collect all friends who have that count, preserving their order.

So for example, in the first sample input:

Friend 0 (Fedorov) has 1 taxi, 1 pizza, 0 girls.

Friend 1 (Melnikov) has 0 taxi, 0 pizza, 3 girls.

Friend 2 (Rogulenko) has 6 taxi, 1 pizza, 0 girls.

Friend 3 (Kaluzhin) has 2 taxi, 1 pizza, 0 girls.

So the maximum for taxi is 6 (Rogulenko). For pizza, the max is 1, shared by Fedorov, Rogulenko, Kaluzhin. For girls, max is 3 (Melnikov).

So the output is constructed accordingly.

Now, the steps in code:

Read n.

Then, for each friend in n:

   read si and name.

   read si phone numbers.

   for each number:

      process to determine type.

      update counts.

So, code steps:

Read n.

Then for each friend:

   read a line containing si and name. Split into integer si and string name.

   then read si lines of phone numbers.

   initialize taxi, pizza, girl counts to 0.

   for each phone number:

      s = phone number with hyphens removed. So s = number.replace('-', '') → a 6-digit string.

      check if all characters are same: for taxi.

      else, check if digits are strictly decreasing: for pizza.

      else, it's a girl.

      increment the counts accordingly.

Once all friends are processed, for each category (taxi, pizza, girl), collect all friends and their counts.

For each category:

   find the maximum count.

   collect all friends (in order) whose count equals the maximum.

Now, output the required lines.

The output requires that each line starts with a specific phrase, then the list of names separated by comma and space, ending with a period. If multiple names, they are in the order of input.

Now, in Python, for each category:

max_count = max(friend[category_index] for friend in friends_list)

selected = [friend for friend in friends_list if friend[category_index] == max_count]

But the friends_list is the original order, so when we loop through all friends, and collect those with max_count, we can just append their names in the order they were processed.

Wait, but friends_list is a list of the friends in the input order. So when building the selected list, it's in the order of the original input. So for example, in the first sample, for pizza, the selected friends are Fedorov, Rogulenko, Kaluzhin. But how are they ordered? Since they were the first, third, and fourth friends. So the code would collect them in that order.

So in the code, we can create a list of friends as they are read. Then, for each category, iterate through all friends and check if their count is equal to the maximum, appending the name to the list if it is.

Now, the code structure in Python:

Read n.

friends = []

for _ in range(n):

    line = input().split()

    # Split into si and name. But the name can have spaces? Wait, no. The input format says: each friend's data starts with a line containing integer si and namei. The name is a non-empty sequence of uppercase and lowercase letters, no more than 20 characters, and no spaces. Because in the sample inputs, names are single words. So line.split() will split into two parts: si is the first, name is the rest? Wait, no. For example, if the line is '3 John Doe', then split() would give ['3', 'John', 'Doe'], but according to the problem statement, namei is a single string (like "Fedorov"). So the name is a single word. So the line can be split into two parts: si (integer) and name (string). So for line in input:

    parts = input().split(maxsplit=1)

    if len(parts) < 2:  # in case si is 0? Wait, si can be 0. For example, the third sample input has a friend with 0 Smietanka. So when si is 0, the line is '0 Smietanka' → parts would be ['0', 'Smietanka'].

    So for each friend:

    si_part, name_part = parts[0], parts[1]

    si = int(si_part)

    name = name_part.strip()

    Then, read si lines of phone numbers.

    So:

    numbers = [input().strip().replace('-', '') for _ in range(si)]

    Now, process each number.

    taxi = 0

    pizza = 0

    girls = 0

    for num in numbers:

        if all(c == num[0] for c in num):

            taxi +=1

        else:

            # check if strictly decreasing

            is_pizza = True

            for i in range(1,6):

                if num[i] >= num[i-1]:

                    is_pizza = False

                    break

            if is_pizza:

                pizza +=1

            else:

                girls +=1

    friends.append( (name, taxi, pizza, girls) )

Once all friends are processed, for each category (taxi, pizza, girls):

   collect the counts and find the max.

So for taxi:

max_taxi = max(f[1] for f in friends)

selected_taxi = [f[0] for f in friends if f[1] == max_taxi]

Then, output the first line with the names in selected_taxi, joined with ', ', and ending with '.'.

Same for pizza and girls.

Wait, the friends list is in the order of input, so the selected lists will have names in the order they were input, which is correct.

Now, the output formatting:

For each category:

print the phrase, then the list of names separated by ', ', and ending with a '.'.

But if there are multiple names, they are separated by ', ', and the last one is followed by a '.'.

For example, if the selected list is ['A', 'B', 'C'], the output is "A, B, C."

So in code, for a selected list:

if len(selected) == 0:

    # But according to the problem statement, each friend's name is non-empty. Also, the constraints say that si can be zero, but friends can have any counts (including zero in all categories). So in such cases, for example, if all friends have zero taxi numbers, then all are considered as having maximum (zero), and the output will list all friends.

But according to the sample inputs, like the third example, there's a friend with 0 phone numbers. Let's see:

Sample 3 input:

3

3 Kulczynski

numbers...

4 Pachocki

numbers...

0 Smietanka → here, Smietanka's phonebook is empty, so all counts (taxi, pizza, girl) are zero.

So in the third sample's output, for girls, the max is zero (since all friends may have zero). But according to the sample output, the girl's line is: "If you want to go to a cafe with a wonderful girl, you should call: Kulczynski."

Wait, let's look at the third sample input:

Sample input 3:

3

3 Kulczynski

22-22-22 → taxi (count 1)

65-43-21 → check if pizza. 6,5,4,3,2,1 → yes. So pizza count is 1.

98-12-00 → digits are 9,8,1,2,0,0 → not pizza. So this is a girl's number. So Kulczynski's counts: taxi 1, pizza 1, girl 1.

Friend Pachocki has 4 numbers:

11-11-11 → taxi (count 3 times?)

Wait, the input for Pachocki is 4 numbers: 11-11-11 (taxi), 11-11-11 (taxi), 11-11-11 (taxi), 98-76-54 (pizza). So his counts: taxi 3, pizza 1, girl 0.

Friend Smietanka has 0 numbers → all counts zero.

So when considering girls' numbers: Kulczynski has 1, Pachocki 0, Smietanka 0. So the max is 1 (Kulczynski). So the output for the girls line is Kulczynski.

So the code correctly captures that even if some friends have zero, others may have higher.

So the code must handle the case where all friends have zero in a category, which would result in all friends being selected (since max is zero, and all have zero). But that's possible.

So in code, regardless of the counts, it's handled correctly.

So the code for each category is:

max_count = max(friend[category] for friend in friends)

selected = [friend[0] for friend in friends if friend[category] == max_count]

Then, for the output line:

phrase = "If you want to call a taxi, you should call: "

names_str = ", ".join(selected) + '.'

print(phrase + names_str)

Same for the other categories.

Now, the code must read the input correctly. Let's test reading each friend's line.

For example, the input line could be "0 Smietanka", which is split into ['0', 'Smietanka'], so si is 0, name is Smietanka. Then, si lines to read → 0 lines, so no numbers. So the counts are zero.

Another example: "7 Rogulenko" → si is 7, name is Rogulenko. Then read 7 numbers.

Now, code for reading friends:

In Python, after reading n, for each friend:

line = input().strip()

split into parts. But the first part is si, and the rest is name. For example, the line could be "3 Melnikov" → split into ['3', 'Melnikov'], but if the name has a space? According to the problem statement, the name is a non-empty sequence of uppercase and lowercase letters. So the name does not contain spaces. So the line can be split into two parts: the first is si, the second is name. So using split(maxsplit=1) would work.

So code:

for _ in range(n):

    parts = input().split(maxsplit=1)

    if len(parts) < 2:

        # perhaps when the line is like "0" (but according to problem statement, namei is non-empty, so this is impossible. So maybe the input is always correct.)

    si = int(parts[0])

    name = parts[1].strip()

    numbers = [input().strip().replace('-', '') for _ in range(si)]

Then process the numbers.

Now, for the pizza check. Let's code that.

For a given number string (digits as a 6-length string), check if each digit is strictly less than the previous.

For example, '987654' → 9>8>7>6>5>4 → yes.

In code:

def is_pizza(s):

    for i in range(1, 6):

        if s[i] >= s[i-1]:

            return False

    return True

But the code can inline this check.

So for each number in numbers:

if all(c == s[0] for c in s):

    taxi +=1

else:

    is_pizza = True

    for i in 1 to 5:

        if s[i] >= s[i-1]:

            is_pizza = False

            break

    if is_pizza:

        pizza +=1

    else:

        girls +=1

Yes.

Now, considering edge cases.

For example, a pizza number with digits 5,4,3,2,1,0 → valid.

A number like 543210 → yes.

A number like 543210 → same as 543-21-0, concatenated.

Another case: 654321 → yes.

But a number like 654321 → yes.

Another case: 112233 → not pizza, since digits are not decreasing.

Another case: 987654 → yes.

What about 987754 → the third digit is 7, next is 7. So 7 >=7 → not pizza.

Now, code seems correct.

Testing the code with sample input 1:

Sample input 1:

4

2 Fedorov

22-22-22 → becomes '222222' → all same → taxi count 1.

98-76-54 → becomes '987654' → digits 9>8>7>6>5>4 → pizza count 1.

So Fedorov's counts: taxi 1, pizza 1, girl 0.

3 Melnikov

75-19-09 → 751909 → check:

7>5? yes. 5 < 1 → no. So not pizza. So it's a girl.

23-45-67 → 234567 → check digits: 2 <3 → no. So pizza check fails. So girl.

99-99-98 → 999998 → first two digits same → not taxi (since not all same). Check pizza: 9>9 → no. So girl. So Melnikov's counts: 0 taxi, 0 pizza, 3 girls.

Then the code's processing of these numbers should correctly count.

Now, code for the third sample input:

Friend 0: Kulczynski has 3 numbers.

22-22-22 → taxi (count 1).

65-43-21 → digits 6>5>4>3>2>1 → pizza (count 1).

98-12-00 → 981200 → check digits: 9>8 → yes. 8>1 → yes. 1 < 2 → no. So not pizza. So girl count 1.

So his counts are taxi:1, pizza:1, girl:1.

Friend 1: Pachocki has 4 numbers.

11-11-11 → taxi (count 1).

11-11-11 → taxi (count 2).

11-11-11 → taxi (count 3).

98-76-54 → pizza (count 1).

So his counts are taxi:3, pizza:1, girl:0.

Friend 2: Smietanka has 0 numbers → counts 0,0,0.

So for taxi category, max is 3 (Pachocki). So output Pachocki.

For pizza, the max is 1 (Kulczynski, Pachocki). So their pizza counts are 1 each. So selected names are Kulczynski, Pachocki.

Wait, in the third sample input, the output for pizza is "Kulczynski, Pachocki."

Wait, but the sample output is:

"If you want to order a pizza, you should call: Kulczynski, Pachocki."

But according to the sample input's third example:

Friend 0: Kulczynski has 1 pizza.

Friend 1: Pachocki has 1 pizza.

Friend 2: Smietanka has 0.

So the max is 1, and the selected friends are Kulczynski and Pachocki.

Which matches the sample output.

So the code's logic is correct.

Now, code for output.

In code, after collecting the selected names for each category, we need to join them with ', ' and append a '.'.

So for selected list:

print the phrase + ', '.join(selected) + '.'.

But if the selected list is empty, but according to the problem statement, each friend's name is non-empty, and the code includes all friends (even if they have zero counts) if the maximum is zero.

But how can the selected list be empty? Only if there are no friends, but n is at least 1 (as per the constraints, n ≥1). So n is 1 or more. So for each category, the selected list will have at least one name.

Thus, in code:

For each category, compute the selected list, then format as required.

Thus, the code should handle all cases.

Now, let's code this.

But code in Python:

Read n.

Then for each friend:

Read the line with si and name.

Read si lines of numbers.

Process each number.

Then store the counts.

Then, after processing all friends, for each category (taxi, pizza, girls):

Compute max count.

Collect names of friends with that count in order.

Print the phrase followed by the names joined with ', ' and a '.'.

Now, code:

n = int(input())

friends = []

for _ in range(n):

    # Read friend's data line

    parts = input().split(maxsplit=1)

    si = int(parts[0])

    name = parts[1].strip()

    # Read si phone numbers

    numbers = []

    for _ in range(si):

        num = input().replace('-', '')  # remove hyphens

        numbers.append(num)

    # Count taxi, pizza, girl

    taxi = 0

    pizza = 0

    girls = 0

    for num in numbers:

        if all(c == num[0] for c in num):

            taxi +=1

        else:

            is_pizza = True

            for i in range(1,6):

                if num[i] >= num[i-1]:

                    is_pizza = False

                    break

            if is_pizza:

                pizza +=1

            else:

                girls +=1

    friends.append( (name, taxi, pizza, girls) )

# Now process each category

# Taxi is friends[i][1]

max_taxi = max(f[1] for f in friends)

selected_taxi = [f[0] for f in friends if f[1] == max_taxi]

# Pizza is friends[i][2]

max_pizza = max(f[2] for f in friends)

selected_pizza = [f[0] for f in friends if f[2] == max_pizza]

# Girls is friends[i][3]

max_girls = max(f[3] for f in friends)

selected_girls = [f[0] for f in friends if f[3] == max_girls]

# Output

print(f"If you want to call a taxi, you should call: {', '.join(selected_taxi)}.")
print(f"If you want to order a pizza, you should call: {', '.join(selected_pizza)}.")
print(f"If you want to go to a cafe with a wonderful girl, you should call: {', '.join(selected_girls)}.")

Wait, but the problem says to follow the output format strictly. Let's check the sample input 1's output:

In sample input 1, the pizza selected list is "Fedorov, Rogulenko, Kaluzhin."

The code for selected_pizza would be [f[0] for f in friends if f[2] == max_pizza]

But in sample input 1, the friends are:

Fedorov (index 0): pizza 1.

Melnikov (index 1): pizza 0.

Rogulenko (index 2): pizza 1.

Kaluzhin (index 3): pizza 1.

So selected_pizza would be the names of friends 0, 2, 3. Which are in the order of input, so the code correctly appends them in the order of their occurrence in the input.

Thus, the code's output for sample 1's pizza line would be "Fedorov, Rogulenko, Kaluzhin." which matches the sample output.

Now, the code uses f-strings to format the output. The phrases must be exactly as specified. Let me check:

The first line's phrase is "If you want to call a taxi, you should call: ".

The code uses:

print(f"If you want to call a taxi, you should call: {', '.join(selected_taxi)}.")

Which is correct.

Yes.

Now, what about friends with the same name? The problem says that friends are given in the input, but their names are not necessarily unique. But the code will process them as per the input, including the same names multiple times. But according to the problem statement, the names are printed in the order of input. So even if two friends have the same name, both will be listed. For example, if two friends named John are in the input, and both are selected, they will appear as "John, John."

Now, code seems correct.

Testing with an executable snippet.

```python
def test_program(input_stream, output_stream):
  n = int(input_stream.readline())
  friends = []
  for _ in range(n):
      parts = input_stream.readline().split(maxsplit=1)
      si = int(parts[0])
      name = parts[1].strip()
      numbers = [input_stream.readline().replace('-', '') for _ in range(si)]
      taxi = pizza = girls = 0
      for num in numbers:
          if all(c == num[0] for c in num):
              taxi += 1
          else:
              is_pizza = True
              for i in range(1, 6):
                  if num[i] >= num[i-1]:
                      is_pizza = False
                      break
              if is_pizza:
                  pizza += 1
              else:
                  girls += 1
      friends.append((name, taxi, pizza, girls))

  max_taxi = max(f[1] for f in friends)
  selected_taxi = [f[0] for f in friends if f[1] == max_taxi]
  print(f"If you want to call a taxi, you should call: {', '.join(selected_taxi)}.", file=output_stream)

  max_pizza = max(f[2] for f in friends)
  selected_pizza = [f[0] for f in friends if f[2] == max_pizza]
  print(f"If you want to order a pizza, you should call: {', '.join(selected_pizza)}.", file=output_stream)

  max_girls = max(f[3] for f in friends)
  selected_girls = [f[0] for f in friends if f[3] == max_girls]
  print(f"If you want to go to a cafe with a wonderful girl, you should call: {', '.join(selected_girls)}.", file=output_stream)

import io

TEST_CASES = [{
    "input": """\
4
2 Fedorov
22-22-22
98-76-54
3 Melnikov
75-19-09
23-45-67
99-99-98
7 Rogulenko
22-22-22
11-11-11
33-33-33
44-44-44
55-55-55
66-66-66
95-43-21
3 Kaluzhin
11-11-11
99-99-99
98-65-32\
""",
    "output": """\
If you want to call a taxi, you should call: Rogulenko.
If you want to order a pizza, you should call: Fedorov, Rogulenko, Kaluzhin.
If you want to go to a cafe with a wonderful girl, you should call: Melnikov.\
""",
}, {
    "input": """\
3
5 Gleb
66-66-66
55-55-55
01-01-01
65-43-21
12-34-56
3 Serega
55-55-55
87-65-43
65-55-21
5 Melnik
12-42-12
87-73-01
36-04-12
88-12-22
82-11-43\
""",
    "output": """\
If you want to call a taxi, you should call: Gleb.
If you want to order a pizza, you should call: Gleb, Serega.
If you want to go to a cafe with a wonderful girl, you should call: Melnik.\
""",
}, {
    "input": """\
3
3 Kulczynski
22-22-22
65-43-21
98-12-00
4 Pachocki
11-11-11
11-11-11
11-11-11
98-76-54
0 Smietanka\
""",
    "output": """\
If you want to call a taxi, you should call: Pachocki.
If you want to order a pizza, you should call: Kulczynski, Pachocki.
If you want to go to a cafe with a wonderful girl, you should call: Kulczynski.\
""",
}, ]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    test_program(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, \
        f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

print('Tests passed 😎')
```

RUN_SNIPPET
```text
Traceback (most recent call last):
  File "<stdin>", line 124, in <module>
AssertionError: Test case 0 failed.
Expected: 'If you want to call a taxi, you should call: Rogulenko.\nIf you want to order a pizza, you should call: Fedorov, Rogulenko, Kaluzhin.\nIf you want to go to a cafe with a wonderful girl, you should call: Melnikov.'
Got: 'If you want to call a taxi, you should call: Fedorov, Melnikov, Rogulenko, Kaluzhin.\nIf you want to order a pizza, you should call: Fedorov, Rogulenko, Kaluzhin.\nIf you want to go to a cafe with a wonderful girl, you should call: Rogulenko.'
```