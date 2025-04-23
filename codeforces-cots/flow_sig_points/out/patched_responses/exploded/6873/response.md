<think>
Okay, let's see. The problem is about formatting a given XML-text according to specific indentation rules. Hmm. The input is a valid XML-text string with nested tags, and we need to output each tag on a separate line with the correct number of spaces before it. The spaces are 2 times the level of nestedness.

First, I need to parse the input string into individual tags. Each tag is either an opening tag like <a> or a closing tag like </a>. So the first step is to split the input into these tags. The input string has no spaces, so it's a continuous sequence of these tags.

How to split the string into tags? Well, each tag starts with '<' and ends with '>'. So, the input can be processed by splitting at each occurrence of '><', but maybe that's not entirely accurate. Wait, for example, the input might start with a single '<a>...', so the first character is '<', and each tag starts with '<' and ends with '>'. So perhaps splitting the string by '><' and then adjusting for the first and last parts.

Wait, for example, the input is "<a><b></b></a>". The tags are <a>, <b>, </b>, </a>. Splitting on '><' gives ['<a', 'b', '/b', '/a>']. Wait, no. The original string is "<a><b></b></a>". So splitting on '><' gives ['<a', 'b></b', '/a>'], which isn't correct. Hmm, that's a problem. So maybe a better way is to iterate through the string and extract each tag.

Each tag starts with '<' and ends with '>'. So, the tags can be found by starting at each '<' and capturing until the next '>'. So the correct way is to split the string into substrings that start with '<' and end with '>'. So for example, in the input string, every time we see a '<', we start a new tag and read until '>'.

So, for example, the input starts at index 0 with '<', then until the next '>', which is at index 3 (for <a>), then the next '<' is at index 3 (but wait, the next character after '>' is '<' again. So for input like "<a><b></c>", the tags are '<a>', '<b>', '</c>'.

So the correct approach is to split the string by '><' but also account for the initial and closing parts. Wait, perhaps another approach: iterate through each character and collect the tags.

Alternatively, split the entire string on '><' and then adjust the first and last elements. For example, the input is a string s. Split s[1:-1] on '><'? Because the entire string starts with '<' and ends with '>', right? Because the input is a valid XML-text. So for example, the input "<a><b></b></a>" would be processed as follows: the entire string is from index 0 to 15 (assuming length 16). So s starts with '<' and ends with '>'. So if we take the substring from 1 to len(s)-2 (since the last character is '>'), then split on '><', we get the tags. Let's see:

Original string: <a><b></b></a> → s[1:-1] is 'a><b></b></a'? Wait, no. Wait, s is the entire string. For example, the string is "<a><b></b></a>", which is 14 characters long. The first character is '<', the last is '>'. So s[1:-1] would be 'a><b></b></a'. Splitting that on '><' would give ['a', 'b', '/b', '/a']. Then, each part is the content of a tag. So we can prepend '<' and append '>' to each part? Or, wait, each tag is in the form '<x>' or '</x>'. So for the split parts, for example, the split parts are 'a', 'b', '/b', '/a'. So each of these becomes '<a>', '<b>', '</b>', '</a>'. Because the split was on '><', which is the joining parts. So the first tag is '<a>', the next is '<b>', then '</b>', then '</a>'.

So the way to split the tags is:

Take the entire string, split into the parts between '<' and '>', but considering that each tag starts with '<' and ends with '>'. So perhaps the correct way is to split the string into tokens by splitting on '<' and '>', but that might include empty strings. Wait, for example, the string "<a><b></b></a>", split on '<' would give ['', 'a>', 'b>', '/b>', '/a>', '']— no, that's not helpful.

Alternative approach: Iterate through the string, whenever a '<' is found, start capturing characters until the next '>', and that's a tag.

So code steps:

1. Split the input into tags by scanning for '<' and '>'.

   For example, the input string is processed as follows:

   Initialize a list of tags.

   Start at index 0. The first '<' is at 0. Then scan until the next '>', which is at index 3. So the tag is s[0:3+1] → '<a>'. Then the next '<' is at index 4, which is the start of '<b>', and so on.

   So code can be written to iterate through the string, find each occurrence of '<' and '>' to split into tags.

But how to do that in Python?

Maybe using a loop:

Initialize a list called tags. Initialize i=0. While i < len(s):

   if s[i] == '<':

       start = i

       while i < len(s) and s[i] != '>':

           i += 1

       i += 1  # to include the '>'

       tag = s[start:i]

       tags.append(tag)

   else:

       i +=1

Wait, but the input is guaranteed to be a valid XML-text, so there are no characters outside the tags. So the entire string is a sequence of tags. So this approach will collect all the tags correctly.

Yes. So for each '<' found, we capture until the next '>', then add that substring as a tag.

Once the tags are extracted, the next step is to determine the indentation level for each tag.

The indentation level is determined by the nesting depth. Opening tags increase the depth, and closing tags decrease it (but the closing tag's indentation is based on the current depth before processing).

Wait, the level for a tag is h. For an opening tag, when we print it, the current depth is h, and after printing, the depth increases by 1. For a closing tag, the current depth is h, and after printing, the depth decreases by 1.

But how do we track this?

Let me think. The level of a tag's nestedness is h. For example, in the first example:

<a> is level 0. Then <b> is level 1. <c> is level 2. Then </c> is level 2. Then </b> is level 1. Then </a> is level 0.

Wait, but the output for </c> is indented with 2*2 =4 spaces, which is correct. So the closing tag's indentation is based on the current level before processing it.

So the process is:

We have a stack that represents the current depth. For each opening tag, when we process it, the current depth is h. Then we push it onto the stack (h+1). For a closing tag, when we process it, the current depth is h, then we pop the stack (so the depth becomes h-1).

Wait, but the closing tags are processed after the opening ones. So for example, for the first example:

The tags are <a>, <b>, <c>, </c>, </b>, </a>.

Processing:

- <a>: level 0. Print with 0*2 spaces. Then push, current level becomes 1.

- <b>: level 1. Print with 1*2 spaces. Push, level 2.

- <c>: level 2. Print with 2*2. Push, level 3.

- </c>: current level is 3. But the closing tag's level is 2. Because when you process a closing tag, the level is (current level -1). Wait, perhaps the closing tag's indentation is (current level -1) * 2 spaces.

Wait, because when you have an opening tag, the indentation is h, and then the depth increases by 1. For a closing tag, the indentation is h, and then the depth decreases by 1.

So for example, take the first example:

Start with depth 0.

Tag <a>: printed at depth 0. Then depth becomes 1.

Tag <b>: printed at depth 1. Then depth 2.

Tag <c>: depth 2. Then depth 3.

Tag </c>: it's a closing tag. So its indentation is (3-1) =2. Because after closing, the depth decreases by 1.

Wait, maybe the closing tag's indentation is the same as the current depth minus one. Because when you open a tag, the depth increases after printing. So for the opening tag, the depth is h when printed, then h becomes h+1. For a closing tag, the depth is h when printed, and then becomes h-1.

Wait, let's model this:

Initialize depth =0.

For each tag in tags:

   if it's an opening tag (like <a>):

       print 2*depth spaces followed by the tag.

       depth +=1.

   else (it's a closing tag, like </a>):

       depth -=1.

       print 2*depth spaces followed by the tag.

Wait, no. Because when you process a closing tag, the current depth is h. But according to XML nesting, the closing tag is at the same level as the opening tag. So for example, the opening tag is printed at depth h, then the closing tag is also printed at depth h. But how?

Wait, in the first example:

The opening tags are processed as:

<a> → depth 0 → printed. Then depth becomes 1.

<b> → depth 1 → printed. Then depth 2.

<c> → depth 2 → printed. Then depth 3.

Then comes </c> → which is a closing tag. So for this, the correct indentation is depth 2. But according to the approach above:

Wait, when processing a closing tag, the depth is 3. Then we subtract 1 (depth becomes 2), then print 2*2 spaces. Which is correct.

Yes. So for the closing tag, before processing, the depth is h. Then we decrease the depth by 1, and the printed indentation is h-1 *2.

Wait, no. Let's see:

The processing steps for the first example:

Processing the tags in order:

1. <a> is opening. Print at depth 0 (0 spaces). Then depth increases to 1.

2. <b> is opening. Print at depth 1 (2 spaces). Then depth 2.

3. <c> is opening. Print at depth 2 (4 spaces). Then depth 3.

4. </c> is closing. So before processing, the depth is 3. We need to print it with (3-1)*2 =4 spaces. Then depth becomes 2.

Wait, no. Let's see:

When you have a closing tag, the level of the tag is h, which is one less than the current depth before processing. Because when the opening tag was processed, the depth was h and then increased to h+1. So the closing tag's level is h, which is current depth (h+1) minus 1.

So the approach is: for a closing tag, subtract 1 from the current depth, then print with that depth multiplied by 2. Then, since we already subtracted 1, the depth is now h.

Wait, perhaps the correct approach is:

For opening tags:

- print the tag with current depth * 2 spaces.

- increment depth by 1.

For closing tags:

- decrement depth by 1.

- print the tag with current depth * 2 spaces.

Wait, let's test this with the first example.

Processing tags:

Initial depth =0.

1. <a> is opening:

   print 0*2 spaces. Then depth becomes 1.

2. <b> is opening:

   print 1*2 =2. Then depth 2.

3. <c> opening: print 2*2=4, depth 3.

4. </c> is closing:

   decrement depth to 2.

   print 2*2=4 spaces.

5. </b> is closing:

   decrement to 1, print 1*2=2.

6. </a> closing:

   decrement to 0, print 0.

Yes, that's correct.

So the correct way is:

For a closing tag, first decrease the depth by 1, then print with current depth (which is the correct level) multiplied by 2.

Yes. Because when the closing tag is processed, the current depth is h+1 (since the opening tag was at h, then depth increased to h+1). So when processing the closing tag, we decrease the depth to h, then print with h * 2 spaces.

So the steps are:

- When processing a closing tag, first subtract 1 from the current depth, then print.

So the algorithm would be:

Initialize depth =0.

For each tag in the tags list:

   if the tag starts with '</' (closing):

       depth -=1

       print '  ' * depth + tag

   else:

       print '  ' * depth + tag

       depth +=1

Wait, but that's the reverse. For example, the first opening tag is printed at depth 0, then depth becomes 1. For the closing tag, we first decrease depth, then print. So for the first closing tag, the depth was 1, then subtract 1 to get 0, then print with 0 *2.

Wait, but in the first example, the first closing tag is </c>, which is the third tag. Let's see:

After processing <c> (third tag), depth is 3. Then comes </c> (fourth tag):

   Since it's a closing tag, we subtract 1 from depth (now 2), then print with 2*2=4 spaces. Correct.

Yes. Then the next closing tag is </b> (fifth tag). Processing it:

   Subtract 1, depth becomes 1. Print 1*2=2.

Then </a> (sixth tag):

   subtract 1, depth 0. Print 0*2.

Yes, correct.

So the algorithm is:

For each tag:

   if it's a closing tag:

       subtract 1 from depth before printing.

       then print the tag with depth *2 spaces.

   else:

       print the tag with current depth *2 spaces.

       then add 1 to depth.

So, in code:

We need to loop through each tag. For each tag, check if it starts with '</' (closing tag). Then adjust depth accordingly.

So, steps:

1. Split the input into tags.

   How to split the input into tags?

   As discussed earlier, we can split by looking for '<' and '>'. So code can be written as:

   s = input().strip()

   tags = []

   i = 0

   while i < len(s):

       if s[i] == '<':

           j = i

           while j < len(s) and s[j] != '>':

               j +=1

           j +=1  # to include '>'

           tags.append(s[i:j])

           i = j

       else:

           i +=1

   But since the input is guaranteed to be a valid XML-text, there are no characters outside the tags. So this loop will capture all the tags.

2. For each tag in the tags list, determine if it's an opening or closing tag.

   A closing tag starts with '</', so tag[1] is '/'.

3. Initialize depth =0.

4. For each tag in tags:

   if closing:

       depth -=1

       print '  ' * depth + tag

   else:

       print '  ' * depth + tag

       depth +=1

Wait, no. Wait, for opening tags, we first print, then increment the depth. For closing tags, we first decrement the depth, then print.

Wait, for example, the first tag is <a> (opening). We print it at depth 0, then depth becomes 1.

Then <b> is opening. Print at depth 1, then depth becomes 2.

Then <c> is opening. Print at depth 2, depth 3.

Then </c> is closing. We subtract 1 (depth 2), then print with depth 2*2 spaces. Then depth is 2.

Yes, correct.

But according to the code logic above, for closing tags, we subtract 1 first, then print. So for the closing tag, the code would be:

depth starts at 3 (after processing <c>).

Then, for </c>, it's a closing tag. So code:

depth -=1 → now 2.

print '  ' *2 + tag.

Which is correct.

So the code steps are:

For each tag in tags:

   if tag starts with '</':

       depth -=1

       print ' ' * (depth * 2) + tag

   else:

       print ' ' * (depth * 2) + tag

       depth +=1

Yes. So that's the correct logic.

Now, how to split the tags. Let's test this.

Sample input 1:

<a><b><c></c></b></a>

The input string is "<a><b><c></c></b></a>".

Processing to split tags:

i=0: starts with '<', find next '>'. At index 3. So tag is '<a>', i becomes 4.

i=4: starts with '<', next '>' is at index 6 (since substring is '<b>'). So tag is '<b>', i becomes7.

i=7: starts with '<', next '> is at 10 (substring '<c>'). i becomes 11.

i=11: starts with '<', but next is '/c>'. Wait, the string at this point is "</c></b></a>".

Wait, perhaps I should code this correctly.

Alternatively, in the code:

s = input().strip()

tags = []

i = 0

n = len(s)

while i < n:

    if s[i] == '<':

        j = i

        while j < n and s[j] != '>':

            j +=1

        j +=1  # include the '>'

        tags.append(s[i:j])

        i = j

    else:

        i +=1

This loop should correctly capture all the tags.

Testing the first sample:

Input string is "<a><b><c></c></b></a>".

Processing:

i=0: '<' found. j starts at 0. Increment j until '>' is found. s[0] is '<', s[1] is 'a', s[2] is '>'. So j increments until s[j] == '>', which is index 2. Then j becomes 3 (i:0 to j:3, substring s[0:3] is '<a>'? Wait, no. Wait, the code is s[i:j], which is from i=0 to j (exclusive). So when j is 3 (after the loop found s[2] is '>'), j is incremented by 1 (j becomes 3), then s[0:3] is from 0 to 2 (since Python slicing is up to but not including the end index). Wait, no.

Wait, the code does:

j starts at i (0), then loops until s[j] is '>'. For the tag '<a>', the indices are 0,1,2, where s[0] is '<', s[1] is 'a', s[2] is '>'. So j increments until j=3 (since j starts at 0, loops while j < n and s[j] != '>'. Once j is 2, s[j] is '>', the loop exits. Then j is incremented by 1 (j=3). So the tag is s[i:j], which is s[0:3] → '<a>'?

Wait, no. Let me see:

For i=0, j starts at 0. Then in the loop, j increments until s[j] == '>'. The first loop iteration:

j=0: s[0] is '<' → continue.

j increments to 1: s[1] is 'a' → not '>', j increments.

j increments to 2: s[2] is '>' → loop exits.

Now, j is 2. Then j is incremented to 3. So the tag is s[0:3], which is characters 0,1,2 → '<a>', which is correct.

Yes. Then i is set to j=3.

Next, i=3. s[3] is '<' → start processing. j starts at 3. Loop until s[j] is '>'. s[3] is '<', s[4] is 'b', s[5] is '>'. So j increments until 5. Then j is incremented to 6. So the tag is s[3:6] → '<b>'.

And so on.

So the code correctly splits the input into tags.

Now, for each tag, process as per the logic.

Sample input 1:

Tags list: ['<a>', '<b>', '<c>', '</c>', '</b>', '</a>']

Processing:

depth starts at 0.

First tag: <a> → opening. Print 0 spaces, then depth becomes 1.

Second tag: <b> → opening. Print 2 spaces (depth 1 * 2). Then depth 2.

Third tag: <c> → opening. Print 4 spaces. Depth 3.

Fourth tag: </c> → closing. Decrement depth to 2. Print 2 *2 =4 spaces. Then depth remains 2.

Fifth tag: </b> → closing. Decrement to 1. Print 2*1=2 spaces. Depth 1.

Sixth tag: </a> → closing. Decrement to 0. Print 0*2=0 spaces.

Which matches the sample output.

Another test case: the second example.

Input: "<a><b></b><d><c></c></d></a>"

Tags list: ['<a>', '<b>', '</b>', '<d>', '<c>', '</c>', '</d>', '</a>']

Processing:

depth 0.

First tag: <a> → print with 0. depth 1.

Second tag: <b> → print 2. depth 2.

Third tag: </b> → closing. decrement to 1. print 1*2=2 spaces. Then depth 1.

Fourth tag: <d> → opening. print 1*2=2. depth 2.

Fifth tag: <c> → print 2*2=4. depth 3.

Sixth: </c> → decrement to 2. print 2*2=4. depth 2.

Seventh: </d> → decrement to 1. print 2*1=2. depth 1.

Eighth: </a> → decrement to 0. print 0.

Which matches the sample output.

So the code should work.

Now, the code steps in Python:

Read the input, split into tags, then process each tag.

But in Python, for splitting the tags, perhaps a more efficient way is possible. Let's see.

Alternative approach: using string.split('><') and then adjust the first and last elements.

Wait, for example, the input is "<a><b></b></a>".

s = s[1:-1] → "a><b></b></a".

split on '><' → ['a', 'b', '/b', '/a'].

Then each part is a tag content. So the first tag is '<a>', then '<b>', then '</b>', then '</a>'.

Wait, because the split on '><' gives the parts between the '>' and the '<'. So each part is the content of the tag (without the < and >). So to reconstruct the tags, each part is surrounded by '<' and '>'. So for each part in the split list, the tag is '<' + part + '>'.

But how about the first and last parts?

Wait, original s is '<a><b></b></a>'.

s[1:-1] is 'a><b></b></a'.

Split on '><' → ['a', 'b', '/b', '/a'].

Each part is part of the tag. So the first part is 'a' → becomes '<a>'.

Second part 'b' → '<b>'.

Third '/b' → '</b>'.

Fourth '/a' → '</a>'.

Yes. So the code can be:

s = input().strip()

parts = s[1:-1].split('><')

tags = ['<'+ part + '>' for part in parts]

But wait, the first split is after the first '>'. Let's see.

But this approach is more efficient than the loop. Let's see.

For example, the first example's input after [1:-1] is 'a><b><c></c></b></a'.

Wait, no. Wait, the first example's input is:

Input string is "<a><b><c></c></b></a>".

s[1:-1] is "a><b><c></c></b></a".

Split on '><' → ['a', 'b', 'c', '/c', '/b', '/a'].

Then each part is made into tags as '<a>', '<b>', '<c>', '</c>', '</b>', '</a>'.

Yes. Which is correct.

Another example: the second sample input.

Input is "<a><b></b><d><c></c></d></a>"

s[1:-1] is 'a><b></b><d><c></c></d></a'.

Split on '><' → ['a', 'b', '/b', 'd', 'c', '/c', '/d', 'a'] → wait, no.

Wait, the original s is "<a><b></b><d><c></c></d></a>".

s[1:-1] is 'a><b></b><d><c></c></d></a'.

Split on '><' gives:

Looking at the substring:

a><b></b><d><c></c></d></a

Split on '><' → parts are:

a

b</b

d

c</c</d

/a

Wait, no. Let's see:

The substring is:

a><b></b><d><c></c></d></a

Split on '><' → the split occurs at every occurrence of '><'. Let's see:

Looking for '><' in the substring:

The substring starts with 'a', followed by '><', then 'b', then '></', then 'b', then '><', etc. Hmm, perhaps this approach isn't reliable. Let me test:

s = "<a><b></b><d><c></c></d></a>"

s[1:-1] is 'a><b></b><d><c></c></d</a'

Wait, the original string is:

Assuming input is "<a><b></b><d><c></c></d></a>"

The length is let's see:

Original string: <a> → 3 chars, <b> → 3, </b> →4, <d> →3, <c> →3, </c> →4, </d> →4, </a> →5. Wait total length is 3+3+4+3+3+4+4+5? Not sure. But s[1:-1] would be the string between the first '<' and the last '>'. Let's see.

Original string: starts with '<' and ends with '>'.

s[1:-1] is the substring from index 1 to len(s)-2.

But perhaps splitting on '><' in this case would produce:

For example, the substring is "a><b></b><d><c></c></d></a".

Split on '><' gives:

['a', 'b', '/b', 'd', 'c', '/c', '/d', '/a']

Wait, no. Let's see:

The substring is:

a><b></b><d><c></c></d></a

The split occurs at every occurrence of '><'.

Breaking it down:

The first occurrence of '><' is after 'a', then between 'b' and '</b', then between '</b' and '<d>', then between 'd' and '<c>', etc.

Wait, maybe this approach is not reliable. For example, the part '</b' would be part of the split. So the code would generate a tag '<</b>' which is invalid.

Wait, that's a problem. Because splitting on '><' may split in the middle of a closing tag.

For example, the input "<a></a>", the s[1:-1] is 'a></a', which split on '><' gives ['a', '/a']. Then the tags are '<a>', '</a>', which is correct.

But in the second sample input, the s[1:-1] is 'a><b></b><d><c></c></d</a' (assuming the input ends with '>'). Wait, no, perhaps I'm getting confused.

Alternatively, perhaps the split approach is incorrect when there are closing tags. Let's take the second example input:

Original input string: "<a><b></b><d><c></c></d></a>"

s[1:-1] is "a><b></b><d><c></c></d</a".

Wait, no. Let's see:

The original string is:

Let me write it out:

Original string: starts with '<a><b></b><d><c></c></d></a>'.

The entire string is:

< a > < b > < / b > < d > < c > < / c > < / d > < / a >

But the actual string is "<a><b></b><d><c></c></d></a>".

The s[1:-1] is the substring from index 1 to len(s)-2.

Let's compute the length:

Original string: the first example input is 14 characters (including all tags).

But for the second example, let's see:

The tags are <a>, <b>, </b>, <d>, <c>, </c>, </d>, </a>. So each tag contributes to the length. Let's count the characters:

<a> → 3

<b> →3

</b> →4

<d> →3

<c> →3

</c> →4

</d> →4

</a> →5

Total length: 3+3+4+3+3+4+4+5 = 29 characters. So the s[1:-1] is from index 1 to 27 (since len(s) is 29, indexes 0-28; s[1:-1] is 1 to 27-1 = 26? Or 28-1=27? Wait, in Python, s[1:-1] is from index 1 up to but not including index len(s)-1. So for a string of length 29, indexes 0 to 28. s[1:-1] is indexes 1 to 27 (inclusive?), no, because in Python, s[1:-1] is from index 1 up to but not including index -1 (which is len(s)-1-1 = len(s)-2). So for len(s) 29, s[1:-1] is indexes 1 to 28-1=27. So the substring is s[1] to s[27], inclusive.

But in any case, the split on '><' in the s[1:-1] may not work correctly if there are tags like '</b>' which split into 'b></' when split on '><'.

But this suggests that the split approach may not work correctly in some cases.

Hmm. So perhaps the initial approach of splitting with the loop is more reliable.

So the code for splitting the tags should use the loop method to extract all tags correctly.

Thus, the code for splitting the tags is:

s = input().strip()

tags = []

i = 0

n = len(s)

while i < n:

    if s[i] == '<':

        j = i

        while j < n and s[j] != '>':

            j +=1

        j +=1  # to include '>'

        tags.append(s[i:j])

        i = j

    else:

        i +=1

This loop will correctly capture all tags, even if they are closing tags.

Once the tags are split correctly, the next step is to process each tag and print with the appropriate indentation.

Now, code for processing:

depth = 0

for tag in tags:

    if tag.startswith('</'):

        depth -=1

        print('  ' * depth + tag)

    else:

        print('  ' * depth + tag)

        depth +=1

Yes.

So putting it all together.

Testing the first sample input:

Input: <a><b><c></c></b></a>

Processing tags:

['<a>', '<b>', '<c>', '</c>', '</b>', '</a>']

depth starts at 0.

<a> → print with 0 spaces → then depth 1.

<b> → 2 → depth 2.

<c> →4 → depth3.

</c> → subtract 1 → depth2. print 4 spaces.

</b> → subtract →1. print 2.

</a> → subtract →0. print 0.

Which matches the sample.

Another test case with the second sample.

Tags list: ['<a>', '<b>', '</b>', '<d>', '<c>', '</c>', '</d>', '</a>']

Processing:

depth 0.

<a> →0 → depth1.

<b> →2 → depth2.

</b> → subtract1 → depth1. print 2 spaces (1*2).

<d> → print 2 → depth2.

<c> →4 → depth3.

</c> → subtract →2. print 4.

</d> → subtract→1. print2.

</a> → subtract →0. print0.

Which matches the sample.

Thus, the code should work.

Now, considering edge cases.

Edge case 1: empty string? The problem says the input is a non-empty string.

Another edge case: a single tag.

Wait, the problem says that the input is a valid XML-text, which can't be a single tag. Because XML-text is defined as either empty, or a properly nested structure. So a single tag like <a> is not possible. The minimal XML-text is <a></a>, but according to the problem statement, the input is non-empty. So for example, the input is "<a></a>".

Processing:

Tags list is ['<a>', '</a>'].

depth starts at 0.

First tag <a> → printed at 0, depth 1.

Second tag </a> → subtract 1, depth 0. printed with 0 *2 spaces.

So output:

<a>

</a>

Yes.

Another case: nested tags with siblings.

So code should handle any valid XML-text.

Now, considering time and memory constraints. The input is up to 1000 characters. So even with O(n) time, it's acceptable.

The code should be efficient enough. The loop to split tags is O(n), processing each character once.

Thus, the code should work.
</think>

```python
s = input().strip()
tags = []
i = 0
n = len(s)
while i < n:
    if s[i] == '<':
        j = i
        while j < n and s[j] != '>':
            j += 1
        j += 1
        tags.append(s[i:j])
        i = j
    else:
        i += 1

depth = 0
for tag in tags:
    if tag.startswith('</'):
        depth -= 1
        print('  ' * depth + tag)
    else:
        print('  ' * depth + tag)
        depth += 1
```