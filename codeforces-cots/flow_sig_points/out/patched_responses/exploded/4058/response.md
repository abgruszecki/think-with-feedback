<think>
Okay, let's see. The problem is about finding the minimum cost for Vladik to travel from airport a to airport b, considering the companies each airport belongs to. Hmm. So, the cost between two airports depends on their company. If they're the same, cost is 0; otherwise, it's the absolute difference of their IDs. 

First, I need to find the minimal possible cost path from a to b. Let's think about the possible scenarios. 

Wait, the airports are arranged in a straight line, but the IDs might not be in order? Wait no, the IDs are from 1 to n, so they are in order. But the arrangement on the straight line might just be in order of their IDs, right? So, for example, airport 1 is next to 2, which is next to 3, etc. But the actual positions might not matter except for the distances calculated as |i-j|. 

The key point is the company each airport belongs to. Because when moving from airport i to j, the cost is zero if same company, else |i-j|. So, the problem reduces to finding the path from a to b where each step's cost is determined by the companies of the airports involved. 

But what's the optimal path here? Let's think. If a and b are the same, then cost is zero. That's straightforward. Otherwise, what's the minimal cost?

Let's consider the case where a and b belong to the same company. Then Vladik can just fly directly from a to b with cost zero. So the answer is zero. 

If a and b are different companies, then the direct flight would cost |a - b|. But maybe there's a cheaper path by going through other airports. For example, if there's an airport x that's the same company as a, and then from x to some other airport y that's same as b, and so on. Wait, but maybe switching companies once would be optimal. 

Wait, let's look at the first example. The input is 4 airports, a=1, b=4. The company string is 1010. So airports 1 is 1, 2 is 0, 3 is 1, 4 is 0. So a is company 1, b is company 0. So direct flight from 1 to 4 would cost |1-4|=3. But in the example, the optimal path is 1→2 (cost 1) and 2→4 (cost 0). So total cost 1. 

So the key here is that even though a and b are in different companies, by going through an airport in a different company (like 2 in this case), the total cost can be lower. 

Hmm. So the minimal cost when a and b are different companies is not necessarily |a - b|. It could be lower if there exists an airport in the same company as a but located closer to b, allowing a cheaper transition. 

Wait, but how do we model this? Since the cost between any two airports is determined by their company, the problem seems to resemble a graph where each node is an airport, and edges have certain weights. But with n up to 1e5, building such a graph is impossible. So we need a smarter approach. 

Let's think: the minimal cost can be either the direct cost (if a and b are different companies) or zero (if same). But the example shows that sometimes there's a cheaper path. So the minimal cost is the minimum between the direct cost and the minimal possible cost by switching companies once. 

Wait, maybe the minimal cost is either the direct cost (when a and b are different companies) or zero (same companies). But how do other paths factor in? 

Wait, suppose a and b are different companies. Then any path from a to b must involve at least one flight between different companies. Because to get from a's company to b's company, you need to switch. 

But each such flight between different companies adds |i-j| to the cost. So maybe the minimal cost is the minimal possible |i-j| where i is in a's company and j is in b's company, plus |i-a| (if i is in a's company) and |j -b| (if j is in b's company). Wait, no. Because if you fly a to i (same company, cost 0), then i to j (different, cost |i-j|), then j to b (same company, cost 0). The total cost would be |i-j|. So the minimal possible |i-j| where i is in a's company and j is in b's company. 

But in the first example, a is 1 (company 1), b is 4 (company 0). So looking for i in company 1 (like 1 and 3) and j in company 0 (like 2 and 4). The possible pairs are (1,2) → |1-2|=1, (1,4) →3, (3,2)=1, (3,4)=1. The minimal among these is 1. So the minimal cost is 1. Which matches the example. 

So the minimal cost is the minimal |i-j| where i is in a's company and j is in b's company. Because then the path would be a → i (free), i → j (cost |i-j|), j → b (free). 

But if a and b are in the same company, then the answer is 0. 

So the steps are:

1. Check if a and b are the same. If yes, cost is 0.
2. Else, check if the companies of a and b are the same. If same, cost is 0.
3. Else, find the minimal |i-j| where i is in a's company and j is in b's company. The minimal cost is the minimal such |i-j|. 

Wait, but in the example, a and b are different companies. So the answer is the minimal |i-j| between any pair of a's company and b's company. 

But then, the minimal possible |i-j| could be compared with the direct flight cost (which is |a-b|). Because perhaps taking the direct flight is cheaper than any i-j pair. 

Wait, no. Because in the direct flight, the cost is |a - b|, which is exactly the cost of the flight from a to b. But if there exists a pair i and j where |i-j| is less than |a - b|, then using that path would give a lower total cost. 

Wait, but the minimal possible |i-j| for any i in a's company and j in b's company would give a cost of |i-j|. So the minimal cost is the minimum between |a-b| and the minimal |i-j|. 

Wait, no. Because the direct flight is |a -b|, which is the same as the pair (a, b). But (a, b) is a pair where i is a and j is b. So when a is in their company and b is in the other, then |i-j| is |a -b|. So the minimal possible |i-j| can't be larger than |a-b|. Because (a, b) is a candidate pair. 

Wait, that makes sense. So the minimal |i-j| is at most |a-b|. So the answer is the minimal |i-j| between any a's company i and b's company j. 

So, the algorithm would be:

If the companies of a and b are the same, output 0.

Else, find the minimal |i-j| where i is in a's company and j is in b's company. That's the answer.

So, the problem reduces to: when a and b are in different companies, find the minimal |i -j| between any i in company of a and j in company of b. 

So how do we compute that efficiently?

We can precompute two lists: one for the indices of a's company and another for b's company. Then find the pair (i, j) from these two lists with minimal |i-j|. 

But n is up to 1e5. So for example, if the a's company has 1e5 elements and the same for b's, comparing all pairs would be O(1e10), which is impossible. So we need a better approach.

An efficient way to find the minimal |i-j| between two sorted lists is to use two pointers. Because the companies' indices are sorted (since the input is given in order). For example, a's company has a list of sorted indices, and b's company has a sorted list. Then, we can use a two-pointer approach to find the minimal difference between any two elements in the two lists. 

Alternatively, we can merge the two sorted lists and track the minimal adjacent difference. But that's O(n) for each list. 

Wait, but let's think. The two lists (A and B) are sorted. For example, A is the list of indices in a's company, sorted. B is the list of indices in b's company, sorted. The minimal |i - j| would be the minimal of the minimal in A and B as if they were merged. 

So here's the approach:

1. Generate list A: all indices where the company is same as a's. (including a itself)
2. Generate list B: all indices where the company is same as b's. (including b itself)
3. Since both A and B are sorted, use two pointers to find the minimal |i-j|. 

This approach is O(m + k), where m is the size of A and k is the size of B. Since m and k can be up to 1e5 each, this would be manageable, as 1e5 operations are acceptable. 

So, steps for the solution:

- If a == b: cost is 0.
- Else if company of a == company of b: cost is 0.
- Else: compute the minimal |i-j| between any i in A and j in B.

Now, how to efficiently compute this minimal |i-j|.

Let me think of the two sorted lists. For example, A is sorted in ascending order, B is sorted in ascending order. To find the minimal difference between elements from A and B.

The optimal approach here is to iterate through both lists with two pointers. Let's see:

Initialize i = 0, j = 0. The minimal difference is initially a large number.

While i < len(A) and j < len(B):

   current_diff = abs(A[i] - B[j])

   if current_diff < min_diff:

       min_diff = current_diff

   if A[i] < B[j]:

       i += 1

   else:

       j += 1

This works because once we move the pointer of the smaller element, we are trying to find a closer element. For example, if A[i] is less than B[j], moving i forward could find a larger A[i] that's closer to B[j]. Similarly for the other case. This approach is O(m + k) and finds the minimal difference. 

Wait, but is that correct? Let's test with some examples.

Suppose A = [1,3], B = [2,4]. Then:

i=0, j=0: 1 vs 2 → diff 1. min is 1.

Since 1 < 2, move i to 1. Now, A[i] =3. Compare with B[j]=2. 3 vs 2 → diff 1. min remains 1. Now since 3>2, move j to 1. Now compare 3 vs4 → diff1. min still 1. Then i reaches end. So the minimal is 1. Which is correct.

Another example: A = [1,4,5], B = [2,3,6]. 

Start i=0, j=0 → 1 vs2 → diff1. min=1. Since 1 <2, i becomes1.

A[1]=4 vs B[0]=2: diff 2. min remains 1. Since 4>2, j becomes1. 

A[1]=4 vs B[1]=3: diff1. min remains 1. Since4>3, j becomes2. 

A[1]=4 vs B[2]=6: diff2. Since4<6, i becomes2. 

A[2]=5 vs6: diff1. min is now 1. 

So the minimal is 1. 

This approach works. So this two-pointer method can find the minimal difference between two sorted arrays in O(m +k) time.

So the plan is:

- Check if a and b are same → 0.

- Else, check if their companies are same → 0.

- Else, collect all indices in a's company (sorted) and all in b's company (sorted).

- Use two pointers to find minimal |i-j|. That's the answer.

So, for the code:

First, read n, a, b. Then the company string. 

But note that the company string's indices are 0-based in the input, but the airport IDs are 1-based. So the i-th character (0-based) in the string corresponds to airport ID i+1. 

So, for airport x (1-based), its company is the (x-1)th character in the string.

So, company_a = s[a-1], company_b = s[b-1]. 

If a == b → output 0.

Else, if company_a == company_b → output 0.

Else:

Collect all airports in company_a's list (A) and company_b's list (B). Then find minimal |i-j| between i in A and j in B.

But how to collect A and B?

Loop through all x from 1 to n:

if s[x-1] == company_a → add x to A.

Similarly for B.

But for n up to 1e5, this is O(n) time, which is acceptable.

Once we have A and B sorted (since we're adding in order), then apply the two-pointer method.

Wait, but the airports are ordered from 1 to n, so when we collect them in order, the lists A and B will be sorted in ascending order. So no need to sort them again.

So, code steps:

Read n, a, b.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, a, b = map(int, input_stream.readline().rstrip("\n").split())
    s = input_stream.readline().rstrip("\n").strip()

    if a == b:
        print(0, file=output_stream)
    else:
        company_a = s[a-1]
        company_b = s[b-1]
        if company_a == company_b:
            print(0, file=output_stream)
        else:
            A = []
            B = []
            for i in range(n):
                if s[i] == company_a:
                    A.append(i+1)
                if s[i] == company_b:
                    B.append(i+1)
            i = j = 0
            min_diff = float('inf')
            lenA = len(A)
            lenB = len(B)
            while i < lenA and j < lenB:
                current = abs(A[i] - B[j])
                if current < min_diff:
                    min_diff = current
                    if min_diff == 0:
                        break
                if A[i] < B[j]:
                    i += 1
                else:
                    j += 1
            print(min_diff, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 5 2
10110
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

Second example:

5 5 2

10110

s is '10110', which is indexes 0-4 correspond to airports 1-5.

a is 5 → company is s[4] = '0'. b is 2 → s[1] = '0'. So same company. So output 0. Correct.

Another test case where a and b are in different companies, and the minimal is |a-b|. For example:

n=3, a=1, b=3. s=100. So a's company is '1', b's is '0'. So A is [1], B is [2,3]. The minimal |i-j| is 1 (1-2). So output is 1. Which is less than |1-3|=2.

So code would return 1.

Another test case: a=2, b=5, s=0 1 0 1 0. So a's company is 1 (s[1] is '1'), b's company is 0 (s[4] is '0'). So A is [2,4], B is [1,3,5]. The minimal pairs are (2,1) →1, (2,3) →1, (4,3)→1, (4,5)→1. So minimal is 1. So code returns 1.

So the code should work.

Now, considering the constraints. For n=1e5, the lists A and B can be up to 1e5 elements each. The two-pointer approach is O(m +k), which is acceptable. The initial loops to generate A and B are O(n) each. So total time is O(n), which is acceptable for n=1e5.

Memory-wise, for n=1e5, storing two lists of up to 1e5 elements each is 2*1e5 integers, which is around 800KB (assuming 4 bytes per integer), which is manageable within 256MB.

Thus, the code should pass all test cases.
</think>

```python
n, a, b = map(int, input().split())
s = input().strip()

if a == b:
    print(0)
else:
    company_a = s[a-1]
    company_b = s[b-1]
    if company_a == company_b:
        print(0)
    else:
        A = []
        B = []
        for i in range(n):
            if s[i] == company_a:
                A.append(i+1)
            if s[i] == company_b:
                B.append(i+1)
        i = j = 0
        min_diff = float('inf')
        lenA = len(A)
        lenB = len(B)
        while i < lenA and j < lenB:
            current = abs(A[i] - B[j])
            if current < min_diff:
                min_diff = current
                if min_diff == 0:
                    break
            if A[i] < B[j]:
                i += 1
            else:
                j += 1
        print(min_diff)
```
