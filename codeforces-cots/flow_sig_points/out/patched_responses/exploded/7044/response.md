<think>
Okay, let's see. The problem is about two companies choosing elements such that their selected elements don't overlap, and we need to maximize the total income. Hmm. So each company picks a subset of their elements, but if any element is present in both subsets, that's not allowed. We need to find the maximum possible sum of their incomes under this condition.

First, I need to process the input. For each company, they have a list of elements with unique IDs and values. The key point here is that if the same element exists in both companies' lists, then we can't take both. So for any element that appears in both companies, we have to choose whether to take it from ChemForces, from TopChemist, or neither. But since each element is unique within each company's list (as per the input constraints), the conflict can only occur between elements from different companies that have the same ID.

So the approach should be:

1. For each element ID, check if it exists in both companies.
2. For such elements, decide whether to take it from ChemForces, TopChemist, or neither, whichever gives the maximum total.
3. For elements that are unique to one company, we can take them unconditionally if their value is positive (since adding them increases the total).

Wait, but even elements that are unique can be taken as long as they are in their company's subset. But since the companies can choose any subset, we need to include all elements that contribute positively. Because if an element's value is positive, adding it will increase the total sum. So for elements that are unique (appear only in one company), we should take them if their value is positive. For elements that are present in both companies, we need to choose which company's version to take (or neither) such that the sum x_i + y_j (but only if they are not the same element) is maximized.

Wait, no. For elements that are in both companies, you can take the element from either company, but not both. So for each such element, the maximum contribution is the maximum of the two values (x_i and y_j) if that maximum is positive. Otherwise, you take neither. Because if the maximum is negative, taking neither gives 0, which is better than taking the negative sum.

So the plan is:

- Create a dictionary to map element IDs to their values in both companies.
- For each element in ChemForces, check if it's also in TopChemist.
- For elements present in both, sum the maximum of the two values (but only if it's positive) for each.
- For elements present in only one company, add their value if it's positive.

But how do we efficiently check which elements are present in both companies?

The steps I should take:

1. Read all elements from ChemForces and store them in a dictionary (say, a hash map), where the key is the element ID and the value is x_i.
2. Read all elements from TopChemist, and for each element, check if it's in the ChemForces dictionary.
   - If it is, then we need to decide whether to take ChemForces' x_i, TopChemist's y_j, or none. The best choice is to take the maximum of x_i and y_j. If the maximum is positive, add it to the total. If not, add zero.
   - If it's not, then add y_j if it's positive.
3. For the elements in ChemForces that are not in TopChemist, add their x_i if positive.

Wait, but this approach would miss the case where an element is in both companies. Because after processing the TopChemist elements, how do we handle the ChemForces elements that were already considered in the overlapping case?

Hmm. Let's think again.

We need to process all elements once, but for the overlapping ones, take the maximum. For the others, take their own if positive.

So:

- Combine all elements from both companies, grouping by their ID.
- For each group:
   - If the group has elements from both companies, compare their values and take the max if positive.
   - If the group has elements from only one company, take the sum of those elements (but each element is in one company's list, so sum the ones with positive values).

Wait, but each group is for a single element ID. For example, element 1 is in ChemForces with value 2 and in TopChemist with value 4. Then, for this group, we take max(2,4) =4, which is added to the total. Then, the other elements (from either company) that are not overlapping are added if their value is positive.

So the correct approach would be:

1. Create a dictionary that for each element ID tracks the ChemForces value (if any) and the TopChemist value (if any).
2. For each element in this dictionary:
   a. If both companies have the element, add the maximum of the two values, but only if it's positive.
   b. If only ChemForces has it, add its value if positive.
   c. If only TopChemist has it, add its value if positive.

But how do we efficiently build this dictionary?

We can proceed as follows:

- Read all n elements from ChemForces and store them in a dict (cf_dict) where keys are a_i and values are x_i.
- Read all m elements from TopChemist and for each, check if the element exists in cf_dict:
   - If it does, then for that element, we compute max(cf_value, tc_value) and add it to the total if the max is positive. Then, we need to mark that this element has been processed so that we don't process it again when we iterate through the cf_dict entries.
   - If not, add the tc_value if positive.
- Then, iterate through all elements in cf_dict. For each element, if it's not present in the tc elements, add its value if positive. But wait, how do we track which elements have been processed? Because when processing the tc elements, if an element exists in both, we process it and add the max. So in the cf_dict, the elements that are in both have already been considered. So when we iterate through the cf_dict, we need to check if the element was present in tc. If not, add its x_i if positive.

Wait, perhaps a better approach is:

1. Merge both lists into a single dictionary where each key is the element ID, and the value is a tuple (x, y) where x is the value from ChemForces (if present) and y from TopChemist (if present). For example, if an element is only in ChemForces, then the tuple is (x, 0) or (x, None)? Or perhaps (x, None) and (None, y). Hmm, maybe using a dictionary where each entry has the ChemForces value and TopChemist value.

Alternatively, create two separate dictionaries. Let's say:

cf_dict: a dictionary where key is element ID, value is x_i.

tc_dict: a dictionary where key is element ID, value is y_j.

Then, the set of all elements is the union of the keys of cf_dict and tc_dict.

For each element in this union:

- If the element is present in both, then take max(cf_val, tc_val) if positive, else 0.
- If present only in cf_dict, add cf_val if positive.
- If present only in tc_dict, add tc_val if positive.

But how to compute the union efficiently?

But in Python, the union of the keys of two dictionaries can be done with set(cf_dict.keys()) | set(tc_dict.keys()). However, when n and m are up to 1e5 each, this might be O(n + m), which is acceptable.

Wait, but 1e5 + 1e5 is 2e5 elements. So for each element in the union of keys:

But this would take O(n + m) time, which is acceptable.

So steps:

1. Read n elements, store in cf_dict as {a_i: x_i}.
2. Read m elements, store in tc_dict as {b_j: y_j}.
3. Create a set of all element IDs (keys from both dictionaries).
4. Initialize total_income to 0.
5. For each element in the union of keys:
   a. Check if present in both.
   b. If yes: add max(cf_val, tc_val) if positive. If max is negative, add 0.
   c. If in cf only: add cf_val if positive.
   d. If in tc only: add tc_val if positive.
6. Sum all these to get the total.

This approach would work, but how efficient is it?

The time complexity is O(n + m + (n + m)), since the union of the keys is O(n + m) (since each key is unique per company, but possible overlaps), and processing each key is O(1) per element. So overall O(n + m) time, which is acceptable for n and m up to 1e5.

But storing two dictionaries and then processing the union of their keys would take O(n + m) space. However, since n and m are up to 1e5 each, the space is acceptable (each dictionary would have 1e5 entries, each storing an integer key and value. That's manageable within 256MB).

So this seems like a viable approach.

Let's test this logic against the examples.

First example:

ChemForces has elements 1 (2), 7 (2), 3 (10).

TopChemist has elements 1 (4), 2 (4), 3 (4),4 (4).

The union of keys is {1,7,3,2,4}.

Processing each element:

1: present in both. max(2 vs 4) =4. add 4.

7: only in cf. 2 is positive. add 2.

3: present in both. max(10 vs4) =10. add 10.

2: only in tc. 4 positive. add4.

4: only in tc. 4 positive. add4.

Total sum: 4 +2 +10 +4 +4 = 24. Which matches the example.

Second example:

ChemForces has 1e9 (239).

TopChemist has 14 (15), 92 (65), 35 (89). All elements are unique. So for each, add their values if positive. So 239 (cf) +15+65+89 = 239+169=408. Correct.

Another test case: suppose an element is present in both, but the max is negative. For example, cf has element 5 with value -3, and tc has element 5 with value -5. Then, for this element, we add 0, since the max is -3 and -5, which is -3. Since negative, we don't take it.

Another case: element is in both, but one is positive. Like cf has 6 (5), tc has 6 (-10). Then max is 5, which is positive. So add 5.

So this logic seems correct.

Now, how to implement this in Python efficiently?

First, read the inputs.

Read n, then read n lines of a_i and x_i. Store in a dictionary.

Read m, then read m lines of b_j and y_j. Store in another dictionary.

Then, get all unique keys in the union of the two dictionaries.

For each key:

Check if it's in both.

Compute the contribution.

Sum all contributions.

So code steps:

Read n.

cf = {}

for _ in range(n):

    a_i, x_i = map(int, input().split())

    cf[a_i] = x_i

Read m.

tc = {}

for _ in range(m):

    b_j, y_j = map(int, input().split())

    tc[b_j] = y_j

Then, create a set of all keys: all_elements = set(cf.keys()) | set(tc.keys())

total = 0

for elem in all_elements:

    cf_val = cf.get(elem, 0)

    tc_val = tc.get(elem, 0)

    if cf_val > 0 or tc_val >0:

        # compute max between cf_val and tc_val, but only if present in both?

        # Wait, no. Because if the element is in both, then cf_val and tc_val are their values.

        # If the element is in both, then take max(cf_val, tc_val). If that's positive, add it.

        # Else, add 0.

        # If element is in only one, then add that value if positive.

        if elem in cf and elem in tc:

            current_max = max(cf_val, tc_val)

            if current_max >0:

                total += current_max

        else:

            # only in one of them

            if elem in cf:

                if cf_val >0:

                    total += cf_val

            else:

                if tc_val >0:

                    total += tc_val

But wait, that's not correct. For example, if an element is only in cf, and its value is positive, then add it. Similarly for tc.

Alternatively, for each element in all_elements:

cf_val = cf.get(elem, 0)

tc_val = tc.get(elem, 0)

max_val = max(cf_val, tc_val)

if elem in cf and elem in tc:

    # in both, take max_val if positive

    if max_val >0:

        total += max_val

else:

    # only in one, add that if positive

    if cf_val >0:

        total += cf_val

    elif tc_val >0:

        total += tc_val

Wait, that might not work. For example, if an element is in only cf, but cf_val is 5, then add 5. If it's in only tc and tc_val is 5, add 5.

But how do we check whether the element is in both?

Wait, the code:

if elem in cf and elem in tc:

   handle overlapping case

else:

   handle non-overlapping case

But in the else case, the element is in either cf or tc.

So for the else case:

sum_val = 0

if elem in cf:

   sum_val += cf_val if cf_val >0 else 0

else:

   sum_val += tc_val if tc_val >0 else 0

But how to code this.

Alternatively, in the else case:

sum_val = max(cf_val, tc_val) if max(cf_val, tc_val) >0 else 0

But no, because if the element is in only one, then one of the values (cf_val or tc_val) is zero (since we used get with default 0). For example, if elem is in cf, then tc_val is 0.

So, in that case, max(cf_val, 0) would be cf_val if positive. So for the else case, sum_val = max(cf_val, tc_val) if positive, else 0.

But since in the else case, the element is in only one of the companies, the sum_val is the max of (its value, 0). So, sum_val = max(cf_val, tc_val) if that is positive, else 0.

Wait, but in the else case, the element is in exactly one company. So for example, if it's in cf, then tc_val is 0, so max(cf_val, 0) is cf_val. So sum_val is cf_val if it's positive, else 0. Which is the same as adding cf_val if positive.

So the code can be simplified as:

for elem in all_elements:

    in_cf = elem in cf

    in_tc = elem in tc

    cf_val = cf.get(elem, 0)

    tc_val = tc.get(elem, 0)

    if in_cf and in_tc:

        current_max = max(cf_val, tc_val)

        if current_max > 0:

            total += current_max

    else:

        # in only one of them

        if in_cf:

            if cf_val >0:

                total += cf_val

        else:

            if tc_val >0:

                total += tc_val

Alternatively, the code can be written as:

for elem in all_elements:

    cf_val = cf.get(elem, 0)

    tc_val = tc.get(elem, 0)

    if elem in cf and elem in tc:

        total += max(cf_val, tc_val) if max(cf_val, tc_val) >0 else 0

    else:

        total += (cf_val if cf_val >0 else 0) + (tc_val if tc_val >0 else 0)

Wait, but no. Because in the else case, the element is present in only one company, so either cf_val is the value (and tc_val is 0), or tc_val is the value (and cf_val is 0). So the sum would be the value if positive. For example, in the else case, if the element is in cf, then tc_val is zero. So cf_val + tc_val is cf_val. If cf_val is positive, add it. Else, add zero.

So in the else case, sum (cf_val + tc_val) if the sum is positive. But in the else case, the element is in exactly one company, so cf_val + tc_val is the value of that company. So, for example, if the element is in cf with value 5, then cf_val is 5, tc_val is 0. Sum is 5. So if positive, add it.

So the code can be written as:

for elem in all_elements:

    cf_val = cf.get(elem, 0)

    tc_val = tc.get(elem, 0)

    if elem in cf and elem in tc:

        current_max = max(cf_val, tc_val)

        if current_max >0:

            total += current_max

    else:

        contribution = cf_val + tc_val

        if contribution >0:

            total += contribution

Because in else case, either cf_val is zero or tc_val is zero. So cf_val + tc_val is the value of the element in the company where it exists. So if that's positive, add it.

This is a more concise way to write it.

So for example, in the else case:

if the element is in cf only, then tc_val is 0, so contribution is cf_val. If cf_val is positive, add it. Else, 0.

Similarly for tc only.

So this code is correct.

So this approach should work.

Now, let's code this in Python.

But we need to process the elements efficiently.

But for handling 1e5 elements in each company, using dictionaries is the right approach.

So, code steps:

Read n.

Read n lines, store in cf.

Read m.

Read m lines, store in tc.

Compute all_elements = set(cf.keys()) | set(tc.keys())

Initialize total = 0

For each elem in all_elements:

   cf_val = cf.get(elem, 0)

   tc_val = tc.get(elem, 0)

   if elem is in both:

       current_max = max(cf_val, tc_val)

       if current_max >0:

           total += current_max

   else:

       contribution = cf_val + tc_val

       if contribution >0:

           total += contribution

But how to check if elem is in both?

In Python:

if elem in cf and elem in tc:

So for each element in all_elements, check if it's present in both dictionaries.

Thus, the code becomes:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    cf = {}

    for _ in range(n):

        a_i, x_i = map(int, input_stream.readline().rstrip("\n").split())

        cf[a_i] = x_i

    m = int(input_stream.readline().rstrip("\n"))

    tc = {}

    for _ in range(m):

        b_j, y_j = map(int, input_stream.readline().rstrip("\n").split())

        tc[b_j] = y_j

    all_elements = set(cf.keys()).union(tc.keys())

    total = 0

    for elem in all_elements:

        in_cf = elem in cf

        in_tc = elem in tc

        cf_val = cf.get(elem, 0)

        tc_val = tc.get(elem, 0)

        if in_cf and in_tc:

            current_max = max(cf_val, tc_val)

            if current_max >0:

                total += current_max

        else:

            contribution = cf_val + tc_val

            if contribution >0:

                total += contribution

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
1000000000 239
3
14 15
92 65
35 89
""",
            "output": \
"""\
408
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

Sample Input 2:

1

1000000000 239

3

14 15

92 65

35 89

cf has {1000000000:239}

tc has {14:15,92:65,35:89}

all_elements = {1000000000,14,92,35}

Processing:

1000000000: only in cf. contribution 239. Add.

14: only in tc. 15 added.

92: 65 added.

35: 89 added.

Sum 239+15+65+89=408. Correct.

Another test case where an element is present in both but the max is negative:

cf has {5: -3}, tc has {5: -5}

Processing: element 5 is in both. max is -3. Since it's negative, add 0.

Another case where element is in both but one is positive:

cf {6:5}, tc {6: -10}. Max is5. Add5.

So code works.

Now, about efficiency.

The code reads the inputs in O(n + m) time. Then, creating the union of keys is O(n + m). Then, iterating through all elements is O(n + m). Each iteration is O(1) for dictionary lookups. So overall O(n + m) time, which is acceptable for 1e5 elements each.

Space-wise, the dictionaries are O(n + m) which is acceptable for 256MB.

So this code should work within the time and memory constraints.

Therefore, this is the correct and optimal approach.
</think>

```python
n = int(input())
cf = {}
for _ in range(n):
    a, x = map(int, input().split())
    cf[a] = x

m = int(input())
tc = {}
for _ in range(m):
    b, y = map(int, input().split())
    tc[b] = y

all_elements = set(cf.keys()).union(tc.keys())
total = 0

for elem in all_elements:
    in_cf = elem in cf
    in_tc = elem in tc
    cf_val = cf.get(elem, 0)
    tc_val = tc.get(elem, 0)
    if in_cf and in_tc:
        current_max = max(cf_val, tc_val)
        if current_max > 0:
            total += current_max
    else:
        contribution = cf_val + tc_val
        if contribution > 0:
            total += contribution

print(total)
```
