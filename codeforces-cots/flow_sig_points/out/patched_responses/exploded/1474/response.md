<think>
Okay, I need to solve this problem where we have to find the maximum possible length of a consecutive G's after swapping at most one S with a G. Let's think about how to approach this.

First, let's understand the problem. The input is a string of G's and S's. We can swap any two characters (not necessarily adjacent) once. Our goal is to maximize the longest run of G's possible after this swap.

Wait, but swapping is only useful if we can replace an S in a possible long sequence of G's with a G from elsewhere. Because if we swap two G's, it doesn't change anything. So the optimal approach must involve swapping an S in a group of G's (with some S's) and a G that's outside of that group.

Wait, but maybe there's a case where there's an S in a run that's between two G runs. For example, if the string is like GGG S GGG, then swapping that S with a G from somewhere (like another S's position, but wait, maybe there's no other Gs. Wait, but the total number of G's is fixed. Hmm.

Alternatively, maybe the optimal approach is to find all the positions of G's, and see if there's a way to merge two adjacent groups of G's by replacing the S in between with a G, and then using an extra G from somewhere else. But how?

Let me think of the possible scenarios.

Case 1: There are no G's. Then the answer is 0. Like the third example.

Case 2: All are G's. Then the answer is n, like the second example.

Otherwise, we have a mix of G and S.

The key is that after swapping an S in a group of G's (if possible) with a G from another position, we can extend the length of the consecutive G's.

Alternatively, if there's an S that's within a group of G's, swapping it with a G that's outside the group can turn that S into a G, thus merging the groups around it.

Wait, but the swap could be between an S in a G group and a G that's in another part. For example, suppose we have GGG S GGG. The middle S is between two G groups. If there's another G somewhere else (but in the example given, the total G's are 6, so swapping the S with that G would make the entire group 6+1=7 G's, but wait, the example in the first input gives a result of 7, which is exactly that.

So, the approach would be to track all the positions of S in the current groups of G's. Then, for each S in a group of G's, see if there's a G elsewhere that can be swapped here, thereby converting that S to a G and allowing the adjacent G groups to merge.

But how do we model this?

Alternatively, here's a standard approach for similar problems (like the maximum consecutive ones problem where you can flip k zeros). The solution uses a sliding window approach where you track the positions of the S's and allow up to k swaps. But in this problem, we can only swap once. However, the twist here is that each swap can replace an S with a G only if there is a G elsewhere to swap with. So the number of available swaps depends on the total number of G's.

Wait, because a swap can only replace an S with a G if there exists at least one S in the array. Wait no, because we can swap any two elements, but to turn an S into a G, there must be a G to swap with. So the total number of G's in the array is fixed. If all elements are G's, then the maximum is n, as in the second example.

So first, we need to count the total number of G's. Let's call it total_g. If total_g is n, then the answer is n.

If total_g is zero, the answer is zero.

Otherwise, the answer is the maximum possible sequence of G's after possibly swapping one S with a G (but we have to ensure that there's an S in the array to swap with a G. Wait, no. Because when we swap two elements, one of them is G and the other is S. So when we do the swap, we can replace an S in a group with a G from elsewhere. But if there are no S's in the array (all G's), then we can't do any swaps. But in that case, the answer is n.

So, the steps are:

1. Compute total_g. If total_g == 0, return 0. If total_g == n, return n.

2. Otherwise, find the maximum length of consecutive G's that can be achieved by swapping one S in a group with a G from outside.

So, the problem reduces to finding the longest possible sequence of G's where at most one S is present, and that S can be swapped with a G from elsewhere. But how to model this?

Alternatively, here's a way to think:

We can imagine that after the swap, the sequence will have an extra G (if we swapped an S in the group with a G outside). But wait, the total number of G's remains the same. Because a swap is between a G and an S. So the swap converts an S into G and a G into S. Wait, no. For example, if the original string is G S, swapping the two gives S G. The total number of G's remains 1.

Wait, no. A swap between two elements (i and j) where one is G and the other is S will change the count of G's only if they are different. Wait, the count of G's is the same as before. Because if you swap a G and an S, you have one less G (the position where G was becomes S) but one more G (the position where S was becomes G). So the total remains the same.

So the total number of G's is fixed. So, when you swap, you can turn an S into a G, but another G into an S. Therefore, the total_g is fixed. So, the maximum possible consecutive G's is min(total_g + 1, ...). Wait, no. Because the swap may not give a longer run. For example, if you have all G's except one S. Then, total_g is n-1. Swapping the S with a G (but there's no other S) would not change the array. Wait, but if the array is all G's except one S, then after a swap, you can move the S to a position that allows the longest possible run of G's. But the total_g remains n-1.

Wait, perhaps the maximum possible length of consecutive G's after swap is either:

- The length of the maximum existing consecutive G's (if we can't swap to improve it), or

- The length of a certain segment that can have an S swapped in.

But how?

Let's think of the approach:

We can look for all intervals where there is exactly one S, and then see if there exists a G outside of this interval. If so, we can swap that S with that G, thereby converting the interval into all G's (but losing one G somewhere else). Wait, but the total_g is fixed, so the interval can have (number of G's in the interval) + 1 (if the swapped S is replaced by a G from outside). But perhaps not.

Alternatively, the sliding window approach: track the maximum window where the number of S's is <= 1. Then, if there are at least one S's in the array (i.e., total_g < n), then the maximum possible window is that window length, but only if there's a G outside the window to swap with the S in the window. Because if the window has one S, we can swap it with a G outside, thereby converting the window into all G's.

So the idea is:

- Find all possible windows with at most one S.

- For each such window, the maximum possible length after swap is the length of the window. But to be able to swap, there must be at least one G outside the window (so that we can swap the S in the window with a G outside). Or, if the window has zero S's, then the maximum length is the window length (no need to swap). But if the window has one S, then to swap it, there must be at least one G outside the window.

Wait, but the window could have one S, and the total_g is the number of G's. The window has (number of G's in the window) + (number of S in the window) = length of window. The S in the window is one. So the number of G's in the window is (window_length - 1). The total_g is the total number of G's in the entire array. So, the number of G's outside the window is total_g - (window_length - 1).

To swap the S in the window (the one S) with a G outside, there must be at least one G outside. So total_g - (window_length - 1) >= 1.

So if that's the case, then the window can be converted to window_length G's. Otherwise, even if we have a window with one S, but there are no G's outside, then swapping the S with a G inside the window is not possible. Wait, but the G's inside the window are already part of the window. So swapping the S in the window with a G inside the window would not change the window's composition. So, in that case, the window would still have one S (since we swap two elements within the window: the S and a G in the window. The S becomes G, but the G becomes S. So the number of G's in the window remains (window_length - 1) + 1 (since S is replaced by G) - 1 (since G is replaced by S). So net change is -1 +1 = 0. So the window would have (window_length -1) G's and 1 S again. So no improvement.

Therefore, for a window with one S, the only way to convert it into all G's is if there's a G outside the window. Then, swapping that S in the window with the G outside would result in the window having (window_length -1 +1) G's, i.e., window_length G's, and the G outside becomes S. But the total_g remains the same.

So the maximum possible length in this case is the window_length, provided that:

- The window has 0 or 1 S.

If the window has 0 S, then the maximum is window_length (no swap needed).

If the window has 1 S, then the maximum is window_length if there exists at least one G outside (so that we can swap the S with that G).

So the algorithm is:

Compute all possible maximum window lengths where the number of S's is at most 1. Then, for each such window, if the number of S's is 0, the contribution is the window length. If the number of S's is 1, the contribution is window length if (total_g >= (number of G's in the window) + 1). Because the number of G's in the window is (window length -1), and the total_g is the sum of G's in the window plus those outside. So:

If window has 1 S:

G_in_window = window_length - 1 (since one S is present)
G_outside = total_g - G_in_window = total_g - (window_length - 1)

We need at least one G outside to swap. So if G_outside >=1, then we can swap and the window becomes all G's. So the possible maximum is window_length.

If G_outside is zero, then we can't swap, so the maximum possible is the original window's G's plus zero (since the S can't be replaced). Wait, no. Because the original window has G_in_window = window_length -1 G's and one S. So the maximum consecutive G's in that window is (window_length -1). But after swapping, if there's no G outside, then swapping that S with a G inside the window would not help. Because that would replace the S with a G (so window now has window_length G's), but the other G becomes S. So the window has (window_length -1 +1) -1 (since one G is swapped out) = window_length -1. So no gain.

So in this case, when the window has one S but no G's outside, the maximum possible for that window is (window_length -1), which is the same as the original.

But that's not better than the existing maximum.

So, the algorithm would be:

- Compute the maximum window length with at most one S.

For each such window:

   if S_count == 0:

      candidate = window_length

   else:

      if (total_g >= (window_length -1 + 1)): i.e., if (total_g >= window_length). Because G_in_window is window_length -1. So G_outside is total_g - (window_length -1). So to have G_outside >=1, we need total_g - (window_length -1) >=1 → total_g >= window_length.

      So when the window has one S, the candidate is window_length if total_g >= (window_length -1) +1 → total_g >= window_length.

Wait, total_g is the total number of G's in the array. So in the window, the number of G's is (window_length -1) (since 1 S). So the number of G's outside is total_g - (window_length -1). For there to be at least one G outside, total_g - (window_length -1) >=1 → total_g >= window_length.

If that's true, then swapping the S in the window with a G outside gives us a window of window_length G's. Otherwise, it's not possible.

So for such a window, the candidate is window_length if total_g >= window_length. Otherwise, it's (window_length -1).

But how do we compute this for all possible windows?

Alternatively, the maximum possible candidate is the minimum between the window length (if possible to swap) and the total_g (since the total number of G's can't exceed total_g). Because the maximum possible consecutive G's can't be more than the total number of G's, because even if all G's are consecutive, that's the length. Wait, no. Because after swapping, the G's can be arranged in a longer consecutive sequence by moving an S that's inside a group. For example, suppose total_g is 5. If they are in two groups separated by S's, but after swapping an S in between with a G elsewhere, the consecutive sequence could be 5. But the total_g is 5, so the maximum possible is 5.

Wait, the maximum possible consecutive G's after any swap can't be more than the total number of G's. Because you can't have more G's than the total. So the maximum possible answer is min(max_window_candidate, total_g).

Wait, that's an important point. For example, if the array is G G G S G G, total_g is 5. The maximum possible after swap is 5. Because you can swap the S with one of the G's, making all G's consecutive.

But the total_g is 5, so the answer is 5. So the maximum possible is the total_g. But in the first example, the input has 7 G's. The output is 7. Which equals total_g.

So, the maximum possible answer is min( the maximum window length with 1 S that can be swapped, or the maximum window with 0 S, but that's already all G's, but if the total_g is higher than that, it's not possible. So the maximum possible answer is the minimum between the maximum possible candidate (from window) and total_g.

So, the approach is:

1. Compute total_g.

2. If total_g is 0 → 0.

   If total_g == n → n.

3. Else, compute the maximum window with at most one S.

   For each such window:

      if the window has 0 S → candidate is window length.

      else (1 S):

          if total_g >= window_length → candidate is window_length.

          else → candidate is (window_length -1 + (1 if there's a G outside else 0)).

          Wait, maybe not. Because if the window has 1 S, but the total_g is less than the window_length, then even after swapping, the maximum is window_length. Wait, no. Because total_g is the total number of G's. So if the window has window_length, which requires that the entire window becomes G's. But the total number of G's is total_g. So if the window_length is larger than total_g, then that's impossible, because we can't have more G's in the window than the total.

Wait, this is a critical point. Let's think again.

Suppose the window is of length L and has 1 S. Then, the maximum possible consecutive G's after swapping is L only if there's a G outside to swap with. But if the total_g is >= L → because:

In the window, there are L-1 G's and 1 S. The total_g is T. The number of G's outside the window is T - (L-1). For there to be a G outside, T - (L-1) >=1 → T >= L.

If T >= L, then swapping the S in the window with a G outside gives us L G's in the window. But since T is the total number of G's, this is possible only if T >= L. Because the window is length L, but after swap, all L positions are G's, which requires T >= L. Because the total number of G's is T, so the maximum possible consecutive G's after swap cannot exceed T.

So, for the window with 1 S, the candidate is min(L, T) if T >= L. Or if T < L, then even if we swap, the maximum possible is T (since all G's in the array can be consecutive). But how?

Wait, maybe the candidate in that case is (L -1) + 1 (from swapping) → but that would require that there's a G outside. But if T is less than L, then T - (L-1) (number of G's outside) is T - (L-1). Since T < L, T - (L-1) is negative. Which is impossible. So in that case, there are no G's outside. So swapping is impossible. So the candidate for the window is (L-1).

So putting it all together:

For each window with 1 S:

   if total_g >= (L-1) +1 → T >= L → then candidate is L.

   else → candidate is (L-1).

But the total_g is T. So the candidate for such a window is min(L, T) if there's a G outside (T >= L), else (L-1).

But how to compute this?

Alternatively, the maximum possible answer is the minimum between the maximum window length (after considering possible swaps) and the total number of G's.

So, the maximum possible answer is the minimum of:

   the maximum window (with at most 1 S and possible to swap) → which can be up to the window length.

   and the total_g.

Because you can't have a longer consecutive G's than the total number of G's.

For example, in the first example:

input is 10, with 7 G's. The maximum window with 1 S is length 8 (including 1 S). But since T is 7, which is less than 8. So the candidate is min(8, 7) =7, which is the correct answer.

So the algorithm is:

Compute all possible windows with at most one S. For each such window:

   if S_count == 0:

       candidate = window length.

   else:

       if T >= window length → candidate is window length.

       else → candidate is T.

But wait, in the case where T is less than window length, but there are G's outside (which can be swapped with the S in the window), then the candidate would be window length. But since T is less than window length, that's impossible. Because the total number of G's is T. So the maximum consecutive G's possible is T.

So, in that case, the candidate for the window is min(window length, T) if there are G's outside. But if there are no G's outside (T < L → T - (L-1) < 1 → T - L +1 <1 → T < L → L > T), then there are no G's outside, so can't swap. So the candidate is (L-1).

But how to handle this?

Alternatively, the maximum possible answer after considering all windows is:

max_candidate = max (for each window:

   if S_count ==0 → window length

   else:

       if (T >= L) → L

       else → (L-1) if (T >= (L-1) +1 - (L-1) is the current G's in the window plus 1 swapped, but no, not sure.)

Wait, perhaps this is getting too complicated.

Let me think of the approach:

The sliding window can track the maximum window with at most one S. Then, the maximum possible candidate after considering swaps is:

If the window has 0 S → window length.

Else (window has 1 S):

   if the total_g >= (number of G's in the window) + 1 → can swap that S with a G outside. Then the window can have (window length) G's. But the total number of G's is T. So the actual maximum for this case is min(window length, T).

So the candidate for this window is min(window length, T) if there's a G outside (i.e., T >= (number of G's in window) +1 → which is (window length -1) +1 → window length). So T >= window length.

Wait, number of G's in the window is (window length -1) (since there's 1 S). The number of G's outside is T - (window length -1). We need that to be >=1. So T - (window length -1) >=1 → T >= window length.

So in that case, candidate is min(window length, T). But since T >= window length, min is window length.

But if T < window length, then even if we can swap, the maximum possible is T. So candidate for this window is T.

Wait, no. Because if T is less than window length, then the window's possible G's after swap is (window length -1 +1) = window length. But since T is the total number of G's, which is less than window length, that's impossible.

For example, if the window is of length 5, with 1 S (so 4 G's). Suppose T is 4. Then, total G's is 4. So the number of G's outside the window is 4-4 =0. So we can't swap. So the candidate for this window is 4 (the original number of G's in the window).

But if T is 5, and the window length is 6 (with 5 G's and 1 S), then T is 5. So the number of G's outside is 5 -5 =0. So again, no swap possible. So the candidate is 5 (original G's in the window).

So for a window with 1 S, the candidate is:

if there exists a G outside (T >= window length → T >= (window_length -1) +1 → T >= window_length), then the candidate is window_length (but can't exceed T). But since T >= window_length in this case, the candidate is window_length.

But if T < window_length, then no G's outside → candidate is (window_length -1).

But wait, (window_length -1) is the number of G's in the window. So the candidate is (window_length -1).

So for a window with 1 S, the candidate is:

min( (window_length if T >= window_length else (window_length -1)), T )

Because even if we can swap, the maximum possible can't exceed T.

Wait, that's probably the correct way to model it.

So the candidate for a window with 1 S is:

if T >= window_length → candidate is window_length.

else → candidate is min( (window_length -1), T )

But wait, if T is less than (window_length -1), then the candidate can't be more than T. For example, if window_length is 5 (with 4 G's), and T is 3. Then the window's candidate is 4 (window_length -1), but T is 3, so the actual maximum is 3.

So the candidate for such a window would be min( (window_length -1), T ), but T is 3. So candidate is 3.

So the correct candidate for a window with 1 S is:

min( (window_length if T >= window_length else (window_length -1)), T )

But since T is fixed, perhaps the candidate is min( (window_length if T >= window_length else (window_length -1)), T )

But this seems complicated. Alternatively:

For a window with 1 S:

possible_after_swap = window_length if (there's a G outside) else (window_length -1)

But possible_after_swap can't exceed T.

So possible_after_swap = min( possible_after_swap, T )

So combining:

possible_after_swap = min( (window_length if (T >= window_length) else (window_length -1)), T )

But how to compute that.

Alternatively:

if T >= window_length:

   possible_after_swap = window_length

else:

   possible_after_swap = min( window_length -1, T )

But wait, if T is less than window_length, but window_length -1 is larger than T, then possible_after_swap is T.

But if T is larger than window_length -1, then possible_after_swap is window_length -1.

So for a window with 1 S:

possible_after_swap = min( window_length, T ) if T >= window_length else min( window_length -1, T )

But perhaps a simpler way is:

possible_after_swap = min( (window_length if T >= window_length else window_length -1), T )

But maybe not. Let's think of cases.

Case 1: T >= window_length.

possible_after_swap = window_length. But since T >= window_length, min( window_length, T ) = window_length.

So candidate is window_length.

Case 2: T < window_length.

possible_after_swap = window_length -1. But if window_length -1 > T, then min( window_length-1, T ) = T.

So possible_after_swap = min( window_length-1, T )

But how to compute that.

Alternatively, possible_after_swap = min( (window_length if (T >= window_length) else window_length -1 ), T )

But this may not capture all cases.

Alternatively, possible_after_swap is the minimum between T and (the maximum possible after swapping for the window).

So for the window:

max_possible_swap = (window_length if (T >= window_length) else (window_length -1))

possible_after_swap = min( max_possible_swap, T )

But since T is the total number of G's, this would ensure that the possible_after_swap is not more than T.

So, for example:

window_length =5, T=4.

max_possible_swap =5 (if T >=5). But T is 4, so max_possible_swap is 5-1=4. Then possible_after_swap is min(4,4) =4.

Another example: window_length=5, T=3.

max_possible_swap is 4 (window_length-1=4), but T is 3. So possible_after_swap=3.

So the formula would be:

possible_after_swap = min( (window_length if (T >= window_length) else (window_length-1)), T )

Which is the same as possible_after_swap = min( (window_length if (T >= window_length) else (window_length-1)), T )

So the candidate for a window with 1 S is possible_after_swap.

So putting it all together:

The maximum possible answer is the maximum among all windows of:

   if window has 0 S → window length

   else → possible_after_swap (as computed above)

Then, the overall maximum is the maximum of all these candidates.

So the steps to implement are:

1. Precompute the positions of all S's.

2. Use a sliding window approach to find the maximum window with at most one S.

3. For each such window, compute the candidate as per the above.

4. Take the maximum of all candidates.

Now, the sliding window approach for at most one S is manageable.

But how to implement this efficiently?

Sliding window (two pointers) approach:

Initialize left=0. For each right, track the number of S's in the window. If the count exceeds 1, move left to reduce the count.

At each step, record the maximum window length where the count is <=1.

Once we have the maximum window length (max_len), but we need to process each window to compute the candidate.

But how to track the maximum candidate across all possible windows.

But perhaps, during the sliding window process, whenever a window with <=1 S is found, we can compute the candidate for that window and track the maximum.

But since the sliding window approach finds the maximum window length, perhaps the maximum candidate comes from the maximum window length.

But perhaps not. For example, a shorter window with a higher candidate (due to T constraints) could yield a higher candidate.

But that's unlikely, but possible.

So during the sliding window process, for each window that has S_count <=1, compute the candidate and track the maximum.

But since the sliding window process is O(n), this would be manageable.

So here's the plan:

Initialize left=0, max_candidate=0, s_count=0, total_g is precomputed.

For each right in 0 to n-1:

   if s[right] == 'S': s_count +=1

   while s_count >1:

       if s[left] == 'S': s_count -=1

       left +=1

   current_window_length = right - left +1

   # compute candidate for this window

   current_s_count = s_count

   if current_s_count ==0:

       candidate = current_window_length

   else:

       # current_s_count is 1

       if total_g >= current_window_length:

           possible_swap = current_window_length

       else:

           possible_swap = current_window_length -1

       candidate = min( possible_swap, total_g )

   max_candidate = max( max_candidate, candidate )

At the end, the answer is max_candidate.

But wait, what about the case where the total_g is less than current_window_length, but there's a G outside?

For example, let's say the window is of length 5 (with 1 S), total_g is 4. Then, the possible_swap would be 5-1=4, and min(4,4)=4.

Which is correct.

But in this case, the window is of length 5 (1 S), so the G's in the window are 4. The total_g is 4. So the number of G's outside is 0. So swapping is not possible. So the candidate is 4 (the current G's in the window). Which is correct.

Another example:

window_length is 6, 1 S. total_g is 5.

So possible_swap is 6-1=5. min(5,5) →5. Which is correct.

Because the total_g is 5. So the maximum possible consecutive G's is 5. So swapping the S with a G outside (but in this case, the number of G's outside is 5 -5 (window G's) =0. So no G's outside. So we can't swap. So the candidate is 5 (the original G's in the window plus 0 from swap → 5. Which is 5 (window G's is 5, which is equal to total_g). So the candidate is correct.

So the algorithm correctly computes the candidate.

So this sliding window approach, combined with the candidate computation, should work.

Now, let's test against the examples.

First example:

Input: 10

GGGSGGGSGG

The string is G G G S G G G S G G.

The total_g is 8? Let's count.

Let's see:

Indices (0-based):

0: G

1: G

2: G

3: S

4: G

5: G

6: G

7: S

8: G

9: G

Total G's: 0,1,2,4,5,6,8,9 → 8 G's. Wait, but the sample input says the output is 7. Wait, the sample input's output is 7. Which suggests that the total_g is 7? Let me check.

Wait the input is "GGGSGGGSGG".

Breaking it down:

Characters: 1 2 3 4 5 6 7 8 9 10 (assuming 1-based, but in code it's 0-based).

But the string is:

GGGSGGGSGG → positions 0-9.

Characters:

0: G

1: G

2: G

3: S

4: G

5: G

6: G

7: S

8: G

9: G

So total G's are 8 (positions 0,1,2,4,5,6,8,9). So total_g is 8.

But the sample output is 7.

Wait, according to the sample explanation, after swapping indices 4 (the first S) and 10 (assuming 1-based), which would be position 3 (0-based) and 9 (0-based) in the string. So swapping the S at index 3 with G at index9. The string becomes GGG GGGGSG S → no, perhaps I need to recheck.

Wait the sample input is:

10

GGGSGGGSGG → the original string has two S's. So after swapping the two S's with G's? But wait, the S's are at positions 3 and 7. To swap them with a G outside, but all other positions are G. So swapping one of the S's (e.g., position3) with a G from the end (position9) would turn the string into GGGG GGG SGS (or similar). Wait, the sample explanation says that the resulting string is GGGGGGGSGS. Which has a run of 7 G's.

So total_g is 8 (since the swap moves S's to other positions but the total remains 8). But the maximum consecutive is 7. Which is less than total_g. Because the total_g is 8, but the consecutive after swap is 7. So why?

Ah, because in this case, the maximum possible window with one S and possible swap would be 8 (but total_g is 8, so min(8,8) =8. But the sample output is 7. So this suggests that the algorithm as described might not handle this case correctly.

Wait, why? Let's think.

In the sample input, the maximum window with one S is perhaps 8 (including the S). So the algorithm would calculate:

current_window_length is 8. s_count is 1. total_g is 8.

So possible_swap is min(8,8) =8. So the candidate is 8.

But the actual maximum after swap is 7.

Hmm, this suggests that the algorithm would give a candidate of 8, but the correct answer is7.

But that's a problem. So what's wrong here?

Wait, perhaps the algorithm is not correctly considering that swapping the S in the window with a G outside the window may not result in all G's in the window. Because the G that is swapped into the window is from outside, so the window can have all G's. But in the sample input, after swapping the S (position3) with a G (position9), the window (positions0-7) would be GGG GGGGS (the swapped S is at position9, so in the window positions0-7, there is an S at position7. So the maximum run is positions0-6 (7 G's).

Wait, I'm getting confused. Let's think again.

The original string is G G G S G G G S G G.

The S's are at positions3 and7.

After swapping position3 (S) and position9 (G), the string becomes:

positions0-9: G G G G G G G S S G.

Wait, swapping position3 and9: the S at3 is replaced by G (from9), and the G at9 is replaced by S. So the new string is G G G G (position3 is now G), then G G G S (positions4-7), then S G (positions8-9).

So the maximum consecutive G's is 7 (positions0-6: 7 G's).

So why does the algorithm's candidate for a window of length8 with one S (e.g., positions0-7) have a candidate of8? Because total_g is8, which is >=8. So the algorithm would think that swapping is possible, leading to a candidate of8.

But in reality, swapping that S with a G outside the window (position9's G) would give that window (positions0-7) 7 G's and the S at position7 is swapped to position9. So the window becomes positions0-7 as GGG GGGG G (position7 is now G). So the entire window becomes 7 G's (positions0-7 have 7 G's? Wait, original positions0-7 in the window are GGG S GGG S. So after swapping the S at position3 with the G at position9, the window (positions0-7) becomes GGG G (from position3) GGG S (position7 remains S). So the window is GGGGGGS S. So the maximum consecutive G's in the window is6 (positions0-5: 6 G's), and position6 is G, position7 is S. So the maximum consecutive is6.

But according to the algorithm's calculation, the candidate for this window would be8 (window_length=8, total_g=8). But the actual maximum after swapping is6. So the algorithm's approach is incorrect.

So this indicates that the approach is wrong.

So why is this happening?

Because the algorithm assumes that swapping the S in the window with a G outside the window will turn the entire window into G's. But in reality, the swap affects two positions: the S inside the window and a G outside the window. So the S becomes a G, and the G becomes an S.

So after swapping, the window's S is replaced by a G, but another position (the one outside the window) is replaced by an S.

But the algorithm's logic is that the window after swap would have all G's. Which is incorrect.

So the algorithm's approach is flawed.

Oh right! Because the swap is between an S in the window and a G outside the window. So the S in the window becomes a G, increasing the G count in the window by1. But the G outside becomes an S, which might be in another window.

So the window after the swap would have (original G's in the window) +1 (because the S is replaced by G). But since the total_g is fixed, the G outside the window is reduced by1. So the total_g remains the same.

But the window's G's are increased by1 (from S to G), but the G outside is lost (replaced by S).

But when we swap, the window's S is replaced by G. So in the window, the number of G's becomes (original G's) +1. But since the original window has s_count=1 (so original G's is window_length -1), the new G's in the window is window_length -1 +1 = window_length. But this is possible only if the G swapped in is from outside.

But the G swapped in is from outside, so the window's S is replaced by G, but the G outside is now S.

So in the window, after swap, all positions are G's. But the total_g remains the same.

So the window's length is window_length, and since the total_g is T, the maximum consecutive G's after swap would be window_length, but only if T >= window_length (since you can't have more G's than T).

But in the sample input, the window_length is8, T is8. So the candidate is8.

But in reality, after the swap, the maximum consecutive G's is7.

So why is this discrepancy?

Because the window in question (of length8) includes one S. When we swap that S with a G outside, the window's S becomes G, but the G outside becomes S. However, that S outside might be part of another group. But the window in question is the entire window of length8. After swapping, the window becomes all G's (since the S inside is replaced by G). So the window of length8 is now all G's. So the maximum consecutive G's would be8. But in the sample input, after swapping, the maximum is7.

So where is the error in the reasoning?

Ah, the example in the sample input's note says that after swapping indices4 and10 (assuming 1-based), the string becomes GGGGGGGSGS.

Wait, the original input is 10 characters. Swapping indices4 and10 (1-based) would be positions3 and9 (0-based). So original S at3 is swapped with G at9.

The resulting string is:

positions0: G

1: G

2: G

3: G (from position9)

4: G (original position4 was G)

5: G

6: G

7: S (original S at7)

8: S (original position8 was G, but after swap, position9 is S. So position8 is G?)

Wait, I think I'm getting confused with the indices here.

Original string is:

0: G

1: G

2: G

3: S

4: G

5: G

6: G

7: S

8: G

9: G

So swapping positions3 (S) and9 (G):

After swap:

position3 becomes G.

position9 becomes S.

So the new string is:

0: G

1: G

2: G

3: G

4: G

5: G

6: G

7: S

8: G

9: S

So the consecutive G's are from 0-6 (7 G's), then S at7, then G at8, S at9.

So the maximum consecutive G's is7.

But according to the algorithm's calculation, the window of positions0-7 (length8) has one S (at position7). The total_g is8 (original was8, but after swap, the total_g is8 (since we swapped an S and a G, so total remains same).

Wait, in the original string, the total_g is 8.

After swapping, the total_g is still8 (swap S and G: one G is added, one is removed. So total remains same).

So the algorithm's candidate for the window of length8 (positions0-7) with S at7 is:

current_s_count=1.

total_g=8.

window_length=8.

possible_swap =8.

candidate=8.

But after swapping, the window (positions0-7) has the S at7 replaced by G (from position9). But position9 is outside the window. So after swapping, the window becomes all G's. So the consecutive G's in the window would be8. But in the sample input's explanation, the maximum is7.

So why is that?

Ah, because after the swap, the window (positions0-7) has S at7? No. Because the S at7 was not swapped. The S that was swapped is at position3 (originally), and the S at7 remains.

Wait, the sample explanation says that after swapping indices4 (S) and10 (G), which are positions3 and9 (0-based), the S at3 is replaced by G, and the G at9 is replaced by S. So the S at7 remains.

So the window of positions0-7 (after swap) would be:

0-3: G's.

4-6: G's.

position7: S.

So the window of 8 characters (positions0-7) has an S at7, so the consecutive G's in this window would be 7 (positions0-6) and then S at7. So the maximum consecutive in the window is7.

So the algorithm's candidate for this window is8, but the actual maximum after swap is7.

So the algorithm is overestimating the candidate.

This indicates that the approach is incorrect.

What's the problem here?

The algorithm assumes that swapping the S in the window (position3) with a G outside (position9) will turn the entire window into G's. But in reality, the window is positions0-7. The S in the window is position3. After swapping with position9 (outside), the S at3 becomes G, and the G at9 becomes S. So the window (0-7) now has positions0-3 as G's, positions4-7 as G's (except position7, which is S). So the window now has an S at7 (which was not swapped). So the window's S count is now 1 (at position7), but the original S was at3.

Wait, this is getting confusing. Let me re-examine.

Original window: positions0-7. S's are at3 and7. s_count is 2. But this is invalid, because the sliding window approach only allows windows with at most one S. So how did this window get considered?

Ah, no. Because in the sliding window approach, the window will have s_count<=1.

So the window can't include both S's. So the algorithm's window with s_count=1 would not include both S's.

So for the sample input, the sliding window approach will find a window that includes one S.

For example, the window from0-3 (GGGS) has s_count=1, length4. The window from4-7 (GGGS) has s_count=1, length4. But the maximum window with one S could be, for example, the first three G's plus the S and next three G's, making a window of length7 (GGGSGGG), which has one S. Or perhaps a longer window that skips one of the S's.

Wait, how to find the maximum window with at most one S.

Let's see the sample input:

Indices: 0 1 2 3 4 5 6 7 8 9

Chars: G G G S G G G S G G

The S's are at3 and7.

The sliding window approach:

At each step, track the number of S's.

For example, when the right pointer is at3 (the first S), the s_count becomes1. The window is0-3, length4.

As the right pointer moves to4 (G), s_count remains1. The window expands to0-4 (length5).

Then to5 (G): window0-5 (length6).

To6 (G): window0-6 (length7).

To7 (S): s_count becomes2. So we need to move the left pointer until s_count<=1.

Left pointer moves to1 (G), then to2 (G), to3 (S): s_count becomes1. So the window is4-7 (length4).

So the maximum window with one S is7 (positions0-6, which includes the S at3) or something else?

Wait, let's walk through the sliding window steps step by step.

Initialize left=0, s_count=0, max_candidate=0.

right=0: char is G. s_count=0. current_window_length=1. s_count is0. candidate is1. max_candidate=1.

right=1: G. s_count=0. window_length=2. candidate=2. max_candidate=2.

right=2: G. s_count=0. window_length=3. candidate=3. max_candidate=3.

right=3: S. s_count=1. window_length=4. candidate: since s_count=1, possible_swap is min(4,8) if T=8 >=4. So possible_swap=4. candidate=4. max_candidate=4.

right=4: G. s_count=1. window_length=5. candidate: min(5,8)=5. max_candidate=5.

right=5: G. candidate=6. max=6.

right=6: G. candidate=7. max=7.

right=7: S. s_count=2. So enter the while loop to move left.

left=0: s[0] is G → s_count remains2. left becomes1.

left=1: G → left becomes2.

left=2: G → left becomes3.

s[3] is S → s_count decreases to1. left becomes4. Now, the window is4-7 (chars SGGGS → wait, no. After moving left to4, the window is4-7 (chars GGG S). So s_count=1.

current_window_length=4. candidate: s_count=1. possible_swap=4, min(4,8)=4. max_candidate remains7.

right=8: char G. window is4-8 (length5). s_count=1. candidate:5. max_candidate=7.

right=9: char G. window4-9 (length6). s_count=1. candidate:6. max_candidate=7.

So the maximum candidate is7, which matches the sample output.

So the algorithm works for this case.

Wait, in this case, the maximum candidate comes from the window0-6 (length7) with s_count=1.

But total_g is8.

So possible_swap for this window is min(7,8) →7. Which is correct.

So the algorithm produces the correct candidate of7 for this window, which is the correct answer.

So why did the earlier analysis with the window of length8 suggest a problem? Because such a window would have s_count=2, which is invalid and thus not considered by the sliding window approach.

So the sliding window approach correctly captures the maximum possible window with at most one S, and the candidate computation for each window correctly captures the possible_swap based on the total_g.

So the algorithm works.

Another example:

Sample input 2: all G's. total_g=4. So the answer is4.

Sample input3: all S's. answer is0.

So the algorithm works.

Thus, the steps are:

- Compute total_g.

- If total_g is0 or n, return the appropriate value.

- Else, use a sliding window approach to find all windows with at most one S.

- For each such window, compute the candidate as follows:

   if window has 0 S → candidate is window length.

   else (1 S):

       if total_g >= window length → candidate is window length.

       else → candidate is min( window length-1, total_g )

- The answer is the maximum of all candidates.

So the Python implementation would be:

Read the input.

Compute total_g.

Handle edge cases.

Then sliding window.

Now, let's code this.

The code would look like this:

n = int(input())
s = input().strip()

total_g = s.count('G')

if total_g == 0:
    print(0)
elif total_g == n:
    print(n)
else:
    left = 0
    s_count = 0
    max_candidate = 0
    for right in range(n):
        if s[right] == 'S':
            s_count +=1
        # Shrink the window until s_count <=1
        while s_count >1:
            if s[left] == 'S':
                s_count -=1
            left +=1
        current_len = right - left +1
        current_s = s_count
        if current_s ==0:
            candidate = current_len
        else:
            if total_g >= current_len:
                possible = current_len
            else:
                possible = current_len -1
            candidate = min(possible, total_g)
        if candidate > max_candidate:
            max_candidate = candidate
    print(max_candidate)

Testing this code with the first sample:

Sample input:

10

GGGSGGGSGG

The code would compute total_g=8.

Then the sliding window would process each character.

When right is6 (index6), the window is0-6 (length7). s_count=1.

Candidate is7 (since total_g >=7 →8 >=7. possible is7, min(7,8)=7).

At this point, max_candidate is7.

When right is7 (S), s_count becomes2. So the left is moved until s_count is1. The window becomes4-7 (length4). candidate is4 (possible=4, min(4,8)=4). max_candidate remains7.

Other steps don't produce a higher candidate.

So the code outputs7.

Another test case:

Sample input2:

4

GGGG

total_g=4. So code outputs4.

Sample input3:

3

SSS

total_g=0. code outputs0.

Thus, the code works for the examples.

Now, considering edge cases.

Test case: n=2, s= 'GS' → total_g=1. The maximum possible is1 (swap gives 'SG' → max is1, or 'GS' → max is1. Or, if we swap G and S, it's 'SG' → max 1. But according to the code:

The sliding window would process:

For right=0 (G): window len1, s_count 0 → candidate1.

For right=1 (S): s_count1. current_len=2. candidate is min(2, 1) →1. So max_candidate is1.

Thus, code outputs1.

But swapping the two gives 'SG', which has max 1. So correct.

Another test case:

n=5, s= 'GSSG G' → 'GSSGG' → total_g=3.

The sliding window:

Looking for the maximum window with at most one S.

Possible windows:

GSSGG → the S's are at1 and2.

The maximum window with one S could be positions0-3: GSSG (s_count=2 → no. Wait.

Let me think.

The code will track left=0, and for each right:

When right is0 (G), s_count=0. window len1. candidate1.

right=1 (S): s_count=1. window len2. candidate is2 if total_g >=2. total_g=3>=2 → candidate is2. max=2.

right=2 (S): s_count=2. Shrink window.

left moves to1 (S): s_count becomes1. left=1+1=2. window is2-2 (S). s_count=1. current_len=1. candidate is0 (current_s=1, total_g=3 >=1 → possible=1. min(1,3) =1. So candidate1.

max remains2.

right=3 (G): window2-3. chars SG. s_count=1. len2. candidate is2. max remains2.

right=4 (G): window2-4. len3. s_count=1. candidate is3. total_g=3 >=3 → possible=3. min(3,3)=3. max becomes3.

Thus, code outputs3.

Which is correct. Because the string is G S S G G.

The best swap is to swap one of the S's (position1 or2) with a G.

For example, swap position1 (S) with position3 (G). The string becomes G G S S G → the maximum consecutive G's is2 (positions0-1). But wait, that's not right. Wait, after swapping, the string becomes:

positions0: G

1: G (from position3)

2: S

3: S

4: G.

So the longest consecutive G's is 2 (positions0-1). But the code gives3.

Ah, but perhaps the window after swap is different.

Wait, the code's logic assumes that after swapping the S in the window with a G outside, the entire window becomes G's.

But in this test case, the window is positions2-4 (len3), s_count=1 (position2 is S).

 total_g=3 >=3 → candidate3.

But after swapping position2 (S) with position0 (G), the window positions2-4 becomes G's, but position0 becomes S.

So the new string is S S G G G. The maximum consecutive G's is3 (positions2-4), which is correct.

So the code's candidate of3 is correct.

Thus, the code works correctly.
</think>

```python
n = int(input())
s = input().strip()

total_g = s.count('G')

if total_g == 0:
    print(0)
elif total_g == n:
    print(n)
else:
    max_candidate = 0
    left = 0
    s_count = 0
    for right in range(n):
        if s[right] == 'S':
            s_count += 1
        # Ensure the window has at most one 'S'
        while s_count > 1:
            if s[left] == 'S':
                s_count -= 1
            left += 1
        current_len = right - left + 1
        if s_count == 0:
            candidate = current_len
        else:
            if total_g >= current_len:
                candidate = current_len
            else:
                candidate = current_len - 1
            candidate = min(candidate, total_g)
        if candidate > max_candidate:
            max_candidate = candidate
    print(max_candidate)
```