<think>
Okay, let's tackle this problem. So, the task is to determine the maximum possible height each participant's mushroom can reach after two periods of growth, considering that each participant can choose the order of their two speeds (ai before the break and bi after, or vice versa). Then, we have to sort them in descending order of height, and if equal, by their original numbers.

Hmm, first, let's understand the problem step by step. Each participant has two speeds, ai and bi. The competition has two parts: the first part lasts t1 seconds, then during the break, the mushroom's growth is reduced by k percent. Then the second part is t2 seconds. The participant can choose which speed to use before and after the break. We need to compute for each participant the maximum possible height between the two possible strategies.

Wait, wait. The reduction during the break is k percent. So, the growth during the first part is vi * t1. Then, during the break, the growth is reduced by k percent. Wait, no. Wait, the problem statement says that during the break, for unexplained reasons, the growth of all mushrooms is reduced by k percent. So, after the break, when they start growing again, the total height after the first part is (vi * t1) * (1 - k/100), and then they add ui * t2. Wait, no. Wait, no. Wait, during the first part, they grow for t1 seconds at speed vi, then during the break, their total height is reduced by k percent. So, the first part's contribution is vi * t1, then that's multiplied by (1 - k/100), then the second part is ui * t2 added to that. So the total is (vi * t1 * (1 - k/100)) + (ui * t2). But the participant can choose whether to use ai as vi and bi as ui, or bi as vi and ai as ui. Because the order matters here.

So for each participant, the two options are:

Option 1: Use speed a in the first part, then speed b in the second part. The total height would be (a * t1) * (1 - k/100) + b * t2.

Option 2: Use speed b in the first part, then speed a in the second part. The total would be (b * t1) * (1 - k/100) + a * t2.

The participant will choose whichever of these two options gives a higher height.

So for each of the n participants, we need to compute the maximum between these two options. Then, we sort them first by descending height, and then by ascending participant number.

Now, the problem is to compute this for all participants and output them in the correct order.

Constraints: n can be up to 1000. So we need to process 1000 participants, which is manageable.

Now, let's think about the data structures. For each participant, we calculate their maximum height, then store along with their index. Then, we sort the list of tuples (height, original index) in descending order of height, and ascending order of index if heights are equal.

So the steps are:

1. Read n, t1, t2, k.

2. For each participant i (from 1 to n):

   a. Read a_i and b_i.

   b. Compute option1: (a_i * t1) * (1 - k/100) + b_i * t2.

   c. Compute option2: (b_i * t1) * (1 - k/100) + a_i * t2.

   d. Take the maximum of option1 and option2 as the participant's height.

3. Create a list of tuples containing (-height, original index, formatted_height) for each participant. Wait, no. We need to sort in descending order of height. So for sorting, we can have a list of tuples (height, original index) and then sort with a key that sorts primarily by -height, then by original index.

Wait, in Python, when you sort, you can use a key that is a tuple. For example, to sort in descending order of height and ascending order of index, the key can be (-height, index). Then, when sorted, the list will be ordered first by higher height, then by lower index.

Yes. So for each participant, compute their max height, then create a list of (max_height, index) where index is 1-based. Then sort the list using a key of (-max_height, index). Then, when sorted, the participants with higher max_height come first, and in case of ties, the one with the lower index comes first.

Once sorted, we need to output each participant's index and their max_height formatted to two decimal places.

But how to format the max_height with exactly two decimal digits. Also, the problem says the answer must be absolutely accurate, so we can't use floating-point approximations. Wait, but how to compute this correctly.

Wait, the formula for each option is (a * t1) * (1 - k/100) + b * t2. Let's see: since a and b are integers, t1 and t2 are integers, and k is an integer. So 1 - k/100 is (100 -k)/100. So the first term is a * t1 * (100 -k) / 100. The second term is b * t2. So the total is (a * t1 * (100 -k) / 100) + (b * t2). Similarly for the other option.

So all these are computed as exact values. However, when we output, we need to present two decimal digits, even if the number is, say, 15.00 (like in the first example). So the key is to compute the values precisely as floating points, but since all the terms are integers multiplied and divided by 100, perhaps the calculation can be done as exact fractions.

Wait, perhaps using integers. For example, let's compute each option as a numerator, then divide by 100. For example, a * t1 * (100 -k) is an integer, then divided by 100. So the first term is (a * t1 * (100 -k) + 100 * b * t2) / 100. Similarly for the other option. So for each option, the total can be represented as a fraction with denominator 100, which when divided out gives two decimal places.

Therefore, the maximum of the two options can be represented as a number with up to two decimal digits, and when formatted correctly, can be displayed with exactly two decimal digits, even if the trailing digits are zero.

But how to handle this in Python to avoid floating-point inaccuracies? Because if we compute using floating-point numbers, there might be precision errors. For example, 0.1 is not exactly representable in binary floating-point. However, in this problem, since all the terms can be represented exactly as multiples of 0.01, perhaps using integers to compute the total in hundredths (like cents) and then divide by 100 to get two decimal places would avoid errors.

Yes. For example, each option's value can be calculated as an integer multiplied by the necessary factors and divided by 100. So let's see:

For option1:

(a * t1) * (100 -k) + (b * t2 * 100) 

Then, divided by 100. Because (a * t1 * (100 -k) ) / 100 + (b * t2) = [a t1 (100 -k) + 100 b t2 ] / 100.

Similarly for option2.

So for each option, compute the numerator as a * t1 * (100 -k) + 100 * b * t2. Then the value is numerator / 100. Similarly for the other option.

But for option1 and option2, the numerators are integers, so when divided by 100, they can have up to two decimal digits. Thus, the maximum between the two options can be computed as the maximum of the two numerators, then divided by 100 to get the exact decimal value.

Wait, but this depends on the options. Let me clarify.

Option1's value is (a * t1 * (100 -k) + 100 * b * t2) / 100.

Option2's value is (b * t1 * (100 -k) + 100 * a * t2) / 100.

So the maximum of these two can be found by comparing their numerators. Because dividing by 100 is the same for both. So to find which is larger, compare (a * t1 * (100 -k) + 100 * b * t2) and (b * t1 * (100 -k) + 100 * a * t2). The larger numerator will correspond to the larger value.

So for each participant, we can compute both numerators and compare them, then take the maximum. Then, the maximum's numerator is divided by 100 to get the exact two decimal digits.

This approach avoids floating-point inaccuracies because all calculations are done with integers, and the division by 100 is exact when the numerator is an integer. So when we format the result as a float with two decimal places, it will be accurate.

Therefore, the steps are:

For each participant i (1-based index):

a. a and b are the two speeds.

b. Compute numerator1 = a * t1 * (100 - k) + 100 * b * t2.

   Compute numerator2 = b * t1 * (100 - k) + 100 * a * t2.

c. max_numerator = max(numerator1, numerator2).

d. The height is max_numerator / 100.0.

So the key is to compute these numerators as integers, then divide by 100.0 to get the height as a float with exactly two decimal digits.

This approach ensures that there's no floating-point error, since all operations are done with integers and division by 100 will give exactly two decimal digits.

For example, in the first sample input:

n=2, t1=3, t2=3, k=50.

Participant 1: a=2, b=4.

Option1: 2*3*50 (since 100-50=50) + 100*4*3 = 300 + 1200 = 1500 → 1500/100=15.00.

Option2:4*3*50 + 100*2*3= 600 + 600=1200 →12.00. So max is 15.00.

Participant 2: a=4, b=2.

Option1:4*3*50 + 100*2*3=600 + 600=1200 →12.00.

Option2:2*3*50 +100*4*3=300+1200=1500 →15.00. So max is 15.00.

So their heights are 15.00 and 15.00, but sorted by index, so 1 comes before 2.

Now, for the output, we need to print each participant's index and their height with exactly two decimal places.

In Python, formatting can be done using the format string "%.2f" to show two decimal digits. However, since the numbers are calculated precisely, perhaps using integer division and then formatting as two decimal places would work.

But when we compute max_numerator as an integer, dividing by 100.0 gives a float that can be represented exactly. For example, 1500 / 100.0 is 15.0, which when formatted as %.2f becomes 15.00. Similarly, 93703 (from the second example) would be 93703 / 100.0 = 937.03, which is correct.

So the plan is:

- For each participant, compute numerator1 and numerator2 as integers.

- Take the maximum of those two.

- The height is that maximum divided by 100.0.

Then, we can sort the participants based on their height (descending) and index (ascending).

Once sorted, output each participant's index and the height with two decimal digits.

Now, to implement this:

First, read n, t1, t2, k.

Then, for each of the next n lines, read a and b.

Compute the two numerators as integers.

Take the maximum.

Store the max_height (as a float: max_numerator / 100.0) along with the original index (i+1, since input starts from 1-based? Wait, the input lines are 1-based. Wait, in the input, each of the next n lines corresponds to participant number i (1 ≤ i ≤ n). So participant numbers are 1-based.

So for the first line, it's participant 1, then 2, etc.

So for each participant, the original index is i+1? No. Wait, the first line after the initial four is participant 1, second line is 2, etc. So when looping from 0 to n-1 (assuming zero-based loop), the participant number is the loop index +1.

So in code:

participants = []
for i in range(n):
    a, b = map(int, input().split())
    # compute numerators
    numerator1 = a * t1 * (100 - k) + b * t2 * 100
    numerator2 = b * t1 * (100 - k) + a * t2 * 100
    max_num = max(numerator1, numerator2)
    height = max_num / 100.0
    participants.append( (-height, i+1, max_num) )

Wait, but why store max_num? Because when dividing by 100, perhaps using the integer to avoid floating points. Wait, but in the code, perhaps we can compute height as a float, but when formatted, since the max_num is an integer, it's exactly divisible by 100, so the result has exactly two decimal digits.

But when stored as a float, it's possible that due to floating point precision, the value may not be exact. For example, 0.1 can't be represented exactly. However, in this problem, since max_num is an integer and divided by 100.0, all possible values will be of the form x.xx, where x are two decimal digits. So dividing an integer by 100.0 will result in a float that represents exactly two decimal digits, right?

Wait, for example, 1500 divided by 100 is 15.0, which is exactly representable. 93703 divided by 100 is 937.03, which is 93703 / 100 = 937.03. But can 93703 be stored exactly as a float? Well, 93703 is 93703.0, and divided by 100 gives 937.03. The float can represent this exactly?

Wait, let's see: 93703 is an integer. Divided by 100, 937.03. But 0.03 is 3/100. So 937.03 is 93703 * 1e-2. So as a binary fraction, 0.03 is 3/100 = 0.00001111010111000010100011110101110000101000111101... repeating. So when stored as a float, this would have a repeating decimal and thus be an approximation. Wait, but 93703 is 93703, which can be stored as an integer. Then, when divided by 100, it's 937.03. However, in Python, when you do 93703 / 100.0, the result may not be exact. Wait, but 93703 is an integer, so 93703 / 100 is 937.03, but in binary, 0.03 can't be represented exactly. Wait, but how to avoid this?

Ah, but maybe the problem statement allows us to use the exact decimal representation, and when the problem says that the answer must be considered correct if it is absolutely accurate, perhaps the calculation using integers and then formatted with two decimal places is correct. Because when the max_numerator is stored as an integer, dividing by 100.0 will give a float that, when formatted to two decimal places, will show the correct digits. For example, 93703 / 100 is 937.03. When stored as a float, the actual value might be 937.0299999999... or something, but when we format to two decimal places, it would round to 937.03. Wait, but in Python, when you format a float with two decimal places, it uses the rounding rules. So for example, 937.029999999999 would be rounded to 937.03 if the third decimal is 9 (as in 937.0299999 is closer to 937.03 than 937.02). But this could be a problem.

Wait, but how to avoid this? Because the problem says that the answer must be absolutely accurate, so perhaps the correct approach is to avoid floating points altogether and instead store the value as a string formatted correctly. But how?

Alternatively, perhaps the problem expects us to calculate the value as a decimal with two digits, which can be done by using integer arithmetic and then formatting with two decimal places.

So for example, when max_num is 93703 (as in the second example's first participant), then 93703 / 100 is 937.03. So when stored as a string, this is exactly "937.03".

But in Python, if we compute 93703 / 100.0, it would be 937.03, but due to floating point precision, maybe not exactly. So how to handle this?

Wait, perhaps when we compute the integer max_num, then we can format it as a string by dividing into integer and decimal parts. For example, the max_num is an integer. Then, the integer part is max_num // 100, and the decimal part is max_num % 100. Then, the string can be formed as f"{integer_part}.{decimal_part:02d}".

Yes! That way, we avoid any floating-point errors. For example, max_num = 1500 → 15.00, max_num=93703 →937.03, max_num=37999 →379.99.

So this approach would ensure that the decimal is exactly two digits, even if the division by 100.0 would give a float that's not exactly representable.

Therefore, the correct way to format is to split the integer into integer and decimal parts and format as a string with two decimal digits. So in Python, for each max_num, the formatted string would be "{}.{:02d}".format(max_num // 100, max_num % 100). But wait, if max_num is 93703, then 93703 // 100 is 937, 93703 % 100 is 3. So 937.03. But in that case, the code would output 3 as 03, which is correct. Similarly, 37999 → 379.99.

So this approach would avoid any floating-point issues.

So the steps in code:

For each participant, compute max_num (the maximum of numerator1 and numerator2).

Then, when storing the data, store the max_num as an integer. Then, when outputting, format it as (max_num // 100).(max_num % 100), ensuring that the decimal part is two digits with leading zero if needed.

So, the code can collect the max_num as integers, then during sorting, compare the max_num (since higher max_num implies higher height) and the original index.

So the list of participants can be stored as tuples (-max_num, index), so that when sorted in ascending order (because of the negative), the first elements are the largest max_num and the smallest index.

Wait, but the sorting key should be:

- primary key: max_num (descending order). To sort in descending order, using the negative in the key. So for the tuple, the first element is -max_num. Then, when sorted in ascending order, the largest max_num comes first.

- secondary key: index (ascending order). So the tuple would be (-max_num, index).

Then, when sorted, the participants are ordered by max_num descending, then index ascending.

So the code steps:

Read n, t1, t2, k.

Then, read each of the n participants:

For each i in 0..n-1:

   read a and b.

   compute numerator1 = a * t1 * (100 -k) + b * t2 * 100.

   numerator2 = b * t1 * (100 -k) + a * t2 * 100.

   max_num = max(numerator1, numerator2).

   append (-max_num, i+1, max_num) to the list.

Sort the list.

Then, for each entry in the sorted list:

   index is the second element (i+1), max_num is the third element.

   integer_part = max_num // 100.

   decimal_part = max_num % 100.

   formatted_str = f"{integer_part}.{decimal_part:02d}"

   print(f"{index} {formatted_str}")

Wait, but for example, if max_num is 15, then 15 // 100 is 0, and 15 % 100 is 15 → 0.15. That can't be right. Wait, no. Wait, for max_num = a * t1 * (100 -k) + 100 * b * t2.

Wait, let's take the first example:

max_num for participant 1 is 1500. 1500 // 100 is 15. 1500 % 100 is 0 → 15.00. Which is correct.

Another example, in the second sample input:

Participant 4: a=693, b=970.

Compute the two options:

option1: 693 *1 *99 (since 100 -1 =99) + 970 *1 *100 → 693*99 = 68607 + 97000 = 165607. So 165607 /100 = 1656.07.

So max_num is 165607 → formatted as 1656.07.

So yes, this method works.

So the code should collect max_num as an integer and then format as described.

So this approach is safe and avoids any floating point inaccuracies.

Now, let's code this.

First, read the input:

n, t1, t2, k = map(int, input().split())

Then, for each participant:

participants = []
for i in range(n):
    a, b = map(int, input().split())
    # compute the two options
    num1 = a * t1 * (100 - k) + b * t2 * 100
    num2 = b * t1 * (100 - k) + a * t2 * 100
    max_num = max(num1, num2)
    # store as (-max_num, index, max_num) for sorting
    participants.append( ( -max_num, i+1, max_num ) )

Then, sort the participants:

participants.sort()

Once sorted, loop through each and output:

for p in participants:
    max_num = p[2]
    index = p[1]
    integer_part = max_num // 100
    decimal_part = max_num % 100
    print(f"{index} {integer_part}.{decimal_part:02d}")

Yes, that should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, t1, t2, k = map(int, input_stream.readline().rstrip("\n").split())
    participants = []
    for i in range(n):
        a, b = map(int, input_stream.readline().rstrip("\n").split())
        num1 = a * t1 * (100 - k) + b * t2 * 100
        num2 = b * t1 * (100 - k) + a * t2 * 100
        max_num = max(num1, num2)
        participants.append((-max_num, i + 1, max_num))
    participants.sort()
    for p in participants:
        index = p[1]
        total = p[2]
        integer = total // 100
        decimal_part = total % 100
        print(f"{index} {integer}.{decimal_part:02d}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 1 1 1
544 397
280 101
280 101
693 970
""",
            "output": \
"""\
4 1656.07
1 937.03
2 379.99
3 379.99
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

Another test case: the second sample input:

4 1 1 1

544 397 → participant 1.

Compute num1: 544 *1*(99) + 397 *1 *100.

544 *99 = 544 *100 -544 = 54400-544=53856. 397 *100=39700. Sum 53856+39700=93556. So num1 is 93556 →935.56.

num2:397*1*99 +544 *1*100 → 397*99=39303 +54400=93703. So num2 is 93703 →937.03. So max_num is 93703.

So participant 1's entry is (-93703, 1, 93703).

Participant 2:

a=280, b=101.

num1:280 *1*99 +101 *1*100 →280*99=27720 + 10100=37820 →37820 →378.20.

num2:101 *99 +280 *100 →9999 +28000=37999 →379.99. So max_num is 37999.

Participant 3's a=280, b=101 (same as participant 2?), so same calculation. So max_num is 37999.

Participant4: a=693, b=970.

num1=693*1*99 +970 *1*100 →693*99= 68607 +97000= 165607 →1656.07.

num2=970*99 +693*100 → 96030 +69300=165330. So max_num is 165607.

So the participants are stored as:

participant 4: (-165607, 4, 165607)

participant1: (-93703, 1, 93703)

participant2: (-37999, 2, 37999)

participant3: (-37999, 3, 37999)

When sorted, the order is:

participant4's tuple is (-165607,4, ...) → the smallest first element (since it's -165607) comes first.

Then, the next is participant1 (-93703,1), then participant2 (-37999,2), then participant3 (-37999,3). So when sorted, the order is:

participant4, participant1, participant2, participant3.

So output:

4 1656.07

1 937.03

2 379.99

3 379.99

Which matches the sample.

So the code works.

Now, let's code this.

The code reads the inputs, computes the two options as integers, takes the max, then sorts with the key (-max_num, index), then outputs as described.
</think>

```python
n, t1, t2, k = map(int, input().split())
participants = []
for i in range(n):
    a, b = map(int, input().split())
    num1 = a * t1 * (100 - k) + b * t2 * 100
    num2 = b * t1 * (100 - k) + a * t2 * 100
    max_num = max(num1, num2)
    participants.append((-max_num, i + 1, max_num))
participants.sort()
for p in participants:
    index = p[1]
    total = p[2]
    integer = total // 100
    decimal_part = total % 100
    print(f"{index} {integer}.{decimal_part:02d}")
```
