<think>
Okay, let's see. The problem is to determine if a given string has two non-overlapping substrings "AB" and "BA". The order can be either AB followed by BA or BA followed by AB. But they can't overlap. Hmm.

So first, I need to find all occurrences of "AB" and "BA" in the string. Then check if there are two such substrings (one AB and one BA) that don't overlap.

Wait, but how to efficiently check this? Because for each AB occurrence, we need to see if there's a BA occurrence that doesn't overlap with it, and vice versa. But considering that the string can be up to 1e5 characters long, checking all possible pairs would be O(n^2) which is not feasible. So we need a smarter approach.

Let me think. Maybe we can find the first occurrence of AB and then look for BA after it (with at least one character in between), or find the first BA and look for AB after it. Alternatively, we could track the earliest and latest positions to find possible non-overlapping pairs.

Another approach: find all the positions where AB occurs and all positions where BA occurs, then check if there's an AB followed by a BA with at least one character between them (so their indices don't overlap). Or a BA followed by an AB.

Alternatively, perhaps the optimal way is to scan the string once, keeping track of possible AB and BA pairs and their positions, then check for non-overlapping in linear time.

Let's think of possible scenarios.

Case 1: There's an AB at position i, then a BA at position j >= i+2. So AB is at i and i+1, BA is at j and j+1. So j >= i+2.

Case 2: There's a BA at position i, then an AB at position j >= i+2.

If either case is possible, the answer is YES.

So the plan could be:

1. Find all indices where AB occurs.
2. Find all indices where BA occurs.
3. For each AB index, check if there's a BA index that is either >= AB_index + 2 (so BA starts after AB ends) or <= AB_index -2 (so BA ends before AB starts).
4. Similarly for BA indices checking for ABs before or after.

But even this approach could be O(n) for each occurrence, which in the worst case (all ABs and BAs) would be O(n^2). So that's not feasible for n=1e5.

We need a way to find in O(1) or O(n) time whether any AB and BA meet the non-overlapping condition.

Alternative idea: find the earliest occurrence of AB and the latest occurrence of BA such that AB is before BA, and check if they don't overlap. Similarly, find the earliest BA and the latest AB that comes after it.

Wait, perhaps we can precompute the earliest and latest positions of AB and BA.

Let me break it down.

We can split the problem into two possibilities:

Either there exists an AB followed by a BA, with their positions non-overlapping. Or a BA followed by an AB, non-overlapping.

So for the first case (AB followed by BA):

The earliest possible AB's position is the first occurrence of AB. Then, check if there's a BA that starts at or after AB's start + 2. Similarly, the latest possible BA's position is the last occurrence of BA. Check if there's an AB that starts before BA's start -1 (so that AB ends at BA's start-1).

Wait, perhaps the steps can be:

Check if there exists an AB and a BA such that the BA starts at least two positions after the AB ends. Or a BA starts at least two positions before the AB starts.

Alternatively, for AB followed by BA:

Find the earliest occurrence of AB. Then, look for any BA that starts at AB's start + 2 or later. If such a BA exists, then return YES.

Similarly, find the earliest BA and look for an AB that starts after BA's end +1. If either of these is true, return YES.

Alternatively, find the latest possible BA occurrence and see if there's an AB before it (with non-overlapping). Or the latest AB and see if there's a BA after.

Alternatively, the earliest AB and the latest BA (if earliest AB is before the latest BA, and they don't overlap). Or earliest BA and latest AB.

Hmm. Let's think of the first scenario: AB occurs before BA. So AB's end is at i+1. The BA's start must be >= i+2. So the earliest AB (the first one) could be the best candidate to leave room for a BA after. So if after the first AB, there's a BA that starts at i+2 or later, then that's a possible YES.

Similarly, if the latest BA is such that there's an AB before it (but not overlapping), then that's a possible YES.

So, here's a possible approach:

1. Find all the positions where AB occurs. Store them in a list AB_indices.

2. Find all the positions where BA occurs. Store them in a list BA_indices.

3. Check if any AB in AB_indices has a BA in BA_indices that starts at AB's start +2 or later. If yes, return YES.

4. Check if any BA in BA_indices has an AB in AB_indices that starts at BA's start +2 or later. If yes, return YES.

But how to check this efficiently.

For step 3:

If AB_indices is not empty and BA_indices is not empty:

We can find the earliest AB (AB_earliest) and the latest BA (BA_latest). If BA_latest >= AB_earliest + 2, then they are non-overlapping. But that's not necessarily true. Because maybe the latest BA is after AB_earliest +2, but there could be a BA before that which is after AB_earliest +2.

Alternatively, for all AB in AB_indices, check if there's a BA that starts at >= AB + 2 (since AB starts at i, ends at i+1. So BA starts at i+2).

But even that could be O(n) for each AB, but n can be up to 1e5. So if there are O(n) ABs, this would be O(n^2), which is not acceptable.

Alternatively, for each AB, the earliest possible BA that is after it is the first BA in BA_indices that is >= AB +2. If there exists such a BA, then yes.

But how to find this efficiently.

If BA_indices are sorted (since we collected them in order), then for a given AB, we can binary search in BA_indices for the first value >= AB +2. If such a value exists, then yes.

Similarly, for each BA in BA_indices, check if there exists an AB in AB_indices >= BA +2.

But even this would be O(m log n), where m is the number of ABs and n the number of BAs, which could be up to 1e5 each. So O(1e5 log 1e5) is acceptable, but perhaps there's a better way.

Wait, but perhaps we can precompute the earliest AB and check the earliest BA after it. Or the latest BA and check if there's an AB before it.

Alternatively, here's a possible approach:

Find all AB positions and BA positions.

For the case where AB comes first:

Check if there exists an AB at position i, and a BA at position j >= i+2.

To find the earliest possible j, we can check the first occurrence of BA >= i+2. If any AB has a BA after it in BA_indices that starts at j >= i+2, then return YES.

Similarly, for the case where BA comes first, check if there's a BA at position i, and an AB at j >= i+2.

So, how to do this efficiently.

For the AB-first case:

We can collect all the AB positions, and for each AB in AB_indices, check if there's a BA that starts at >= i +2.

But even for a string with many ABs, this could take time. However, if the BA_indices are sorted, then for each AB's i, we can binary search BA_indices for the first value >= i+2. If found, then return YES.

Similarly, for BA-first case: for each BA in BA_indices, check if there's an AB in AB_indices >= j+2. If any such exists, return YES.

But again, this could be O(m log n) for each case. But perhaps m and n are O(1e5), which would make the total operations 2e5 log 1e5. Which is acceptable.

But how to collect AB_indices and BA_indices.

Let's see. We can scan the string once and collect all the starting indices of AB and BA.

For example, for string s of length n, loop from 0 to n-2:

For each i, check if s[i] is 'A' and s[i+1] is 'B' → add to AB_indices.

Similarly for BA.

This is O(n) time and O(n) space, which is acceptable for n=1e5.

Once we have AB_indices and BA_indices sorted (as we collect them in order), then for each AB in AB_indices, perform a binary search on BA_indices to see if any BA starts at >= i+2.

Wait, but BA_indices is sorted in increasing order, right? Because we collect them as we traverse the string from left to right.

So for example, if the first AB is at index 0, then BA must start at 2 or later. So we can search the BA_indices for the first value >= 2.

If BA_indices has any such value, then that BA occurs after the AB, non-overlapping. So in this case, return YES.

But even if there's a BA after the first AB, but the AB is later, perhaps the earliest AB is the best candidate. Because the earlier the AB is, the more room there is for a BA after it.

Wait, but the first AB may not have a BA after, but a later AB may have. So we need to check all ABs.

But that's O(m log n) time. For m=1e5 and log n=20, that's 2e6 operations, which is manageable.

Similarly for the BA case.

So the steps are:

Collect AB_indices and BA_indices.

If either AB_indices is empty or BA_indices is empty, return NO.

Now, check for AB followed by BA:

For each AB in AB_indices, check if there exists a BA in BA_indices where BA's start >= AB.start + 2.

If yes, return YES.

Otherwise, check for BA followed by AB:

For each BA in BA_indices, check if there exists an AB in AB_indices where AB.start >= BA.start +2.

If yes, return YES.

If neither case is found, return NO.

But this approach could be O(m log n + n log m), which is acceptable.

But perhaps we can optimize further. Because for AB followed by BA, the earliest possible AB (the first one) gives the earliest possible chance to find a BA after. So maybe if the earliest AB has a BA after, then return YES. Otherwise, check other ABs.

Wait, but no. Suppose the first AB is at position 0, and the first BA is at position 3. Then the first AB can pair with BA at 3. But if the first AB is at 0, but BA starts at 1, then no. But perhaps the second AB is at position 2, which allows a BA at position 4.

So the earliest AB may not be the right one, but a later AB could be. So we need to check all ABs.

Alternatively, perhaps we can precompute the earliest AB and then find the first BA that is after it. Similarly, precompute the earliest BA and see if any AB is after.

Wait, but that's not sufficient. For example:

ABABABABABAB... Then the earliest AB is at 0. The earliest BA is at 1. But if after 0, there's a BA at 2, but BA starts at 2 (so after 0+1=1). So AB at 0 can pair with BA at 2.

Hmm. So the first AB's start is 0. BA needs to start at 2 or later. So if the BA_indices has any element >= 2, then return YES.

So for the AB case, the check can be: after the earliest AB, is there any BA that starts at or after earliest AB's start +2.

If yes, then return YES. Because the earliest AB allows the earliest possible BA after it.

Wait, but that's not necessarily true. Because maybe the earliest AB is followed by BAs that are overlapping, but later ABs have BAs that are non-overlapping. So, for example:

ABABAB:

Indices 0 (AB), 2 (AB), 4 (AB).

BA occurs at 1, 3, 5.

The earliest AB is 0. Check if BA has any >= 2. The first BA after 0 is 1 (starts at 1, which is 0+1, which is overlapping. Then BA at 3 (starts at 3), which is 0+2 +1? Wait, 0+2 is 2. So BA starts at 3 is >=2. So yes. So the earliest AB can pair with BA at 3.

Thus, in this case, the check for earliest AB would find a BA at 3, which is >=0+2. So returns YES.

So perhaps instead of checking all ABs, it's sufficient to check the earliest AB and the latest BA.

Wait, maybe the optimal approach is:

Check if the earliest AB's position i has any BA in BA_indices that starts >= i+2. If yes, then return YES.

Similarly, check if the latest BA's position j has any AB in AB_indices that starts >= j+2. If yes, return YES.

But why would that work?

Let's see. Suppose the earliest AB is at position i. If there exists a BA at position j >= i+2, then the earliest AB and that BA form a valid pair. So the answer is YES.

If not, then maybe there's an AB that comes after some BA. But in that case, the latest BA (the last occurrence) would be the best candidate. So if there's a BA at position j, and any AB in AB_indices that starts >= j+2, then return YES.

But perhaps this approach could miss some cases.

For example, suppose the earliest AB is at 0, but there are no BAs after 2. But there's another AB at position 5, and a BA at position 3. So AB at 5 and BA at 3 is invalid. But maybe there's a BA before the AB. But in this case, the BA is at 3, and the AB is at 5. So BA is before AB. So we need to check if there's a BA that comes before an AB, with AB starting >= BA's start +2.

So the approach would need to check both possibilities:

1. There exists an AB followed by a BA (non-overlapping).

2. There exists a BA followed by an AB (non-overlapping).

So perhaps the correct way is:

Find the earliest AB and see if there's any BA after it (i.e., BA starts >= AB's start +2). If yes, return YES.

If not, find the latest AB and see if there's any BA before it (i.e., BA starts +1 < AB's start).

Wait, no. Because for BA followed by AB, the BA can be at position j, and AB can be at position k >= j+2.

So for the BA followed by AB case, check if there's any BA in BA_indices such that there's an AB in AB_indices starting at >= j+2.

So, to check the BA followed by AB case:

Check if any BA in BA_indices has an AB in AB_indices that starts at >= BA's start +2.

Again, to find this efficiently, for each BA in BA_indices, check via binary search if there's an AB starting at >= BA.start +2.

But this could again be O(m log n). But perhaps we can optimize by checking the earliest BA and the latest AB.

Wait, for the BA followed by AB case, the latest AB is the last occurrence. So if the BA is at position j, and the latest AB is >= j+2, then that's a valid pair.

So check if the latest AB is >= (earliest BA's start + 2). Wait, no. The earliest BA's start could be followed by a later AB.

Alternatively, for the BA followed by AB case, check if the earliest BA has an AB after it. Or check the latest BA and see if there's an AB after it.

Alternatively, for the BA case, the latest BA's start is j. So any AB in AB_indices that is >= j+2 is valid.

So the latest BA's j is the largest possible. So if the latest BA's j is such that there's an AB after j+1, then return YES.

Similarly, the earliest AB's i is the smallest possible. If there's a BA after i+1, then return YES.

So the steps can be:

Check if earliest AB exists, and the earliest BA after i+1.

Or check if latest BA exists, and latest AB after j+1.

Wait, perhaps the steps are:

1. Collect AB_indices and BA_indices. If either is empty, return NO.

2. Check if the earliest AB (AB_earliest) has any BA in BA_indices that starts at >= AB_earliest +2. If yes, return YES.

3. Check if the earliest BA (BA_earliest) has any AB in AB_indices that starts at >= BA_earliest +2. If yes, return YES.

4. Check if the latest AB (AB_latest) has any BA in BA_indices that starts <= AB_latest -2. That is, BA starts before AB_latest -1, so BA ends at BA_start +1 <= AB_latest -1. So AB starts at AB_latest >= BA_start +2. But this would be BA followed by AB. Wait, no. Because AB_latest is the latest AB. So if there's a BA that starts at some j where j +1 < AB_latest. Then BA is before AB, and AB starts at AB_latest >= j+2. So BA is at j, and AB is at AB_latest >= j+2.

But the latest AB is the last possible AB. So if there's a BA that is before the latest AB, and the latest AB starts >= BA's start +2, then that's a valid pair.

So perhaps check if the latest AB is after a BA. So find any BA in BA_indices that starts <= AB_latest -2.

So the BA starts at j, AB starts at i (AB_latest). So i >= j+2.

So BA starts at j <= i-2.

But how to find if there exists a BA in BA_indices where j <= i-2.

Which can be done by checking if the first BA in BA_indices is <= i-2. But no. Because the BA could be anywhere before i-1.

Wait, for the latest AB (i), if there exists a BA that starts at j <= i-2, then the BA is at j and j+1, and the AB is at i and i+1. So BA ends at j+1 <= i-2 +1 = i-1. So AB starts at i >= j+2. So no overlap.

So for this case, check if BA_indices has any element <= i-2.

Since BA_indices are sorted, the latest BA that is <= i-2 is the largest such j. So if BA_indices has any elements <= i-2, then the answer is YES.

But how to check that.

We can binary search BA_indices for the largest j <= i-2. If such a j exists, return YES.

Similarly, for the latest BA (j), check if there exists an AB in AB_indices >= j +2.

So the steps would be:

Check the following four possibilities:

a) The earliest AB has a BA after it.

Check if BA_indices has any element >= earliest_ab + 2.

b) The earliest BA has an AB after it.

Check if AB_indices has any element >= earliest_ba + 2.

c) The latest AB has a BA before it.

Check if BA_indices has any element <= latest_ab -2.

d) The latest BA has an AB after it.

Check if AB_indices has any element >= latest_ba + 2.

If any of these four conditions is true, return YES. Else, return NO.

But why would this cover all possible cases? Let's see.

Suppose there exists an AB followed by BA (non-overlapping). Then, earliest_ab is the first occurrence of AB, and there exists a BA after it. So condition a) would find it.

Or if the latest BA has an AB after it (condition d), but the latest BA is the last occurrence, then even if the earliest AB didn't have a BA after, the latest BA might have an AB after.

Alternatively, consider a case where the earliest AB is at i, but no BA after. But there's a BA at j where j is before another AB at k >= j+2.

For example:

BA at j=0, AB at k=2. So BA is at 0-1, AB at 2-3. They are non-overlapping. So in this case, condition c) (latest AB is at 2, check if any BA <= 0 (since latest_ab-2 is 0). So BA at 0 would satisfy condition c).

Similarly, if there's a BA followed by AB, then either condition b) (earliest BA followed by any AB) or condition d) (latest BA followed by any AB) would cover it.

Hmm. But how to confirm that the four conditions cover all possibilities.

Alternatively, perhaps we can check the following two possibilities:

1. There exists an AB followed by a BA (non-overlapping).

   - Check if the earliest AB has a BA after it (condition a), or the latest BA is after the earliest AB (but not necessarily the latest BA is after earliest AB +2. Hmm, no.)

   So perhaps condition a) is sufficient for this case.

2. There exists a BA followed by an AB (non-overlapping).

   - Check if the earliest BA has an AB after it (condition b), or the latest AB is after the earliest BA (but again, not necessarily after +2).

Alternatively, perhaps the two possibilities can be covered by checking:

If the earliest AB has a BA after it, or the earliest BA has an AB after it.

But that may not cover all possibilities.

Alternatively, perhaps checking the earliest AB and the latest BA.

Wait, perhaps this approach is sufficient:

Check if the earliest AB is followed by any BA (even after other ABs). So for the earliest AB, check if there's a BA in the BA_indices that starts at >= earliest_ab +2. If yes, return YES.

Else, check if there's a BA in BA_indices which is followed by an AB that starts at BA_start +2 or later. So check if the earliest BA has any AB after it, or the latest BA has any AB after it.

But how to efficiently check that.

Alternatively, for the BA followed by AB case:

Check if the latest BA is followed by an AB. So check if there's an AB in AB_indices that starts >= latest_ba +2.

If yes, return YES.

So combining these two:

Check if earliest AB is followed by a BA (condition a), or latest BA is followed by an AB (condition d). If either is true, return YES.

But would this cover all possible cases?

Let's think of a case where there's an AB followed by a BA, but the earliest AB is not the one that pairs, but a later AB does.

For example:

AB occurs at positions 2, 5, 7. BA occurs at 0, 3, 8.

The earliest AB is at 2. The BA after 2 would be BA at 3 (starts at 3 >= 2+2? 2+2=4. BA at 3 starts at 3, which is less than 4. So not allowed. Then BA at 8: 8 >= 2+2=4. So yes. So earliest AB (2) has BA at 8. So condition a) would find it.

But what if there's another AB at 5, which has BA at 3. No, because BA starts at 3, which is 5's start-2=3. So 5-3=2. So BA starts at 3, AB starts at5. 3+1 =4 <5. So non-overlapping. So in this case, AB at5 and BA at3. But BA occurs before AB. So this would be covered under BA followed by AB.

In this case, the latest BA is 8. Check if there's an AB after 8+2=10. But AB is at7, which is before 10. So condition d) would not find it.

But the AB at5 and BA at3 would require that there's a BA (3) followed by an AB (5 >=3+2=5. 5 >=5 → yes). So BA at3 is followed by AB at5.

But in this case, the earliest BA is 0. So condition b) would check if there's any AB after earliest BA (0) +2=2. AB at2 is >=2. So yes. So condition b) would be true.

But wait, in this example, the earliest BA is 0. So condition b) is checking if there's an AB in AB_indices >=0+2=2. The ABs are at2,5,7. So yes. So condition b) returns yes.

So the problem is, this approach checks the earliest AB and earliest BA, and the latest BA and latest AB.

But perhaps checking the earliest AB and earliest BA is sufficient.

But let's see another example.

Suppose the string is BAAB:

Indices 0: BA, 2: AB.

Here, BA occurs at0, AB at2.

The earliest BA is0. Check if AB occurs at >=0+2=2. AB is at2. So yes. So condition b) returns yes.

Another example: ABBA.

AB occurs at0, BA occurs at2. So answer is yes. The earliest AB is0. BA occurs at2 >=0+2. So condition a) is yes.

Another example: BACFAB (sample input 2).

AB occurs at4 (s[4] is A, s[5] is B).

BA occurs at0 (s[0] B, s[1] A). Also, BACFAB: positions 0-1 BA, then 4-5 AB.

So earliest AB is4. BA occurs at0. So for AB followed by BA, the earliest AB is4. BA after 4+2=6 is not possible. But BA occurs at0. But in the case of BA followed by AB, the earliest BA is0. Check if AB occurs at >=0+2=2. AB occurs at4. So yes. So condition b) returns yes.

So the sample input 2 would trigger condition b) and return yes.

Another example: ABA (sample input 1). AB occurs at0, BA occurs at1. Check if earliest AB (0) has BA at >=2. BA occurs at1, which is less than 2. So no. Check earliest BA (1) has AB >=3. No. So returns no.

So the approach of checking the earliest AB and earliest BA, along with latest BA and latest AB, may cover all cases.

But how to code this.

So the steps would be:

1. Collect AB_indices and BA_indices.

2. If either is empty, return NO.

3. Check if any of the following is true:

   a. There exists a BA in BA_indices that is >= earliest AB +2.

   b. There exists an AB in AB_indices that is >= earliest BA +2.

   c. There exists a BA in BA_indices that is <= latest AB -2.

   d. There exists an AB in AB_indices that is >= latest BA +2.

If any of a, b, c, d is true, return YES. Else, NO.

Wait, but perhaps this covers all possibilities.

For example, in case of BA followed by AB where BA is not earliest but latest, and AB is not earliest but exists.

But perhaps the code can be optimized to check these four conditions.

To check these four conditions:

For a) earliest AB is ab_earliest = AB_indices[0].

Check if there's any BA in BA_indices >= ab_earliest +2.

For b) earliest BA is ba_earliest = BA_indices[0].

Check if there's any AB in AB_indices >= ba_earliest +2.

For c) latest AB is ab_latest = AB_indices[-1].

Check if there's any BA in BA_indices <= ab_latest -2.

For d) latest BA is ba_latest = BA_indices[-1].

Check if there's any AB in AB_indices >= ba_latest +2.

If any of these four is true, return YES.

Because:

a) handles AB followed by BA where the earliest AB has a BA after.

b) handles BA followed by AB where the earliest BA has an AB after.

c) handles BA followed by AB where the latest AB has a BA before.

d) handles BA followed by AB where the latest BA has an AB after.

So why would these four conditions cover all possibilities?

Let's see.

Case 1: There exists an AB followed by BA (non-overlapping).

In this case, the AB could be the earliest AB. So condition a) will be true.

If the AB is not the earliest, but there's a BA after it, then the earliest AB is before this AB. But the earliest AB's BA after may or may not exist. However, if there's a BA after this AB, then the earliest AB's BA may also exist. For example, if there's AB at i=5 followed by BA at j=7, but the earliest AB is at i=0. If there's no BA after i=0, but there is BA at j=7. Then condition a) would not be triggered. But condition d) would check if the latest BA is j=7 and see if there's an AB after 7+2=9. Which there is not. So condition d) not met. But the original AB is at5, BA at7. How is this case covered?

Ah, here's a problem. The AB at5 and BA at7 would form a valid pair (AB starts at5, BA starts at7. 5+2=7 → BA starts at7 >=5+2=7. So yes. So condition a) would check the earliest AB (i=0) and look for BA >=0+2=2. But in this case, BA at7 is >=2. So condition a) would be true, even though the AB in question is at5.

Wait, no. Because the earliest AB is at0. So condition a) checks if there's a BA >=0+2=2. Since BA is at7, this is true. So the code would return YES even though the AB at0 may not have any BA after. But in reality, the AB at0's BA after is at7. So the code would return YES, which is correct. Because the earliest AB and the BA at7 form a valid pair.

So in this scenario, condition a) would correctly find a BA after the earliest AB.

So even if the AB that forms the pair is a later one, the earliest AB's possible BA after would have been found.

So, perhaps the four conditions are sufficient.

So the code can proceed as follows:

Collect AB_indices and BA_indices.

If either is empty, return NO.

Check the four conditions.

Now, how to implement this.

For each of the four conditions, we can use binary search to check.

For example, for condition a:

We have ab_earliest = AB_indices[0].

We need to check if there exists a BA in BA_indices that is >= ab_earliest +2.

Since BA_indices is sorted, we can binary search for the first element >= ab_earliest +2. If such an element exists, return YES.

Similarly for the other conditions.

So the code in Python could be:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    ab_indices = []
    ba_indices = []

    n = len(s)
    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'B':
            ab_indices.append(i)
        elif s[i] == 'B' and s[i+1] == 'A':
            ba_indices.append(i)

    if not ab_indices or not ba_indices:
        print("NO", file=output_stream)
        return

    # Check condition a: earliest AB followed by BA
    ab_earliest = ab_indices[0]
    pos = bisect.bisect_left(ba_indices, ab_earliest + 2)
    if pos < len(ba_indices):
        print("YES", file=output_stream)
        return

    # Check condition b: earliest BA followed by AB
    ba_earliest = ba_indices[0]
    pos = bisect.bisect_left(ab_indices, ba_earliest + 2)
    if pos < len(ab_indices):
        print("YES", file=output_stream)
        return

    # Check condition c: latest AB has BA before
    ab_latest = ab_indices[-1]
    pos = bisect.bisect_right(ba_indices, ab_latest - 2)
    if pos > 0:
        print("YES", file=output_stream)
        return

    # Check condition d: latest BA followed by AB
    ba_latest = ba_indices[-1]
    pos = bisect.bisect_left(ab_indices, ba_latest + 2)
    if pos < len(ab_indices):
        print("YES", file=output_stream)
        return

    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
BACFAB
""",
            "output": \
"""\
YES
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
import bisect


def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    ab_indices = []
    ba_indices = []

    n = len(s)
    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'B':
            ab_indices.append(i)
        elif s[i] == 'B' and s[i+1] == 'A':
            ba_indices.append(i)

    if not ab_indices or not ba_indices:
        print("NO", file=output_stream)
        return

    # Check condition a: earliest AB followed by BA
    ab_earliest = ab_indices[0]
    pos = bisect.bisect_left(ba_indices, ab_earliest + 2)
    if pos < len(ba_indices):
        print("YES", file=output_stream)
        return

    # Check condition b: earliest BA followed by AB
    ba_earliest = ba_indices[0]
    pos = bisect.bisect_left(ab_indices, ba_earliest + 2)
    if pos < len(ab_indices):
        print("YES", file=output_stream)
        return

    # Check condition c: latest AB has BA before
    ab_latest = ab_indices[-1]
    pos = bisect.bisect_right(ba_indices, ab_latest - 2)
    if pos > 0:
        print("YES", file=output_stream)
        return

    # Check condition d: latest BA followed by AB
    ba_latest = ba_indices[-1]
    pos = bisect.bisect_left(ab_indices, ba_latest + 2)
    if pos < len(ab_indices):
        print("YES", file=output_stream)
        return

    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
AXBYBXA
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

Sample input3: AXBYBXA → no AB or BA.

So ab_indices and ba_indices are empty. Output no.

Another test case: ABBA.

ab_indices = [0], ba_indices=[2].

Condition a: check BA >=0+2=2. BA_indices[0]=2. So pos=0. 0 <1 → yes. So condition a is true. So output yes.

Another test case: BAAB.

ab_indices = [2], ba_indices=[0].

Condition a: ab_earliest=2. BA must be >=4. BA_indices has 0. No.

Condition b: ba_earliest=0. AB >=2. ab_indices has 2. So yes.

Another test case: ABABAB → AB occurs at 0,2,4; BA occurs at1,3,5.

Condition a: ab_earliest=0. Check BA >=0+2=2. BA_indices are [1,3,5]. The first BA >=2 is at3 (index1 in BA_indices). So yes.

So code would return yes.

Another test case: AB followed by BA with overlapping. Like ABBA.

Which is handled correctly.

Now, what about a case where the earliest AB doesn't have a BA after, but a later AB does.

For example:

AB occurs at 0 and 3. BA occurs at4.

Condition a: earliest AB is0. Check BA >=0+2=2. BA is at4. So yes. So code returns yes.

Another case: AB occurs at3, BA occurs at0 and 5.

Then condition a: earliest AB is3. BA must be >=5. BA at5 is >=5. So yes.

But code would check condition a: earliest AB (3) +2=5. BA_indices have 0 and5. bisect_left(5) on BA_indices returns 1 (since 5 is at index1). 1 <2 → yes.

So code returns yes.

So the code should handle all cases.

Now, time and memory constraints.

The code runs in O(n) time for collecting the indices. Then, for each of the four conditions, a binary search (O(log k) where k is the size of the indices lists). So overall O(n + 4 log k) → O(n), which is acceptable for n=1e5.

Memory-wise, storing the indices lists could be up to O(n) in worst case (if every pair is AB or BA). For n=1e5, this would be 1e5 elements per list, which is acceptable for Python.

Thus, this approach should be optimal.
</think>

```python
import bisect

s = input().strip()
ab_indices = []
ba_indices = []

n = len(s)
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'B':
        ab_indices.append(i)
    elif s[i] == 'B' and s[i + 1] == 'A':
        ba_indices.append(i)

if not ab_indices or not ba_indices:
    print("NO")
else:
    # Check earliest AB followed by BA
    ab_earliest = ab_indices[0]
    pos = bisect.bisect_left(ba_indices, ab_earliest + 2)
    if pos < len(ba_indices):
        print("YES")
        exit()
    
    # Check earliest BA followed by AB
    ba_earliest = ba_indices[0]
    pos = bisect.bisect_left(ab_indices, ba_earliest + 2)
    if pos < len(ab_indices):
        print("YES")
        exit()
    
    # Check latest AB has BA before
    ab_latest = ab_indices[-1]
    pos = bisect.bisect_right(ba_indices, ab_latest - 2)
    if pos > 0:
        print("YES")
        exit()
    
    # Check latest BA followed by AB
    ba_latest = ba_indices[-1]
    pos = bisect.bisect_left(ab_indices, ba_latest + 2)
    if pos < len(ab_indices):
        print("YES")
        exit()
    
    print("NO")
```
