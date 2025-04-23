<think>
Okay, let's try to figure out this problem. So the problem is about finding the minimum number of stolen utensils after a dinner where each guest ate the same number of dishes. The key points here are understanding the structure of the utensils and how they were distributed.

First, let's restate the problem. We have a list of remaining utensils. We need to determine the minimal possible stolen utensils based on the possible original setup. The original setup must be such that every guest had the same number of dishes, and each dish comes with a set of utensils. Each set is the same, and each type in a set is unique. So, for example, if a set is {1,2,3}, then each dish for each guest has exactly these three utensils. So, if a guest had two dishes, they would have two sets: two of each type 1, 2, 3.

So, the stolen utensils are the original total minus the remaining ones.

The approach here is to find out what's the possible original set size (number of utensils per set) and the number of dishes per guest (let's call it m), then compute the minimal stolen utensils.

But how do we model this?

Let's break it down:

1. The original set of utensils is some subset S of the types. Each set is the same, so all dishes use the same S. The remaining utensils must be a subset of S, because any type not in S couldn't have been in the original setup. Wait, but the problem says that the remaining utensils could have some types that are not part of the original sets. No, wait, no. Because the problem states that "every set of utensils is the same and consists of different types of utensils". So the remaining utensils must all be part of that set. Because any utensil not in the original set S would not have been present. Wait, the note in the second example says that some types (like 2 and 4) may not be present in the set. But in the example input, the remaining utensils include 1,3,5,5,100. Wait, the original set could have some types, and the stolen utensils are the ones missing from the remaining. So the stolen ones are from the original set. But the remaining utensils can include types not in the original set? Wait, no. Because the original sets consist of the same set of utensils. So all utensils that were present in the dinner are part of this set. Because each set served is the same. So any remaining utensil must be part of the original set. Otherwise, where did it come from?

Wait, the problem statement says: the list of all utensils left. So the remaining utensils are all those that weren't stolen. But the original setup only includes utensils from the set S. So any utensil left that's not in S would imply that S included that type, which contradicts the original setup.

Wait no. Wait, the original setup is that each set is the same. So all utensils in the original setup are part of that set. So any remaining utensil must be part of the set. Because otherwise, they were not part of the original setup. So the problem's first step is that the original set S must include all types present in the remaining utensils. Because if a remaining utensil is of a type not in S, then that's impossible because all original utensils are from S.

So first, S must be a superset of the unique types in the remaining utensils. Because the remaining utensils can't have types not present in the original set.

So, the first thing we can determine is that the original set S must consist of exactly the unique types present in the remaining utensils. Or perhaps a larger set? Wait, no. Because the problem says that the set S is the same for every dish. So any utensil of a type not in S would not have been present in the original setup. So the remaining utensils must have types only from S. Therefore, the original set S must include all the types present in the remaining utensils. However, S can include additional types (which would have been present in the original sets but all were stolen, so they aren't in the remaining utensils).

Wait, no. Because if S has additional types (not present in the remaining), then those types were all stolen. Because in the original setup, each set has all the types in S. So, for example, if S is {1,2,3}, and each guest had m dishes, then the original number of utensils of each type in S is m * k. But if some of those were stolen, and in the remaining there are none of type 2, then all m*k utensils of type 2 were stolen. But the problem allows that.

So the original set S can have more types than those present in the remaining. But those types would have to have all their utensils stolen (since none are left). So, for example, in the first sample input:

5 2
1 2 2 1 3

The remaining utensils are types 1,2,3. So S must include at least these three. But S could be larger. However, adding more types to S would require that all of those additional types have all their original utensils stolen, which would add more stolen utensils. Since we want the minimal stolen, perhaps the optimal S is exactly the unique types in the remaining, because adding more types would require more stolen (all of those types' utensils).

So the minimal stolen would be achieved when S is exactly the set of unique types in the remaining utensils. Because adding more types to S would require all of those to be stolen, increasing the total stolen.

Thus, for the purpose of finding the minimal stolen, the original set S must be exactly the set of unique types present in the remaining utensils. Because any other choice of S (either a subset, which is impossible, or a superset, which increases stolen count) would not lead to a better solution.

So step one: compute the set S as the unique elements in the remaining utensils. Let s be the size of S, i.e., the number of different types in S.

Then, the original setup is that each of the k guests had m dishes. Each dish requires a set of s utensils (one of each type in S). So, for each guest, m dishes → m sets → m * s utensils per guest. But wait, each dish has one set. So each dish has s utensils (each type once). So per dish, s utensils. So per guest, m * s utensils. But since there are k guests, the total per type is m * k. Because each dish's set includes one of each type in S. So for each type in S, there are m * k utensils originally (since each of the k guests ate m dishes, each with one of that type).

Now, the remaining utensils for each type is a_i's count. Let's say for type t, the remaining count is c_t. Then, the original count for type t is m * k. So the stolen for type t is (m*k - c_t). But m must be such that m*k >= c_t for all t in S. Otherwise, it's impossible. Because you can't have more remaining than the original.

So, the problem reduces to:

Find the minimal possible stolen, which is sum over all types in S of (m*k - c_t) minus the sum of any other types in S (but we already considered S as the unique types in the remaining). Wait, no. Because S is the set of unique types in the remaining. So all other types in S (if any) must have their counts considered. Wait, no. S is exactly the unique types in the remaining. So all types in S are present in the remaining. So for each t in S, c_t is at least 1. So the original count for each t in S is m*k >= c_t.

So the steps are:

1. Compute S as the set of unique elements in the remaining utensils.

2. For each type t in S, compute the count c_t (how many are remaining).

3. Determine m (number of dishes per guest) such that m is a positive integer, and for all t in S, m*k >= c_t.

4. The minimal m is the minimal possible that satisfies m >= ceil(c_t /k) for all t in S. Because for m to be valid, m must be at least the maximum of ceil(c_t /k) for all t. Because m*k must be >= c_t. So m >= ceil(c_t/k). The minimal possible m is the maximum of these ceil values.

Wait, because for each type, m must be at least ceil(c_t /k). For example, if c_t is 5 and k is 2, then m must be at least 3, since 2*3=6 >=5. So the minimal m is the maximum of ceil(c_t /k) across all t in S.

Once m is determined, then the original total is (s * m * k). The stolen is original_total - sum of remaining utensils.

Because sum of remaining is sum(c_t for t in S). So stolen is s*m*k - sum(c_t).

So the minimal stolen is computed as s*m*k - sum(c_t), where m is the minimal possible m (the maximum of ceil(c_t/k) for each t).

But wait, the stolen could be minimized by choosing the minimal possible m. Because as m increases, the original total increases, thus stolen increases. Wait, no. If m increases, then original_total = s * m *k. sum(c_t) is fixed. So s*m*k - sum(c_t) increases as m increases. So to minimize the stolen, we need to find the minimal possible m that satisfies all constraints (m >= ceil(c_t/k) for all t in S).

So the problem reduces to:

Compute S as the set of unique elements in the input.

Compute for each t in S: c_t = count of t in the input.

Compute m_min = max(ceil(c_t /k) for all t in S).

The stolen is (s * m_min *k) - sum(c_t).

So that's the approach.

Now, let's test this against the examples.

First example:

Input:

5 2

1 2 2 1 3

The unique types are {1,2,3} → s=3.

Counts:

1: 2

2: 2

3: 1

k=2.

For each t:

ceil(2/2) = 1 (for 1 and 2)

ceil(1/2) = 1 (for 3).

So m_min is 1.

Original total: 3*1*2 =6.

Sum(c_t) = 2+2+1=5.

Stolen: 6-5=1. Which matches the first example.

Second example:

Input:

10 3

1 3 3 1 3 5 5 5 5 100

Unique types: {1,3,5,100} → s=4.

Counts:

1: 2

3: 3

5:4

100:1

k=3.

For each t:

ceil(2/3) → 1 (since 2/3 is 0.666, ceil is 1)

ceil(3/3)=1

ceil(4/3)=2 (since 4/3 is 1.333, ceil is 2)

ceil(1/3)=1.

So the maximum is 2 → m_min=2.

Original total:4*2*3=24.

Sum(c_t): 2+3+4+1=10.

Stolen:24-10=14. Which matches the second example.

So the approach seems correct.

So now the steps for the code:

1. Read n and k.

2. Read the list of a_i.

3. Compute S as the set of a_i, then convert to a list perhaps, but counts are needed.

4. For each t in S, compute the count c_t.

5. Compute m_min as the maximum of (ceil(c_t /k) for all t in S).

6. Compute original_total = len(S) * m_min *k.

7. sum_remaining = sum(c_t for t in S).

8. stolen = original_total - sum_remaining.

9. Output stolen.

But how to compute ceil(c_t /k) in Python? Because in Python, we can do (c_t + k -1) //k.

Yes. For example:

c_t=5, k=2: (5+2-1)//2 =6//2=3.

c_t=4, k=3: (4+3-1)//3=6//3=2.

Yes.

So code steps:

Read n, k.

Read list a.

counts = a frequency count.

s = len(counts.keys())

sum_remaining = sum(counts.values())

Compute m_min = max( (v +k -1) //k for v in counts.values() )

stolen = s * m_min *k - sum_remaining

print(stolen)

So that's the code.

Now, handling the input. Let's see.

In Python, using a Counter.

So the code would be:

from collections import Counter

n, k = map(int, input().split())

a = list(map(int, input().split()))

counts = Counter(a)

s = len(counts)

sum_remaining = sum(counts.values())

max_ceil = 0

for v in counts.values():

    current = (v + k -1) // k

    if current > max_ceil:

        max_ceil = current

stolen = s * max_ceil * k - sum_remaining

print(stolen)

Yes.

Testing with first example:

a is [1,2,2,1,3]

counts is 1:2, 2:2, 3:1.

s=3.

sum_remaining=5.

max_ceil for each v:

2 → (2 +2-1)/2 =3//2=1.

Same for 2 →1.

1 → (1+2-1)/2=2//2=1. So max_ceil is 1.

3*1*2=6. 6-5=1.

Second example:

counts are 1:2,3:3,5:4,100:1.

k=3.

for each:

2: (2+3-1)/3 =4/3=1.333 →1.

3: (3+3-1)/3=5//3=1 →1.

5:4 → (4+3-1)/3=6//3=2.

100:1 → (1+3-1)/3=3//3=1.

max_ceil is 2.

s=4, 4*2*3=24. sum_remaining is 2+3+4+1=10. 24-10=14.

Yes.

Edge cases.

Test case where n=0? But according to constraints, n is >=1. So no.

Another case: all counts are <=k, so m_min=1.

So stolen is s*k*1 - sum_remaining.

E.g., n=3, k=3, a=[1,2,3]. counts are 1 each. sum_remaining=3.

m_min is max(1,1,1) =1.

stolen is 3*3*1 -3=9-3=6. Which would be correct if each guest had one dish, 3 dishes total. Original is 3*1*3=9 (each of 3 types, 3 guests). So 9-3=6 stolen.

Another test case: if a utensil has a count that is exactly m*k.

E.g., n=2, k=2. a=[1,1]. counts: {1:2}.

m_min=ceil(2/2)=1.

original total:1*1*2=2. sum_remaining=2. stolen is 0.

Which is correct, as nothing stolen.

Another case: a utensil's count is zero. But according to the problem statement, the input is the list of remaining utensils. So counts can't be zero. So all counts are at least 1.

So code is correct.

So the code seems to handle all cases correctly.
</think>

```python
from collections import Counter

n, k = map(int, input().split())
utensils = list(map(int, input().split()))
counts = Counter(utensils)
s = len(counts)
sum_remaining = sum(counts.values())
max_ceil = 0
for v in counts.values():
    current = (v + k - 1) // k
    if current > max_ceil:
        max_ceil = current
stolen = s * max_ceil * k - sum_remaining
print(stolen)
```