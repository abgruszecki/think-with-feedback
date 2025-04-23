<think>
Okay, I need to solve this programming problem. Let's read it carefully.

So, the problem is about a robot that picks items from either end of a line. Each time it uses a hand (left or right), and if the previous action was the same hand, it adds an extra Ql or Qr energy cost. The goal is to find the minimal total energy needed to pick all items.

Hmm. Let's think about the possible approaches here.

First, the constraints: n can be up to 1e5, which is 10^5. That suggests that any O(n^2) approach is probably too slow. So, we need an O(n) or O(n log n) solution.

Let's think about the possible choices. For each step, the robot can take either the leftmost or rightmost item. But the decision affects the next step's possible costs because of the consecutive same-hand penalty.

Wait, but the penalty applies only if the previous action was the same. So, the state for dynamic programming might need to track the last action (left or right) and perhaps the count of consecutive actions. But with n up to 1e5, tracking the last action might be manageable if the transitions are O(1) per step.

But wait, even if we model the DP state as (left, right, last_hand, consecutive_count), that could be O(n^2) in the worst case, which is not feasible for n=1e5.

Alternative approach: find a way to model the problem such that the DP can be optimized to O(n) time.

Alternatively, perhaps there's a greedy approach here, but considering the penalties, it's not obvious. For example, the optimal choice might not be simply taking the left or right item based on current minimal cost, because future penalties might offset any immediate gains.

Another angle: the problem requires choosing a sequence of left and right picks, such that the sum of the individual costs plus the penalties for consecutive same-hand usage is minimized.

Let's think about the total number of times we switch hands. For example, if we take several items from the left in a row, each after the first would add Ql. Similarly for the right.

But perhaps the optimal strategy involves taking a certain number of lefts, then some rights, then some lefts, etc., but again, considering the penalties.

Alternatively, maybe the best approach is to split the items into a left segment and a right segment. For example, take the first k items from the left, and the rest from the right. But then, consecutive same-hand operations could add penalties. But how?

Wait, suppose we take some items from the left, then switch to taking all remaining from the right. In that case, the lefts are all consecutive, so each after the first adds Ql. Similarly, the rights are consecutive, each after the first adds Qr.

But maybe the optimal approach is to take all from left, or all from right, or split between left and right such that the number of consecutive same-hand actions is minimal.

Wait, but what if the split is such that the left and right hands are alternated? Like left, right, left, right. But then, after each switch, there's no penalty. But that's only possible if the number of items is even. Otherwise, one hand has to take the last one.

Hmm. Let's think of some examples.

In the first sample input, n=3. The optimal sequence was left, right, left. So two lefts and one right. The first left has no penalty, the right (after left) has no penalty, then the left after right incurs a penalty because the previous was left? Wait no. Wait, the first left is taken. Then the next action is right. Then the third is left again. So the third action's previous was right, so no penalty. Wait, but according to the note, the total was 4*42 (first left) + 4*99 (right) +4*3 (left again). The penalty would be added only if the previous action was same. So in this case, the third action is left after right, so no penalty. So in this case, the total is just the sum of each weight multiplied by l or r, plus any penalties for consecutive same.

So, in this example, the third action's previous was right, so no penalty. So the total is (42*4) + (99*4) + (3*4) = 4*(42+99+3) = 4*144=576.

Ah, so in that case, the penalty is only when the same hand is used consecutively. So for a sequence like left, left, the second left incurs a penalty of Ql.

So the key is to model the transitions between left and right, keeping track of the previous action.

But with n up to 1e5, a standard DP approach where we track the last action and the number of consecutive steps might not be feasible. Because for each step, there are two possibilities (last action was left or right), but each step could require O(1) time.

Wait, perhaps a DP approach where for each possible left and right index, and the last action, we track the minimal cost. Let's model the problem as follows:

We have left index i and right index j. The next possible actions are take i+1 (left) or j-1 (right). But this approach would require O(n^2) time, which is impossible for n=1e5.

So that's not going to work.

Alternative idea: since the items are arranged in a line and we have to take them all, the problem can be viewed as choosing a split between some left items and some right items, with possible overlaps when switching hands.

Wait, perhaps the optimal strategy is to take a certain number of left items, then some right items, but the number of same-hand consecutive steps would determine the penalties.

Alternatively, maybe the minimal cost is to take all from left or all from right, whichever is better, but considering the penalties for consecutive steps. For example, taking all left would have (n-1) * Ql penalties, because each step after the first adds Ql.

But perhaps that's not optimal. Let's see.

For example, if taking all left:

Total cost would be sum(w_i * l) + Ql * max(0, (number of left steps -1) - 0). Since each consecutive step after the first adds a Ql. So if there are k consecutive left steps, the penalty is (k-1) * Ql.

So for taking all left: the penalties are (n-1) * Ql.

Similarly for all right: (n-1)* Qr.

But maybe splitting into left and right steps can avoid some penalties.

So perhaps the minimal cost is the minimum between taking all left, all right, or some split.

But how to model the split.

Another observation: the penalty only depends on consecutive same-hand steps. So if there's a split where the left and right steps are alternated, there are no penalties except possibly in the middle.

Wait, but the items are taken in order, so the leftmost and rightmost are taken in some order. For example, if you take left, then right, then left again, etc.

So perhaps the optimal approach is to take a certain number of items from the left, then some from the right, and possibly alternate, but the key is to minimize the penalties.

Alternatively, maybe the optimal solution is to take some items from the left and some from the right, with the split at some position k, so that you take the first k items from the left and the remaining (n-k) from the right. But then, when you switch from left to right, there's a transition. The penalties would be (k-1)*Ql (if k>1) plus (n-k-1)*Qr (if n-k>1). But if the split is such that you take all left then all right, then the sequence is left k times, then right (n-k) times. So between the left steps and the right steps, there's a transition. The last left step is followed by the first right step: no penalty. So for the left steps, there are (k-1)*Ql penalties. For the right steps, (n-k-1)*Qr penalties.

But wait, when you take k left steps and then (n-k) right steps, the total penalties are (max(k-1,0)) * Ql + max(n-k-1, 0)* Qr. Then, when you switch from left to right, there's no penalty for that switch, but between the left steps, the penalties accumulate.

But when k is 0, then all are right steps. When k is n, all left steps.

But perhaps the minimal cost is to take all left or all right, but perhaps for some splits, the sum is lower.

But how to compute this for all possible splits k (0 <=k <=n) efficiently.

Wait, but for each split k, the cost would be:

sum_{i=1 to k} w_i * l + sum_{j=k+1 to n} w_j * r + (max(0, k-1)) * Ql + (max(0, (n -k) -1)) * Qr) + additional penalties if the split is such that the left and right steps are consecutive and require a penalty.

Wait, no. Wait, if you take all k left steps first, then all (n-k) right steps. So for the left steps: the first left step has no penalty, then each subsequent left step adds Ql. So (k-1) * Ql. For the right steps: first step (after the left steps) has no penalty, then (n-k-1) steps each adding Qr. So total penalties for right steps is (n-k-1)*Qr.

But wait, if the split is k left steps followed by (n-k) right steps, then the total penalties are (k-1)*Ql + (n-k-1)*Qr. However, there's an additional penalty if k>0 and (n-k) >0, but after the first right step, no. Because the left steps are consecutive, then the right steps are consecutive. So the penalties for left steps and right steps are computed as (k-1)*Ql and (n-k-1)*Qr.

But then, the total cost is:

sum_left = sum(w_i for i in 1..k) * l + sum_right = sum(w_j for j in k+1..n) * r

plus penalties (k-1)*Ql + (n-k-1)*Qr.

But is that the correct model? Let's see.

For example, in the first sample input:

n=3, k=2 (take two left steps and then 1 right step). Wait no. Wait, the first sample's note says the sequence was left, right, left. So the split is not left followed by right. So this model of taking k left and then (n-k) right would not capture that scenario. Hence, this approach may not consider all possible possibilities.

So this suggests that considering splits where all left are taken first, then all right, may not be sufficient. So the model of splitting into k left and n-k right steps may miss some optimal sequences.

So perhaps the optimal solution requires a more complex pattern of left and right steps, such as left, right, left, etc. But how to model that.

Alternative idea: For any sequence of left and right steps, the total penalties are the sum of Ql for each consecutive left steps after the first, plus Qr for each consecutive right steps after the first.

So, for example, a sequence of L, L, R, R, R would have penalties Ql (for the second L), Qr (for the third R), Qr (for the fourth R).

So the total penalties are 1*Ql + 2*Qr.

The problem is to find the sequence of left and right steps that picks all items, and has the minimal total cost (sum of (l or r) * w_i for each step, plus the penalties).

Hmm. But how to model this for n up to 1e5.

Dynamic programming approach:

We can model the DP state as the last hand used (left or right), and the number of consecutive steps taken with that hand so far. Wait, but that's not sufficient. Because if the last step was left, and the previous was left, then the next step if left would add another Ql. But if the next step is right, no penalty.

But for DP, perhaps we can track the last hand used. Then, for each position (i, j) (left and right pointers), and the last hand, we can track the minimal cost.

But again, with n up to 1e5, this approach would be O(n^2) time and space, which is impossible.

Alternative approach: since we have to take all items, the problem can be considered as a sequence where each step takes either the leftmost or rightmost remaining item. So the process reduces the range of items until none are left.

At each step, the decision is to take left or right. The decision affects the next step's possible penalties.

So the state can be represented by the current left and right pointers (i and j), and the last hand used (left or right). The minimal cost for each state can be stored, but for n up to 1e5, this would be O(n^2) states, which is not feasible.

Thus, this approach is not suitable.

Alternative idea: Maybe the optimal strategy is to take all possible left steps first, then all right steps, or vice versa. Or take some left steps, then some right steps, but only switch once. Because switching multiple times might not be better.

Wait, considering that each switch between hands allows avoiding penalties, but the cost of switching could be outweighed by the penalties.

But how?

Alternatively, the minimal cost occurs when the number of consecutive steps in one direction is maximized. So perhaps the optimal solution is to take all left, all right, or split into two groups (left and right), but with possible penalties for the larger group.

So let's explore this idea.

Suppose we split the items into k left steps and (n-k) right steps, but the left and right steps are taken in a way that minimizes the penalties.

If we take all left steps first, then all right steps:

Penalty for left steps is (k-1)*Ql.

Penalty for right steps is (n-k-1)*Qr.

But if k > (n-k)+1, then there's an additional penalty for the left steps. For example, if we take 5 left steps and 3 right steps. The left steps have 4 penalties (5-1=4), the right steps have 2 penalties (3-1=2). Total penalties 4*Ql + 2*Qr.

But maybe there's a case where taking some steps from left and some from right, but in a way that the numbers are such that the penalties are minimized.

Alternatively, if the left steps are taken in a way that they are not consecutive, but interspersed with right steps, but that would require multiple switches. However, this may not be optimal because each switch allows avoiding a penalty, but the cost of the item (which is taken with the other hand) could be higher.

So perhaps the optimal solution is to choose between:

1. Taking all left steps, with penalties (n-1)*Ql.

2. Taking all right steps, with penalties (n-1)*Qr.

3. Taking some split k left and (n-k) right steps, with penalties (max(0, k - (n-k) -1 )) * Ql + (max(0, (n-k) -k -1 )) * Qr.

Wait, where did that come from?

Wait, when we take k left steps and (n-k) right steps, but the steps are taken in such a way that they alternate as much as possible. For example, the number of consecutive steps in each direction is limited by the difference between k and (n-k). For example, if k is much larger than (n-k), then after taking (n-k) steps of left and right alternately, there are (k - (n-k)) left steps left, which would have to be consecutive, leading to penalties.

Hmm. Let's think of it as follows:

Suppose we have a left and right split. The minimal number of penalties is when we alternate as much as possible between left and right steps. But if one side has more steps than the other, the excess steps would be consecutive, leading to penalties.

For example, if k is the number of left steps and (n-k) is the number of right steps.

If k > (n-k), then the number of excess left steps is (k - (n-k)) = 2k -n. So these steps would be consecutive, leading to (2k -n -1) * Ql penalties.

Similarly, if (n-k) >k, then excess right steps lead to (2(n-k) -k -1) * Qr penalties.

So the total penalties would be:

penalty = max(0, (k - (n -k) -1)) * Ql + max(0, ( (n -k) -k -1 )) * Qr.

Wait, perhaps the formula is:

If the left steps are k and the right steps are m =n-k.

The maximum possible number of alternations is min(k, m). Then, the excess is (k - m) if k > m, else (m -k).

The excess steps are consecutive, so for each excess step beyond the first, you add a penalty.

For example, if there are 5 left steps and 3 right steps. The maximum alternations are 3 pairs (left, right), leaving 2 left steps. These two are consecutive, so the penalty is 1 * Ql (since (2-1) steps after the first).

So the formula for the penalty when k > m:

excess = k - m.

penalty = (excess -1) * Ql.

Similarly, when m >k: (excess -1)* Qr.

But when k and m are equal (even split), then there's no excess, so penalties are (k-1) * Ql + (m-1)* Qr? Wait no. Because if you alternate all steps, then after each step, the hand switches. So there are no consecutive same-hand steps. Hence, penalties are zero.

Wait, in that case, if k =m, then the sequence is left, right, left, right, ..., alternately. So no consecutive steps. So penalties are zero.

So the penalty would be:

if k >= m:

penalty = max(0, (k - m -1)) * Ql.

if m >=k:

penalty = max(0, (m -k -1 )) * Qr.

So the formula is:

penalty = max(0, (k - m -1 )) * Ql if k > m.

penalty = max(0, (m -k -1 )) * Qr if m >k.

If k ==m, then penalty is zero.

So combining all cases:

penalty = max(0, (k - m -1)) ) * Ql + max(0, (m -k -1 )) * Qr.

But since only one of (k -m -1) or (m -k -1) can be positive, the sum is equivalent to:

penalty = max(0, (k - m -1)) * Ql if k > m.

penalty = max(0, (m -k -1)) * Qr if m >k.

If k ==m, then penalty is zero.

So, for example, if k=5, m=3:

excess =5-3=2.

excess-1 =1 → 1*Ql.

So penalties are 1 * Ql.

If k=3, m=5:

excess is 5-3=2 → 2-1=1 → 1 * Qr.

So for a split of k left and m right steps, the total cost would be:

sum_left = sum(w_i) * l for left steps.

sum_right = sum(w_j) * r for right steps.

plus penalty as calculated above.

So, the total cost is:

sum_left + sum_right + penalty.

If we can precompute the prefix sums for left and suffix sums for right, then for each possible split k (number of left steps taken), we can compute the sum_left as prefix[k] * l, sum_right as (total_sum - prefix[k]) * r.

Then, compute the penalty based on the difference between k and (n-k).

Then, find the minimal total cost among all possible k (from 0 to n).

But how to compute this efficiently.

The steps would be:

1. Precompute prefix sums of the array.

2. Iterate k from 0 to n (number of left steps), compute m =n -k.

3. For each k, calculate the penalty.

4. Calculate sum_left = prefix[k] * l.

sum_right = (prefix[n] - prefix[k]) * r.

total = sum_left + sum_right + penalty.

5. Find the minimal total.

But since k can be up to 1e5, and each iteration is O(1), this would be O(n) time.

Yes. So this approach is feasible.

So the key idea is to consider all possible splits into k left steps and (n-k) right steps. For each split, calculate the penalty based on the excess steps in the majority hand. Then, choose the split with the minimal total cost.

But why is this approach correct?

Because any optimal sequence must have a split into left and right steps where after all left steps are taken, then all right steps are taken. Or, perhaps, the optimal sequence can be modeled as taking some left steps first and then right steps, with the penalties calculated as described. But this is not obvious.

Wait, the example given in the first sample input:

n=3, l=4, r=4, Ql=19, Qr=1.

The optimal solution was to take left, right, left. So the split is k=2 left steps and m=1 right steps.

In this case, the split is k=2, m=1. So k > m.

Excess is 2-1=1.

Penalty is (1-1) * Ql =0. So according to the model, penalty is zero.

But according to the note, the sum is 42*4 +99*4 +3*4 = 576. No penalties because after the first left, the next is right (no penalty), then left again (previous was right, no penalty). So the model's penalty calculation for split k=2 (left steps) and m=1 (right steps) gives zero penalty, which matches the actual case.

So according to the model, the penalty would be (k -m -1) * Ql. Here k=2, m=1: 2-1-1=0. So max(0, 0) *19=0. So yes, correct.

Another example: the second sample.

Input:

4 7 2 3 9

1 2 3 4

The optimal sequence is R, L, R, R.

So split into k=1 left steps (after the first R, take L, then two Rs). So according to the model, k=1 (left steps), m=3 (right steps). So m=3, k=1.

Excess is 3-1=2. So penalty is (2-1)*9=9*1=9.

But according to the note, the sum of penalties is 9 (the last two Rs contribute 9).

Wait, in the note's example:

The sequence is right (take 4), left (take 1), right (take 3), right (take 2).

So the steps are R, L, R, R.

The penalties:

The first R: no penalty.

Then L: no penalty (switched).

Then R: no penalty (switched from L).

Then R: previous was R → add Qr (9) penalty.

So total penalties: 9.

In the model's calculation for k=1 (left steps) and m=3 (right steps), the penalty is (3-1-1)*9= (1)*9=9. Which matches.

So the model works for this case.

Thus, the model of splitting into k left and m right steps, and calculating the penalty as max(0, (k -m -1)) * Ql (if k>m) else max(0, (m-k-1)) * Qr, seems to capture the penalties correctly.

Therefore, the approach is to iterate all possible k from 0 to n, compute the sum and penalty, and select the minimal.

So, the steps are:

1. Compute the prefix sum array.

2. For each k from 0 to n:

   a. sum_left = prefix[k] * l.

   b. sum_right = (prefix[n] - prefix[k]) * r.

   c. m = n -k.

   d. penalty:

      if k > m:

         excess =k - m.

         penalty = max(0, excess -1) * Ql.

      else if m >k:

         excess =m -k.

         penalty = max(0, excess -1) * Qr.

      else:

         penalty =0.

   e. total = sum_left + sum_right + penalty.

3. Find the minimal total.

This approach is O(n) time, which is acceptable for n=1e5.

Now, how to implement this.

First, read n, l, r, Ql, Qr.

Then, read the array w.

Compute the prefix sum array.

Then, iterate k from 0 to n.

For each k, compute the sum_left, sum_right, and penalty.

Find the minimum.

Yes.

But wait, when k=0, then all steps are right steps. So m =n-0 =n.

Excess is n-0 =n, so penalty is (n-0-1) * Qr → (n-1)*Qr.

Which matches the case of all right steps.

Similarly, when k=n, then m=0, penalty is (n-1)*Ql.

Thus, this approach handles all possible splits, including taking all from left or right.

So this approach should find the minimal total cost.

Now, let's test it against the samples.

First sample input:

n=3, l=4, r=4, Ql=19, Qr=1.

w = [42,3,99]

But wait, the input line is 42 3 99. So the items are arranged as 1:42, 2:3, 3:99.

But according to the note, the optimal split is k=2 left steps (42 and 3) and m=1 right step (99). Wait, no. Wait the note's sequence is left, right, left, which would take the first item (42), then the third item (99), then the second (3). So the split is k=2 left steps (taking 42 and 3) and m=1 right step (99). But according to the code's model, the split is k=2 (left steps) and m=1 (right steps).

sum_left = (42+3)*4 =45*4=180.

sum_right = (99)*4=396.

Total sum: 180+396=576.

penalty: (2-1-1) → 0. So total is 576+0=576. Which matches the sample's output.

Second sample:

Input:

4 7 2 3 9

1 2 3 4.

The optimal split is k=1 (left steps) and m=3 (right steps).

sum_left = 1*7=7.

sum_right = (2+3+4)*2 =9*2=18.

sum_left + sum_right=25.

penalty: m=3, k=1. excess=3-1=2. penalty is (2-1)*9=9.

Total 25+9=34, which matches the sample.

So the model works.

Therefore, the approach is to compute all possible splits and select the minimal total.

Thus, the code can be written as follows.

We need to compute the prefix sum, then loop from k=0 to n.

Now, in Python, for n=1e5, the code should run quickly, as each iteration is O(1).

So the steps:

Read the input: n, l, r, Ql, Qr.

Read the list of weights.

Compute the prefix sum.

Compute the total sum (prefix[-1]).

Then, for each k in 0 to n:

sum_left = prefix[k] * l.

sum_right = (total - prefix[k]) * r.

m = n -k.

if k >m:

   excess =k -m

   penalty = max(0, excess-1) * Ql

elif m>k:

   excess =m -k

   penalty = max(0, excess-1)* Qr

else:

   penalty =0.

total_cost = sum_left + sum_right + penalty.

keep track of the minimal total_cost.

Thus, this can be implemented efficiently.

Now, code in Python.

But wait, the prefix sum for a list of 1e5 elements is manageable.

Sample code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, l, r, Ql, Qr = map(int, input_stream.readline().rstrip("\n").split())

    w = list(map(int, input_stream.readline().rstrip("\n").split()))

    prefix = [0]*(n+1)

    for i in range(n):

        prefix[i+1] = prefix[i] + w[i]

    total = prefix[-1]

    min_energy = float('inf')

    for k in range(n+1):

        m = n - k

        sum_l = prefix[k] * l

        sum_r = (total - prefix[k]) * r

        if k > m:

            excess = k - m

            penalty = max(0, excess -1) * Ql

        elif m > k:

            excess = m -k

            penalty = max(0, excess -1)* Qr

        else:

            penalty =0

        total_cost = sum_l + sum_r + penalty

        if total_cost < min_energy:

            min_energy = total_cost

    print(min_energy, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 7 2 3 9
1 2 3 4
""",
            "output": \
"""\
34
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

Second sample:

n=4.

w is [1,2,3,4].

prefix is [0,1,3,6,10,10? Wait no. Wait n=4, so prefix has 0,1, 3 (1+2), 6 (3+3), 10 (6+4).

So for k=1:

sum_l=1*7=7.

sum_r= (10-1)*2=9*2=18.

m=4-1=3. m>k: 3>1. excess=3-1=2. penalty (2-1)*9=9.

7+18+9=34.

Which is correct.

Thus, the code should work.

Edge Cases:

Test case where all are left steps.

Another test case where all are right steps.

Another where k and m are equal.

For example, n=2.

k=1, m=1.

excess is 0. Penalty 0.

Thus, sum_l = (w1) *l. sum_r= w2*r. penalty 0.

Yes.

Thus, the code should handle all cases.
</think>

```python
n, l, r, Ql, Qr = map(int, input().split())
w = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + w[i]
total = prefix[-1]
min_energy = float('inf')

for k in range(n+1):
    m = n - k
    sum_l = prefix[k] * l
    sum_r = (total - prefix[k]) * r
    if k > m:
        penalty = max(0, (k - m - 1)) * Ql
    elif m > k:
        penalty = max(0, (m - k - 1)) * Qr
    else:
        penalty = 0
    current = sum_l + sum_r + penalty
    if current < min_energy:
        min_energy = current

print(min_energy)
```
