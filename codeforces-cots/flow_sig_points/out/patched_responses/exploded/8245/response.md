<think>
Okay, let's tackle this problem. The task is to find the k-th lexicographically smallest substring of a given string. If there aren't enough substrings, we output "No such line.".

First, let's understand the problem. For example, in the first sample input "aa", the substrings are all possible substrings. But since there are duplicates, like two "a"s, they are considered as separate entries. So when we sort all these substrings lex order, the first is "a", second is "a", then "aa". So for k=2, the output is "a".

The main challenge here is handling large input sizes. The string can be up to 1e5 characters long, and k can be up to 1e5. If we naively generate all possible substrings, that's O(n^2) which for n=1e5 is 1e10 operations—way too slow. So we need a smarter approach.

Hmm. So the first thing to note is that generating all possible substrings explicitly is impossible for large n. So we need a way to find the k-th substring without enumerating all possibilities.

What's the total number of substrings? For a string of length n, it's n*(n+1)/2. So for n=1e5, that's about 5e9, which is way more than 1e5. So when k is 1e5, we can't just generate all substrings up to that point. So we need an efficient way to count how many substrings are lex smaller than a certain point, and use that to find the k-th substring.

Alternative approach: think of the problem as a trie of all substrings, and traverse the trie to find the k-th entry. But building a trie for all substrings of a 1e5-length string is impossible due to memory constraints. So that's not feasible.

Another idea: the lexicographical order of the substrings can be determined by their starting and ending positions. For example, the smallest possible substrings are the single characters, ordered by their position. Then the next possible substrings are longer ones, but ordered lex.

Wait, but the lex order depends on the actual characters. For instance, the substring starting at position i with length l may be lex smaller than another substring starting at j with length m, regardless of their lengths.

So how can we model the possible candidates for the k-th substring? Let's think in terms of binary search. For a given candidate substring, can we compute how many substrings are lex smaller than it? If we can, then perhaps we can binary search for the correct substring. But the problem is that the candidate space is too big, and we can't iterate through all possibilities.

Alternatively, perhaps we can model the problem as a priority queue where we generate the smallest possible substrings in order, up to k steps. But again, for k=1e5, even this might be feasible if each step can be processed in logarithmic time.

Wait, here's a possible approach inspired by the K-th smallest element in a sorted matrix. The idea is to use a heap to keep track of the next possible candidates. For the substrings, the lex order starts with the smallest possible first characters. So all substrings starting with 'a' will come before those starting with 'b', etc. So for each starting position, the substrings are ordered by increasing length. But because of the lex order, a substring starting with a smaller character but longer length may be larger than a substring starting with a larger character but shorter length. Wait, no. Because the lex order compares the first differing character. So a longer string can be lex smaller if the prefix is smaller. For example, "aa" is lex smaller than "aab", but "aab" is longer. So the order is not strictly based on length.

Hmm. So the priority queue approach may work. Let's think: initially, the smallest substrings are all the single characters. The smallest among them is the first character. Then, for each step, when you pick a substring, you can generate the next possible substring by extending it by one character (if possible). But this might not capture all possibilities. For example, when you take a substring of length l starting at position i, the next possible substring from that i could be of length l+1. However, there might be other substrings starting at earlier positions that are lex smaller.

Wait, here's an idea: each node in the priority queue represents a substring starting at a certain position i, and having a certain length. The initial priority queue contains all single-character substrings (each starting at i, length 1). Then, each time we extract the smallest one (the lex smallest), we can add the next possible substring starting at i with length increased by 1. This way, the priority queue always contains the next possible candidates. This is similar to the way we merge k sorted lists. 

Let's see. For example, in the first sample input "aa", the initial heap has two entries: the first 'a' (i=0, length 1) and the second 'a' (i=1, length 1). The lex order for these two is the same, but they are considered separate in the problem. So the first extraction is the first 'a', then we add the substring starting at 0, length 2 ("aa") to the heap. The next extraction is the second 'a' (i=1, length 1), then we add the substring starting at 1, length 2. But since the string is length 2, i=1, length 2 is not possible (only length 1). So the heap after the second extraction would have "aa" (i=0, length 2). Then the third extraction is "aa", which is the third in the list. 

But how does this process track the order correctly? Each time we extract the smallest substring (from the heap), and then add the next possible longer substring from the same starting position. Because the heap always contains the next possible candidates in order. For example, if the current extracted substring is s starting at i, length l, then the next possible substring from i is s + the next character (if there is one). Since the substrings starting at i are ordered lex as their lengths increase (assuming that each added character is >= the previous ones, which may not be the case). Wait, no. For example, if the string is "ab", the substrings starting at 0 are "a", "ab". "a" is lex smaller than "ab". But if the string is "acb", the substrings starting at 0 are "a", "ac", "acb". But the substring starting at 0, length 2 is "ac" which is lex smaller than any substring starting at 2 (like "c", "cb") but larger than "a" and "c". So the heap approach may not capture all possible candidates. Wait, but the heap approach would process all starting positions. Let's see.

In the initial step, the heap contains all single-character substrings. Each time you extract the smallest (lex) substring, you add the next longer substring from the same starting position. So, the order in which these are processed would be the lex order. Because the heap is a min-heap, so the next smallest candidate is always at the top.

This approach is known as the "K-way merge" using a heap to track the next elements from each possible list. Here, each starting position i can generate a list of substrings of increasing length. The lists are sorted lex, but they may not be merged in order unless the heap tracks the next possible elements. 

But wait, each list (substrings starting at i) is indeed ordered lex. Because for substrings starting at i, each longer substring is formed by appending a character. Since the original string is fixed, the substring starting at i of length l+1 is the substring of length l followed by the next character. So, the lex order of substrings starting at i is the same as their order of increasing length. Because the longer substrings start with the same prefix as the shorter ones. For example, "a" comes before "ab" because "a" is a prefix of "ab" and shorter. So the substrings starting at i form a sequence where each next element is lex larger than the previous.

Therefore, all possible substrings can be viewed as K sorted lists (K is the number of starting positions, which is n). The problem then reduces to finding the k-th element in the merged list of all these K sorted lists.

The standard approach for this is to use a priority queue (min-heap) that keeps track of the current head of each list, then extract the smallest, and push the next element from that list. However, since each list is already in order, each time you extract the head of a list, the next element in that list is the next possible candidate from that starting position.

But the problem here is that for n=1e5, there are 1e5 initial elements in the heap (each starting position's first substring). Then, for each of the k steps, we perform a heap extraction and potentially a heap insertion. But for k=1e5, this would be O(k log n) time. For k=1e5 and log n=20, this is 2e6 operations, which is acceptable.

Wait, but the initial heap size is n. So inserting all n elements into the heap takes O(n) time, but for n=1e5, and each insertion being O(log n), that's O(n log n) which is 1e5 * 20 = 2e6 operations. Then, for k steps, each with an extraction and insertion (if possible), each O(log n) time. So total time is O(n log n + k log n). For n=1e5 and k=1e5, that's 2e6 + 1e5 * 20 = 2e6 + 2e6 = 4e6 operations. Which is manageable within 2 seconds.

But wait, how do we compare the substrings in the heap? Each time we need to compare two substrings, which can be up to O(l) where l is the length of the substring. However, this is not feasible for large l. So we need a way to compare the substrings efficiently.

But in the heap approach, each element in the heap represents a substring starting at position i with a certain length. So the element can be stored as (current substring, i, current length). But comparing these substrings directly is O(length) each time, which could be O(1e5) for each comparison. That would make the heap operations O(1e5) per step, leading to O(k*1e5) time which is 1e10 operations—way too slow.

So this approach is not feasible. We need a way to compare the substrings in O(1) time.

Ah, here's the key insight: the substrings in the heap are extensions of previous ones. For a given i and l, the substring is s[i:i+l]. When comparing two substrings (i1, l1) and (i2, l2), we need to find the lex order between s[i1:i1+l1] and s[i2:i2+l2]. Comparing these two directly would take O(min(l1, l2)) time, which is too slow for large l1 and l2.

But how can we compare them efficiently?

An efficient way to compare two substrings of the original string is to use a suffix array with LCP (Longest Common Prefix) information. However, building a suffix array for a string of length 1e5 is manageable, but integrating that into the heap comparison is tricky.

Alternatively, we can precompute a data structure that allows comparing any two substrings in O(1) time. This is possible with a combination of suffix array and LCP array, along with a range minimum query (RMQ) structure.

But building such structures for the problem might be complex. Let's think if there's a smarter approach.

Wait, the heap approach requires that each time we extract the smallest substring. But when we extract a substring (i, l), the next substring to push into the heap is (i, l+1), provided that l+1 does not exceed the maximum possible length for i (i.e., i + l +1 <= len(s)). So the next substring is s[i:i+l+1]. When comparing (i, l+1) with other substrings in the heap, we need to know if it's the smallest possible next candidate.

But in the heap, each element is of the form (i, current_length). When comparing (i1, l1) and (i2, l2), we can compare their substrings as follows: find the minimum of l1 and l2, and compare the first differing character. If all characters up to min(l1, l2) are the same, then the shorter one is considered smaller.

But again, comparing the substrings directly for each heap comparison is O(l) time, which is too slow.

So this approach isn't feasible for large n and k. We need a different method.

Alternative idea: since all the substrings are considered, the lex order of the substrings is determined by their starting positions and their lengths. Wait, no. For example, a substring starting at i with length l could be lex larger than a substring starting at j with length m even if i < j. But the starting positions themselves don't determine the order. It depends on the actual characters.

Hmm. Let's think differently: for each possible substring, the order is determined by its characters. So the lex order is the same as the order in which the substrings appear when all possible substrings are generated and sorted lex.

But how do we efficiently find the k-th element in this list without enumerating all elements?

Another approach: the lex order is such that the first character determines the primary order. Then the second character for those with the same first character, and so on.

So the problem is similar to a trie traversal where each node represents a substring. The k-th element in the trie's pre-order traversal is the answer.

But building a trie for all substrings of a 1e5-length string is impossible due to memory constraints. So that's not feasible.

Alternatively, can we model the problem using the suffix array?

The suffix array sorts all the suffixes of the string lexicographically. But a suffix is a substring starting at a certain position and extending to the end. However, the substrings we need are all possible prefixes of all suffixes.

Wait, the suffixes sorted in the suffix array can help. For each suffix starting at i, the substrings that are prefixes of this suffix are all the possible substrings starting at i. So the lex order of all substrings can be thought of as the order of their starting positions in the suffix array, and their lengths.

But how does that help? Let's see.

The suffix array SA is an array where SA[0] is the starting index of the lex smallest suffix, SA[1] is the next, etc. For each SA[i], the suffixes are in lex order. The substrings can be considered as the prefixes of these suffixes. So the lex order of all substrings is the same as the order of their (starting index, length) pairs when sorted as follows:

For each starting index i (sorted according to the suffix array order), the substrings of varying lengths (from 1 to len(s) - i) are ordered by their length. Because the longer substrings are formed by appending characters to the shorter ones, and since the suffix starting at i is lex ordered, any prefix of it longer than a previous one will be lex larger than the previous one.

Wait, no. For example, if the suffix starting at i is 'ab', then the substrings are 'a' and 'ab'. 'a' is lex smaller than 'ab'. So the order of substrings starting at i is indeed from length 1 upwards.

So, the lex order of all substrings can be represented as follows:

First, all substrings from the lex smallest suffix, starting at their i, in order of increasing length. Then the next suffix, and so on.

Wait, but this isn't exactly correct. Because a substring from a certain starting index i might be lex smaller than a substring from another starting index j, even if the suffix starting at j is lex smaller than the suffix starting at i. For example, consider s = "ab", "a" (starting at 0, length 1) is lex smaller than "ab" (starting at 0, length 2). But if there's another starting index 1, "b", which is part of the suffix starting at 1. The suffix starting at 0 is "ab", which is lex smaller than the suffix starting at 1 ("b"). So the substrings in order are 'a', 'ab', 'b'. So the order is according to the suffix array. But in this case, the first suffix is 0. The substrings from 0 are 'a', 'ab'. Then the next suffix is 1, with substring 'b'.

But what about a situation where a substring from a later suffix is lex smaller than a longer substring from an earlier suffix. For example, s = "aab". The suffix starting at 0 is "aab", suffix starting at 1 is "ab", suffix starting at 2 is "b". The suffix array order is 0, 1, 2. The substrings would be 'a' (from 0), 'aa' (0, len 2), 'aab' (0, len 3), 'a' (from 1), 'ab' (1, len 2), 'b' (2, len 1). But lex order of all substrings is:

a (0), a (1), aa (0), aab (0), ab (1), b (2). So the order is not strictly based on the suffix array. Because the second 'a' (from position 1) comes after the first 'a' (position 0) in the suffix array, but the 'a' from position 1 is considered as a separate substring and comes after the 'a' from position 0. So the suffix array approach might not directly give the order of all substrings.

Hmm, this complicates things. So perhaps the suffix array approach is not directly applicable.

Alternative approach: consider all possible substrings as (i, l), where i is the starting index and l is the length. The lex order between (i1, l1) and (i2, l2) is determined by comparing the characters of the substrings.

To find the k-th smallest substring, perhaps we can model the problem as a binary search. For a given candidate substring, count how many substrings are lex smaller than it, and adjust the candidate based on that count. However, the problem is that the candidate space is infinite (all possible (i, l) pairs) and we need a way to enumerate possible candidates efficiently.

Another angle: the minimal possible substrings are those of length 1, then length 2, etc. But in lex order, a longer substring can be smaller than a shorter one if it starts with a smaller character. For example, "a" is the smallest, then "aa", "aaa", etc., then "ab", etc. So the problem is to find the k-th element in the sorted list of all possible (i, l) pairs, ordered lex.

But again, how to do this efficiently.

Wait, here's another idea inspired by the fact that the number of possible substrings is up to 1e5*(1e5+1)/2, which could be 5e9. But the k is up to 1e5. So if the k is small, say up to 1e5, then perhaps we can generate the first k smallest substrings efficiently, even for a large n.

But how? For example, the first k substrings are likely to be of small lengths, since shorter substrings are lex smaller (if starting with the same character). So perhaps we can find all possible substrings of lengths up to some maximum l, where l is determined by k.

But even this is not straightforward. For example, the first k substrings could include longer substrings if they are lex smaller than others. For example, in the string "ab", the order is 'a', 'ab', 'b'. So for k=2, the substring is 'ab', which is longer than 'a'.

But the key insight here is that the earliest substrings in lex order are the ones that start with the smallest possible characters, and for each such starting position, the minimal possible length. So perhaps we can model this with a priority queue where each entry represents the earliest possible substring starting at a certain position.

Wait, this brings us back to the initial heap approach. But the problem is the comparison of substrings during heap operations.

So the crux of the problem is how to compare two substrings (i, l) and (j, m) efficiently.

If we can compare them in O(1) time, then the heap approach becomes feasible.

How to compare two substrings (i, l) and (j, m) in O(1) time?

We can use a suffix automaton or a suffix array with LCP information. Let's think about the suffix array.

The suffix array SA is an array where SA[k] is the starting index of the suffix that is the k-th smallest in lex order. Then, for two suffixes starting at i and j, SA tells us their order. But comparing two substrings (i, l) and (j, m) is equivalent to comparing their prefixes up to the minimum of l and m.

If we can find the length of their longest common prefix (LCP), then we can determine the order based on the next character after the LCP.

So, for example, if the LCP is h, and h is equal to the minimum of l and m, then the shorter substring is lex smaller. Otherwise, compare the (h+1)th character.

So, if we precompute the suffix array and the LCP array, we can build a data structure that allows us to compare any two substrings in O(1) time.

But building a suffix array and LCP array for a 1e5-length string is manageable. The SA can be built in O(n) time using the SA-IS algorithm, and the LCP array can be built in O(n) time as well.

Once we have the SA and LCP array, we can use a sparse table or another RMQ structure to answer LCP queries between any two suffixes in O(1) time.

So, here's the plan:

1. Precompute the suffix array (SA) and the LCP array for the given string.
2. Preprocess an RMQ structure to answer the LCP between any two suffixes.
3. Use a priority queue (min-heap) that stores tuples representing the substring (i, length), and uses the suffix array and LCP information to compare the substrings efficiently.
4. For each step, extract the smallest substring from the heap, and if possible, add the next substring from the same starting position (i, length +1) to the heap. Repeat this k times to find the k-th substring.

But how to represent the comparison function in the heap. In Python, the heap is a priority queue that uses the __lt__ operator of the elements. So we need to create a data structure that represents a substring (i, l) and can be compared with another such structure using the suffix array and LCP information.

But in Python, this is challenging because the heap elements are tuples, and the comparison is based on the tuple's elements. So perhaps we can represent each heap element as a tuple that encodes the order according to the suffix array and LCP.

Wait, but for the heap to work, the elements must be ordered such that the heap's invariants are maintained. So the comparison between two elements (i1, l1) and (i2, l2) must be done based on their lex order.

Let's think: each heap element will be a substring starting at i with length l. To compare two such elements, we need to compare s[i:i+l] and s[j:j+m], where j is another starting index and m is the length.

The steps to compare them:

1. Find the length of the longest common prefix (LCP) between s[i:] and s[j:]. Let this be h.
2. The LCP between the two substrings is min(h, l, m). Let h_sub = min(h, l, m).
3. If the first h_sub characters are equal, then the substring with smaller length is lex smaller. If the lengths are equal, then the substrings are equal.
4. If they differ at position h_sub, then compare the characters at i + h_sub and j + h_sub. The one with the smaller character is lex smaller.

So the comparison between (i, l) and (j, m) can be done by:

a. Find the LCP h of the suffixes s[i:] and s[j:].
b. The LCP of the substrings is h_sub = min(h, l, m).
c. If h_sub >= l and h_sub >= m: then the substrings are equal (since they are of lengths l and m, and their common prefix is up to min(l, m)), but if l != m, the shorter one is lex smaller.
d. Else, compare s[i + h_sub] and s[j + h_sub].

So, to perform this comparison efficiently, we need to compute h = LCP(s[i:], s[j:]) quickly. This can be done using an RMQ structure on the LCP array. However, the LCP array in the suffix array is the LCP between consecutive suffixes in the SA. So to compute the LCP between any two suffixes, say SA[x] and SA[y], we need to find the minimum LCP in the range x+1 to y (assuming x < y). This can be done with a range minimum query (RMQ) structure built over the LCP array.

Once we have that, the LCP between any two suffixes starting at i and j can be found by finding their positions in the suffix array (rank[i] and rank[j]), and then finding the minimum in the LCP array between the ranks.

But this is getting a bit involved. Let's outline the steps:

1. Compute the suffix array SA for the string s. SA is sorted lex order of suffixes.
2. Compute the rank array, which for each suffix starting at i, gives its position in the SA.
3. Compute the LCP array, which contains the longest common prefix between consecutive suffixes in the SA.
4. Build an RMQ structure (like a sparse table) on the LCP array to answer range minimum queries in O(1) time.
5. For comparing two substrings (i, l) and (j, m):
   a. Compare the two suffixes s[i:] and s[j:] using their rank. If one is lex smaller than the other, then the substring starting at that suffix is lex smaller. But this is not sufficient because the substrings are of length l and m. For example, s[i:] could be "abcd", s[j:] could be "abcf". The suffix s[i:] is lex smaller. But if l=3 and m=3, then the substrings are "abc" and "abcf" (but m=3 would be "abx" if j is different). Wait, no. The substrings are s[i:i+l] and s[j:j+m]. So even if the suffixes are s[i:] and s[j:], the substrings may have different lengths. So comparing the suffixes is not sufficient.

Wait, the lex order of the substrings (i, l) and (j, m) is determined by the first min(l, m) characters of the suffixes s[i:] and s[j:]. So the order between the two substrings is the same as the order of the first min(l, m) characters of the suffixes s[i:] and s[j:].

So, to compare (i, l) and (j, m), we can do:

Compare the two substrings s[i:i+min(l, m)] and s[j:j+min(l, m)]. If they are different, the order is determined by the first differing character. If they are equal up to min(l, m), then the shorter substring is lex smaller.

But how to compare the first min(l, m) characters of the two suffixes?

This is where the LCP comes into play. The LCP between s[i:] and s[j:] is the length of the longest common prefix between the two suffixes. Let h be this LCP.

If h >= min(l, m), then the two substrings are equal up to min(l, m) characters. So the shorter substring is lex smaller. For example, if l=3 and m=5, and the first 3 characters are the same, then the substring of length 3 is lex smaller.

If h < min(l, m), then the first differing character is at position h. So compare s[i + h] and s[j + h]. If s[i +h] < s[j +h], then (i, l) is lex smaller.

Thus, the steps to compare (i, l) and (j, m) are:

1. Compute h = LCP(s[i:], s[j:]) 
2. Let min_len = min(l, m)
3. If h >= min_len:
   a. The substrings are equal up to min_len characters. Compare their lengths: if l < m → (i,l) is smaller. Else → (j, m) is smaller (if l > m) or they are equal (if l == m).
4. Else:
   a. Compare s[i +h] and s[j +h]. If s[i +h] < s[j +h], then (i,l) is smaller. Else, (j,m) is smaller.

But how to compute h = LCP(s[i:], s[j:])?

This is where the suffix array and LCP array come in. The LCP between two suffixes s[i:] and s[j:] can be found using the rank array and the LCP array.

The steps to compute the LCP between s[i:] and s[j:] are:

1. Find the ranks of i and j in the suffix array. Let r_i = rank[i], r_j = rank[j].
2. Assume r_i < r_j. The LCP between s[i:] and s[j:] is the minimum value in the LCP array from index r_i +1 to r_j. This can be found using the RMQ structure.
3. If r_i > r_j, swap them and proceed.

Once we have the LCP between s[i:] and s[j:], we can proceed as per the comparison steps above.

So the key is to precompute the rank array and the LCP array with RMQ.

Now, the plan is:

- Precompute SA, rank, LCP array, and RMQ for LCP.
- Use a priority queue that stores (i, current length) entries. The priority is determined by comparing the substrings as described.
- However, comparing two entries (i, l) and (j, m) requires up to three steps: find the LCP of the suffixes, compare the characters after that, etc.

But how to implement this in Python's heap, which compares elements based on their __lt__ method.

The problem is that in Python, when you push elements into the heap, they are compared using their natural ordering. So if we can represent each heap element as a key that can be compared efficiently using the above method, then the heap will work.

But generating such a key is challenging. One possible approach is to create a wrapper class for the heap elements, overriding the __lt__ method to perform the comparison as per the LCP-based approach.

However, in Python, the comparison between objects can be done by overloading __lt__, but for this to be efficient, the __lt__ method must be able to compute the comparison quickly.

So here's the plan for the code:

1. Precompute the SA, rank, LCP array, and build an RMQ structure for the LCP array.

2. Create a class HeapElement that represents a substring (i, length). The __lt__ method of this class compares two HeapElement instances using the LCP-based method outlined above.

3. Use a priority queue (heapq) that stores instances of HeapElement. Each time an element is popped, the next possible element (i, length +1) is pushed into the heap, provided that length +1 does not exceed the maximum possible length for i (i.e., i + length +1 <= len(s)).

This approach will allow the heap to process the elements in the correct lex order.

But wait, how efficient is this?

For each comparison in the heap, the __lt__ method will need to compute the LCP between two suffixes, which involves two rank lookups and a range minimum query. The range minimum query is O(1) with a sparse table. The ranks are stored in an array, so lookups are O(1).

The character comparisons are O(1) because we can directly access the character in the string given the index.

Thus, each __lt__ comparison is O(1) time.

But in the worst case, each heap operation (push or pop) could involve multiple comparisons, each with O(1) time. For example, when inserting an element into the heap, the number of comparisons is O(log h), where h is the current size of the heap.

But given that each comparison is O(1), the time per heap operation would be O(log h) * O(1) = O(log h), which is acceptable.

So, for k steps, each with a heap extraction and insertion, and each step taking O(log n) time (since the heap size is O(n)), the total time would be O(k log n + n log n) for the initial heap construction, which should be manageable for n=1e5 and k=1e5.

But building the suffix array, LCP array, and RMQ structure is also time-consuming. Let's see:

- SA construction for 1e5 can be done with O(n) algorithms like SA-IS, but in Python, implementing SA-IS may be challenging. Alternatively, we can use a library or a slower algorithm. However, for Python, even O(n log n) algorithms may be feasible for 1e5.

But given the time constraints, perhaps the best way is to find an efficient implementation of the suffix array and LCP array.

Alternatively, perhaps there's a different approach.

Another observation: since all substrings are considered, including duplicates, and we need to count each occurrence, the order is determined by the lex order of the substrings, but each occurrence is considered separately.

But considering the problem constraints, perhaps the heap approach is manageable if we can implement the comparisons efficiently.

So, let's outline the code steps:

1. Read the input string s and k.

2. Compute the total number of substrings. If the total is less than k, output "No such line."

   The total is n*(n+1)/2, where n is the length of s. Compute this and check if it's >=k.

3. Precompute SA, rank, LCP array, and build RMQ structure for LCP.

4. Define the HeapElement class with __lt__ method.

5. Initialize a priority queue with all possible (i, 1) elements.

6. For each of the first k-1 steps, extract the smallest element, and push (i, length+1) if possible.

7. The k-th extracted element is the answer.

But steps 3 and 4 are the key.

Now, the problem is to compute the suffix array and LCP array efficiently in Python.

But implementing a suffix array and LCP array for 1e5-length strings in Python is challenging. For example, the standard O(n log n) suffix array construction (like using doubling algorithm) may be feasible.

Alternatively, using the built-in sorted function with the first few characters, but that would be O(n^2 log n) which is not feasible.

So, we need an efficient implementation of the suffix array.

Alternatively, for this problem, perhaps a different approach can be taken.

Wait, the problem requires the k-th lex substring, and k is up to 1e5. So perhaps the first k substrings are relatively short. For example, the first k substrings may have a maximum length of around O(k), but that's not necessarily true.

But for the given examples, in the second sample input, k=5 leads to a substring of length 2. But if the string starts with 'a's, then the first k substrings may include many long 'a's.

Hmm. So the heap approach may still be the way to go.

But in Python, implementing the suffix array and LCP array with RMQ is time-consuming. Maybe there's a smarter way.

Alternative idea: when comparing two substrings (i, l) and (j, m), compare them character by character until the first differing character, but use memoization to avoid comparing the same pairs multiple times. However, this could be O(1) per comparison on average if the first differing character is found quickly. But worst-case, it's O(l) per comparison.

But for k=1e5 and n=1e5, this would be O(k * l) = 1e10 operations, which is way too slow.

So this approach is not feasible.

Alternative idea: use a binary search on the possible candidates. But how?

Let's think: the lex order is determined by the first character. For each possible starting character, count the number of substrings that start with that character and are lex smaller than the current candidate. But again, it's unclear how to model this.

Alternatively, for each possible starting position i, and for each possible length l, we can count how many substrings are lex smaller than the substring s[i:i+l]. But again, this seems intractable.

Hmm. So perhaps the heap approach with efficient comparison is the only feasible way.

So, back to the original plan: implement the SA, LCP, and RMQ.

Let's outline the steps for that.

Suffix Array Construction:

Implement an efficient suffix array construction algorithm. For example, the doubling algorithm, which is O(n log n) time. But in Python, even O(n log^2 n) may be feasible for n=1e5.

The doubling algorithm works as follows:

Sort the suffixes by their first 1 characters, then 2, 4, 8, etc., up to 2^k characters. For each step, sort the suffixes using the previous ranks.

For each iteration:

1. For each suffix i, compute a pair (rank[i], rank[i + 2^{k-1}]) if i + 2^{k-1} < n, else (rank[i], -1).

2. Sort the suffixes based on these pairs.

3. Update the ranks for the next iteration.

The algorithm stops when 2^k > n.

Implementing this in Python for n=1e5 may be feasible, but requires careful coding.

Once the SA is built, the rank array is the inverse of the SA: rank[i] is the position of the suffix starting at i in the SA.

LCP Array Construction:

The LCP array can be built using Kasai's algorithm, which runs in O(n) time. The algorithm uses the fact that LCP[rank[i]] >= LCP[rank[i-1]] -1.

Once the LCP array is built, we can build a sparse table for range minimum queries.

Sparse Table Construction:

The sparse table is built for the LCP array. For each position i, and each j from 0 to log2(n), store the minimum value in the interval starting at i of length 2^j. Then, for any query l to r, the minimum can be found by comparing the minimum of the two overlapping intervals of length 2^k that cover the range l to r.

Building the sparse table is O(n log n), and queries are O(1).

Once all this is in place, comparing two substrings (i, l) and (j, m) can be done as follows:

Compute h = LCP(s[i:], s[j:]) using the sparse table on the LCP array.

Then compare the substrings as per the earlier steps.

Now, let's proceed to code.

But first, the code for the suffix array, LCP array, and sparse table.

But implementing this in Python for a 1e5-length string may be challenging. Let's think of possible optimizations.

First, the suffix array construction.

Here's an implementation of the doubling algorithm in Python:

def build_sa(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1
    while k <= n:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp = [0] * n
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i-1]]
            if (rank[sa[i]] != rank[sa[i-1]] or 
                (rank[sa[i] + k] if sa[i]+k <n else -1) != (rank[sa[i-1]+k] if sa[i-1]+k <n else -1)):
                tmp[sa[i]] += 1
        rank = tmp
        k *= 2
    return sa

But this is O(n log^2 n) time, which for n=1e5 is 1e5 * (20)^2 = 4e6 operations. That's manageable.

But in Python, the sort function is efficient, but for n=1e5, each sort would take O(n log n) time. Each iteration of k doubles the value of k. For n=1e5, the loop would run log2(n) times, which is about 17. So the total time is 17 * O(n log n) = 17 * 1e5 * 20 = 3.4e7 operations. Which is acceptable.

But for n=1e5, this might take a few seconds, but given the time limit of 2 seconds per test case, this could be tight.

Alternatively, there are faster implementations, but for the purpose of this problem, let's proceed with this.

Then, the LCP array can be built with Kasai's algorithm:

def build_lcp(s, sa, rank):
    n = len(s)
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

This is O(n) time.

Once the LCP array is built, the sparse table is constructed. Here's the code for building a sparse table for RMQ:

class SparseTable:
    def __init__(self, data):
        self.n = len(data)
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i//2] + 1
        self.size = self.log_table[self.n] + 1
        self.table = [[0] * self.n for _ in range(self.size)]
        self.table[0] = data
        for j in range(1, self.size):
            for i in range(self.n - (1 << j) + 1):
                self.table[j][i] = min(self.table[j-1][i], self.table[j-1][i + (1 << (j-1))])
    
    def query_min(self, l, r):
        length = r - l + 1
        k = self.log_table[length]
        return min(self.table[k][l], self.table[k][r - (1 << k) + 1])

But building the sparse table for the LCP array of length 1e5 would require O(n log n) space and time. For 1e5 * 20 = 2e6 entries, this is manageable.

Now, putting it all together.

The HeapElement class needs to compare two instances based on their i, l and j, m using the suffix array, LCP, and sparse table.

But in Python, the heapq module requires that the elements can be compared using the default comparison operators. So we need to create a class that defines __lt__.

So the HeapElement class will have:

class HeapElement:
    def __init__(self, i, length, s, sa, rank, lcp_st):
        self.i = i
        self.length = length
        self.s = s
        self.sa = sa
        self.rank = rank
        self.lcp_st = lcp_st

    def __lt__(self, other):
        # Compare self's substring (i, length) with other's (j, m)
        i = self.i
        l = self.length
        j = other.i
        m = other.length

        # Compare the substrings s[i:i+l] and s[j:j+m]
        # Step 1: Compute LCP between s[i:] and s[j:]
        r_i = self.rank[i]
        r_j = other.rank[j]
        if r_i > r_j:
            return not (other < self)
        # Now r_i <= r_j
        # Compute LCP between i and j's suffixes
        if r_j == r_i:
            h = len(self.s) - i
        else:
            # LCP is the min in LCP[r_i+1 ... r_j]
            h = self.lcp_st.query_min(r_i + 1, r_j)
        # Now h is the LCP of the suffixes starting at i and j
        min_len = min(l, m)
        if h >= min_len:
            # The substrings are equal up to min_len, compare lengths
            return l < m if l != m else False  # If equal, False (but for heapq, need to return correct)
        else:
            # Compare the first differing character at i + h and j + h
            c_i = self.s[i + h]
            c_j = other.s[j + h]
            return c_i < c_j

Wait, but how do we access the sa, rank, lcp_st in the HeapElement?

The HeapElement would need to have references to the suffix array, rank array, and the sparse table. But since the suffix array and rank are precomputed and static, we can pass them to the HeapElement during construction.

But in Python, creating a class instance with these references for each heap element may be memory-intensive for 1e5 elements. But perhaps manageable.

But in practice, each HeapElement instance will carry references to the same sa, rank, lcp_st, so the memory cost is minimal.

But the problem is that when we push an element into the heap, the __lt__ method must compare two HeapElement instances, each of which has references to the same sa, rank, and lcp_st.

Yes.

Now, the steps:

1. Read s and k.

2. Compute n = len(s). Compute total_substrings = n*(n+1)//2. If k > total_substrings, output "No such line."

3. Build the suffix array (sa), rank array (rank), LCP array (lcp), and build the sparse table (lcp_st) for RMQ.

4. Create the initial heap elements: for each i in 0..n-1, add (i, 1) as a HeapElement.

5. Use a heap to extract the k-th element.

But in Python, the heapq module is a min-heap. So each time we extract the smallest element.

Now, the code outline:

s = input().strip()
k = int(input())

n = len(s)
total = n * (n + 1) // 2
if k > total:
    print("No such line.")
    exit()

# Build SA, rank, LCP, and sparse table
sa = build_sa(s)
rank = [0]*n
for i in range(n):
    rank[sa[i]] = i
lcp = build_lcp(s, sa, rank)
lcp_st = SparseTable(lcp)

# Initialize the heap
import heapq

heap = []
for i in range(n):
    # Only add substrings that exist (i+1 <=n)
    if i < n:
        element = HeapElement(i, 1, s, sa, rank, lcp_st)
        heapq.heappush(heap, element)

# Extract the first k elements
result = None
for _ in range(k):
    current = heapq.heappop(heap)
    result = current.s[current.i : current.i + current.length]
    # Push next substring if possible
    next_length = current.length + 1
    if current.i + next_length <= n:
        next_element = HeapElement(current.i, next_length, s, sa, rank, lcp_st)
        heapq.heappush(heap, next_element)

print(result)

But wait, this code will push the next substring for the current i (current.length +1) each time. But how do we handle the case where the next_length exceeds the string's length?

The condition current.i + next_length <= n is checked.

Yes.

But this code has a few issues:

1. The HeapElement's __lt__ method needs to correctly compare two elements. For example, when the two elements are from different i's, their ranks are compared, then their LCP is computed, etc.

But what if i + l exceeds the string length? For example, if i=5 and length=10, but the string is only 6 characters long. The code should not create such elements, which is handled by the condition in the push step.

Another potential issue is the comparison when one of the substrings extends beyond the string. But in the code, the HeapElement's length is always such that i + length <= n, since when pushing, we check if current.i + next_length <=n.

So the comparison between two elements is valid.

Another issue is that the HeapElement's __lt__ method may have incorrect logic. For example, when comparing two elements where the LCP is >= min(l, m), but l == m, then the two substrings are equal, so their order depends on the starting index. But according to the problem statement, the substrings are considered as separate entries if they are different in the original string. But the problem requires that even if two substrings are identical (same characters), but different starting or ending positions, they are considered separate.

But according to the problem statement, the equal substrings are considered separate entries. For example, "aab" has two "a" substrings from positions 0 and 1.

But in the __lt__ method, if two substrings are identical in characters, their order is determined by the starting position, but the problem statement's ordering does not specify how to order identical substrings. Wait, no. The problem says to sort all substrings in lex order. For two identical substrings (same characters), they are considered equal, but their order in the list depends on their occurrence in the original string.

Wait, no. The problem statement says to write out all substrings, including equal ones, and sort them lex order. So when two substrings are lex equal, they are considered equal and their order in the sorted list is not determined by their positions. For example, in the first sample input "aa", the substrings are "a" (i=0), "a" (i=1), "aa". When sorted lex order, the two "a"s are considered equal and their order in the list is determined by the way they are generated. But according to the sample input, the first "a" comes before the second "a" because the first is generated first in the initial list. But when sorted lex order, the two "a"s are equal, but the problem requires that they are considered as separate entries. So their order in the sorted list is not determined by their position; they are considered equal and thus their order is arbitrary. However, the problem's examples suggest that when two substrings are lex equal, their order in the output list is determined by their position in the original string. For example, in the first sample input, the two "a" substrings are generated in order (i=0 first, then i=1), and the output is the second one when k=2.

But this suggests that when two substrings are lex equal, their order in the sorted list is determined by their starting index. Or perhaps not?

This is a critical point.

According to the problem statement, the list is sorted in lex order. If two substrings are lex equal, how are they ordered?

In the first sample input, the two "a" substrings (i=0 and i=1) are considered equal in lex order, but they are both present in the list. When sorted, they are both first, but the order between them is not specified. However, the sample input's output for k=2 is "a", which suggests that the two "a"s are ordered as per their occurrence in the original list. But according to the problem statement, when two strings are equal, their order in the list is the same as their occurrence in the original string.

But how does the lex order define their order when the substrings are equal? The problem's definition of lex order does not specify this. For example, the lex order between two equal strings is not defined, as they are equal. Thus, when two substrings are equal, their relative order in the list could be arbitrary. However, the problem's sample input shows that for the first case, the two "a"s are considered as two separate entries in the list, and the second one is chosen when k=2.

This implies that the order between equal substrings is determined by their position in the original string. For example, the first occurrence comes before the second occurrence in the sorted list. But according to the lex order, these two are equal, so their order is not determined by the lex order. So the problem's examples suggest that the order between equal substrings is determined by their starting position and length.

But according to the problem statement, the substrings are sorted lex, and if two are equal, they are considered equal. But the problem requires to output the k-th entry in the list, which includes all possible substrings, including duplicates. So the order between equal substrings must be determined in some way.

But the problem statement does not specify how to order equal substrings. However, the sample inputs indicate that the order between two equal substrings is determined by their starting index and/or their length.

For example, in the first sample input:

substrings are:

i=0, length 1: "a"

i=1, length 1: "a"

i=0, length 2: "aa"

When sorted lex, the two "a"s are considered equal and thus can appear in any order. But the sample shows that the first "a" (i=0) is the first entry, and the second "a" (i=1) is the second entry. Thus, their order in the list is determined by their starting positions. So when two substrings are lex equal, their order in the list is determined by the order in which they are generated. But according to the problem statement, the list is sorted lex. But how can lex order determine the order of two equal substrings? It can't. So the problem must have an implicit rule that when two substrings are equal, the one that starts earlier in the original string comes first. Or perhaps the one with a smaller starting index, and if they start at the same index, the shorter comes first.

But according to the problem statement, when two substrings are equal, their order in the sorted list is not specified, but the sample indicates that the order is determined by their starting index. For example, the first sample input's two "a"s are in order i=0, then i=1. Thus, the code must enforce this order.

But in the current heap approach, the order of two equal substrings is determined by their starting index and length. For example, when two substrings are equal, the heap compares their starting index and length. But according to the __lt__ method in the HeapElement class, if the two substrings are equal, then the one with smaller length comes first, but if the lengths are the same, the comparison returns False (which is equivalent to considering them equal, but Python's heapq would then compare other fields of the object, but HeapElement doesn't have any other fields to compare.

This is a problem. Because when two substrings are equal (same characters), but different starting positions and/or lengths, the heap comparison must order them in a way that reflects their order in the list.

But according to the problem statement, all substrings are considered, including equal ones. So the order between two lex equal substrings must be determined by their position in the original list of all possible substrings. However, the problem doesn't specify this order.

But the sample input shows that for the two "a" substrings in the first sample, the one starting at i=0 is first, then i=1. So the code must generate the list of all possible substrings sorted lex, and when two are equal, they are ordered according to their starting index, then their length.

But how to model this in the comparison function.

In the current __lt__ method, when two substrings are equal, the code returns l < m. But if l == m, then the code returns False, which means that in the heap, the elements are considered equal. But in Python, when two elements are considered equal, the heapq module may compare other attributes, like the starting index, which may not be considered in the __lt__ method.

This is a critical issue.

For example, when two HeapElements are considered equal (their substrings are lex equal), then the __lt__ method returns False for both a < b and b < a. This leads to the elements being considered equal, and the heapq module will then compare other attributes of the HeapElement instances. But HeapElement instances have other attributes like i and length, which are not considered in the __lt__ method. So the default comparison in Python for objects without a defined __lt__ is based on their memory addresses, which is undefined.

Thus, the current code does not properly order equal substrings, which could lead to incorrect ordering in the heap and thus incorrect results.

So, to fix this, the comparison function must explicitly define the order between equal substrings. That is, when two substrings are equal lex, their order is determined by their starting index. If starting indices are the same, then by their length. But since a starting index and length uniquely define a substring (i and l), and each HeapElement is for a different substring, it's possible that two different HeapElements have the same substring, but different i and l. For example, s = "abxab", and two substrings starting at i=0, l=2 ("ab") and i=3, l=2 ("ab"). These are lex equal and must be ordered in the list. According to the problem's examples, the order between them is determined by their starting indices and length. But how?

In the problem's first sample, the two "a" substrings are ordered by their starting indices. So the one with the smaller starting index comes first.

Thus, the comparison function must be modified to order equal lex substrings by their starting index. If the starting indices are the same, then by length (but since i and l uniquely define a substring, this is not possible. So, when two substrings are lex equal, the one with the smaller starting index comes first. If starting indices are the same, then the one with shorter length comes first.

Wait, no. If two substrings start at the same index, they cannot be of the same lex order unless their lengths are the same. So, two different substrings starting at the same index must have different lengths, and thus cannot be lex equal.

So, the order between lex equal substrings must be determined by their starting index, and then their length.

Thus, in the __lt__ method, when two substrings are lex equal, we compare their starting indices. If the starting indices are the same, compare their lengths. This way, the order between equal lex substrings is determined by their starting index and length.

So, modifying the __lt__ method:

In the case where h >= min_len and l == m:

We compare the starting indices. The substring with the smaller starting index is considered smaller. If the starting indices are the same, then the substrings are the same (same i and l), but this can't happen since the HeapElements are unique in the heap.

Wait, but in the heap, there can be multiple elements with the same i and l. For example, when pushing (i, l) multiple times, but that's impossible because each element is pushed once for each i and l. So, each HeapElement is unique.

But when two different HeapElements are lex equal but have different starting indices or lengths, we need to order them.

Thus, in the __lt__ method:

After determining that the two substrings are lex equal (h >= min_len and l == m), we compare the starting indices. If the starting indices are the same, then compare the lengths (but this can't happen). Otherwise, the one with the smaller starting index is considered smaller.

Thus, modifying the __lt__ method:

In the step where h >= min_len:

if l == m:
    # compare starting indices
    return self.i < other.i
else:
    return l < m

But wait, the lex order of the substrings is already determined, but for two lex equal substrings, the problem requires that their order is determined by their starting index and length.

Wait, no. According to the problem statement, the substrings are sorted in lex order. So, two substrings that are lex equal will be considered equal in the sorted list. But since the problem requires to output the k-th entry, including duplicates, the order between lex equal substrings must be handled.

But the problem's examples suggest that the order between lex equal substrings is determined by their starting index. For example, in the first sample, the two "a" substrings are ordered as (i=0, l=1) followed by (i=1, l=1). Since they are lex equal, their order is determined by their starting indices.

Thus, the __lt__ method must compare the starting indices when the substrings are lex equal and have the same length. If the substrings are lex equal and have different lengths, the shorter one comes first.

But in the case where two substrings are lex equal but have different lengths, this is impossible. Because if their lengths are different, then one is a prefix of the other. For example, "a" and "aa". But "a" is lex smaller than "aa". So, two lex equal substrings must have the same length.

Wait, no. For example, the substrings "a" and "a" are lex equal and have the same length. Substrings "a" and "aa" are not lex equal. So, the only way two lex equal substrings can have different lengths is if they are the same up to the shorter length, and the longer one has no additional characters. For example, "a" and "a"—same length. Or, if one is a prefix of the other but the other has extra characters. But in that case, the shorter one is lex smaller. So two substrings of different lengths can't be lex equal.

Thus, when two substrings are lex equal, their lengths must be the same. So, in the case where h >= min_len and l == m, we have lex equal substrings. But according to the problem's examples, their order in the list is determined by their starting index.

Thus, the __lt__ method must return True if self.i < other.i, otherwise False.

But what about when two substrings have the same starting index and length? That's impossible, since each (i, l) is unique.

Thus, the __lt__ method should be modified as follows:

In the case where h >= min_len and l == m:

return self.i < other.i

Thus, the __lt__ method becomes:

    def __lt__(self, other):
        i = self.i
        l = self.length
        j = other.i
        m = other.length

        r_i = self.rank[i]
        r_j = other.rank[j]
        if r_i > r_j:
            return not (other < self)
        # Now r_i <= r_j
        if r_j == r_i:
            h = len(self.s) - i
        else:
            # LCP is the min in LCP[r_i+1 ... r_j]
            h = self.lcp_st.query_min(r_i + 1, r_j)
        min_len = min(l, m)
        if h >= min_len:
            # The substrings are equal up to min_len
            if l == m:
                # Lex equal and same length: compare starting indices
                return i < j
            else:
                return l < m
        else:
            c_i = self.s[i + h]
            c_j = other.s[j + h]
            return c_i < c_j

This way, when two substrings are lex equal and of the same length, the one with the smaller starting index is considered smaller. This aligns with the first sample input.

With this change, the heap will order the two "a" substrings (i=0 and i=1) as the one with i=0 comes first.

Now, the code should handle the sample inputs correctly.

But let's test the first sample:

Input:
aa
2

The substrings are:

i=0, l=1 → "a" (first)
i=1, l=1 → "a" (second)
i=0, l=2 → "aa" (third)

The heap will first push (0,1) and (1,1). The initial heap will compare them. Their rank is 0 and 1 (since the suffix array for "aa" is [0,1], assuming the doubling algorithm orders them correctly).

For comparing (0,1) and (1,1):

r_i = rank[0] = 0, r_j = rank[1] = 1.

h is the LCP between suffix 0 and suffix 1. For "aa", the suffix 0 is "aa", suffix 1 is "a". The LCP between them is 1.

min_len = min(1,1) = 1. h >= min_len (1 >=1). l == m (1 ==1). So compare i=0 and i=1: 0 <1 → returns True. So (0,1) is considered smaller than (1,1). So the first extraction is (0,1), then (1,1), then (0,2).

So for k=2, the second extraction is (1,1), which gives the substring "a" as expected.

Thus, the code should work.

Now, the code also needs to handle the case where the heap elements have varying lengths and starting indices.

But the main challenge is to correctly implement the SA, rank, LCP, and the comparison logic.

Another potential issue is the sparse table implementation. For example, if the LCP array is zero-based, and the RMQ is built correctly.

Now, after implementing all this, the code should be correct.

But there's one more thing to check: in the HeapElement's __lt__ method, when comparing two elements, the code uses the rank array and the sparse table.

But the code in the __lt__ method assumes that the rank array and the sparse table are correct.

Now, let's proceed to write the code.

But given the time constraints, here's the final code.
</think>

```python
import sys
import heapq

def build_sa(s):
    n = len(s)
    sa = list(range(n))
    sa.sort(key=lambda x: s[x:])
    return sa

def build_lcp(s, sa, rank):
    n = len(s)
    lcp = [0] * n
    k = 0
    for i in range(n):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp

class SparseTable:
    def __init__(self, data):
        self.n = len(data)
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i//2] + 1
        self.size = self.log_table[self.n] + 1
        self.table = [[0]*self.n for _ in range(self.size)]
        self.table[0] = data
        for j in range(1, self.size):
            for i in range(self.n - (1 << j) + 1):
                self.table[j][i] = min(self.table[j-1][i], self.table[j-1][i + (1 << (j-1))])
    
    def query_min(self, l, r):
        if l > r:
            return 0
        length = r - l + 1
        k = self.log_table[length]
        return min(self.table[k][l], self.table[k][r - (1 << k) + 1])

class HeapElement:
    def __init__(self, i, length, s, rank, lcp_st):
        self.i = i
        self.length = length
        self.s = s
        self.rank = rank
        self.lcp_st = lcp_st
    
    def __lt__(self, other):
        i = self.i
        l = self.length
        j = other.i
        m = other.length
        
        if i == j and l == m:
            return False
        
        r_i = self.rank[i]
        r_j = other.rank[j]
        if r_i > r_j:
            return not other.__lt__(self)
        if r_i == r_j:
            h = len(self.s) - i
        else:
            h = self.lcp_st.query_min(r_i + 1, r_j)
        min_len = min(l, m)
        if h >= min_len:
            if l == m:
                return i < j
            else:
                return l < m
        else:
            c_i = self.s[i + h] if (i + h) < len(self.s) else ''
            c_j = other.s[j + h] if (j + h) < len(other.s) else ''
            return c_i < c_j

def main():
    s = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    n = len(s)
    total = n * (n + 1) // 2
    if k > total:
        print("No such line.")
        return
    
    sa = build_sa(s)
    rank = [0] * n
    for idx, pos in enumerate(sa):
        rank[pos] = idx
    lcp = build_lcp(s, sa, rank)
    lcp_st = SparseTable(lcp)
    
    heap = []
    for i in range(n):
        element = HeapElement(i, 1, s, rank, lcp_st)
        heapq.heappush(heap, element)
    
    result = None
    for _ in range(k):
        current = heapq.heappop(heap)
        result = s[current.i:current.i + current.length]
        if current.i + current.length + 1 <= n:
            new_element = HeapElement(current.i, current.length + 1, s, rank, lcp_st)
            heapq.heappush(heap, new_element)
    
    print(result)

if __name__ == "__main__":
    main()
```