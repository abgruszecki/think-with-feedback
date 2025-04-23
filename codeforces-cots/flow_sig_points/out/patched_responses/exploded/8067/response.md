<think>
Okay, let's see. The problem is to check if the given sequence of submissions is in chronological order according to the rules described. 

So each submission has x and k. The x is the number of previous distinct solutions the same participant k had before this submission. For a submission to be valid, when a participant k submits with x=0, it means it's their first unique solution. Then, if later there's an x=1 for the same k, that means there was exactly one previous unique submission from them before that. And so on. The key point is that for a submission (x, k) to be valid, the participant k must have previously submitted exactly x unique solutions. So each x for a participant k must be exactly equal to the count of unique submissions they made before this one.

So the task is to process each submission in order and check for each (x, k) pair whether x equals the current count of unique submissions made by k. If all submissions satisfy this, output YES; otherwise, NO.

How do we track this efficiently?

Let's think about data structures. For each participant k, we need to track how many unique submissions they've made so far. Because, when a new submission comes in, x must equal the current count. Then, if x is correct, we increment the count for k by 1 (since this submission becomes a new unique one). If x is not equal to the current count, the data is invalid.

So the approach is:

1. Initialize a dictionary (let's call it counts) where each key is a participant k, and the value is the number of unique submissions they've made so far.
2. For each submission (x, k) in the input order:
   a. Check if counts.get(k, 0) equals x.
   b. If not, return "NO".
   c. If yes, increment counts[k] by 1.
3. If all submissions pass, return "YES".

Yes, this seems right. Because when a participant submits a new solution with x, that x must be exactly equal to the number of previous unique solutions (so the count before processing this submission). Then, this submission adds a new unique one, so the count increases by 1.

Now, considering the constraints. n can be up to 1e5, and k can be up to 1e5. The dictionary approach should handle this efficiently, as each operation (lookup and update) is O(1) average case. So for 1e5 operations, this should be manageable within the time limit.

Now, let's test this logic against the examples.

First example:
Input:
2
0 1
1 1

Processing:
First submission (0,1). For k=1, counts is 0, so 0 == 0: yes. Then counts[1] becomes 1.
Second submission (1,1). Current count is 1. 1 ==1: yes. counts becomes 2. Output YES.

Second example:
4
0 1 → counts[1] is 0 → valid → counts[1] becomes 1.
1 2 → counts[2] is 0, but x is 1. So invalid. So the output would be NO. Wait, but in the example, the output is NO. Let me check the input:

The second input is:
4
0 1
1 2 → x is 1, k=2. counts for 2 is 0. 1 !=0 → invalid. So the program would return NO here. Which matches the example.

Third example:
4
0 1 → counts[1] becomes 1.
1 1 → check 1 vs counts[1] (1). Yes. counts becomes 2.
0 1 → counts[1] is 2, but x is 0. So invalid? Wait, no. Wait, the third line is (0,1). So when processing it, the current count for k=1 is 2. So x is 0. 0 != 2. So this would return NO. But the example output is YES. Wait, what's the third example input?

Wait the third input is:

4
0 1 → valid (count becomes 1)
1 1 → valid (count becomes 2)
0 1 → x is 0. counts is 2. 0 !=2 → invalid. But the output is YES. Wait, no. Wait the third example's input is:

Looking back:

Third example input:
4
0 1
1 1
0 1
0 2

Processing:

First submission (0,1): valid. count[1] =1.

Second (1,1): count is 1. So 1 ==1. Valid. count becomes 2.

Third (0,1): x is 0. count is 2. 0 !=2 → invalid. But the sample output is YES. Wait, that's conflicting. Hmm, maybe I misunderstood the problem statement.

Wait, perhaps I'm misunderstanding x. Let me re-read the problem statement.

Ah, problem statement says:

Each solution is characterized by x and k. x is the number of different solutions sent before the first occurrence of this solution. So for a submission (x, k), x is the number of previous unique submissions for k that were made before the first occurrence of this solution. But the current submission is identical to the first occurrence. So if a participant k sends the same solution multiple times, all those subsequent submissions have the same x as the first one.

But the chronological order requires that if a submission (x, k) is present in the list, then the first occurrence of that solution (the one that made x=number of previous unique) must have come earlier, and all prior submissions of that participant must have exactly x-1, x-2, etc.

Wait, the key point is that for a submission (x, k), the testing system must have already stored a submission (x-1, k) for the same k, because that's the condition for the chronological order. But no, the problem states:

The problem requires that the data is stored in chronological order. So for each submission (x, k) in the list, the x must equal the number of unique solutions that participant k had before this submission. Because when the submission is made, x is the count of previous unique solutions (for the first occurrence of this solution). So all subsequent duplicates of this solution (same code) will have the same x, but the x must be exactly the count of unique solutions that k had before the first occurrence.

Wait, that's the crux. So if a participant submits a solution that is a duplicate, but the x is not equal to the current count of unique solutions at the time of the first occurrence, then it's invalid. Because all duplicates of a solution must have the same x as the first occurrence. So for example, the first time a solution is sent by k, x is equal to the current count of unique solutions. Then, any duplicates of that solution (sent later) must have the same x. However, the problem says that the data is stored in chronological order. So each submission in the list is processed in order. For a submission (x, k), if it's the first occurrence of this solution, then x must equal the number of unique submissions k has made before. If it's a duplicate, then x must be equal to the x of the first occurrence. Because duplicates must have the same x as the first occurrence.

Wait, but the problem says "if the testing system has a solution with x (x>0) of the participant k, then there must be a solution with x-1 of the same k stored before".

Wait, that's part of the problem statement. So the data is in chronological order if for every (x, k) where x>0, there exists a submission (x-1, k) that comes before it (not necessarily immediately) in the list.

But how does that fit with the x being the count of unique solutions before the first occurrence?

Alternatively, the problem is to check that for each submission (x, k), the following holds: if x>0, then the participant k must have already made exactly x unique submissions prior to this one. Because for the first occurrence of a solution, x must be the count of previous unique solutions. For duplicates of that solution, x must be the same as the first occurrence, but that x must have been valid at the time of the first submission.

But the problem states that all identical solutions have the same x. So, in the list of submissions, whenever a solution is the same as a previous one (same code), its x is equal to the x of the first occurrence of that solution.

But when we check the data for chronological validity, we need to ensure that for each submission (x, k) in the list, the following holds: the number of unique solutions that participant k had before this submission is exactly x. Because the x is determined at the time of the first submission of that solution, and duplicates must have the same x. However, the chronological order requires that when a submission (x, k) is made (the first occurrence), there were exactly x previous unique submissions from k. Then, when duplicates of that solution are submitted, the x remains the same. But the problem's data is the list of all submissions, including duplicates, and we need to check that each submission (including duplicates) has x equal to the number of unique submissions that k had before the first occurrence of this solution. However, the problem statement says that the data is in chronological order. So when a duplicate is processed, the x for that duplicate must equal the x of the first occurrence, but also the x of the first occurrence must have been valid when the first occurrence was processed.

So how do we model this? Because the duplicates' x must match the x of their first occurrence, and the x of the first occurrence must have been valid at the time.

So for each submission in the list, if it's the first occurrence of a solution (i.e., the first time a particular code is submitted by k), then x must equal the current count of unique submissions from k. Then, any subsequent duplicates of that solution must have x equal to that same x.

But how do we track which solutions (code) have been submitted before? Because the problem doesn't give us the code, only x and k. So how can we know if a submission (x, k) is a duplicate of a previous one?

Wait, the problem says that if a participant sends the same code multiple times, all those submissions (including the first) have the same x. But how can x be the same for all of them? Because the first submission's x is the count of previous unique submissions. Then, when the same code is submitted again, the x must be the same as the first time. So for example, the first submission (0, 1) is a new code. Then the same code is submitted again, so x is 0 again. But according to the problem statement, the data must be in chronological order, which implies that after the first submission, the participant has 1 unique submission. So when they submit the same code again, the x is 0, but the current count of unique submissions is 1. So this submission would be invalid, because x (0) must equal the count (1) at the time of submission.

But that's a contradiction. Wait, perhaps I'm misunderstanding the problem.

Let me re-read the problem statement carefully.

Problem Statement:

Each solution A is characterized by x and k. x is the number of different solutions that are sent before the first solution identical to A. So all identical solutions have the same x. So when a solution is submitted for the first time, x is equal to the number of previous unique solutions from k. Then, when the same solution is submitted again (duplicate), x is the same as in the first submission.

The problem says that the data must be in chronological order, which requires that if there is a solution (x, k) in the data with x>0, then there must be a solution (x-1, k) before it. So this implies that for the first occurrence of a solution with x= m, there must be m previous unique solutions from k. The subsequent duplicates of that solution will have x= m, but when they are processed, the current count of unique solutions from k is already m+1 (since the first submission of this solution increased the count to m+1). So processing a duplicate submission (x= m, k) after that would require that m equals the current count of unique solutions (which is m+1). But that's impossible, unless m is x+1. Wait, this is confusing.

Alternatively, perhaps the problem is that the x for a submission (including duplicates) must equal the number of previous unique submissions made by k before the first occurrence of that solution. So for example, the first time a solution is submitted (x= m), then m is the count of previous unique submissions. Then, any duplicates of that solution have x= m. But when processing the duplicates, the x is m, but the current count of unique submissions for k could be higher. However, the problem's data is considered valid if for each submission (x, k), the x is the number of unique submissions that k had before the first occurrence of that solution. But the chronological order condition requires that the first occurrence's x is valid, and the duplicates' x is the same, but their position in the list is allowed even if the current count is higher.

Wait, no. The problem statement says that the data is stored in chronological order, and the chronological order requires that if there is a solution with x>0 of k, then there's a solution with x-1 of k before it. So for example, the first occurrence of (x=3, k=5) must be preceded by x=2, x=1, x=0 for k=5. But the duplicates of (x=3, k=5) can appear after the first occurrence. But when processing the duplicates, the x=3 must be equal to the count of unique submissions from k=5 at the time of the first occurrence. However, the problem's check is to make sure that each submission (x, k) in the list meets the condition that when it was submitted, the number of unique solutions from k before that submission was exactly x.

Wait, perhaps the key point is that for each submission in the list (whether it's the first occurrence of a solution or a duplicate), the x must be equal to the number of unique solutions from k that were present before this submission. So even if it's a duplicate, x must be equal to the count of unique solutions that k had before this submission.

But that can't be the case. Because duplicates are allowed. For example, in the first example:

Input:
0 1 → count becomes 1.
1 1 → x=1 must be equal to count (1). Then count becomes 2.

But if there's a duplicate submission (x=0, k=1) after the first two submissions, then x is 0. But the count before this submission is 2. So x=0 would not equal 2, making the submission invalid.

So the problem requires that for every submission in the list, x must be equal to the number of unique submissions from k before that submission. If it's a duplicate, then x must equal that count. But in reality, duplicates of a previous solution should have x equal to the x of the first occurrence, which may not match the current count. So how can this be possible?

This is a contradiction unless the problem's actual condition is different. Let's re-examine the problem statement.

Problem statement:

"We know that many participants use random numbers in their programs and are often sent several solutions with the same source code to check."

So, the same source code is sent multiple times. Each submission (same code) has the same x. Because x is the number of previous unique solutions before the first occurrence of that code. So, for example, when a code is first submitted (x= m), then for any subsequent submissions of the same code, x must be m. However, the chronological order is that the data must be stored in the order of submission. So, when the first submission is processed, x must be m, which equals the count of unique solutions from k before that submission. Then, the count increases by 1. When the same code is submitted again, x is m, but the current count of unique solutions from k is m+1. So, in this case, the x of the duplicate submission (m) is not equal to the current count (m+1), which would make the submission invalid, and thus the data is invalid.

But according to the problem statement, duplicates are allowed. So how can the data be valid when duplicates have x not matching the current count?

Ah, perhaps I'm misunderstanding the problem. Let's re-read the problem statement's description of x:

"x is the number of different solutions that are sent before the first solution identical to A."

So, for a solution A, x is the number of previous unique solutions sent by the same participant before the first occurrence of A. So, for the first occurrence of A, the x is correct. For subsequent duplicates of A, x remains the same. However, the problem's data must be in chronological order. So, when a duplicate submission is made, the x must be equal to the number of unique solutions sent by the participant before the first occurrence of A. But the problem's check is to verify that, for each submission in the list, when that submission was made, the x for that submission was correct.

But for duplicates, when they are submitted, the x may not match the current count of unique submissions. However, the problem's data is valid if the x of the first occurrence of a solution is correct, and all duplicates have the same x as the first occurrence. But the problem's check is that each submission in the list (including duplicates) must have x equal to the number of unique submissions that the participant had before that submission.

Wait, that can't be. Because in the case of duplicates, when they are submitted, the participant may have submitted more unique solutions since the first occurrence of the solution. So the x would not equal the current count.

So this suggests that the problem is not possible to have duplicates in the data. But the problem statement says that participants do send duplicates, but the data must be stored in chronological order, which includes the duplicates. So how to reconcile this?

Ah, perhaps the x for a duplicate submission is not checked against the current count of unique submissions. Instead, the x for a duplicate submission must be equal to the count of unique submissions that existed before the first occurrence of that solution. And the chronological order requires that all the previous submissions required by the x of that solution exist.

But the problem says that the data is in chronological order if, for each submission (x, k), the following holds: if x>0, then there is a submission (x-1, k) before it. So, this is a way to check that the x is valid without tracking the counts.

Wait, maybe the correct approach is to track for each participant k the maximum x value seen so far, and for each submission (x, k), we check if x is equal to the current maximum x for k, and then increment the maximum x. Because, each submission (x, k) must be the next in the sequence.

Wait, but that's similar to the initial approach. Because the first occurrence of a solution would have x equal to the current count. Then, any duplicates would have x equal to some previous count. But according to the problem statement's constraints, how can a submission (x, k) be valid if x is not equal to the current count?

But according to the first example, which includes a submission (0,1) followed by (1,1), which is valid.

Another example: If a participant k=1 submits (0,1) (valid, count becomes 1), then submits another (0,1) (the same solution again), then x is 0, which would not equal the current count (1). So this submission is invalid, and the data is invalid.

But in the third example:

Input:
4
0 1 → count becomes 1.
1 1 → count becomes 2.
0 1 → x=0, current count is 2 → invalid. But the sample output is YES. So this suggests that my initial approach is incorrect.

Wait, the third example's input is:

4
0 1 → count=0 → x=0: valid. count becomes 1.
1 1 → x=1: current count is 1 → valid. count becomes 2.
0 1 → x=0: current count is 2 → invalid. So the sample output should be NO, but according to the example, the output is YES. So there must be a misunderstanding here.

Wait, looking back at the third example:

Third input:

4
0 1
1 1
0 1
0 2

Sample output is YES.

Processing according to the initial approach:

Submission 1: x=0, k=1 → counts is 0 → valid. counts[1] becomes 1.

Submission 2: x=1, k=1 → counts is 1 → valid. counts becomes 2.

Submission 3: x=0, k=1 → counts is 2 → 0 !=2 → invalid. So according to this logic, the third submission is invalid, so the answer should be NO. But the sample output is YES. So there's a conflict here. Which means my initial understanding of the problem is wrong.

So this suggests that my initial approach is incorrect. Therefore, I must re-examine the problem statement.

Ah! The problem says that x is the number of previous unique solutions before the first occurrence of this solution. So for duplicates, x is not necessarily the current count, but the count at the time of the first occurrence. So when a duplicate submission is made, x is allowed to be equal to the count that was valid when the first occurrence was processed. But how can we check this?

For example, the third submission in the third example is (0,1). This is a duplicate of the first submission (0,1). So the x here is 0, which was the count at the time of the first submission. But when processing the third submission, the current count for k=1 is 2. So according to the problem's logic, the submission is valid even though x=0 is not equal to the current count. Because x is fixed as the count from the first occurrence.

But how do we model this? Because the problem requires that the data is in chronological order, which means that for each submission (x, k), the x must be equal to the number of unique submissions from k before the first occurrence of this solution. Also, the x must be valid (i.e., the first occurrence must have x equal to the count at that time). So the problem is to check that for each submission (x, k), there exists a first occurrence of that solution (with x equal to the count at that time), and that any duplicates of that solution also have x equal to that value.

But how can we track which (x, k) pairs have been seen before (i.e., their first occurrence was processed)?

So the approach would be:

For each participant k, keep track of the set of x values that have been previously processed as first occurrences. For a submission (x, k):

- If this is a new solution (i.e., the x has not been seen for k before), then x must be equal to the current count of unique submissions for k. Then, we add x to the set for k and increment the count.

- If this x has been seen before for k (i.e., it's a duplicate of a previous solution), then it's allowed, and the count remains the same. But the x must have been valid when it was first added.

So the data structure for each k would be a set of x's that have been encountered as first occurrences. For a submission (x, k):

If x is not in the set for k:

   Check if x equals the current count. If yes, add x to the set and increment the count.

Else:

   If x is in the set, then it's valid, but the count doesn't change.

Wait, but how does the count change? Because each first occurrence increases the count by 1. Duplicates do not increase the count.

So the count for k is the number of unique solutions they have submitted. The set for k contains all the x's of the unique solutions. So the count is equal to the size of the set.

So for a submission (x, k):

If x is not in the set:

   Check if x equals the size of the set (current count). If yes, add x to the set (increasing count by 1).

   If no, then invalid.

If x is in the set:

   It's a duplicate. So x is valid, but the count remains the same.

So this approach would handle both first occurrences and duplicates correctly.

Let's test this on the third example:

Third example:

Submissions:

1. 0 1 → set is empty. x=0 is not in set. Current count (size of set) is 0. 0 ==0 → valid. Add to set. Set size becomes 1.

2. 1 1 → x not in set. Current count is 1. 1 ==1 → valid. Add to set. Size becomes 2.

3. 0 1 → x=0 is in the set. So valid. Do not add to set. Count remains 2.

4. 0 2 → x=0 not in set for k=2. Count (size of set for k=2) is 0. 0 ==0 → valid. Add to set. Count becomes 1.

All submissions are valid. So output is YES. Which matches the sample.

Ah! So this is the correct approach. The initial approach was incorrect because it considered all submissions (including duplicates) to require that x equals the current count. But duplicates can have x equal to any value that was previously added to the set for k. So the correct way is to track for each k the set of x's that have been added as first occurrences, and the count is the size of that set. For a new submission (x, k):

If x is not in the set:

   Check if x equals the size of the set. If yes, add x to the set.

   Else, invalid.

If x is in the set:

   It's a duplicate, so valid.

So this model correctly handles duplicates, as their x is already in the set, indicating that the first occurrence was valid.

So the data structures needed are:

A dictionary, say 'max_x' which maps each k to the count of unique submissions (size of their set). But we don't need to store the set; instead, since the x's must be consecutive and start from 0, each new x for k must be exactly equal to the current count. For example, if the first submission is x=0, which is added. Then next must be x=1, added. Then x=2, etc. So the set for k is {0,1,2,...}, which forms a consecutive sequence. Therefore, the count for k is the maximum x in the set plus 1. Wait, no. Wait, if the set for k is {0,1,3}, that's not consecutive. Then the count would be 3 (size of set), but the next submission must have x=3. So perhaps the set must be exactly {0,1,2,..., m} where m is the count-1.

Wait, because for the first occurrence submissions for k:

The first submission must have x=0. The second must have x=1, which is the new count. The third x=2, etc. Because each new submission (first occurrence) must have x equal to the current count. So the x's for first occurrences must be 0,1,2,... in order. So the set for k is exactly the numbers from 0 to current count-1. So for example, if the count is 3, the set is {0,1,2}. So the next first occurrence submission must have x=3.

Therefore, for a participant k, the current count is the number of unique solutions, which is the size of the set, and each new x must be equal to the current size. So the set is {0, 1, 2, ..., m-1} where m is the count.

So for a submission (x, k):

If it's a first occurrence (x not in the set):

   x must equal the current count (m). Then, m increments by 1.

If it's a duplicate (x is in the set):

   Valid.

So the data structure can be simplified. For each k, we can track the current count m (number of unique submissions), and for a submission (x, k):

- If x < m and x is in the set (i.e., x is part of the existing unique submissions):

   It's a duplicate. Valid.

- If x == m: new unique submission. Valid. Increment m.

- Else: invalid.

Wait, but how do we track which x's are already part of the unique submissions for k? Because for the initial approach, the set for k is {0,1,...,m-1}. So any x in this set is considered part of the unique submissions, and any submission with x in this set is a duplicate. Therefore, when processing a submission (x, k):

if x is in {0,1,...,m-1}: it's a duplicate. Valid.

elif x == m: new unique. Valid. m increments.

else: invalid.

So for each k, we can track m (the current count), and for a submission (x, k):

if x is equal to m → valid, increment m.

elif x < m → valid (duplicate).

else → invalid.

This is a much simpler approach. Because the x must be <= m. If x is m, it's a new unique submission. If x is less than m, it's a duplicate.

So this approach requires that for each submission (x, k):

x <= current count for k.

If x is equal to the current count → new unique, increment count.

Else, x must be less than the current count → duplicate, allowed.

But why is this correct?

Because the first time a solution is submitted, its x must be equal to the current count m (the number of previous unique submissions). Then, the count becomes m+1. Any duplicates of that solution will have x=m, which is less than the new count. So when processed, x will be less than the current count. But according to the problem statement, duplicates are allowed and have the same x as the first occurrence.

So this approach seems to handle all cases correctly.

Let's test this with the third example:

Third example:

k=1 starts with m=0.

Submission 1: (0,1). x=0 == m=0 → valid. m becomes 1.

Submission 2: (1,1). x=1 == m=1 → valid. m becomes 2.

Submission 3: (0,1). x=0 < m=2 → valid. m remains 2.

Submission 4: (0,2). x=0 == m=0 for k=2 → valid. m for k=2 becomes 1.

All valid → output YES. Which matches the sample.

Another example: 

Sample input 2:

4
0 1 → m=0 → valid. m becomes 1.
1 2 → m for 2 is 0. x=1 is not equal to 0. → invalid. Output NO.

Sample input 1:

2
0 1 → m=0 → valid. m=1.
1 1 → x=1 == m=1 → valid. m=2. Output YES.

Another test case:

Submission (0,1), then (0,1) again. For k=1:

First submission: x=0 == m=0 → valid. m=1.

Second submission: x=0 < m=1 → valid. So the data is valid. Output YES.

But according to the initial approach (where x must equal current count), this would have been invalid. But according to the revised approach, it's valid. Which aligns with the problem's third example.

So the correct approach is:

For each k, track the current count m of unique submissions.

For each submission (x, k):

   if x > m → invalid.

   elif x == m → increment m.

   else (x < m) → valid.

So this approach correctly handles duplicates, which have x < m.

This is a much simpler approach and requires only a dictionary to track m for each k. For each submission, we check if x is <= m. If x is exactly m, increment m. Otherwise, if x < m, it's valid.

This is O(1) per submission, which is efficient for 1e5 submissions.

So the code would be:

Initialize a dictionary, say 'count', default 0 for any new k.

For each submission (x, k):

   current = count.get(k, 0)

   if x > current:

       print 'NO'

       exit

   elif x == current:

       count[k] = current + 1

   else:

       pass

After processing all, print 'YES'.

Yes. This approach is correct.

Testing this on the third example:

Submission 3: x=0 for k=1. current is 2. 0 < 2 → valid.

Yes.

Another test case where a submission is a duplicate but x is valid.

This approach works.

So the code will read n, then for each of the n lines, read x and k.

We can implement this in Python as follows:

Use a dictionary (defaulting to 0), and for each x and k:

current = counts.get(k, 0)

if x > current: invalid.

elif x == current: counts[k] +=1.

else: valid.

So the code is:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    counts = {}
    for _ in range(n):
        x, k = map(int, input_stream.readline().rstrip("\n").split())
        current = counts.get(k, 0)
        if x > current:
            print("NO", file=output_stream)
            return
        elif x == current:
            counts[k] = current + 1
    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
0 1
1 2
1 1
0 2
""",
            "output": \
"""\
NO
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

</think>

```python
n = int(input())
counts = {}
for _ in range(n):
    x, k = map(int, input().split())
    current = counts.get(k, 0)
    if x > current:
        print("NO")
        exit()
    elif x == current:
        counts[k] = current + 1
print("YES")
```
