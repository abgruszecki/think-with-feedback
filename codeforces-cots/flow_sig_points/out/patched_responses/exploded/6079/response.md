<think>
Okay, let's try to solve this problem. So the problem is about Dima not wanting to be the one who has to clean. The way the selection works is based on the total number of fingers shown by everyone, including Dima. The total determines how many people they count, starting with Dima. The person they land on has to clean. So Dima wants to choose a number of fingers (from 1 to 5) such that when you sum all the fingers (his plus friends') and then count that sum in a circle starting from him, the last person counted is not him. We need to find out how many such choices he has.

Let me break this down. The key is to figure out for each possible choice of Dima's fingers (1-5), whether the total sum leads to him not being the one selected. Then count how many such choices there are.

First, the steps:

1. Calculate the sum of friends' fingers. Let's call this sum_friends.
2. For each possible Dima's fingers d (1 to 5), calculate total = sum_friends + d.
3. The total determines how many people are counted. Since there are n friends plus Dima, total people is (n+1). So when counting total steps, we start at Dima (position 0?), and then count each step. But since it's a circle, we can model this as (total) modulo (n+1) to find the position where it stops.

Wait, but how exactly does the counting work? Let's take the first example:

Sample Input 1:
1
1

So n is 1 friend. Friends' sum is 1. Dima's possible choices are 1,2,3,4,5. So total can be 2,3,4,5,6.

The sample output is 3, meaning that for 3 of these choices, Dima doesn't end up selected.

Let's see the first example. The friends plus Dima are two people (n+1 = 2). The sum is friends_sum + d.

For example, in the note, when Dima shows 3 fingers, sum is 1+3=4. The count is 4 steps. The positions are:

Start at Dima (position 0). Then each count steps. So step 1 is Dima (count 1), step 2 is friend (count 2), step 3 is Dima again (count 3), step4 is friend (count4). Wait, but the total is 4, so the last person is friend. So Dima is safe. So in that case, when sum is 4, the selected person is (sum mod (n+1)) ?

Wait, the count is total steps. Let's see. For sum S, the steps are S people counted, starting from Dima. Since the people are arranged in a circle, the position where the count ends is (Dima's position + S - 1) mod (n+1), perhaps?

Wait, let's think of the first example: sum is 7. Then n+1 is 2 (Dima and one friend). So 7 mod 2 is 1. Because when you count 7 steps, starting with Dima (step 1), then friend (step2), Dima (step3), friend (step4), Dima (step5), friend (step6), Dima (step7). So the 7th step is Dima. So that's why in the note, when sum is 7, Dima has to clean. Because 7 mod 2 is 1. Wait, 7 divided by 2 is 3 with remainder 1. So the position is (0 + 7) mod 2 = 1 mod 2 is 1. But positions are 0 (Dima) and 1 (friend). So if the mod result is 1, then the friend is selected. Wait, maybe the formula is (sum) mod (n+1). If the remainder is 0, then the last person is the (n+1)th, which is Dima. Wait, maybe the correct formula is:

The selected position is (sum - 1) mod (n+1). Let's see.

In the first sample's note where sum is 7, (7-1) mod 2 =6 mod2=0. So 0 corresponds to Dima, so he is selected. Which matches the note.

Another example from the first sample's note: sum is 8. (8-1) mod2=7 mod2=1. So friend is selected. So Dima's choice of 3 gives sum 4: (4-1) mod2=3 mod2=1. So friend is selected. So in that case, Dima's choice of 3 is valid (counted in the answer). So the answer counts how many Dima's choices lead to (sum-1) mod (n+1) not equal to 0.

So the formula is: the position is (sum - 1) mod (n+1). If that position is 0 (Dima's position), then he is selected and we don't count that choice. Otherwise, we do.

So the approach is:

1. Compute sum_friends from the input.
2. For each d in 1..5:
   a. total = sum_friends + d
   b. mod = (total - 1) % (n+1)
   c. if mod != 0, then this d is a valid choice (since the selected person is not Dima)
3. Count the number of such d's.

So the problem reduces to checking for each possible d (from 1 to 5) whether (sum_friends + d -1) mod (n+1) is not zero.

Let me test this with the first sample input:

Sample Input 1:
1
1

sum_friends =1, n+1=2.

d can be 1,2,3,4,5.

For d=1: total=2. (2-1) mod2 =1 mod2=1 !=0 → valid.
d=2: total=3. (3-1)=2 mod2=0 → invalid.
d=3: total=4 → 3 mod2=1 → valid.
d=4: total=5 →4 mod2=0 → invalid.
d=5: total=6 →5 mod2=1 → valid.

So valid d's are 1,3,5 → 3 options. Which matches the sample output.

Another sample input:
1
2 → sum_friends=2, n+1=2.

Check each d from 1-5:

d=1: total=3. 3-1=2 mod2=0 → invalid.
d=2: total=4 →3 mod2=1 → valid.
d=3: total=5 →4 mod2=0 → invalid.
d=4: total=6 →5 mod2=1 → valid.
d=5: total=7 →6 mod2=0 → invalid.

So valid d's are 2 and4 → output 2, which matches the second sample.

Third sample input:

n=2, friends 3 and5 → sum_friends=8. n+1=3.

Check each d (1-5):

d=1: total=9. (9-1)=8 mod3=8 mod3=2 → not zero → valid.
d=2: 10 →9 mod3=0 → invalid.
d=3: 11 →10 mod3=1 → valid.
d=4:12 →11 mod3=2 → valid.
d=5:13 →12 mod3=0 → invalid.

So valid d's are 1,3,4 → 3 options. Which matches the third sample.

So this approach works.

Now, the code steps:

Read n.

Read the list of friends' fingers. Sum them to get sum_friends.

Compute (n+1) as the number of people.

For each d in 1-5:

total = sum_friends +d

mod_val = (total -1) % (n+1)

if mod_val !=0 → count +=1

return count.

So the code is straightforward.

Now, implement this in Python.

Edge Cases:

What if sum_friends +d is 0? But sum_friends is at least n (since each friend's fingers are at least 1). So n >=1, sum_friends >=1. So sum_friends +d is at least 2. So (total-1) is at least 1, so mod_val can't be negative.

Another edge case: n=0? But according to the problem statement, n is the number of Dima's friends. The constraints say n ≥1. Wait, no. Wait the first line says "1 ≤ n ≤ 100".

Wait the problem statement says: the first line contains integer n (1 ≤ n ≤ 100). So n can't be zero. So the code doesn't need to handle n=0.

So code:

Read n.

sum_friends = sum of the list of integers in the second line.

count =0

for d in 1,2,3,4,5:

    total = sum_friends +d

    mod = (total -1) % (n+1)

    if mod !=0:

        count +=1

print(count)

Yes.

Now, code:

Read n.

Then read the next line as a list of integers, sum them.

Then loop d from 1 to 5.

So the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    friends = list(map(int, input_stream.readline().rstrip("\n").split()))
    sum_friends = sum(friends)
    total_people = n +1
    count =0
    for d in range(1,6):
        total = sum_friends +d
        mod_val = (total -1) % total_people
        if mod_val !=0:
            count +=1
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
2
""",
            "output": \
"""\
2
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

Yes.

So this code should work.

Another sample input:

Input 2:

1

2

sum_friends=2, total_people=2.

d=1: total 3 →2 mod2=0 → no.

d=2:4 →3 mod2=1 → yes.

d=3:5 →4 mod2=0 → no.

d=4:6 →5 mod2=1 → yes.

d=5:7 →6 mod2=0 → no.

So count is 2, correct.

Third sample:

n=2, friends 3 and5 → sum 8. total_people=3.

d=1: total 9 →8 mod3= 8%3=2 → yes.

d=2:10 →9 mod3=0 → no.

d=3:11 →10 mod3=1 → yes.

d=4:12 →11 mod3=2 → yes.

d=5:13 →12 mod3=0 → no.

So count is 3, correct.

Looks like the code works.

Now, in terms of optimization, this code is O(1), since it's looping 5 times. So even for n up to 100, no problem.

So the code is correct.
</think>

```python
n = int(input())
friends_sum = sum(map(int, input().split()))
people = n + 1
count = 0
for d in range(1, 6):
    total = friends_sum + d
    if (total - 1) % people != 0:
        count += 1
print(count)
```
