<think>
Okay, let's see. I need to solve this problem where there are two types of queries. The first type updates the suspicion value of a victim, and the second type queries a string q to find the maximum suspicion value among all victims whose names are a contiguous substring of q. The challenge is handling this efficiently, especially with the large constraints—n and m up to 3e5, and the total length of all s_i and q's also up to 3e5 each. So, the solution must be optimized for both time and memory.

First, let's think about the naive approach. For each query of type 2, we can check all possible substrings of q and see if any of them are in the database. Then, track the maximum suspicion value. But this is way too slow. For example, if q is of length L, there are O(L^2) substrings. For each of these, checking in a hash map (like a Python dict) would take O(1) per substring, but even O(L^2) per query is way too slow when L is 3e5 and m is 3e5. So that's not feasible.

So we need a better way. The problem is similar to substring matching, and we need to find all substrings of q that are present in the database. Then, among those, find the maximum suspicion value. The key is to process all possible substrings of q efficiently and find which are in the database, then get the max value.

This sounds like a problem that can be addressed with a trie or a suffix automaton. But considering that the database is fixed (since the names don't change, only their suspicion values), perhaps building a trie or a suffix automaton (like Aho-Corasick) for all the victim names would help. Then, for a given query string q, we can process it through the automaton and collect all the possible names that are substrings, then find the maximum value.

But how to track the maximum suspicion value for each possible substring? Let's think: for each node in the trie (representing a certain prefix), we can track the maximum value among all the victim names that end at this node. Then, when processing the query string q, as we traverse through the trie for each possible starting position, we can keep track of the maximum value encountered.

Wait, but even that approach might not be efficient enough. Let's break it down.

The Aho-Corasick automaton is designed for efficiently finding all occurrences of a set of patterns in a text. Here, each victim's name is a pattern, and the query string is the text. So, for each query of type 2, we can use the automaton to find all the patterns (names) that are substrings of q, and then collect their current suspicion values. The maximum of these values would be the answer.

But the problem is that each query of type 2 could involve a large q, and the number of matches could be large. So, traversing the automaton and checking all possible matches would take O(len(q) + number of matches) time. However, if the number of matches is high (like if q is a long string and many names are present), this could be O(L + K) per query, where K is the number of matches, which might be up to O(L^2) in the worst case. That's not acceptable for L up to 3e5 and m up to 3e5.

Therefore, this approach would not work for large inputs. So we need a way to track the maximum suspicion value efficiently without having to check all possible matches.

Hmm. Alternative approach: For each possible substring in the database (i.e., for each name in the victims), we need to know the current maximum suspicion value. Then, for a query q, we need to find all substrings of q that are in the database and track the maximum. But how?

Another idea: For each possible name in the database, precompute all possible occurrences and track the maximum value. But when a query comes, we need to check all possible substrings of q and see which ones are in the database. The maximum of those is the answer. But again, this is O(L^2) per query, which is too slow.

Wait, but the problem requires the maximum value. So maybe for each possible substring of the query q, if that substring is a name in the database, we can track the maximum value. So the key is, for each position in q, check all possible suffixes (or prefixes) and see if they are present in the database. Then, keep track of the maximum.

But even checking for all possible suffixes can be time-consuming. For example, for each position i in q, check all possible lengths of substrings starting at i. For each possible length, check if the substring is present in the database. If it is, get the current max suspicion value.

But again, this is O(L) per query (if we can check each possible substring in O(1) time) multiplied by the average number of possible lengths per position. For example, if a victim's name can be of any length up to some maximum, then for each position i in q, we need to check all possible lengths up to the maximum name length. If the maximum name length is, say, 1000, then for each position i, we check up to 1000 possible lengths. But if the maximum name length is large (like up to 3e5), then this would be O(L^2), which is again impossible.

So the solution must find a way to process the query string in linear time, O(L), regardless of the number of possible matches.

Another angle: For all the names in the database, we can precompute a trie structure. Then, for a given query string q, we can process each character in q, and for each position, traverse the trie as far as possible, keeping track of the maximum suspicion value encountered along the way.

Wait, maybe that's possible. Let's think:

1. Build a trie for all names in the database. Each node in the trie represents a prefix of some name. For each node that corresponds to the end of a name (i.e., the full name), we keep track of the maximum suspicion value among all names that end at this node. But since names can be updated (queries of type 1), each node that is the end of one or more names must have a way to track the maximum value of those names.

But how? For example, if two different names "a" and "ab" end at different nodes. Wait, no. Each name would be inserted into the trie as a path from the root. So each name corresponds to a unique path. So for each node in the trie, if any name ends there, then we can keep a value (the maximum of all names that end at that node). Wait, but the same name could be present multiple times in the database. But according to the problem statement, the victim names are not necessarily unique. So for example, there could be two victims with the same name. When the query is of type 2, all occurrences of their name as a substring contribute their individual suspicion values to the maximum.

So the problem is, each name in the database (even if duplicated) contributes to the possible maximum. So for the same substring (name) appearing multiple times, each with their own suspicion value, the maximum of those values is what's needed.

Therefore, the trie approach would need to track, for each possible name (string), the maximum current suspicion value among all victims with that name. Because even if the same name is present multiple times, when a query checks for that name as a substring, all of their suspicion values are considered, and the maximum is taken.

So, for example, if there are three victims with name "abc", their suspicion values could be 10, 20, 30. Then, the maximum for "abc" would be 30. If one of them is updated to 40, then the maximum becomes 40.

So the key is to, for each unique name, track the maximum suspicion value of all victims with that name. Then, when processing a query, we need to find all substrings of q that are present as a name (unique, but with their maximum value), and take the maximum among those.

So, here's a plan:

- For all names in the database, build a trie or a hash map that maps each unique name to the current maximum suspicion value for that name. Then, for each query of type 2, we need to find all substrings of q that are present in the hash map, collect their maximum values, and take the overall maximum.

But how to find all substrings of q that are present in the hash map efficiently?

The problem here is that generating all possible substrings of q and checking the hash map is O(L^2), which is not feasible for large q (e.g., L=3e5 would take 9e10 operations).

So the crux of the problem is to find all possible names present in q as substrings, and find the maximum value among them, but in O(L) time.

Another approach: For each query string q, we can precompute all possible names that are substrings of q and are present in the database, and then take the maximum value. But again, how to do this efficiently.

Alternative Idea: Use a suffix automaton of the database names. Then, for a query q, traverse the automaton and collect all possible names that are substrings. However, even this might not work because the number of possible matches could be large.

Wait, but the maximum value is what's needed. So perhaps during the traversal of the automaton for q, we can track the maximum value encountered. Let's think:

1. Preprocess all names into a trie or automaton, where each state represents a substring (prefix) of the names. For each state that corresponds to the end of a name, we track the maximum value of all names that end here. But since names can have different lengths, perhaps we can have for each node (state) the maximum value of all names that end at that state. Then, as we process each character in q, we can keep track of the current nodes in the automaton (for all possible starting positions), and update the maximum value encountered.

Alternatively, here's a possible approach inspired by the Aho-Corasick algorithm:

- Build a trie of all names in the database. Then, build the failure links for the trie (Aho-Corasick automation). For each node in the trie, store the maximum value of any name that ends at that node or any of its suffix links (failure links). Then, when processing the query q character by character, we can traverse the trie, and for each step, collect the maximum value from the current node and its suffix chain. This way, each character in q is processed once, and for each position in q, the maximum value of all names that end at that position (as a substring) is computed. The overall maximum is the answer.

Wait, that sounds promising. Let's elaborate.

The Aho-Corasick automaton is built for the names, and each node (state) represents a set of possible prefixes. For each node, we can precompute the maximum value of any name that ends at that node. But also, when following failure links (which point to the longest proper suffix that is present in the trie), we can compute for each node the maximum value along the path of failure links. This way, when we process a character in the query string, we can traverse through the trie and the failure links, and collect the maximum value encountered along the way.

Wait, here's the detailed plan:

1. Build a trie for all the names. Each node represents a sequence of characters. For each node that is the end of a name, track the maximum value of all names that end here. But since multiple names can end at the same node (if they are the same string), then whenever a name's value is updated, we need to update the node's maximum value. Wait, but each unique name corresponds to exactly one path in the trie. So if multiple victims have the same name, then the node at the end of that path would track the maximum value among all of them.

But how to handle updates? For example, if a victim's name is "abc", and there are three entries in the database with that name. The node for "abc" in the trie would track the maximum of the three values. When a query of type 1 updates one of these, the node's maximum value should be updated accordingly.

Wait, no. Because each victim's name is stored in the database. So the trie needs to track all possible names (strings) from the database. For each unique string s, there might be multiple victims with that name. The maximum suspicion value for s is the maximum of the values of all victims with that name. So for example, if the database has three victims with name "abc", each with values 10, 20, 30, then the maximum for "abc" is 30. If one of them is updated to 40, then the maximum becomes 40. So the trie's node for "abc" should track this maximum.

Thus, the trie's nodes for the end of each name (s) must have the current maximum value of all victims with that name. So, for each unique name s in the database, when building the trie, we create a path for s, and the end node for s will track the maximum value of all victims with that name. Then, when a query of type 1 is performed (updating the i-th victim's value), we need to find the name s_i of that victim, and update the maximum value for s_i. If the new value is higher than the current maximum for s_i, then the node in the trie for s_i is updated. Otherwise, perhaps we need to track all values for s_i and find the maximum when needed, but that would be inefficient.

Wait, but for each unique name s, we need to track the current maximum of all victims with that name. So for the trie's end node for s, we can store the current maximum. Then, when a victim's name is updated, we can recompute the maximum for that name.

But how to track all victims with the same name? We can have a dictionary that maps each name s to a list of indices (victim indices) that have this name. Then, when a victim's value is updated (query type 1), we check if the new value affects the maximum for s. For example, if the previous maximum for s was M, and the updated victim's value is now x, if x > M, then the new maximum is x. If the previous maximum was from another victim, but x is not larger, then the maximum remains M. However, if the previous maximum was the victim being updated, and x is now less than M, then the maximum needs to be recomputed by checking all victims with name s.

But recomputing the maximum each time a victim's value is updated could be O(k) time, where k is the number of victims with that name. For example, if a name has 3e5 occurrences (all with the same name), then updating one of them could take O(3e5) time, which is not feasible.

Therefore, we need a way to track the maximum value for each unique name efficiently, allowing for O(1) updates and O(1) queries.

An efficient data structure for this is a max-heap, but even then, if the maximum is removed, we need to find the next maximum. Alternatively, for each unique name, track the current maximum value. Whenever a victim's value is updated, we check if it's part of the current maximum and update accordingly.

Wait, here's a plan:

- For each unique name s in the database, maintain a list of all victims with that name. Also, track the current maximum value for s.

- When a victim i (with name s) is updated to x:

   - If x is greater than the current maximum of s, then update the maximum to x.

   - Else, if the previous value of victim i was the current maximum, then we need to scan all victims with name s to find the new maximum.

But this approach could lead to O(1) updates in the best case (if the new value is higher than the current maximum) and O(k) in the worst case (if the previous maximum is being reduced and we have to find a new maximum). This is not acceptable for large k.

Thus, this approach is not feasible for the problem's constraints. So, we need a data structure that allows for O(1) time updates and O(1) time maximum queries for each unique name. How can this be achieved?

The answer is to use a structure where each unique name's maximum is tracked, and all victims of that name are stored in a way that allows the maximum to be maintained efficiently. However, in Python, such a structure would be difficult to implement, but perhaps we can use a dictionary for each name to track the maximum.

Wait, here's an alternative approach: whenever a victim's value is updated, we check if the new value is higher than the current maximum for their name. If it is, then we update the maximum. Otherwise, if the previous value was the maximum, then we need to find the new maximum. To avoid scanning all elements each time this happens, perhaps we can track all the values for each name in a way that allows us to quickly find the maximum. However, this requires a priority queue structure that can handle dynamic updates. But such a data structure is not standard in Python and would be complex to implement.

Alternative Idea: Instead of maintaining the maximum for each name, we can precompute all possible names and their maximum values, and for each query of type 1, we can update the maximum for the name of the victim being modified.

Wait, here's the plan:

1. Create a dictionary called max_values where the keys are the unique names in the database, and the values are the current maximum suspicion values for those names.

2. For each victim, track their current suspicion value and their name.

3. When a query of type 1 comes (update victim i to x), we need to:

   a. Get the victim's current name s.

   b. Decrement the count for s if necessary. Wait, no. Wait, when the victim's value is updated, the previous value may have been the maximum for s. So, if the previous value was the maximum, then the max for s may need to be recomputed. For example, suppose s's max was 100 (from victim i), and we set victim i's value to 50. Then, the max for s may now be the next highest value among all victims with name s.

But how to track that without scanning all victims with s each time?

This seems like a problem that requires a data structure that can track the maximum value of a dynamic set. A possible solution is to use a binary max-heap for each name. However, when a value is updated, it's hard to efficiently update the heap. Alternatively, using a balanced binary search tree for each name, allowing for O(log k) insertion, deletion, and maximum queries.

But in Python, the standard library doesn't have a built-in balanced BST, but we can simulate it using modules like `bisect` for sorted lists. However, for each name, maintaining a sorted list of values would allow us to find the maximum in O(1) time (the last element), but inserting and deleting would take O(k) time (since inserting into a sorted list requires shifting elements). This is not feasible for large k.

Alternative Idea: Since the suspicion values can be updated, and we need to track the maximum for each name, perhaps the best approach is to track for each name the current maximum value, and whenever a victim's value is updated, if the name's current maximum is affected, then recompute the maximum for that name.

For example:

- For each unique name s, keep a list of all current values of victims with that name.

- max_values[s] is the maximum of this list.

When a victim is updated:

   a. Suppose the victim's old value was old_val and new value is new_val.

   b. If s's current max is old_val and new_val < old_val:

       i. We need to find the new max by scanning all values of s.

   c. Else:

       i. If new_val > max_values[s], then update max_values[s] to new_val.

       ii. Else, do nothing for the max (since the old max is still valid).

But in the case where the old value was the max and the new value is lower, we have to scan all the values of s to find the new max. This could take O(k) time per update, which is O(n) in the worst case (if all victims have the same name). For n=3e5, this is O(3e5) per update, which is not feasible.

So this approach is not efficient enough.

Alternative Idea: We can track for each name s the current maximum and a count of how many times the maximum appears. For example, if max_values[s] is 100, and there are 5 victims with that name and value 100, then if any of them are updated to a lower value, we decrement the count. Only when the count reaches zero do we need to recompute the maximum.

But this approach requires tracking all occurrences of the maximum for each name. For example, for each name s, we can have:

- max_val: the current maximum.

- count: the number of victims with name s and value equal to max_val.

Then, when a victim's value is updated:

   a. If the victim was part of the max_val (old_val == max_val):

       i. If new_val < old_val:

           - Decrement count.

           - If count becomes zero, then recompute max_val and count by scanning all victims of s.

       ii. Else if new_val == old_val:

           - Do nothing (count remains the same).

       iii. Else (new_val > old_val):

           - This is impossible because old_val was the max.

   b. Else (old_val < max_val):

       i. If new_val > max_val:

           - Update max_val to new_val, count = 1.

       ii. Else if new_val == max_val:

           - Increment count by 1.

       iii. Else:

           - Do nothing.

But this approach still requires that when the count becomes zero, we have to scan all victims of s to find the new max. For example, if all victims with max_val are updated to lower values, then we have to scan the entire list again.

In the worst case, this could still be O(k) per update.

But perhaps this reduces the number of times we need to scan. For instance, if there are multiple victims with the same maximum value, then each update that reduces their value would decrement the count. Only when all are updated do we need to recompute.

But again, in the worst case, this approach may not be feasible.

Hmm. So perhaps the problem requires a different approach. Let's think again about the queries.

For each query of type 2, we need to process the string q and find the maximum suspicion value among all substrings of q that are present in the database.

But the key insight here is that the maximum possible value could come from the longest possible name, or perhaps any name. But how to track that.

Another Idea: For each possible name in the database, track the maximum value. Then, for a query q, the maximum value is the maximum of all max_values for names that are substrings of q.

Thus, the problem reduces to finding all names that are substrings of q and then taking their max_values.

The question is: how to efficiently find all names that are substrings of q and compute the maximum of their max_values.

The challenge is to do this in O(L) time per query, where L is the length of q.

So the problem is equivalent to, given a large set of strings S (the names in the database), for each query string q, find the maximum value among all strings in S that are substrings of q.

This is a classic problem in string processing, and one efficient solution is to use the Aho-Corasick algorithm. But with the twist that we need to track the maximum value during the traversal.

Here's the plan:

1. Preprocess all names into an Aho-Corasick automaton. For each node (state) in the automaton, which corresponds to a prefix of some name, track the maximum value of any name that ends at this node.

   - When building the automaton, each name is added to the trie. For each node that marks the end of a name (i.e., the end of the path for that name), we record the current max value for that name. However, since multiple names can be added (if the same string is present in multiple victims), the maximum is the maximum of all their suspicion values.

2. For each query of type 2, process the string q through the automaton. For each position in q, as we traverse the automaton, we check all possible states (nodes) that represent the end of a name, and keep track of the maximum value encountered.

But how to efficiently track the maximum value as we process q.

In Aho-Corasick, during the traversal, each step processes a character, and the current state transitions according to the trie and the failure links. The failure links allow the automaton to efficiently find all occurrences of any pattern in the text (q) in linear time.

But to find the maximum value, we can modify the Aho-Corasick automaton so that each node also tracks the maximum value of any name that ends at that node or any of its failure links (since a longer suffix may be a name). Alternatively, during the traversal, for each node visited, we can traverse up the failure links and collect the maximum value.

But traversing the failure links for each character in q would take O(L * K), where K is the average number of failure links traversed per character. However, in practice, for Aho-Corasick, the failure links are optimized such that each transition is O(1), but the traversal up the failure links could still take O(1) per step due to precomputed links.

Alternatively, during the construction of the Aho-Corasick automaton, each node can have a "output" value which is the maximum of the node's own value (if it's the end of a name) and the output values of its failure link. This way, each node's output value represents the maximum value of any name that ends at this node or any of its suffixes (via the failure links). This is similar to the way in which the Aho-Corasick algorithm collects all matches.

If we precompute this during the automaton construction, then during the traversal of q, for each character, we can track the current node and check its output value, which gives the maximum value of any name ending at that position in q. We can then keep a global maximum of all such values encountered during the traversal.

This approach would allow processing each query in O(L) time, which is acceptable for L up to 3e5 and m up to 3e5.

So here's the detailed plan:

1. For each unique name in the database:

   a. Insert it into the trie.

   b. When inserting, for each node in the trie path, if the node is the end of a name (i.e., the current name ends here), then we need to track the maximum value of all victims with that name.

   c. However, since the same name can be present multiple times (for different victims), each insertion of the same name must contribute to the maximum value stored at the end node. So, when building the trie, for each name, we insert it once and track the maximum value for that name. But if the same name is added multiple times (from different victims), the maximum value for the end node is the maximum of all those victims' initial values (which are 0). Wait, but initially, all suspicion values are 0. Then, during updates, the max_values for each name are updated. So the trie's nodes need to have a way to reference the current max value for their corresponding name.

Wait, this is a problem. Because the trie is built once, but the max values for names can change dynamically due to type 1 queries. Therefore, storing the max value in the trie's nodes during the build time is incorrect, as the values can change over time.

So the initial approach of building an Aho-Corasick automaton with max values precomputed is not feasible, because those values can change after updates.

This is a key realization. The Aho-Corasick approach is static, but our problem requires dynamic updates to the max values. Thus, any solution based on a static automaton would not work unless we can find a way to dynamically update the max values in the automaton.

So this complicates things. Because during a query of type 2, the automaton needs to have up-to-date max values for each name. But if those max values can change dynamically (due to type 1 queries), we need a way to update the automaton's nodes with the current max values.

But modifying the automaton's nodes each time a type 1 query is processed could be time-consuming, especially if many type 1 queries are issued. For example, if each type 1 query requires traversing the trie to find the end node for the victim's name and updating its max value, this could take O(k) time per update, where k is the length of the name.

But given that each name's max value is stored in the end node of its trie path, and the trie is built once, perhaps for each type 1 query, we can:

   a. Get the victim's name s.

   b. Find the end node in the trie for s (which can be done in O(len(s)) time).

   c. Update the max value stored at that node.

But wait, the end node's stored max value should be the maximum of all victims with that name. So when a victim's value is updated, we need to recompute the max for that name and update the end node's value.

This suggests that the trie's end nodes must have a reference to the current max value of the name. But how to track this.

So here's the revised plan:

- For each unique name s in the database, maintain a list of victims with that name, and track the current maximum value for s. This can be done with a dictionary, say name_to_max, where name_to_max[s] is the current maximum value for s.

- The trie's end nodes for each name s must reference this max value. So when building the trie, for each name s, we create a path in the trie and at the end node, store a pointer (or a reference) to the corresponding name_to_max[s]. Thus, when processing a query of type 2, the automaton can quickly retrieve the current max value for s by looking up the name_to_max[s] via the end node.

But how to link the end node to the name's max value.

In Python, this can be done by having each end node in the trie contain a key (the name s), and then when processing the trie during a query, upon reaching an end node, the current max value is retrieved from name_to_max[s].

Alternatively, during the construction of the trie, for each end node, we can store the name s, and then during a query, when the automaton reaches that node, we look up name_to_max[s] and compare it to the current maximum.

But storing the name s in the trie node may not be feasible due to memory constraints, especially if the names are long. So an alternative is to have a separate dictionary that maps the end nodes to their corresponding name s. But this may not be necessary.

Alternatively, during the insertion of a name s into the trie, for each node along the path, when we reach the end of s, we can record that this node represents the name s, and thus, when processing a query, the max value for s is name_to_max[s].

Thus, during the query processing, whenever the automaton encounters a node that is the end of a name, it can look up name_to_max[s] and check if it's the current maximum.

But during the automaton's traversal of q, how do we collect all the possible names that are substrings of q and find their current max values?

The solution requires that during the traversal of q through the automaton, for each possible position in q where a name ends, we retrieve the current max value of that name and track the overall maximum.

This seems possible with the following approach:

1. Preprocess all names into an Aho-Corasick automaton. For each name s, its path in the trie ends at a node which is marked as representing the name s. The automaton is built with failure links.

2. For each node in the automaton, during the preprocessing phase, compute a "output" which is a set of names (s) that end at this node or any of its failure links. However, since the failure links point to the longest proper suffix, this could allow us to collect all possible names that end at any point during the traversal.

But this approach would collect all possible names that are substrings of q, but each occurrence of a name would require checking its current max value.

But during query processing, for each character in q, we traverse the automaton, and for each node encountered, we check all names in its output set. For each such name, we look up the current max value and keep track of the maximum.

However, if the output sets for nodes can be large, then this approach would again be O(L + K) per query, where K is the total number of matches. This is not feasible for K up to O(L^2), which is possible for large L.

Thus, this approach would not work for the problem's constraints.

Alternative Idea: To find the maximum value among all possible names that are substrings of q, we can track for each position in q the maximum value of any name ending at that position. The maximum of these values across all positions is the answer.

Thus, for each position i in q (1-based), we need to find the maximum value of any name s that is a substring ending at i. For example, if s has length l, then it starts at i - l + 1 and ends at i.

To compute this efficiently for all positions, we can preprocess the names into a trie and for each position in q, find the longest possible name ending there, then check all possible names that are suffixes of the current substring.

But how to do this quickly.

This sounds like the problem of finding the longest prefix of a string that matches any name, but in reverse. Alternatively, building a suffix automaton for the names and then processing q to find the maximum value.

Another Idea: Use a suffix automaton to process q and find all possible names that are substrings, then track the maximum value. But I'm not sure.

Alternatively, for each position i in q, check all possible prefixes of q[0..i] (i.e., substrings ending at i) and see if they are present in the database. For each such substring, check its max value. The maximum of these is the answer for the query.

But again, this is O(L^2), which is not feasible.

Thus, the crux of the problem is to find a way to process q in O(L) time, while dynamically updating the max values for the names.

Let's think differently. What if we precompute for all possible prefixes of the query string q the set of possible names that end at each position, and then for each of these names, we look up their max value and keep track of the maximum.

But how to find these names quickly.

Another Idea: For each name s in the database, build a hash of s. Then, for the query string q, generate all possible substrings and check if they exist in the hash. For each substring that exists, get its max value and track the maximum.

But generating all possible substrings of q is O(L^2) time, which is not feasible.

So, the only way to make this work is to find a way to process the query string in O(L) time, using an automaton that allows us to track all possible names that are substrings of q, and retrieve their current max values on the fly.

Thus, the solution must use an automaton structure that can be updated dynamically as the max values of names change.

But in practice, building such a structure is complicated.

Another Idea: Since the names in the database are fixed (only their suspicion values change), the trie structure can be built once, and each end node in the trie contains a reference to the current max value of the corresponding name.

Thus, when a type 1 query updates the max value of a name, we only need to update the entry in the dictionary (name_to_max[s]), and the end node in the trie can reference this value.

So here's the detailed approach:

1. Preprocess all names into a trie. For each name s in the database, add it to the trie. For each end node in the trie (where a name ends), keep a pointer to the max value of that name. Initially, all max values are 0.

2. For each name s, maintain a dictionary name_to_max that maps s to its current max value. This is initially 0 for all names, but when a type 1 query updates a victim's value, we need to update the max value for s (the name of that victim).

Wait, but how to compute the max value for s. We need to track all victims with that name and their current values, then compute the max.

But this brings us back to the problem of how to track the max for each name efficiently.

So, for each name s, we need to track all victims with that name and their current values, and the current max.

So, during preprocessing:

- For each victim i (0-based or 1-based?), we record their name s_i.

- We group all victims by their name. For each name s, victims[s] is a list of indices of victims with that name.

- For each name s, name_to_max[s] is the maximum of the current values of the victims in victims[s].

- The trie's end node for s contains a reference to name_to_max[s].

Then, for a type 1 query (1 i x):

- Get the victim's index i (assuming it's 1-based, so subtract 1 to get 0-based if necessary).

- Find their name s = names[i].

- Update the victim's value (assuming we have an array values where values[i] is the current value of victim i).

- Check if the previous value was equal to name_to_max[s]. If yes, then we need to recompute the max for s. Otherwise, if the new value x is greater than name_to_max[s], then update name_to_max[s] to x.

But recomputing the max can be expensive if there are many victims with the same name.

Thus, to handle this efficiently, we need to track for each name s:

- The current max value.

- The list of victims with name s.

- A data structure that allows quickly finding the max value when one of the elements is updated.

In Python, the most efficient way to do this is to use a priority queue (heap), but the problem is that when a value in the heap is updated, it's not straightforward to update the heap structure. However, we can use a max-heap and track the current max, but when a victim's value is updated, if the new value is higher than the current max, then it becomes the new max. Otherwise, if the old value was the max, we need to rebuild the heap.

But this is not efficient.

Alternative Idea: For each name s, maintain a list of the current values of victims with that name. Then, the max is the maximum of this list. However, for each update, if the victim's value is part of s's list, we can update it and then recompute the max. But this would be O(k) time for s with k victims.

This is not feasible for large k.

Thus, the only way to handle this efficiently is to track for each name s the current maximum value, and when a victim's value is updated:

- If the new value is greater than the current max, update the current max.

- If the old value was the current max, check if there are any other victims with the same max. If not, recompute the max by scanning the list.

But how to track if there are other victims with the same max.

For example:

For each name s:

- current_max: the maximum value.

- count: the number of victims with value == current_max.

When a victim's value is updated from old_val to new_val:

If the victim was part of s's victims:

   a. If old_val == current_max:

      i. Decrement count.

      ii. If count == 0:

          - Compute new current_max as the maximum of all victims in s, and set count to the number of victims with new current_max.

   b. If new_val > current_max:

      i. current_max = new_val

      ii. count = 1

   c. Else if new_val == current_max:

      i. count += 1

   d. Else:

      i. Do nothing.

But when count == 0 after decrementing, we have to scan all victims in s to find the new maximum and count. This is O(k) time, which could be expensive if k is large.

But given that the number of type 1 queries is up to 3e5, and each may take O(k) time in the worst case, this is not feasible.

Thus, this approach is not efficient enough.

Alternative Idea: The problem requires that for each name s, the max value is tracked, and that when a victim's value is updated, the max is updated if necessary. But the problem allows the max to be stored for each name s in a way that can be queried in O(1) time.

Thus, perhaps we can accept that in the worst case, some type 1 queries will take O(k) time. But this is not acceptable for large k.

Hmm. This seems like a dead end. Let's think of alternative approaches.

Let's focus back on the query of type 2. We need to find the maximum value among all names that are substrings of q.

But perhaps we can process q using a suffix automaton and for each possible substring, track the maximum value. But again, this seems similar to the previous approaches.

Another Idea: Use a rolling hash for all possible substrings of q. For each substring, compute its hash and check if it exists in a precomputed hash map of names. For each hash that exists, get the max value and keep track of the overall maximum.

But the problem is that the number of possible substrings of q is O(L^2), which is not feasible for L=3e5. So this approach is not suitable.

Thus, the only viable solution is to use the Aho-Corasick automaton approach, but with dynamic updates to the max values.

Here's the plan:

1. Preprocess all names into an Aho-Corasick automaton.

2. For each node in the automaton that marks the end of a name, store a reference to the current max value of that name (using a dictionary name_to_max).

3. For each query of type 2, traverse the automaton with q, and for each character, follow the trie and failure links. For each node visited, check if any of the names ending here have a current max value, and track the overall maximum.

But how to collect all names that end at any node along the way.

In the Aho-Corasick algorithm, when processing a text, the automaton is designed to visit all possible matches as they occur. So during the traversal of q, each time a name is found as a substring, the automaton can collect it.

But in this problem, we need to find all such names and track their current max values, then find the maximum.

However, if the automaton is modified to, for each node, track the maximum value of any name that ends at that node or any of its suffix links (failure links), then during the traversal, for each character, we can check the current node's max value and update the global maximum.

But how to precompute this.

Here's a way to do it:

During the automaton's construction, for each node, we precompute the maximum value of any name that ends at this node or any of its suffix links (i.e., the failure chain). This maximum value is computed once during the automaton's construction and stored in the node.

However, this approach is static and does not account for updates to the max values of the names. Thus, when a type 1 query updates the max value of a name, the nodes in the automaton that correspond to that name's path would need to have their stored max values updated, which is not feasible if the failure chain's max values are also dependent on other nodes.

Thus, this approach would not work for dynamic updates.

So, the crux of the problem is that the max values can change dynamically, and the automaton needs to reflect these changes in real-time.

Given that, the only way to handle this is to have the automaton's nodes reference the current max values stored in the name_to_max dictionary. This way, when the max value of a name changes, the nodes that correspond to that name in the automaton automatically reference the new value.

Thus, the steps are:

1. Build a trie for all names. For each name s, insert it into the trie, and for the end node of s, store a reference to name_to_max[s].

2. Build the Aho-Corasick automaton with failure links.

3. For each query of type 2, process q through the automaton. For each character, traverse the trie, and for each node visited (including failure links), check if any name ends here, and if so, retrieve the current max value from name_to_max[s], and track the overall maximum.

But how to efficiently retrieve the current max values for all names encountered during the traversal.

The solution is to modify the Aho-Corasick automaton such that each node has a list of names that end at that node. However, this would require storing all possible names for each node, which is memory-intensive.

Alternatively, during the traversal of the automaton, for each node, we can traverse the failure links and check if any of the nodes along the failure chain have names that end there. For each such node, we retrieve the current max value of the corresponding name and update the global maximum.

But this would require, for each character in q, traversing the failure chain until the root node, which could take O(L) time per query in the worst case. For example, if the query string is 'aaaa...' and the names are 'a', 'aa', 'aaa', etc., each failure chain could be long.

Thus, this approach may not be feasible.

Another Idea: During the automaton's construction, precompute for each node the maximum value of any name that ends at that node or any of its failure links. This can be done by propagating the maximum value during the construction of the automaton. However, since the max values can change dynamically, this approach won't work.

Thus, the conclusion is that the only feasible way to handle dynamic updates is to for each query of type 2, process the query string q using the automaton, and for each node visited, traverse the failure chain and collect the current max values of all names ending at those nodes. But this would take O(L * average failure chain length) time per query, which might be acceptable if the average failure chain length is small.

But in practice, the average failure chain length per character is O(1) due to the way the failure links are constructed. For example, the failure links in Aho-Corasick are such that the failure chain for any node has a length of O(1) amortized per character.

Thus, this approach could be feasible.

So here's the plan:

1. Preprocess all names into an Aho-Corasick automaton. For each name s, when inserting into the trie, the end node for s will have a reference to the name_to_max[s] dictionary.

2. For each query of type 2, process the string q through the automaton. For each character in q:

   a. Move to the appropriate child node, following failure links as needed (standard Aho-Corasick traversal).

   b. Once the current node is determined, traverse the failure chain from that node to the root. For each node in this chain:

       i. If the node marks the end of any names, retrieve the current max values for those names and update the global maximum.

But wait, each node in the trie can be the end of multiple names (if the same name is inserted multiple times). Or, perhaps each node marks the end of exactly one name (since each name is a unique path). Wait, no. Each unique name is inserted once into the trie, and its end node is unique. So each end node corresponds to exactly one name.

Thus, during the insertion of names into the trie, each name is added once, and its end node stores a reference to the current max value for that name (name_to_max[s]).

Then, during the traversal of the query string q:

   a. For each character in q, move to the next node in the trie.

   b. Then, from this node, traverse the failure links (failure chain) and for each node in the chain:

       i. If it is an end node of a name, retrieve name_to_max[s] and track the maximum.

Thus, for each character in q, we process O(1) failure nodes on average, and for each, check if it's an end node, retrieve the current max, and update the global maximum.

This approach would process each query in O(L) time on average, which is acceptable.

The steps are:

For each query of type 2:

   Initialize current node to the root.

   max_val = -1.

   For each char in q:

      while current node has no child for char, follow failure link.

      if current node has child for char:

          move to child.

      temp_node = current node.

      while temp_node is not root:

          if temp_node is an end node (has a name s):

              current_max = name_to_max[s]

              if current_max > max_val:

                  max_val = current_max

          temp_node = temp_node.failure_link

      if temp_node is root and temp_node is an end node:

          check and update max_val.

   After processing all characters, output max_val if >=0, else -1.

But how to efficiently determine if a node is an end node and retrieve its name.

Each node in the trie can have a 'name' attribute, which is None unless the node is the end of a name. For end nodes, the 'name' attribute is the string s, and we can then look up name_to_max[s].

Thus, during the insertion of a name s into the trie:

   current = root

   for char in s:

       if char not in current.children:

           create new node.

       current = current.children[char]

   current.is_end = True

   current.name = s

Then, during the traversal of the failure links for a node, we check if the node has a name. If yes, we look up name_to_max[name] and compare it to the current maximum.

Thus, the critical part is that the trie nodes for the end of names have their 'name' attribute set, and during query processing, each node in the failure chain is checked for being an end node.

Now, for the type 1 queries, when a victim's name is updated, we need to:

   a. Get the victim's name s.

   b. Update the victim's value in the list of values for s.

   c. Recompute the max value for s and update name_to_max[s].

But how to track the max value for s.

To handle this efficiently:

- We can maintain for each name s a list of victims (their indices) and their current values.

- For each name s, name_to_max[s] is the maximum value among these victims.

- When a victim's value is updated, we need to update the list for s and recompute the max if necessary.

But recomputing the max each time a victim's value changes is expensive. Thus, we need a way to track the current max for s efficiently.

Given the problem constraints, the only feasible way is to track for each name s the current max value and accept that some type 1 queries may take O(k) time in the worst case.

But given that the problem allows for 3e5 type 1 queries, and each could take O(k) time, this may not be feasible.

However, the problem constraints may be such that in practice, the average case is manageable. For example, if most names are unique, then the max for a name is simply the current value of the victim.

Thus, here's the plan for handling type 1 queries:

- Maintain an array values[] where values[i] is the current value of victim i.

- Maintain a dictionary name_to_victims where name_to_victims[s] is a list of indices of victims with name s.

- For each name s, name_to_max[s] is initially 0.

- When a type 1 query is processed (1 i x):

   a. Convert i to 0-based index (assuming input is 1-based).

   b. Get the victim's old value old_val = values[i].

   c. Update values[i] to x.

   d. Get the victim's name s = names[i].

   e. If name_to_max[s] == old_val:

       i. Check if any other victim in name_to_victims[s] has a value >= old_val.

       ii. If yes, name_to_max[s] remains old_val.

       iii. If not, recompute name_to_max[s] as the new maximum of all victims in name_to_victims[s].

   f. Else if x > name_to_max[s]:

       i. Update name_to_max[s] to x.

   g. Else:

       i. Do nothing.

But step e.iii requires recomputing the max, which takes O(k) time for a name with k victims. This could be O(n) in the worst case (if all victims have the same name).

Thus, this approach is not feasible for large k.

Alternative Idea: For each name s, track the current max and the list of values. When a victim's value is updated, if the new value is higher than the current max, update the max. Otherwise, if the old value was the max, recompute the max. Otherwise, do nothing.

This way, the majority of updates would be O(1), except for cases where the old value was the max and new value is lower than the current max, which requires O(k) time.

But in practice, if the max is not frequently being reduced, this could be manageable.

Thus, the code would look like this:

For each type 1 query:

   i is 1-based, so idx = i-1.

   s = names[idx]

   old_val = values[idx]

   new_val = x

   values[idx] = new_val

   if name_to_max[s] < new_val:

       name_to_max[s] = new_val

   elif old_val == name_to_max[s]:

       current_max = max( values[v] for v in name_to_victims[s] )

       name_to_max[s] = current_max

This way, most updates are O(1), except when the old value was the max and the new value is not. In that case, we have to scan all victims of s to find the new max.

In the worst case, this is O(k) time per update, which is not acceptable for large k.

But given that the time limit is 2 seconds per test case, and 3e5 operations, each taking up to 3e5 steps, this would be O(9e10) operations, which is way too much.

Thus, this approach is not feasible.

Given the time constraints, it's clear that this problem requires a different approach.

Alternative Idea: Consider that the problem's answer is the maximum value among all names that are substrings of q. For the query, it's possible that the maximum value is from the longest possible name, or a particular name. But how to find this efficiently.

Another Idea: For each query of type 2, the maximum value can be obtained by checking all names present in q. Thus, for each query, the answer is the maximum of name_to_max[s] for all s that are substrings of q.

The problem is to find all s in the database that are substrings of q, and take their maximum.

Thus, the problem reduces to, for a given q, find the maximum value among all s that are substrings of q.

The key is to find all such s quickly.

An alternative approach is to precompute for each name s its occurrence in any q string, but this is not possible.

Thus, the only feasible solution is to use the Aho-Corasick automaton approach, and during query processing, track the maximum value of any name that is a substring of q.

Thus, the solution is:

- Preprocess all names into an Aho-Corasick automaton.

- For each name s, track its current max value in a dictionary.

- For each query of type 2, traverse q through the automaton, and for each character, traverse the failure chain to collect all possible names ending there, and track the current max.

The steps are as follows:

Implement the Aho-Corasick automaton with each node storing whether it is the end of a name, and the corresponding name.

For each query of type 2, iterate over each character in q, moving through the automaton, and for each node visited, follow the failure chain to check for end nodes, and keep track of the maximum value.

Thus, the code will involve building the trie, adding failure links, and for each query of type 2, processing the string through the automaton.

Now, the implementation.

But implementing the Aho-Corasick automaton in Python is time-consuming, especially given the large constraints. However, given that the total length of all names is up to 3e5, the trie can be built efficiently.

But in Python, using dictionaries for the trie's children may be too slow for large datasets. Thus, we can use a list of nodes, where each node is an object with a dictionary of children and other attributes.

Here's the code outline:

1. Read n and m.

2. Read the n names, storing them in a list names.

3. For each name, build the trie.

4. For each name, maintain a list of victims with that name, and compute name_to_max[s] as the maximum of their values.

5. Build the failure links for the trie (Aho-Corasick automaton).

6. Process each query:

   a. For type 1: update the victim's value and possibly update name_to_max[s].

   b. For type 2: process the string q through the automaton, tracking the maximum value.

The key challenge is to handle the type 1 queries efficiently and the type 2 queries efficiently.

But given the time constraints, we need to proceed with this approach, even if it's not optimal.

But how to track the victims and their names.

First, when building the trie, each name is added once. For each name s, we can track the max value as the maximum of the initial 0 values. But since the initial values are all 0, name_to_max[s] will be 0 for each s.

For each victim, their initial value is 0.

For type 1 queries, when a victim's value is updated, we need to check if their name's current max is affected.

But how to track all victims with the same name.

Thus, for each name s, we need to maintain a list of the victims with that name and their current values.

This requires:

- A dictionary name_to_victims: s -> list of indices (victim indices) with name s.

- An array values: values[i] is the current value of victim i.

- A dictionary name_to_max: s -> current max value for s.

Initially, values[i] = 0 for all i. name_to_max[s] is 0 for all s.

For each type 1 query:

   i is given as 1-based, so idx = i - 1.

   x is the new value.

   s = names[idx]

   old_val = values[idx]

   new_val = x

   values[idx] = new_val

   current_max = name_to_max[s]

   if new_val > current_max:

       name_to_max[s] = new_val

   else if old_val == current_max:

       # Need to recompute the max for s.

       max_val = max( values[i] for i in name_to_victims[s] )

       name_to_max[s] = max_val

   # else, do nothing.

Thus, the worst case for a type 1 query is O(k) time, where k is the number of victims with name s. This could be O(n) time for a name with all victims. But given the problem's constraints, this may not be feasible.

But given the time limits, perhaps this is the only way to proceed, and the problem expects this solution.

Now, the implementation.

First, build the trie.

The trie structure:

Each node has a dictionary of children, a failure link, and a name (if it's the end of a name).

The Aho-Corasick automaton's failure links are built using BFS.

Then, for each query of type 2:

   current_node = root

   max_val = -1

   for c in q:

       # Move to the child node with c, following failure links if necessary.

       while current_node is not None and c not in current_node.children:

           current_node = current_node.failure

       if current_node is None:

           current_node = root

       else:

           current_node = current_node.children.get(c, root)

       # Now, traverse the failure chain and check for names.

       temp_node = current_node

       while temp_node != root:

           if temp_node.name is not None:

               current_max = name_to_max.get(temp_node.name, -1)

               if current_max > max_val:

                   max_val = current_max

           temp_node = temp_node.failure

       # Also check the root node.

       if temp_node.name is not None:

           current_max = name_to_max.get(temp_node.name, -1)

           if current_max > max_val:

               max_val = current_max

   if max_val == -1:

       print(-1)

   else:

       print(max_val)

This code for the query processing would process each character in q and traverse the failure chain.

But in the worst case, for each character, the failure chain traversal could take O(L) time, leading to O(L^2) time per query, which is not feasible.

Thus, this approach may not pass the time constraints.

But given the problem's difficulty, perhaps this is the intended solution.

Thus, the final code would involve building the Aho-Corasick automaton and handling the type 1 and type 2 queries as described.

Now, let's proceed to write the code.

First, read the names, build the trie, then build the failure links.

But in Python, building a trie with failure links can be done with a BFS.

Implementing the trie:

class TrieNode:
    __slots__ = ['children', 'failure', 'name']

    def __init__(self):
        self.children = {}
        self.failure = None
        self.name = None

root = TrieNode()

For each name in the database:

names = []
name_to_victims = defaultdict(list)
for i in range(n):
    s = input().strip()
    names.append(s)
    # Add to trie
    node = root
    for c in s:
        if c not in node.children:
            node.children[c] = TrieNode()
        node = node.children[c]
    # Mark this node as the end of s
    if node.name is None:
        node.name = s
    else:
        # This can happen if multiple victims have the same name. But in the trie, the node.name is set once.
        # However, since the name is the same, the node.name remains the same, and name_to_max[s] will track the max of all victims with name s.
        pass
    name_to_victims[s].append(i)

Then, build the failure links using BFS.

queue = deque()
root.failure = None
queue.append(root)

while queue:
    current_node = queue.popleft()
    for char, child in current_node.children.items():
        if current_node == root:
            child.failure = root
        else:
            p = current_node.failure
            while p is not None:
                if char in p.children:
                    child.failure = p.children[char]
                    break
                p = p.failure
            if p is None:
                child.failure = root
        queue.append(child)

        # Also, merge the output
        # For this problem, we don't need to collect all outputs, since we'll traverse the failure links during queries.

But during the query processing, for each node, we need to traverse the failure links to collect all possible names.

But this is time-consuming.

Thus, to optimize, during the BFS, for each node, we can precompute the list of all names that end at this node or any of its failure links. But this is not feasible for dynamic updates.

Thus, during the query processing, we must traverse the failure chain for each node visited.

Thus, the code for type 2 queries is as described earlier.

Now, the code for type 1 queries:

values = [0] * n
name_to_max = defaultdict(int)
for s in name_to_victims:
    name_to_max[s] = 0  # Initially all are 0

for each type 1 query:

i, x = map(int, parts[1:])
idx = i-1
s = names[idx]
old_val = values[idx]
new_val = x

values[idx] = new_val

current_max = name_to_max[s]

if new_val > current_max:
    name_to_max[s] = new_val
elif old_val == current_max:
    # Recompute the max for s
    max_val = max(values[v] for v in name_to_victims[s])
    name_to_max[s] = max_val

Now, putting it all together.

But this code may not pass the time constraints for large n and m, especially when there are many type 1 queries requiring recomputing the max.

But according to the problem's examples and the time constraints, this is the best possible approach.

Testing against sample input 1.

```python
import sys
from collections import deque, defaultdict


def main(input_stream, output_stream):
    input = input_stream.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr +=1
    
    names = []
    for _ in range(n):
        names.append(input[ptr])
        ptr +=1
    
    class TrieNode:
        __slots__ = ['children', 'failure', 'name']
        def __init__(self):
            self.children = {}
            self.failure = None
            self.name = None
    
    root = TrieNode()
    name_to_victims = defaultdict(list)
    
    # Build the trie
    for idx, s in enumerate(names):
        node = root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        if node.name is None:
            node.name = s
        name_to_victims[s].append(idx)
    
    # Build failure links using BFS
    queue = deque([root])
    root.failure = None
    while queue:
        current_node = queue.popleft()
        for char, child in current_node.children.items():
            if current_node == root:
                child.failure = root
            else:
                p = current_node.failure
                while p is not None:
                    if char in p.children:
                        child.failure = p.children[char]
                        break
                    p = p.failure
                if p is None:
                    child.failure = root
            queue.append(child)
    
    # Initialize values and name_to_max
    values = [0] * n
    name_to_max = defaultdict(int)
    for s in name_to_victims:
        name_to_max[s] = 0  # Initially all 0
    
    output = []
    for _ in range(m):
        query = input[ptr]
        ptr +=1
        if query == '1':
            i = int(input[ptr]) - 1  # convert to 0-based
            ptr +=1
            x = int(input[ptr])
            ptr +=1
            s = names[i]
            old_val = values[i]
            values[i] = x
            current_max = name_to_max[s]
            if x > current_max:
                name_to_max[s] = x
            elif old_val == current_max:
                max_val = max(values[v] for v in name_to_victims[s])
                name_to_max[s] = max_val
        else:
            q = input[ptr]
            ptr +=1
            current_node = root
            max_val = -1
            for c in q:
                while current_node is not None and c not in current_node.children:
                    current_node = current_node.failure
                if current_node is None:
                    current_node = root
                else:
                    current_node = current_node.children.get(c, root)
                # Traverse failure links
                temp_node = current_node
                while temp_node != root:
                    if temp_node.name is not None:
                        current_max = name_to_max.get(temp_node.name, -1)
                        if current_max > max_val:
                            max_val = current_max
                    temp_node = temp_node.failure
                # Check root node
                if temp_node.name is not None:
                    current_max = name_to_max.get(temp_node.name, -1)
                    if current_max > max_val:
                        max_val = current_max
            if max_val == -1:
                output.append("-1")
            else:
                output.append(str(max_val))
    
    print('\n'.join(output), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 15
a
ab
ba
b
a
ba
2 aa
1 4 4
2 bbb
1 2 1
1 2 18
2 b
2 c
1 6 10
2 aba
2 abbbba
1 2 12
2 bbaaab
1 1 11
1 5 5
2 baa
""",
            "output": \
"""\
0
4
4
-1
18
18
12
11
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

</think>

```python
import sys
from collections import deque, defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr +=1
    
    names = []
    for _ in range(n):
        names.append(input[ptr])
        ptr +=1
    
    class TrieNode:
        __slots__ = ['children', 'failure', 'name']
        def __init__(self):
            self.children = {}
            self.failure = None
            self.name = None
    
    root = TrieNode()
    name_to_victims = defaultdict(list)
    
    # Build the trie
    for idx, s in enumerate(names):
        node = root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        if node.name is None:
            node.name = s
        name_to_victims[s].append(idx)
    
    # Build failure links using BFS
    queue = deque([root])
    root.failure = None
    while queue:
        current_node = queue.popleft()
        for char, child in current_node.children.items():
            if current_node == root:
                child.failure = root
            else:
                p = current_node.failure
                while p is not None:
                    if char in p.children:
                        child.failure = p.children[char]
                        break
                    p = p.failure
                if p is None:
                    child.failure = root
            queue.append(child)
    
    # Initialize values and name_to_max
    values = [0] * n
    name_to_max = defaultdict(int)
    for s in name_to_victims:
        name_to_max[s] = 0  # Initially all 0
    
    output = []
    for _ in range(m):
        query = input[ptr]
        ptr +=1
        if query == '1':
            i = int(input[ptr]) - 1  # convert to 0-based
            ptr +=1
            x = int(input[ptr])
            ptr +=1
            s = names[i]
            old_val = values[i]
            values[i] = x
            current_max = name_to_max[s]
            if x > current_max:
                name_to_max[s] = x
            elif old_val == current_max:
                max_val = max(values[v] for v in name_to_victims[s])
                name_to_max[s] = max_val
        else:
            q = input[ptr]
            ptr +=1
            current_node = root
            max_val = -1
            for c in q:
                while current_node is not None and c not in current_node.children:
                    current_node = current_node.failure
                if current_node is None:
                    current_node = root
                else:
                    current_node = current_node.children.get(c, root)
                # Traverse failure links
                temp_node = current_node
                while temp_node != root:
                    if temp_node.name is not None:
                        current_max = name_to_max.get(temp_node.name, -1)
                        if current_max > max_val:
                            max_val = current_max
                    temp_node = temp_node.failure
                # Check root node
                if temp_node.name is not None:
                    current_max = name_to_max.get(temp_node.name, -1)
                    if current_max > max_val:
                        max_val = current_max
            if max_val == -1:
                output.append("-1")
            else:
                output.append(str(max_val))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
```
