<think>
Okay, let's tackle this problem. Hmm. The problem is about forming teams of exactly three people from groups of students. Some groups have 1 student, others have 2. The key thing is that groups of two must be kept together. So, if a group of two is used, both students must be in the same team. And each team can only be of three people. So we need to find the maximum number of such teams possible.

Let me start by thinking about the possible combinations. Let's see. A team can be formed in a few ways:

1. Three single groups (1+1+1). That's one team.
2. One group of two and one single group (2+1). Because 2+1 =3.

Wait, wait. Wait, no. Because a group of two plus a single is 3. So that's a possible team. So for each group of two, we can pair them with a single. But how do these combinations affect the overall count?

So the approach here is to count how many groups of 1 and 2 there are, and then find the optimal way to combine them into teams of three.

Let me denote the count of groups of 1 as 'ones' and groups of 2 as 'twos'.

The possible team compositions are:

- All three members from single groups: each team uses three ones. So the number of such teams is ones // 3.
- Or, a two and a one: each such team uses one two and one one. Because the two contributes two people and the one contributes one, total three.

But we can't have a mix of these two in a way that uses the resources optimally. So the problem is to find the right balance between using ones in triplets and in pairs with twos.

Wait, but also, perhaps combining some twos with ones. For example, if we have a lot of twos and some ones. Let's see.

The maximum number of teams would be the sum of:

- The number of teams formed by combining a two and a one. Let's call this possible_teams_1 = min(twos, ones) (but wait, each team here uses one two and one one, so if there are T twos and O ones, the maximum possible teams via this is min(T, O) // 1? Wait, no. Because each such team requires 1 two and 1 one. So for each two, you can pair it with a one. But each team here uses 1 two and 1 one. So the number of such teams is the minimum of the number of twos and the number of ones available. Wait, no. Because each team is one two and one one. So if there are 3 twos and 5 ones, then we can form 3 teams, using 3 twos and 3 ones. Then the remaining ones could form teams of three. So in this case, 3 teams from 2+1, and then (5-3) //3 = 0. So total 3.

Alternatively, if there are 4 twos and 4 ones. Then possible_teams_1 would be 4 (using 4 twos and 4 ones). But then, the remaining 0 ones and 0 twos. So total 4 teams.

But what if the ones and twos are in different proportions?

So the problem is to find the optimal way to combine the two possibilities.

But how?

Let me think of the variables:

Let ones be the count of single-person groups.

Let twos be the count of two-person groups.

We can form teams in two ways:

1. (twos, ones) → each team uses 1 two and 1 one. So each such team uses 1 two and 1 one. The number of such teams possible is min(twos, ones). But wait, no. Because each team requires one two and one one, so the maximum possible here is the minimum of the two. For example, if there are 5 twos and 3 ones, then we can form 3 teams (using 3 twos and 3 ones). The remaining 2 twos can't form any teams (since each requires a one).

Alternatively, perhaps not. Because maybe combining the remaining ones in other ways is better.

Wait, but the other way is to use three ones per team. So, for example, if we have:

twos = 3, ones =5.

If we form 3 teams of 2+1, that uses 3 twos and 3 ones. Then the remaining 2 ones can form 0 teams. So total 3.

Alternatively, if we form 1 team of 2+1 (using 1 two and 1 one), then we have 4 ones left. Then 4 //3 =1. So total teams would be 1 +1=2. Which is worse.

So in this case, using all possible 2+1 teams is better.

Hmm, but maybe there's a case where using some 2+1 teams and some 1+1+1 teams gives a better total.

So the problem is to find the optimal split between these two types of teams.

Let me think of possible scenarios.

Case 1: There are enough ones to pair with all twos.

In this case, the maximum number of teams would be the number of twos plus (ones - twos) //3. For example, if twos=3, ones=5. Then 3 teams (2+1), then 5-3=2 → 0, total 3. But if twos=3, ones=6. Then 3+ (6-3)/3= 3+1=4.

But wait, wait. Let's see: twos=3, ones=6.

If we make 3 teams of 2+1, that uses 3 ones. The remaining 3 ones can form 1 team. So total 4. Which is correct.

But another approach: what if we take 2 teams of 2+1 (using 2 twos and 2 ones), then have 1 two left and 4 ones. Then, the remaining two can pair with one of the 4 ones, making another team, and then 3 ones left. So total 3+1=4. Same result.

So in this case, the optimal is to pair as many twos as possible with ones, then use the remaining ones for triplets.

But what if the ones are not enough to pair all twos, but combining some with triplets gives a better result?

For example: twos=5, ones=3.

If we pair 3 ones with 3 twos, forming 3 teams. Then, remaining 2 twos. But they can't form any teams. So total 3.

Alternatively, maybe use 1 two and 1 one (so 1 team), then the remaining 2 ones and 4 twos. Then, the 2 ones can form 0 triplets, and the 4 twos can't form anything. So total 1. Which is worse.

So the initial approach of using as many 2+1 teams as possible (i.e., min(twos, ones)) and then the remaining ones in triplets is better.

Another example: twos=4, ones=5.

If we pair all 4 twos with 4 ones: forming 4 teams. Then ones left=1. So no more teams. Total 4.

Alternatively, pairing 3 twos with 3 ones: 3 teams. Then, ones left=2. Can't form a triplet. So total 3. So worse than 4.

So again, pairing as many as possible is better.

But wait, what if there are some cases where reducing the number of 2+1 teams allows for more overall teams?

Let me think of another example: twos=2, ones=4.

Option 1: pair 2 twos with 2 ones → 2 teams. Then, remaining 2 ones → no teams. Total 2.

Alternatively, use 1 team of 2+1 (using 1 two and 1 one). Then, remaining 1 two and 3 ones. The 3 ones form one team. So total 2. So same result.

But what if ones are 5, twos=2.

Option 1: pair 2 twos with 2 ones → 2 teams. Remaining 3 ones → 1 team. Total 3.

Which is better.

So the initial approach is to pair as many twos as possible with ones, then form triplets from remaining ones. So the formula would be:

teams = min(twos, ones) + (remaining ones after using min(twos, ones)) //3.

Wait, no. Wait, after pairing as many as possible, the remaining ones would be ones_remaining = ones - min(twos, ones).

But if twos >= ones, then min is ones. So the remaining twos are twos - ones. But twos are groups of two, which can't form a team by themselves. So the remaining twos can't contribute to any teams.

So the formula is:

teams = min(twos, ones) + (max(ones - twos, 0)) // 3.

Wait, but let's see.

If ones >= twos, then:

- The number of 2+1 teams is twos.

- Then, the remaining ones are (ones - twos).

- Then, add (ones - twos) //3.

So total is twos + (ones - twos) //3.

If ones < twos:

- The number of 2+1 teams is ones.

- Then, the remaining twos is (twos - ones). These can't form any teams, since each requires a single.

- The remaining ones are zero.

So total is ones.

But wait, maybe there's a case where some of the remaining twos can be combined with the triplets? No, because the triplet is three singles. The groups of two can't contribute to that. Because each group of two must be used as a whole or not at all.

So the formula would be the sum of the two possible team types.

But wait, maybe there's another approach. Let me think of the third example:

Input 3:

7

2 2 2 1 1 1 1 → twos=3, ones=4.

The optimal solution is 3 teams. How?

Each team is a two and a one. But 3 twos, and 4 ones. So 3 teams. So ones left is 1. So 3+0=3.

But according to the formula:

teams = min(3,4)=3 + (4-3)/3= 0.333... → 0. So total 3. Which matches the example.

Another example in input 4: 3 ones → teams is 3//3=1. Correct.

So the formula seems to work.

But wait, what about the case where there are some twos left and some ones. Could we have a better combination?

Another example: twos=1, ones=5.

Using the formula:

min(1,5)=1 → 1 team (2+1). Remaining ones 4. 4//3=1. Total 2.

Which is correct. 1+1=2.

Yes.

But what if there are twos=2, ones=4.

The formula gives 2 + (4-2)/3= 2 + 0=2. Which is correct. But another way is 2 teams of 2+1, then two ones left. So total 2.

But if we take one team of 2+1 and then three ones, that's 1 +1=2. Same result.

So the formula works.

Another example: twos=5, ones=5.

Formula: min(5,5)=5 → 5. Then (5-5)/3=0. Total 5.

Which is 5 teams of 2+1. Each uses 1 two and 1 one. So total 5*3=15 people.

But 5 teams *3=15 people. Which is correct.

But wait, each team uses one two (2 people) and one one (1), so yes.

So the formula seems correct.

But wait, what about when the ones are in excess but not enough to cover all twos. Then, we pair all possible, but no more.

Another case: twos=3, ones=7.

Formula: 3 teams of 2+1 (using 3 ones). Then 7-3=4 → 4//3=1. So total 3+1=4.

Which is correct. The four teams would use 3*2 +3*1 +3*1 = 3*3 (from the first 3 teams) + 3 (from the triplet) → total 12 people. Which is 4*3=12. Correct.

So the formula works.

So the approach is:

- Count the number of ones and twos.

- The maximum number of teams is the minimum of ones and twos (number of 2+1 teams) plus the remaining ones after that (divided by 3 for 1+1+1 teams).

But wait, no. Because the remaining ones after using min(twos, ones) is (ones - min(twos, ones)), but only if ones >= twos. Otherwise, the remaining ones is zero.

Wait, for example:

If ones >= twos:

remaining_ones = ones - twos.

teams = twos + (remaining_ones //3).

If ones < twos:

remaining_ones = 0.

teams = ones + 0.

So the formula can be written as:

teams = min(twos, ones) + ((max(ones - twos, 0)) //3).

Yes.

So this should be the correct approach.

But wait, let's check the sample input 3:

Sample Input 3:

7

2 2 2 1 1 1 1 → twos=3, ones=4.

According to formula: min(3,4)=3. Remaining_ones=4-3=1. 1//3=0. So total 3, which matches the sample.

Sample Input 1:

4

1 1 2 1 → ones=3, twos=1.

min(1,3)=1 → remaining_ones=2. 2//3=0. Total 1. Correct.

Sample Input 2:

2

2 2 → ones=0, twos=2. So min(0,2)=0. remaining_ones=0. Total 0. Correct.

Sample Input 4:

3

1 1 1 → ones=3, twos=0. min(0,3)=0. remaining_ones=3. 3//3=1. Total 1. Correct.

Another test case: twos=4, ones=5.

min(4,5)=4. Remaining_ones=1. 1//3=0. Total 4.

But wait, 4 teams of 2+1 (using 4 twos and 4 ones), leaves 1 one. So 4 teams, correct.

Another test case: twos=2, ones=5.

min(2,5)=2. Remaining_ones=3 → 3//3=1. Total 3 teams.

Yes. 2+1 + 1 → total 3.

So the formula works.

But wait, what if the remaining ones after pairing can be combined with some of the twos that weren't used, but that's only possible if ones < twos.

Wait, no. If ones < twos, then we can only pair 'ones' number of 2+1 teams, leaving (twos - ones) twos unused.

But in that case, those remaining twos can't form any teams, because each requires a single.

But perhaps there's a case where using some of the twos and some of the ones in a different way would give a better result.

Wait, for example:

twos=3, ones=3.

Using all 3 twos and 3 ones in 3 teams of 2+1 → total 3.

But if we use 2 teams of 2+1 (using 2 twos and 2 ones), then we have 1 two left and 1 one. Then, the remaining one can't form a team. Or, perhaps, the remaining two groups: 1 two and 1 one. But that can form a team. Wait, that's 2+1=3, which is valid. So total 3 teams. Which is same as the initial approach.

Wait, but according to the formula, it's min(3,3)=3, so 3 teams. Which is correct.

So no problem.

Another example: twos=2, ones=4.

The formula gives 2 + (4-2)/3= 2 + 0.666 → 2. So total 2.

Which is correct. Because two teams of 2+1, using 2 twos and 2 ones. Then 2 ones left, which can't form a team.

Alternatively, make one team of 2+1 (using 1 two and 1 one), leaving 1 two and 3 ones. Then form a team of 3 ones. So total 2 teams. Same as the formula.

So the formula works.

So the approach is to compute the number of 2+1 teams as the minimum of twos and ones, then the remaining ones (if any) divided by 3. Sum those two for the total.

So the code would be:

Read n.

Then read the list a.

Count the number of ones and twos.

Calculate:

twos = count of 2 in the list.

ones = count of 1 in the list.

teams = min(twos, ones) + (max(ones - twos, 0) // 3)

Print teams.

Wait, but no. Wait, the code needs to compute:

teams = min(twos, ones) → this is the number of 2+1 teams.

Then, after that, the remaining ones are ones_remaining = ones - min(twos, ones) → which is (ones - twos) if ones >= twos, else 0.

So teams += ones_remaining //3.

Which is the same as:

teams = min(twos, ones) + (max(ones - twos, 0) //3)

Yes.

So that's the code.

Let me test this against all the examples.

First example:

Input 4:

4

1 1 2 1 → ones=3, twos=1.

min(1,3)=1 → 1. remaining_ones=3-1=2. 2//3=0 → total 1. Correct.

Second example:

2

2 2 → ones=0, twos=2.

min(0,2)=0. remaining_ones=0. total 0.

Third example:

7

2 2 2 1 1 1 1 → twos=3, ones=4.

min(3,4)=3. remaining_ones=1. 1//3=0. total 3. Correct.

Fourth example:

3

1 1 1 → ones=3, twos=0.

min(0,3)=0. remaining_ones=3. 3//3=1. total 1. Correct.

Another example where ones are 5 and twos 2:

twos=2, ones=5.

min(2,5)=2. remaining_ones=3 → 3//3=1. total 3.

Which is correct.

So the code works.

But wait, there is a case where we could form more teams by using fewer 2+1 teams and more 1+1+1 teams.

For example:

twos=2, ones=4.

The formula gives 2 + (4-2)/3 = 2 + 0 = 2.

But the optimal is 2.

Alternatively, if we use one 2+1 team and one 1+1+1 team: total 2.

Same as formula.

But suppose twos=3, ones=5.

Formula gives 3 + (5-3)/3 → 3 + 0 =3. But what if there's a way to make more teams.

Wait, 3 twos and 5 ones:

3 teams of 2+1: uses 3 twos, 3 ones. Remaining 2 ones. No more teams.

Total 3.

Alternatively, using 2 twos and 2 ones (2 teams), then remaining 1 two and 3 ones. Then, 1 two and 1 one: another team. Then remaining 2 ones. So total 3 teams. Same as formula.

So no gain.

Another example: twos=1, ones=4.

Formula: 1 + (4-1)/3= 1 +1=2. So total 2 teams. Which is correct. 1 team of 2+1 and 1 team of 1+1+1.

Yes.

So the code is correct.

Thus, the code is straightforward: count the number of ones and twos, compute the formula, output the result.

Now, the code in Python.

The input is:

First line: n.

Second line: n integers a_1 ... a_n.

We need to count the number of 1s and 2s.

In Python, this can be done with a list's count method.

For example:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    ones = a.count(1)

    twos = a.count(2)

    teams = min(twos, ones) + (max(ones - twos, 0) //3)

    print(teams, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
2 2
""",
            "output": \
"""\
0
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    ones = a.count(1)

    twos = a.count(2)

    teams = min(twos, ones) + (max(ones - twos, 0) //3)

    print(teams, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 1 1
""",
            "output": \
"""\
1
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    ones = a.count(1)

    twos = a.count(2)

    teams = min(twos, ones) + (max(ones - twos, 0) //3)

    print(teams, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
2 2 2 1 1 1 1
""",
            "output": \
"""\
3
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

Sample4:

3

1 1 1 → ones=3, twos=0. min(0,3)=0. (3-0=3 → 3//3=1). total 1.

All correct.

Another test case: twos=2, ones=5.

min(2,5)=2. 5-2=3 →3//3=1. total 3.

Yes.

Another example: twos=1, ones=5.

teams=1+ (5-1)/3=1 +4//3=1+1=2.

Which is correct.

Thus, the code works.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
ones = a.count(1)
twos = a.count(2)
teams = min(ones, twos) + max(0, (ones - twos)) // 3
print(teams)
```
