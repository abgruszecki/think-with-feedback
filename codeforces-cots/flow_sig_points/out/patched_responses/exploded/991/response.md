<think>
Okay, let's see. The problem is about finding the minimal number of layers needed to draw all possible segments between 0 and N (inclusive) such that no two segments in the same layer overlap. Oh right, they can touch at endpoints but not overlap. So each layer can have non-overlapping segments.

First, I need to understand how the segments are arranged. For a given N, the number of segments is N*(N+1)/2. But the arrangement into layers depends on how they can be packed without overlapping.

Let me think about small examples to find a pattern.

For N=2, the example output is 2. Let's list all the possible segments. They are:

0-0 (length 0, just a point?), but maybe considering segments as [a,b] where a <= b, so for N=2, the possible segments are [0,0], [0,1], [0,2], [1,1], [1,2], [2,2]. Wait, but when you have a segment from a to b where a <= b, the total count is (N+1)*(N+2)/2 / 2? Wait, no. Wait, the number of segments is the same as the number of possible pairs (a, b) where a <= b. For N=2, the points are 0,1,2. The possible segments are (0,0), (0,1), (0,2), (1,1), (1,2), (2,2). So 6 segments. Which is 3*4/2 = 6. So yes, the formula given in the problem is correct.

Now, how to arrange these into layers. The minimal layers needed. For N=2, the answer is 2. Let's see how. The layers could be:

Layer 1: [0,0], [0,2], [1,1], [2,2] (but wait, [0,2] is a long segment covering 0 to 2. If another segment is in the same layer and overlaps, that's not allowed. So maybe the layers are divided based on the length of the segments. Alternatively, maybe there's a pattern related to the maximum number of overlapping segments at any point.

Alternatively, for each point x in the coordinate axis, what's the maximum number of segments that cover x. Then the minimal number of layers required would be the maximum of these counts. Because each layer can have at most one segment covering x. So the maximum number of overlapping segments at any point x would dictate the minimal layers needed.

For example, for N=2, consider the middle point 1. How many segments cover 1? Let's see:

Segments [0,1], [0,2], [1,1], [1,2]. So at x=1, there are four segments. Wait, but how? The segment [0,1] covers x=0 and 1. The segment [0,2] covers 0,1,2. [1,1] is just x=1. [1,2] covers x=1 and 2. So at x=1, all four of these segments include it. So the maximum count here would be 4. But the example output is 2. Hmm, that's conflicting. So this approach might not be correct.

Wait, maybe my initial assumption is wrong. Let's think again. The minimal number of layers is the maximum number of overlapping segments at any point on the axis. Because each layer can have at most one segment covering that point. So if at some x, there are k overlapping segments, then we need at least k layers. And if we can arrange the segments such that this maximum is achieved, then that's the minimal possible.

But in the N=2 example, according to the example, the answer is 2. But according to x=1, the overlapping count is 4. So this approach must be incorrect.

Hmm. So what's wrong here. Let's re-examine the N=2 example. Wait, the example's output is 2. So perhaps the maximum number of overlapping segments is 2. But how?

Wait maybe I miscalculated the overlapping segments. Let's list all the segments for N=2:

Segments and their coverage:

0-0: covers x=0.

0-1: covers 0 and 1.

0-2: covers 0,1,2.

1-1: x=1.

1-2: x=1 and 2.

2-2: x=2.

Now, let's check for each x:

x=0: covered by 0-0, 0-1, 0-2. So 3 segments.

x=1: covered by 0-1, 0-2, 1-1, 1-2. That's 4.

x=2: covered by 0-2, 1-2, 2-2. 3.

So maximum is 4. But the answer is 2. So clearly, the maximum number of overlapping segments is not the correct approach. So the initial assumption is wrong.

Hmm. So what's the correct approach here?

Alternative approach: think about arranging the segments in layers such that no two in the same layer overlap. So the problem is equivalent to scheduling intervals on a line with no overlaps, and finding the minimal number of colors needed in an interval graph coloring problem. Wait, interval graph coloring! Yes, that's right. Because each segment is an interval, and overlapping intervals cannot be in the same layer. The minimal number of layers needed is the minimal number of colors in a valid coloring of the interval graph, which is equal to the graph's chromatic number. For interval graphs, the chromatic number equals the maximum clique size. And the maximum clique size in an interval graph is the maximum number of overlapping intervals at any point. So the initial approach was correct, but perhaps the example's explanation is different.

Wait, but in the N=2 case, according to this, the maximum clique size is 4, but the example's answer is 2. That's a contradiction. So there's a mistake here. Therefore, perhaps the problem isn't equivalent to interval graph coloring. Or perhaps the initial analysis is incorrect.

Wait wait, no. Wait, in the N=2 example, the answer is 2. But according to the interval graph approach, the maximum number of overlapping intervals is 4, so the answer should be 4. But that's not matching. So clearly, there's an error in my reasoning.

Ah, but wait! Wait, the problem counts segments as endpoints between integer points. So perhaps the segments are considered as intervals on the real line, but between integer coordinates. For example, the segment [a, b] is from a to b, and includes all real numbers x such that a ≤ x ≤ b. But overlapping segments would share some real number x. So in that case, two segments [a,b] and [c,d] overlap if there's an x where both include x, i.e., their intervals intersect.

But in the example N=2, the answer is 2. Let's see the sample input and output. For N=2, the output is 2. So how is that possible?

Wait, maybe the example explanation gives a way to arrange the segments into 2 layers. Let's think.

Suppose for N=2, the layers can be:

Layer 1:

[0,0], [1,2], [0,2]

Layer 2:

[0,1], [1,1], [2,2]

Wait, but [0,2] is a segment that covers 0 to 2. So in layer 1, if we have [0,2], then no other segments can be in that layer except those that don't overlap with it. But [0,0] is a point (maybe treated as a zero-length segment). So if [0,0] is in the same layer as [0,2], they are overlapping because [0,0] is included in [0,2]. So that's not allowed. So perhaps the arrangement is different.

Alternatively, perhaps the problem's segments are considered as points. Wait, but the problem statement says that segments can touch at endpoints but not overlap. So two segments [a, b] and [b, c] can be in the same layer, but [a, c] and [b, d] (with a < b < c < d) would overlap in [b, c], so can't be in the same layer.

But the N=2 example's answer is 2. So perhaps the maximum clique isn't 4. Let's re-examine the intervals.

For N=2, the segments are:

0-0: covers 0 only.

0-1: covers [0,1].

0-2: covers [0,2].

1-1: covers 1.

1-2: covers [1,2].

2-2: covers 2.

So for each point on the real line, how many segments include it?

For x=0: the segments 0-0, 0-1, 0-2. So 3.

For x=0.5: segments 0-1, 0-2. So 2.

For x=1: 0-1, 0-2, 1-1, 1-2. That's 4.

For x=1.5: 0-2, 1-2. So 2.

For x=2: 0-2, 1-2, 2-2. 3.

So the maximum is 4 at x=1. But the answer is 2. So how can this be?

This suggests that the interval graph coloring approach is not applicable here. So perhaps the problem has some other constraints or the way the segments are counted is different.

Wait, perhaps the problem's definition of overlapping is that two segments share a common interior point. So if two segments touch at an endpoint, they are allowed in the same layer.

In other words, segments [a, b] and [b, c] can be in the same layer, as they only touch at b, which is an endpoint. But if two segments have overlapping interiors, then they can't be in the same layer.

In that case, the problem is equivalent to interval graph coloring where two intervals can be in the same color if they do not share any interior points. So the overlapping is defined as having a common interior point.

In such a case, the maximum number of overlapping intervals (sharing a common interior point) would be the chromatic number.

So for N=2, let's re-calculate the maximum number of overlapping intervals (sharing an interior point).

For example, the segment [0,1] has interior (0,1). The segment [1,2] has interior (1,2). So they don't overlap in their interiors. But [0,2] has interior (0,2). So any segment that is entirely inside (0,2) would share an interior point with [0,2]. So segments [0,1], [1,2], [0,2] all have interiors overlapping. Wait, [0,2] includes the entire [0,1] and [1,2] segments. So their interiors would all be part of (0,2). So at any x in (0,1), [0,1] and [0,2] are overlapping. At x in (1,2), [0,2] and [1,2] are overlapping. So in terms of overlapping (interior), the maximum number of overlapping segments is 2.

Wait, maybe for N=2, the maximum number of overlapping intervals (by interior) is 2, leading to the answer of 2 layers. That would align with the sample input.

So let's re-examine the problem's definition of overlapping. The problem says that segments can touch at the endpoints but can't overlap. So overlapping here means that they share at least one point that is not an endpoint of both. So, for example, [0,1] and [1,2] can be in the same layer because they only touch at 1 (the endpoint of both). But [0,2] and [1,1] can be in the same layer since [1,1] is a point and doesn't have an interior. Wait, but [1,1] is a zero-length segment. So any segment that includes 1 in its interior would overlap with [1,1]? Or is [1,1] considered as not overlapping with any other segment except those that also have 1 as their start and end?

This is getting complicated. Let's check the problem statement again.

Problem statement: in each layer, the segments don't overlap (they might touch at the endpoints though). So two segments can be in the same layer if they touch only at endpoints, but not otherwise.

So, overlapping is when their intervals share any point that is not an endpoint for at least one of them.

So for example, [0,2] and [1,1] (the point) would overlap, because [1,1] is a single point. So [0,2] includes 1 as an interior point. So [0,2] and [1,1] cannot be in the same layer. Wait, but [1,1] is a point. So the [0,2] segment includes the point 1 as part of its interior (since 0 < 1 < 2). So the two segments [0,2] and [1,1] would overlap (since 1 is interior to [0,2]). Therefore, they cannot be in the same layer.

But perhaps the [1,1] segment is considered as having no interior. So overlapping would be when two segments have a common interior point. So a zero-length segment (like [a,a]) does not have any interior. So overlapping occurs only when two segments share an interior point.

In that case, [a,a] can be placed in any layer, as it does not overlap with any other segment except those that include a in their interior.

Wait, this is getting a bit unclear. Let's clarify the problem's definition of overlapping:

Segments cannot overlap, but they can touch at the endpoints. So two segments [a,b] and [c,d] are considered overlapping if their intersection contains more than a single point (assuming they are not touching at a single point). Alternatively, they are considered overlapping if there exists a point in their intersection that is not an endpoint of both.

For example:

- [0,2] and [1,1] (the point 1): the point 1 is the endpoint of [1,1], but for [0,2], 1 is an interior point. So the two segments overlap because their intersection is the point 1, which is an endpoint of [1,1] but not of [0,2]. Wait, but according to the problem statement, overlapping is when they share any point that is not an endpoint of both. So in this case, 1 is an endpoint of [1,1], but not of [0,2]. So the two segments share a point which is an endpoint of one but not the other, so they do overlap. Hence, they can't be in the same layer.

Alternatively, perhaps the definition is that two segments are considered overlapping if their intersection has a non-zero length. But this is not the case for [1,1], which is a point.

This is quite ambiguous. So perhaps the problem's definition of overlapping is that two segments [a, b] and [c, d] are considered overlapping if there exists at least one integer point x (since all endpoints are integers) such that x is strictly between a and b (i.e., a < x < b) and also between c and d (i.e., c < x < d). Because all the segments' coordinates are integers.

Wait, but in that case, two segments [0,2] and [1,1] would have overlapping if any integer x exists in their interiors. The [0,2] segment includes x=1 as an interior point (since 0 < 1 < 2). But the [1,1] segment has no interior (since a = b =1). So their interiors don't overlap. So [0,2] and [1,1] would be allowed in the same layer.

But according to the problem's sample input N=2, how is the answer 2? Let's think again.

For N=2, the possible segments are:

Segments with a=0:

0-0, 0-1, 0-2.

Segments with a=1:

1-1, 1-2.

Segments with a=2: 2-2.

So the total is 6.

Now, the minimal layers needed. Let's try to arrange them.

If we can find a way to arrange the segments into 2 layers.

Layer 1:

0-0, 0-2, 1-1, 2-2.

Wait, but 0-2 covers from 0 to 2. The other segments in this layer are 0-0 (point 0), 1-1 (point 1), 2-2 (point 2). But the 0-2 segment would overlap with any other segment that is contained within it. For example, 0-1 is contained within 0-2 and their interiors overlap (since 0 < x <1 is in the interior of both). So in layer 1, if there is 0-2, then no other segments except those that do not have any interior overlapping with it can be in the same layer.

So, perhaps the layers are arranged based on the parity of the segment length. Wait, not sure.

Alternatively, perhaps the minimal number of layers required is equal to the maximal number of overlapping segments at any integer point, considering that overlapping occurs only if two segments have an overlapping interval in their interiors.

Wait, let's re-calculate for N=2:

For each integer x between 0 and 2, count the number of segments that include x in their interior.

For x=0: segments that include x=0 in their interior. Wait, the interior of a segment [a,b] is a < x < b. So for x=0 to be in the interior, the segment must be a <0 <b. But all segments have a and b as integers between 0 and 2. So there's no segment that includes 0 in its interior. Because the segment would have to start before 0 and end after 0, but the endpoints are all >=0.

Similarly, for x=1: how many segments have x=1 in their interior (i.e., a <1 <b).

Segments where a <1 <b would have a=0 and b=2 (0-2) is the only one. Because 0 <1 <2. Also, segments like 0-1 have b=1, so 1 is the end. So x=1 is not in the interior of 0-1.

Similarly, 1-2: a=1, b=2. x=1.5 is in the interior, but for integer x=1, it's an endpoint.

So for x=1 (integer), the only segment that has x=1 in the interior is 0-2. So the count here is 1. For x=1.5 (non-integer), the segments 0-2 and 1-2 include x=1.5. So for non-integer x, the maximum number of overlapping segments could be higher. But if the problem's definition of overlapping is based on overlapping at any real point (including non-integers), then the maximum number of overlapping segments would be higher.

But according to the problem's sample input N=2, the answer is 2, which suggests that for N=2, the maximum number of overlapping segments (sharing an interior real point) is 2.

Wait, let's re-examine for N=2:

Segments:

0-0: no interior.

0-1: interior is (0,1).

0-2: interior is (0,2).

1-1: no interior.

1-2: interior is (1,2).

2-2: no interior.

So for a point x in (0,1), the segments 0-1 and 0-2 overlap here. So overlapping count is 2. For x in (1,2), segments 0-2 and 1-2 overlap here. So count is 2. For any x in (0,2) but not in (0,1) or (1,2), like x=0.5, it's covered by 0-1 and 0-2. So overlapping count is 2. So the maximum is 2, which matches the sample output of 2.

Ah, so this must be the key. The minimal number of layers is equal to the maximum number of segments overlapping at any real point (considering their interiors). Because each layer can contain at most one segment covering that point.

So for N=2, the maximum is 2, hence the answer is 2.

For N=3, the sample output is 4. Let's see why. Let's calculate the maximum number of overlapping segments in their interiors.

For N=3, the segments are [0,0], [0,1], [0,2], [0,3], [1,1], [1,2], [1,3], [2,2], [2,3], [3,3].

Let's pick a point x in (1,2). How many segments include x in their interiors? Let's see:

Segments that start before 1 and end after 2. So:

0-3 (covers (0,3) → x is in it).

0-2 (covers up to 2, x is 1.5, which is in (0,2) → yes.

0-1 is (0,1), x is 1.5, so no.

1-2: (1,2), x is inside → yes.

1-3: (1,3) → x is inside → yes.

2-3: starts at 2, so x is 1.5 is not covered.

So for x=1.5, the segments that include it are 0-3, 0-2, 1-2, 1-3. That's 4 segments. Hence the maximum is 4, so the answer is 4 for N=3. Which matches the sample.

Similarly, for N=4, the sample output is 6. Let's check:

At x=2.5 (midpoint between 2 and 3), how many segments include this point in their interiors?

Segments that start before 2.5 and end after 2.5.

These include:

Segments with a ≤2 and b ≥3.

For N=4:

Segments like 0-4 (covers 0-4, so x=2.5 is inside).

0-3: covers 0-3 → includes 2.5.

0-2: no, ends at 2.

1-3: starts at 1, ends at 3 → yes.

1-4: ends at 4 → yes.

2-3: covers 2-3 → x=2.5 is inside.

2-4: yes.

3-3: no.

So let's see:

For x=2.5 in N=4:

Segments that include x in their interior are:

0-4, 0-3, 1-3, 1-4, 2-3, 2-4. That's 6 segments. Hence the maximum is 6, which matches the sample output.

So the pattern seems to be that for a given N, the maximum number of overlapping segments is equal to the number of pairs (i,j) where i < x < j, and x is a midpoint between two integers, perhaps. Or more generally, the maximum occurs at a point x where x is a half-integer (like 0.5, 1.5, etc.), which maximizes the number of segments that include x in their interiors.

So the problem reduces to finding the maximum number of segments that cover any point x in their interiors. The minimal number of layers is equal to this maximum.

Now, how to compute this maximum for a given N.

Let's model the segments as intervals (a, b), where a and b are integers, 0 ≤ a ≤ b ≤ N. A segment [a, b] contributes to the count for x if a < x < b.

For a given x, how many segments (a, b) satisfy a < x < b.

To find the maximum such count over all x in real numbers.

But since x is a real number, the maximum will occur at a point where x is not an integer. Because between two integers, the count can be higher.

For example, between a and a+1, the maximum for x in that interval is the number of segments that start before a+1 and end after a.

Wait, perhaps we can model this as follows:

For any integer k between 0 and N-1, the maximum number of segments that include a point x in the interval (k, k+1) is equal to the number of segments with a ≤ k and b ≥ k+1. Because for x in (k, k+1), a <x implies a ≤k (since x is greater than k), and x <b implies b ≥k+1 (since x is less than k+1). So the count is the number of segments (a, b) where a ≤k and b ≥k+1.

So for each k from 0 to N-1, compute the number of such segments. The maximum of these values is the required answer.

Because the maximum number of segments covering any x in (k, k+1) is equal to the number of segments that start at or before k and end at or after k+1.

So, for each k in 0..N-1:

count = (number of a's <=k) * (number of b's >=k+1)

Because for a given a (<=k), the possible b's are from k+1 to N. So the number of possible b's is N - (k+1) +1 = N -k.

The number of a's <=k is k+1 (since a can be 0,1,...,k).

The number of b's >=k+1 is (N - (k+1) +1) = N -k.

So for each k, the count is (k+1) * (N -k).

Thus, the maximum over all k of (k+1)*(N -k) is the answer.

So the problem reduces to computing the maximum value of (k+1)*(N-k) for k in 0 ≤k ≤N-1.

Let's test this for the sample inputs.

Sample Input 2 (N=2):

k ranges from 0 to 1.

k=0: (0+1)*(2-0) =1*2=2.

k=1: (1+1)*(2-1) =2*1=2.

Maximum is 2. Which matches the sample output.

Sample Input 3 (N=3):

k ranges 0,1,2.

k=0: 1*3=3.

k=1: 2*2=4.

k=2:3*1=3.

Maximum is 4. Which matches the sample.

Sample Input4 (N=4):

k ranges 0,1,2,3.

k=0:1*4=4.

k=1:2*3=6.

k=2:3*2=6.

k=3:4*1=4.

Maximum is 6. Which matches the sample.

So the formula holds.

Thus, the solution is to compute the maximum of (k+1)*(N-k) for k from 0 to N-1.

The maximum occurs when k is the floor of (N-1)/2. But since N can be up to 100, it's easy to compute the maximum by iterating all possible k.

So the code is straightforward: loop through all k in 0 to N-1, compute (k+1)*(N-k), find the maximum value.

Thus, the code can be written as:

Read N, compute max over k=0..N-1 of (k+1)*(N-k).

So for N=100, the maximum will be at k=49 and k=50. For example, when N is even, say N=2m, then k=m-1 and k=m give (m)*(m+1) and (m+1)*(m). Both are same. So maximum is (m)*(m+1).

For N=100 (even):

m=50.

max is 50 *50=2500? Wait, wait, N=100, k=50 would be (50+1)*(100-50)=51*50=2550. Or wait, N=100 is even, so m=50. The maximum would be at k=49 and 50?

Wait, let's compute for N=4:

k=1: (2) *3 =6.

k=2:3 *2=6.

So for even N, the maximum is (N/2) * (N/2 +1) ? Or no.

Wait N=4:

N=4 is even. For k=1, (1+1)*(4-1)= 2*3=6. For k=2, 3*2=6. So maximum is 6.

Which is (4/2) * (4/2 +1) = 2*3=6. So yes.

For N=100: even, m=50. So maximum is (50) * (50) +50? Wait no. Wait for k=49: (49+1) * (100-49) =50 *51=2550. For k=50:51 *50=2550. So the maximum is 2550.

Which is (50) *51.

So the code can compute this quickly.

Thus, the code is simple: compute the maximum of (k+1)*(N -k) for k in 0 to N-1.

So the code can be written as:

Read N.

max_val = 0

for k in range(N):

    current = (k+1)*(N -k)

    if current > max_val:

        max_val = current

print(max_val)

Wait, but k ranges from 0 to N-1. Because the interval is between k and k+1, which for k= N-1 is between N-1 and N. So the loop should be for k in 0 to N-1.

In Python, for N=2, the loop is k in 0 and 1.

Which is correct.

So the code is correct.

Thus, the solution is to compute this maximum value.
</think>

```python
n = int(input())
max_layers = 0
for k in range(n):
    current = (k + 1) * (n - k)
    if current > max_layers:
        max_layers = current
print(max_layers)
```