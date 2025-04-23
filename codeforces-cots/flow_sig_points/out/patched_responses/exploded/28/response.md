<think>
Okay, so I've got this problem to solve. Let me read through it carefully to understand what's being asked.

The problem is about Natasha planning an expedition to Mars for n people. The key thing is providing food. Each participant must eat exactly one food package each day, and they all have to eat the same type of food every day. Different participants can have different types, but each one's type has to be consistent across all days.

The warehouse has m food packages, each of a certain type a_i. The goal is to find out the maximum number of days the expedition can last, given these constraints. The output is the maximum possible days, or 0 if not even one day is possible.

Hmm. So, the main question is: how many days can all n participants be supplied, given that each participant's food type must have enough packages to cover all the days. For each day, each participant needs one package of their chosen type. So, if a participant is assigned a type that has k packages, they can contribute up to k days. But the total days for all participants must be the same. Wait, no. Wait, no, the days that the expedition can last is the minimum of the number of days each participant's food can support. But wait, no. Because all participants must have enough food for the same number of days. Because the expedition lasts for d days, so each participant must have exactly d packages of their type. So for each participant j, if they are assigned a food type with count c, then c must be >= d. So the total number of participants that can be assigned to a particular food type with count c is floor(c / d), but sum of all (floor(c_i / d)) across all food types) must be >= n.

Wait, yes. Because each food type contributes some number of participants: for example, if a food type has 5 packages and the expedition lasts 2 days, then each participant using this food would need 2 packages, so 5//2 = 2 participants can be assigned this food (using 4 packages, leaving 1). So the sum over all food types of (count_i // d) must be >= n. The maximum d where this is true.

So the problem reduces to finding the largest possible d such that the sum over all (count_i // d) is >= n.

Yes! That's the key insight. So the steps are:

1. Count the frequency of each food type. For example, if the input is [1,5,2,1,1,1,2,5,7,2], then the counts are:
1:4, 2:3,5:2,7:1.

Wait, let's see. The given example input is 4 participants, m=10. The counts for each type would be 1 appears 4 times (indices 0,3,4,5?), wait let me check: the second line is 1 5 2 1 1 1 2 5 7 2. So the counts are:
1: 1, 5:2 (positions 1 and 7?), 2:3 (positions 2,6,9?), 1: positions 0,3,4,5. Wait, no. Let me count again. The second line is 1,5,2,1,1,1,2,5,7,2. So:

1 appears at positions 0,3,4,5 → 4 times.
5 appears at positions 1,7 → 2 times.
2 appears at positions 2,6,9 → 3 times.
7 once.

So counts are 4,2,3,1. Then for the first example, the maximum d is 2. Let's see: sum over (count // 2) for each type. 4//2=2, 2//2=1, 3//2=1, 1//2=0. Sum is 2+1+1=4, which is equal to n (4). So yes, that's why d=2 is possible.

So the approach is to find the maximum d such that the sum of (count_i // d) across all food types is >= n.

So how do we find this d efficiently?

Constraints: n and m are up to 100. Each a_i is up to 100. So the maximum possible d is up to the maximum count of any food type. For example, if a food type has 100 packages, then d can be up to 100. But for each d from 1 up to max_count, check if sum of (count//d) across all counts is >=n.

But given that m is up to 100, and for each d up to 100, checking is O(m) per d, which is acceptable. So the total time is O(m * max_count), which for m=100 and max_count=1e4 (if a_i is up to 1e5, but in the problem a_i is up to 100) is manageable.

Wait, but the problem says a_i is up to 100. So the maximum possible count for any food type is 100 (if all m packages are the same, m=100). So the maximum possible d is 100. So the total iterations would be 100 (d from 1 to 100) multiplied by m (100), which is 1e4 operations. That's very manageable.

So the plan is:

1. Count the frequency of each food type. So create a frequency dictionary (like a Counter) for the given list.

2. Get all the counts (the values in the Counter), let's call them counts.

3. For d in possible days, check if sum( (c // d) for c in counts ) >= n. The maximum d where this is true is the answer.

But what's the possible range for d? We can start from 1 up to the maximum possible possible d.

What's the maximum possible d? The maximum possible is when a single food type has all the packages. So for example, if all m packages are of the same type, then the maximum d is floor(m / n). Wait, no. For example, in the third sample input:

n=2, m=5, packages [5,4,3,2,1]. Each type occurs once. So counts are all 1. For d=1: sum(1//1) for all 5 types is 5, which is >=2. So d=1 is possible. Which is the correct answer.

Another example: fourth input, 3 people, 9 packages all 42. Count is 9. For d=3: 9//3=3, sum is 3 >=3. So answer is 3.

So the maximum possible d is the maximum count divided by 1 (if sum is sufficient), but perhaps higher when other counts contribute.

But to find the maximum possible d, we can iterate d from 1 up to the maximum possible possible value, which is (sum of all counts) // n. Wait, but sum of counts is m, since each package is counted once. So m must be >= n * d, because each of the n participants requires d packages (for d days). So the maximum possible d is floor(m /n). Because if m <n, then even for d=1, you can't have n packages. So the maximum possible d is floor(m/n). But that's only if the sum of (count_i//d) is >=n. Wait, no. For example, if m is 10, n=4. Then 10/4 is 2.5 → 2. Which is the case in the first example, where d=2 is possible. But if the counts are such that even when d is floor(m/n), the sum of count_i//d could be less than n.

Wait, but m is the total number of packages. So in order to have d days, each participant needs d packages, so total required is n*d. So m must be >=n*d. Thus, the maximum possible d is floor(m /n). But this is a necessary condition, not sufficient. Because even if m >=n*d, if the packages are spread across many types, sum of (count_i //d) may be less than n.

For example, in the third sample input: m=5, n=2. 5 >=2*d → d can be up to 2. But when d=2, sum of (1//2) for all 5 types is 0, which is <2. So the maximum d is 1, which is floor(5/2)=2's floor is 2 but it's not possible. So the maximum possible d is the minimum between the maximum possible (floor(m/n)) and the maximum d where sum >=n.

So the approach is to check all possible d from 1 to floor(m/n) (inclusive), and find the maximum d where sum of (count_i//d) >=n.

If m <n, then even d=1 is impossible, because sum of (count_i//1) is sum of count_i = m <n. So the answer is 0.

So the steps are:

- If m <n → output 0.

Else:

- Compute the maximum possible d as floor(m/n).

- Iterate d from that maximum down to 1, and for each d, compute sum of (count_i //d). The first d where sum >=n is the answer.

- If none found, output 0.

This way, we start checking from the largest possible d (floor(m/n)), which is the upper bound. Once we find the first d that satisfies sum >=n, that's the maximum possible d.

This approach is efficient because in the worst case, floor(m/n) could be up to 100 (if m=100 and n=1). So even if we loop from 100 down to 1, checking each step, it's 100 iterations. Each iteration involves summing over all counts (up to m=100 elements). So 100 * 100 = 1e4 operations, which is acceptable.

So the plan is:

1. Read n and m.

2. Read the array a.

3. If m <n → output 0.

4. Else, compute frequency counts of each type.

5. max_possible_d = m //n.

6. For d in range(max_possible_d, 0, -1):

   a. For each count in the frequency counts, compute count //d.

   b. Sum them all.

   c. If sum >=n → return d.

7. If none found → return 0.

Wait, but in step 5, for example, if m =n, then max_possible_d is 1. But what if all counts are 1? Then sum of (1//1) for all n counts is n, which is >=n. So d=1 is possible. Correct.

Another example: in the third input:

n=2, m=5. m//n=2. For d=2, each count is 1. sum(1//2) for 5 elements is 0. So not enough. So loop to d=1. sum(5//1) is 5 >=2. So answer is 1.

So yes.

Now, code steps:

In Python:

Read n and m.

If m <n: print(0) and exit.

Else:

Read the list of a_i.

counts = a list of the counts of each unique food type (using collections.Counter).

max_d = m //n

for d in range(max_d, 0, -1):

   total = sum(c //d for c in counts.values())

   if total >=n:

       print(d)

       exit()

print(0)

Wait, but in the case where m >=n but the sum of (count_i//d) is never >=n for any d in 1..max_d. For example, if all counts are 1 and m >=n but sum(1//d) for d=1 is sum(1) which is m. So if m >=n, then for d=1, sum is m >=n. So in this case, the code would output 1.

But if, for example, all counts are 1, m=5, n=3. Then m//n=1. So d=1 is checked. sum(5//1) is 5 >=3 → yes, output 1.

So the code should handle all cases correctly.

Let's test the second sample input:

Input:

100 1 → m=1 <n=100 → output 0.

Third sample input:

n=2, m=5. m >=n, max_d=5//2=2. Check d=2: sum of 1//2 (each count is 1, 5 counts) → 0. Then d=1: sum 5, which is >=2 → output 1.

Fourth sample input:

n=3, m=9. All counts are 9. max_d=9//3=3. Check d=3: 9//3=3. Sum is 3 >=3 → output 3.

Yes.

Another test case: n=3, m=6. Suppose counts are [3,3]. sum for d=2: 3//2=1 and 3//2=1 → sum 2 <3. d=1: 3+3=6 >=3 → output 1.

So code is correct.

So the code seems to handle all cases.

Now, code implementation:

We can use collections.Counter to get the counts.

But in Python, even if the input is up to 100 elements, it's manageable.

So the code steps:

Read n, m from input. Then read the list of a's.

But the second line is a list of m integers.

In code:

n, m = map(int, input().split())

a = list(map(int, input().split()))

if m <n:

    print(0)

else:

    from collections import Counter

    counts = Counter(a)

    max_d = m //n

    for d in range(max_d, 0, -1):

        total = 0

        for c in counts.values():

            total += c //d

            if total >=n:  # early exit

                break

        if total >=n:

            print(d)

            exit()

    print(0)

Wait, but even better: during the summation, once total >=n, we can break early. So in the code, for each c in counts.values(), add c//d to total. If at any point total >=n, break and return yes.

This could save some iterations. For example, if the first few counts contribute enough, we don't need to check the rest.

Yes. So that's an optimization. So in the loop:

total =0

for c in counts.values():

    total += c//d

    if total >=n:

        break

if total >=n: → yes.

So the code is more efficient.

This is especially useful when counts are large. For example, if there's a count that is very large, like 1e5, then for d=1, each count//d is the count itself. So the sum could reach n quickly.

Thus, adding the early exit is a good idea.

Now, let's test with the first sample input:

n=4, m=10 → max_d=10//4=2. For d=2:

counts are 4 (type 1), 2 (type5?), 3 (type2?), 1 (type7). Wait, the counts from the first sample are:

Looking at the input:

1 5 2 1 1 1 2 5 7 2 → sorted as [1,5,2,1,1,1,2,5,7,2]. So Counter would be {1:4, 5:2, 2:3,7:1}.

counts.values() → [4,2,3,1] (order may vary, but in Python 3.7+ Counter preserves insertion order. However, the order does not matter here).

For d=2:

4//2=2, sum is 2. Then 2//2=1 → sum 3. Then 3//2=1 → sum 4. At this point, sum is 4 which is >=n=4. So loop breaks. So returns 2.

Yes.

So the code works.

Another test case: n=3, m=9. counts is [9]. For d=3: 9//3=3 → sum 3 >=3. So output is 3.

Another case: n=2, m=5. counts are [1,1,1,1,1]. For d=2, each 1//2=0. sum is 0. Then check d=1: each 1//1=1. sum after adding all 5 is 5 >=2. So output 1.

So code works.

So the code is correct.

Now, implement this in Python.

But we need to make sure that the code reads the input correctly, and that for the case m <n, we output 0.

Also, the code should not have any debug prints.

So the code is as follows.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
if m < n:
    print(0)
else:
    from collections import Counter
    counts = Counter(a)
    max_d = m // n
    for d in range(max_d, 0, -1):
        total = 0
        for c in counts.values():
            total += c // d
            if total >= n:
                break
        if total >= n:
            print(d)
            exit()
    print(0)
```