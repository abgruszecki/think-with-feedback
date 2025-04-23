<think>
Okay, I need to solve this problem where I have to find the minimal number of operations to make at least two elements in the array equal by applying some number of AND operations with x. Let's think about how to approach this.

First, let's understand the operation. Each element can either be in its original form (if we don't apply the operation) or transformed to ai & x (if we do apply the operation). The key is that for each element, there are two possible values: the original and the modified one (unless the original is already the same as the modified, in which case there's only one possibility). 

The goal is to have at least two elements (possibly after modification) that are equal. So for each element, we can consider both possibilities and check if any two of them (from any elements) can be equal. The minimal number of operations would be the sum of the steps required for those two elements to reach that value, which could be 0, 1, or 2 steps (since each element can be either kept or modified once).

Wait, but each operation can be applied once per element. Because applying the operation more than once doesn't change the value. For example, if you do ai & x once, doing it again will not change the value. So for each element, after at most one operation, the value can't change further. So each element can be either in its original state (0 operations) or modified once (1 operation). So for each element, there are two possible states.

So the problem reduces to checking all pairs of elements (i, j) where i < j, and for each pair, check if there's a common value between the possible values of ai and aj. Then, among all such possible pairs, find the one that requires the minimal sum of operations (sum of steps for i and j).

For example, if ai's original value is already equal to aj's original value, then the sum is 0. If ai's original equals aj's modified, then the sum is 0 (for ai) + 1 (for aj). Or if ai's modified equals aj's modified, sum is 1 + 1. We need to find the minimal such sum across all possible pairs.

But considering that n can be up to 1e5, checking all pairs (which is O(n^2)) is impossible. So we need a smarter way.

So, how can we find the minimal steps without checking all pairs?

Let's think of the possible values for each element. For each element, there are two possible values: original and modified (if they are different). For each possible value, we need to track how many elements can reach that value with 0, 1, or combined steps. Then, for each value that appears in any of these possibilities, find if there are at least two elements that can reach it, and compute the minimal sum of steps required for two of them.

So, the plan is:

1. For each element, generate all possible values (original and modified, but if they are the same, just one entry). For each of these values, track the minimal steps required to get there for that element. For example, for an element where the original and modified are different, the possible values are original (cost 0) and modified (cost 1). If they are the same, it's one value (cost 0 or 1, but using 0 is better).

Wait, but for each element, the modified value is ai & x. So for any element, the modified value is ai & x. The original value is ai. So for each element, possible options are:

- Keep it as ai (cost 0)
- Change to ai & x (cost 1), but only if ai != (ai & x). Otherwise, changing it is a no-op, so it's equivalent to cost 0 (but applying the operation doesn't change anything, so maybe you can ignore this case).

So for each element, collect the possible (value, cost) pairs. Then, for all possible pairs of elements, check if any of their possible values overlap, and if so, compute the sum of the minimal costs for each.

But again, with n up to 1e5, this approach might be too slow. So we need a way to track for each possible value, the minimal costs from different elements, and then find the minimal sum of two elements' costs for the same value.

So here's the idea:

We can create a dictionary (hash map) where the key is the possible value, and the value is a list of all possible costs (0 or 1) that different elements can take to reach this value.

Once we have this dictionary, for each key, if the list of costs has at least two elements (i.e., there are at least two elements that can reach this value with some cost), then the minimal sum of two costs for this key is the sum of the two smallest costs in the list.

For example, if a value has costs [0,1,0], then the minimal sum is 0 + 0 = 0. If the list is [1,1], then sum is 2. So for each value, we need to track the two smallest costs, then compute their sum.

Then, among all possible values, the minimal such sum is the answer. If there are no such values, return -1.

So the steps are:

1. For each element in the array:

   a. Compute original = ai, modified = ai & x.

   b. For each of these values, add to the dictionary the possible costs. But for the original value, the cost is 0. For the modified value, the cost is 1 (but only if modified != original; otherwise, modified is same as original, and cost can be 0 or 1 but using 0 is better, so perhaps we can ignore the cost 1 in that case).

Wait, but if original equals modified, then applying the operation doesn't change the value. So in that case, the element can have its value as original (cost 0) or same as original (cost 1, but same value). So for such elements, the possible options for the value are the same, but with two possible costs (0 or 1). However, when considering pairs, we can use the same value from the same element with different costs. Wait, but that's not possible. Because a single element can't contribute two entries for the same value. Wait, no: each element can contribute to the possible entries for its possible values. For example, if original and modified are the same, then the element can contribute two entries for the same value: one with cost 0 and one with cost 1. But that's redundant because using cost 0 is better. But when considering pairs, perhaps using two elements where one has cost 0 and the other cost 1 (from the same value) would sum to 1. But that's possible.

But for the purpose of the minimal sum, for a given value, if an element can contribute both 0 and 1 (because original and modified are same), then when building the list of possible costs for that value, we can include both. But in reality, the element can only be in one state (either 0 or 1), but since the sum requires two different elements, maybe including the 0 and 1 from the same element's possibilities is not allowed. Wait, no. Because the same element can't be used twice. So each element's possible values are two options (if they are different) and the cost for each. But when building the list for the value in the dictionary, each element can contribute up to two entries (if the original and modified are different, and both contribute to the same value). Wait, no. For example, original is 5, modified is 3. Then for the value 5, the cost is 0; for 3, cost is 1. So for those two different values. But if original and modified are same, then for the same value, the element contributes two possible costs (0 and 1). However, when two elements can reach the same value, but one uses cost 0 and the other cost 1, their sum is 1. So we need to track all possible costs per value.

But how to handle elements where original and modified are the same. For such elements, their possible contributions to a value (same as original) are two possibilities: cost 0 and cost 1. But using cost 0 is better, but for pairs, if there's another element that can reach the same value with cost 1, the sum would be 0+1=1.

Wait, but if the element's original and modified are same, then even if you apply the operation, the value doesn't change. So in this case, the element can have its value as that value with 0 operations (original) or 1 operation (modified, which is same). So for the purposes of the problem, this element can be considered as having two possible states (but same value) but different operation counts. However, when trying to pair with another element, the minimal sum would consider the minimal possible sum. For example, if an element A has value v with cost 0 and 1 (because modified is same as original), and another element B has value v with cost 0, then the minimal sum is 0+0 (from A and B, both using cost 0) which is 0. But if there's another element C that can reach v with cost 1, then the sum for A (cost 0) and C (cost 1) is 1.

So in the case where an element can contribute multiple costs for the same value, we need to include all possible costs in the list for that value. Then, when looking for the minimal sum of two different elements, we can select any two elements' costs (possibly from the same element's options? No, because the same element can't be used twice.)

Wait, no. Each element can be used once in the pair. So for example, if element A can contribute to value v with cost 0 and 1 (because modified is same as original), then when paired with another element B that contributes to v with cost 0, the possible pairs are:

A (cost 0) + B (cost 0): sum 0.

A (cost 0) + B (cost 1): sum 1.

A (cost 1) + B (cost 0): sum 1.

A (cost 1) + B (cost 1): sum 2.

So the minimal sum is 0.

But in this scenario, element B can be the same as A? Wait, no. Because the problem requires two distinct elements. So for the same element, if it can contribute two costs for the same value, can we use both in a pair? For example, if the array has only one element, but the problem requires two elements. So no. So each element can contribute at most two entries to the list, but when building pairs, we can't use the same element twice. So the list for each value is a collection of the possible costs from different elements.

Wait, but the problem allows us to apply operations to any elements. So for a single element, applying the operation or not will result in the same value (if original and modified are same). But in that case, the element's possible contributions to the value are two entries (0 and 1), but when we select two elements (which could be the same element?), but the problem requires two distinct indices. So the pair must consist of two different elements. So in the list for a value, each element can contribute multiple entries (like two costs for the same value), but when considering pairs, the two costs must come from different elements.

Ah, this complicates things. Because when we have a value v in the dictionary, each entry in the list of costs for v comes from a different element. So for example, if an element A contributes two costs (0 and 1) to v, then in the list, there are two entries (0 and 1) from the same element. But when selecting two entries from the list for v, the minimal sum is the sum of two different elements. But if the list has both 0 and 1 from the same element, then those can't be used together. So this approach of tracking all possible costs in a list for each value would not work, because some entries may be from the same element, which can't form a pair.

So the problem is that when an element contributes multiple costs to a value v, those are from the same element and cannot be paired. So the way we track the possible costs per value must be adjusted.

This suggests that for each element, for each possible value it can contribute, we need to track the minimal cost for that element to reach the value. Then, when considering the value's list, each element contributes only the minimal cost for that value. Or, perhaps track all possible costs but ensure that each element's contributions are considered properly.

Hmm. Let's think again. For each element, the possible values are original and modified (if different). For each such value, the cost is 0 or 1. However, for the same element, if both original and modified are the same, then the element can contribute to that value with cost 0 (since applying the operation is optional, but not required). So for such elements, the minimal cost for that value is 0, but the element could also be considered as having cost 1. But why would that help? Because for example, if two elements can reach the same value, but one with cost 0 and the other with cost 1, then the sum is 1, which is better than some other pairs.

But the key is that each element can contribute to a value in multiple ways, but when considering pairs, the two elements must be distinct.

So the approach should be:

For each value v in the possible values (after considering original and modified for all elements), collect all the minimal costs from each element. That is, for each element, if it can reach v with cost 0, then include 0 in the list. If it can't reach v with 0, but can reach it with 1 (and original and modified are different), then include 1. But if the element can reach v with both 0 and 1 (like when modified equals original), then only include 0 (since it's the minimal cost, and the 1 is redundant because applying the operation doesn't change the value, so it's better to take 0).

Wait, but that's not entirely correct. Because if an element can reach v via 0 (original) or 1 (modified, which is same as original), then using the original (cost 0) is better. So for each element, for each possible value it can contribute, we can track the minimal cost. So for example, if the element's original is v (cost 0), then even if modified is also v (cost 1), the minimal cost is 0. So for that element, when considering v, we can only track 0 as the possible cost.

But that would miss the possibility of pairing this element with another element that can reach v via cost 1. For example, element A can reach v with cost 0 (original), element B can reach v with cost 1 (modified). Their sum is 0 + 1 = 1. But if we only track the minimal cost (0 for A), then for the list of v, it's [0, 1], and the sum is 0+1=1. So including all possible costs (but considering that for some elements, both 0 and 1 can be possible for the same value) is necessary.

But how to model this correctly.

Alternative approach:

For each element, generate all possible (value, cost) pairs. But for elements where original and modified are the same, generate only (value, 0). Because applying the operation here is redundant. So for such elements, there's no point in considering cost 1, since the value doesn't change, and it's better to take cost 0.

Wait, but in the problem statement, the operation can be applied any number of times. But since applying it again doesn't change the value, once you have applied it once, applying again is irrelevant. So for such elements, the possible states are either not applying (cost 0) or applying once (cost 1, but same value). So the element can contribute to the value's list with both 0 and 1. But when considering pairs, the same element can't be used twice. So for example, if an element has (v,0) and (v,1), but that's for the same element. So when building the list for v, we can't use both entries from the same element. So the minimal approach is for each element, for each value that it can contribute, track all possible costs (0 and/or 1), but when building the list, we need to include all possible costs from all elements, but when considering pairs, the two costs must come from different elements.

But how to track this efficiently.

This is getting complicated. Let's think of the example where original and modified are the same. For example, x is 3, ai is 1. Then ai & x is 1. So the element can choose to apply the operation (cost 1, but value is same) or not (cost 0). So for the value 1, the element contributes two possible costs: 0 and 1. But when building the list for value 1, these are two separate entries, but from the same element. So when choosing two elements, you can't take both 0 and 1 from the same element. So the list for value 1 may have multiple entries from the same element. But how to avoid pairing them.

This complicates the approach because, for the list of costs in a value, some entries are from the same element. So when looking for the minimal sum, we need to ensure that the two costs come from different elements.

So perhaps the correct way is to track, for each value, all possible elements that can reach it, along with their minimal cost.

Wait, but the minimal cost per element for that value. For example, for each element, if it can reach the value in 0 steps (original), then that's the minimal. Otherwise, it can reach it in 1 step (modified). So for each element and each possible value (original and modified), the minimal cost is the minimal steps to reach that value.

But then, for each value, the list of costs for each element is the minimal cost to reach that value. For example:

If an element can reach value v via 0 steps (original) and 1 step (modified), then the minimal cost is 0, so for value v, it's 0. But if the element can't reach v via 0 steps, but can via 1 step, then the minimal cost is 1.

Wait, but the element can only choose to either apply or not apply the operation once. So for each element, the possible values are original (cost 0) and modified (cost 1), unless original and modified are the same, in which case modified is same as original (so cost 0 or 1, but value is same). But the element can contribute to the value's list in two ways (if original and modified are same) but the minimal cost is 0, so in that case, perhaps for each element, for each possible value it can reach, we can track the minimal cost to reach that value.

Wait, no. Because the element's modified value is ai & x. So for example, if ai is 5 and x is 3, then modified is 1. So the element can contribute to 5 (cost 0) and 1 (cost 1). For another element, say 1 and x is 3, modified is 1. So that element can contribute to 1 via cost 0 or 1 (but since modified is same as original, the minimal cost is 0). So in this case, for value 1, the costs from the two elements are 0 (from the second element) and 1 (from the first element's modified step).

So for the value 1, the list of costs would be [0,1], which can be summed as 0+1=1 for a pair. The minimal sum for this value is 0 (if there are two elements that can reach it with 0 cost) or 1 (if one can reach with 0 and another with 1).

So the correct way is to track for each value, all the possible costs from different elements. Then, for each value, we need to find the two smallest costs (but from different elements) and compute their sum.

But how do we track this for each value.

Alternative plan:

- For each element, compute its original value (a) and modified value (b = a & x).
- For each element, add to a dictionary for a (original) with cost 0, and for b (modified) with cost 1 (if a != b).
- If a == b (i.e., modified is same as original), then only add the cost 0. Because applying the operation doesn't change the value, so the element can contribute to the same value with cost 0 or 1. But adding both would allow for a situation where two elements can pair with costs 0 and 1. But since the same element can't be paired with itself, we need to avoid that.

Wait, but if we add both 0 and 1 for a value when a == b, then for that element, the value's list will have two entries (0 and 1). But when considering pairs, if there's another element that contributes a 0 to the same value, then the sum is 0+0. But if the same element's 0 and 1 are in the list, but you can't pair them. So adding both 0 and 1 for elements where a == b is problematic.

Alternatively, for elements where a == b, the only cost that's needed is 0. Because applying the operation doesn't change the value. So whether you apply it or not, the value is same, but the cost can be 0 or 1. But the minimal sum for pairs would be better to take 0 if possible. But perhaps adding both 0 and 1 to the list for that value allows for better combinations.

Wait, but here's the problem: if an element can contribute to a value with cost 0 and 1 (because a == b), and another element can also contribute to that value with cost 0, then the minimal sum is 0+0=0. But if the same element is the only one that can contribute to that value, then having 0 and 1 in the list is not helpful. So perhaps adding both 0 and 1 for elements where a == b is not necessary, and we can instead add only 0, since that's the minimal cost for that element to reach the value.

But in the example where x is 3 and ai is 1 (so a == b), the element can contribute to value 1 with cost 0 (original) or 1 (modified). But since applying the operation doesn't change the value, using cost 0 is better. However, if another element can reach 1 via cost 1, then combining the 0 (from the first element) and 1 (from the second) gives a sum of 1, which might be better than other options.

But in this case, the first element's cost 0 is already better. So adding the cost 1 for the same element is not useful. Because when considering pairs, you can't use the same element twice. So in the list for value 1, we can have:

element 1: cost 0 and 1 (but same element)
element 2: cost 1 (modified)

But the sum for element 1's 0 and element 2's 1 is 1, which is possible.

But if we only track the minimal cost (0) for element 1, then the list for value 1 would have [0,1]. The sum is 0+1=1. So it's the same result.

But if element 1's possible costs are 0 and 1 (same element), and element 3's possible costs are 0 and 1 (same element), then the list for value 1 is [0,1,0,1]. The minimal sum would be 0+0=0 (using two different elements, each with cost 0). But in reality, those elements can reach the value 1 with cost 0 (original), so the sum is 0. So if we track all possible costs (including 0 and 1 for elements where a == b), then the list will have multiple 0s. So when finding the two smallest entries in the list, we can take the two smallest 0s, which sum to 0.

But if we only track the minimal cost (0) for each element, then in the case where a == b, the list for value v is filled with 0s from all such elements, and the sum is 0 for any pair. So that's correct.

So perhaps the correct approach is:

For each element, add to the dictionary the original value with cost 0. Also, add the modified value (if different from original) with cost 1. So for elements where original and modified are different, they contribute two entries (original cost 0, modified cost 1). For elements where original and modified are same, they contribute one entry (original cost 0).

This way, each element's possible contributions are considered, but for elements where a == b, they can only contribute with cost 0. Because applying the operation doesn't change the value, but the cost can be 0 or 1. However, since the modified value is same as original, adding cost 1 for that value would not change the sum if there's another element contributing a 1. But since the element's modified is same as original, it's better to track the minimal cost (0) for that value.

Wait, but in this case, the element can choose to either apply the operation or not. But since applying the operation doesn't change the value, the element can be in the same value with cost 0 or 1. So in this scenario, the element contributes two possible entries (value, cost 0) and (value, cost 1). However, when building the list for that value, this would add both 0 and 1. But the same element can't be used twice in a pair.

So, for example, if an element contributes (v, 0) and (v, 1) to the list for v, then when looking for pairs, we can't take 0 and 1 from the same element, but we can take 0 from two different elements.

Thus, including both 0 and 1 for elements where a == b may lead to incorrect pairs (using the same element's 0 and 1). But since the elements are distinct, but their costs are added as separate entries, the list may have multiple entries from the same element, which could lead to considering pairs that are invalid (same element).

So the approach of adding both 0 and 1 for elements where a == b is wrong.

Therefore, the correct approach is:

For each element, add the original value (a) with cost 0. Then, compute the modified value (b = a & x). If b is different from a, add the modified value with cost 1. So, elements where a == b do not contribute the cost 1 entry. 

This way, each element can contribute up to two entries (if a and b are different) or one entry (if a and b are same). But when a and b are same, adding the cost 0 is sufficient. Because applying the operation (cost 1) doesn't change the value. So for such elements, whether you apply the operation or not, the value is same. So the minimal cost is 0. But if another element can reach the same value with cost 1, then pairing the two elements' 0 and 1 gives sum 1.

Thus, the correct way to build the dictionary is:

For each element ai:

- original = ai, cost 0 → add to the dict.

- modified = ai & x, cost 1 → add to the dict only if modified != original.

This ensures that for each element, the possible entries are:

- original (cost 0)

- modified (cost 1) if it's different from original.

So, the elements where original == modified will contribute only the original (cost 0). The elements where original != modified contribute both.

Now, the dictionary for each value will have a list of costs from different elements, with each element contributing at most two entries (but only for different values).

Once this dictionary is built, for each value in the dictionary, check if the list of costs has at least two entries. If so, then find the minimal sum of two costs from different elements.

The minimal sum for each value is the sum of the two smallest costs in the list. Because we need two different elements, so the two costs must be from different elements.

So, for example, if the list is [0, 0], sum is 0. If the list is [0, 1, 1], sum is 0 + 1 = 1. If the list is [0, 0, 1], sum is 0 + 0 = 0.

So the minimal sum for the value is the sum of the two smallest elements in the list.

But wait, the two smallest elements may come from the same element. For example, if an element contributes two entries (0 and 1) for a value. Then the list for the value has [0,1, 0], and the two smallest are 0 and 0 (from two elements), sum is 0. But if the two 0s are from the same element (which is possible?), then that's invalid.

Wait, but in our approach, for elements where original == modified, the element contributes only one entry (cost 0). So the same element can't contribute multiple entries to the same value.

Wait, for example, an element where original is 5 and modified is 3. So the element contributes 5 (cost 0) and 3 (cost 1). These are different values, so added to different entries in the dictionary.

Another example: original is 3, modified is 3. So the element contributes 3 (cost 0). So the list for value 3 will have this 0.

So, the entries in the dictionary for a value are from different elements. Because each element can contribute to the same value at most once (if a == modified, then once, else once for original and once for modified if they are different, but different values).

Wait, no. For example, element A has original 5, modified 3. So it contributes 5 (cost 0) and 3 (cost 1). Element B has original 3, modified 3 (so contributes 3 cost 0). So the value 3's list is [0 (from B), 1 (from A)]. So the sum would be 0 (B's 0) + 1 (A's 1) → 1.

So in this case, the entries are from different elements.

So in this approach, the list of costs for each value in the dictionary consists of costs from different elements, each contributing at most one entry (even if the element contributes two entries to different values). So when considering pairs, the two costs in the list are from different elements.

Therefore, to find the minimal sum, for each value's list of costs, we can sort the list and take the first two entries (smallest two), sum them. Then, track the minimal sum across all values.

So, the steps are:

1. For each element ai in the array:

   a. Compute original = ai → add (original, 0) to the dictionary.

   b. Compute modified = ai & x → if modified != original, add (modified, 1) to the dictionary.

2. For each value in the dictionary, collect all the costs in a list.

3. For each value's list, if the length is >= 2:

   a. Sort the list.

   b. Compute the sum of the first two elements (smallest two).

   c. Keep track of the minimal such sum across all values.

4. If any such minimal sum exists, return it. Otherwise, return -1.

This approach should work because each entry in the list for a value comes from a different element (since each element can contribute at most one entry to a given value). For example, an element can contribute to two different values (original and modified) but not to the same value twice. So when the list has multiple entries for a value, they come from different elements.

This way, when we select the two smallest entries in the list, they are from two different elements, and their sum is the minimal possible for that value.

Now, let's test this approach against the examples.

First example:

Input:

4 3

1 2 3 7

For each element:

ai | original | modified (ai & 3) | modified != original?

1 → modified is 1 &3=1 → same as original. So add (1, 0).

2 → modified is 2&3=2 → same as original. Add (2, 0).

3 → modified is 3 → same as original. Add (3,0).

7 → modified is 7&3=3 → different. So add (7,0) and (3,1).

So the dictionary:

1 → [0]

2 → [0]

3 → [0 (from ai=3), 1 (from ai=7)]

7 → [0]

So for value 3, the list is [0,1]. The minimal sum is 0+1=1. Which matches the first example's output.

Second example:

Input:

2 228

1 1

For each element:

ai=1. modified is 1 &228 = 1 (since 228 in binary is 11100100, so 1 in binary is 00000001. AND gives 0, which is 0? Wait, wait 228 is 228 in decimal. 1 &228 = 0. So modified is 0.

Wait, original is 1, modified is 1&228. Let's compute 228 in binary: 228 is 128+64+32 + 4 → 11100100. So 1 in binary is 00000001. AND is 00000000 → 0. So modified is 0, which is different from original (1). So for each element:

ai=1: add (1,0) and (0,1).

So the dictionary:

1 → [0,0] (from the two elements)

0 → [1,1]

So for value 1, the list is [0,0]. Sum is 0+0=0, which is the correct output.

Third example:

3 7

1 2 3

x=7 (binary 0111). For each element:

ai=1: modified is 1 &7=1 → same. Add (1,0).

ai=2: 2&7=2 → same. Add (2,0).

ai=3: 3&7=3 → same. Add (3,0).

So the dictionary for each value is:

1 → [0], 2 → [0], 3 → [0].

Each list has length 1. So no possible pairs. Output is -1.

Which matches the third example.

Another test case: 

Sample where two elements can reach the same value via cost 0 and 1. For example:

n=2, x=3.

array [5, 2]

ai=5: original is 5 (cost 0), modified is 5&3=1 (cost 1).

ai=2: original is 2 (cost 0), modified is 2&3=2 (same as original, so only add 0).

So for value 1 (from ai=5's modified), the list is [1].

For value 2 (from ai=2's original and modified, but modified is same as original, so list is [0].

For value 5, list is [0].

So the possible pairs are:

Looking for any value with at least two entries.

But no value has that. So output is -1.

But wait, what if the array is [5,1], x=3.

ai=5: original 5 (0), modified 1 (1).

ai=1: original 1 (0), modified 1&3=1 (same as original, so only add 0).

So the value 1's list is [0 (from ai=1), 1 (from ai=5)]. So sum is 0+1=1. So output is 1.

Yes. So this approach seems to work.

Now, the challenge is to implement this efficiently.

Given n up to 1e5, and each element generating up to two entries in the dictionary, the total number of entries is up to 2e5. So this is manageable.

For each value in the dictionary, we need to collect all the costs. Then, for each such list, if length >=2, we sort it and take the first two elements.

But sorting each list can be expensive if the lists are large. For example, if all elements contribute to the same value with 0 and 1. Wait, but how can that happen? For example, x is 0, then ai&x is 0 for all elements. So for each element, original is ai (cost 0) and modified is 0 (cost 1). So for x=0, each element contributes (ai, 0) and (0,1). So the value 0's list will have all the 1's from each element (since modified is 0, and different from original ai). Also, the original ai's are added as well. So for the value 0, the list will have 1's for each element (since for each element, modified is 0, which is different from original ai).

But if x is 0, then the modified is 0. So for each element, modified is 0. So each element contributes (ai, 0) and (0,1). Then, the list for 0 will have a 1 from each element. For example, n=1e5 elements, list for 0 will have 1e5 entries of 1. So the sum is 1+1=2. So the minimal sum would be 2.

But if there are two elements with original ai == 0, then their original is 0, cost 0. So the list for 0 will have two 0's and many 1's. The minimal sum is 0+0=0.

So, the code must handle this.

But for the general case, how to efficiently find the minimal sum for each list.

An alternative is to track for each value, the count of 0's and 1's. Because each element contributes at most one entry to a value's list (either 0 or 1, but not both for the same value).

Wait, no. Because for a given element, it can contribute to two different values (original and modified). But for a particular value, the element can contribute at most once (either 0 or 1). For example:

element ai=5, x=3. Original is 5 (cost 0), modified is 1 (cost 1). So for value 5, the element contributes 0. For value 1, contributes 1. For another element ai=1, x=3: original is 1 (cost 0), modified is 1 (cost 1 is not added since modified == original). So for value 1, contributes 0. So the list for value 1 has 1 (from ai=5) and 0 (from ai=1). Sum is 0+1=1.

So for each value, the list is built from different elements, each contributing 0 or 1.

So, for each value, the list consists of 0's and 1's from different elements.

So, the minimal sum for a value is the minimal sum of two distinct elements' costs.

The minimal sum would be the sum of the two smallest entries in the list.

So, the minimal possible sum for a value is:

- If there are at least two 0's → sum is 0.

- If one 0 and at least one 1 → sum 1.

- If no 0's and at least two 1's → sum 2.

Thus, for each value's list, the minimal sum is determined by the count of 0's and 1's.

So instead of storing the entire list, we can track the count of 0's and 1's for each value.

This is more efficient. Because for each value, we can track how many 0's and 1's are present. Then, for each value, we can compute the minimal sum as follows:

If the count of 0's >= 2 → sum is 0.

Else if count of 0's >= 1 and count of 1's >=1 → sum is 0 +1=1.

Else if count of 1's >=2 → sum is 2.

Otherwise, not possible.

So, for each value, we can track the number of 0's and 1's. This reduces the space and processing time.

This approach is better because we don't need to sort the list. Instead, we can compute the minimal sum directly based on the counts.

So, the steps are:

1. For each element, compute original and modified.

2. For each value, track the count of 0's and 1's.

3. For each value, compute the minimal possible sum based on the counts.

4. Find the overall minimal sum across all values.

So, the code can proceed as follows:

- Initialize a dictionary, say from collections.defaultdict, where each key is the value (after original or modified), and the value is a tuple (count0, count1).

- For each element ai:

   a. Add original value: increment count0 for that value.

   b. Compute modified. If modified != original, add modified value: increment count1 for that value.

- Then, for each value in the dictionary:

   a. count0 = number of elements that can reach this value with cost 0.

   b. count1 = number of elements that can reach this value with cost 1.

   c. Now, compute possible minimal sum for this value.

      i. If count0 >= 2 → sum is 0.

      ii. Else if count0 >=1 and count1 >=1 → sum is 1.

      iii. Else if count1 >=2 → sum is 2.

      iv. Else → no possible sum for this value.

   d. Keep track of the minimal sum across all values.

- Finally, return the minimal sum found, or -1.

This approach is O(n) time and space, which is efficient for n up to 1e5.

Let's test this approach against the examples.

First example:

After processing all elements:

value 3 has count0=1 (from ai=3), count1=1 (from ai=7).

So count0=1, count1=1 → sum is 1.

Which matches the example.

Second example:

After processing:

value 1 has count0=2, count1=0 (since modified is 0, but for each ai=1, modified is 0 which is added to 0's count1. Wait, wait. Let me re-calculate.

Wait, in the second example, input is ai=1, x=228.

Original ai=1 (add to 1's count0: count0 becomes 2).

modified = 1&228 = 0. So for each element, modified is 0, which is different from original. So add to 0's count1.

So in the dictionary:

value 1 → count0=2, count1=0.

value 0 → count0=0, count1=2.

So for value 1, count0=2 → sum 0.

For value 0, count1=2 → sum 2.

But since the original elements are 1 and 1, which have value 1 in original (count0=2). So the minimal sum is 0. Which matches the example.

Third example: for each element, the count0 for their respective values is 1. No value has count0 >=2. So sum is not possible. Output is -1.

Another test case where two elements contribute 0 and 1 to a value:

For example, value 3 has count0=1 (from ai=3) and count1=1 (from ai=7). So sum is 1.

Thus, this approach works.

So the code can be written as:

- Read n and x.

- Read the array.

- Initialize a defaultdict with default value (0, 0) for count0 and count1.

- For each ai in the array:

   original = ai

   modified = ai & x

   # add original to count0

   counts[original] = (counts[original][0] + 1, counts[original][1])

   # add modified to count1 if modified != original

   if modified != original:

       counts[modified] = (counts[modified][0], counts[modified][1] + 1)

- Iterate over all values in counts:

   for each value, get count0 and count1.

   compute possible minimal sum:

   min_sum = infinity

   if count0 >= 2:

       min_sum = 0

   elif count0 >=1 and count1 >=1:

       min_sum = 1

   elif count1 >=2:

       min_sum = 2

   else:

       continue

   keep track of the global minimum.

- If global minimum is found, output it. Else, -1.

Wait, but what about combinations where there are multiple ways to reach the sum? For example, if a value has count0=3, then the sum is 0. But if another value has count0=2 and count1=5, sum is 0. So the minimal sum is 0.

This is correct.

Another case: a value has count0=1 and count1=3. Then sum is 1 (0+1). But another value has count0=0, count1=3 → sum is 2. So the minimal sum is 0 or 1, whichever is present.

So this approach captures the correct minimal sum.

Thus, the code can be implemented in this way.

Now, let's code this.

We need to read the input, process each ai, and update the counts. Then, for each value in counts, compute the possible minimal sum.

We'll need to import defaultdict from collections.

Now, edge cases to consider:

- All elements are already the same. For example, input array is [5,5,5], x=anything. The original values are 5, so count0 for 5 is 3. Sum is 0.

- Some elements can be modified to same value. For example, array [5,6], x=3. 5&3=1, 6&3=2. So no common values. Output -1.

So code seems correct.

Now, coding:

In Python:

We can use a dictionary where each key is the possible value, and the value is a tuple (count0, count1).

We can use collections.defaultdict with a default of (0, 0). Or, use a normal dict and check if the key exists.

But in Python, for defaultdict, initializing with a default of a tuple (0,0) is a bit tricky. Because defaultdict expects a factory function that returns the default value.

So we can use:

from collections import defaultdict

counts = defaultdict(lambda: (0, 0))

Then, for each ai:

original = ai

modified = ai & x

count0, count1 = counts[original]

counts[original] = (count0 + 1, count1)

if modified != original:

    current_count0, current_count1 = counts[modified]

    counts[modified] = (current_count0, current_count1 + 1)

Wait, no. Because for modified, we are adding to count1 (the second element of the tuple). For example, when we process modified, it's being added as a cost of 1. So the count1 for that value is incremented by 1.

Yes.

Once the counts are built, iterate through each value in counts, and compute the minimal possible sum for that value.

Then, track the overall minimal sum.

The code steps:

Read n and x.

Read the array as a list of integers.

Initialize counts as a defaultdict with default (0,0).

For each ai in the array:

   original = ai

   modified = ai & x

   # Add original to count0

   counts[original] = (counts[original][0] + 1, counts[original][1])

   # Add modified to count1 if different

   if modified != original:

       counts[modified] = (counts[modified][0], counts[modified][1] + 1)

Now, loop through each value in counts:

min_ops = infinity

for key in counts:

   count0, count1 = counts[key]

   # compute possible sum for this value

   current_min = infinity

   if count0 >=2:

       current_min = 0

   elif count0 >=1 and count1 >=1:

       current_min = 1

   elif count1 >=2:

       current_min = 2

   else:

       continue

   if current_min < min_ops:

       min_ops = current_min

if min_ops is still infinity, output -1 else output min_ops.

But we need to initialize min_ops to something larger than possible. Since the maximum possible minimal sum is 2 (two 1's), but initializing to infinity (like float('inf')) and then if after all values, min_ops is still infinity, output -1.

So code:

Testing against sample input 1.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, x = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))

    counts = defaultdict(lambda: (0, 0))

    for ai in a:
        original = ai
        modified = ai & x

        # Update original's count0
        cnt0, cnt1 = counts[original]
        counts[original] = (cnt0 + 1, cnt1)

        # Update modified's count1 if different
        if modified != original:
            cnt0_m, cnt1_m = counts[modified]
            counts[modified] = (cnt0_m, cnt1_m + 1)

    min_ops = float('inf')

    for key in counts:
        cnt0, cnt1 = counts[key]
        current_min = float('inf')
        if cnt0 >= 2:
            current_min = 0
        elif cnt0 >= 1 and cnt1 >= 1:
            current_min = 1
        elif cnt1 >= 2:
            current_min = 2

        if current_min < min_ops:
            min_ops = current_min

    if min_ops != float('inf'):
        print(min_ops, file=output_stream)
    else:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 228
1 1
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

Testing against sample input 2.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, x = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))

    counts = defaultdict(lambda: (0, 0))

    for ai in a:
        original = ai
        modified = ai & x

        # Update original's count0
        cnt0, cnt1 = counts[original]
        counts[original] = (cnt0 + 1, cnt1)

        # Update modified's count1 if different
        if modified != original:
            cnt0_m, cnt1_m = counts[modified]
            counts[modified] = (cnt0_m, cnt1_m + 1)

    min_ops = float('inf')

    for key in counts:
        cnt0, cnt1 = counts[key]
        current_min = float('inf')
        if cnt0 >= 2:
            current_min = 0
        elif cnt0 >= 1 and cnt1 >= 1:
            current_min = 1
        elif cnt1 >= 2:
            current_min = 2

        if current_min < min_ops:
            min_ops = current_min

    if min_ops != float('inf'):
        print(min_ops, file=output_stream)
    else:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 7
1 2 3
""",
            "output": \
"""\
-1
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

Third example:

Input:

3 7

1 2 3

Processing:

Each ai's modified is same as original (since x=7, binary 111. So 1&7=1, 2&7=2, 3&7=3).

So counts:

After ai=1: counts[1] → (1,0).

modified is same → no count1.

ai=2: counts[2] (1,0).

ai=3: counts[3] (1,0).

No other entries.

Each key has count0=1, count1=0. So no possible sum. Output is -1.

Thus, the code works.

Another test case where two elements contribute 0 and 1 to a value.

Example:

n=2, x=3.

array [5,1].

Processing:

ai=5:

original=5 → counts[5] (1,0).

modified=5&3=1 → different. So counts[1] (0,1).

ai=1:

original=1 → counts[1] (1,0+1) → (1,1)?

Wait, no. Let's see.

For ai=5:

original is 5 → counts[5] becomes (1,0).

modified is 1 → counts[1] becomes (0,1).

For ai=1:

original is 1 → counts[1] was (0,1) → becomes (1,1).

modified is 1&3=1 → same as original. So no update.

So for key=1, counts are (1,1). So cnt0=1, cnt1=1 → sum is 1.

Thus, output is 1.

Thus, the code works.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    counts = defaultdict(lambda: (0, 0))  # (count0, count1)
    
    for ai in a:
        original = ai
        modified = original & x
        
        # Update count0 for original
        cnt0, cnt1 = counts[original]
        counts[original] = (cnt0 + 1, cnt1)
        
        # Update count1 for modified if different from original
        if modified != original:
            cnt0_m, cnt1_m = counts[modified]
            counts[modified] = (cnt0_m, cnt1_m + 1)
    
    min_ops = float('inf')
    for key in counts:
        cnt0, cnt1 = counts[key]
        current_min = float('inf')
        if cnt0 >= 2:
            current_min = 0
        elif cnt0 >= 1 and cnt1 >= 1:
            current_min = 1
        elif cnt1 >= 2:
            current_min = 2
        if current_min < min_ops:
            min_ops = current_min
    
    print(-1 if min_ops == float('inf') else min_ops)

if __name__ == "__main__":
    main()
```
