<think>
Okay, let's see. The problem is about Kirito defeating dragons. He needs to fight all of them in some order. The key is choosing the right order so that he can defeat all without losing any. Hmm.

So the initial strength is s. Each dragon has xi and yi. If Kirito's strength is not greater than xi when he fights the dragon, he dies. Otherwise, he wins and his strength increases by yi. So the order in which he fights the dragons matters a lot.

Wait, how to determine the optimal order? Because some dragons have lower xi but maybe a higher yi, but maybe others have higher xi but lower yi. But if he can fight the ones with lower xi first, he can get their bonuses and then take on the tougher ones.

But how do we model this? Maybe we should fight the dragons in an order where the required xi is as low as possible first. That way, Kirito can accumulate as much strength as possible early on. So the strategy would be to sort the dragons in increasing order of xi, and then for dragons with the same xi, maybe sort by the bonus yi in descending order to maximize the gain early.

Wait, but even if two dragons have the same xi, the order in which we fight them doesn't matter as long as Kirito can defeat both. Like, if after fighting one, his strength increases, but he had enough to fight both in either order.

So the main idea is to sort the dragons by their xi in ascending order. Because Kirito needs to fight the weakest possible dragons first, to get their bonuses, which will allow him to take on stronger ones later.

Let me test this logic with the examples.

First example: the input is s=2, n=2. The dragons are (1,99) and (100,0). If sorted by xi, the first dragon is (1,99), then (100,0). Kirito starts with 2, beats the first (1 < 2), gains 99 to 101. Then he can beat the second (100 < 101). So yes, this works.

Second example: s=10, one dragon (100,100). He can't fight it because 10 <= 100. So no.

So the approach seems to work for these cases.

So the steps would be:

1. Sort all dragons in non-decreasing order of xi.
2. For each dragon in this order, check if Kirito's current strength is greater than xi.
   a. If yes, add yi to his strength.
   b. If no, return "NO".
3. If all dragons are defeated, return "YES".

But wait, what if there's a dragon that has a lower xi than another, but even after defeating the lower xi one, Kirito's strength plus the bonus isn't enough for the higher xi one? Then maybe there's a different order where he could fight some other dragons first to get more bonuses.

Wait, but the problem requires that he can defeat all dragons in some order. So the question is whether there exists any possible order where he can defeat all. But the optimal order (greedy approach) is to fight the dragons with the lowest xi possible first, as that allows him to gain maximum bonuses as early as possible. Because any other order would require him to have higher strength to fight a dragon with higher xi, but if he can't even fight the lower ones first, then he can't get the bonuses needed.

So the greedy approach of sorting by xi ascending is the correct strategy. Because any other order would have Kirito facing a dragon with a higher xi than possible, unless he has the bonuses from lower xi dragons.

So the algorithm is: sort all dragons by xi in ascending order, then check if he can defeat them in that order.

But what about two dragons where xi is the same? For example, two dragons with xi=5. The order between them doesn't matter, but the one with higher yi should be fought first? Or wait, the order between them doesn't matter because their xi is same. If Kirito's strength is higher than 5, he can fight either. Adding the yi from the first would help in the next. So perhaps when xi is the same, we should prioritize dragons with lower yi first? Or maybe higher yi? Because higher yi would give a bigger boost, which could help in future dragons.

Wait, no. Because in the same xi group, the order between them doesn't affect whether he can defeat them. Suppose he has strength s > xi for both. He can fight them in any order, but fighting the one with higher yi first would give a bigger boost. So in that case, when xi is same, it's better to take higher yi first to get more strength earlier.

But since the problem is to find whether there exists any order that allows him to defeat all dragons, the greedy approach of fighting in sorted order (xi ascending) is sufficient, regardless of the order of yi for same xi. Because in the sorted approach, he will be able to defeat all dragons if possible, and if not, then no order exists.

But how can we be sure of that? Suppose there's a case where two dragons have xi=3 and xi=5. Then, if he can defeat 3 first, get a yi, then 5. But maybe if he fights 5 first (even if his initial strength is just 4, which is less than 5, so he can't). So the sorted order is necessary here.

So the correct approach is to sort dragons by their xi in ascending order and process them in that order. If Kirito can defeat them all in that order, then the answer is yes; otherwise, it's no.

So the steps for the solution are:

- Read s and n.
- Read n pairs of xi and yi.
- Sort the list of dragons in ascending order of xi.
- Iterate through each dragon in this sorted list:
   - If current s > xi: add yi to s.
   - Else: return "NO".
- After all dragons, return "YES".

That's the plan. Now, let's think about the implementation.

In Python, we can read the input as follows:

s, n = map(int, input().split())
dragons = []
for _ in range(n):
    xi, yi = map(int, input().split())
    dragons.append( (xi, yi) )

Then sort dragons by xi:

dragons.sort(key=lambda x: x[0])

Then loop through each dragon in the sorted list:

for xi, yi in dragons:
    if s > xi:
        s += yi
    else:
        print("NO")
        exit()
print("YES")

Wait, but wait: the condition is "if Kirito's strength is not greater than the dragon's strength xi, he loses." So if s is equal to xi, he loses. So the condition is s must be strictly greater than xi.

Yes. So the check is s > xi. If not, he can't fight this dragon and loses.

So the code above is correct.

Testing the first sample:

Sample 1 input:

2 2

1 99

100 0

After sorting, the dragons are (1,99), (100,0).

First, s=2 >1: add 99. s becomes 101. Then next dragon: 101>100, add 0. All done. Output YES.

Sample 2: s=10, 1 dragon (100,100). Sorted list is (100,100). 10 is not >100. Output NO.

Another test case: what if there's a dragon with xi equal to another, but different yi? Like two dragons with xi=5. Suppose Kirito's initial s is 6.

If he fights the one with yi=10 first, s becomes 16. Then the next (xi=5) gives s 21. If he had fought them in reverse order (yi=0 first), then s would be 6+0=6, then add 10: 16. Either way, he can defeat both. So the order in same xi doesn't matter for the outcome of whether he can defeat all. Because once he has enough to defeat the first, adding the yi's will make sure he can defeat the others with same xi.

But what if there's a dragon with xi=3 and yi=0, and another with xi=3 and yi=5. Then, fighting the one with yi=5 first gives more strength. Which could help in subsequent dragons. So in this case, fighting the higher yi first is better. So if same xi, we should sort them in order of descending yi. Because that way, the maximum possible strength is accumulated early.

But in the code above, we sort by xi only. So in the case where two dragons have same xi, their order is not determined by yi. So if the code's sorting leaves them in arbitrary order (like as per their insertion order), then perhaps for some cases, the code would fail.

Wait, but in the problem statement, the code must output "YES" if there exists any order where Kirito can defeat all dragons. The approach of sorting by xi and not considering yi for same xi may not cover all possible orders, but perhaps it's sufficient.

Wait, no. Because if the code's approach is to sort by xi in ascending order, but for same xi, the order is arbitrary. So perhaps there exists a scenario where the code's approach would fail, but another order would work.

For example:

Suppose Kirito's s is 5. There are two dragons: (5, 5) and (5, 0). Wait, no. Because 5 is not greater than 5, he can't fight either. So he would lose. But if there are two dragons with xi=4 and yi=1 and another with xi=5 and yi=0. Let's see.

s=5.

Dragon 1: xi=5, yi=0.

Dragon 2: xi=4, yi=1.

If sorted by xi, the order is dragon2 (xi=4), dragon1 (xi=5).

So first fight dragon2: s=5>4. Add 1. s becomes 6. Then fight dragon1: 6>5. Add 0. Success.

But if sorted in the original order (5 and 4), then the code would check 5 vs s=5. Since s is not greater than 5, he can't fight. So in this case, the code works because the dragons are sorted in ascending order.

Wait, no. The initial order of the dragons in the input is (5,0) then (4,1). The code sorts them by xi, so the sorted list is (4,1) then (5,0), so the code would process them in the right order.

So the code's approach of sorting by xi is correct.

But here's a scenario where same xi but different yi:

Kirito's s is 6. Two dragons: (5, 1) and (5, 2). Suppose there's another dragon with xi=7. So after defeating the first two, s would need to be >7.

So after defeating both 5's, s would be 6+1+2=9. Then 7 is 7 <9: s becomes 9+ bonus.

But if in the code's sorted order, the dragons are sorted as (5,1) and (5,2). If he fights (5,1) first: s becomes 7, then (5,2) gives 9. Then the next dragon (7) is 7<9. So works.

But if the code's sorted order had (5,2) first, then (5,1), then he would have s=6+2=8, then 8+1=9. Same result.

But the code's approach sorts by xi only, so the order between same xi dragons is based on their original order. However, in this case, the code would still process all same xi dragons as long as Kirito's initial s is greater than xi.

Wait, but the order of same xi dragons doesn't matter in this code. Because as long as Kirito's strength is greater than xi, he can fight any of them. The order in same xi group may affect the total strength gained, but if after processing all same xi dragons, his strength is the sum of all their yi plus initial s, then the order between them doesn't matter. Because each dragon in same xi group has s > xi, so he can fight them in any order. Adding all their yi would give the same total sum, but the order of adding would affect intermediate steps. Wait, no. Because the order in which he fights them affects the intermediate s. For example, fighting a dragon with yi=5 first gives s +5, which may allow fighting another dragon with higher yi. Wait, but no. All dragons in the same xi group have xi equal. So if Kirito's initial strength is greater than xi, then he can fight them in any order, but the total bonus is the sum of all yi. So if he can fight all, the order doesn't matter for the total. Because each gives a yi, and the sum is additive. So the order between same xi dragons is irrelevant. Because once s is > xi, you can fight all in any order. So the code's approach of processing same xi dragons in any order is okay.

But wait, what if there are two dragons with xi=3, and Kirito's initial s is 4. The first dragon gives yi=1, the second yi=3. So if he fights the first, his s becomes 5, then the second gives 8. But if he fights the second first, s becomes 7, then first gives 8. The order doesn't matter for the sum. But what if after these two, there's a dragon with xi=5. In either order, the sum is 8, which is greater than 5. So same result.

So the code's approach of processing same xi dragons in any order (as sorted by original input order or whatever) is okay. Because the sum of their yi is the same regardless of order. So the code doesn't need to sort same xi dragons by yi.

But wait, in a case where the same xi dragons' yi's affect whether he can defeat other dragons. For example:

s = 5, dragons:

xi=3, yi=1

xi=3, yi=3

xi=6, yi=0

In this case, if he fights the first dragon (3,1) first, his s becomes 6. Then he can fight the next (3,3), s becomes 9. Then the dragon with xi=6: 9>6, yes. So works.

If he had fought the (3,3) first, s becomes 8, then (3,1) gives 9. Then same result.

But what if the next dragon was xi=5, and Kirito's s after two dragons is 9. If he had fought the first dragon in any order, the sum is same.

So the order between same xi dragons doesn't matter for the sum. So the code's approach is correct.

Therefore, the code should sort the dragons by xi in ascending order, and process them in that order. The code as written is correct.

Now, let's think about possible edge cases.

Edge case 1: n=0. But according to the constraints, n is at least 1. So no.

Edge case 2: s is just 1 more than a dragon's xi. Then after defeating, the bonus may allow other dragons.

Another edge case: all dragons have xi less than s. Then he can fight them all in any order, but sorted order is still okay.

Another case where after defeating a dragon, the bonus allows defeating others.

So the code is correct.

Now, implementing this in Python. The code is straightforward. Read s and n. Read the dragons. Sort by xi. Then loop through each, check if s > xi. If yes, add yi. Else, print NO and exit. If all passed, print YES.

Testing this code against the examples:

First example:

Input:

2 2

1 99

100 0

After sorting, the dragons are [(1,99), (100,0)]. The loop checks 2>1: add 99, s=101. Then 101>100: add 0. Output YES.

Second example: 10 1, (100,100). Sorted list has (100,100). 10>100? No. Output NO.

Another test case:

s=5, dragons: [(5, 5), (5,0)]. Then sorted by xi, both are 5. Kirito's s is 5. The first dragon's xi is 5. 5>5? No. So he can't fight either. So output NO. But if he could fight in some order where first is the (5,0) and (5,5) next, but his initial s is 5, he can't fight either. So code's answer is correct.

Another case where s=6, dragons [(5,1), (5,2), (7,0)]. Sorted as [(5,1), (5,2), (7,0)]. After first two, s becomes 6+1+2 =9. Then 9>7: yes. So output YES.

So the code works.

Now, code:

Read s and n.

Read n dragons.

Sort by xi.

Loop:

for xi, yi in dragons:

   if s > xi:

      s += yi

   else:

      print("NO")

      exit

print("YES")

Yes.

So that's the code.
</think>

```python
s, n = map(int, input().split())
dragons = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
for xi, yi in dragons:
    if s > xi:
        s += yi
    else:
        print("NO")
        exit()
print("YES")
```