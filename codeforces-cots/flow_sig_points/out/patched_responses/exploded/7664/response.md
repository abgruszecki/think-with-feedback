<think>
Okay, let's see. The problem is about maximizing the characteristic of an array after moving exactly one element to any position. The characteristic is the sum of a_i * i for each element. So, we need to find the best possible move to maximize this sum.

Hmm. The initial sum is easy to compute. For each element a_i in position i, we calculate a_i * i and sum all. Now, when we move an element a_k from position k to position m (could be any position, including the same one?), but we have to do exactly one move. Wait, the problem says "exactly once", so even if moving it to the same position, it's considered a move. But maybe in such a case, the sum remains the same. So the maximum can be either the original sum or some improved sum by moving an element.

But how do we find the best possible move efficiently?

Let's think about what happens when we move element a_k from position k to position m. The positions of other elements will shift. For example, if m is after k, then elements from k+1 to m will shift left by one. If m is before k, elements from m to k-1 shift right by one. But considering that this is a single move, perhaps we can model the effect of moving a_k to position m.

Wait, but for each possible a_k, how do we find the best position m to place it so that the new sum is maximized?

Alternatively, perhaps for each element a_k, the optimal position to move it is either as far left as possible or as far right as possible. Or maybe there's a specific position where the gain is maximum.

Alternatively, let's model the change in the sum when moving a_k from position i to j.

The original contribution of a_k is a_k * i. When moved to position j, the new contribution is a_k * j. But the other elements between i and j will shift. For example, if j < i (moving left), then elements from j to i-1 will shift right by one. Each of these elements' contributions will increase by their a value multiplied by (shift of 1). Similarly, if j > i, moving a_k to the right, elements from i+1 to j will shift left by one, each losing 1 in their position, so their contribution decreases by a value.

So the total change in the sum (delta) when moving a_k from i to j is:

delta = a_k * (j - i) + (sum of a elements between min(i+1, j) and max(i-1, j) that are shifted) * direction.

Wait, perhaps it's better to split into two cases:

Case 1: moving a_k from position i to position j where j < i.

When we insert a_k into position j, the elements from j to i-1 (originally positions j, j+1, ..., i-1) shift right by one. So their contribution increases by a[j] + a[j+1] + ... + a[i-1]. Because each of these elements is now in a position that's one higher. So the total delta for this case is a_k*(j - i) + sum_{pos = j to i-1} a[pos].

Case 2: moving a_k from position i to position j where j > i.

Here, when we insert a_k into position j, elements from i+1 to j (original positions) shift left by one. So their contribution decreases by sum_{pos = i+1 to j} a[pos]. The delta here is a_k*(j - i) - sum_{pos = i+1 to j} a[pos].

Wait, maybe. Let's think again.

Original sum is sum(a_p * p for all p).

After moving a_k from i to j:

- a_k is now at position j. So its contribution changes by a_k*(j - i).

The other elements: between i and j, their positions change. Let's see.

If j is to the left of i (j < i):

After moving a_k to j, the elements that were in positions j, j+1, ..., i-1 now move to positions j+1, j+2, ..., i. So each of these elements' positions increases by 1. So the sum of these elements' contributions increases by sum(a_p for p in j to i-1) * 1.

So the total delta in this case is a_k*(j - i) + sum_{p=j}^{i-1} a_p.

Similarly, if j is to the right of i (j > i):

The elements that were in positions i+1 to j now move to positions i to j-1. So each of their positions decreases by 1. The sum of their contributions decreases by sum_{p=i+1}^j a_p. So the delta here is a_k*(j - i) - sum_{p=i+1}^j a_p.

So the overall delta when moving a_k from i to j is:

delta = a_k * (j - i) + (sum between j and i-1 if j < i) or delta = a_k * (j - i) - (sum between i+1 and j if j > i).

Our goal is to find the maximum possible delta over all possible moves (i,j) where 1 <= j <=n, and then add that delta to the original sum.

But trying all possible i and j is O(n^2), which is impossible for n up to 2e5.

We need a way to compute for each element a_k, the best possible delta it can contribute, and then pick the maximum among all elements.

So for each element a_k at position i, we need to find the j that maximizes the delta for moving a_k to j.

So the problem reduces to, for each i, compute the maximum delta over all j possible, then take the maximum over all i.

Now, how can we compute this efficiently for each i?

Let's consider for each i, the possible j where moving a_k (a[i]) from position i to j gives the maximum delta.

We can model this as two separate cases for each i: j < i and j >= i.

Wait, perhaps not. Let's think.

For each i, the optimal j could be anywhere. Let's see.

Case 1: j < i.

The delta is a_k*(j - i) + sum_{p=j}^{i-1} a[p].

We can write this as a_k * (j - i) + (prefix_sum[i] - prefix_sum[j]).

Because sum from j to i-1 is prefix_sum[i] - prefix_sum[j], assuming prefix_sum is 1-based, with prefix_sum[0] =0.

Similarly, for case j > i.

The delta is a_k*(j -i) - (prefix_sum[j] - prefix_sum[i]).

So for each i, the maximum delta is the maximum over all j of (a[i]*(j -i) + (prefix_sum[i] - prefix_sum[j]) if j <i) OR (a[i]*(j -i) - (prefix_sum[j] - prefix_sum[i]) if j >i).

Hmm. So for each i, let's compute the maximum delta achievable by moving a[i] to any j.

We need to find the j that maximizes the delta for each i, then take the maximum over all i.

But how to compute this efficiently.

Let's first handle the case where j <= i.

In this case, delta for j is (a[i]*(j -i) ) + (prefix_sum[i] - prefix_sum[j]).

We can rearrange this as (a[i] * j - a[i] *i) + (prefix_sum[i] - prefix_sum[j]).

This simplifies to (a[i] * j) - a[i]*i + prefix_sum[i] - prefix_sum[j].

Which can be rewritten as (a[i] *j - prefix_sum[j]) + (prefix_sum[i] - a[i] * i).

Notice that (prefix_sum[i] - a[i] *i) is a constant for a particular i. So, the term that varies with j is (a[i] *j - prefix_sum[j]).

So for j <= i, the maximum delta is (max (a[i] *j - prefix_sum[j] for j in 1..i)) ) + (prefix_sum[i] - a[i] *i).

Similarly, for j >= i, the delta is a[i]*(j -i) - (prefix_sum[j] - prefix_sum[i]).

Which simplifies to a[i] j - a[i]i - prefix_sum[j] + prefix_sum[i].

Again, this can be written as (a[i] j - prefix_sum[j]) + (prefix_sum[i] - a[i]i).

Wait, same as the previous case? Wait, for j >=i:

delta = a[i] (j -i) - (prefix_sum[j] - prefix_sum[i]) 

= a[i] j - a[i]i - prefix_sum[j] + prefix_sum[i]

= (a[i] j - prefix_sum[j]) + (prefix_sum[i] - a[i]i)

So, for both j <=i and j >=i, the delta is (a[i] j - prefix_sum[j]) + (prefix_sum[i] - a[i]i).

Wait, that's interesting. So regardless of j's position relative to i, the delta is (a[i]j - prefix_sum[j]) + (prefix_sum[i] - a[i]i).

But wait, is that correct? Because when j <=i, the sum is prefix_sum[i] - prefix_sum[j], but when j >=i, the sum is prefix_sum[j] - prefix_sum[i+1] (since the sum from i+1 to j is prefix_sum[j] - prefix_sum[i]?), wait no:

Wait, in the case where j >i, the sum subtracted is the sum from i+1 to j. Because when you move a[i] to j, the elements i+1 to j shift left by one. So their sum is sum_{p=i+1}^j a[p] = prefix_sum[j] - prefix_sum[i].

So delta for j>i is a[i]*(j-i) - (prefix_sum[j] - prefix_sum[i]).

So combining both cases, the delta for any j is (a[i] j - prefix_sum[j]) + (prefix_sum[i] - a[i]i).

Wait, let me verify:

For j < i:

delta = a[i]*(j -i) + (prefix_sum[i] - prefix_sum[j]) 

= a[i] j - a[i] i + prefix_sum[i] - prefix_sum[j]

= (a[i]j - prefix_sum[j]) + (prefix_sum[i] - a[i]i)

Yes.

For j >i:

delta = a[i]*(j-i) - (prefix_sum[j] - prefix_sum[i])

= a[i] j - a[i]i - prefix_sum[j] + prefix_sum[i]

= (a[i]j - prefix_sum[j]) + (prefix_sum[i] -a[i]i)

Same as before.

So regardless of j being less than or greater than i, the delta is (a[i] j - prefix_sum[j]) + (prefix_sum[i] - a[i]i).

But wait, for j =i, the delta would be (a[i] i - prefix_sum[i]) + (prefix_sum[i] - a[i]i) = 0. Which makes sense because moving to the same position doesn't change anything. But the problem requires exactly one move. So even if j=i, we have to perform the move. But in that case, the delta is zero, so the sum remains the same. So the maximum delta could be the best possible delta over all possible j, including j=i (but if all other deltas are negative, then moving to j=i gives zero delta, which is better than doing nothing? Wait, no. Wait, the problem says that the operation must be performed exactly once. So even if all possible moves result in a delta of zero or negative, we have to perform one move, so the sum can't be higher than the original. Wait, but in that case, the best option is to pick any move that gives the least loss, but since we have to perform exactly one move, even if all are worse than original. So in our approach, the delta is the maximum possible (could be positive or negative, but the original sum plus delta will be the maximum possible after exactly one move).

So, regardless of j, the delta for moving a[i] to j is (a[i] j - prefix_sum[j]) + (prefix_sum[i] - a[i]i).

So, for each i, the maximum delta is the maximum over all j of (a[i] j - prefix_sum[j]) plus the term (prefix_sum[i] - a[i]i).

The term (prefix_sum[i] - a[i]i) is a constant for a given i. So for each i, the maximum delta is (max (a[i] j - prefix_sum[j] for all j in 1..n )) + (prefix_sum[i] - a[i]i).

Wait, that's a key insight. Because for any j, the delta is this expression. So for each i, we need to find the j (can be any position from 1 to n) that maximizes (a[i] j - prefix_sum[j]), and then add the (prefix_sum[i] - a[i]i) term.

So the problem reduces to: for each i, compute the maximum value of (a_i * j - prefix_sum[j]) for j in 1..n. Then add (prefix_sum[i] - a_i *i) to get the delta. Then find the maximum delta over all i.

Once we have the maximum delta, we add it to the original sum to get the answer.

But how to compute, for each i, the maximum of (a_i * j - prefix_sum[j]) for all j.

Wait, but a_i varies per i. So for each a_i, the function f(j) = a_i * j - prefix_sum[j] is a linear function in j. The maximum of this function over j from 1 to n can be found by looking for the j that maximizes a_i *j - prefix_sum[j]. 

But how to compute this for each i efficiently?

The prefix_sum array is known. For each i, a_i is known. So for each i, f(j) = a_i *j - prefix_sum[j].

We can precompute the prefix_sum array once. Then for each i, compute the maximum of f(j) over j=1..n.

But doing this naively for each i would be O(n^2), which is not feasible for n=2e5.

So we need a way to compute for each a_i the maximum of a_i * j - prefix_sum[j], which can be found quickly.

This is similar to the problem of finding for a given slope a_i, the maximum value of a_i * x - y, where (x, y) is a set of points (j, prefix_sum[j]).

In computational terms, this is equivalent to finding the maximum of linear functions evaluated at a_i. This can be approached using convex hull trick (like for line arrangements and maximum queries). But how?

The convex hull trick works when you have a set of lines (or linear functions) and you want to query for a given x which line gives the maximum value. Here, the functions are f_j(x) = x * j - prefix_sum[j]. For each j, the line is f_j(x) = j * x - prefix_sum[j]. Then, when given a_i (as x), we need to find the j that maximizes f_j(a_i). So the maximum value of j*a_i - prefix_sum[j] over j.

So the convex hull trick can be applied here. We can precompute the lines for all j, and then for each query x=a_i, compute the maximum f_j(x).

But in this problem, the lines are ordered in j from 1 to n. So the convex hull can be built in a way that allows efficient querying.

Wait, but the convex hull trick is used when the lines are added in a certain order (like increasing or decreasing slope) and queries are made in a certain order. For this problem, the lines are f_j(x) = j * x - prefix_sum[j]. So the slope of each line is j. Since j increases from 1 to n, the slopes are in increasing order.

So the lines are added in order of increasing slope, which allows building a convex hull that can be used for querying. So when the slopes are in increasing order, and the query points can be arbitrary, but we need to find the maximum for each x=a_i, which can be done using a binary search on the convex hull.

So, the plan is:

1. Precompute the prefix_sum array.

2. Preprocess all lines f_j(x) = j * x - prefix_sum[j], which are ordered by increasing slope (since j is increasing).

3. Build a convex hull data structure (like a lower/upper hull) that allows querying the maximum f_j(x) for a given x.

4. For each a_i (x = a_i), compute the maximum value of j * a_i - prefix_sum[j], which is the maximum of f_j(a_i) over all j. This can be found efficiently using the convex hull data structure.

Once we have that maximum value for each a_i, then the delta for moving a_i is (max_j) + (prefix_sum[i] - a_i * i).

Then, the answer is the original sum plus the maximum delta over all i.

This approach would be O(n) for building the convex hull (since the slopes are in order, so we can build the hull incrementally in linear time) and O(n) for querying each a_i (each query is O(1) or O(log n) depending on the convex hull implementation). For n up to 2e5, this is acceptable.

So the steps are:

- Compute original sum.

- Compute prefix_sum array.

- Precompute for each j the line (slope j, intercept -prefix_sum[j]).

- Build a convex hull data structure that allows querying the maximum line at a given x.

- For each i, compute the maximum value of (a_i *j - prefix_sum[j]) using the convex hull.

- Compute delta_i = max_val + (prefix_sum[i] - a_i *i).

- Find the maximum delta_i, then add to original sum.

Now, the key is to implement the convex hull trick efficiently.

But wait, in this case, the lines are added in order of increasing slope. So the convex hull can be maintained in a way that each new line is added to the hull, and any previous lines that are no longer part of the upper envelope (for maximum) are removed. This is known as the convex hull trick with offline processing when the lines are sorted by slope and queries can be in any order.

Implementing the convex hull trick with lines sorted in increasing slope:

The upper envelope (for maximum) can be maintained using a deque. For each new line, we check if adding it makes the previous lines in the deque irrelevant. The condition for removing lines is based on the intersection points.

The convex hull can be built as follows:

Initialize a deque. For each j from 1 to n:

   while the deque has at least two lines, say l1 and l2 (where l2 is the last line in the deque), and adding the new line l3 (current j) would make l2 irrelevant. To check this, compute the intersection x of l2 and l3, and the intersection x of l1 and l2. If the x of l2 and l3 is <= x of l1 and l2, then l2 is not part of the upper envelope and can be removed.

   add the current line to the deque.

Once all lines are processed, the deque contains the lines in the upper envelope.

Then, for querying x=a_i, we can perform a binary search on the deque to find the line that gives the maximum value at x.

But for large n (2e5), a binary search per query (each a_i) would be O(n log n) total time, which may be acceptable.

Alternatively, if the queries are not sorted, then each query would require a binary search over the deque. So for n=2e5, it's 2e5 log (2e5) steps, which is manageable.

Alternatively, we can use a pointer approach. Since the lines are sorted by slope, and x can vary, but for each query x, the optimal line is the one where the slope is the largest possible such that the line is still optimal at x.

But I'm not sure. So perhaps the binary search approach is safer.

So, the steps for the convex hull trick:

Each line is represented as (m, b) where m is the slope (j), and b is the intercept (-prefix_sum[j]).

The deque stores lines in a way that the upper envelope can be queried.

For querying x=a_i:

We need to find the line in the deque that maximizes m *x + b.

Since the lines are sorted by increasing m, their intersection points form a sequence that allows binary search.

The binary search checks where x is in the sequence of intersection points.

So, the code would look something like this:

Initialize the deque.

For j in 1..n:

   add line (m=j, b= -prefix_sum[j]) to the deque, maintaining the upper envelope.

Once all lines are added, the deque contains the lines in the upper envelope.

For each a_i (x), perform a binary search on the deque to find the line that gives the maximum value at x.

But how?

The deque contains lines in order of increasing slope. The intersection points between consecutive lines in the deque form increasing x values. So for the deque, the lines are ordered such that their intersection x values are increasing.

So, to find the optimal line for a given x, we can binary search on the deque to find the first line where the intersection with the next line is >=x. Then, the optimal line is the previous one.

Alternatively, the optimal line is the last line in the deque for which the intersection with the next line is <=x.

This is a standard approach for the convex hull trick with sorted lines and arbitrary queries.

But implementing this correctly can be a bit tricky.

Alternatively, here's a way to perform the binary search:

We can compute for consecutive lines in the deque their intersection points. For example, lines[i] and lines[i+1] intersect at x = (b_{i+1} - b_i) / (m_i - m_{i+1}).

Since the lines are in order of increasing m, m_i < m_{i+1}.

So for the upper envelope, the intersection points between consecutive lines are increasing. So the x coordinates where the optimal line changes are in increasing order.

Thus, to find the optimal line for a given x, we can binary search the deque to find the largest index i where the intersection between lines[i] and lines[i+1] is <=x. The optimal line is lines[i+1], or lines[0] if all intersections are >x.

But perhaps more accurately, the optimal line is the one where x is between the previous intersection and the next intersection.

Alternatively, the binary search can find the first line where the intersection with the next line is >=x, and then the optimal line is the one before that.

But perhaps the easiest way to code this is to use a binary search over the deque.

However, with a deque, we can't directly index elements. So perhaps we need to convert the deque to a list first, then perform the binary search on the list.

But with n up to 2e5, converting a deque to a list each time we process a query is O(n), which is not feasible.

Wait, no. The convex hull is built once for all j, and then all queries are processed. So during the building of the convex hull, we can collect the lines in a list, which is possible if we manage the convex hull as a list.

Wait, the standard convex hull trick for offline processing (lines added in order) builds the convex hull as a list. So during the building phase, we can manage the list as follows:

Initialize an empty list.

For each j from 1 to n:

   while the list has at least two elements, check if the last line in the list is not needed when adding the new line. To check this, compute the intersection between the last line (l2) and the new line (l3), and compare it to the intersection between the second last line (l1) and l2. If the intersection between l1 and l2 is >= the intersection between l2 and l3, then l2 can be removed.

   add the new line (j, -prefix_sum[j]) to the list.

Once all lines are processed, the list contains the lines in the upper envelope, ordered by increasing slope, and their intersection points are increasing.

Once the list is built, for each query x (a_i), perform a binary search on this list to find the line that maximizes m *x + b.

So, how to perform the binary search:

We can iterate through the list and find the first line where the intersection with the next line is >=x. The optimal line is the one before that.

Wait, perhaps the binary search can find the largest index k where the x is >= the intersection point between lines[k] and lines[k+1], and the optimal line is lines[k+1].

Alternatively, here's an approach:

We can binary search the index k such that lines[k] is the optimal line for x.

The binary search works by checking if x is to the left of the intersection between lines[mid] and lines[mid+1]. If yes, then the optimal line is in the left half. Otherwise, in the right half.

The code would look something like this:

left = 0

right = len(lines) - 1

while left < right:

   mid = (left + right) // 2

   if x < intersect(lines[mid], lines[mid+1]):

       right = mid

   else:

       left = mid + 1

The optimal line is lines[left], but perhaps I need to check this.

Wait, perhaps I should check for the line where lines[k] is the last line such that the intersection between lines[k] and lines[k+1] is >=x.

Alternatively, the code can be structured to find the line that gives the maximum value.

But this might get complicated.

Alternatively, since the lines are in order of increasing slopes, and their intersection points are in increasing order, the optimal line for x is the last line in the list where x is to the right of its intersection with the previous line. But I'm not sure.

Alternatively, here's a different approach. For the lines in the upper envelope list (lines), the intersection points between consecutive lines are x_0, x_1, x_2, etc. These x's are in increasing order because the lines are added in order of increasing slope.

So, for any x, the optimal line is the first line in the list such that x is <= x_i (the intersection between line i and line i+1). If x is <= x_0, then line 0 is optimal. If x_0 < x <=x_1, then line 1 is optimal, and so on. If x is larger than all x_i, then the last line is optimal.

So the binary search would find the smallest k where x <= x_k. Then line k is the optimal line.

But how to implement this.

Alternatively, the binary search can find the largest k where x >= x_{k-1}, where x_{k-1} is the intersection between line k-1 and line k.

But this might require handling the edge cases (k=0 and k = len(lines)-1).

Alternatively, the code can proceed as follows:

if len(lines) == 1:

   return lines[0]

else:

   low = 0

   high = len(lines) -1

   while low < high:

       mid = (low + high) // 2

       if get_x(lines[mid], lines[mid+1]) >= x:

           high = mid

       else:

           low = mid +1

   return lines[high]

Wait, this is a possible approach. Let's see.

For example, for the lines list:

line0, line1, line2, line3.

The intersections are x0 (line0 and line1), x1 (line1 and line2), x2 (line2 and line3).

We want to find the smallest k where x <= xk.

If x <= x0, then the optimal line is line0.

If x0 < x <=x1, the optimal line is line1.

If x1 <x <=x2, optimal line is line2.

If x> x2, optimal line is line3.

The binary search starts with low=0 and high=3-1=2 (since len(lines) is 4, len(lines)-1 is 3? Wait, lines are 0-based, so len(lines) is 4, indexes 0-3.

Wait, perhaps the code above is not correct. Let's adjust.

Suppose lines is a list of 4 elements (indices 0-3). The intersections are between lines[0] and lines[1], lines[1] and lines[2], lines[2] and lines[3]. So there are 3 intersection points.

In this case, the binary search for high would start at len(lines) -2.

But perhaps the code should be adjusted to handle the indices correctly.

Alternatively, the code can use the following steps:

Initialize left=0, right=len(lines)-1.

While left < right:

   mid = (left + right) // 2

   if the intersection between lines[mid] and lines[mid+1] >=x:

       right = mid

   else:

       left = mid +1

At the end, lines[left] is the optimal line.

But in the case where x is larger than all intersection points, the binary search will end up with left=len(lines)-1, which is correct.

Let's test this logic with a sample.

Suppose lines have 3 lines (indices 0,1,2), and their intersection points are x0 and x1, where x0 <x1.

If x is greater than x1, then the optimal line is line2.

The binary search starts with left=0, right=2.

mid=(0+2)/2=1. Check if x <=x1. If x is larger, then the condition (intersection lines[mid] and lines[mid+1] >=x) is false. So left becomes mid+1=2. Loop ends, left=2. So lines[2] is returned.

Yes.

Another example: x is between x0 and x1. The binary search:

left=0, right=2. mid=1. Check if x <=x1 (the intersection between lines[1] and lines[2]). If yes, then right=1. Now left=0, right=1. mid=0. Check if x <=x0 (intersection between lines[0] and lines[1]). If x is >x0, then left becomes 1. Now left=right=1. So lines[1] is selected.

Which is correct.

So the code seems to work.

Thus, the binary search approach can be used.

Once we have the optimal line, we can compute the value m*x + b, where m is j, and b is -prefix_sum[j].

So for each a_i (x), the maximum value is the maximum of all lines evaluated at x.

Now, the code outline is:

Compute prefix_sum.

Build the convex hull lines.

For each a_i in the array:

   x = a_i

   perform binary search on the lines to find the optimal line.

   compute the value of the line (m*x +b).

   delta_i = value + (prefix_sum[i] - a_i * i)

Compute the maximum delta_i.

Original sum + maximum delta_i is the answer.

But wait, the original sum is sum(a_i * i for i in 0..n-1 (if 0-based)).

Yes.

Now, the code steps:

Read n.

Read array a (1-based or 0-based? Well, in Python, it's easier to use 0-based, but the problem uses 1-based positions. So let's adjust accordingly.)

Compute prefix_sum where prefix_sum[0] =0, and prefix_sum[i] = a[0] + a[1] + ... +a[i-1], assuming 0-based a array.

Wait, the problem's input is the array a of length n, with elements a_1 to a_n (since 1 ≤ i ≤n in the input description). So in code, perhaps we can read the array as 0-based (indexes 0 to n-1), but the positions are 1-based. So for the code, the element at index i in the array is a_i+1 in the problem's terms.

Wait, perhaps better to read the array as 0-based, and then for the original sum, for each element a[i], multiply by (i+1) (since the first element is position 1).

Similarly, the prefix_sum array can be 1-based (prefix_sum[0] =0, prefix_sum[1] =a[0], prefix_sum[2] =a[0]+a[1], etc.)

So, for example:

n =4, a = [4,3,2,5]. Then positions are 1,2,3,4.

prefix_sum[0] =0.

prefix_sum[1] =4.

prefix_sum[2] =4+3=7.

prefix_sum[3] =9.

prefix_sum[4] =14.

But in code, we can compute prefix_sum as a 1-based array.

But in Python, it's easier to have prefix_sum as a list where prefix_sum[i] is sum(a[0..i-1]).

So for code:

prefix_sum = [0]

for num in a:

   prefix_sum.append(prefix_sum[-1] + num)

So prefix_sum[i] is sum of a[0] to a[i-1].

Thus, sum from j to i-1 (inclusive) is prefix_sum[i] - prefix_sum[j].

Now, building the convex hull:

For each j from 1 to n (since positions are 1-based):

   m = j

   b = -prefix_sum[j]

   add the line (m, b) to the convex hull.

But the problem uses 1-based positions. So j ranges from 1 to n.

In code:

lines = []
for j in range(1, n+1):
    m = j
    b = -prefix_sum[j]
    while len(lines) >=2:
        # check if the last line and the one before can be popped
        # lines[-2], lines[-1], new_line
        # compute intersection between lines[-2] and lines[-1] as x1
        # compute intersection between lines[-1] and new_line as x2
        # if x2 <=x1, then lines[-1] is not part of the upper hull
        x1 = intersection(lines[-2], lines[-1])
        x2 = intersection(lines[-1], (m,b))
        if x2 <= x1:
            lines.pop()
        else:
            break
    lines.append( (m, b) )

But how to compute the intersection between two lines (m1, b1) and (m2, b2)?

The intersection x is (b2 - b1) / (m1 - m2). But since m1 < m2 (since j increases), m1 - m2 is negative.

So x = (b2 - b1) / (m1 - m2).

But to compare x1 and x2, we can compute them as fractions.

But in code, perhaps using floating points is not safe. However, since j can be up to 2e5, but the a_i can be up to 1e6, the denominator can be up to 2e5. But in Python, using floating points should be precise enough for comparison purposes.

Alternatively, compute the cross product to avoid division.

But perhaps using floating points is manageable.

So the function to compute the intersection is:

def get_intersect(line1, line2):
    # line1: (m1, b1), line2: (m2, b2)
    # returns x where m1*x +b1 = m2*x +b2
    if line1[0] == line2[0]:
        # parallel lines, no intersection
        return float('-inf') if line1[1] < line2[1] else float('inf')
    return (line2[1] - line1[1]) / (line1[0] - line2[0])

So for two lines, line1 and line2, the intersection x is (b2 -b1)/(m1 - m2).

Now, during the convex hull building phase:

For each new line (m, b), we check if adding it causes the previous lines to be irrelevant.

So in code:

lines = []
for j in range(1, n+1):
    m = j
    b = -prefix_sum[j]
    # Add current line to the hull
    # Check if the last two lines and the new line form a concave structure
    while len(lines) >= 2:
        line1 = lines[-2]
        line2 = lines[-1]
        line3 = (m, b)
        # Calculate x where line2 and line3 intersect
        x2 = get_intersect(line2, line3)
        # Calculate x where line1 and line2 intersect
        x1 = get_intersect(line1, line2)
        if x2 <= x1:
            # line2 is dominated by line1 and line3, so remove it
            lines.pop()
        else:
            break
    lines.append( (m, b) )

Once all lines are added, the lines list contains the upper envelope.

Then, for each query x = a_i (for each element in the array, but wait, the array is 0-based. For example, the element at index 0 is a_1 in the problem statement. So when the problem says "move a_k", which is position k in 1-based terms, but in code, the array is 0-based.

Wait, the original array is given as a_1 to a_n. So in code, the array is read as a list, say, arr = list of a_1 to a_n, which is 0-based in code.

Wait, no. Wait, in the input, the second line contains n integers, which are the elements a_1, a_2, ..., a_n. So in code, when we read the array, it's 0-based in code, but represents the a_1 to a_n elements.

So in code, for the j-th position (1-based in problem terms), the code's array index is j-1.

But in the code, the lines are built for j from 1 to n, which are the 1-based positions.

So for the lines, each j corresponds to a position in the problem's terms.

Now, for each element a_i in code's 0-based array, which corresponds to a_{i+1} in problem terms, and is at position (i+1) in the problem's array.

So for the code's a[i], in the problem's terms, it is a_{i+1}, located at position i+1.

Thus, when processing each a_i in code (i from 0 to n-1), the original position is i+1.

So for each a_i in code, we need to compute delta_i = (max_j (j * a_i - prefix_sum[j]) ) + (prefix_sum[i+1] - a_i * (i+1) )

So the code steps are:

original_sum = sum( a[i] * (i+1) for i in range(n) )

Then, for each code's a_i (original position is i+1):

delta_i = (max_j (a_i * j - prefix_sum[j]) ) + (prefix_sum[i+1] - a_i * (i+1))

Now, the lines list is built for j from 1 to n (problem's terms), which corresponds to code's j in 1-based. So the j here is the position in problem terms.

Thus, for each a_i in code's array (element a_{i+1} at position i+1), the query x is a_i (the value of the element in code's array). Because the element's value is a_{i+1} in problem terms, which is the code's a[i].

So for example, in the first sample input:

4

4 3 2 5

code's a is [4,3,2,5], positions 0-3. Problem's a_1 is 4 (code's a[0]), a_2 is 3 (code's a[1]), etc.

The original sum is 4*1 +3*2 +2*3 +5*4 =4 +6 +6 +20=36.

The lines are built for j=1 to 4. For each j, the line is m=j, b= -prefix_sum[j], where prefix_sum[j] is the sum of the first j elements in problem's terms (a_1 to a_j).

So prefix_sum[1] =4, prefix_sum[2] =7, prefix_sum[3]=9, prefix_sum[4]=14.

Thus, for j=1: line (1, -4)

j=2: line (2, -7)

j=3: line (3, -9)

j=4: line (4, -14)

So the convex hull will process these lines.

For each code's a_i (values 4,3,2,5):

For a_0 =4 (code's i=0, which is problem's element a_1, position 1):

x =4.

We query the lines for x=4.

What's the optimal line?

We need to find j where j*4 - prefix_sum[j] is maximum.

Compute for each j:

j=1: 4*1 -4 =0

j=2: 3*2 -7 =6-7 =-1

j=3: 2*3 -9 =6-9 =-3

j=4:5*4 -14=20-14=6.

So maximum is 6 (j=4).

So delta_i =6 + (prefix_sum[1] -4*1) =6 + (4 -4) =6.

So if we move a_1 (value4) to j=4, the delta is6. The original sum is36 +6=42. But the sample's answer is39. Wait, that doesn't make sense.

Wait, this suggests that there's a mistake in the approach.

Wait, perhaps I made a mistake in the example.

In the first sample input:

The best move is to take the first element (4) and move it before the third (5), which is position3 in the problem's terms (code's j=3).

The new array becomes [3,2,4,5], but in problem's terms, positions1-4:3 is at position1 (3*1), 2 at position2 (2*2),4 at position3 (4*3),5 at4 (5*4). Sum is3+4+12 +20=39.

But according to the code's approach for the first element (a_0=4), the code would compute delta_i as6, leading to sum 36+6=42. Which contradicts.

Hmm. So there's a mistake in the approach.

Ah, wait, what's the delta when moving a_1 (problem's a_1, code's a[0], value4) to position4 (problem's j=4).

In this case, the new array is [3,2,5,4].

The positions are:

3*1 +2*2 +5*3 +4*4 =3 +4 +15 +16 =38. The delta is38-36=2. Which would be the original sum plus delta of2, which is38, but according to code's approach, it's36+6=42. So something is wrong.

This indicates that the approach is incorrect.

So where is the error?

Ah, I see. The code's approach computes the maximum possible delta for each element, but perhaps this delta is not achievable when moving the element to j.

Wait, perhaps the code's approach allows j to be any position, including those that are not possible. For example, moving a_i to j may not take into account the shifting of other elements correctly.

Wait, according to the model, the delta computed is a_k*(j -i) + sum_{p=j}^{i-1} a_p (if j <i), which is correct.

But the code's approach models the delta as (a_i *j - prefix_sum[j]) + (prefix_sum[i] -a_i*i), which is supposed to be equivalent.

But perhaps there's a miscalculation here.

Let's re-calculate for the first sample.

Original sum:4*1 +3*2 +2*3 +5*4 =4 +6 +6 +20 =36.

Now, for the code's a[0], which is4. The original position is i=1 (code's i=0, problem's position1).

When moving this element to j=4 (problem's j=4), the delta is:

a_i*(j-i) - (prefix_sum[j] - prefix_sum[i]) ?

Wait, j=4 is larger than i=1. So delta is:

a_i (j -i) - (prefix_sum[j] - prefix_sum[i]) 

=4*(4-1) - (prefix_sum[4] - prefix_sum[1]) 

=4*3 - (14 -4) 

=12 -10 =2.

Which would add 2 to the original sum (36+2=38). Which matches the actual sum when moving to j=4.

But according to the code's approach, the delta is (max_j (a_i *j - prefix_sum[j])) + (prefix_sum[i] -a_i *i).

So for i=1 (code's a[0] is4), prefix_sum[i] is prefix_sum[1] =4.

The term (prefix_sum[i] -a_i *i) is4 -4*1=0.

The max_j (a_i *j - prefix_sum[j]) is max(4*1 -4=0, 4*2 -7=1, 4*3 -9=3, 4*4 -14=2). The maximum is3 (at j=3).

So delta_i is3 +0=3. So the new sum would be36+3=39, which matches the sample.

Ah! So why is the code's approach giving the delta as3, which when added to 36 gives39.

But earlier, when considering j=4, the code's approach gives delta_i =6+0=6. That's incorrect. So perhaps the model is wrong.

Wait, what's the code's approach for the first sample.

In the code's approach, when j=3 (problem's j=3), the line for j=3 has m=3, b=-9. So a_i=4, x=4.

value is 3*4 + (-9) =12-9=3.

Which is correct. So delta_i is3+0=3.

But when j=4, line for j=4 has m=4, b=-14. value is4*4 + (-14)=16-14=2.

So the maximum for x=4 is3 (from j=3), not 2 or 6.

So delta_i is3, which when added to36 gives39. Which matches the sample.

So the code's approach is correct.

Earlier mistake was because when I calculated j=4, I forgot that the line for j=4 is (4, -14), so 4*4 -14=2, not6. So the code's approach is correct.

Thus, the code's approach works.

Now, the code should correctly find the maximum delta.

Thus, the code's approach is correct.

Now, the code needs to be written.

First, compute the original_sum.

Then compute prefix_sum.

Then build the convex hull.

Then for each a_i in code's array, compute x =a_i, find the optimal line, compute the maximum (m*x +b), add (prefix_sum[i+1] - a_i*(i+1)) to get delta_i.

Finally, find the maximum delta_i, add to original_sum.

Now, let's code this.

But in Python, handling large n is possible, but needs to be efficient.

The convex hull building is O(n) time because each line is added once and removed at most once.

The binary search for each query is O(log m), where m is the number of lines in the convex hull (which is up to n, but in practice much less).

Thus, for n=2e5, this is acceptable.

Now, code.

Read n.

Read a as list of integers (code's 0-based, but represents a_1 to a_n).

Compute prefix_sum.

Build lines.

Then for each code's a_i (i in 0..n-1):

   x =a[i]

   perform binary search on lines to find the best line.

   compute value =m*x +b.

   delta_i =value + (prefix_sum[i+1] - a[i]*(i+1)).

Compute maximum delta.

Add to original_sum.

Now, code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    prefix_sum = [0] * (n +1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + a[i]

    original_sum = sum( (i+1)*a[i] for i in range(n) )

    # Build convex hull
    lines = []
    for j in range(1, n+1):
        m = j
        b = -prefix_sum[j]
        # Add to lines and maintain convex hull
        while len(lines) >=2:
            # Check if last two lines and new line are such that the second last can be removed
            line1 = lines[-2]
            line2 = lines[-1]
            # Compute intersection of line2 and new line
            x2 = (b - line2[1]) / (line2[0] - m)
            # Compute intersection of line1 and line2
            x1 = (line2[1] - line1[1]) / (line1[0] - line2[0])
            if x2 <= x1:
                lines.pop()
            else:
                break
        lines.append( (m, b) )

    max_delta = 0

    # Precompute the list of lines for binary search
    lines_list = lines

    for i in range(n):
        x = a[i]
        # Find the best line in lines_list for this x
        # Binary search on the lines_list
        left = 0
        right = len(lines_list) -1
        while left < right:
            mid = (left + right) //2
            if mid +1 > len(lines_list)-1:
                break
            # Compute intersection between lines[mid] and lines[mid+1]
            line_mid = lines_list[mid]
            line_next = lines_list[mid+1]
            intersect = (line_next[1] - line_mid[1]) / (line_mid[0] - line_next[0])
            if x <= intersect:
                right = mid
            else:
                left = mid +1
        best_line = lines_list[left]
        value = best_line[0] * x + best_line[1]
        current_term = prefix_sum[i+1] - a[i] * (i+1)
        delta = value + current_term
        if delta > max_delta:
            max_delta = delta

    print(original_sum + max_delta, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 1 2 7 1
""",
            "output": \
"""\
49
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

Sample Input 1:

4

4 3 2 5

prefix_sum is [0,4,7,9,14]

lines are built for j=1 to4.

j=1: line (1, -4). lines becomes [ (1,-4) ]

j=2: line (2,-7). Check if the previous two lines (only one exists). Add to lines. Now lines is [ (1,-4), (2,-7) ]

Check if last two lines can be popped.

For j=2:

lines[-2] is (1,-4), lines[-1] is (2,-7). new line is (2,-7).

But the loop for checking is not triggered since lines is now len 2.

Then, j=3: line (3,-9).

Check if lines has at least two.

Compute the intersection between lines[-2] (1,-4) and lines[-1] (2,-7):

x1 = (-7 - (-4)) / (1-2) = (-3)/ (-1) =3.

Then, new line (3,-9). intersection between lines[-1] and new line is x2 = (-9 - (-7)) / (2-3) = (-2)/(-1)=2.

x2=2 <=x1=3, so lines[-1] is popped. Now lines is [ (1,-4), (3,-9) ].

Check again: len(lines) is now 2. j=3.

Then add line (3,-9).

j=4: line (4,-14).

Check lines[-2] and lines[-1] (1,-4) and (3,-9).

x1 is intersection between them: ( -9 - (-4) ) / (1-3) = (-5)/-2 = 2.5.

new line (4,-14).

intersection with lines[-1] (3,-9) is ( -14 - (-9) )/(3-4) = (-5)/-1 =5.

x2=5 >x1=2.5. So no pop. Add to lines. lines becomes [ (1,-4), (3,-9), (4,-14) ].

Now, for a_i=4 (i=0):

x=4.

Binary search in lines_list.

lines_list is [ (1,-4), (3,-9), (4,-14) ]

left=0, right=2.

mid=1.

line_next is lines_list[2].

intersect between lines[1] (3,-9) and lines[2] (4,-14) is ( -14 - (-9) )/(3-4) = (-5)/-1 =5.

x=4 <=5? Yes. So right=1.

Now left=0, right=1.

mid=0.

Check lines[0] and lines[1]. intersect is ( -9 - (-4) )/(1-3) = (-5)/-2=2.5.

x=4 <=2.5? No. So left=1.

Now left=1, right=1. Loop ends.

best_line is lines_list[1] (3,-9).

value=3*4 + (-9) =12-9=3.

current_term is prefix_sum[0+1] -4*(0+1) =4-4=0.

delta=3+0=3.

max_delta is 3.

For other elements:

i=1 (a=3):

x=3.

binary search in lines_list.

Compute intersections between lines:

lines[0] and lines[1] at 2.5.

lines[1] and lines[2] at5.

x=3.

Check mid=1.

intersect between lines[1] and lines[2] is5. x=3 <=5: yes. right=1.

Check left=0, right=1.

mid=0. lines[0] and lines[1] intersect at2.5. x=3>2.5, so left=1.

best line is lines[1]. value=3*3 -9=0. current_term= prefix_sum[2] -3*2 =7 -6=1. delta=0+1=1. So delta is1.

Not better than 3.

i=2, a=2.

x=2.

Binary search.

Check lines:

intersect between lines[0] and lines[1] is2.5.

x=2 <2.5: optimal line is lines[0].

value=1*2 -4= -2.

current_term=prefix_sum[3] -2*3 =9-6=3. delta=-2+3=1.

i=3, a=5.

x=5.

Binary search.

Check lines[2] intersect at5.

x=5 is >=5, so best line is lines[2].

value=4*5 -14=20-14=6.

current_term=prefix_sum[4] -5*4=14-20= -6. delta=6-6=0.

So max_delta is3.

Original sum36 +3=39, which matches the sample.

Thus, the code works for this case.

Another sample: input 3:

3

1 1 2

Original sum:1*1 +1*2 +2*3=1+2+6=9.

Sample output is9. Which implies that the best move is to do nothing (but since we must move once, the delta is0. So moving an element to the same position.

But according to the code:

For each element, compute delta.

For example, moving the third element (2) to position3 gives delta of0.

But let's see:

The code computes for each element:

For i=2 (a=2, original position3):

x=2.

The lines are built for j=1,2,3.

prefix_sum is [0,1,2,4].

lines:

j=1: (1, -1)

j=2: (2,-2)

Check intersection between (1,-1) and (2,-2) is ( (-2 - (-1)) )/(1-2) = (-1)/(-1)=1.

j=3: (3,-4). Check intersection between (2,-2) and (3,-4) is ( (-4 - (-2) )/(2-3) )= (-2)/(-1)=2.

Since 2>1, so lines becomes [ (1,-1), (3,-4) ].

For i=2, x=2.

Binary search:

lines_list is [ (1,-1), (3,-4) ]

left=0, right=1.

mid=0: check intersect between lines[0] and lines[1] is ( (-4 - (-1) )/(1-3) )= (-3)/-2=1.5.

x=2 >1.5 → left=1.

best_line is lines[1], value=3*2 + (-4)=6-4=2.

current_term =prefix_sum[3] -2*3=4-6= -2. delta=2-2=0.

So delta for this move is0.

Other elements:

i=0 (a=1):

x=1.

lines_list is [ (1,-1), (3,-4) ].

intersect between lines[0] and lines[1] is1.5.

x=1 <=1.5 → best line is lines[0]. value=1*1-1=0.

current_term=prefix_sum[1] -1*1=1-1=0 → delta=0+0=0.

i=1 (a=1):

x=1.

best line is lines[0]. value=1*1-1=0.

current_term=prefix_sum[2] -1*2=2-2=0 → delta=0.

So max_delta is0.

Thus, the new sum is9+0=9.

Which matches the sample.

Thus, the code works.

Therefore, the code should handle all cases correctly.
</think>

```python
import bisect

n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + a[i]

original_sum = sum((i+1)*a[i] for i in range(n))

# Build convex hull
lines = []
for j in range(1, n+1):
    m = j
    b = -prefix_sum[j]
    while len(lines) >= 2:
        line1 = lines[-2]
        line2 = lines[-1]
        x1 = (line2[1] - line1[1]) / (line1[0] - line2[0])
        x2 = (b - line2[1]) / (line2[0] - m)
        if x2 <= x1:
            lines.pop()
        else:
            break
    lines.append((m, b))

max_delta = float('-inf')
lines_list = lines  # For easier access

for i in range(n):
    x = a[i]
    left, right = 0, len(lines_list) - 1
    while left < right:
        mid = (left + right) // 2
        if mid + 1 > len(lines_list) - 1:
            break
        line_mid = lines_list[mid]
        line_next = lines_list[mid+1]
        intersect = (line_next[1] - line_mid[1]) / (line_mid[0] - line_next[0])
        if x <= intersect:
            right = mid
        else:
            left = mid + 1
    best_line = lines_list[left]
    value = best_line[0] * x + best_line[1]
    current_term = prefix_sum[i+1] - a[i] * (i+1)
    delta = value + current_term
    if delta > max_delta:
        max_delta = delta

print(original_sum + max_delta)
```
