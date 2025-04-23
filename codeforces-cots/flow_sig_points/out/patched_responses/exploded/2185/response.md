<think>
Okay, let's try to figure out this problem. So the problem is about me and my friend collecting prizes along a line. We need to split the prizes between us such that the total time taken is minimized. The time taken is the maximum of the times each of us takes, right? Because we can do things in parallel.

Hmm. Let's think about the setup. I start at position 1, my friend at 1e6. All prizes are between 2 and 999,999. Each prize's position is unique and given in ascending order. We have to assign each prize to either me or the friend. Then, for each of us, the time we take is the time to collect all the prizes assigned to us in some optimal path.

Wait, but how do we calculate the time each person takes? For example, if I have a set of prizes, what's the minimal path to collect them? Oh right, because the optimal path for me would be to collect them in order from left to right (since I start at 1), so the furthest prize to the right that I collect is my maximum distance. Similarly for my friend, since he starts at 1e6, he should collect prizes in descending order, so the leftmost prize he collects determines his time (since he has to walk from 1e6 to that position). Wait, no. Wait, for me: starting at 1, the time it takes to collect all my prizes is (max position of my prizes) - 1. Because I can collect them in order from left to right. So if I collect a prize at position 5, then one at 3, then one at 7, the maximum is 7, so the time is 7-1 =6 seconds. Because moving from 1 to 3, then 3 to5, then5 to7. Total steps: 2+2+2=6. Which is 7-1=6. Oh right, because the maximum position is 7. So regardless of the order, the time for me is the maximum of (ai -1), where ai are the prizes I take. Similarly for the friend, his time is (1e6 - min_aj), where aj are the prizes he takes. Because he starts at 1e6 and can collect all his prizes by going to the leftmost one, which would take (1e6 - min_aj) steps.

Wait, because the friend is at 1e6, and all his prizes are to the left of that. So the minimal path would be to go to the leftmost prize first, then collect others as he moves right. But wait, no. Suppose the friend has prizes at positions 999,995 and 999,997. He can go from 1e6 to 999,995 (which is 5 steps), then to 999,997 (2 steps). Total 5+2=7 steps. But his maximum (1e6 - min_aj) is 5. So how does that compute? Because 999,995 is the leftmost, so 1e6 - 999,995 =5. But the actual steps he takes are 5+2=7. Hmm, that's a problem. So my initial thought was wrong. So my approach to compute each person's time as the maximum of (ai-1) for me and (1e6 - aj) for the friend is incorrect.

Wait, that's a big issue here. So the previous reasoning that the time taken is (max ai -1) for me and (1e6 - min aj) for the friend is not correct. Because when you have to collect multiple prizes, you have to move through them in some order, and the time depends on the path taken.

So how do we model the time taken for each person's path?

Ah, right! For a person, the minimal time to collect a set of prizes is the time required to traverse the path that covers all those prizes. For example, for me starting at 1, the minimal time is the time to walk from 1 to the rightmost prize, passing through all the prizes assigned to me. Similarly, for the friend starting at 1e6, the minimal time is to walk to the leftmost prize assigned to him, passing through all his prizes. Because when you arrange the prizes in a sorted order, the optimal path is to go from left to right (for me) or right to left (for the friend), but the total time is determined by the distance between the start and the furthest point. Wait, no. Let's think again.

For me: Suppose I have prizes at positions a1, a2, a3, ..., am, sorted in increasing order. My path would be 1 → a1 → a2 → ... → am. The time taken would be (a1 - 1) + (a2 - a1) + ... + (am - a_{m-1}) ) = am -1. So the total time is indeed am -1. So regardless of the order, if the prizes are sorted, the time is the maximum position minus 1. So my initial reasoning was correct. Because when you collect the prizes in order, you just add up the steps, which sum to the rightmost prize minus the start position (1). So for me, the time is (my_max_pos - 1).

Similarly, for the friend, the time is (1e6 - friend_min_pos). Because the friend starts at 1e6, and the minimal time is to go to the leftmost of his prizes, and then collect others in order. But the path would be 1e6 → friend_min_pos → ... → friend_max_pos (if there are multiple prizes). The steps would be (1e6 - friend_min_pos) + (other steps). But since the friend can collect the prizes in any order, but the minimal time is determined by the leftmost prize. Because once he reaches the leftmost, he can collect all others by moving to the right, but the time to reach the leftmost is (1e6 - friend_min_pos). The rest of the steps are (friend_max_pos - friend_min_pos). But the total time would be (1e6 - friend_min_pos) + (friend_max_pos - friend_min_pos) = 1e6 - friend_min_pos + friend_max_pos - friend_min_pos = (friend_max_pos - friend_min_pos) + (1e6 - friend_min_pos) = friend_max_pos + (1e6 - 2* friend_min_pos). Hmm, that's not the same as 1e6 - friend_min_pos. So my initial reasoning was wrong for the friend.

Wait, no. Let's take an example. Suppose friend has prizes at 5 and 10, and starts at 1e6. Then the minimal path is to go from 1e6 to 5 (taking 999,995 steps), then go to 10 (5 steps). Total steps: 999,995 +5 = 1,000,000 steps. But the friend's time would be 1e6 -5 = 999,995 (if he just collects the 5 prize). But in this case, he has to collect both. So the total time is 999,995 +5 = 1,000,000. But according to the formula (1e6 - friend_min_pos) + (friend_max_pos - friend_min_pos) = (999,995) +5 =1,000,000. So the total time is (1e6 - friend_min_pos) + (friend_max_pos - friend_min_pos) = 1e6 - friend_min_pos + friend_max_pos - friend_min_pos = 1e6 + friend_max_pos - 2* friend_min_pos. But that's not the same as (1e6 - friend_min_pos). So the initial approach is incorrect.

Wait, so the friend's time is not (1e6 - friend_min_pos), but (1e6 - friend_min_pos) + (friend_max_pos - friend_min_pos). Which equals (1e6 - friend_min_pos + friend_max_pos - friend_min_pos) = (friend_max_pos + 1e6) - 2* friend_min_pos. But this depends on both the min and max of the friend's prizes. So how can we model this?

Alternatively, perhaps the friend's time is (1e6 - friend_min_pos) + (friend_max_pos - friend_min_pos) = 1e6 - friend_min_pos + (friend_max_pos - friend_min_pos) = 1e6 + friend_max_pos - 2* friend_min_pos.

But this is the same as (1e6 - friend_min_pos) + (friend_max_pos - friend_min_pos) = (friend_max_pos - friend_min_pos) + (1e6 - friend_min_pos) = the total time taken by the friend.

But this complicates things, because now the friend's time depends on both the min and max of his assigned prizes. So how can we model this?

Alternatively, perhaps the friend's optimal path is to collect all the prizes in such a way that the total time is the maximum between (1e6 - x) for all x in his prizes. Because if he collects them in some order, the path would require that he covers the entire range from his min to max. But that's not possible. Wait, no. Let's think of another example. Suppose the friend's prizes are at 3 and 5. Then he starts at 1e6, goes to 3 (taking 999,997 steps), then to 5 (2 steps). Total 999,999 steps. The maximum (1e6 - x) for x in {3,5} is 999,997 and 999,995. The maximum is 999,997. But the actual time taken is 999,997 +2= 999,999, which is larger than the maximum (999,997). So the initial approach of taking the maximum (1e6 - x) for the friend's prizes is not sufficient.

Hmm. So this complicates the problem. Because now the friend's time is not just the maximum (1e6 - x) for his prizes, but also depends on the arrangement. So how can we model this?

Wait, perhaps the friend's time is (1e6 - min_x) + (max_x - min_x), which is equal to (1e6 - min_x) + (max_x - min_x) = 1e6 + max_x - 2* min_x. Because he has to go from 1e6 to the leftmost prize (min_x), which takes 1e6 - min_x steps, then move right to collect the others up to max_x, which takes (max_x - min_x) steps. So the total time is (1e6 - min_x) + (max_x - min_x) = 1e6 + max_x - 2* min_x.

So for the friend, the time is determined by his min and max. So the friend's time is (1e6 - min_x) + (max_x - min_x) = 1e6 - min_x + max_x - min_x = 1e6 + max_x - 2* min_x.

But how can we model this when we split the prizes between the two people?

So the problem becomes: split all prizes into two groups. For the first group (me), compute the maximum a_i. For the second group (friend), compute the min a_j and max a_j. Then, the time taken by me is (max_me -1), the time taken by the friend is (1e6 + max_friend - 2* min_friend). The total time is the maximum of these two values. We need to split the prizes into these two groups such that the maximum of the two is minimized.

But how to do this efficiently, especially given that n can be up to 1e5?

Alternatively, perhaps there's a better way to model this. Let's think of each prize as a choice: assign to me or to the friend. Then, for each possible assignment, compute the times for me and friend and take the maximum. The goal is to find the assignment that minimizes this maximum.

But trying all possible assignments is impossible for n=1e5. So we need a smarter approach.

So, perhaps the optimal approach is to find a split point where all prizes to the left (or up to a certain point) are assigned to me, and those to the right are assigned to the friend. Because the prizes are sorted, this might be the case. Because any other assignment (where a prize to the left is assigned to the friend and a prize to the right is assigned to me) would be worse. Let's see.

Suppose there's a prize at x and another at y, where x < y. If x is assigned to the friend and y to me, then the friend's time is influenced by x (as part of the min), and my time is influenced by y (as max). But if we swap them, x is mine and y is friend's, then my time increases (since y is higher than x) but the friend's time might decrease. But perhaps the optimal split is where all prizes up to some k are assigned to me, and the rest to the friend.

If this is the case, we can iterate through the sorted list and find the split point where the maximum of (my time, friend's time) is minimized.

So, the approach would be:

1. Sort the prizes (already given sorted in the input).

2. For each possible split point k (0 <= k <=n), where the first k prizes are assigned to me and the remaining n-k to the friend.

3. For each split, compute my_time = (a_{k-1} -1) if k>0 else 0 (if I take no prizes, my time is 0). Wait, but if I take no prizes, my time is 0 (since I start at 1 and don't move). Similarly, if the friend takes no prizes, his time is 0 (stays at 1e6).

Wait, but according to the problem statement, all prizes must be collected by either me or the friend. So the split can't leave any prize unassigned. So for split k, all prizes up to a certain index (maybe) are assigned to me, the rest to the friend.

Wait, but the split can be that I take some prizes, the friend takes others, but not necessarily contiguous. However, given that the prizes are sorted, perhaps the optimal split is contiguous. For example, if a prize at position x is assigned to me, then all prizes to the left of x would be better to be assigned to me as well. Because if there's a prize at y < x, assigning y to me would not increase my time (since the max is x), and if y is assigned to the friend, it would require the friend to have a min of y, which may increase their time.

So perhaps the optimal split is to choose a split where all prizes up to a certain position are mine, and the rest are the friend's. So we can iterate over all possible split points (including 0 and n), compute the maximum time for each split, and choose the split with the minimal maximum.

But how many splits do we need to check? Since the prizes are sorted, we can precompute for each possible split the my_time and friend_time.

But how to compute friend_time for the split. For the friend's group (prizes from k to n-1), the friend's min is a[k], and the friend's max is a[-1]. So the friend's time is (1e6 - a[k]) + (a[-1] - a[k]) = 1e6 + a[-1] - 2*a[k].

Wait, no. Wait, the friend's group would be from a[k] to a[-1]. Wait, no. If the split is after the k-th prize, then the friend's group is all the prizes from k+1 to n-1? Or maybe the split is between 0 and n. For example, split at k means that the first k prizes are assigned to me, and the remaining n-k are assigned to the friend.

So for split k:

- My group is a[0..k-1]. So my time is a[k-1] -1 (if k>0). If k=0, my time is 0.

- Friend's group is a[k..n-1]. His time is (1e6 - a[k]) + (a[-1] - a[k]) ) = 1e6 + a[-1] - 2*a[k] (if friend's group is non-empty, else 0).

So the total time for split k is the maximum between my_time and friend_time.

Wait, but for the friend's group, a[k] is the minimal in his group because the prizes are sorted. So the friend's min is a[k], and his max is a[-1]. So his time is (1e6 - a[k]) (time to reach the leftmost prize) plus (a[-1] - a[k]) (time to collect all from left to right). So total time is 1e6 - a[k] + a[-1] - a[k] = 1e6 + a[-1] - 2*a[k].

If the friend's group is empty (k =n), then his time is 0.

So, for each possible k in 0 ...n:

my_time = a[k-1] -1 if k>0 else 0

friend_time = (1e6 + a[-1] - 2*a[k]) if k <n else 0

Then, the maximum of these two is the total time for this split. We need to find the split k where this maximum is minimized.

So the problem reduces to finding the k in 0..n that minimizes the maximum of:

- (a[k-1] -1 if k>0 else 0)

- (1e6 + a[-1] - 2*a[k] if k <n else 0)

But since the array is sorted, this can be done efficiently by iterating through all possible k and finding the minimum.

Now, given that n can be up to 1e5, iterating through all possible k (n+1 possibilities) is acceptable, as it's O(n) time.

So the algorithm steps are:

1. Read n and the list a (sorted).

2. If n=0 (but constraints say n >=1), handle edge case (but according to the problem statement, n is at least 1).

3. For each possible split k (from 0 to n), compute my_time and friend_time as described.

4. Compute the maximum for each split, then choose the split with the minimal maximum.

But wait, for each k, the split is between the first k prizes and the remaining n-k. So k can be 0 (all assigned to friend) to n (all assigned to me).

Now, for each k, how do we compute my_time and friend_time?

For my_time:

If k=0: 0.

Else, the max of my assigned prizes is a[k-1] (since the first k are assigned to me). So my_time is a[k-1] -1.

For friend_time:

If k ==n: 0.

Else, the friend's assigned prizes are a[k], a[k+1], ..., a[n-1]. The min in this group is a[k], the max is a[-1]. So friend_time is (1e6 - a[k]) + (a[-1] - a[k]) = 1e6 + a[-1] - 2*a[k].

So for each k from 0 to n:

current_max = max( (a[k-1]-1 if k>0 else 0), (1e6 + a[-1] - 2*a[k] if k <n else 0) )

We track the minimum of current_max across all k.

So the code can compute this in O(n) time.

But wait, for each k, we need to check the two conditions. Let's code this.

Let's test this approach with the examples.

First example:

Input: 3 prizes at 2,3,9.

n=3.

a = [2,3,9]

Possible splits:

k=0: all to friend.

friend_time: 1e6 +9 - 2*2 = 1e6 +9-4= 1e6+5. my_time is 0. max is 1e6+5. Not optimal.

k=1: I take 2. my_time is 2-1=1.

friend takes 3,9. friend_time: 1e6 +9 - 2*3 =1e6 +9-6= 1e6+3. max is 1e6+3. Still big.

k=2: I take 2,3. my_time=3-1=2.

friend takes 9. friend_time: 1e6 +9 -2*9 =1e6 -9. my_time is 2. max is 1e6-9=999991. Still not.

k=3: I take all. my_time=9-1=8. friend_time=0. max is8. Which matches the first example.

So the minimal is 8.

Second example:

n=2, prizes at 2 and 999995.

a = [2,999995]

Check k=0: friend takes both. friend_time is 1e6 +999995 - 2*2 = 1e6 +999995-4 = 1,999,991. My time 0. Max 1,999,991. Not.

k=1: I take 2. my_time 1. Friend takes 999995. friend_time: 1e6 +999995 - 2*999995 = 1e6 +999995 -1,999,990 = (1e6 -1,999,990) +999,995. Wait 1e6 is 1,000,000. So 1,000,000 -1,999,990 is -999,990. Add 999,995: total is -999,990 +999,995=5. So friend_time is5. Max(1,5) is5. Which is the correct answer.

k=2: I take both. my_time 999995-1=999994. Max is 999994. So the minimal is5.

So the approach works.

Another test case: the second example.

So the code should compute for each k the current_max, and find the minimal.

Thus, the optimal approach is to iterate k from 0 to n, compute the current_max, and track the minimum.

Now, how to implement this efficiently.

In Python, for a list a sorted, and given that n can be 1e5, this loop will run 1e5+1 times, which is acceptable.

Now, code steps:

Read n.

Read list a as a sorted list (the input gives them in ascending order, so we can just read and perhaps verify they are sorted, but according to the problem statement, the input is given in ascending order).

Compute the maximum a[-1] (which is needed for friend_time).

For each k in 0 to n inclusive:

my_time = 0 if k==0 else a[k-1] -1.

friend_time = 0 if k==n else (1e6 + a[-1] - 2 * a[k])

current_max = max(my_time, friend_time)

keep track of the minimal current_max.

Finally, output the minimal current_max.

But wait, what if k is n? Then friend_time is 0. My_time is a[n-1] -1.

So current_max is a[n-1] -1.

Which is the case where I take all prizes.

So this approach covers all possibilities.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if n ==0:

        print(0, file=output_stream)

        return

    min_time = float('inf')

    max_a = a[-1]

    for k in range(n+1):

        my_time = a[k-1] -1 if k >0 else 0

        if k <n:

            friend_time = (10**6 + max_a - 2 * a[k])

        else:

            friend_time =0

        current_max = max(my_time, friend_time)

        if current_max < min_time:

            min_time = current_max

    print(min_time, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
2 999995
""",
            "output": \
"""\
5
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

Second example:

a = [2,999995], max_a=999995.

k=1: my_time is 2-1=1. friend_time =1e6 +999995 - 2*999995 =1e6 -999995 =5.

current_max is5. Which is correct.

So the code works for these cases.

But what about when the friend's group is empty (k=n)?

Then my_time is a[n-1] -1. friend_time 0. So current_max is a[n-1]-1.

Which could be a candidate for the minimal. For example, if all prizes are very close to 1e6. Like prizes at 999,999 and 999,997. Assigning all to me would take 999,999-1=999,998 steps. Assigning to the friend would take (1e6 -999,997) + (999,999 -999,997) =3+2=5. So the max is5, which is better.

So code would find the correct split.

But the code considers all possible splits.

Now, considering that for n=1e5, this code would loop 1e5+1 times, which is O(n), acceptable for Python.

But wait, for each iteration, the code accesses a[k], which for k=0..n. But for k=n, the code checks k <n (no), so friend_time is 0.

But when k is up to n, a[k] is a[n] which is out of bounds. But in the code, for k in 0..n, when k <n, a[k] is valid. So when k reaches n, k <n is false, friend_time is 0.

So the code is correct.

Thus, the code seems correct.

So the final code is as follows.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
if not a:
    print(0)
    exit()
max_a = a[-1]
min_time = float('inf')
for k in range(n + 1):
    my_time = a[k - 1] - 1 if k > 0 else 0
    if k < n:
        friend_time = (10**6 + max_a - 2 * a[k])
    else:
        friend_time = 0
    current_max = max(my_time, friend_time)
    if current_max < min_time:
        min_time = current_max
print(min_time)
```
