<think>
Okay, let's try to understand this problem. So, the task is to find the minimal number of passwords we need to select such that, regardless of which password is the admin's, at least one of our selected passwords will be equivalent to it. The equivalence here is defined as either direct (they share a common character) or indirect through other passwords.

Hmm, the equivalence here sounds a lot like a graph problem. Each password is a node, and there's an edge between two nodes if they share a common character. Then, the equivalence would form connected components. So, two passwords are in the same component if there's a path connecting them via shared characters. But wait, the equivalence can also be through intermediate passwords. So, the problem reduces to finding the connected components based on the characters present in the passwords.

Wait, maybe another way to model this. Each password is a set of characters. For the equivalence, any two passwords that share at least one character are connected directly. But also, if there's a chain of passwords where each consecutive pair shares a character, they're all in the same component. So the connected components are determined by the union of all the character sets of the passwords in the component. Because if password A has characters {a}, password B has {b}, and password C has {a,b}, then A is connected to C, B is connected to C, so all three are in the same component. So the component is determined by the union of all the characters of the passwords in it.

Wait, but how do we model the connectedness here? The key insight is that two passwords are in the same component if their character sets are connected via overlapping characters. So, the problem can be modeled as a graph where each node is a password, and edges exist between passwords that share at least one character. Then, the connected components of this graph would represent equivalence classes. But building such a graph is O(n^2) in the worst case, which is not feasible for n up to 2e5.

That's a problem. Because with n=2e5, we can't check all pairs. So we need a smarter way to compute the connected components.

Another approach: think of each character as a node. Then, each password connects all the characters in it. So for a password like "abc", the characters a, b, c are all connected to each other. So the idea is that the characters form a graph where any two characters appearing in the same password are connected. Then, the connected components of the characters determine the equivalence of the passwords. Each password is part of the component of its characters, which are all connected. Wait, maybe this is the right approach.

Wait, for example, if two passwords share a common character, their character sets are in the same connected component. So the passwords' character sets are part of the same connected component of characters. Therefore, the equivalence between passwords can be determined by the connected components of the characters. Because if two passwords have any characters in the same component, then those passwords are in the same equivalence class.

So here's the idea: For each password, collect all the characters in it. These characters form a group where each is connected to others via being in the same password. Then, all passwords that have characters in the same group (connected component of characters) belong to the same equivalence class. So the number of equivalence classes for the passwords is the number of connected components of the character graph. Wait, no. Because a password may have multiple characters, each of which is part of the same component. So the passwords are part of the same equivalence class if their character sets share a connected component in the character graph.

Wait, maybe each password contributes to connecting all its characters. For example, password "ab" connects 'a' and 'b'. Another password "bc" connects 'b' and 'c'. So 'a', 'b', 'c' are in the same component. Then, any password that has any of these characters is part of the same equivalence class. So the equivalence classes of the passwords are determined by the connected components of the characters. So all passwords that have at least one character in a certain connected component of the character graph are in the same equivalence class.

Wait, but that's not quite right. Because if two passwords have characters that are in the same connected component of the character graph, then they are in the same equivalence class. Because, via the characters, there's a path between the two passwords. So for example, if password A has 'a', and password B has 'b', and 'a' and 'b' are connected through some other passwords, then A and B are in the same equivalence class.

So the equivalence classes of the passwords are determined by the union of the connected components of their characters. So the problem reduces to building a graph where each node is a character, and two characters are connected if there exists a password that contains both. Then, each connected component of characters defines an equivalence class. Then, all passwords that have at least one character in a connected component belong to the same equivalence class. Because any two passwords in that component can be connected via the characters.

Wait, but maybe I should model it as the connected components of the characters. Let's see:

Each password is a collection of characters. For each password, all the characters in it are connected to each other (since they are in the same password, which implies that any two characters in the password are connected). So for each password, we can merge all the characters in it into a single group. Then, the connected components of the characters are the unions of all such merges.

Once we have the connected components of the characters, then each password belongs to exactly one equivalence class, which is the connected component of any of its characters (since all its characters are in the same connected component). Then, all passwords that share any character in the same connected component are in the same equivalence class.

Wait, but a password's characters are all in the same connected component. Because when we process the password, we merge all its characters. So if a password has characters a, b, c, then in the character graph, a, b, c are all connected. So when building the character graph, processing each password would connect all its characters.

So the steps are:

1. For each password, take all characters in it. For each such set of characters, connect all of them into a single group (using Union-Find data structure). For example, if the password has characters a, b, c, then we union a and b, then a and c, etc. But that's O(k^2) per password, where k is the number of characters in the password. But since the maximum password length is 50, this is manageable. Alternatively, for each password, we can take all characters and union them with the first character, which reduces the operations to O(k) per password.

Yes, that's better. For each password, take the first character, then union all other characters in the password with the first. This way, all characters in the password are connected through the first character, forming a single connected component. So for example, in a password with a, b, c, first union a and b, then a and c. Then a, b, c are in the same group. This way, each password is processed in O(k) time, where k is the length of the password.

Once all characters are processed, the connected components of the characters represent the equivalence classes. Each password belongs to the connected component of its characters (since all are in the same component). Then, all passwords that have at least one character in the same connected component are in the same equivalence class.

Therefore, all passwords in the same equivalence class (i.e., their characters' connected component) form a group. The problem now is to find the minimal number of passwords to select such that, for every possible connected component (i.e., every possible equivalence class), if there is at least one password in that component, then at least one password from that component is selected. Because the admin's password is in one of the components, and to cover all possibilities, we need to select one password from each component. Wait, no. Because the admin's password could be any of the passwords. So the hacker needs to select a set of passwords such that, no matter which password is the admin's, at least one of the selected passwords is in the same equivalence class as the admin's password.

So the problem reduces to: each password is part of a group (the connected component of its characters). The groups are the equivalence classes. We need to select the minimal number of passwords such that every possible group that contains at least one password is covered. Because if a group has any password, then the admin's password could be in that group, and we need to have at least one password from that group in our selected set. Therefore, the minimal number of passwords required is equal to the number of connected components in the character graph that have at least one password in them.

Wait, but how does that work? Let's see:

Each connected component in the character graph corresponds to a group. All passwords that have at least one character in that group belong to this group. So each password is part of exactly one group (since all their characters are in the same connected component). Therefore, the number of groups is equal to the number of connected components in the character graph. But we need to count the number of connected components that have at least one password. Because if a connected component in the character graph has no passwords (which is impossible, because all passwords contribute to the character graph), but since each password has at least one character, each password's characters are part of some connected component. So every password is part of exactly one group (the connected component of its characters). So the number of groups is the number of connected components in the character graph. But wait, what if a connected component in the character graph has multiple passwords? Then all those passwords are in the same group. So the minimal number of passwords needed is the number of such groups. Because selecting one password from each group ensures that, regardless of which group the admin's password is in, the selected set will have a password from that group.

So the answer is the number of connected components in the character graph where there is at least one password that belongs to that component.

Wait, but perhaps the same connected component in the character graph can have multiple passwords. But regardless, each password in that component is in the same group. So to cover all groups, the hacker needs to select one password per group. Therefore, the minimal number is the number of connected components in the character graph that have at least one password.

But how do we track which connected components in the character graph have at least one password?

Wait, the connected components in the character graph are built by processing all the passwords. For example, if a password has characters a and b, then a and b are connected. If another password has c and d, they are connected. Then, if a password has a and c, then a, b, c, d are all in the same component. So each password's characters are part of the connected components. So all passwords are part of the groups formed by the connected components of the character graph. Therefore, the number of groups is equal to the number of connected components in the character graph. Therefore, the minimal number of passwords needed is the number of connected components in the character graph.

Wait, but no. For example, in the first sample input:

4
a
b
ab
d

The characters are a, b, d. Let's see:

- The password "a" connects a (only character). So a's component is {a}.
- "b" connects b → {b}.
- "ab" connects a and b. So merging a and b's components into one. Now the component is {a, b}.
- "d" connects d → {d}.

So the connected components of the character graph are {a, b}, {d}. So the number of connected components is 2. Therefore, the answer is 2, which matches the sample output.

In the second example:

3
ab
bc
abc

Each password connects their characters. Let's process them:

- "ab": connects a and b. Component {a, b}.
- "bc": connects b and c. Now, component {a, b, c}.
- "abc": all characters a, b, c are already connected. So component remains {a, b, c}.

So all characters are in the same component. Thus, there's only one connected component. The answer is 1.

Third example: one password. Its characters are all connected. So the component is size 1. Answer 1.

So the approach is correct. So the problem reduces to:

1. Build a Union-Find (disjoint set) structure for the 26 lowercase letters.
2. For each password, process all its characters, connecting them (all characters in the password are connected to each other).
3. Then, for each password, find the root of any of its characters (since they are all in the same component).
4. Collect all the unique roots from all passwords. The count of these unique roots is the minimal number of passwords needed.

Wait, that's exactly the case. Because each password's characters are in a connected component. So the root for any of the password's characters is the same. Then, the set of all roots from all passwords is the set of connected components that have at least one password. Because each password contributes the root of its component. So the number of unique roots across all passwords is the number of connected components that have at least one password. So the answer is the size of this set.

But how do we compute this? For example, even if a password has multiple characters, we only need to take the root of any one of them, since they are all in the same component.

So the steps are:

- Initialize the Union-Find structure for 26 letters.
- For each password, iterate through its characters. For each password, take all the characters and union them together. To do this efficiently, for each password, take the first character, then union all other characters in the password with the first.
- Then, collect all the roots of the first character of each password. Because each password is part of the component of its first character (after processing). Wait, but after processing all passwords, the first character's root may have changed. So, for each password, we can pick any character (since all are in the same component), get its root, and add that to a set. The size of the set is the answer.

Wait, no. Because the password's characters are all in the same component. So for any password, all its characters' roots are the same. So for example, if the password is "abc", after processing, a's root is same as b's and c's. So when we process the password, we can take any character's root (e.g., a's root) and add it to the set. So for each password, we can pick any character (like the first), find its root, and add that to a set. Then, the number of elements in the set is the number of connected components that have at least one password, which is the answer.

Yes. Because each password contributes exactly one root (since all its characters are in the same component). So for each password, the root of its component is the same as any of its characters. So, the number of unique roots across all passwords is the number of connected components that have passwords. Thus, the answer is the size of this set.

But wait, what about passwords that have overlapping characters but are processed in different orders? For example, a password "ab" and then "ba". But the union operations would have connected all their characters regardless.

So the steps are:

- Initialize the Union-Find structure for the 26 letters.
- For each password, process all its characters, connecting them. For each password, iterate through the characters, and for each character after the first, union it with the first character. So all characters in the password are in the same component.
- Then, for each password, take any character (say, the first) and find its root. Add this root to a set.
- The size of the set is the answer.

But wait, what if two different passwords have the same root? For example, two passwords in the same component. Then, adding their roots (same) to the set will count as one. Thus, the set's size is the number of connected components that have at least one password. Which is the answer.

So the answer is the number of distinct roots of the first character of each password, after processing all unions. Because each password's first character is in a component, and the root is the same as any other characters in the password. So each password's root is unique per component. Thus, the count of unique roots across all passwords is the number of components.

So, the algorithm is:

1. Read all passwords.
2. For each password, process its characters into the Union-Find structure.
3. For each password, take the root of any of its characters (e.g., first character) and add to a set.
4. The size of the set is the answer.

Now, let's test this with the sample inputs.

First sample:

Passwords are "a", "b", "ab", "d".

Processing each password:

For "a": first char is 'a'. No other chars. So, 'a' is in its own set.

For "b": first char is 'b'. Own set.

For "ab": first char 'a'. Process other chars: 'b' is unioned with 'a'. So now 'a' and 'b' are in the same set.

For "d": own set.

Then, the roots for each password's first char:

- "a" → 'a's root (let's say 'a').
- "b" → 'b's root (after processing "ab", 'b's root is 'a'? Wait, no. Let me think.

Wait, the union-find structure is for the characters. Let's track how the unions happen.

When processing password "ab":

- The first character is 'a'. Then, for each other character (just 'b'), we union 'a' and 'b'. So, during the union, the parent of 'b' becomes 'a', or vice versa depending on the union by rank. But in any case, after the union, 'a' and 'b' are in the same set. Let's say that 'a' becomes the parent of 'b'.

Then, when processing password "b", the first character is 'b'. The root of 'b' is 'a'. So when processing "b", the root is 'a'.

But wait, the password "b" is processed first. Let's re-examine the order.

Sample input 4:

1. "a" → process. No other chars. So 'a' is in own set.

2. "b" → process. No other chars. 'b' is in own set.

3. "ab" → process. First char is 'a'. Then 'b' is unioned with 'a'. Now, 'b' is connected to 'a'.

4. "d" → own set.

Now, for each password, the first character's root:

1. "a" → 'a's root is 'a'.

2. "b" → 'b's root is 'a' (after union with 'a' in the third password).

Wait, no. Wait, the password "b" is processed before the "ab" password. Let's see:

Processing "a": 'a' is parent of itself.

Processing "b": 'b' is parent of itself.

Processing "ab": first character is 'a'. For the other character 'b', we union 'a' and 'b'. So during the union, which one becomes the parent? Depending on the union by rank or size.

Assuming that in the Union-Find data structure, when unioning two elements, the parent is chosen based on the size (or rank). Let's say that in this case, 'a' and 'b' have the same rank. So when we union them, 'a' becomes the parent of 'b'.

So after processing "ab", 'b's parent is 'a'.

Then, when processing the password "b", which is the second password. When processing this password, the code first takes the first character 'b', and then unions all other characters (none) with 'b'. So the password "b" is processed by processing the first character 'b', which at that time is its own parent (since the union with 'a' hasn't happened yet). Wait no: the password "b" is processed before the password "ab". So during the processing of "b", we are adding the characters of "b" (only 'b'). So the code unions all other characters in the password (there are none) with the first character. So the code for "b" would process only 'b', and since there's no other characters, no unions are done. So after processing "b", 'b' is in its own component.

Then, the third password "ab" is processed. For this, the first character is 'a'. The code then unions 'a' and 'b' (the other character). So during this step, 'b' is merged into 'a's component. So now, 'a' is the root of 'a' and 'b'.

Then, when we process each password to collect their roots:

Password "a": root is 'a'.

Password "b": when we take 'b' and find its root, which is 'a' (since after the union, 'b's parent is 'a').

Password "ab": 'a' is root.

Password "d": root is 'd'.

So the set of roots is {'a', 'd'}, size 2. Which matches the sample output.

So the approach works.

Another example: the second sample input.

Passwords are "ab", "bc", "abc".

Processing "ab": first char 'a'. Union 'a' and 'b'. 'a' and 'b' are in same component.

Processing "bc": first char 'b'. Other characters are 'c'. Union 'b' and 'c'. Now, 'a', 'b', 'c' are in the same component.

Processing "abc": first char 'a'. Other characters are 'b' and 'c'. 'a' is already in the same component as 'b' and 'c'. So no new unions, but when processing, we union 'a' with 'b' (already same), then 'a' with 'c' (same as 'b' and 'c').

Then, the roots of each password's first character:

"ab" → 'a' (root is 'a' if using union by size and 'a' is the root of the component).

Wait, after processing all three passwords:

After "ab", a and b are connected.

After "bc", 'b' and 'c' are connected. So 'a', 'b', 'c' are connected.

After "abc": all characters are already connected.

So when we collect the roots for each password:

For "ab": first char is 'a', root is the root of the component (a).

For "bc": first char is 'b', which's root is a.

For "abc": first char is 'a', root is a.

So the set is {a}, size 1. Correct.

So the approach works.

So the steps are:

- For each password, process the characters, union them into a connected component.

- Then, for each password, find the root of its first character (since all characters are in the same component as the first character).

- The answer is the number of unique roots found.

Now, let's think about the implementation.

The Union-Find (Disjoint Set Union) data structure needs to handle 26 elements (lowercase letters). Each element is a character. So we can map 'a' to 0, 'b' to 1, etc., to use integers for the DSU.

The DSU operations are path compression and union by rank (or size) for efficiency.

Processing each password:

For each password, take the set of unique characters. Because if a password has duplicate characters, it's redundant to process them multiple times. For example, password "aaa" is just 'a', processing it once. So for each password, first get the unique characters. For example, for "ab", the unique characters are {'a', 'b'}.

Then, for each password's unique characters:

If the password has at least one character, take the first character. Then, for each other character in the set, union it with the first character.

This way, all characters in the password are in the same component.

Once all unions are done, for each password, take the first character (or any character) and find its root. Add that root to a set. The size of the set is the answer.

So, the steps in code:

Read n.

Read n passwords.

For each password:

   unique_chars = sorted list of unique characters in the password (but order doesn't matter, except for choosing the first)

   if no characters (but per problem statement, passwords are non-empty), so process each password's unique_chars.

   first_char = unique_chars[0]

   for char in unique_chars[1:]:

      union(first_char, char)

Then, collect the roots of the first_char of each password (after all unions).

The code can be written as:

Initialize DSU for 26 letters.

roots = set()

for each password in passwords:

   chars = sorted(list(set(password)))  # sorted for consistency, but any order is ok.

   if not chars:

      continue  # but problem says passwords are non-empty.

   first = chars[0]

   for c in chars[1:]:

      dsu.union(ord(first) - ord('a'), ord(c) - ord('a'))

for each password in passwords:

   chars = list(set(password))  # get unique chars

   first = chars[0]

   root = dsu.find(ord(first) - ord('a'))

   roots.add(root)

answer is len(roots)

Wait, but when we process the password again in the second loop, we have to take the unique characters again. For example, a password like "aabba" would have unique chars {'a', 'b'}, so first is 'a'. So the root is 'a's root.

But in the second loop, for each password, we need to collect the root of any of its characters. However, to get the unique characters again, perhaps it's better to process the password again, but this time just take any character (like the first) and get its root.

But storing all the passwords could be memory-intensive if n is 2e5 and each password is up to 50 characters, but the total characters is 1e6, which is manageable.

Alternatively, during the first pass (processing unions), we can also collect the unique characters of each password and store them. Then, in the second pass, we can process those stored unique characters. But that would require storing for each password the set of unique characters, which is O(n * k), where k is up to 26 (since a password can have up to 26 unique letters). But 2e5 * 26 is 5.2e6, which is manageable.

But perhaps the better approach is to process the password once, extract the unique characters, and store them for later.

But for code efficiency, perhaps it's better to process each password once, extract the unique characters, and process the unions, and then in the second loop, process each password's unique characters again.

But for the code, perhaps we can process each password in the first loop to extract the unique characters and process the unions, and then store the first character of each password's unique set, then in the second loop, just use those stored first characters.

But for code simplicity, perhaps during the first loop, for each password, we can store the first character of its unique set. Then, in the second loop, we can process those stored first characters.

Wait, but during the first loop, the unions may affect the roots of the characters. For example, when a password is processed, the first character's root may change after subsequent unions. So during the first loop, processing a password's characters and storing the first character's root then would not be correct, as later passwords may merge the components.

Therefore, the correct approach is to process all unions first, and then for each password, process its unique characters again to find the root of the first character (after all unions have been completed).

Thus, the code steps:

Read all passwords, process each to get their unique characters, then:

Process each password's unique characters to perform unions.

Then, for each password, process their unique characters again (or stored from the first step) to find the root of the first character.

But this would require storing the unique characters for each password.

Alternatively, during the first pass, for each password, extract the unique characters and process the unions, but not store them. Then, during the second pass, re-process each password to extract unique characters again, take the first character, find its root, and add to the set.

But this would process each password twice. For n=2e5, and each password up to 50 characters, this is acceptable as O(2*2e5*50) = 2e7 operations.

But extracting the unique characters each time may be time-consuming. So perhaps during the first loop, we can store the unique characters for each password.

But how?

Alternative code steps:

passwords = []

for _ in range(n):

    s = input().strip()

    unique_chars = list(sorted(set(s)))  # sorted is optional, but ensures that the first char is the same every time.

    passwords.append(unique_chars)

    first = unique_chars[0]

    for c in unique_chars[1:]:

        dsu.union(ord(first) - ord('a'), ord(c) - ord('a'))

roots = set()

for unique_chars in passwords:

    if not unique_chars:

        continue

    first = unique_chars[0]

    root = dsu.find(ord(first) - ord('a'))

    roots.add(root)

print(len(roots))

This would work. Because during the first loop, for each password, we extract the unique characters, process the unions, and store the unique_chars list. Then, in the second loop, we process each password's unique_chars again, take the first character, find its root (after all unions have been done), and add to the set.

But the problem is that during the first loop, the code for processing the unions uses the first character (unique_chars[0]) and unions all others with it. Then, during the second loop, the same unique_chars list is used, so the first character is the same. Thus, the code correctly captures the root of the first character (after all unions) for each password.

Yes. So this code would work.

Now, let's test this with the sample inputs.

First sample:

Passwords are:

"a" → unique_chars is ['a']

"b" → ['b']

"ab" → sorted unique is ['a', 'b']

"d" → ['d']

Processing unions:

First password: no unions. a is in own set.

Second: b in own set.

Third: a and b are united.

Fourth: d in own set.

Then, for each password's unique_chars:

For "a", first is 'a', root is a's root (after all unions, which is a's root). Since a and b were united, during the third password processing, a and b are in the same component. So after all processing, a's root may be a or b, depending on how the DSU is implemented.

Wait, but the DSU's find function returns the root with path compression. So for example, when the third password is processed, 'a' and 'b' are united. Let's say that during the union, 'a' becomes the parent of 'b'. Then, when processing the second password (which is 'b'), during the first loop, the code would process 'b' (but in that password's processing, there are no other characters, so no unions are done). Then, during the second loop, the password's unique_chars is ['b'], so first character is 'b'. The find function for 'b' would return 'a' (after path compression). So the root for 'b' is 'a', which is the same as the root for 'a'.

Thus, the roots for the first password (a) is 'a's root (a), the second (b) is a, the third (a and b) is a, the fourth (d) is d. So the set is {a, d}, size 2.

Thus, the code works.

Another example: third sample input with one password "codeforces". The unique_chars are the sorted list of unique letters in "codeforces". Let's say sorted gives ['c', 'd', 'e', 'f', 'o', 'r', 's']. The first character is 'c'. All other characters are united with 'c'. So all are in the same component. Then, in the second loop, the first character is 'c', which's root is the root of the component. So the set has one element. Thus, answer 1.

Yes.

Now, considering the DSU implementation. The DSU needs to handle 26 elements (0 to 25). So the code for DSU can be as follows:

class DSU:

    def __init__(self, size):

        self.parent = list(range(size))

        self.rank = [1] * size

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        x_root = self.find(x)

        y_root = self.find(y)

        if x_root == y_root:

            return

        if self.rank[x_root] < self.rank[y_root]:

            self.parent[x_root] = y_root

        else:

            self.parent[y_root] = x_root

            if self.rank[x_root] == self.rank[y_root]:

                self.rank[x_root] += 1

This is a standard DSU with path compression and union by rank.

But since the letters are only 26, the size is 26.

Now, the code steps:

Read n.

Read n passwords, for each, extract unique characters, sorted, and process the unions.

Then, collect the roots of the first character of each password's unique characters.

Now, the code should be efficient. For n=2e5 and passwords up to 50 characters, the code is O(n * k), where k is up to 50 (for each password, processing the characters). But since the total characters is 1e6, the total time is acceptable.

Now, the code must be written in Python, with reading from input and output.

But wait, the code must process all the passwords, but the passwords may have duplicate characters, but we need to process the unique characters. So for each password, converting to a set and then sorted list is O(m) where m is the password length, but the total sum of m is 1e6, so acceptable.

But in Python, the code for each password would be:

s = input().strip()

unique_chars = sorted(list(set(s)))

But sorted is O(k log k), where k is the number of unique characters. For each password, the maximum k is 26, so O(26 log 26) is negligible. Thus, this step is acceptable.

So the code is feasible.

Now, let's code this.

The code will:

- Read n.

- Read n lines, each stripped.

- For each password, process the unique characters.

- For each password's unique characters, union them all with the first character.

- Then, collect the roots of each password's first character.

- The answer is the size of the roots set.

Now, code:

class DSU:

    def __init__(self, size):

        self.parent = list(range(size))

        self.rank = [1]*size

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        x_root = self.find(x)

        y_root = self.find(y)

        if x_root == y_root:

            return

        if self.rank[x_root] < self.rank[y_root]:

            self.parent[x_root] = y_root

        else:

            self.parent[y_root] = x_root

            if self.rank[x_root] == self.rank[y_root]:

                self.rank[x_root] += 1

n = int(input())

dsu = DSU(26)

passwords = []

for _ in range(n):

    s = input().strip()

    unique_chars = sorted(list(set(s)))

    passwords.append(unique_chars)

    if not unique_chars:

        continue

    first = unique_chars[0]

    for c in unique_chars[1:]:

        dsu.union(ord(first) - ord('a'), ord(c) - ord('a'))

roots = set()

for unique_chars in passwords:

    if not unique_chars:

        continue

    first = unique_chars[0]

    root = dsu.find(ord(first) - ord('a'))

    roots.add(root)

print(len(roots))

But wait, the problem statement says that passwords are non-empty, so the 'if not unique_chars' check is redundant. But including it is safe.

Testing this code with the samples.

Sample 1:

4

a

b

ab

d

Passwords:

['a'], ['b'], ['a','b'], ['d']

Processing unions:

For ['a'], no other chars.

For ['b'], no other.

For ['a','b'], union a and b.

For ['d'], no other.

Then, for each password's unique_chars, take first and find root.

For 'a' → root is a's root. After union, a and b are connected. So for the first password, the root is a's root. After union, when we find(a), since during the third password processing, we unioned a and b, but during the first two passwords, a and b were separate. But the code processes all unions first. So after all processing, 'a' and 'b' are in the same component.

So for the first password, first char is 'a', root is find(a) → which after union, could be the same as a's root. Let's say the DSU's union by rank:

Processing the third password:

unique_chars is ['a', 'b'], sorted.

First is 'a', then 'b'.

dsu.union(a (0), b (1)):

x_root = 0, y_root = 1.

Ranks are 1 and 1. So x's rank is not less than y's. So y's parent becomes x's. So parent[1] = 0. rank[0] becomes 2.

So when find(b) is called, it returns 0.

Thus, for the second password (['b']), first char is 'b'. find(1) returns 0.

So the roots set will have:

For the first password: 0.

Second: 0.

Third: 0.

Fourth: 3 (d is 3).

So the roots set is {0,3} → size 2. Correct.

Sample 2:

3

ab → sorted unique ['a','b']

bc → sorted unique ['b','c']

abc → sorted unique ['a','b','c']

Processing unions:

First password: a and b are united.

Second: b and c are united. So, in DSU:

Initially, a and b are in same component (0).

Processing second password: first char is 'b', which is in component 0. Then 'c' is added. So union(0, 2). Now, the component is 0 (a, b, c).

Third password: first char 'a'. Other chars are 'b' and 'c'. They are already in the same component.

So all three passwords are in component 0. Thus, the roots set is {0}, size 1.

Sample 3: 1 password, "codeforces". The unique chars sorted would be ['c','d','e','f','o','r','s'].

Processing all these characters: union them with 'c'.

Thus, all are in the same component. The roots set has one element.

Thus, code works.

Now, code is correct and efficient. The DSU operations are O(alpha(26)), which is O(1). Processing each password is O(k), with k up to 50, and total sum of k is 1e6, which is acceptable.

Thus, this is the optimal approach.
</think>

```python
class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

n = int(input())
dsu = DSU(26)
passwords = []

for _ in range(n):
    s = input().strip()
    unique_chars = sorted(list(set(s)))
    passwords.append(unique_chars)
    if not unique_chars:
        continue
    first = ord(unique_chars[0]) - ord('a')
    for c in unique_chars[1:]:
        dsu.union(first, ord(c) - ord('a'))

roots = set()
for unique_chars in passwords:
    if not unique_chars:
        continue
    first = ord(unique_chars[0]) - ord('a')
    roots.add(dsu.find(first))

print(len(roots))
```