<think>
Okay, I need to solve this problem where I have to compute the sum of the integer points in the intersection of every possible k-sized subset of the given segments. Let's think about how to approach this efficiently, especially given the constraints that n can be up to 200,000. A brute-force approach of checking every possible subset is impossible here because the number of subsets is C(n, k), which is way too big for n=2e5. So we need a smarter way.

First, let's understand the problem. For each combination of k segments, we compute the intersection of all of them. The intersection is another interval [L, R], and we need to sum (R - L + 1) for all possible combinations. Then take modulo 1e9+7.

Hmm. So the key is to find how each possible point contributes to the total sum. Because directly calculating for each subset is impossible, perhaps inclusion-exclusion or some other combinatorial approach can help.

Wait, maybe we can model this by considering each integer point x and determine in how many subsets of k segments x is included in the intersection. Then sum over all x multiplied by the number of subsets where x is in the intersection.

Wait, that makes sense. Because for a point x, if it is covered by m segments, then the number of subsets of k segments where x is in all of them is C(m, k). So for each x, if it's covered by exactly m segments, then the contribution is C(m, k) * 1 (since each such subset contributes 1 for this x). Then the total sum is the sum over all x of C(m, k), where m is the number of segments that include x.

But how do we compute this efficiently?

The problem is that x can be very large, up to 1e9. So enumerating all x's isn't feasible. Instead, we can model the coverage of the intervals and compute the sum over intervals where the coverage is the same. For example, between two events (like the start or end of a segment), the number of covering segments (m) is constant. So we can find all intervals where m is a certain value and compute how many integer points are in that interval, then multiply by C(m, k) for that m.

So the plan is:

1. For all segments, track the start and end points, and count how many segments are covering each interval. Then for each such interval, compute the number of integer points in it, multiply by C(m, k) where m is the coverage count for that interval, and sum all these contributions.

But how to efficiently track the coverage intervals?

This is similar to the line sweep algorithm. Let's think: process all the start and end points in order. For each event (like a start or end of a segment), we can track the current coverage. The intervals between events have a constant coverage count. So we can process these events in sorted order and compute the coverage intervals.

Each segment [l_i, r_i] contributes a start event at l_i (increasing coverage by 1) and an end event at r_i + 1 (decreasing coverage by 1). Because the interval is inclusive, the coverage is up to and including r_i. So the end event is at r_i + 1, which is the point where the coverage ends.

Once all events are sorted, we can sweep through them, tracking the current coverage count and the current position. The interval between two consecutive events (from prev_pos to current_pos) has coverage count equal to the current coverage. The number of integer points in [prev_pos, current_pos) is current_pos - prev_pos. But wait, the interval [a, b) includes all x where a <= x < b. So for example, between a=2 and b=5, the integers are 2,3,4 (3 points). So the count is (5-2) =3. So for each interval between two events, the number of points is (current_pos - previous_pos) multiplied by the coverage count's contribution (if coverage >=k, then C(coverage, k) else 0).

So the steps are:

- Collect all events (start and end) from all segments.
- Sort the events in order. However, events at the same position need to be ordered such that end events come before start events. Wait, no. Let's think: when a segment starts at l_i, it's adding to the coverage. When a segment ends at r_i, the end is at r_i +1. So for example, two events at position x: one is a start (adding 1) and another is an end (subtracting 1). Which should come first?

Wait, suppose two events are at the same position. For example, a segment ends (event at x) and another starts (event at x). The end event (subtracting) should be processed before the start event (adding). Because the end event's effect is to decrease the coverage after x, but during x, the coverage is still active. Wait, maybe not. Let's see.

Suppose a segment [2,3] ends at x=4 (since end event is r_i +1 =3+1=4). Another starts at x=4. The coverage during [3,4) is (after processing the end event), so the start event at x=4 would be processed after the end event. So when events are at the same position, end events (which are of type -1) should be processed before start events (type +1). Because the end event reduces coverage from x onwards, and the start increases it from x onwards. So for events at the same position, the end events (-1) come first.

So the events are sorted by their position. If two events have the same position, the one with a delta of -1 comes before +1.

Once events are sorted, we can sweep through them, track the current coverage, and between each pair of consecutive events, compute the contribution of the interval [prev_pos, current_pos) multiplied by C(current_coverage, k), but only if current_coverage >=k. The number of points is (current_pos - prev_pos), which is the length of the interval. So for each such interval, we calculate the contribution as (current_pos - prev_pos) * C(m, k), where m is the coverage during that interval.

So the steps are:

1. Process all segments into events.
2. Sort the events as described.
3. Sweep through the events, keeping track of current coverage and the previous position.
4. For each interval between events, calculate the contribution.

Now, the problem is how to compute C(m, k) efficiently. Since m can be up to n (2e5), and k up to 2e5 as well. Precomputing combinatorial numbers C(m, k) for all m up to 2e5 is feasible.

But wait, since we need C(m, k) for m >=k, and 0 otherwise, we can precompute a list where for each m, we have the value of C(m, k) mod MOD. But how?

Alternatively, for each m, C(m, k) can be computed as m*(m-1)*...*(m -k +1)/(k!) mod MOD. But for k up to 2e5, precomputing factorial and inverse factorial arrays would help. Let's think.

Let's precompute factorials up to n, inverse factorials up to n. Then, C(m, k) can be computed as factorial[m] * inv_fact[k] * inv_fact[m -k] mod MOD. But this is only valid when m >=k. Otherwise, it's 0.

But for this, when k is up to 2e5, and n is up to 2e5, precomputing factorial and inverse factorial is manageable. So we can precompute these arrays once, and then for each m, compute C(m, k) if m >=k, else 0.

Wait, but wait. The problem is that for each m, k can vary. But in this problem, k is fixed. So once k is given, we can precompute C(m, k) for all m from 0 to n, and then use that array for all intervals.

So during preprocessing, compute for all m, the value of comb(m, k) mod MOD. This can be done using the formula comb(m, k) = comb(m-1, k-1) * m / (m -k + 1), but that's not straightforward. Alternatively, compute it as factorial[m] * inv_fact[k] * inv_fact[m -k] mod MOD. But when m <k, this is zero. So for each m, compute:

if m <k: 0

else: factorial[m] * inv_fact[k] * inv_fact[m -k] mod MOD.

So to compute this array, we need to precompute factorial up to n, and inv_fact up to n. Then for each m, compute the combination.

But how to precompute factorial and inverse factorial up to 2e5?

Yes. Let's proceed.

So steps:

1. Read n and k.

2. Read all the segments, and create events for start (l_i) and end (r_i +1). For each segment, add two events: (l_i, +1) and (r_i +1, -1).

3. Sort all events. The sorting is done by the position. For events with the same position, the event with delta -1 comes first. So in the list, events are sorted primarily by their x position, and secondarily by their delta (delta=-1 comes before delta=+1 if x is same).

4. Precompute factorial and inverse factorial up to n. Then compute comb(m, k) for all m from 0 to n, and store in an array.

5. Sweep through the sorted events, keeping track of the current coverage and previous position. For each interval between previous position and current position, compute the contribution as (current_x - prev_x) * comb_val, where comb_val is comb(current_coverage, k) if current_coverage >=k, else 0. Sum all these contributions modulo MOD.

But wait, during the interval between prev_x and curr_x, the coverage is the current coverage (after processing all events up to prev_x). So when processing the events in sorted order, after each event, the coverage is updated. So the interval between events is [prev_x, curr_x), and the coverage during that interval is the coverage after processing all events at prev_x. Wait, no. Let's think:

Suppose we have events in the order x0, x1, x2, ... The initial coverage is 0. Then, for the first interval (before any events), there's nothing. Then, between x0 and x1, the coverage is what was set after processing the event at x0.

Wait, no. Let's see:

The events are sorted. Let's say we start with coverage 0.

At x=prev_x, we process all events at prev_x (since there could be multiple events at the same x). After processing all those events, the coverage is updated. Then the next event is at curr_x. The interval between prev_x and curr_x is [prev_x, curr_x), and during that interval, the coverage is the coverage after processing all events at prev_x.

So the algorithm would be:

prev_x = None

current_coverage = 0

sum_ans =0

for event in sorted_events:

    curr_x = event.x

    if prev_x is not None and curr_x > prev_x:

        # the interval is [prev_x, curr_x)

        length = curr_x - prev_x

        comb_val = comb(current_coverage, k) if current_coverage >=k else 0

        sum_ans += length * comb_val

        sum_ans %= MOD

    # process the event (update coverage)

    current_coverage += event.delta

    prev_x = curr_x

Wait, but after processing all events at curr_x, the coverage is updated, and the next interval will be from curr_x to next event's x.

So the steps are:

Initialize current_coverage to 0, prev_x to None.

For each event in sorted order:

   if prev_x is not None and curr_x > prev_x:

       compute the contribution between prev_x and curr_x with current_coverage (before processing the event)

   process the event (update coverage)

   prev_x = curr_x

Wait, no. Because events at the same x are processed all at once. So for example, if there are multiple events at x=5, they are processed in the order of their delta (the end events first). So after processing all events at x=5, the coverage is updated, and the next interval starts from x=5.

Wait, no. Let's clarify.

Suppose we have events at x=5: first a delta of -1 (end), then a delta of +1 (start). So the current coverage is 0 (initially). When we process the events at x=5:

Before processing, the interval from prev_x (which was before 5) to x=5 is considered. Then, the events at x=5 are processed. So the coverage during the interval up to x=5 is the previous coverage.

So the correct approach is:

- The events are sorted in order of their x, and within the same x, end events (-1) come before start events (+1).

- Between events, the coverage is the same. So for the interval [prev_x, curr_x), the coverage is the current coverage before processing the events at curr_x.

So during the loop:

prev_x starts as None.

For each event in the sorted list:

   if prev_x is not None and curr_x > prev_x:

       compute the contribution for [prev_x, curr_x) with current_coverage.

   process the event (update coverage).

   set prev_x to curr_x.

So this way, the interval between events is handled correctly.

Yes. So the code would process events in order, and between the previous x and current x, the coverage is the current coverage (before processing the current events). Then, the events are processed (changing coverage), and the next interval starts at current x.

This logic is correct.

Now, the main steps are:

- Process all events.

- Precompute comb(m, k) for m from 0 to n.

- Then sweep the events and accumulate the answer.

Now, the next question is handling the events properly.

But how to represent the events?

Each event has a position x and a delta (+1 or -1). So we can create a list of tuples (x, delta), then sort them.

But the sorting key is x, and then delta. Because for same x, events with delta -1 should come before delta +1. So when sorted, the tuple comparison would be (x, delta). So for two events with same x, (5, -1) comes before (5, 1). Because -1 < 1. So when we sort the list of (x, delta), this is automatically handled.

So yes, in Python, when you sort a list of tuples, the tuples are compared element-wise. So (5, -1) is less than (5, 1), which is what we need.

So for each segment [l, r], we add two events: (l, +1) and (r+1, -1).

Once all events are generated, sort them.

Now, the precomputing of combinations.

We need to compute comb(m, k) for all m from 0 to n. But for m <k, it's 0. For m >=k, it's C(m, k) mod MOD.

To compute this, precompute factorials up to n, inverse factorials up to n.

But for n up to 2e5, this is manageable.

The formula is C(m, k) = m!/(k! (m -k)!) mod MOD.

So, precompute fact array where fact[i] = i! mod MOD.

Precompute inv_fact array where inv_fact[i] = (i!)^{-1} mod MOD.

Then, for each m >=k, comb[m] = fact[m] * inv_fact[k] * inv_fact[m -k] mod MOD.

So steps for precomputing:

1. Precompute fact and inv_fact up to n.

But what if k is larger than n? Well, according to the problem statement, 1 <=k <=n. So m can be up to n. So for m <k, comb is 0.

So the code for precomputing comb is:

max_m = n

comb = [0] * (max_m + 1)

for m in range(0, max_m +1):

    if m <k:

        comb[m] =0

    else:

        comb[m] = (fact[m] * inv_fact[k] % MOD) * inv_fact[m -k] % MOD

But for n up to 2e5, precomputing fact and inv_fact is feasible.

How to compute fact and inv_fact?

Compute fact as:

fact[0] =1

for i in 1..n:

    fact[i] = fact[i-1] * i % MOD

Compute inv_fact using Fermat's little theorem, since MOD is prime.

inv_fact[n] = pow(fact[n], MOD-2, MOD)

then for i in n-1 downto 0:

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

So that's the standard way.

Once comb array is computed, during the sweep phase, for each interval where the coverage is m, we look up comb[m] and multiply by the length of the interval.

Now, let's test this approach with the sample input.

Sample 1:

3 2

Segments:

1-2, 1-3, 2-3.

Events for each segment:

Segment 1: l=1, r=2 → events (1, +1), (3, -1).

Segment 2: l=1, r=3 → events (1, +1), (4, -1).

Segment3: l=2, r=3 → events (2, +1), (4, -1).

All events sorted:

The list of events is:

(1, +1), (1, +1), (2, +1), (3, -1), (4, -1), (4, -1).

Wait, no. Wait, the third segment's events are (2, +1) and (4, -1).

So the events list is:

(1, +1) → from first and second segment.

Then (1, +1) → same, but same x. So sorted by x, then delta. Since the delta is +1, same as others. So the first two events are (1, +1) and (1, +1). Then (2, +1) from third segment. Then (3, -1) (end of first segment), then (4, -1) (end of second and third segments).

So sorted events:

1: events at x=1, delta +1 (two events), then x=2, delta +1, then x=3, delta -1, then x=4, delta -1 (two events).

So during the sweep:

prev_x starts as None.

current_coverage starts at 0.

Processing events in order:

First event is x=1, delta +1.

But before processing, since prev_x is None, we skip the contribution step.

Process the event: current_coverage becomes 1.

prev_x is set to 1.

Then next event is x=1, delta +1. So prev_x is 1, curr_x is 1. So curr_x is not > prev_x. So contribution is zero. Process the event: current_coverage becomes 2. prev_x is 1.

Next event is x=2, delta +1. curr_x is 2. Now, prev_x is 1, so interval [1,2) is 1 →2-1=1. Current coverage is 2 (before processing the event). So contribution is 1 * comb(2,2) =1 * 1=1. sum_ans becomes 1.

Then process the event: current_coverage becomes 3. prev_x is 2.

Next event is x=3, delta -1. curr_x is 3. prev_x is 2. So interval [2,3) →1 (3-2=1). current coverage is 3. comb(3,2) is 3. So contribution is 1 *3=3. sum_ans is 1+3=4.

Process the event: current_coverage becomes 2.

prev_x is 3.

Next event is x=4, delta -1. curr_x is 4. interval [3,4) →1. current coverage is 2. comb(2,2)=1. contribution is 1*1=1. sum_ans 4+1=5.

Process event: coverage becomes 1.

prev_x is 4.

Next event is x=4, delta -1. curr_x is same as prev_x. no contribution.

Process event: coverage becomes 0.

prev_x remains 4.

No more events. So total sum is 5, which matches the first sample.

Yes. So the approach works for the first sample.

Now, the code.

First, read n and k.

Then read n lines of li and ri.

Generate events for each segment. For each, add (l_i, +1) and (r_i +1, -1).

Sort the events.

Precompute fact and inv_fact.

Compute comb array.

Then, sweep through events.

But what about the fact that some events may have the same x? The code handles it because the events are sorted correctly.

Now, code structure.

In Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, k = map(int, input_stream.readline().rstrip("\n").split())

    segments = []

    events = []

    for _ in range(n):

        l, r = map(int, input_stream.readline().rstrip("\n").split())

        events.append( (l, 1) )

        events.append( (r+1, -1) )

    events.sort()

    # Precompute factorial and inv factorial

    max_m = n

    fact = [1]*(max_m +1)

    for i in range(1, max_m +1):

        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1]*(max_m +1)

    inv_fact[max_m] = pow(fact[max_m], MOD-2, MOD)

    for i in range(max_m-1, -1, -1):

        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    # Compute comb array

    comb = [0]*(max_m +1)

    for m in range(0, max_m+1):

        if m <k:

            comb[m] =0

        else:

            comb[m] = fact[m] * inv_fact[k] % MOD

            comb[m] = comb[m] * inv_fact[m -k] % MOD

    # Sweep

    current_coverage =0

    prev_x = None

    ans =0

    for x, delta in events:

        if prev_x is not None and x > prev_x:

            length = x - prev_x

            if current_coverage >=0 and current_coverage <= max_m:

                c = comb[current_coverage]

            else:

                c=0

            ans = (ans + length * c) % MOD

        current_coverage += delta

        prev_x = x

    print(ans % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
1 3
1 3
1 3
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

Another sample:

Input 3 3:

All three segments are [1,3]. So each contributes events (1, +1), (4, -1).

So events are:

(1,1) ×3, (4,-1) ×3.

sorted as:

(1,1), (1,1), (1,1), (4,-1), (4,-1), (4,-1).

Sweep:

prev_x None → first event: x=1, process delta. coverage becomes 1. prev_x=1.

Next event x=1, delta=1: coverage 2. prev_x=1.

Next event x=1, delta=1: coverage 3. prev_x=1.

Next event is x=4. x>1: interval 1→4 is 3 units. coverage is 3. comb[3] when k=3 is 1. contribution 3*1=3. ans=3.

current_coverage becomes 3-1=2 (after first delta=-1), then 1, then 0.

So sum is 3, which matches the sample.

Another sample:

Input 3 1:

Segments are [1,2], [2,3], [3,4].

Each has events:

[1,2] → (1,1), (3,-1)

[2,3] → (2,1), (4,-1)

[3,4] → (3,1), (5,-1)

So events list:

(1,1), (2,1), (3,-1), (3,1), (4,-1), (5,-1).

Sorted as:

(1,1), (2,1), (3,-1), (3,1), (4,-1), (5,-1).

Sweep:

prev_x None → process first event. coverage becomes 1. prev_x=1.

Next event x=2. x>1: interval 1→2. coverage is 1. length 1. comb[1,1] is 1. ans +=1*1=1.

Process delta+1 → coverage 2. prev_x=2.

Next event x=3. delta-1.

Interval 2→3: length 1. coverage 2. comb[2,1]=2. ans +=1*2 → total 3.

Process delta-1 → coverage 1.

Next event x=3, delta+1. x is same as prev_x (3). No contribution. Process delta+1 → coverage 2. prev_x=3.

Next event x=4. interval 3→4: length 1. coverage 2 → comb 2 → contribution 2. ans=5.

Process delta-1 → coverage 1. prev_x=4.

Next event x=5. interval 4→5: length 1. coverage 1 → comb[1,1] =1. ans=5+1=6.

Process delta-1 → coverage 0. prev_x=5.

No more events. sum is 6, which matches sample.

So the code works.

Now, code considerations:

- Handling large x values: but since the code uses x and delta, even for x up to 1e9, the code can handle them, as they are stored as integers.

- Time constraints: for n=2e5, generating 2n events (4e5 events) is acceptable. Sorting 4e5 elements is O(4e5 log 4e5) which is manageable. The precomputing of factorial and inverse factorial is O(n), which is acceptable. The loop through the events is O(4e5), which is okay.

But in Python, for n=2e5, precomputing factorial and inverse factorial arrays of size 2e5+1 may take some time but should be manageable.

Another possible optimization: when k=0, but according to the problem statement, k is at least 1. So no need to handle that case.

Potential issues:

- The comb array is built for m up to n, but during the code, coverage can be up to n (if all segments are active). So this is correct.

What if during the loop, current_coverage exceeds n? For example, if all segments start at the same point. But since we have n segments, current_coverage can't be more than n. So the comb array is sufficient.

Thus, the code should work correctly.

Now, implement this code.
</think>

```python
MOD = 10**9 + 7

n, k = map(int, input().split())
events = []
for _ in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))
    events.append((r + 1, -1))

events.sort()

max_m = n
fact = [1] * (max_m + 1)
for i in range(1, max_m + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_m + 1)
inv_fact[max_m] = pow(fact[max_m], MOD-2, MOD)
for i in range(max_m -1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

comb = [0] * (max_m + 1)
if k == 0:
    c_k = 1
else:
    c_k = inv_fact[k]
for m in range(max_m + 1):
    if m < k:
        comb[m] = 0
    else:
        comb[m] = fact[m] * c_k % MOD
        comb[m] = comb[m] * inv_fact[m - k] % MOD

current_coverage = 0
prev_x = None
ans = 0

for x, delta in events:
    if prev_x is not None and x > prev_x:
        length = x - prev_x
        if current_coverage <= max_m:
            ans = (ans + length * comb[current_coverage]) % MOD
    current_coverage += delta
    prev_x = x

print(ans % MOD)
```
