<think>
Okay, let's tackle this problem. Hmm, the problem statement is a bit complex. Let me read through it again to make sure I understand all the requirements.

So, the task is to format the given string according to specific rules. Let's break down the requirements one by one.

First, the string must not start with a space. That's straightforward. So any leading spaces need to be trimmed.

Second, there should be exactly one space between consecutive words. So any multiple spaces between words should be collapsed into a single space. But also, we need to make sure that words are properly separated, and that there's no space before commas or dots. Wait, but according to the third point, a punctuation (comma or dot) must have a Latin letter immediately before it, and a space after unless it's the last character.

Wait, the third requirement says: a punctuation (dot or comma) must be immediately preceded by a Latin letter. So no space before the punctuation. And after the punctuation, there must be exactly one space if there's a word following. Otherwise, no space. So for example, if the punctuation is at the end of the string, no space after. Otherwise, a space.

Then, the fourth requirement is about the case. All letters must be lowercase except the first letters of sentences. A sentence's first word is the first word of the entire string or a word after a dot. So every time a dot is encountered, the next word (if any) starts with a capital letter. Also, commas don't start a new sentence. So after a comma, the next word is lowercase.

So the steps I need to perform are:

1. Process the original string to handle spaces:
   a. Remove leading and trailing spaces.
   b. Collapse multiple spaces into single ones.
   But also, ensure that between words, there's exactly one space, and that punctuation is properly placed (no space before, space after unless it's the end).

Wait, but handling the punctuation's spacing is part of the processing. So maybe I should split the original string into tokens, considering words and punctuation, then apply the rules.

Alternatively, process the string character by character, keeping track of the current state (like whether the next character needs to be capitalized, whether a space is needed before the next word, etc.)

Let me think about possible steps.

First, the input string can have various issues: multiple spaces, incorrect punctuation spacing, wrong cases. So perhaps the steps are:

- Normalize all the spaces: split into tokens where each token is a word (letters) or a punctuation (comma or dot), with spaces removed. Then, when rebuilding the string, ensure that after a punctuation (except at end), there's a space. Also, words are separated by single spaces.

But handling the punctuation's position relative to the words is crucial. For example, commas and dots are always directly after a word, with no space. Then, after the punctuation, there's a space (unless it's the end).

So perhaps the approach is to process the string into a list of tokens, where each token is a word, a comma, or a dot. Then, when outputting, arrange these tokens with appropriate spaces and case.

Wait, but commas and dots are part of the tokens, but they must be preceded by a word. So for example, the input could have "hello,  world", which should become "hello, world".

So the first step is to split the input into the correct sequence of elements: words followed by punctuation (if any), and then the next word, etc.

Wait, but each punctuation must have a word before it. So the processing should collect words and punctuations, ensuring that a punctuation is only allowed after a word. So perhaps the tokens are in the order of word, then punctuation, then word, etc. But there might be multiple punctuations in a row? No, according to the problem statement's constraints, it's guaranteed that between any two punctuation marks there's at least one letter. So the input has no cases like ".." or ".,", but even if the problem allows processing such, the problem states that the input is such that between two punctuation marks there's a letter. So the input is always possible to process.

So perhaps the steps are:

1. Split the input into tokens where each token is either a word (letters), a comma, or a dot, but the punctuations are considered separate tokens. But also, ensure that punctuations are properly attached to the preceding word.

Wait, for example, in the input "hello ,i AM veRy GooD.Boris", the tokens would be:

hello , i AM veRy GooD . Boris

But in the corrected output, it's "Hello, i am very good. Boris".

So the commas and dots are separate tokens that follow a word. So perhaps the processing is to parse the original string into a list of elements where each element is either a word, a comma, or a dot. But the original string may have spaces and other characters that need to be split into these elements.

So perhaps the first step is to split the input into words and punctuation, ignoring spaces. Then, process these elements to ensure that the punctuation is properly placed and the spacing is correct.

But how to split the original string into these elements?

Let me think: the original string may have letters, spaces, commas, dots.

We can process the string, collecting letters into a word token until we hit a non-letter (space, comma, dot). When a comma or dot is found, we add the current word (if any) to the tokens list, then add the punctuation as a separate token. Then, we skip any spaces until the next word or punctuation.

Wait, but the problem states that between punctuation marks there's at least one letter, so we don't have consecutive commas or dots. So the input is valid in that sense.

So the algorithm could be:

Initialize a list of tokens. Current word is empty.

Iterate through each character in the input string:

- If the character is a letter, add to current word.

- If the character is a comma or dot:
   - If there's a current word, add it to tokens.
   - Add the punctuation to tokens.
   - Reset current word to empty.

- If the character is a space:
   - If there's a current word, add it to tokens and reset current word.
   - Then, ignore spaces until the next non-space.

Wait, but this would split words separated by spaces into separate tokens. But in the original string, words can have multiple spaces between them, which should be collapsed into a single space. So for example, "a   b" becomes "a b".

But according to the tokenization approach, the spaces are handled by splitting into word tokens. So in the example, the two words 'a' and 'b' are in the tokens list, separated by spaces. But the processing would have to collapse any multiple spaces between them into a single space. But perhaps the tokenization step collects words and punctuation, ignoring spaces, so the tokens list is a sequence of words and punctuation. Then, when outputting, each word is followed by punctuation (if present), and after punctuation, a space (unless it's the end).

Wait, perhaps the tokenization step is to create a list of elements where each is a word, followed by any punctuation (comma or dot) that comes immediately after it. But I'm not sure. Alternatively, perhaps the punctuation is a separate token, and the order is word, punctuation, word, punctuation, etc. But since the problem allows sentences to end with a punctuation (like the second example ends with a dot), the tokens list can have a punctuation as the last element.

Wait, for example, in the second input example:

Input: a. b,   C  .

After processing, the tokens would be:

['a', '.', 'b', ',', 'c', '.'] 

But when outputting, we need to make sure that each punctuation is followed by a space unless it's the end. So for this case, the output is "A. B, c."

So the tokens are ordered as word, punctuation, word, punctuation, word, punctuation.

So the tokenization process is to split into words and punctuations, in order.

So the tokenization approach would be:

Loop through each character in the input:

- collect letters into a word. When a punctuation (comma or dot) is encountered, add the current word (if any) to the tokens list, then add the punctuation to the tokens list. Then, reset the current word. Then, skip any spaces until the next letter or punctuation.

Wait, but how do we handle cases where the punctuation is followed by a space? For example, in the input "hello , there", the comma is after a space. But according to the problem, the comma must be preceded by a letter (so no space before it), and followed by a space (if there is a word after).

So during tokenization, the space after the comma is handled by the next word.

So perhaps during the tokenization phase, all spaces are ignored except when separating words.

So the steps for tokenization are:

Initialize tokens = []
current_word = []
current_punctuation = None

for each char in s:

    if char is a letter (upper or lower):
        add to current_word

    elif char is comma or dot:
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
        tokens.append(char)  # punctuation is added as a separate token

    else:  # space
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
        # else, ignore the space (since leading or trailing, or between words)

But wait, this would split words into separate tokens whenever a space is encountered, but if a space comes after a punctuation, that's part of the necessary processing. For example, "hello,   world" would be tokenized as ['hello', ',', 'world'].

Then, during the output phase, each punctuation is followed by a space (if there is a next word), and words are separated by spaces.

But how to handle the case where a punctuation is followed by another punctuation? According to the problem statement, it's guaranteed that between any two punctuation marks there is at least one letter. So that scenario doesn't occur. So the tokens list will have words and punctuation in order, but no two punctuations in a row.

So the tokens list would be a sequence like [word, punctuation, word, punctuation, word, ...].

Once we have the tokens list, we can process each token to apply the case rules and spacing.

Now, for the case rules:

All letters must be lowercase except the first letters of sentences. A sentence starts with a word that is either the first word of the entire string or a word that comes after a dot.

So, the first word is a sentence start. Then, any word following a dot is the start of a new sentence.

So, when processing each word in the tokens list, we need to determine if it's the start of a sentence.

We can track a flag, like 'new_sentence', which is True initially (since the first word is a sentence start), and after each dot, set it to True again.

So, for each token in the tokens list:

- if the token is a word:
   - if new_sentence is True:
       - capitalize the first letter, lowercase the rest
       - set new_sentence to False
   - else:
       - all lowercase

   then, add the processed word to the result.

- if the token is a punctuation (comma or dot):
   - add it to the result (without any changes)
   - if it's a dot, set new_sentence to True (so the next word is capitalized)
   - commas don't affect new_sentence.

Then, the spacing between elements:

After a word, if the next token is a punctuation, there's no space. After a punctuation, if there's a next token (word), then we add a space.

For example, tokens [word1, ',', word2, '.', word3, '.'] would be formatted as "word1, word2. word3." (assuming word1 is capitalized, word2 is lowercase, etc.)

Wait, but the output example shows that after a punctuation (like a comma), a space is added. So for the example, after the comma, a space is added. Between the punctuation and the next word, there's exactly one space.

So when processing the tokens list, between each token, we need to insert spaces according to the following rules:

- after a word, if the next token is a punctuation, no space. So "word,".

- after a punctuation, if there is a next token (word or punctuation?), but according to the problem statement, there can't be a punctuation immediately after punctuation. So after a punctuation, the next token is a word. So after a punctuation, add a space if there is a next token (word).

Wait, for example:

If tokens are [ 'a', '.', 'b', ',', 'c', '.' ]

Then the output should be "A. B, c."

So after the first '.', the next token is 'b', so after the '.', there's a space. Then after 'b', the next token is ',', so no space. Then after the ',', there's a space before 'c'. Then after the '.', there's no space since it's the last token.

So the logic is: when building the result string, for each token in the tokens list, after adding the token, check if the next token is a punctuation or a word. If the current token is a punctuation and there's a next token (which must be a word), then add a space. If the current token is a word and the next token is a punctuation, don't add a space. Otherwise, add a space between word and next word.

But perhaps a better approach is to iterate through the tokens, and for each position, decide whether to add a space after the current token.

So for each index i in tokens:

- current token is tokens[i]

- if current token is a word:

   process its case (based on new_sentence flag)

   if the next token (i+1) exists and is a punctuation, then no space after.

   else, if there is a next token (which is a word), add a space.

- if current token is a punctuation:

   add the punctuation.

   if there is a next token (which must be a word, because the problem says there's a letter between two punctuations), then add a space.

So the rule is: after a punctuation, add a space if there's a next token. Because the next token would be a word, so the punctuation must be followed by a space and the word.

So the steps for building the output string are:

Initialize result as an empty list.

new_sentence = True.

for i in range(len(tokens)):

   token = tokens[i]

   if token is a word:

       process case: if new_sentence is True, capitalize first letter, others lowercase. Else, all lowercase.

       add the processed word to result.

       new_sentence = False  (unless the word is followed by a dot?)

       check the next token (i+1) if exists.

       if next token is a punctuation (comma or dot):

           do not add space here. The punctuation will be added next, and then after that, if there's a next token, add space.

       else:

           if there is a next token (which is a word), add space.

   else: # punctuation

       add the punctuation to result.

       if it's a dot, set new_sentence = True.

       check if there is a next token (i+1 < len(tokens)):

           if yes, add a space.

So for example:

tokens = ['hello', ',', 'i', 'AM', 'veRy', 'GooD', '.', 'Boris']

Processing:

i=0: 'hello' is a word. Since new_sentence is True (it's the first word), capitalize to 'Hello'. Add to result. Next token is ',', so no space. new_sentence remains False (since comma does not affect it). So result is ['Hello'].

i=1: ',', add to result. Next token is 'i' (i=2), so add a space. Result becomes ['Hello', ',', ' '].

i=2: 'i' is a word. new_sentence is False. So lowercase to 'i'. Add to result. Next token is 'AM' (word). So add a space. Result becomes ['Hello', ',', ' ', 'i', ' '].

And so on.

But wait, after a punctuation, if there's a next token, add a space. So after adding the comma (i=1), the next token is 'i' (a word), so a space is added.

So the output would be "Hello, i ..."

So combining the token processing and the spacing.

Let me outline the steps again:

- Tokenize the input into words and punctuation.

- Process each word's case based on whether it's the start of a sentence.

- Determine where spaces should be added between tokens.

So let's code this step by step.

First, tokenization.

The tokenization process:

Loop through each character in the input.

We can ignore spaces except when they separate words. So, collect letters into a current word. When a punctuation is encountered, if the current word is non-empty, add it to tokens, then add the punctuation to tokens. Then, reset current word. Any space after that is ignored until the next letter or punctuation.

Wait, but spaces between words (like "a   b") should be treated as a single space. So during tokenization, any sequence of letters becomes a word, and any sequence of punctuations (which is impossible per problem constraints) is handled as per problem. But according to the problem, between any two punctuation marks there is a letter. So the tokenization process can proceed as:

Initialize tokens as empty list.

current_word = ''

for char in s:

    if char.isalpha():

        current_word += char

    elif char in {',', '.'}:

        if current_word:

            tokens.append(current_word)

            current_word = ''

        tokens.append(char)

    else: # space

        if current_word:

            tokens.append(current_word)

            current_word = ''

        # else, ignore the space (already handled)

After processing all characters, check if current_word is non-empty (in case the string ends with a letter). If so, add to tokens.

This will split the input into words and punctuations. For example:

Input "hello ,i AM veRy GooD.Boris" will be split into:

tokens = ['hello', ',', 'i', 'AM', 'veRy', 'GooD', '.', 'Boris']

Now, process each word's case:

We need to track whether the next word is the start of a sentence. The first word is a start. Also, after a dot, the next word is a start.

So:

new_sentence = True

for each token in tokens:

    if token is a word:

        if new_sentence:

            processed_word = token[0].upper() + token[1:].lower() if token else ''

            new_sentence = False

        else:

            processed_word = token.lower()

        add processed_word to processed_tokens.

    else:

        add token to processed_tokens.

        if token is '.':

            new_sentence = True

        else:

            pass

Then, handle the spacing between processed_tokens.

So, after processing the tokens for case, we need to build the output string with correct spacing.

For each token in processed_tokens, check the next token to decide whether to add a space after.

Initialize output as a list.

for i in range(len(processed_tokens)):

    current = processed_tokens[i]

    output.append(current)

    if i == len(processed_tokens) -1:

        continue  # no space after last token

    next_token = processed_tokens[i+1]

    if current in {',', '.'}:

        # after punctuation, add a space if next token exists (which is a word)

        output.append(' ')

    elif isinstance(current, str) and (current not in {',', '.'}):

        # current is a word. next token could be punctuation or word.

        if next_token in {',', '.'}:

            # no space, since punctuation follows

            pass

        else:

            # next is a word, add space

            output.append(' ')

Wait, but how to distinguish between a word and a punctuation in the processed_tokens? Because in the processed_tokens, the elements are either words (lowercase, except first letters) or punctuation (',', '.').

So for each token in processed_tokens, after appending it to output, check the next token.

So:

For each i from 0 to len(processed_tokens)-1:

   current = processed_tokens[i]

   output.append(current)

   if next token is punctuation:

       if current is punctuation: no (since after punctuation, we have a space)

       else: if current is a word, then no space (since punctuation is next)

   else:

       if current is punctuation: add space

       else: add space (since next is a word)

Wait, perhaps the rules are:

- If current token is a punctuation, add a space if there is a next token (since next token is a word, according to problem constraints).

- If current token is a word, add a space unless the next token is a punctuation.

So, after appending the current token, check:

if there is a next token:

   if current is punctuation:

       add a space

   else:

       if next token is a punctuation: do not add space

       else: add space

So in code:

for i in range(len(processed_tokens)):

    output.append(processed_tokens[i])

    if i < len(processed_tokens) -1:

        next_token = processed_tokens[i+1]

        if processed_tokens[i] in {',', '.'}:

            output.append(' ')

        else:

            if next_token in {',', '.'}:

                # no space between word and punctuation

                pass

            else:

                output.append(' ')

So, let's test this logic with the first example.

Processed tokens after case processing would be:

['Hello', ',', 'i', 'am', 'very', 'good', '.', 'boris']

Then, processing the spacing:

i=0: current is 'Hello', next is ',', so no space.

output becomes ['Hello', ','].

i=1: current is ',', next is 'i'. Since current is punctuation, add space. So output becomes ['Hello', ',', ' '].

i=2: current is 'i', next is 'am'. Next is a word, so add space. So output appends 'i', then space.

and so on.

But wait, in code:

After appending each token, check if there's a next token. Then decide whether to add space.

Let's step through the example:

processed_tokens = ['Hello', ',', 'i', 'am', 'very', 'good', '.', 'boris']

Loop for each i:

i=0, current is 'Hello', next is ','.

Since current is a word and next is punctuation, do not add space. So output is 'Hello, '.

Wait, no. Let's see:

After appending 'Hello', check next token is ',' (punctuation). So:

current is a word, next is punctuation → no space. So after 'Hello', no space. Then i=1 is ','.

current is ',', next is 'i' (word). So after ',', add a space. Then i=2 is 'i'.

current is 'i', next is 'am' (word). So add space after 'i'.

So the output would be:

Hello, i am very good. Boris

Which matches the example.

Another example:

Input: a. b,   C  .

Tokenization step: ['a', '.', 'b', ',', 'C', '.']

Processed tokens for case:

First word 'a' → new_sentence is True → 'A'.

Then '.' → new_sentence becomes True.

Next token is 'b' → new_sentence is True → 'B'.

Then ',' → new_sentence remains False (since comma doesn't affect it).

Next token is 'C' → new_sentence is False → 'c'.

Then '.' → new_sentence becomes True.

So processed_tokens = ['A', '.', 'B', ',', 'c', '.'].

Now, spacing:

i=0: current is 'A', next is '.', which is punctuation → no space. So output 'A.'.

i=1: current is '.', next is 'B' → add space → 'A. '.

i=2: current is 'B', next is ',' → no space. So 'A. B,'.

i=3: current is ',', next is 'c' → add space → 'A. B, '.

i=4: current is 'c', next is '.' → no space. → 'A. B, c.'.

i=5: current is '.', no next token. → done.

Result is 'A. B, c.', which matches the example.

So the logic for spacing seems correct.

Putting it all together:

The steps are:

1. Tokenize the input into words and punctuation.

2. Process each word's case based on whether it's the start of a sentence.

3. Generate the output with correct spacing between tokens.

Now, code.

First, tokenization:

We can process the input string character by character, collecting letters into a word, and when a punctuation is found, add the word (if any) and then the punctuation. Spaces are used to separate words.

In code:

s = input().strip()

tokens = []
current_word = []

for c in s:
    if c.isalpha():
        current_word.append(c.lower())  # normalize to lowercase first; will handle case later
    elif c in {',', '.'}:
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
        tokens.append(c)
    else:  # space
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
# after loop, check if there's remaining current_word
if current_word:
    tokens.append(''.join(current_word))

Wait, but this code will collect letters as lowercase. But during case processing, the first letter may be uppercase. So perhaps during tokenization, we should collect the letters as their original case, then process the case in the next step.

Wait no: the case processing step will handle the entire word's case. So during tokenization, we need to collect the letters as they are. So the code for current_word should append c, not c.lower().

Oops, that's a mistake. Because during tokenization, the letters are collected as they are. For example, the input 'AM' would be added as 'AM' to the token, then in processing, converted to lowercase except the first letter if it's a sentence start.

So the code for tokenization should collect letters as they are. So:

for c in s:
    if c.isalpha():
        current_word.append(c)
    elif c in {',', '.'}:
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
        tokens.append(c)
    else:  # space
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
if current_word:
    tokens.append(''.join(current_word))

Then, process the case:

processed_tokens = []
new_sentence = True

for token in tokens:
    if token not in {',', '.'}:  # it's a word
        if new_sentence:
            # capitalize first letter, lowercase rest
            if not token:
                processed_word = ''
            else:
                processed_word = token[0].upper() + token[1:].lower()
            processed_tokens.append(processed_word)
            new_sentence = False
        else:
            processed_tokens.append(token.lower())
    else:  # punctuation
        processed_tokens.append(token)
        if token == '.':
            new_sentence = True

Then, generate the output with correct spacing.

output = []
for i in range(len(processed_tokens)):
    current = processed_tokens[i]
    output.append(current)
    if i < len(processed_tokens) -1:
        next_token = processed_tokens[i+1]
        if current in {',', '.'}:
            output.append(' ')
        else:
            if next_token not in {',', '.'}:
                output.append(' ')
            # else, do not append space

But wait, in code:

For each current token, after adding to output, check if there is a next token. If yes:

- If current is punctuation (comma or dot), add space.

- Else (current is word), check if next token is punctuation. If yes, no space. Else, add space.

So code:

for i in range(len(processed_tokens)):
    current = processed_tokens[i]
    output.append(current)
    if i < len(processed_tokens) -1:
        next_token = processed_tokens[i+1]
        if current in {',', '.'}:
            # punctuation followed by word: add space
            output.append(' ')
        else:
            if next_token not in {',', '.'}:
                # word followed by word: add space
                output.append(' ')
            # else, word followed by punctuation: no space

So this should handle all cases.

Putting all together:

Read the input, process the tokens, then build the output.

Now, test the code against the first example.

Sample Input 1:

hello ,i AM veRy GooD.Boris

Tokenization step:

The input is 'hello ,i AM veRy GooD.Boris'.

Processing each character:

- 'h' → current_word becomes ['h']

... until 'hello' is formed. Then space is encountered. current_word is non-empty, so add 'hello' to tokens. current_word is reset.

Then space is skipped.

Then comma is encountered. Since current_word is empty, add comma to tokens.

Then 'i' is part of the current_word. Then space is encountered. current_word has 'i' → add to tokens. Then spaces are skipped.

Then 'AM' → current_word is ['A', 'M'] → when space is encountered, add 'AM' to tokens.

Then 'veRy' → added as a word.

Then 'GooD' → added as a word. Then '.' → add 'GooD' to tokens, add '.' to tokens.

Then 'Boris' → added to tokens.

So tokens list is:

['hello', ',', 'i', 'AM', 'veRy', 'GooD', '.', 'Boris']

Processing case:

new_sentence is True.

First token is 'hello' → new_sentence is True → 'Hello'. new_sentence becomes False.

Then comma → added as ',', new_sentence remains False.

Then 'i' → lowercase → 'i'.

Then 'AM' → lowercase → 'am'.

Then 'veRy' → 'very'.

Then 'GooD' → 'good'.

Then '.' → added, new_sentence becomes True.

Then 'Boris' → new_sentence is True → 'Boris' becomes 'Boris' (capitalized first letter, others lowercase).

processed_tokens = ['Hello', ',', 'i', 'am', 'very', 'good', '.', 'Boris']

Then generate output:

i=0: current 'Hello', next is ',' → add 'Hello' to output. Since next is punctuation (comma), no space. So output is ['Hello'].

i=1: current ',' → add to output. Next is 'i' → add space. Output becomes ['Hello', ',', ' '].

i=2: current 'i' → add. Next is 'am' → add space. Output ['Hello', ',', ' ', 'i', ' '].

i=3: current 'am' → next is 'very' → add space. Output appends 'am '.

i=4: current 'very' → next is 'good' → add space. Appends 'very '.

i=5: current 'good' → next is '.' → no space. Appends 'good'.

i=6: current '.' → next is 'Boris' → add space. Appends '.' and ' '.

i=7: current 'Boris' → no next token. Appends 'Boris'.

Final output list is ['Hello', ',', ' ', 'i', ' ', 'am', ' ', 'very', ' ', 'good', '.', ' ', 'Boris'].

When joined, this becomes "Hello, i am very good. Boris" which matches the sample.

Another test case: input 'a. b,   C  .' → output 'A. B, c.'

Tokenization:

After processing:

tokens are ['a', '.', 'b', ',', 'C', '.']

Processing case:

a → new_sentence True → 'A'. new_sentence becomes False.

. → added, new_sentence True.

b → new_sentence True → 'B'. new_sentence False.

, → added. new_sentence still False.

C → new_sentence False → 'c'.

. → added, new_sentence True.

processed_tokens = ['A', '.', 'B', ',', 'c', '.']

Spacing:

i=0: current 'A' → next is '.' → no space. output 'A.'

i=1: current '.' → next 'B' → add space → 'A. '.

i=2: current 'B' → next ',' → no space. output 'A. B,'.

i=3: current ',' → next 'c' → add space → 'A. B, '.

i=4: current 'c' → next '.' → no space. output 'A. B, c.'.

i=5: current '.' → no next token. done.

Result is 'A. B, c.'.

Which matches the sample.

Now, code.

But need to handle the tokenization correctly. Also, edge cases like leading or trailing spaces.

Another edge case: input is '   test.   ' → after stripping, 'test.'. Tokenization is ['test', '.']. Processed tokens: ['Test', '.']. Output 'Test.'.

Another case: input 'a, a. a' → tokens ['a', ',', 'a', '.', 'a'] → processed as 'A, a. A' → output 'A, a. A'.

So the code seems to handle that.

Now, code.

Let me code the steps:

Read input s.

But the input may have leading or trailing spaces. So first, process s as is.

Then tokenize into tokens.

Then process case.

Then build output.

Putting all together:

s = input().strip()  # remove leading/trailing spaces

tokens = []
current_word = []
for c in s:
    if c.isalpha():
        current_word.append(c)
    elif c in {',', '.'}:
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
        tokens.append(c)
    else:  # space
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
# Add remaining current_word if any
if current_word:
    tokens.append(''.join(current_word))

processed_tokens = []
new_sentence = True

for token in tokens:
    if token in {',', '.'}:
        processed_tokens.append(token)
        if token == '.':
            new_sentence = True
    else:
        # it's a word
        if new_sentence:
            processed_word = token[0].upper() + token[1:].lower() if token else ''
            processed_tokens.append(processed_word)
            new_sentence = False
        else:
            processed_tokens.append(token.lower())

output = []
for i in range(len(processed_tokens)):
    current = processed_tokens[i]
    output.append(current)
    if i < len(processed_tokens) - 1:
        next_token = processed_tokens[i+1]
        if current in {',', '.'}:
            output.append(' ')
        else:
            if next_token not in {',', '.'}:
                output.append(' ')

result = ''.join(output)
print(result)

Testing this code with the examples.

First sample input:

hello ,i AM veRy GooD.Boris → tokens after processing:

['hello', ',', 'i', 'AM', 'veRy', 'GooD', '.', 'Boris']

processed_tokens after case:

['Hello', ',', 'i', 'am', 'very', 'good', '.', 'Boris']

output list becomes:

['Hello', ',', ' ', 'i', ' ', 'am', ' ', 'very', ' ', 'good', '.', ' ', 'Boris']

joined → "Hello, i am very good. Boris"

Second example:

a. b,   C  . → tokens are ['a', '.', 'b', ',', 'C', '.']

processed_tokens → ['A', '.', 'B', ',', 'c', '.']

output list:

['A', '.', ' ', 'B', ',', ' ', 'c', '.']

joined → "A. B, c."

Which is correct.

Another test case: input '   .a.   ' → but the input is invalid according to the problem's constraints. But the code would process it. However, the problem says that between punctuation marks there is a letter. But the code may handle it as per the input.

But the problem states that the input is guaranteed to meet certain conditions (like at least one letter between punctuation marks). So the code doesn't have to handle invalid cases.

Thus, this code should work correctly.
</think>

```python
s = input().strip()

tokens = []
current_word = []
for c in s:
    if c.isalpha():
        current_word.append(c)
    elif c in {',', '.'}:
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
        tokens.append(c)
    else:
        if current_word:
            tokens.append(''.join(current_word))
            current_word = []
if current_word:
    tokens.append(''.join(current_word))

processed_tokens = []
new_sentence = True
for token in tokens:
    if token in {',', '.'}:
        processed_tokens.append(token)
        if token == '.':
            new_sentence = True
    else:
        if new_sentence:
            processed_word = token[0].upper() + token[1:].lower() if token else ''
            processed_tokens.append(processed_word)
            new_sentence = False
        else:
            processed_tokens.append(token.lower())

output = []
for i in range(len(processed_tokens)):
    current = processed_tokens[i]
    output.append(current)
    if i < len(processed_tokens) - 1:
        next_token = processed_tokens[i + 1]
        if current in {',', '.'}:
            output.append(' ')
        else:
            if next_token not in {',', '.'}:
                output.append(' ')

print(''.join(output))
```