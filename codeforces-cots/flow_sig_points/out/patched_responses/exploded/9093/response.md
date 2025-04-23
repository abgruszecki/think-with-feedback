<think>
Okay, let's tackle this problem. Hmm. So the task is to process a program written in this VPL language and determine which catch block's message gets displayed when a throw happens. Let's think through the requirements.

First, the program has exactly one throw. We need to find the right catch block that handles this exception. The rules are a bit specific. The activated catch must satisfy two conditions: its try is before the throw, and its catch is after the throw. Also, among all such possible catch blocks that match the exception type, we choose the one that appears earliest (i.e., the catch that was declared first in the code).

Wait, no. Wait, the problem says: when the exception is thrown, we look for the try-catch block where the try is before the throw, the catch is after the throw, and the catch's exception type matches the thrown type. Among all such blocks, the one whose catch operator is the earliest (i.e., the one that's encountered first when processing the program) is selected. Or wait, no. Let me check the problem statement again.

The problem statement says: "the system activates the block whose catch operator occurs earlier than others." So, when there are multiple possible blocks that could handle the exception (their try is before throw, catch is after throw, and their type matches), the one whose catch comes first in the program order is the one chosen. So among those valid candidates, the earliest catch in the code is picked.

So the steps are:

1. Find the throw statement in the code. Get the exception type 'a' from it.
2. For all try-catch blocks:
   a. The try is before the throw line.
   b. The catch is after the throw line.
   c. The catch's exception type matches 'a'.
3. Among all such blocks, select the one with the earliest catch in the code. Then output its message.
4. If no such block exists, output "Unhandled Exception".

So, how do we model this? Let's think about the structure of the code.

Each try must be matched with a catch. So when parsing the code, each try is pushed onto a stack. Each catch pops the last try from the stack, and records the try and catch line numbers, along with the exception type and message.

Wait, but the problem requires that each catch is the closing of the last open try. So the try-catch blocks are properly nested, like a stack structure.

So, for each line in the code, we can parse whether it's a try, catch, or throw. For each catch, we can record which try it's associated with. Then, for each try-catch block, we can store the line numbers of the try and catch, the exception type, and the message.

Once we have all the try-catch blocks, and the throw's line and exception type, we can process the possible candidates.

So, the approach would be:

- Parse each line to identify its type (try, catch, throw).
- For each catch, when parsed, associate it with the most recent try (since they form a pair).
- Keep track of all the try-catch blocks, each with their try line, catch line, exception type, and message.
- Find the throw line's position (there's exactly one) and get the exception type 'a'.
- For each try-catch block:
   Check if the try line is before the throw line.
   Check if the catch line is after the throw line.
   Check if the exception type matches 'a'.
   If all true, add to candidates.
- Among all candidates, select the one with the earliest catch line. That's the first one in the code order among the candidates. Because the earliest catch line would be the first such block that's processed.
- If there are no candidates, output the unhandled message.

So, the key steps are:

1. Parsing each line correctly to extract the necessary information.
2. Building the list of try-catch blocks with their line numbers and exception details.
3. Finding the throw line and the exception type.
4. Filtering the try-catch blocks based on the criteria and selecting the earliest catch.

Now, let's think about parsing each line.

Each line can be:

- try: starts a try block.
- catch(..., ...): closes the latest try. We need to parse the exception type and message.
- throw(...): which contains the exception type.

But lines can have leading/trailing spaces, and the catch and throw lines may have spaces around brackets, commas, etc.

So for example, a line like "catch ( BE , "BE in line 3" ) " is a valid catch line. We need to parse the exception type as BE, message as BE in line 3.

So, parsing steps:

For a line, first, strip leading and trailing whitespace. If the line is empty after stripping, ignore.

Then, check if the line starts with 'try', 'catch', or 'throw'.

For 'try' lines: it's a try statement. Push to a stack.

For 'catch' lines: parse the parameters. Extract the exception type and message.

The catch line syntax is catch ( exception_type , "message" ). So after 'catch', there's a parameter list inside parentheses, separated by comma. The first parameter is the exception type (possibly with spaces around), the second is the message (enclosed in quotes, possibly with spaces around the quotes).

Similarly for throw: throw ( exception_type )

So, for parsing a catch line:

- Remove any leading 'catch' and then process the rest.

For example, after stripping the line and checking it's a catch, the part inside the parentheses is processed.

So, for a line like 'catch ( AE , "AE somewhere" )', the inner part is 'AE , "AE somewhere" '.

Split on commas (but considering possible spaces around commas), so the first part is the exception type, the second is the message.

But how to parse this correctly, considering possible spaces?

One approach is to split the parameters inside the parentheses. Let's extract the contents between the parentheses first.

So, for a catch line:

- The entire line after stripping is something like 'catch(...)'.
- So, split on '(', then split on ')', take the part in between. That's the parameters.
- Split that parameters part into two parts: exception type and message.

But how to split correctly. Let's take the parameters string and split on commas, ignoring commas inside quotes. Wait, but the message is in quotes, and the parameters are two: exception type and message.

So, for a catch line, the parameters are (exception_type, message). So for example, the parameters part could be ' BE , "BE in line 3" '.

So, split into two parts: first part is exception type, second is message.

Processing:

- Remove all whitespace except inside the message. Wait, the exception type is a non-empty string of letters. So, for the first parameter, any spaces around it can be stripped, then the exception type is the remaining string.

For example, in ' BE ', the exception type is 'BE'.

For the message, it's enclosed in quotes, but the quotes are stripped. Also, the message can have spaces. So, for the second parameter, after splitting on the comma, we take the part inside the quotes.

But splitting on commas may not work if the comma is inside the message. Wait, no, because the message is in quotes, but the parameters are two. So the parameters are two, separated by a comma. So for example, the parameters part is exception_type, "message".

So, we can split the parameters into two parts, splitting on commas but only the first comma.

So:

params_str = ... (the part inside the parentheses)
params = [part.strip() for part in params_str.split(',', 1)]

So for example, for ' AE , "AE somewhere" ', split into two parts: 'AE' and '"AE somewhere"'.

Then, the exception type is 'AE'.

The message is the part after the first comma, stripped of whitespace, then the quotes are removed. For example, the second part is '"AE somewhere"'. So we can strip any whitespace, then take the part inside the quotes. The message is 'AE somewhere'.

Similarly for the throw line: extract the exception type, which is inside the parentheses. So the parameters part is ' CE ', so exception type is 'CE'.

So, during parsing:

For each line:

1. Strip leading and trailing whitespace. If empty, skip.
2. Check the first word:
   - 'try': record as a try, push to the stack.
   - 'catch': parse the parameters. Pop the latest try from the stack (since catch must close the last open try). Record the try line number (the line of the 'try' that was pushed to the stack), catch line number (current line's index), exception type, message.
   - 'throw': parse the exception type. Record this line's index and the exception type. Since there's exactly one throw, we can note this as we parse.

Now, the stack of tries: each time a 'try' is encountered, push its line number (the line index, starting from 0) onto the stack. When a 'catch' is encountered, pop the top of the stack (the corresponding 'try') and create a try-catch block with try line, catch line, exception type, message.

This way, each catch is paired with the correct try.

Once all lines are parsed, we have:

- A list of all try-catch blocks (each with try_line, catch_line, exception_type, message).
- The throw_line and exception_type.

Then, for each try-catch block, check:

try_line < throw_line (since try must be before throw)
catch_line > throw_line (since catch must be after throw)
exception_type matches the thrown type.

If all these are true, the block is a candidate.

From the candidates, select the one with the smallest catch_line (earliest in the code), because that's the first catch that meets the criteria. Among all candidates, the earliest catch_line is the first one that can handle the exception, per the problem statement.

If there are no candidates, output 'Unhandled Exception'.

So, the steps in code:

1. Read n lines from input.

But note that the input lines can have leading/trailing spaces, and empty lines.

But the problem says each line contains no more than one operator. So, for each line in the input, after stripping, it's either empty (no operator), or contains exactly one operator (try, catch, throw).

So during parsing:

Process each line, even empty ones. Because the line numbers matter (the line indexes in the original code). For example, a throw in line 3 (0-based or 1-based? The problem's examples use line numbers starting from 1? Let's see the first example:

In the first sample input:

The throw is on line 3 (the third line after the first line n=8). So the input is 8 lines, but after the first line (n=8), the next 8 lines are the program. So in the code, line 0 is the first program line (since the first line is n). Wait, the input format says:

The first line is n. Then n lines follow. So the lines are 0-based in the code (assuming that we read the n lines after the first as the program lines). So the code lines are 0 to n-1.

Wait, in the first sample input, the input is:

8
try
try
throw ( AE )
catch ( BE, "BE in line 3")
try
catch(AE, "AE in line 5")
catch(AE,"AE somewhere")

So the n=8. Then the next 8 lines are the program. So lines 0 to 7 (0-based). The throw is on line 2 (third line after the first). The output says the first sample's answer is 'AE somewhere'. Which is the last catch in the code. Let's see:

In the first sample, the throw is at line 2 (0-based). Then the try-catch blocks:

The first try is line 0, catch line 3 (BE). The second try is line 1, catch line 6 (AE). The third try is line 4, catch line 5 (AE). Then there's another catch line 7 (AE).

Wait, but when the program is parsed:

Line 0: try → push 0 to stack.

Line 1: try → push 1 to stack.

Line 2: throw (AE).

Line3: catch (BE) → pops the try line 1. So this try-catch is try line 1, catch line3, type BE.

Line4: try → push 4.

Line5: catch(AE) → pops 4. So this try-catch is try line4, catch line5, type AE.

Line6: catch(AE) → pops the next try. Wait, after line0's try is pushed, then line1's try. When line3's catch is processed, it pops line1's try. Then line4's try is pushed. Then line5's catch pops line4's try.

Then line6's catch would pop the next try in stack, which is line0's try. So the try-catch block for line0's try has catch line6? Or wait, perhaps I'm getting the order wrong.

Let me re-examine the first sample's code lines:

Line 0: try → stack is [0]

Line1: try → stack [0,1]

Line2: throw → stack remains as is.

Line3: catch → pop 1. So this catch is for try line1. The exception type is BE, message "BE in line3".

Line4: try → stack [0,4]

Line5: catch → pop4. This catch is for try line4, type AE, message "AE in line5".

Line6: (assuming it's the next line) → perhaps no, the sample code shows 8 lines after n=8. Wait the first sample's input after n=8 is 8 lines. Let's count:

After the first line (8), the next 8 lines are:

1. try
2. try
3. throw ( AE )
4. catch ( BE, "BE in line 3")
5. try
6. catch(AE, "AE in line 5")
7. catch(AE,"AE somewhere")

Wait, those are 7 lines. Oh, maybe the sample input is missing a line. Wait in the first sample input as given:

The input is:

8
try
try
throw ( AE )
catch ( BE, "BE in line 3")
try
catch(AE, "AE in line 5")
catch(AE,"AE somewhere")

Wait, that's 8 lines after the first line. Let's count:

Line 0 (after n=8): try

Line1: try

Line2: throw ( AE )

Line3: catch ( BE, "BE in line 3")

Line4: (empty line?)

No, wait the input as written in the first example:

The input is:

8

Then 8 lines:

1. try

2. try

3. throw ( AE )

4. catch ( BE, "BE in line 3")

5. (empty line?)

6. try

7. catch(AE, "AE in line 5")

8. catch(AE,"AE somewhere")

But the code in the first sample's input is written as:

The code lines are:

Line 0: try

Line1: try

Line2: throw ( AE )

Line3: catch ( BE, "BE in line 3")

Line4: (empty?)

Line5: try

Line6: catch(AE, "AE in line 5")

Line7: catch(AE,"AE somewhere")

Assuming that after line3 there's an empty line (as per the code in the input example, perhaps). But the input may have empty lines. So in this case, the stack processing would be as follows:

When line3 is processed (catch), it pops the top of the stack (the latest try, which is line1's try). So the try-catch block for line1 is catch line3 (BE).

Then line4 is processed: maybe empty. So skipped.

Line5 is try → push to stack. Stack becomes [0,5].

Line6 is catch → pops 5 → try line5, catch line6, exception type AE, message "AE in line5".

Line7 is catch → pops 0 → try line0, catch line7, exception type AE, message "AE somewhere".

So, when the throw is on line2 (0-based), the candidates are:

We need to find try-catch blocks where try_line < 2, catch_line > 2, and exception_type is AE.

The candidates are:

For the catch line3: exception type BE → no.

The catch line6: try_line5 (which is line5, which is after the throw line2 → no. Wait, line5's try is line5 (the 6th line in the code?), which is after line2. So no.

Wait, line5 is the try in line5 (the code line with index5). Since the throw is at line2, any try after line2 would not be considered. So the try for line5 is at line5, which is after the throw at line2. So no.

The catch line7's try is line0 (code line0). The catch line is7, which is after throw line2. The exception type is AE. So this is a candidate.

But what about the catch line3's try (line1) → try line1 is before throw line2. Catch line3 is after throw line2. But the exception type is BE. So only if the thrown exception is AE, that's not a candidate.

So the only candidate is the catch line7 (try line0, catch line7, type AE).

So the message is 'AE somewhere', which matches the sample.

So the approach works.

So the code steps:

We need to process each line, track the stack of try's, parse each catch and throw.

Once we have all the try-catch blocks, and the throw's line and type, we can filter.

Now, for code in Python:

We can loop through each line, track the stack, parse the lines.

So first, read n lines. Then process each line.

But the input may have empty lines, but each line (after the first) is part of the program.

So code steps:

Read n.

Then read n lines.

Then, for each line in these n lines (0-based index is their line number in the program):

Process each line.

We need to track:

- The stack for try blocks: a list of line numbers where 'try' occurred.

- A list of all try-catch blocks: each is a tuple (try_line, catch_line, exc_type, message).

- The throw_line and throw_type: once found, set these variables.

So code:

stack = []
try_catch_blocks = []
throw_line = -1
throw_type = ''

for line_num in range(n):
    line = input().strip()
    if not line:
        continue
    if line.startswith('try'):
        # push the line number to stack
        stack.append(line_num)
    elif line.startswith('catch'):
        # parse the catch parameters
        # check if stack is not empty (per problem statement, the input is correct)
        try_line = stack.pop()
        # extract the parameters
        # line is 'catch ( ... )', etc.
        # split into parts after 'catch', then extract between parentheses
        # split after 'catch' to get the parameters
        # first, find the index of '('
        param_start = line.find('(')
        param_end = line.rfind(')')
        params_str = line[param_start+1 : param_end].strip()
        # split into exception type and message
        params = [p.strip() for p in params_str.split(',', 1)]
        exc_type = params[0]
        message = params[1].strip()
        # message is in quotes, so remove the quotes
        # split on " then take the middle part
        # message is in the form "..." or " ... " with possible spaces around the quotes
        # so first, strip whitespace, then split on first " and last " ?
        # better to use split on '"' and take the parts between.
        # example: ' "AE somewhere" ' → split on " → ['', 'AE somewhere', '']
        message_parts = [s for s in params[1].split('"') if s.strip() != '']
        # message_parts may be empty?
        # assuming the input is correct, the message is properly quoted.
        # so take the first part that's not empty.
        # or after splitting, the non-empty parts are the message.
        # for example, if the message is "hello", the split gives ['', 'hello', ...] → message is 'hello'
        # so:
        msg = ''
        in_quotes = False
        current = []
        for c in params[1]:
            if c == '"':
                if in_quotes:
                    msg = ''.join(current)
                    break
                else:
                    in_quotes = True
                    current = []
            elif in_quotes:
                current.append(c)
        # so after extracting, msg is the message
        # Alternatively, using split:
        parts = params[1].split('"')
        # between the first and second " is the message.
        # for example: ' "abc" ' → split into ['', 'abc', '' ] → parts[1] is 'abc'
        # but if the input is ' "a b c" ', split into ['', 'a b c', ... ] → parts[1] is 'a b c'
        # so the message is parts[1]
        msg = parts[1].strip() if len(parts) >= 2 else ''
        # but need to make sure that the message is properly enclosed in quotes. However, the problem says the input is correct, so this should work.
        try_catch_blocks.append( (try_line, line_num, exc_type, msg) )
    elif line.startswith('throw'):
        # parse the exception type
        # line is 'throw ( AE )' → extract 'AE'
        param_start = line.find('(')
        param_end = line.rfind(')')
        exc_type = line[param_start+1 : param_end].strip()
        throw_line = line_num
        throw_type = exc_type

Once we have all the try_catch_blocks and the throw_line and throw_type, we can process the candidates.

Now, filter the try_catch_blocks:

candidates = []
for block in try_catch_blocks:
    try_line, catch_line, exc_type, msg = block
    if try_line < throw_line and catch_line > throw_line and exc_type == throw_type:
        candidates.append( block )

Then, among the candidates, find the one with the smallest catch_line (earliest in code order).

If there are candidates, select the one with the earliest catch_line. Output the message.

Else, output 'Unhandled Exception'.

So, code:

if candidates:
    # sort by catch_line and pick the first one
    # since the first in code order is the one with the smallest catch_line.
    candidates.sort(key=lambda x: x[1])
    print(candidates[0][3])
else:
    print("Unhandled Exception")

Wait, but candidates could be in any order. The code sorts them by catch_line and picks the first, which is the earliest catch_line. That's correct.

Wait, but the list could be in the order of the try_catch_blocks. Since try_catch_blocks are added in the order they are parsed (i.e., in the order of their catch lines), but in the code, a catch may have a catch_line that is earlier than others. For example, two try-catch blocks: one with catch_line 5 and another 3. So when the candidates are both valid, the one with catch_line 3 is earlier and should be selected.

Sorting the candidates by catch_line and selecting the first will work.

So code is okay.

Now, let's test this approach against the sample input.

First sample:

throw_line is 2 (0-based?), throw_type is AE.

The try_catch_blocks are:

For the first try (line0) and catch line3 (BE), but exc_type BE.

Another try (line1) and catch line3 (BE), but exc_type BE. Wait no, the first sample's code may have more try-catch blocks.

Wait, perhaps I should re-examine the code parsing.

In the first sample, the code lines are:

Lines 0: try → push 0.

Line1: try → push 1.

Line2: throw.

Line3: catch → pop 1 (try_line=1). So this block is try_line 1, catch_line3, exc_type BE.

Line4: try → push 4.

Line5: catch → pop 4. exc_type AE, message "AE in line5".

Line6: catch → pop 0. exc_type AE, message "AE somewhere".

So the try_catch_blocks would be:

(1,3, BE, "BE in line 3")

(4,5, AE, "AE in line5")

(0,6, AE, "AE somewhere")

Wait, but when line3 is processed as a catch, it pops the try_line 1 (since stack was [0,1] before processing line1). So the block is try_line 1, catch_line3.

Then line4: try, pushed to stack (now stack is [0,4]).

Line5: catch, pops 4. So try_line4, catch_line5.

Line6: catch, pops 0. So try_line0, catch_line6.

So the blocks are:

(1,3, BE, ...)

(4,5, AE, ...)

(0,6, AE, ...)

Now, throw_line is line2 (0-based?), throw_type is AE.

For each block:

Check try_line < 2, catch_line>2.

Block1: try_line1 <2 → yes. catch_line3>2 → yes. exc_type BE != AE → no.

Block2: try_line4 >2 → no.

Block3: try_line0 <2 → yes. catch_line6>2 → yes. exc_type AE == AE → yes.

So this is a candidate. So the candidate is the third block. Its message is "AE somewhere".

Which matches the first sample.

So the code works.

Now, for the second sample:

throw_line is line2 (0-based?), exception type AE.

try_catch_blocks are:

After processing:

Line3's catch: try_line1, catch_line3, exc_type AE, message "AE in line3".

Line6's catch: try_line0, catch_line6, exc_type AE, message "AE somewhere".

So during filtering:

Block1: try_line1 <2 → yes. catch_line3>2 → yes. exc_type AE → yes. So candidate.

Block2: try_line0 <2 → yes. catch_line6>2 → yes. exc_type AE → yes.

So two candidates. Their catch_lines are 3 and6. The earliest is 3. So the message is "AE in line3".

Which matches the sample.

So the code works.

Third sample: exception type CE. No candidates. Output "Unhandled".

Now, for parsing the message. The code for parsing the message may have issues.

For example, in a line like 'catch( AE , " AE somewhere  " )' → the message is ' AE somewhere  ' (stripped of quotes, but the spaces inside are kept). Wait, the problem statement says that the message is surrounded by quotes and the quotes shouldn't be printed. So the code needs to extract the exact content inside the quotes, including leading and trailing spaces. For example, if the message is "  Hello World  ", the output should be "  Hello World  ".

So in the code, when extracting the message, we need to split on the quotes and take the part between them.

In the code, we have:

For the message part, after splitting params[1] on '"' and taking parts[1]. So for params[1] being ' " AE somewhere " ', the split would be ['', ' AE somewhere ', ... ] → parts[1] is ' AE somewhere ', which has leading and trailing spaces. So the message is that string. But according to the problem statement, the message is surrounded by quotes, which should not be printed. So the code correctly takes the content inside the quotes, including any spaces.

So the code for parsing the message is correct.

Now, considering that the code must be efficient for n up to 1e5. So the code must process each line in O(1) time, and then filter the try_catch_blocks, which can be up to O(n) in the worst case (if all lines are try and catch). But 1e5 is manageable.

The code uses a list to collect try_catch_blocks and then filters them. For n=1e5, this is O(n) time. Then the candidates are sorted, which in the worst case could be O(k log k), where k is the number of candidates. But in practice, k is likely small. But even if k is 1e5, sorting would be O(1e5 log 1e5), which is acceptable for Python in 2 seconds.

Wait, but in Python, for 1e5 elements, sorting takes about 0.1 seconds. So even in worst case, it's manageable.

Alternatively, to avoid sorting, we can track the best candidate (the one with the earliest catch_line) as we process each block. This would save some time. Since for each candidate, we check if it's better than the current best.

So, instead of collecting all candidates and sorting, we can:

Initialize best_catch_line = infinity (like a very large number), best_message = None.

For each block in try_catch_blocks:

   if block meets criteria:

       if block's catch_line < best_catch_line:

           best_catch_line = block.catch_line

           best_message = block.msg

So, after processing all blocks, if best_message exists, output it. Else, unhandled.

This is O(k) time, which is better. So this optimization is better.

So the code can be adjusted.

So in the code:

best_catch_line = float('inf')

best_msg = None

for block in try_catch_blocks:

    try_line, catch_line, exc_type, msg = block

    if try_line < throw_line and catch_line > throw_line and exc_type == throw_type:

        if catch_line < best_catch_line:

            best_catch_line = catch_line

            best_msg = msg

if best_msg is not None:

    print(best_msg)

else:

    print("Unhandled Exception")

This would be more efficient, as it avoids sorting.

So this is better.

So, the code now is:

Parse all lines, collect try_catch_blocks.

Find the throw line and type.

Loop through try_catch_blocks, check criteria, and track the earliest catch_line.

Thus, the code is O(n) time, which is acceptable.

Now, edge cases.

Case where multiple candidates have the same catch_line. But the problem says that the program is correct, but there could be multiple try-catch blocks with same catch_line. But per the problem statement, the code is correct. So maybe no, because each catch is paired with a try. So each catch_line is unique. So no.

Another edge case: the throw occurs in the first line. So no try can be before it. So output is unhandled.

Another case: the throw occurs in line 0 (the first line of the program). Then no try can be before it. So no candidates.

Another case: the throw is on line 5. A try is line4, catch line6. So if the exception type matches, this is a candidate.

So code seems correct.

Now, code implementation.

Parsing the lines correctly is crucial.

Testing the code with sample input 1:

Sample input 1:

8

try

try

throw ( AE )

catch ( BE, "BE in line 3")

try

catch(AE, "AE in line 5")

catch(AE,"AE somewhere")

So the lines (after n=8) are:

Line0: 'try' → push 0.

Line1: 'try' → push 1.

Line2: 'throw ( AE )' → parsed as AE. throw_line=2.

Line3: 'catch ( BE, "BE in line 3")' → params_str after split: 'BE' and "BE in line 3".

Message is 'BE in line 3'.

This catch_line is3. try_line is1.

Line4: empty line → skip.

Line5: 'try' → push 4 (line5's index is5? Or wait, after the throw line is line2, which is the third line after the first line (n=8). So the line numbers are 0-based.

Yes, the lines after the first are 0-based. So line3 is the fourth line (index3).

So line3 is processed as catch. Pop try_line1. So the try-catch block is (1,3, BE, 'BE in line3').

Line4: empty.

Line5: 'try' → line5's index is5. push to stack → stack becomes [0,5].

Line6: 'catch(AE, "AE in line5")' → pop 5. try_line5 (line5), catch_line6. exc_type AE. message 'AE in line5'.

Line7: 'catch(AE,"AE somewhere")' → pop0. try_line0, catch_line7. exc_type AE. message 'AE somewhere'.

So the try_catch_blocks are:

(1,3, 'BE', 'BE in line3')

(5,6, 'AE', 'AE in line5')

(0,7, 'AE', 'AE somewhere')

Now, throw_line=2, throw_type=AE.

Check each block:

Block (1,3, BE): exc_type BE != AE → no.

Block (5,6, AE): try_line5 >2 → no.

Block (0,7, AE): try_line0 <2, catch_line7>2 → yes. So this is a candidate. So best_catch_line is7. No other candidates, so message is 'AE somewhere'.

Sample 1's output is correct.

Sample2:

In the second sample input:

The throw is line2 (0-based), type AE.

The try_catch_blocks include:

After line3: catch (AE, ...) → try_line1, catch_line3.

Another catch line7 (try_line0, catch_line7, AE).

So during filtering:

Block (1,3, AE) is a candidate.

Block (0,7, AE) is a candidate.

The best_catch_line is3. So output is the message from block3.

Sample3: no matching exc_type, so output unhandled.

So code works.

Now, code in Python:

Handle the parsing of catch and throw lines correctly.

Now, code steps:

Read n.

Read n lines, but in Python, after input().readlines() may have '\n's. But using input().strip() for each line is better.

Wait, but the lines may have leading and trailing spaces. So read each line as is, then process.

But in Python, for each line, we can read as:

lines = [input().strip() for _ in range(n)]

But this strips leading and trailing spaces. But the problem states that the input can have lines that are empty (after stripping), but each line contains no more than one operator. So processing each line as stripped is correct.

But wait, the problem says that the input lines can have spaces at the beginning, end, etc. So for example, a line like '  try  ' is a try operator.

But after stripping, it's 'try', which is processed correctly.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    stack = []
    try_catch_blocks = []
    throw_line = -1
    throw_type = ''

    n = int(input_stream.readline().rstrip("\n"))
    for line_num in range(n):
        line = input_stream.readline().rstrip("\n").strip()
        if not line:
            continue
        if line.startswith('try'):
            stack.append(line_num)
        elif line.startswith('catch'):
            # parse catch
            if not stack:
                # according to problem statement, input is correct, so stack is not empty
                pass  # should not happen
            try_line = stack.pop()
            # parse params
            param_start = line.find('(')
            param_end = line.rfind(')')
            params_str = line[param_start+1 : param_end].strip()
            params = [p.strip() for p in params_str.split(',', 1)]
            exc_type = params[0]
            # parse message
            msg = ''
            parts = params[1].split('"')
            for i in range(1, len(parts)):
                if parts[i-1].strip() == '':
                    msg = parts[i]
                    break
            # parts after splitting on " will have the message in parts[1]
            # if parts has more than one element, parts[1] is the message.
            # for example: "abc" → split into ['', 'abc', '']
            # for example: '  "abc" ' → split into ['  ', 'abc', ' ']
            # so find the first part that is non-empty after splitting.
            # alternative:
            # parts = params[1].split('"')
            # for part in parts:
            #     if part.strip() != '':
            #         # not the message part
            #         pass
            # So the message is the first part between quotes.
            # So, the message is parts[1], but leading and trailing spaces in the quotes are preserved.
            # So code can be:
            # msg = parts[1] if len(parts) >=2 else ''
            # but to handle cases where there are multiple quotes (invalid per problem statement, but input is correct)
            # So, perhaps split on " and take the first part that is in between.
            # For example, in params[1] = ' "msg" ', split gives [' ', 'msg', ' '], so parts[1] is 'msg'.
            # So code:
            if len(params) <2:
                msg = ''
            else:
                msg_part = params[1].strip()
                if msg_part.startswith('"'):
                    msg = msg_part[1:-1] if msg_part.endswith('"') else msg_part[1:]
                else:
                    # split on quotes
                    parts = msg_part.split('"')
                    if len(parts) >=2:
                        msg = parts[1]
                    else:
                        msg = ''
            # So better to use the following approach:
            # Split on " and find the part inside the quotes.
            parts = params[1].split('"')
            msg = ''
            found = False
            for i in range(len(parts)):
                if i % 2 == 1:  # inside quotes
                    msg = parts[i]
                    found = True
                    break
            if not found:
                msg = ''
            try_catch_blocks.append( (try_line, line_num, exc_type, msg) )
        elif line.startswith('throw'):
            # parse throw
            param_start = line.find('(')
            param_end = line.rfind(')')
            exc_type = line[param_start+1 : param_end].strip()
            throw_line = line_num
            throw_type = exc_type

    # Now process the try_catch_blocks
    best_catch_line = float('inf')
    best_msg = None

    for try_line, catch_line, exc, msg in try_catch_blocks:
        if try_line < throw_line and catch_line > throw_line and exc == throw_type:
            if catch_line < best_catch_line:
                best_catch_line = catch_line
                best_msg = msg

    if best_msg is not None:
        print(best_msg, file=output_stream)
    else:
        print("Unhandled Exception", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
try
try
throw ( AE )
catch ( AE, "AE in line 3")
try
catch(BE, "BE in line 5")
catch(AE,"AE somewhere")
""",
            "output": \
"""\
AE in line 3
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

Another example: catch line with message "  Hello  " → parsed as '  Hello  '.

The code should extract the message correctly.

So the code for parsing the message is:

parts = params[1].split('"')

msg = ''

for i in range(len(parts)):

    if i % 2 == 1:

        msg = parts[i]

        break

This works because the first occurrence of being between quotes is the message. Even if there are multiple quotes, the problem statement says the input is correct, so the message is properly enclosed in quotes.

So the code should correctly extract the message.

Thus, the code should work.
</think>

```python
n = int(input())
stack = []
try_catch_blocks = []
throw_line = -1
throw_type = ''

for line_num in range(n):
    line = input().strip()
    if not line:
        continue
    if line.startswith('try'):
        stack.append(line_num)
    elif line.startswith('catch'):
        if not stack:
            continue
        try_line = stack.pop()
        param_start = line.find('(')
        param_end = line.rfind(')')
        params_str = line[param_start+1:param_end].strip()
        params = [p.strip() for p in params_str.split(',', 1)]
        exc_type = params[0]
        msg = ''
        parts = params[1].split('"') if len(params) > 1 else []
        for i in range(len(parts)):
            if i % 2 == 1:
                msg = parts[i]
                break
        try_catch_blocks.append((try_line, line_num, exc_type, msg))
    elif line.startswith('throw'):
        param_start = line.find('(')
        param_end = line.rfind(')')
        throw_type = line[param_start+1:param_end].strip()
        throw_line = line_num

best_catch_line = float('inf')
best_msg = None

for try_line, catch_line, exc, msg in try_catch_blocks:
    if (try_line < throw_line and
        catch_line > throw_line and
        exc == throw_type and
        catch_line < best_catch_line):
        best_catch_line = catch_line
        best_msg = msg

print(best_msg if best_msg is not None else "Unhandled Exception")
```
