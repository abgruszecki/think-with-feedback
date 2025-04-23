<think>
Okay, let's see. The problem is about finding the lex smallest array possible by swapping elements whose sum is odd. Hmm. So the key is understanding what swaps are possible here.

So, swapping two elements when their sum is odd. That means one is even and the other is odd. Because even + odd = odd. Right. So the operation allows swapping an even and an odd element. Wait, but once you swap them, the parity of their positions changes. Wait, no. Let's think: if you have two elements, one even and one odd, their sum is odd. So you can swap them. After swapping, the even is now where the odd was, and vice versa. So in subsequent swaps, those elements can be swapped again as long as their sum is odd. Wait, but after the swap, their sum is even? Wait, no. Wait, the sum of even and odd is odd. So if you swap them, when you swap, the even and odd are in each other's places. So their sum is still even + odd = odd. So you can swap them again. Wait, but in that case, maybe you can perform swaps multiple times between even and odd elements. Wait, but how does that affect the possible permutations of the array?

Wait, maybe the key here is that even and odd elements can be freely reordered among their own parity groups. Because you can use even-odd pairs to swap elements. Let me think. For example, suppose you have even elements E1, E2 and odd elements O1, O2. If you want to swap E1 and E2, but they are both even. How? Since you can't swap them directly. But maybe you can use an odd element as an intermediary. Like, swap E1 with O1 (possible since their sum is odd), then swap O1 with E2 (possible because O1 is now even? Wait, no. Wait, after swapping E1 and O1, O1 is now in E1's position, but it's still odd. Wait, no: O1 is odd. After swapping E1 (even) and O1 (odd), the elements become O1 and E1. So, the swapped elements are O and E. So, when you swap E and O, their sum is odd. Then, after the swap, O is in the even's original position, and E is in the odd's original position.

But how can we use this to move even elements around? Let's say we have E1, E2, O. We want to swap E1 and E2. Here's how: swap E1 and O (sum is odd), which puts O in E1's place and E1 in O's place. Then swap O (now in E1's position) with E2 (even). Their sum is O + E2 (which is odd + even = odd), so that's allowed. Now, E2 is where O was after the first swap, and O is in E2's original position. Then swap E1 (which is now in O's original position) with O (now in E2's position). Wait, sum is even (E1 is even) + odd (O) → sum is odd. So allowed. Now, after these three swaps, E1 and E2 have swapped places. So, through a series of swaps involving an odd element, even elements can be rearranged among themselves. Similarly, odd elements can be rearranged among themselves using even elements as intermediaries.

Wait, so the conclusion here is that if there is at least one even and one odd element in the array, then all evens can be reordered among themselves, and all odds can be reordered among themselves. Because you can use the presence of both parities to perform swaps to move elements around. But if all elements are even, then you can't perform any swaps, so the array remains as is. Similarly, if all are odd, then no swaps can be done either.

So the overall idea is:

- If the array contains both even and odd elements, then the even elements can be sorted in any order, and the odd elements can be sorted in any order. But to get the lex smallest array, we would arrange all evens and odds in sorted order, but interleaved in such a way that the lex order is minimized.

Wait, no. Because the evens and odds can be placed anywhere. Because you can swap any even and odd pair. Wait, but how? Because when you swap even and odd elements, you can permute their positions. So maybe the even and odd elements can be arranged in any order, as long as their parity is preserved. Wait, no. Because when you swap even and odd elements, their positions can be changed. But how does that affect the overall arrangement of parities? Let's see.

Suppose the array has both even and odd elements. Then, the parity of the elements can be rearranged. Wait, no. Because when you swap even and odd elements, their parity remains the same, but their positions are swapped. So the array's parities are a mix of even and odd. For example, if you have a mix of even and odd elements, then any permutation is possible? Or not.

Wait, no. Because the swap operation only allows swapping even and odd elements. Once you swap them, their positions are exchanged, but their parities are the same. So, for example, if you have an even in position 1 and an odd in position 2, you can swap them. Now, the even is in position 2 and the odd is in 1. But you can swap them again. So, the parities of the array elements are fixed. The counts of even and odd elements in the array are fixed. Because each swap exchanges two elements of different parities. So the count of even and odd elements remains the same.

So the key insight here is: the parity of each element in the array is fixed. Even elements stay even, odd elements stay odd. But their positions can be rearranged as long as the swap operations are possible. However, the swap operations can only swap even and odd elements. So, the question is: what permutations can we achieve given these swap operations?

Hmm, this is a crucial point. Let's think of the array as consisting of two groups: even and odd. Let's call them E and O. The swap operation allows swapping any E with any O. Because when you swap E and O, their sum is odd. So, through a series of swaps, can we arrange the E's and O's in any order? For example, can we arrange all E's first, then all O's, or vice versa? Or can we interleave them in any way?

Wait, suppose the array has multiple E's and O's. Let's say E1, E2, O1, O2. The swap operations can swap E1 with O1, then E2 with O2. So the E's can be moved to positions where O's are, and vice versa. So the positions of E's and O's can be rearranged. For instance, you can swap E1 and O1, which puts E1 in O1's position and O1 in E1's. Then swap E2 and O2, putting E2 in O2's position and O2 in E2's. So the E's are now in O's positions, and O's in E's positions. But if you have more E's than O's, then some E's would have to remain in their original group.

Wait, but perhaps the crucial point is that any E can be swapped with any O. So, through a series of swaps, any E can be moved to any position that was originally occupied by an O, and vice versa. For example, let's say there are multiple E's and O's. To move E1 to position j (originally an O's position), you can swap E1 with the O in position j. Then, perhaps other swaps can help in moving other elements around.

But how does this affect the arrangement of E's and O's? For example, if the original array has some E's and O's, can we arrange them in any order by swapping E and O pairs?

Alternatively, perhaps the parity of the elements' positions can be changed. Wait, no. The positions of the elements are indexes, but their parity (even or odd index) isn't directly relevant here. Wait, no. The indexes are just positions. The swap is between any two positions i and j. So, when you swap two elements of different parity, their positions can be anything.

Wait, perhaps the key is that when the array has both even and odd elements, then all even elements can be placed in any positions that originally had even elements or odd elements. Because any even can be swapped with any odd. So, for example, if the array has even elements and odd elements, then through swapping even and odd pairs, we can permute the even elements into any positions, as long as the total number of even and odd elements remains the same. Wait, that might not be correct.

Wait, let's think of it as a graph problem. Each element is a node, and there is an edge between two nodes if they can be swapped. So, two elements can be swapped if they are of different parity. So, in this case, the graph has edges between even and odd elements. So, the connected components are such that all even elements and all odd elements are connected, as long as there is at least one even and one odd. So, if there is even one even and one odd, then all even and all odd elements are in the same connected component. Because any even can be swapped with any odd. So, for example, even elements can be swapped via an odd element. Let's say we have E1, E2, O. To swap E1 and E2:

- Swap E1 and O (allowed because sum is even + odd = odd). Now E1 is in O's position, O is in E1's position.
- Then swap E2 and O (sum is even + odd = odd). Now E2 is in O's current position (which was E1's original), O is in E2's original position.
- Then swap O (now in E2's position) with E1 (now in O's original position). Sum is odd + even = odd. So allowed. Now E1 is in E2's position and E2 is in E1's original position. So overall, E1 and E2 have swapped. So through the presence of an O, two even elements can be swapped. Similarly, two odd elements can be swapped using an even element as an intermediary.

So the conclusion is that if there is at least one even and one odd element in the array, then all elements can be reordered in any way. Wait, really? Because then, any permutation is possible. Because even elements can be moved among themselves by using odd elements as intermediaries, and vice versa. So, the parity of elements is fixed (the count of even and odd elements is fixed), but their positions can be arranged in any order. So the entire array can be sorted in non-decreasing order, regardless of the parity of the elements. Wait, but that contradicts the example given.

Wait, looking at the first example:

Input:
3
4 1 7

The output is 1 4 7.

Wait, the original array is [4 (even), 1 (odd), 7 (odd)]. So there are one even and two odds. According to the previous reasoning, if there is at least one even and one odd, all elements can be arranged in any order. So the lex smallest array would be [1,4,7], which is sorted. Which matches the example. But how is that possible? Because 4 is even, and 1 and 7 are odd. So in the original array, 4 is in position 1. The lex smallest would arrange all elements in order. So how can we arrange the even element (4) to come after the odds (1 and 7)?

Wait, according to the reasoning, since there is at least one even and one odd, all elements can be rearranged. So the entire array can be sorted, and that's the lex smallest. So the solution would be to sort the entire array, but only if there is at least one even and one odd. Otherwise, if all are even or all are odd, then we can't perform any swaps, so the array must remain as is. Wait, but that's not correct. Because in the case where all elements are even, you can't perform any swaps. So the lex smallest array is the original array sorted? No. Because you can't swap elements. So the array must stay as it is. But wait, can you even swap any elements? Because for a swap to be possible, the sum must be odd. So if all elements are even, any two elements sum to even, so no swaps can be done. So the array remains as is. But if all are even and the array isn't sorted, then the answer is the original array. Similarly for all odd elements.

Wait, but in the second example:

Input:
2
1 1

The output is 1 1. Since both are odd, no swaps can be done. So the array remains the same, which is already lex smallest.

So the algorithm is:

- Check if there exists at least one even and one odd element in the array.

If yes:

- Then the entire array can be sorted, resulting in the lex smallest possible.

If no:

- Then the array cannot be modified, so the lex smallest is the original array.

Wait, but that can't be right. Wait, what about a case where the array has both even and odd elements but the lex smallest arrangement requires some even elements to come before some odd elements. For example, [2, 1]. The lex smallest is [1,2]. But according to the reasoning, since there's even and odd, you can swap them. So the sorted array is possible. Which is correct.

Wait, but in the first example, the sorted array is [1,4,7], which is possible because the even element can be placed after the odds. So the algorithm seems to hold.

So the conclusion is: if the array has at least one even and one odd element, then the lex smallest array is the entire array sorted. Otherwise, if all even or all odd, then the array is as is (since no swaps can be done).

But wait, let's test a case where this may not hold. Suppose the array is [3, 2, 5]. So two odds and one even. According to the algorithm, the entire array can be sorted to [2,3,5], which is even followed by odds. But how can the even element end up in the first position?

Wait, according to the swap rules, you can swap even and odd elements. So, in the array [3 (odd), 2 (even),5 (odd)], you can swap 3 and 2 (sum is 3+2=5, odd). Then the array becomes [2,3,5]. Which is sorted. So that's possible.

Another example: [5,3,2]. After sorting, [2,3,5]. But the even element can be moved to the first position via swaps. So the algorithm would sort the entire array, which is correct.

So the algorithm works. So the approach is:

Check if there is at least one even and one odd element. If yes, sort the entire array. Otherwise, output the original array.

But wait, why can't the array be sorted when all elements are even or all are odd? Because you can't perform any swaps. So the array must remain as it was. So, the steps are:

- Count the number of even and odd elements.

- If there are both even and odd elements, sort the entire array.

- Else, the array can't be changed, so output the original array.

But wait, in the case where all elements are even, the array can't be sorted, because you can't perform any swaps. So even if the array is unsorted, you can't change it. So the output is the original array.

But that contradicts the initial example. Wait, no. The first example had a mix, so the array could be sorted. But if the array is all even, you can't swap any elements. So the array must remain as is.

So the code can be written as follows:

Read the array. Check if there are both even and odd elements. If yes, sort and output. Else, output the original array.

But wait, this seems too simple. Let me check the example again.

First example: [4,1,7]. Both even and odd. So sorted array is [1,4,7], which is correct.

Another example: [1,1]. All odd. So output is same as input.

Another test case: [2,4,6]. All even. So output is same as input.

Another case: [3,5,2]. Even and odd. Output sorted array [2,3,5].

But wait, how is this possible? Because in the original array, 3 and 5 are odd, 2 is even. So, can the even element be moved to the first position?

Yes. Because 3 (odd) and 2 (even) can be swapped. So after swapping, array becomes [2,5,3]. Then, 5 (odd) and 3 (odd) can't be swapped directly. But wait, since there's an even element (2), can we use it to swap between odds?

Wait, according to the earlier reasoning, when there's at least one even and one odd, all elements can be permuted. So even if two odds are to be swapped, you can do that via the even element. For example:

Original array: [5,3,2].

We want to swap 5 and 3.

First, swap 5 (odd) and 2 (even). Now array is [2,3,5].

Then, swap 3 (odd) and 2 (even). Now array is [3,2,5].

Then swap 5 (odd) and 2 (even). Now array is [3,5,2].

Wait, this isn't helping. Hmm. So perhaps the initial reasoning was wrong. Because in this case, the two odds (5 and 3) cannot be swapped directly. But maybe with an even element, you can do this.

Wait, let's see. Suppose you have elements A (odd), B (odd), and C (even). How can you swap A and B?

Swap A and C. Now the array is C (even), B (odd), A (odd).

Then swap B and C. Wait, can't do that because B is odd, C is even. Sum is odd. So swap B and C. Array becomes B (odd), C (even), A (odd).

Then swap C and A. Sum is even + odd → odd. Swap them. Array becomes B (odd), A (odd), C (even).

So, after three swaps, we have swapped A and B. So it's possible.

So even though the elements are both odd, you can swap them by using the even element as a temporary intermediary.

Therefore, when there's at least one even and one odd, the entire array can be sorted. So the approach holds.

So the code can be written as:

Read the array.

Check if there's at least one even and one odd.

If yes, sort the array and output.

Else, output the original array.

But wait, in the case where all elements are even, you can't sort the array. For example, the array is [4,2,6]. Original array is already sorted, so output is same. But if the array is [6,4,2], which is all even, then output is [6,4,2], since no swaps can be done.

So the code is straightforward.

Testing this approach against the examples.

First example: 3 elements, 4 (even), 1 (odd), 7 (odd). There are even and odd. So sorted array is [1,4,7]. Correct.

Second example: [1,1]. All odd. Output as is.

Another example: [5,3,2]. Sorted as [2,3,5].

Another example: [3,2,5]. Sorted as [2,3,5].

Another case: [2,1]. Sorted as [1,2].

So the code seems correct.

Now, let's code this.

In Python:

Read n.

Read the array as list.

Check if there's at least one even and one odd.

We can do this by checking the set of a_i % 2. If the set has size 2, then yes.

Otherwise, no.

If yes:

Sort the array and print.

Else:

Print the array as is.

But wait, how about the case where the array is all even except one odd, and vice versa?

No, the code handles that.

Now, considering the constraints. n can be up to 1e5. Sorting is O(n log n), which is acceptable for 1e5, as Python can handle that in the time limit.

So, code:

n = int(input())
a = list(map(int, input().split()))
evens = any(x % 2 == 0 for x in a)
odds = any(x % 2 == 1 for x in a)
if evens and odds:
    print(' '.join(map(str, sorted(a))))
else:
    print(' '.join(map(str, a)))

Yes, this should work.

But wait, the code checks if there are both even and odd elements. If yes, sorts the array, else returns the original.

Testing the code against the examples.

First example:

3
4 1 7

evens is True (4 is even), odds is True (1 and 7). So sorted is [1,4,7]. Correct.

Second example:

2
1 1

evens is False, odds is True. So output is [1,1].

Another test case:

n=5

array [2, 4, 6, 8, 10] → all even. output as is.

Another test case:

n=5 with [1,3,5,7,9] → all odd. output as is.

Another test case with even and odd:

n=4, array [3,5,2,4] → sorted is [2,3,4,5].

Yes.

So the code works.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
has_even = any(x % 2 == 0 for x in a)
has_odd = any(x % 2 == 1 for x in a)
print(' '.join(map(str, sorted(a))) if has_even and has_odd else ' '.join(map(str, a)))
```