<think>
Okay, let's tackle this problem. So the task is to make sure all categories have different numbers of publications, and we need to find the minimal total time to add publications to achieve that. The batch already gives some a_i's, and we can't remove any, only add. Each addition for category i takes t_i time per unit. So the goal is to adjust the a_i's such that all are distinct, with the sum of (added numbers) * t_i being minimized.

Hmm. Let's think about the approach. The key here is to arrange the a_i's in such a way that after adding some values, all are unique. But how?

Let's start by sorting the a array. Because when sorted, we can process each element and ensure that each next element is at least one more than the previous. That way, all are unique. But since we can add to the a_i's, maybe this sorted order approach is the way to go.

Wait, but the problem allows adding to any of the categories, not just the ones that are in a certain order. So perhaps we need to sort the original a_i's and then for each position i in the sorted array, compute the minimal required a_i' such that a_i' is at least previous a_i' +1. Then the total additions are the sum of (required a_i' - a_i) * t_i for each category.

But wait, but how do we choose which category to assign which a_i' to? Because the t_i's might vary. For example, categories with lower t_i should be given as much as possible the minimal required increases, while those with higher t_i can be adjusted more. So the order in which we process the categories (sorted by some criteria) will affect the total time.

Ah, right. So the optimal approach would be to sort the categories in such a way that for categories that need to be increased, the ones with the smallest t_i (so cheapest to add) are increased first, while those with higher t_i are increased as little as possible.

But how to model this.

Let me think. Let's first sort the categories based on their a_i values. If there are duplicates in a_i, then those need to be adjusted. But even in the sorted list, we need to ensure that each next element is strictly larger than the previous. But since we can only add to a_i, the minimal way is to have a non-decreasing sequence where each element is at least the previous one +1. Wait, no. For example, if after sorting, the a_i's are [3, 7, 7, 8, 9], then the second 7 must be increased to at least 8. But then the next element is 8, which would then have to be increased to at least 9, etc. But this approach would require adjusting all subsequent elements.

But in that case, the total cost would depend on the order in which we process the elements. But how to model this when considering the t_i's.

Alternatively, perhaps the optimal way is to first sort the a_i's along with their t_i's, and then process them in a way that allows us to greedily minimize the cost. For example, when two elements have the same a_i, we can decide which one to leave as is (or increase) based on their t_i. But when there are multiple elements, this becomes more complex.

Wait, here's an idea. We can sort the categories in non-decreasing order of a_i. Then, for each category in this order, we need to make sure that its a_i is at least one more than the previous category's a_i. But this is only if the previous category's a_i (after adjustment) is greater than or equal to the current a_i. Wait, no. Let's think:

After sorting the a_i's in non-decreasing order, the adjusted a_i's must form a strictly increasing sequence. So for each i from 1 to n-1, adjusted a_i must be >= adjusted a_{i-1} + 1. However, the original a_i's may not satisfy this. So for each category in the sorted list, the minimal adjusted a_i is the maximum between the original a_i and previous adjusted a_i + 1. But this approach would ensure that each adjusted a_i is as small as possible given the previous ones, which would minimize the total additions. However, this approach does not take into account the t_i's. So if two categories have the same a_i, but one has a lower t_i, perhaps it's better to increase the one with lower t_i first, allowing the other to not have to increase as much.

Wait, but how? Because when sorted by a_i, if two elements are the same, their order in the sorted list can be swapped. So perhaps we need to sort the categories not only by their a_i, but also by t_i when a_i's are equal. Because if two categories have the same a_i, then the one with the lower t_i should come first. Because that way, when we adjust the next category (the one with higher t_i), it's possible that we can increase it by less. Let me see.

For example, suppose we have two categories with a_i = 5, t_i = 1 and 10. If we sort them with the t_i=1 first, then:

The first becomes 5. The next must be at least 6. So we have to add 1 to the second, which costs 10*1=10. But if we reverse the order (t_i=10 first), then the first would be 5, the second must be 6, which again requires adding 1 to the second. So the cost is the same. Hmm, that's interesting. So perhaps the order between elements with the same a_i doesn't matter in this case. But what if there are more elements?

Wait, no. Because if three elements have a_i=5, and t_i 1, 2, 3. Let's sort them by a_i and t_i (ascending).

So sorted order would be (5,1), (5,2), (5,3).

Processing them:

First: adjusted is 5.

Second: must be at least 6. So add 1. Cost 2*1=2.

Third: must be at least 7. So add 2. Cost 3*2=6. Total cost is 8.

If instead, we sorted them in a different order, say (5,3), (5,2), (5,1):

Processing:

First: 5.

Second: must be 6. So add 1. Cost 2*1=2.

Third: must be 7. So add 2. Cost 1*2=2. Total cost 2+2=4. Which is better.

Oh wait, that's a better total. So the order in which same a_i elements are processed can affect the total cost. Because when you process the elements in higher t_i first, the lower t_i elements can have more flexibility in their required additions.

Wait, this example shows that the order matters. So the correct approach would be to process the elements with the same a_i in the order of descending t_i. Because for the same a_i's, we want the ones with higher t_i to be processed first, so that when we process the lower t_i ones, they can be adjusted more cheaply.

Wait, how? Let's see the example again.

Original three elements: a=5, t=1, 2,3.

If we process them in order of t descending (3,2,1):

First element: adjusted is 5.

Second element must be at least 6. So add 1. Cost 2*1=2.

Third must be at least 7. Add 2. Cost 1*2=2. Total 4.

If processed in t ascending (1,2,3):

First: 5.

Second must be 6. Add 1. Cost 2*1=2.

Third must be 7. Add 2. Cost 3*2=6. Total 8.

So the order indeed matters. So when a_i's are the same, we should sort the categories in descending order of t_i. Because when you process a category with higher t_i first, the required adjustment for that category is minimal (since it's the first in the group), and the lower t_i categories, which can be adjusted more cheaply, can take the higher required values. Wait, but in this example, by processing higher t_i first, the lower t_i have to add more, but since their t is lower, it's cheaper. So this way, the higher t_i elements are adjusted as little as possible, and the lower ones can take the larger adjustments but at a lower cost.

Yes. So the strategy is: sort the elements first by their a_i in ascending order. For elements with the same a_i, sort them in descending order of t_i. Then, for each element in this sorted list, compute the required a_i' as the maximum between the current a_i and the previous a_i' + 1. The sum of (a_i' - a_i) * t_i for all elements is the answer.

So the steps are:

1. Sort the categories in such a way that a_i is non-decreasing. For categories with the same a_i, sort them in descending order of t_i. So the higher t_i comes first in the same a_i group.

2. Iterate through the sorted list, keeping track of the previous a_i' (the adjusted value). For the current category, the minimal adjusted a_i' is max(a_i, prev + 1). The difference (a_i' - a_i) multiplied by t_i is added to the total time. Update prev to the current a_i'.

This approach should give the minimal total time.

Now, the key is to prove that this approach is correct. Let's think of it this way: by sorting same a_i elements in descending t_i order, we ensure that higher t elements are adjusted first, which allows the lower t elements to be adjusted more (but at a lower cost). For example, when two elements have the same a_i and different t_i, processing the higher t_i first would mean that if their a_i's are same, the higher t one is adjusted to the minimal possible (so a_i' is a_i, or forced to be higher), and the lower t one can then be adjusted to a higher value if needed, but since their t is lower, the cost is less. 

Wait, let's take two elements with a=5, t1=10, t2=1. If sorted in descending order of t, then first is t1=10, then t2=1. 

Processing first: a_i' is 5. 

Processing second: must be at least 5+1=6. So add 1 to the second. Cost is 1 * 1 = 1.

If we had sorted them in the opposite order (t2 first, then t1):

Processing first: a_i' is 5.

Processing second: must be at least 6. So add 1 to t1 (10 * 1 =10). Total cost is 10. Which is worse.

So the correct approach is indeed to process same a_i elements in descending t_i order.

So the plan is:

- Sort the elements by a_i ascending, and then t_i descending.

Then, process each element in this order, ensuring that each element's adjusted a_i is at least previous +1. The minimal required adjustment is then computed, multiplied by t_i, and added to the total.

This should give the minimal possible total time.

Now, how to implement this efficiently.

The constraints are n up to 2e5, so O(n log n) time is acceptable.

So steps for code:

1. Read n.

2. Read a_i list.

3. Read t_i list.

4. Create a list of pairs (a_i, t_i).

5. Sort this list by a_i ascending, then by t_i descending.

6. Initialize previous = -infinity. Or, for the first element, the adjusted is max(a_i, previous +1). Wait, previous starts as the adjusted a_i' of the previous element.

7. Iterate through the sorted list:

   For each (a, t) in sorted list:

       required = max(a, previous + 1)

       add (required - a) * t to total.

       previous = required

8. Output the total.

Let's test this against the sample input.

Sample 1:

Input:

5

3 7 9 7 8

5 2 5 7 5

So the a_i list is [3,7,9,7,8]. t_i [5,2,5,7,5].

We need to pair each a_i and t_i, then sort by a_i ascending, then t_i descending.

The original a_i's are 3,7,9,7,8.

So sorted a_i's would be 3,7,7,8,9.

For the two 7's, their t_i's are 2 and 7 (since original a_i's are 7 and 7, their t_i's are 2 and 7. Wait, original list:

The original a array is [3,7,9,7,8]. So the 7's are at positions 1 and 3. The t for position 1 is 2, position 3 is7. So when sorted by a_i ascending, the 7s are grouped. So the two elements are (7,2) and (7,7). Wait, no. Wait, the sorted a_i is 3,7,7,8,9. The t_i's for these a_i's are: For the first 7, the original index 1 has t=2. The second 7 is index 3 with t=7. So when sorted, these two entries are (7,2) and (7,7), but when sorted by a_i ascending and t_i descending, the same a_i entries are ordered by t_i descending. So for a=7, the t's are 7 and 2. So sorted in descending order of t, the order becomes (7,7), (7,2). 

Wait, no. Wait, the elements with a_i=7 are (7,2) and (7,7). When sorted in descending order of t_i, 7 is higher than 2. So the order of these two would be (7,7) first, then (7,2).

So the sorted list would be:

a=3, t=5

a=7, t=7

a=7, t=2

a=8, t=5

a=9, t=5

Processing these:

prev starts as -infinity.

First element (3,5):

required = max(3, prev +1) → max(3, -inf +1) →3. So no addition. prev becomes 3. Total is 0.

Second element (7,7):

required is max(7, 3+1=4) →7. So addition is 0. prev is 7. Total remains 0.

Third element (7,2):

required is max(7,7+1=8) →8. So addition is 1 *2=2. Total is 2. prev is 8.

Fourth element (8,5):

required is max(8,8+1=9). So 9. Addition is 1*5=5. Total becomes 7. prev is9.

Fifth element (9,5):

required is max(9,9+1=10). 10. Addition is 1*5=5. Total becomes 12. 

But the sample output is 6. Wait, that's a problem. So what's wrong here.

Wait the sample output is 6, but according to this calculation, the code gives 2+5+5=12. But that can't be right. So why is there a discrepancy?

Wait, let's look at the first sample again. The sample input is:

5

3 7 9 7 8

5 2 5 7 5

So the a_i's are [3,7,9,7,8], t_i's [5,2,5,7,5].

The correct answer is 6. The note says that adding three publications to the second type (which is the second a_i=7 with t=2). So how does that fit into the sorted approach?

Wait, perhaps the initial sorting is not correct.

Wait the a_i's are 3,7,9,7,8. When sorted in non-decreasing order, it's 3,7,7,8,9. The t_i's for these a_i's are 5,2,7,5,5. Wait, let's see:

Original indexes:

0: a=3, t=5

1: a=7, t=2

2: a=9, t=5

3: a=7, t=7

4: a=8, t=5

So when sorted by a_i and then t_i descending, the elements would be:

(3,5), (7,7), (7,2), (8,5), (9,5).

Processing:

prev = -inf.

First element: 3, required is 3. prev=3. cost 0.

Second:7. required is max(7, 3+1=4) →7. prev=7. cost 0.

Third:7. required is max(7,7+1=8). So 8. add 1. cost 1*2=2. prev=8.

Fourth:8. required is max(8,8+1=9) →9. add 1. cost 5*1=5. prev=9.

Fifth:9. required is 10. add 1. cost 5*1=5. total is 2+5+5=12. But sample output is 6. So this approach isn't correct. What's wrong here?

Wait the sample's correct answer comes from adding 3 publications to category 2 (original index 1: a=7, t=2). So the adjusted a_i's would be:

3 →3, 7→7+3=10 (since original a=7, t=2, adding 3 gives 10. Then others: 9,7,8.

Wait, but how does that make all unique?

Wait after adding 3 to the second category (a=7 becomes 10), the a_i's would be 3,10,9,7,8. Then sorted, they are 3,7,8,9,10. All distinct. So no need to adjust others.

But according to the sample note, that's possible with cost 3*2=6.

So in that case, the code's approach is not finding the correct solution. So why?

Because the approach of processing elements in sorted order and ensuring each is at least previous +1 would require that the third element (which is 7 in the sorted list) be adjusted to 8, but in the sample solution, the second element (7) is adjusted to 10, allowing others to remain as is. So the approach of processing elements in sorted order and adjusting each to be at least previous +1 might not be the optimal.

So the problem is that the code's approach may not account for the possibility that increasing a lower a_i's by more can allow higher a_i's to stay as they are, leading to a lower total cost.

Hmm. So the initial approach is not correct.

So this suggests that the approach needs to be revised. The problem is that the code's approach forces a non-decreasing sequence of adjusted a_i's. But the sample shows that a higher a_i can be adjusted to a higher value, allowing lower a_i's to be as low as possible.

Wait, but in the sample, the a_i's after adjustment are 3,7→10,9,7→7,8. But sorted, they are 3,7,8,9,10. All distinct. But in the code's approach, after processing, the adjusted a_i's are 3,7,8,9,10. So why is the code's approach giving a higher cost than necessary?

Wait, the code's approach may not consider that other a_i's can be arranged in a way that allows some of them to not be adjusted. But according to the code's approach, after sorting, the elements are processed in a way that ensures each is at least previous +1. But in the sample, the third a_i (original 7, t=2) is adjusted to 8 (adding 1). Then the fourth a_i (8) is adjusted to 9 (adding 1). The fifth (9) adjusted to 10 (adding 1). So total additions: 1*2 +1*5 +1*5 =2+5+5=12. But the sample's optimal solution is to add 3 to the second a_i (7, t=2) to get 10, and leave others as they are, which requires adding 3*2=6. So why is the code's approach not capturing that?

Because the code's approach processes the elements in a certain order (sorted a_i ascending and t_i descending for same a_i). But perhaps the code's approach is not optimal in some cases.

The problem here is that the code's approach requires that the adjusted a_i's form a non-decreasing sequence, but the sample shows that the adjusted a_i's can have a higher a_i in an earlier position (but only if the original a_i is higher). So perhaps the code's approach is too restrictive.

Wait, but the code's approach sorts the a_i's in non-decreasing order, and processes them in such a way that each subsequent adjusted a_i is at least previous+1, forming a strictly increasing sequence. So the code's approach gives a sequence where each a_i' is larger than the previous, but the actual adjusted a_i's can be in any order as long as they are all unique. Wait, no. The code's approach is to sort the a_i's and then adjust each to form a strictly increasing sequence, which ensures that all are unique. However, there might be other ways to assign the adjusted a_i's such that they are unique, but not in a sorted order, leading to a lower cost.

So the code's approach might not be optimal because it forces a certain order (sorted a_i's, adjusted to be increasing), but there might be a better arrangement where some a_i's are increased more, but the sum of (increase * t_i) is lower.

So the problem is that the code's approach is not considering other possible permutations of the adjusted a_i's. 

This suggests that the initial approach is incorrect. We need a different strategy.

Alternative approach: We need to assign to each category i an adjusted value s_i >= a_i, such that all s_i are distinct, and the sum of (s_i - a_i) * t_i is minimized.

How can we model this?

This is a problem of selecting s_i >= a_i, all distinct, to minimize the sum of (s_i -a_i)*t_i.

Each s_i must be at least a_i, and all s_i must form a set of unique integers.

So the problem is to select a multiset of s_i's such that s_i >=a_i, s_i unique, and sum (s_i -a_i)*t_i is minimized.

The key is to find for each a_i the minimal possible s_i, but considering that all s_i's must be unique.

But how to model this.

An optimal approach would assign s_i's such that higher t_i's have minimal possible increases. For example, for a category with high t_i, we want to assign the smallest possible s_i that is >=a_i and not used by any other category. For a category with lower t_i, it can take a higher s_i, which may be cheaper overall.

So the idea is to process the categories in order of increasing t_i. For each category, assign the smallest possible s_i that is >=a_i and not already taken. This way, categories with higher t_i (more costly to increase) get the earliest possible s_i, minimizing their increase.

Wait, perhaps this is the right approach.

For example, in the sample input:

Categories are:

Category 0: a=3, t=5

Category 1: a=7, t=2

Category 2: a=9, t=5

Category 3: a=7, t=7 (t_i is higher than category 1)

Category 4: a=8, t=5

Processing in order of increasing t_i:

Sort by t_i. t's are 2,5,5,5,7.

So order is category 1 (t=2), then 0 (t=5), 2 (t=5), 4 (t=5), 3 (t=7).

Now, assign s_i as the smallest possible >= a_i and not taken.

For category 1 (a=7, t=2): s_i=7.

Next category 0 (a=3, t=5): assign 3.

Category 2 (a=9, t=5): assign 9.

Category 4 (a=8, t=5): assign 8.

Category 3 (a=7, t=7): since 7 is taken, assign 10. So increase by 3. Cost 3*7=21. But total here is 0+0+0+0+21=21. Which is worse than sample's 6. So this approach is also not correct.

Hmm, this is not the correct way. So perhaps the order of processing is crucial.

Alternative idea: to process the elements in the order of increasing a_i and, for same a_i, increasing t_i. Or some other order.

Alternatively, think of the problem as a scheduling problem where each category can be scheduled to a certain s_i, and the s_i's must be unique. The cost is (s_i -a_i)*t_i. We need to assign s_i's >=a_i such that all are distinct, and the sum is minimized.

This seems similar to a greedy problem where we need to assign the earliest possible s_i's to the categories with the highest t_i. Because higher t_i's are more expensive to increase. So we want to assign the minimal possible s_i to the highest t_i's first.

Wait, that makes sense. So process the categories in descending order of t_i. For each category, assign the smallest possible s_i >=a_i that is not yet taken. This way, the higher t_i categories get the earliest possible s_i, which minimizes their increase. Lower t_i categories can take s_i's that are higher, but since their t_i is lower, the cost is less.

Let's try this approach with the first sample.

Sample 1:

Categories sorted by descending t_i:

t=7 (category 3, a=7), t=5 (categories 0,2,4), t=2 (category 1, a=7).

Processing order: category3 (a=7, t=7), then 0,2,4 (t=5), then category1 (t=2).

Available s_i's:

We need to assign each category a s_i >=a_i, unique.

Start with category3 (t=7, a=7): assign s=7.

Next, process category0 (a=3, t=5): assign s=3.

Category2 (a=9, t=5): assign s=9.

Category4 (a=8, t=5): assign s=8.

Now, category1 (a=7, t=2): current a_i=7. The s_i's already assigned are 3,7,8,9. So the minimal available s_i >=7 is 10. So assign 10. Cost (10-7)*2=6. Total is 6, which matches the sample.

So this approach works for the first sample.

Another test case: the second sample where all a_i's are distinct. The code would process each, assign their a_i as s_i, since all are unique. Cost is zero.

So the approach is:

Sort the categories in descending order of t_i. For each category in this order, assign the smallest possible s_i that is >=a_i and not yet used.

So the steps are:

1. Sort the categories in descending order of t_i. For same t_i, perhaps order by a_i? Not sure. But in the sample, the categories with same t_i (5) are processed in arbitrary order. For example, categories 0,2,4 (a=3,9,8). Assigning s_i in their a_i order would allow 3,8,9, which are all available. So in this case, their order doesn't matter.

But for same t_i, the a_i's can be processed in any order. So the key is to assign higher t_i first, and for same t_i, perhaps process lower a_i first to minimize their required s_i.

Wait, for same t_i, processing lower a_i first can allow them to take lower s_i's. But since their t_i is same, it may not matter. But perhaps it's better to process lower a_i's first for same t_i, as they can get lower s_i's, which might free up higher s_i's for other categories. But I'm not sure.

But perhaps for same t_i, the order of a_i's is not important. Let's see.

For example, two categories with same t_i=5: a=5 and a=7. Processing them in a order: first a=5 (s=5), then a=7 (s=7). If processed in reverse order, a=7 would take s=7, then a=5 takes s=5.

Either way, same cost.

But what if they have same a_i. For example, two categories with a=5, t=5. Then, processing in same order would assign s=5 to first, then s=6 to second. If processed in reverse order, same.

But the code's approach of sorting in descending t_i and for same t_i, perhaps sorting by a_i ascending. So that same t_i categories are processed in order of a_i ascending. Because that way, lower a_i's are processed first, which may allow higher a_i's to take their natural s_i's.

So the correct approach is:

Sort the categories in descending order of t_i. For categories with same t_i, sort them in ascending order of a_i. Then, for each category in this order, assign the smallest possible s_i >=a_i and not yet used.

To implement this, we can use a TreeSet (like in Java) to track the assigned s_i's. For each category in the sorted order, find the smallest s >=a_i that is not in the set. However, since n is up to 2e5, a naive approach with a TreeSet would be O(n log n), but for Python, which doesn't have a built-in TreeSet, this may be challenging.

Alternative approach:

We can track the last assigned s_i and determine the required s_i for the current category.

But how?

Another idea: When processing categories in order of descending t_i, and for same t_i, ascending a_i.

For each category, the required s_i is the maximum between a_i and the previous s_i +1. But this is only true if the previous s_i is for a category with higher or equal t_i, and sorted a_i in ascending order.

Wait, perhaps not. For example, if we process a category with higher a_i before a lower a_i, but same t_i.

But according to the sorted order, same t_i categories are processed in ascending a_i order. So the a_i's are processed in non-decreasing order.

So for same t_i, the a_i's are sorted in ascending order. So processing them in that order.

For each category, the required s_i is the maximum of its a_i and the next available s_i, which is the previous s_i +1.

So the algorithm would be:

Sort the categories in descending order of t_i. For same t_i, sort in ascending order of a_i.

Then, process the categories in this order. For each category, the required s_i is the maximum between a_i and the previous s_i +1. Then, the cost is (s_i -a_i)*t_i.

But how does this work?

Let's test this on the first sample.

Sample 1:

Categories sorted by t descending (7,5,5,5,2):

Categories in order: category3 (t=7, a=7), category0 (t=5, a=3), category2 (t=5,a=9), category4 (t=5,a=8), category1 (t=2,a=7).

Then, process them in this order.

prev starts at -infinity.

Processing category3 (a=7, t=7):

s_i = max(7, prev+1) = max(7, -inf +1) →7. cost 0. prev=7.

Processing category0 (a=3, t=5):

s_i = max(3,7+1=8) →8. So 8-3=5. cost 5*5=25. prev=8.

Processing category2 (a=9, t=5):

s_i = max(9,8+1=9) →9. cost 0. prev=9.

Processing category4 (a=8, t=5):

s_i = max(8,9+1=10). So 10-8=2. cost 2*5=10. prev=10.

Processing category1 (a=7, t=2):

s_i= max(7,10+1=11). 11-7=4. cost 4*2=8. Total cost 25+10+8=43. Which is way higher than the sample's 6. So this approach is incorrect.

Wait this suggests that the approach of processing in t descending and a ascending order, then s_i is previous +1 is not correct.

So what's the issue here?

Ah, because this approach forces the s_i's to form a non-decreasing sequence. So in the first sample, when processing category0 (a=3) after category3 (s=7), the required s_i is 8. But this is a large increase (5 units) and high cost. However, the optimal solution is to leave category0's a=3 as is, and adjust category1's a=7 to 10. 

But according to the sorted order, category0 is processed after category3. So the s_i is 7 for category3, then category0's a=3 is processed next. The code's approach requires the s_i for category0 to be max(3, 7+1=8). Which is 8. But the optimal solution assigns category0's s_i to 3. But why is that possible?

Because in the optimal solution, the s_i's are not in the order of processing. The code's approach assumes that the processing order must form a sequence of s_i's in non-decreasing order, but that's not the case.

So this approach is not correct.

So the problem is that the code's approach depends on the processing order to assign s_i's, which may not account for s_i's that are lower than previous ones, but are not yet assigned.

The correct way is to assign s_i's to each category, but allowing any s_i >=a_i, as long as they are unique. How can we do this efficiently?

The key is to model the available s_i's. For each category, we need to select the smallest possible s_i >= a_i that hasn't been taken yet.

But with n up to 2e5, we need an efficient way to track the used s_i's and find the next available.

An efficient data structure for this is a binary search tree or a sorted list. However, inserting and finding the next available s_i for each category in O(log n) time would be O(n log n), which is acceptable for n=2e5.

But in Python, implementing such a data structure is not straightforward. So perhaps we can find a way to compute the required s_i's without explicitly tracking all used s_i's.

Alternative idea:

If we sort the categories in a certain way, then the required s_i can be computed in a way that ensures all are unique.

Let's consider that the optimal s_i's are the minimal possible, given that each category is processed in a way that higher t_i's are processed first, and for each, we assign the smallest possible s_i >=a_i that is not yet taken.

This seems like the greedy approach. So the steps are:

1. Sort the categories in descending order of t_i, and for same t_i, ascending order of a_i.

2. For each category in this order:

   a. Assign s_i as the smallest possible value >= a_i that is not already assigned.

This would ensure that higher t_i categories get the earliest possible s_i, minimizing their increase.

The challenge is efficiently finding the smallest s_i >=a_i that is not yet assigned.

To do this, we can track the assigned s_i's in a sorted list and use binary search to find the next available s_i.

But for Python, with n up to 2e5, using a list and performing binary search each time (bisect module) may be feasible.

But inserting into a list would take O(n) time per insertion, which is O(n^2), which is too slow.

Alternative approach:

We can track the ranges of assigned numbers and find the earliest possible s_i.

But this is more complex.

Alternative approach inspired by the initial code's method:

When processing categories in a certain order, we can compute the required s_i based on the previous categories' s_i's.

But how?

If we process categories in order of descending t_i and ascending a_i, then for each category, the required s_i is the maximum between a_i and the previous s_i +1. But this doesn't work, as seen in the first sample.

Wait, in the first sample, the correct way is to process category3 (t=7, a=7) first. s_i=7. Then category0 (a=3, t=5) gets s=3 (but according to the previous method, it would be max(3,7+1)=8). So why is it possible to assign s=3 here?

Because the previous s_i's are not necessarily forming a contiguous block. So perhaps the initial approach's assumption of maintaining a previous s_i is invalid.

So the problem with the previous approach is that it assumes that the s_i's form a consecutive sequence, which is not the case.

Thus, the correct way is to track all assigned s_i's and find the minimal available s_i >=a_i.

This requires an efficient data structure to track the used s_i's and find the next available.

So how can we model this in Python?

An efficient way is to use a binary indexed tree or a segment tree, but that's complex.

Alternatively, we can use a disjoint-set (Union-Find) data structure to track the intervals of assigned s_i's and find the next available.

The idea is inspired by the "greedy algorithm for assigning meeting rooms" problem.

The Union-Find approach works as follows:

We need to assign the smallest possible s_i >=a_i that is not already used. For each s_i that is used, we can track the next available s_i.

When we assign s, the next available for s+1 can be found.

The Union-Find structure can help track the next available s_i.

Here's the approach:

- For each a_i, we want to find the smallest s >=a_i that is not used.

- The Union-Find structure tracks for each s, the next available s.

- The find function returns the next available s for a given a_i.

- Once we assign s, we merge it with s+1, so that subsequent queries for s will point to s+1.

This approach is known as the "find the smallest available number" and is used in some programming contest problems.

The key steps are:

1. Sort the categories in descending order of t_i. For same t_i, ascending a_i.

2. For each category in this order:

   a. Use the Union-Find structure to find the smallest s >=a_i.

   b. Assign s to this category, and add the cost (s -a_i)*t_i.

   c. Update the Union-Find structure to mark s as used.

The Union-Find structure helps in finding the next available s quickly.

Now, the Union-Find approach for this problem is as follows:

The parent array keeps track of the next available number. Initially, the parent of each s is s itself. When we assign a number s, we union s with s+1. The find function for s returns the smallest available number >=s.

However, since the a_i can be up to 1e9, we can't initialize the parent array for all possible s. So we need to handle this dynamically.

This is possible using a dictionary to represent the parent pointers.

Here's how the find and union operations work:

def find(s):
    if s not in parent:
        parent[s] = s
        return s
    if parent[s] != s:
        parent[s] = find(parent[s])
    return parent[s]

When we want to find the smallest available s >=a_i, we call find(a_i). This returns the smallest available s. Once we find s, we union it with s+1, so that the next find for s will return the next available number.

This approach dynamically tracks the assigned s_i's and efficiently finds the next available s_i.

This method ensures that each category is assigned the smallest possible s_i >=a_i that is not already taken. This is the optimal greedy strategy when processing categories in descending order of t_i.

So the steps are:

- Sort the categories in descending order of t_i. For same t_i, sort in ascending order of a_i.

- For each category in this order:

   - Find the smallest s >= a_i using the Union-Find structure.

   - Assign s to this category.

   - Add (s -a_i) * t_i to the total.

   - Union s with s+1 in the Union-Find structure.

This approach should handle all cases correctly.

Let's test this with the first sample.

Sample 1:

Categories sorted by t descending:

category3 (t=7, a=7)

category0 (t=5, a=3)

category2 (t=5, a=9)

category4 (t=5, a=8)

category1 (t=2, a=7)

Process category3:

find(7). Initially, parent is empty. parent[7] =7. Assign s=7. Cost 0. Then, union 7 with 8. So parent[7] =8.

Process category0: a=3. find(3). parent doesn't have 3. So assign s=3. cost 0. union 3 and 4.

Process category2: a=9. find(9) returns 9. assign s=9. cost 0. union 9 and 10.

Process category4: a=8. find(8) returns 8 (since 8 is not in parent yet). assign s=8. cost 0. union 8 and 9. Now, parent[8] =9. When we call find(8), it would return 9. But since 9 is already assigned, but after union with 10.

Process category1: a=7. find(7) returns parent[7] which is find(8) → parent[8] is 9, so find(9) returns 9. Then, since 9 is assigned, union 9 with 10. So s=9. But wait, no. Let's see:

Processing category1's a=7.

find(7):

Check parent. 7's parent is 8. So call find(8).

8's parent is 9. find(9) returns 9. So the available s is 9. Assign s=9. Then union 9 with 10.

But wait, category2's a=9 was assigned s=9, and then category4's a=8 was assigned s=8. Then category1's a=7 is processed. find(7) would return 7's parent is 8. find(8) returns 8's parent is 9. find(9) returns 9's parent is 9. So available s is9. Assign s=9 to category1. But this is already assigned to category2.

Wait, no. Because when category2's a=9 is processed, find(9) returns 9, which is assigned. Then, union 9 with 10. So parent[9] =10.

So when category1 is processed, a=7.

find(7) → parent[7] is 8. find(8) → parent[8] is9. find(9) → parent[9] is10. find(10) is 10. So s=10 is assigned. cost is 10-7=3. 3*2=6. Which matches the sample.

Ah, right. Because after processing category4 (a=8), the union of 8 and 9 means that find(8) returns 9. Then, when processing category1, the find(7) process would eventually find 10.

So the steps are:

category3's s=7. parent[7] =8.

category0's s=3. parent[3]=4.

category2's s=9. parent[9]=10.

category4's a=8:

find(8). 8 is not in parent. So assign s=8. parent[8] =9.

category1's a=7:

find(7) → parent[7]=8. find(8) → parent[8]=9. find(9) → parent[9]=10. find(10) is 10. So s=10.

So cost is (10-7)*2=6. Which is correct.

Thus, the Union-Find approach works.

So the code needs to implement this approach.

Now, how to implement the Union-Find with path compression and dynamic nodes in Python.

In Python, we can use a dictionary to represent the parent pointers.

The code will look like this:

parent = {}

def find(s):
    if s not in parent:
        parent[s] = s
        return s
    if parent[s] != s:
        parent[s] = find(parent[s])
    return parent[s]

def union(s):
    parent[s] = find(s+1)

Then, for each category in the sorted order:

s = find(a_i)

cost += (s -a_i) * t_i

union(s)

This should work.

But in Python, dictionaries are hash tables and can handle the parent pointers efficiently.

Now, let's think about the time complexity.

Each find and union operation is O(alpha(n)), which is near O(1). But since we process n categories, the total time is O(n alpha(n)), which is acceptable for n up to 2e5.

But the actual number of elements in the parent dictionary depends on the number of s_i's used. For example, if all a_i's are unique and sorted, then the s_i's are the same as a_i's, and the parent dictionary will have O(n) entries. But in worst cases, it could be O(n), which is manageable.

Thus, this approach should work.

So the steps are:

1. Read n.

2. Read a list and t list.

3. Create a list of tuples (t_i, a_i) for each category.

4. Sort this list in descending order of t_i, and for same t_i, ascending order of a_i.

5. Initialize the parent dictionary.

6. Initialize total cost to 0.

7. For each (t_i, a_i) in the sorted list:

   a. s = find(a_i)

   b. add (s -a_i) * t_i to total.

   c. union(s)

8. Output the total.

Testing this with sample 1:

The sorted list is:

(7,7), (5,3), (5,8), (5,9), (2,7).

Wait no. Wait the sorted order is by t descending and a ascending for same t.

The original categories' t_i and a_i are:

category3: t=7, a=7.

category0: t=5, a=3.

category4: t=5, a=8.

category2: t=5, a=9.

category1: t=2, a=7.

So sorted order:

(7,7), (5,3), (5,8), (5,9), (2,7).

Processing:

First category3 (7,7):

find(7) returns 7.

cost 0. union(7) → parent[7] = find(8). Since 8 is not in parent, it becomes 8. So parent[7] =8.

Second category0 (5,3):

find(3) →3. cost 0. union(3) → parent[3]=4.

Third category4 (5,8):

find(8) →8. cost 0. union(8) → parent[8] =9.

Fourth category2 (5,9):

find(9) →9. cost 0. union(9) → parent[9]=10.

Fifth category1 (2,7):

find(7) → parent[7] is 8. find(8) → parent[8] is 9. find(9) is parent[9] is10. find(10) →10. cost 3 *2=6. union(10) → parent[10]=11.

Total is 6.

Which matches the sample.

Another test case:

Sample 2:

Input:

5

1 2 3 4 5

1 1 1 1 1

All a_i's are distinct. So processing in any order (since t_i's are all 1), but sorted by a_i ascending.

For each category, a_i is s_i. So no cost. Output 0.

Thus, the code works.

Thus, the correct approach is to sort the categories in descending order of t_i and ascending order of a_i, then use a Union-Find structure to find the minimal s_i for each category.

Now, implementing this in Python.

The code:

Read n.

Read a as list.

Read t as list.

Create list of tuples: (-t_i, a_i) for sorting in descending t_i and ascending a_i.

Sort this list.

Initialize parent as empty dict.

total =0

for each tuple in sorted list:

    current_t = -t_i

    current_a = a_i

    s = find(current_a)

    total += (s - current_a) * current_t

    union(s)

print(total)

But in Python, the function find and union need to be defined.

But since functions can't be defined inside code that is supposed to be written as a single code block, we need to inline this.

So the code would look like this:

But in Python, the code can use a dictionary for parent and define find as a function with path compression.

But functions can't be nested in code that's to be written as a single code block.

Alternatively, we can implement find and union as helper functions.

But in Python, functions can be defined inside the code block.

So here's the code:

Read n.

Read a list.

Read t list.

Create a list of tuples, sorted by (-t_i, a_i).

Initialize parent as a dictionary.

Define find and union functions.

Process each tuple in sorted list.

So the code would be:

n = int(input())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

categories = sorted(zip(t, a), key=lambda x: (-x[0], x[1]))

parent = {}

def find(s):
    if s not in parent:
        parent[s] = s
        return s
    while parent[s] != s:
        parent[s] = parent[parent[s]]
        s = parent[s]
    return s

total = 0
for ti, ai in categories:
    s = find(ai)
    total += (s - ai) * ti
    parent[s] = s + 1  # union with s+1

print(total)

Wait, wait. The union operation is to set parent[s] = find(s+1), but how to handle that. 

In the code above, the 'find' function with path compression is implemented, but the union step is simply setting parent[s] = s+1. Is this correct?

No. The union step should merge s with s+1, so that subsequent find operations on s will return find(s+1). So after assigning s to the current category, we need to set parent[s] to the find(s+1) result.

But in the code above, after finding s, we set parent[s] = s+1. But this is equivalent to merging s with s+1.

Let's see.

For example, when s=7 is assigned, we call union(7). This sets parent[7] =8.

Then, when someone calls find(7), it will first look at parent[7] =8. Then find(8). If 8 is not in parent, then parent[8] is set to 8, and returns 8. But if 8 is already assigned, it may point to 9, etc.

This is exactly the same as the union in the previous approach.

Thus, the code above correctly implements the union step by setting parent[s] = s+1. 

But why? Because when we assign s, we want the next find(s) to return the find(s+1). So when you call find(s) again, it will follow the path to s+1. So this is a way to path compress s to s+1.

So the code is correct.

Testing this with the first sample:

When category3's ai=7 is processed, find(7) returns 7. Then parent[7] is set to 8.

When category1's ai=7 is processed, find(7) returns find(8). Since parent[8] is 8 (if not processed), and after setting parent[7] =8, find(7) will return 8, which is the next available.

But in the first sample, after processing category3 (s=7), category0 (s=3), category2 (s=9), category4 (s=8), and then category1 (s=7), the code does:

For category3:

s = find(7) →7. parent[7] =8.

For category0:

s = find(3) →3. parent[3] =4.

For category2:

s=find(9) →9. parent[9] =10.

For category4:

s=find(8) →8. parent[8] =9.

For category1:

s=find(7) → parent[7] is 8. find(8) returns 8. So s=8. parent[8] is 9. find(9) returns 9. parent[9] is 10. find(10) returns 10. So s=10.

Then, parent[10] is set to 11.

So the code's calculation is (10-7)*2=6.

Which matches.

Thus, the code is correct.

Another test case: the second sample.

All a_i's are distinct and already in increasing order. So when sorted by t_i (all 1), the a_i's are sorted in ascending order. Each find(ai) returns ai, so no cost. Total is 0.

Thus, the code works.

Thus, this approach is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

categories = sorted(zip(t, a), key=lambda x: (-x[0], x[1]))

parent = {}

def find(s):
    if s not in parent:
        parent[s] = s
        return s
    while parent[s] != s:
        parent[s] = parent[parent[s]]
        s = parent[s]
    return s

total = 0
for ti, ai in categories:
    s = find(ai)
    total += (s - ai) * ti
    parent[s] = s + 1  # Union with s+1

print(total)
```