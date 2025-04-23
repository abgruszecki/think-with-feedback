<think>
Okay, so I need to find the lexicographically maximum subsequence of a given string. Hmm, what's a subsequence here? Oh right, it's a sequence that can be derived by deleting some or no elements without changing the order. So the problem is to choose characters in order such that the resulting string is the largest possible lex order.

The key is to maximize the lex order. Lex order compares characters one by one. So the first character should be as large as possible. Then, for each subsequent position, again choose the largest possible remaining character, but considering the remaining positions.

Wait, but how to do this efficiently? Because if the string is up to 1e5 characters long, we can't do anything that's O(n^2), that's way too slow.

Let me think. Let's consider the example first. For "ababba", the output is "bbba". Let's see why. The original string is a, b, a, b, b, a. The maximum subsequence would take the largest possible characters first. The largest character here is 'b's. There are three 'b's. But the output is four characters. Wait, the output is four 'b's? Wait, no. Wait, the input is ababba. So the characters are positions 0:a, 1:b, 2:a, 3:b,4:b,5:a. So the subsequence is 1,3,4,5? Wait, but 5 is a. Oh wait no, the output is "bbba", which is b, b, b, a. Oh right. Wait, why is the last 'a' included? Because even though 'a' is smaller than 'b's, but when you have three 'b's, adding the 'a' at the end gives a longer subsequence. But since lex order first compares the first character, then the next, etc. So between two sequences of the same length, the one with a higher character in the first differing position is larger. But if one is longer, like if after some same characters, the longer one is larger. Wait, according to the problem statement's definition of lex order, the first condition is if the length is longer and the prefixes are the same up to the shorter's length. So for example, "bbba" is longer than "bbb", so it's larger. But between "bbba" and "bbbc", the latter is larger. So the algorithm needs to maximize the lex order by choosing as many high characters as possible, but also considering the length.

Wait, but the lex maximum is determined first by the first character. So the first character in the subsequence should be the largest possible character in the string. Then, after that, the next character should be the largest possible in the remaining characters (those that come after the first character's position), and so on, but with a possible twist. Wait, but perhaps sometimes you can take a slightly smaller character earlier to get a longer sequence of larger characters later. For example, if the string is "abba", the maximum subsequence would be "bba". But if the string is "abbaa", then maybe "bbaa" is better. Hmm. Wait, in this case, the first 'a' is followed by two 'b's. So the first character is 'b' (the earliest occurrence of the largest character), then the next is the next 'b' after that, then 'a's. So the maximum is "bbaa".

Wait, but how to model this. The classic approach for lex maximum subsequence is to use a greedy approach. Let me recall. The standard problem is to find the maximum subsequence of length k. But here, the length is variable. The key is that the lex maximum subsequence can be obtained by greedily choosing the highest possible character at each step, considering the remaining characters.

Wait, in the problem, the lex order is such that a longer sequence can be better than a shorter one if the prefixes are equal up to the shorter's length. So, for example, if two subsequences are "zzz" and "zzza", then "zzza" is larger. So, in this case, even though the last character is 'a', which is smaller, the longer length makes it better. But if the subsequences are "zzzb" and "zzzaa", then "zzzb" is larger, because the third character 'b' is larger than 'a'.

So the algorithm needs to balance between selecting the largest possible characters and ensuring that the subsequence is as long as possible when possible.

Hmm. So how to approach this.

The problem is similar to finding the maximum possible sequence by choosing characters in order, such that each next character is as large as possible given the remaining positions. But how to do this efficiently.

An efficient approach for this problem is to process the string and build a stack-like structure. The idea is similar to the problem where you want the largest possible number by removing k digits. But in this case, the goal is different.

Wait, another approach: the lex maximum subsequence is the one where each character in the subsequence is as large as possible, given the remaining characters.

So for example, the first character must be the maximum possible in the entire string. Then, the next character must be the maximum possible in the remaining substring (after the first character's position), and so on. However, this approach would not necessarily produce the lex maximum because there might be cases where taking a slightly smaller character earlier allows for more larger characters later, leading to a longer sequence that is lex larger.

Wait, but the lex order gives higher priority to the first differing position. So if two sequences start with the same characters up to position r, then the next character decides. But if one is longer and the prefixes up to the shorter's length are equal, then the longer one is better. So, for example, the sequence "zzzz" is better than "zzz".

But according to the problem statement's definition, "x is larger than y if either |x|>|y| and x1=y1,..., x|y|=y|y|, OR there exists r < min(|x|,|y|) where x1...xr = y1...yr and x_{r+1} > y_{r+1} }".

So, the lex maximum subsequence is the one that is the largest possible in lex order, considering both the characters and the length.

So, the approach is to select the largest possible subsequence in lex order, which is not necessarily the same as selecting the maximum possible characters in order. For instance, in the first example, the output is "bbba". The original string is ababba. So the first 'b' is chosen (position 1). Then the next 'b' is position3, then position4, then position5's 'a' is added. So even though the 'a' is the smallest character, adding it makes the sequence longer. But why not take another 'b'? Because there are no more 'b's after position4, except maybe the ones before. Wait, let's see: the string is a (0), b (1), a (2), b (3), b (4), a (5). So the first 'b' is at 1. Then, after that, the remaining characters are positions 2-5. The next maximum in this substring is 'b' at 3, then after that, positions4 and 5. The next 'b' at4. Then after that, the remaining characters are 5. So the next character is 'a'. So the total is 'bbba'.

But why not take another 'b'? Because there are no more 'b's after position4. So the subsequence built is the maximum possible.

But how do we model this?

Another approach: the lex maximum subsequence is equivalent to the sequence formed by choosing the first occurrence of the largest possible character, then the largest possible in the remaining string, and so on, but allowing for trailing characters to be added even if they are smaller, as long as they are the only ones left.

Wait, perhaps we can model this by building a stack. For each character in the string, we can check if adding it to the stack allows for a larger sequence. For example, if the current character is larger than the last character in the stack, perhaps we can pop the stack's last character to allow for a larger sequence. But this is similar to the problem of creating the largest possible number by removing k digits. However, in this case, since we want the maximum possible subsequence (without any length constraint), perhaps the algorithm needs to be adjusted.

Wait, let's think of the stack approach. The goal is to build the lex maximum subsequence by iterating through each character and deciding whether to keep it in the stack. The stack will maintain the maximum possible sequence up to the current character.

For each character c in the string:
    While the stack is not empty and the current character c is greater than the top of the stack, and there are enough characters remaining to build a longer subsequence, we pop the stack. But how to model "enough characters remaining"?

Alternatively, since we can take any subsequence (any length), perhaps the stack approach can be modified as follows: whenever we have a current character that is larger than the top of the stack, we can pop the stack as long as the current character is larger. This would ensure that higher characters are placed as early as possible, leading to a lex larger sequence.

Wait, let's take the first example: ababba.

Processing each character:

Start with empty stack.

a: stack is empty, add 'a' → stack = ['a']

Next character is 'b'. Now, 'b' is larger than 'a', so we can pop 'a' and add 'b' → stack becomes ['b'].

Next character is 'a': 'a' is less than 'b', so we add it. Stack is ['b', 'a'].

Next character is 'b': 'b' is larger than 'a', so pop 'a' → stack becomes ['b']. Now, compare 'b' with the new top (which is 'b'), same, so add 'b' → stack is ['b', 'b'].

Next character is 'b': same as the top, add it → stack becomes ['b','b','b'].

Next character is 'a': compare with top 'b'. 'a' is smaller, so add it → stack becomes ['b','b','b','a'].

The resulting subsequence is 'bbba' which matches the example.

Hmm, this seems to work. So the algorithm here is:

- Iterate through each character in the string.

- For each character, while the stack is not empty, and the current character is larger than the top of the stack, we pop the top (since we can get a lex larger sequence by taking the current character earlier).

- Then, add the current character to the stack.

Wait, but this would not necessarily include all possible characters, but perhaps the process of popping allows higher characters to be added earlier, leading to a lex larger sequence.

But wait, in the example, after popping 'a' (the first 'a' in the stack) to add the 'b', the next 'a' is added, but then when another 'b' comes, the 'a' is popped again.

So the algorithm here seems to be building a monotonically increasing stack, but in reverse. Wait, no, because we're allowed to replace the top of the stack with a higher character if possible, even if the next characters are higher.

Wait, but why does this work? Because each time we can choose to take the higher character even if it's later, as long as it's possible to form a longer sequence.

Alternatively, perhaps the stack is being built in a way that ensures that the sequence is lex maximum. For example, when a higher character is encountered later, it's better to include it even if that means dropping some previous characters. Because the higher character earlier in the sequence would make the entire sequence larger.

But how to model the fact that even after popping, there are enough characters left to build the rest of the subsequence. Oh, right, but in the problem, we can take any subsequence (including all remaining characters), so we need to ensure that by popping, we don't reduce the length below what is possible.

Wait, but in the standard problem where you want the maximum number by removing k digits, the approach uses a stack and ensures that you have enough characters left to form the required length.

But in this problem, the required length isn't fixed. So the algorithm must allow for building the lex maximum subsequence, which can be of any length. So the approach is to greedily build the stack by ensuring that each character is as large as possible, replacing previous characters if possible.

So the algorithm is:

Initialize an empty stack.

For each character c in s:

    While stack is not empty and c > stack[-1], and (we can pop the stack and still have characters left to include c and the remaining characters):

        pop the stack.

    append c to the stack.

The problem is determining the condition for popping. But perhaps, in this problem, since we can choose to take any number of characters (no k limit), the condition is simply that if the current character is larger than the top of the stack, we can pop the top and replace it with the current character, which leads to a larger sequence.

But how to avoid cases where popping a character leads to a shorter sequence but higher lex order?

Wait, for example, consider the string 'abba'. The stack approach would process:

a → stack [a]

Then 'b' comes: since 'b' > 'a', pop 'a', stack becomes empty. Then append 'b' → stack ['b']

Next 'b' comes: same as top, append → stack ['b', 'b']

Next 'a' comes: 'a' < 'b', append → stack ['b', 'b', 'a']

Result is 'bba', which is the lex maximum. Because 'bbaa' would be lex smaller than 'bba'? Wait, no. Wait, 'bba' is length 3, 'bbaa' is length 4, and the first three characters are same, so longer is better. So the lex maximum would be 'bbaa'.

Wait, so the stack approach would not capture this. So what's wrong here?

In the string 'abba', the stack approach would process the 'a' (pos 0), then 'b' (pos1) pops the 'a', then next 'b' (pos2) is added. Then 'a' (pos3) is added. The stack is 'bb a'. So the result is 'bba', but the actual maximum is 'bbaa', which is longer. So the algorithm as described would fail here.

Hmm, this suggests that the stack approach is not correct. So what's the problem here?

Ah, right, because in this case, the 'a's after the 'b's can be added to form a longer sequence. But the stack approach would not include them because the 'a's are smaller than the previous 'b's. But according to the lex order definition, the longer sequence is better if the prefixes are the same.

So, in this case, the stack approach gives 'bba', which is of length 3, but the correct answer is 'bbaa', which is longer. So the algorithm would fail here.

This indicates that the initial approach is incorrect.

So, the stack approach that greedily picks higher characters, even if it means reducing the length, is not correct. Because sometimes, even if a character is smaller than the previous ones, adding it can result in a longer sequence, which is lex larger.

Wait, but how to balance between the characters and the length.

So the problem is to find the lex maximum subsequence, which could be longer but have some smaller characters at the end.

But how to model this.

Alternative approach: the lex maximum subsequence is the sequence formed by taking as many as possible of the highest possible characters.

So, for example, first find the maximum character in the string. Then, take all occurrences of that character. Then, between those characters, take the maximum possible subsequence.

Wait, but this may not work. Let's see.

In the first example, the maximum character is 'b'. There are three 'b's. The subsequence formed by taking all 'b's would be 'bbb', but the correct answer is 'bbba', which is longer. So adding the 'a' at the end is better because it's longer.

So in this case, even though the 'a' is smaller than the 'b's, adding it gives a longer sequence, which is better.

So the correct approach must take into account that after taking all the maximum possible characters, we need to append any remaining characters, even if they are smaller, as long as they come after the last maximum character. But that's not necessarily the case. For example, in the 'abba' example, after taking the 'b's, the 'a's after can be added to make a longer sequence.

So perhaps the correct approach is to take the maximum possible characters, but also include any characters that come after the last occurrence of the maximum character.

Wait, but that may not be optimal. Let's think.

Suppose the string is 'abbaa'. The maximum character is 'b'. The occurrences of 'b's are at positions 1 and 2. The 'a's after positions 2 can be added. So the maximum subsequence would be 'bbaaa', which is longer and thus better than 'bb'.

But what if there's a higher character after some lower ones? For example, 'abcabc'. The maximum subsequence would be 'ccc' if all 'c's are taken, but if there are 'c's followed by lower characters, then adding the lower characters would make the sequence longer, which is better.

So the key is to collect all the maximum possible characters first, then append any remaining characters after the last maximum character. But wait, this doesn't account for the case where there's a higher character later but you have to skip some to get it. For example, 'abac'. The maximum character is 'c'. The subsequence would be 'ac' (from positions 0 and 3), but the correct maximum is 'bac', which is longer. Wait, no. Wait, 'abac' → the maximum possible is 'c' first. So 'c' is the first character. Then, no characters after. So the subsequence is 'c'. But 'bac' is 'b', 'a', 'c', which is lex smaller than 'c' because the first character is 'c' vs 'b'.

Ah right. So the correct answer is 'c'.

But in the case of 'abbaa', the maximum subsequence is 'bbaaa' (positions1,2,3,4,5). Which is longer than 'bb', so it's better.

So how to model this.

So the algorithm must select the first occurrence of the maximum character, then recursively find the maximum subsequence in the remaining part (after that character) and append it.

Wait, that's a recursive approach. Let's see.

The maximum subsequence is the first occurrence of the maximum character in the string, followed by the maximum subsequence of the remaining string after that character.

This is a recursive approach. For example:

In 'ababba':

The maximum character is 'b', first occurrence at index 1. Then, the remaining string is from index2 to end. In that substring, the maximum is 'b' (index3). Then remaining is index4 onwards. The maximum is 'b' (index4). Remaining is index5 onwards, which is 'a'. So the subsequence is 'bbba', which is correct.

But this approach would work for the first example. Let's test for the 'abbaa' example.

String 'abbaa' is a, b, b, a, a.

The maximum character is 'b', first occurrence at index1. The remaining string is from index2: 'baa'. The maximum in that is 'b' (index2). Remaining is 'aa'. Max is 'a', and then the rest. So the subsequence would be 'bbaaa', which is correct.

But this approach would process the string in O(n^2) time in the worst case, which is not acceptable for n=1e5.

So, we need an efficient way to compute this.

So the algorithm is:

1. Find all the positions where the character is the maximum possible remaining, and select the earliest occurrence possible to allow more characters to be picked later.

But how to do this efficiently.

The recursive approach can be translated into an iterative approach. For example, the subsequence is built by repeatedly appending the maximum character in the remaining substring, then moving to the remaining part after that character's position.

But for a string of length 1e5, this approach would require O(n) steps, each of which may take O(n) time, leading to O(n^2) time, which is not feasible.

So, how to optimize this.

The key is to precompute for each position, the next occurrence of each character. Or perhaps for each position, the maximum character in the suffix starting at that position.

Yes. If we precompute, for each position i, the maximum character in s[i..n-1], then we can use this to build the subsequence.

Here's the idea:

- Precompute for each index i, the maximum character in the suffix starting at i. Let's call this max_char[i].

Then, iterate through the string from left to right. At each step i, if s[i] == max_char[current_position], then include it in the subsequence and move current_position to i+1.

This way, we greedily take the earliest occurrence of the maximum possible character in the remaining suffix.

This approach runs in O(n) time after precomputing the max_char array.

But how to compute the max_char array efficiently.

Yes. The max_char can be computed in O(n) time by iterating from the end of the string to the beginning.

For example:

Initialize max_char array of length n.

max_char[n-1] = s[-1]

for i from n-2 downto 0:

    max_char[i] = max(s[i], max_char[i+1])

This way, for each position i, max_char[i] is the maximum character in the substring s[i..n-1].

Once we have this array, we can iterate through the string and collect the characters where s[i] == max_char[i], but only once. Wait, no. Because each time we select a character s[i], the next selection must be made from the suffix starting at i+1. So the process is:

current_pos = 0

result = []

while current_pos < n:

    current_max = max_char[current_pos]

    # find the earliest position >= current_pos where s[pos] == current_max

    pos = first occurrence of current_max in s starting at current_pos.

    append current_max to result

    current_pos = pos + 1

This would collect the earliest occurrences of each maximum character in the remaining suffix. For example, in 'ababba', the max_char array is:

Indices 0 to 5:

s = a b a b b a

max_char:

At 5: a

4: max(b, a) = b

3: max(b, b) = b

2: max(a, b) = b

1: max(b, b) = b

0: max(a, b) = b

So max_char array is ['b', 'b', 'b', 'b', 'b', 'a'].

So current_pos starts at 0. current_max is 'b'. We look for the first 'b' from position 0, which is at index1. Append 'b' to result. current_pos becomes 2.

At current_pos=2, max_char[2] is 'b'. Find the first 'b' from 2, which is at index3. Append 'b'. current_pos becomes4.

max_char[4] is 'b'. Find first 'b' at4. Append 'b'. current_pos becomes5.

max_char[5] is 'a'. Append 'a'. current_pos becomes6. Exit loop.

Result is 'bbba', which is correct.

Another example: 'abbaa' → a, b, b, a, a.

max_char array:

index4: a

index3: a → max(a, a) = a

index2: max(b, a) = b

index1: max(b, b) = b

index0: max(a, b) = b

So the array is ['b', 'b', 'b', 'a', 'a'].

current_pos starts at0. current_max is 'b'. find first 'b' from0 → index1. Append 'b'. current_pos becomes2.

current_max is 'b' (max_char[2] is 'b'). find first 'b' from2 → index2. Append 'b'. current_pos becomes3.

current_max is 'a'. find 'a' from3 → index3. Append 'a'. current_pos becomes4. append 'a'. current_pos becomes5. Exit. So the result is 'bbaa', which is correct.

So this approach works.

But how to efficiently find the first occurrence of current_max in the substring s[current_pos ... end]?

In the worst case, for each step, we could scan from current_pos until we find the current_max. But if the string is all 'z's, then each step would take O(1) time. But if the string is such that after each step, we have to scan through many characters, like 'abababab...', then each step could take O(n) time, leading to O(n^2) time.

This would be too slow for n=1e5.

So we need a way to find the first occurrence of the current_max in O(1) time per query.

How can we do that?

We can precompute for each position and each character, the next occurrence of that character. But since there are 26 letters, this would require O(26n) space, which is acceptable.

Alternatively, for each position i, we can precompute the next occurrence of each character in s starting from i.

Wait, but how?

We can create an array next_pos, where next_pos[i][c] is the smallest index j >=i where s[j] == c.

This can be built by processing the string from right to left.

Here's how:

Initialize next_pos as a list of dictionaries. For each position i, next_pos[i] is a dictionary mapping characters to their next occurrence.

Start from the end of the string. For each character, keep track of the last occurrence of each character. Then, for each position i, next_pos[i] is a copy of the current last_occurrence, and then we update the last_occurrence for s[i] to be i.

For example, for the string 'ababba' (indices 0-5):

Processing from right to left:

i=5 (char 'a'):

last_occurrence is {'a':5}.

next_pos[5] = {'a':5}.

i=4 (char 'b'):

last_occurrence is updated to {'a':5, 'b':4}.

next_pos[4] = {'a':5, 'b':4}.

i=3 (char 'b'):

update last_occurrence['b'] to 3.

next_pos[3] = {'a':5, 'b':3}.

i=2 (char 'a'):

update last_occurrence['a'] to2.

next_pos[2] = {'a':2, 'b':3}.

i=1 (char 'b'):

update last_occurrence['b'] to1.

next_pos[1] = {'a':2, 'b':1}.

i=0 (char 'a'):

update last_occurrence['a'] to0.

next_pos[0] = {'a':0, 'b':1}.

So for any position i and character c, next_pos[i][c] gives the next occurrence of c starting at i.

But building this data structure for n=1e5 is feasible, as it's O(n * 26) time and space, which is manageable.

Once this next_pos array is built, then for each step, given current_pos and current_max, we can find the first occurrence of current_max in O(1) time by looking up next_pos[current_pos][current_max].

But wait, what if current_max is not present in next_pos[current_pos]? That would mean that there are no occurrences of current_max in the current_pos to end. But according to the max_char array, current_max is the maximum character in the current suffix, so there must be at least one occurrence. So this is not possible.

Thus, the steps would be:

1. Precompute the max_char array from right to left.

2. Precompute the next_pos array from right to left.

3. Iterate through the string, using the max_char and next_pos to build the result.

This approach would run in O(n) time for each of the steps, leading to O(n) total time, which is acceptable for n=1e5.

So now, let's outline the steps in code.

First, compute the max_char array:

n = len(s)

max_char = [0]*n

max_char[-1] = s[-1]

for i in range(n-2, -1, -1):

    max_char[i] = max(s[i], max_char[i+1])

Then, compute the next_pos array. For this, we can use a list of dictionaries, but since Python's default dictionaries can be a bit slow, perhaps we can use a list of lists for each character.

Alternatively, for each character, we can precompute an array that tracks the next occurrence of that character.

But perhaps a more efficient way is to track for each position i and character c, the next occurrence.

To do this, we can first create a list of next positions for each character.

Initialize a list of next_occurrence for each of the 26 letters, initialized to -1.

Then, iterate from the end to the beginning.

For each position i from n-1 downto 0:

    for each character c in 'a' to 'z':

        next_pos[i][c] = next_occurrence[c]

    current_char = s[i]

    next_occurrence[current_char] = i

This way, next_pos[i][c] will be the next occurrence of c after i. But building this for all 26 letters for each position is O(26n) time, which for n=1e5 is 2.6e6 operations—manageable.

But in Python, using a list of dictionaries may be too slow. So perhaps a better approach is to precompute for each position i, and for each character c, the next occurrence.

Alternatively, since we are only interested in the current_max character, which is known at each step, we can optimize.

Wait, but the current_max is known as the maximum character in the suffix. So for each position i, the current_max is max_char[i]. So for each step, when current_pos is i, the current_max is known. Then, we need to find the first occurrence of current_max in s[i...n-1].

So, perhaps instead of precomputing next_pos for all characters, we can precompute for each position i, the next occurrence of the character max_char[i].

But this would require O(n) space and can be computed in O(n) time.

Let me think:

We can create an array next_max_pos, where next_max_pos[i] is the first occurrence of max_char[i] in s[i...n-1].

This can be computed by iterating from the end.

Let's see:

n = len(s)

next_max_pos = [n]*n

last = n

for i in range(n-1, -1, -1):

    if i == n-1:

        next_max_pos[i] = i

    else:

        if s[i] == max_char[i]:

            next_max_pos[i] = i

        else:

            next_max_pos[i] = next_max_pos[i+1]

    # wait, perhaps not. Because the max_char[i] is the same as max_char[i+1], unless s[i] is larger.

Wait, the max_char[i] is the maximum between s[i] and max_char[i+1]. So if s[i] is greater than max_char[i+1], then max_char[i] = s[i]. Else, it's max_char[i+1].

So for example, if s[i] is the new maximum, then the first occurrence of max_char[i] is i. Otherwise, the first occurrence is next_max_pos[i+1].

So, to compute next_max_pos[i], it can be done as:

if s[i] == max_char[i]:

    next_max_pos[i] = i

else:

    next_max_pos[i] = next_max_pos[i+1]

So this can be computed in O(n) time.

Yes. This way, next_max_pos[i] gives the first occurrence of max_char[i] in the suffix starting at i.

So how to compute this:

Initialize next_max_pos as an array of size n.

next_max_pos[-1] = n-1.

for i in range(n-2, -1, -1):

    if s[i] == max_char[i]:

        next_max_pos[i] = i

    else:

        next_max_pos[i] = next_max_pos[i+1]

So for example, in the 'ababba' example:

max_char array is:

Indices 0-5: 'b', 'b', 'b', 'b', 'b', 'a'.

Then, next_max_pos for each i:

i=5: s[5] is 'a', which equals max_char[5], so next_max_pos[5] =5.

i=4: s[4] is 'b', which equals max_char[4] ('b'), so next_max_pos[4] =4.

i=3: 'b' == 'b' → next_max_pos[3] =3.

i=2: 'a' != 'b' (max_char[2] is 'b'), so next_max_pos[2] = next_max_pos[3] =3.

i=1: 'b' == 'b' → next_max_pos[1] =1.

i=0: 'a' != 'b' → next_max_pos[0] = next_max_pos[1] =1.

So next_max_pos array is [1,1,3,3,4,5].

So for each current_pos i, the first occurrence of max_char[i] in s[i..n-1] is next_max_pos[i].

Thus, the algorithm can be written as:

current_pos = 0

result = []

while current_pos < n:

    pos = next_max_pos[current_pos]

    result.append(s[pos])

    current_pos = pos + 1

This loop will collect the earliest occurrences of the maximum characters in each suffix.

This approach runs in O(n) time, as each step moves current_pos forward by at least 1, and each iteration is O(1).

So this is the correct approach.

Now, let's test it on the 'abbaa' example.

The string is 'a','b','b','a','a'.

max_char array is:

i=0: 'b'

i=1: 'b'

i=2: 'b'

i=3: 'a'

i=4: 'a'

next_max_pos:

i=4: s[4] is 'a' equals max_char[4], so next_max_pos[4] =4.

i=3: s[3] is 'a' equals max_char[3] ('a'), next_max_pos[3] =3.

i=2: s[2] is 'b' equals max_char[2] ('b'), next_max_pos[2] =2.

i=1: s[1] is 'b' equals max_char[1] ('b'), next_max_pos[1] =1.

i=0: s[0] is 'a' which is not equal to max_char[0] ('b'), so next_max_pos[0] = next_max_pos[1] =1.

So next_max_pos array is [1,1,2,3,4].

current_pos starts at0.

pos=1 (s[1] is 'b'), append 'b'. current_pos=2.

pos=2 (s[2] is 'b'), append 'b'. current_pos=3.

pos=3 (s[3] is 'a'), append 'a'. current_pos=4.

pos=4 (s[4] is 'a'), append 'a'. current_pos=5. Exit loop.

Result is 'bbaa', which is correct.

Another test case: 'abbcbccacbbcbaaba'.

The sample output is 'cccccbba'.

Let's see if the algorithm works.

But perhaps it's easier to trust that the algorithm works based on the previous examples.

Thus, the steps to solve the problem are:

1. Compute the max_char array.

2. Compute the next_max_pos array.

3. Use these arrays to iterate and build the result.

Now, let's implement this in Python.

In code:

Read the input string s.

Compute max_char array.

Compute next_max_pos array.

Then iterate through the string as per the algorithm.

Now, for Python, handling large strings (1e5) should be manageable as long as the code is optimized.

Implementing the steps:

n = len(s)

if n ==0:

    print("")

max_char = [None]*n

max_char[-1] = s[-1]

for i in range(n-2, -1, -1):

    max_char[i] = max(s[i], max_char[i+1])

Then, compute next_max_pos:

next_max_pos = [0]*n

next_max_pos[-1] = n-1

for i in range(n-2, -1, -1):

    if s[i] == max_char[i]:

        next_max_pos[i] = i

    else:

        next_max_pos[i] = next_max_pos[i+1]

Then, current_pos starts at0, and we collect the characters.

current_pos =0

result = []

while current_pos < n:

    pos = next_max_pos[current_pos]

    result.append(s[pos])

    current_pos = pos +1

Finally, output the joined result.

But in Python, for very large n, appending to a list is O(1) amortized, so this is efficient.

Testing this code with the first sample input 'ababba' gives 'bbba'.

Another example: 'abbcbccacbbcbaaba' → output 'cccccbba'.

Let's see:

max_char array would track the maximum character in the suffix. The maximum character in the entire string is 'c', then after each 'c', the next maximum would be 'c's again.

The next_max_pos array will find the earliest 'c' in each suffix, leading to all 'c's being collected first, then 'b's, etc.

Thus, the code should work.

Now, implement the code.

But in Python, the code is straightforward.

Now, code:

Read the input as s.

Then compute max_char and next_max_pos.

Finally, build the result.

The code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = len(s)

    if n == 0:

        print("", file=output_stream)

    else:

        max_char = [c for c in s]

        # Compute max_char from right to left

        for i in range(n-2, -1, -1):

            if max_char[i+1] > max_char[i]:

                max_char[i] = max_char[i+1]

        # Now compute next_max_pos

        next_max_pos = [0]*n

        next_max_pos[-1] = n-1

        for i in range(n-2, -1, -1):

            if s[i] == max_char[i]:

                next_max_pos[i] = i

            else:

                next_max_pos[i] = next_max_pos[i+1]

        # Build the result

        result = []

        current_pos =0

        while current_pos <n:

            pos = next_max_pos[current_pos]

            result.append(s[pos])

            current_pos = pos +1

        print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
abbcbccacbbcbaaba
""",
            "output": \
"""\
cccccbba
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

The next_max_pos array is computed as:

next_max_pos[5] =5.

i=4: s[4] is 'b' equals max_char[4] ('b') → next_max_pos[4] =4.

i=3: s[3] is 'b' equals max_char[3] → next_max_pos[3]=3.

i=2: s[2] is 'a' != max_char[2] ('b') → next_max_pos[2] = next_max_pos[3] =3.

i=1: s[1] is 'b' equals max_char → next_max_pos[1] =1.

i=0: s[0] is 'a' != max_char → next_max_pos[0] =1.

So next_max_pos array is [1,1,3,3,4,5].

Then, current_pos starts at0:

pos=1 → append 'b' → current_pos=2.

pos=3 → append 'b' → current_pos=4.

pos=4 → append 'b' → current_pos=5.

pos=5 → append 'a' → current_pos=6 → exit.

Result is 'bbba'.

Which is correct.

So the code works.

Another test case: 'abbaa' → max_char array is ['b', 'b', 'b', 'a', 'a'].

next_max_pos:

i=4: next_max_pos[4] =4.

i=3: s[3] is 'a' equals max_char → next_max_pos[3] =3.

i=2: s[2] is 'b' equals max_char → next_max_pos[2] =2.

i=1: s[1] is 'b' equals max_char → next_max_pos[1] =1.

i=0: s[0] is 'a' != max_char[0] ('b') → next_max_pos[0] =1.

Thus, current_pos=0 → pos=1 → append 'b' → current_pos=2.

current_pos=2 → pos=2 → append 'b' → current_pos=3.

current_pos=3 → pos=3 → append 'a' → current_pos=4.

current_pos=4 → pos=4 → append 'a' → current_pos=5.

Result is 'bbaa'.

Which is correct.

Thus, the code works.
</think>

```python
s = input().strip()
n = len(s)
if n == 0:
    print("")
else:
    max_char = list(s)
    for i in range(n-2, -1, -1):
        if max_char[i+1] > max_char[i]:
            max_char[i] = max_char[i+1]
    next_max_pos = [0] * n
    next_max_pos[-1] = n-1
    for i in range(n-2, -1, -1):
        if s[i] == max_char[i]:
            next_max_pos[i] = i
        else:
            next_max_pos[i] = next_max_pos[i+1]
    result = []
    current_pos = 0
    while current_pos < n:
        pos = next_max_pos[current_pos]
        result.append(s[pos])
        current_pos = pos + 1
    print(''.join(result))
```
