<think>
Okay, let's see. I need to parse a string expression that represents function calls and then evaluate it to get the result. The functions are concat, reverse, substr (with either 3 or 4 arguments). The input is a single line, and the output is the evaluated string. The problem also says that function names are case-insensitive, but the actual string literals are case-sensitive. So, when the functions are called, their names can be in any case, like reverse or REVERSE, but when processing the parameters, the actual strings are treated as given.

First, I need to parse the input string into an abstract syntax tree or some structure that represents the nested function calls. Then evaluate that structure step by step.

The main challenge is parsing the expression correctly. Let's think about how the input is structured. The input can have nested functions. For example, reverse(substr(...)), which means that the substr is evaluated first, then reversed.

The steps I need to take:

1. Tokenize the input into components: function names, parentheses, commas, string literals, numbers, etc.
2. Parse the tokens into an abstract syntax tree (AST) representing the nested function calls and literals.
3. Evaluate the AST by applying each function in the correct order.

Tokenization:

The input can have various elements:
- Function names (case-insensitive) like concat, reverse, substr.
- Parentheses ( and ), and commas.
- String literals enclosed in quotes. These can contain uppercase and lowercase letters.
- Numbers, which can be positive or negative, but according to the problem statement, the integers used in the input are <=100 in absolute value. So numbers can have optional negative signs, and digits.

The tokenizer needs to recognize these elements. For example, when it sees a quote, it reads until the next quote (but since the input is valid, we don't need to handle invalid cases). For function names, once we see a letter followed by a parenthesis, we need to read the function name (case-insensitive). But function names can be in any case, like CONcat, reverse, etc.

But functions are part of the expression. For example, the input could be something like CONCAT(REVerse("abc"), substr("def",1,2)).

So the tokenizer needs to split the input into tokens such as:

function names (case-insensitive), '(', ')', ',', string literals (with quotes), numbers (possibly negative).

Parsing the tokens into an AST:

Once we have the tokens, the next step is to build a structure that represents the nested function calls. The root of the AST is the outermost function or the string literal if there's no function.

The parsing process can be done recursively. For example, when we encounter a function name, we process its arguments. Each argument can be a function call, a string literal, or a number.

So the parsing steps could be:

- The main expression is a term. A term can be a function call or a string literal or a number (but numbers only appear as arguments to substr).

So, the parser will look for function calls first. For example, when the current token is a function name (case-insensitive), followed by '(', then parse the arguments until ')', and then proceed.

But how to handle nested functions?

Parsing nested functions can be done using a recursive approach. For example, the arguments of a function call can themselves be function calls, which in turn have their own arguments.

So, the parsing algorithm could be something like this:

When a function is encountered, parse its arguments. Each argument is a term, which can be another function call, a string, or a number.

But how to split the arguments properly, considering commas and parentheses?

Perhaps a recursive descent parser would be appropriate here.

Let's outline the structure:

The parse function would return the current parsed term and the index of the next token.

For example, the main parse function starts at token 0. If the current token is a function name, then process the function: collect all the arguments inside the parentheses, which are separated by commas. Each argument can be parsed by recursively calling the parse function.

But wait, the arguments can be function calls, strings, or numbers. So, when parsing an argument, we need to check what the next token is. For example, an argument could start with a function name (like reverse(...)) or a string literal, or a number.

So, during parsing, when inside a function's arguments, each comma separates the arguments. So, for example, concat(reverse("abc"), substr("def",1,2)) has two arguments: the first is reverse(...), the second is substr(...).

So the steps for parsing a function call would be:

- Read the function name (case-insensitive)
- Read the '('
- Parse the list of arguments, which are separated by commas. Each argument is parsed as a term (which can be a function call, a string, or a number)
- Read the ')'

Each term can be:

- A function call (like reverse(...))
- A string literal (enclosed in quotes)
- A number (integer, possibly negative)

So, the parser needs to handle these cases.

Now, the tokenization phase is crucial.

Let's think about tokenizing:

We can process the input character by character, building tokens as we go.

Possible tokens:

1. Function names: sequences of letters (case-insensitive) followed by '('. But wait, the function name is followed by '(', but in the input, the function may be written as reverse ( with a space? No, the problem statement says that the input is a correct expression. So function names are followed by '(', and there are no spaces. Wait, the problem statement says: "It is guaranteed that the given string is non-empty." So perhaps the input is correctly formatted with no spaces except within string literals.

Wait, the problem says that the input is a correct expression. So in the input, functions are written properly. For example, substr(...) has all the required parameters.

So, the input does not contain any spaces except inside the string literals. So for example, concat ( "a", reverse ( "b" )) would have spaces between the function and the parenthesis, but according to the problem statement, it's guaranteed that the input is correct. Wait, the problem statement says: "the given expression is correct". So perhaps the input has no whitespace except within the string literals. Because in programming languages, spaces are allowed between function names and parentheses, but in the problem statement, maybe the input does not have any spaces except inside the string literals.

Wait, the problem statement's examples do not have any spaces outside the strings. For example, the second sample input is REVerse(substr("helloworld",1,5)), which has no spaces. So perhaps the input does not contain any whitespace except within string literals.

So, during tokenization, we can split the input into tokens without considering any spaces outside the strings.

Therefore, the tokenizer can process the input as follows:

Loop through each character in the input:

- If the character is a quote ( " ), then read the entire string literal until the next quote. Add this as a string token (including the quotes?), or perhaps store the content between the quotes. Wait, for example, "Hello" is a string literal, and when processing, we need to extract "Hello" as a string. So the tokenizer should capture the entire "Hello" as a string token.

Wait, for the purposes of evaluation, the string literals are the characters between the quotes. So when the tokenizer encounters a ", it reads all characters (including other quotes?) until the next unescaped quote. But the problem statement says that the input is correct. So we can assume that each " is properly closed. So the tokenizer can read from the opening " until the next ", and capture that as a string token (including the quotes). Then, when processing the string, we can extract the content (without the quotes) and process that.

So, the tokenizer will generate tokens of the following types:

- FUNCTION: the function name (case-insensitive)
- OPEN_PAREN: '('
- CLOSE_PAREN: ')'
- COMMA: ','
- STRING: the entire quoted string (e.g., "Hello")
- NUMBER: integers, which can be positive or negative.

So, the tokenizer steps:

Initialize a list of tokens.

Initialize a position pointer at 0.

While position < len(input):

   current_char = input[position]

   if current_char is a letter:

       read as long as it's a letter (case-insensitive), until we hit a non-letter (like '(' or comma or number, etc). Then, check if the next character is '('. If so, this is a function name. So the token is the function name (lowercase?), but stored as case-insensitive (like, convert to lowercase for easier handling). For example, 'reverse' becomes 'reverse', 'REVerse' becomes 'reverse', etc.

       So, for example, 'CONcat' becomes 'concat'.

       So, the function name is determined by reading all consecutive letters (case-insensitive), then check if the next character is '('. If so, it's a function name. Otherwise, perhaps it's part of a string literal? No, because strings are enclosed in quotes. So in the input, function names are followed by '(', so after reading the letters, the next character is '('.

       So, for the tokenizer, whenever a sequence of letters is followed by '(', it's a function name. Otherwise, perhaps it's part of a number or something else, but according to the problem statement, the input is correct, so this won't happen.

       So, the tokenizer can read letters until a non-letter is found, then check if that non-letter is '('. If yes, then this is a function name. Otherwise, perhaps that's invalid. But given the problem constraints, the input is correct.

   elif current_char is '(' or ')' or ',':

       add as a separate token.

   elif current_char is '"':

       read until the next '"' to form the string literal. So, starting from position 0, if current_char is ", then the string starts here. Increment position until the next " is found. The substring from start to end (inclusive) is the string token.

   elif current_char is a digit or '-' (for negative numbers):

       read the entire number. For example, '-123' is a number. So, read until we hit a non-digit (but note that after a '-', there must be digits). So, for numbers, the tokenizer can read the entire sequence of digits (including leading '-') as a number token.

       So, numbers can be positive or negative. But according to the problem statement, the integers in the input are <=100 in absolute value. So the tokenizer needs to handle negative numbers.

   else:

       but according to the problem statement, the input is correct, so this case shouldn't happen.

Once the tokens are generated, the next step is parsing.

Parsing the tokens into an AST:

The AST can be represented as nodes. For example:

- Function nodes: have a name (concat, reverse, substr), and a list of arguments (which can be other nodes or literals).

- String literals: the actual string (without the quotes).

- Numbers: integers.

So, the root of the AST is the entire expression.

The parsing can be done recursively:

Define a parse_expression function that parses a term. The term can be a function call, a string literal, or a number.

So, the parse_expression function checks the current token:

If the current token is a function name (case-insensitive), followed by '(', then parse as a function call.

Else if the current token is a string literal, extract the content between the quotes and create a string node.

Else if the current token is a number, create a number node.

But the numbers can only be arguments to substr functions, so during evaluation, they need to be checked for validity (like a and b in substr(x,a,b) must be 1-based, etc.)

So, the parser steps:

The parse_expression function starts at a certain position in the token list.

If the token is a function name:

   function_name = token's lowercase (e.g., 'reverse')

   consume the function name and the '('.

   parse the arguments list (split by commas) by recursively parsing each argument.

   consume the ')'.

   return a FunctionNode with the function name and the arguments.

If the token is a string:

   extract the content (stripping the quotes), return a StringNode.

If the token is a number:

   return a NumberNode with the integer value.

But how to track the current position in the token list during parsing? Because the recursive approach needs to know where it left off.

This suggests that the parse function should keep track of the current index in the token list, and return the parsed node and the next index.

For example, in Python:

def parse(tokens, index):

   current_token = tokens[index]

   if current_token is a function name:

       function_name = current_token.lower()

       index +=1  # consume function name

       assert tokens[index] == '(', "Expected '(' after function name"

       index +=1

       args = []

       while True:

           arg, index = parse(tokens, index)

           args.append(arg)

           if tokens[index] == ')':

               index +=1

               break

           elif tokens[index] == ',':

               index +=1

       return FunctionNode(function_name, args), index

   elif current_token is a string literal:

       content = current_token[1:-1]  # strip the quotes

       index +=1

       return StringNode(content), index

   elif current_token is a number:

       value = int(current_token)

       index +=1

       return NumberNode(value), index

But wait, the tokens list would have elements like 'concat', '(', etc.

Wait, the tokenizer would generate tokens in the following way:

For example, the input CONcat(reverse("abc"), substr("def",1,2)) would be tokenized as:

['concat', '(', 'reverse', '(', "abc", ')', ',', 'substr', '(', "def", ',', 1, ',', 2, ')', ')', ... ]

Wait, no. Let's see:

The input "REVerse(substr("helloworld",1,5))" would be tokenized as:

function name 'reverse', then '(', then 'substr' (function name), '(', then the string "helloworld", comma, 1, comma, 5, ')', ')'.

So the token list would be:

['reverse', '(', 'substr', '(', "helloworld", ',', 1, ',', 5, ')', ')'].

So, during parsing, when we parse the 'reverse' function, which takes one argument. The argument is the substr function call.

So, the parser needs to handle nested functions correctly.

Once the AST is built, the evaluation can be done recursively. Each node in the AST is evaluated to produce a value. For functions, their arguments are evaluated first, then the function is applied.

So, the evaluator function takes a node and returns the evaluated string or number (but numbers are only for substr parameters, which are then processed as indices).

Now, the functions:

concat(x, y): returns x + y.

reverse(x): returns x reversed.

substr has two forms:

substr(x, a, b) returns the substring from a to b (1-based, inclusive), step 1.

substr(x, a, b, c): returns the substring starting at a, then every c steps until b (inclusive). So characters are x[a-1], x[a-1 + c], etc., up to b-1 if necessary.

But the parameters a and b are 1-based. So, for example, substr("Hello", 2,4) is 'ell' (indices 1, 2, 3 in 0-based). So in Python, x[a-1 : b], since Python's slice is up to but not including the end index. But for the step version, it's more complicated.

Wait, the problem's description for substr with step:

substr("HelloWorld",1,10,2) returns "Hlool".

Let's see:

Original string: H e l l o W o r l d (indices 0-9)

Parameters a=1, b=10 (since the length is 10, 1-based indices are 1-10, which in 0-based is 0-9). step 2.

So starting at index 0, take every 2 steps until index 9.

So indices 0, 2, 4, 6, 8. Characters are H, l, o, o, l. Which makes "Hlool".

So the step is applied as per Python's slicing, but with inclusive end.

So in Python, the slice would be x[a-1 : b : step], but ensuring that the end is inclusive. Wait, but Python's slicing is up to but not including the end. So for example, x[0:10:2] would give indices 0, 2, 4, 6, 8. Which is correct.

So for substr(x, a, b, c) the parameters are 1-based a and b, and step c.

So the code for substr with step would be:

start = a-1

end = b-1 (since 1-based to 0-based)

But Python's slice is start : end+1 : step, because to include end.

Wait, for example, if a=1, b=10, step 2: in 0-based, start is 0, end is 9. To include up to 9, the step is 2. So the indices are 0, 2, 4, 6, 8. Which is correct.

So the slice is x[start:end+1:step].

But wait, the end parameter in Python's slice is exclusive. So x[start:end+1] would include end. So for the slice step, x[start : end+1 : step].

So the code for substr(x, a, b, c) is:

x = evaluated x (string)

a_val = a (evaluated as integer)

b_val = b (evaluated as integer)

c_val = c (evaluated as integer)

start_idx = a_val - 1

end_idx = b_val - 1

if start_idx > end_idx:

   then the step is positive, so the slice would be empty. But according to the problem statement, 1 ≤ a ≤ b ≤ len(x), so a <= b, which implies start_idx <= end_idx. So we can assume that.

So the substring is x[start_idx : end_idx+1 : c_val]. Then, take the characters in this slice.

For substr with three arguments (a, b), it's equivalent to substr(x, a, b, 1).

So the code for substr is:

if len(args) ==3 (x, a, b):

   a = a_val, b = b_val. step is 1.

elif len(args) ==4 (x, a, b, c):

   step is c_val.

Now, during evaluation, the arguments of substr must be evaluated. For example, substr(concat(...), a, b, c), the concat is evaluated first, then a, b, c (which could be numbers or expressions that evaluate to numbers).

Wait, but the arguments to substr are evaluated to their respective types. For example, in substr(x, a, b), x is a string, a and b are numbers.

So, during evaluation, when evaluating a function's arguments, each argument is evaluated first.

For example, substr(concat("a", reverse("b")), 1+2, 3) would first evaluate concat("a", reverse("b")) to get a string, then evaluate 1+2 (if it's part of the input), but according to the problem statement, the input is correct, and the functions' arguments are correct. So during evaluation, the arguments to substr must be numbers. But in the input, the numbers can be part of function arguments. For example, substr("hello", 2, 3+1) is not allowed, but according to the problem statement, the input is correct. Wait, the problem statement says that the input is a correct expression, so all the arguments to substr are numbers (literals). Because the functions do not return numbers, except substr returns a string.

Wait, the problem statement says that the expression can consist of functions and string literals. So the arguments to substr's a, b, c must be numbers, which are either literals or evaluated from other functions? No. Because functions return strings. So the arguments a, b, c must be numbers in the input. So the problem statement ensures that the input is correct, which includes that the substr's parameters are valid integers.

So, during parsing, the arguments to substr (a, b, c) would be NumberNodes (since they are integers in the input). So during evaluation, these are numbers. So, when evaluating a substr function's arguments, the first argument is a string (evaluated from a function or string literal), and the other arguments are numbers.

So, during evaluation:

For concat, arguments x and y must evaluate to strings.

For reverse, x must evaluate to a string.

For substr, the first argument must evaluate to a string, and the other arguments must evaluate to integers.

So, during evaluation, the evaluator will check the types of the arguments.

But according to the problem statement, the input is correct, so these checks can be omitted. So during the programming competition, perhaps you can assume that the input is correct, but for the problem's solution, we can process the arguments correctly.

So, the evaluator function will evaluate each node:

def evaluate(node):

   if node is a StringNode:

       return node.value

   elif node is a NumberNode:

       return node.value

   elif node is a FunctionNode:

       function_name = node.name

       args = [evaluate(arg) for arg in node.args]

       if function_name == 'concat':

           # args should be two strings.

           return args[0] + args[1]

       elif function_name == 'reverse':

           # args[0] is a string.

           return args[0][::-1]

       elif function_name == 'substr':

           x = args[0]

           a = args[1]

           b = args[2]

           step = 1

           if len(args) ==4:

               step = args[3]

           # check if a and b are valid.

           # per problem statement, 1 ≤ a ≤ b ≤ len(x), step is positive.

           # compute 0-based indices.

           start = a -1

           end = b -1

           # in Python, slice is start : end+1 : step

           substring = x[start : end+1 : step]

           return substring

       else:

           # impossible, since input is correct.

           raise ValueError("Unknown function")

So, this evaluator handles all the functions.

Putting it all together:

The steps are:

1. Read the input line.

2. Tokenize the input into functions, strings, numbers, parentheses, commas.

3. Parse the tokens into an AST.

4. Evaluate the AST to get the result string.

5. Print the result enclosed in quotes.

But wait, the output is supposed to be the result enclosed in quotes. For example, the first sample input is "HelloWorld" and the output is "HelloWorld".

Wait, looking at the examples:

Sample input 1:

Input: "HelloWorld" (the quotes are part of the input)

Output: "HelloWorld" (quotes included?)

But in the first sample's input, the output is the same as the input. So the output is the evaluated string, which is "HelloWorld" as a string literal, so it's output as "HelloWorld".

Wait, no. Wait, the problem says that the input is an expression. So the input "HelloWorld" is a string literal, and the output is that same string. But according to the sample input 1, the output is "HelloWorld".

But the output is supposed to be the resulting string. But in the input, the string is enclosed in quotes, which is part of the string literal. So when evaluated, it returns "HelloWorld" (the string content is HelloWorld). So the output should be "HelloWorld".

Wait, the string literals in the input are enclosed in quotes. The output is the result of the expression, which is a string. So when the input is "HelloWorld", the evaluated string is HelloWorld (without quotes). But the output is enclosed in quotes. Looking at the sample outputs:

Sample 1:

Input:

"HelloWorld"

Output:

"HelloWorld"

So the output is the string enclosed in quotes. But wait, in the input, the string is "HelloWorld", which is a string literal. So when evaluated, it's the content (HelloWorld), and the output is the same string, enclosed in quotes.

So the output must be enclosed in quotes. Wait, the problem says:

"Print in single line the resulting string."

But the examples show that the output is enclosed in quotes. For example, the first sample's output is "HelloWorld".

Wait, looking at the first sample:

Input is "HelloWorld" (quotes included). So the expression is a string literal. So the result is "HelloWorld" (the content between the quotes is HelloWorld). So the output is "HelloWorld", enclosed in quotes.

Wait, the problem's output requires that the resulting string is printed enclosed in quotes. Or is the output the actual string, not enclosed in quotes?

Wait, the problem's examples show that the outputs are enclosed in quotes. For example, the first sample's output is "HelloWorld", which includes the quotes.

So, the output is the resulting string enclosed in quotes. So the evaluated string is HelloWorld, but the output is "HelloWorld".

But wait, the sample input 2:

Input: REVerse(substr("helloworld",1,5))

The substr is from 1 to 5 (the first 5 characters of "helloworld" which is 'h e l l o' (indices 0-4 in 0-based). The substr returns 'hello', then reversed to 'olleh'. The output is "olleh", enclosed in quotes.

So the output is the evaluated string, enclosed in quotes. So the process is:

The evaluated result is a string (without quotes). Then, the output is that string enclosed in quotes.

Wait, but in the first sample, the input is "HelloWorld" which is a string literal. The evaluated result is the string HelloWorld (without quotes). Then, the output is "HelloWorld" (with quotes). So the output must be enclosed in quotes.

So the steps are:

Evaluate the input expression, which results in a string. Then, print that string enclosed in quotes.

So, regardless of the evaluated result, the output is the result enclosed in quotes. Even if the evaluated string is empty (but the problem states that the answer is non-empty).

So, after evaluating the expression, the code should print the result enclosed in quotes.

Therefore, the code must take the evaluated string and output it between quotes.

For example, if the evaluated result is 'Hello', the output is "Hello".

So, the final step is to enclose the result in quotes and print it.

Now, the main task is to implement the tokenizer, parser, and evaluator.

Let's outline the code structure.

First, tokenization:

Implement a tokenize function that reads the input and splits into tokens.

But how?

Let's think about the process.

The input is a single line. Let's read it as a string.

Then, process each character to build tokens.

Initialize a list of tokens. Initialize a position index at 0.

Loop while position < len(input):

   current_char = input[position]

   if current_char is a letter:

       read all consecutive letters (case-insensitive) until a non-letter is found. Then, check if the next character is '('. If yes, then this is a function name. So, the token is the function name (lowercase) added to the list, and the next character is the '('.

       Wait, no. For example, 'concat' is followed by '('. So after reading the letters, the next character is '('. So the letters form the function name.

       So, in code:

       start = position

       while position < len(input) and input[position].isalpha():

           position +=1

       function_name = input[start:position].lower()

       if position < len(input) and input[position] == '(':

           tokens.append(function_name)

           tokens.append('(')

           position +=1

       else:

           # but according to the problem statement, the input is correct, so this case should not happen.

           pass

   elif current_char == '"':

       # read the string literal.

       start = position

       position +=1

       while position < len(input) and input[position] != '"':

           position +=1

       # include the closing quote.

       position +=1

       tokens.append(input[start:position])

   elif current_char in '(),':

       tokens.append(current_char)

       position +=1

   elif current_char in '-0123456789':

       # read the entire number.

       start = position

       if current_char == '-':  # check if it's a negative number.

           position +=1

       while position < len(input) and input[position].isdigit():

           position +=1

       tokens.append(input[start:position])

   else:

       # according to problem statement, input is correct, so this is not possible.

       pass

Wait, but this code may have some issues. For example, the function name is followed by '(', but the code checks if after reading the letters, the next character is '('. But in the input, there could be numbers immediately after letters, but according to the problem statement, the input is correct, so function names are followed by '('. So the code can assume that.

So, in code, after reading the letters, the next character must be '(', so we can safely add the function name token and the '(' token.

But what about cases where the letters are not a function name? For example, the input is a string literal, which is enclosed in quotes, so letters inside the quotes are part of the string and processed in that case.

So the tokenizer will process letters as part of function names only when they are followed by '(', otherwise they are part of a string (but the string is enclosed in quotes).

So the tokenizer code can proceed.

Once the tokens are generated, the parser will parse them into an AST.

Then, the evaluator processes the AST.

Now, implementing this in Python.

Let's start with the tokenizer.

But first, the code for the tokenizer.

Sample input 1: "HelloWorld"

The input is a single string literal. So the tokenizer will generate a token ['"HelloWorld"'].

Sample input 2: REVerse(substr("helloworld",1,5))

Tokenization steps:

R E V E R S E ( ... )

The letters 'REVerse' are read as a function name (lowercase 'reverse'), followed by '(', then substr is another function.

So the tokens would be:

['reverse', '(', 'substr', '(', '"helloworld"', ',', '1', ',', '5', ')', ')'].

So the function names are stored in lowercase.

The numbers '1' and '5' are tokens as '1' and '5'.

So the tokenizer works as expected.

Now, implementing the tokenizer.

Now, the code for the tokenizer.

Let's code the tokenizer:

def tokenize(s):

    tokens = []

    n = len(s)

    i = 0

    while i < n:

        c = s[i]

        if c.isalpha():

            # function name or part of a string (but strings are in quotes)

            # read all letters

            start = i

            while i < n and s[i].isalpha():

                i +=1

            func_name = s[start:i].lower()

            # check if followed by '('

            if i < n and s[i] == '(':

                tokens.append(func_name)

                tokens.append('(')

                i +=1

            else:

                # this can't happen per problem statement

                pass

        elif c == '"':

            # read until next "

            start = i

            i +=1

            while i < n and s[i] != '"':

                i +=1

            i +=1  # include the closing "

            tokens.append(s[start:i])

        elif c in '(),':

            tokens.append(c)

            i +=1

        elif c in '-0123456789':

            # read the entire number, including leading '-'

            start = i

            if c == '-':

                i +=1

                # must be followed by digits

            while i < n and s[i].isdigit():

                i +=1

            tokens.append(s[start:i])

        else:

            # according to problem statement, input is correct, so this is unreachable

            i +=1

    return tokens

Wait, but the code for the function name may not handle cases where after reading letters, the next character is not '('. But according to the problem statement, the input is correct, so this won't happen. So, we can proceed.

Now, parsing the tokens.

Implement the parser with a recursive function.

Each node can be a dictionary with a type and value.

Alternatively, create classes for each node type.

But for simplicity, perhaps use dictionaries.

But in Python, it's easier to use classes or just tuples.

Alternatively, for the purposes of code brevity, we can represent nodes as tuples.

But perhaps using a class hierarchy is more readable.

Alternatively, use a dictionary with 'type' and 'value' keys.

But for code brevity, perhaps use a recursive approach.

But for the code to be concise, perhaps the parser can return the evaluated value directly. But since functions can be nested, the evaluator must evaluate the arguments first. So the parser must build a structure that allows us to evaluate the arguments in the correct order.

So, during parsing, the FunctionNode will have a list of arguments which are other nodes.

So, for example, in the input 'reverse(substr("abc",1,2))', the parser creates a FunctionNode('reverse', [FunctionNode('substr', [StringNode("abc"), NumberNode(1), NumberNode(2)])]).

Then, during evaluation, the innermost substr is evaluated first.

So, the parser needs to build this structure.

But in Python, for code brevity, perhaps we can represent the nodes as tuples. For example:

('function', name, args)

('string', value)

('number', value)

Alternatively, perhaps use a recursive approach where each function call is processed by evaluating its arguments first.

But since the code needs to be efficient, perhaps the recursive approach is manageable.

Implementing the parser as a recursive function.

The parse function:

def parse(tokens):

    # tokens is a list, and we use a index to track the current position.

    # use a mutable object to track the index, like a list holding the current index.

    index = [0]

    def parse_expression():

        current_token = tokens[index[0]]

        if current_token in ['concat', 'reverse', 'substr']:

            # function call

            func_name = current_token

            index[0] +=1

            # next token must be '('

            assert tokens[index[0]] == '(', "Expected '(' after function name"

            index[0] +=1

            args = []

            while True:

                if tokens[index[0]] == ')':

                    index[0] +=1

                    break

                arg = parse_expression()

                args.append(arg)

                if tokens[index[0]] == ',':

                    index[0] +=1

                elif tokens[index[0]] == ')':

                    index[0] +=1

                    break

            return ('function', func_name, args)

        elif current_token.startswith('"'):

            # string literal

            s = current_token[1:-1]

            index[0] +=1

            return ('string', s)

        elif current_token.lstrip('-').isdigit():

            # number

            num = int(current_token)

            index[0] +=1

            return ('number', num)

        else:

            # unexpected token

            raise ValueError(f"Unexpected token: {current_token}")

    return parse_expression()

But need to handle the case where the current token is a function name (like 'reverse'), then parse the arguments.

Wait, the function names are stored in lowercase in the tokenizer. So the tokens list has 'concat', 'reverse', 'substr' as function names.

So the parser can check if the current token is one of these.

But what about other tokens? For example, '(' or ')'. But according to the problem statement, the input is correct, so the parse_expression is only called when the current token is the start of an expression (function name, string, number).

But how does the parser handle nested function calls? For example, concat(reverse("a"), substr("b",1,2)):

The first token is 'concat', which is a function name. Parse the arguments. The first argument is a function call to reverse, which is parsed as another function call. Then the second argument is a substr call.

So the parse_expression function will handle this recursively.

Now, the evaluator.

Implementing the evaluator:

def evaluate(node):

    if node[0] == 'string':

        return node[1]

    elif node[0] == 'number':

        return node[1]

    elif node[0] == 'function':

        func_name = node[1]

        args = [evaluate(arg) for arg in node[2]]

        if func_name == 'concat':

            return args[0] + args[1]

        elif func_name == 'reverse':

            return args[0][::-1]

        elif func_name == 'substr':

            x = args[0]

            a = args[1]

            b = args[2]

            step = 1

            if len(args) == 4:

                step = args[3]

            # convert a and b to integers (but according to problem statement, they are already)

            # check if a and b are valid.

            # according to problem statement, 1 ≤ a ≤ b ≤ len(x), and step >=1.

            start = a -1

            end = b -1

            # slice x[start : end+1 : step]

            # need to handle the case where step is larger than the possible steps.

            return x[start : end+1 : step]

    else:

        raise ValueError("Unknown node type")

Now, putting it all together.

The code steps:

Read the input line.

Tokenize it.

Parse the tokens into an AST.

Evaluate the AST.

Enclose the result in quotes and print.

But how to handle the case where the input is a single string literal?

For example, the first sample input is "HelloWorld", which is tokenized to a single string token. The parser would return ('string', 'HelloWorld'). Evaluated to 'HelloWorld'. Then, output is "HelloWorld".

So the code should enclose the result in quotes.

But wait, the input may have nested functions that return a string. The evaluator returns the string (without quotes). So the code should then wrap the result in quotes.

So, the final steps are:

input_str = input().strip()

tokens = tokenize(input_str)

ast = parse(tokens)

result = evaluate(ast)

print(f'"{result}"')

But what if the input is a function call without any string literals? Like reverse("abc"), which returns the reversed string.

Yes.

Now, test the code with sample input 2:

Sample input 2:

REVerse(substr("helloworld",1,5))

Tokenize:

The function name is 'reverse' (lowercase), then '(', then substr function.

Parsing:

The root is a function call to reverse, with one argument which is a substr function call.

The substr arguments are "helloworld" (string), 1,5.

Evaluating substr:

The string is 'helloworld' (len 10). a=1, b=5. So start=0, end=4.

The substring is 'hello'.

Then reverse returns 'olleh'.

Output is "olleh".

Sample input 3:

conCAT(rEveRSE("olleh"),"world")

Evaluates to 'hello' + 'world' = 'helloworld'. Output is "helloworld".

Sample input 4:

reversE(concAT(substr("hello",1,2),sUbstr("world",1,5,1)))

Breaking down:

The innermost substr("hello",1,2) is substr of 'hello' from 1-2 (0-based 0-1) gives 'he'.

Then substr("world",1,5,1): a=1, b=5, step=1. The string 'world' is length 5. So start=0, end=4. step 1. So substr is 'world'.

concat('he', 'world') gives 'heworld'. Reverse of this is 'dlrow eh' → wait, no.

Wait, 'heworld' reversed is 'dlrow eh'. But sample input 4's output is "dlroweh". Let's see.

Wait, sample input 4's input is:

reversE(concAT(substr("hello",1,2),sUbstr("world",1,5,1)))

substr("hello",1,2) is the substring from 1 to 2 (1-based), which is 'h' (index 0) and 'e' (index 1). So 'he'.

sUbstr("world",1,5,1): the parameters are a=1, b=5, step=1. The string is 'world', length 5. So a=1 (start 0), b=5 (end 4). step 1. The substr is 'world'.

So concat('he', 'world') is 'heworld'. Reverse of this is 'dlrow eh' → wait, no. 'heworld' reversed is 'dlrow eh' → but the sample output is 'dlroweh'.

Wait, the sample input 4's output is "dlroweh".

Wait, perhaps I made a mistake.

Wait, substr("hello",1,2) is indices 1 and 2 (1-based). Wait, 1-based indices for substr mean that a and b are 1-based. So for "hello" (length 5), substr(1,2) is from index 1 to 2, inclusive. So the substring is 'e' and 'l'? Wait, no. Wait, the first character is index 1 (so 1-based), so the substring from 1 to 2 for "hello" (h is index 1, e is 2? No, wait, 1-based indexing for the string 'hello' is:

1: h

2: e

3: l

4: l

5: o

So substr("hello",1,2) is 'he'.

Wait, no. substr(x, a, b) returns the substring from a to b inclusive. So for a=1, b=2, it's the first two characters. So 'he'.

Yes.

So the first substr is 'he' (from "hello" 1-2). The second substr is "world" (1-5, step 1), which is the entire string. So concat is 'heworld'. Reversing this gives 'dlrow eh' → but sample output is 'dlroweh'.

Wait, what's the actual sample input 4's output?

Sample input 4's output is "dlroweh".

Wait, let's re-examine the sample input.

Sample input 4:

reversE(concAT(substr("hello",1,2),sUbstr("world",1,5,1)))

Wait, the second substr is sUbstr("world",1,5,1). The function is substr with 4 arguments: x, a, b, c.

So the substr parameters are 1,5,1. So a=1, b=5, step=1. The string is 'world' (length 5). So start is 0, end is 4, step 1. So the substring is 'world' (from index 0 to 4, step 1). So substr returns 'world'.

So concat is 'he' + 'world' → 'heworld'.

Reverse of 'heworld' is 'dlrow eh'.

But the sample output is "dlroweh".

Hmm, this indicates a discrepancy. So perhaps I have a mistake in the code.

Wait, perhaps I made a mistake in the handling of substr's parameters.

Wait, substr("hello",1,2) is a=1, b=2. The length of 'hello' is 5. So the substring is characters at 1 and 2 (1-based). So characters 'e' and 'l', so 'el'.

Wait, this is the mistake. I think I had a misunderstanding of the substr function.

Ah, yes! Oh no! Because the problem says that substr(x,a,b) returns the substring between indexes a and b inclusive. So, for the string "hello", indexes are 1-based. So substr("hello",1,2) is the first two characters: 'he'. But wait, that's correct for a=1 and b=2. Because indexes a and b are 1-based. So substr("hello",1,2) is 'he'.

Then substr("world",1,5,1) is the entire string 'world'. So concat('he', 'world') → 'heworld', which is 'heworld' → length 7. Reversed, it's 'dlrow eh' → 'dlrowhe' ?

Wait, 'heworld' → 'h' 'e' 'w' 'o' 'r' 'l' 'd' → reversed is 'd' 'l' 'r' 'o' 'w' 'e' 'h' → 'dlr o w e h' → 'dlroewh'? Or wait:

Original: 'heworld' → indexes 0-6 (h e w o r l d)

Reversed is 'dlr o w e h' → 'dlrow eh' → no. Let's see:

Original string is 'heworld' → letters are h e w o r l d → wait, no. Wait, "hello" is 5 letters, substr(1,2) is 'he'. "world" is 5 letters, substr(1,5,1) is 'world'. So concat is 'heworld' → which is h e w o r l d → no. Wait, 'he' + 'world' is 'heworld' → 2 +5 =7 letters.

Letters: h e w o r l d → indexes 0-6.

Reversed: d l r o w e h → 'dlr o w e h' → 'dlrowe h' → but the sample output is "dlroweh".

Wait, sample output is "dlroweh", which is 'dlroweh'.

Hmm, but according to this analysis, the reversed string should be 'dlrow eh' → which is 'dlrow eh' (with a space?), but there's no space. So the actual reversed string is 'dlrow eh' → 'dlroweh' when the space is not present. Wait, no. Let's think:

Original string is 'heworld' → h e w o r l d → indexes 0-6.

Reversed, the characters are:

index 6: d

index5: l

index4: r

index3: o

index2: w

index1: e

index0: h

So the reversed string is 'd l r o w e h' → 'dlr o w e h' → 'dlrowe h'?

No, in the reversed order, the characters are:

d, l, r, o, w, e, h → concatenated as 'dlr o w e h' → 'dlrowe h'? No, it's 'dlrow eh'?

Wait, let's write out the indices:

Original: 0:h,1:e,2:w,3:o,4:r,5:l,6:d.

Reversed indices would be 6,5,4,3,2,1,0 → the characters are d, l, r, o, w, e, h.

So the reversed string is 'dlrow eh' → which is 'dlrow eh' → but the sample output is 'dlroweh'.

So what's the problem here? There's a discrepancy between the expected output and the code's result. But according to the sample input 4's output, it's 'dlroweh'.

So perhaps there's a mistake in the code's evaluation of substr("hello",1,2) and/or substr("world",1,5,1).

Wait, let's re-examine substr("hello",1,2).

"hello" is h e l l o (indices 0-4 in 0-based).

substr("hello",1,2) is a=1, b=2 → 1-based indices. So a=1 is index 0, b=2 is index 1. So substring is 'he'.

Yes. So the first substr returns 'he'.

substr("world",1,5,1): "world" is 5 letters. a=1, b=5 → 0-based start 0, end 4. step 1. So substr is 'world'.

So concat is 'he' + 'world' → 'heworld' → which is 7 letters: h e w o r l d.

Reversed: d l r o w e h → 'dlrow eh'.

But the sample output is 'dlroweh'. So this suggests that the code is not handling something correctly.

Wait, the sample input is:

reversE(concAT(substr("hello",1,2),sUbstr("world",1,5,1)))

The functions are:

The innermost functions:

substr("hello",1,2) → a=1, b=2 → 'he' (correct).

sUbstr("world",1,5,1) → the function name is substr with 4 arguments (x,a,b,c). So parameters are 1,5,1. So a=1 (0-based start 0), b=5 (0-based end 4), step 1. So substr("world",0,4, step 1) → which is 'world'.

concat('he', 'world') → 'heworld'.

reverse('heworld') → 'dlrow eh'.

But sample output is "dlroweh".

Hmm, this suggests that the code is wrong. So why is there a discrepancy?

Wait, perhaps the code has a mistake in the step calculation. Let me re-calculate the substr("world",1,5,1):

x is 'world' (length 5).

a=1 (0-based start 0), b=5 (1-based). But according to the problem statement, for substr(x,a,b,c), 1 ≤a ≤b ≤n, where n is the length of x. So for x of length 5, b must be ≤5. So substr("world",1,5,1) is a=1, b=5. Then, in code:

start = 1-1 =0.

end =5-1=4.

step=1.

The slice is x[0:5:1] → which is x[0], x[1], x[2], x[3], x[4]. So the entire string 'world'.

So that's correct.

So, the code's evaluation is correct.

But the sample input's output is "dlroweh".

Wait, perhaps the code is correct and the sample input 4's output is correct.

Wait, sample input 4's output is "dlroweh". Let's see what 'dlroweh' is.

'dlroweh' → letters d l r o w e h. Wait, no. Let's see:

No, 'dlroweh' is d l r o w e h → which is 7 letters. How could that be?

If the input is 'heworld' (7 letters), reversed would be d l r o w e h → which is 'dlrow eh' → but there's no space. So the letters are d l r o w e h → 'dlroweh'.

Yes! Because when written without spaces, 'dlrow eh' becomes 'dlr o w e h' → but that's not correct. Let me write it correctly:

Original string is 'heworld' (h e w o r l d) → 7 letters.

Reversed is d l r o w e h → which is 'dlrow eh' → but when written as a single string, it's 'dlr o w e h' → no, each character is:

d (index 6)

l (index 5)

r (index4)

o (index3)

w (index2)

e (index1)

h (index0)

So the reversed string is 'dlrow eh' → but when written as a continuous string, it's 'dlrow eh' → which is 'dlroweh' ?

Wait, no. Let's see:

Indices of the original string 'heworld':

0: h

1: e

2: w

3: o

4: r

5: l

6: d

Reversed indices:

0 →6 →d

1 →5 →l

2 →4 →r

3 →3 →o

4 →2 →w

5 →1 →e

6 →0 →h

So the reversed string is d l r o w e h → which is 'dlrow eh' → but how? The letters are d, l, r, o, w, e, h → concatenated as 'dlrow eh' → but without the space, it's 'dlrowheh'?

Wait, no, no. The letters are d, l, r, o, w, e, h. So the reversed string is 'dlrow eh' → but that's 7 letters: d l r o w e h → which is 'dlr o w e h' → no, no spaces. So the actual reversed string is 'dlrowheh'?

Wait, no:

Indices of the reversed string:

The original string is 'heworld' → characters are h e w o r l d.

Wait, wait, 'he' + 'world' is 'heworld' → h e w o r l d → 7 letters.

The reversed string would be:

d l r o w e h.

Which is d followed by l followed by r followed by o followed by w followed by e followed by h.

So the reversed string is 'dlr o w e h' → 'dlrow eh'? No. The letters are d, l, r, o, w, e, h → 'dlroweh'.

Ah! Yes. So the letters are d l r o w e h → 'dlroweh'.

Yes. So the code is correct, and the sample output is correct.

So the code's evaluator is correct.

Thus, the code should work.

Now, putting all the code together.

But first, the code needs to read the input, tokenize, parse, evaluate, and print the result enclosed in quotes.

But need to handle all cases.

Now, the code:

But wait, in Python, the slice for substr is x[start:end+1:step]. For example, substr("HelloWorld",1,10,2) would be:

start=0, end=9 (since 10-1=9). step 2.

x[0:10:2] is x[0], x[2], x[4], x[6], x[8] → 'Hlool', which matches the sample.

So the code's implementation of substr is correct.

So, the code should handle all cases.

Now, the code.

Implement the tokenizer, parser, evaluator as described.

So, the full code:

Read the input line.

Tokenize it.

Parse into AST.

Evaluate.

Print the result enclosed in quotes.

Now, the code:

But the code needs to read the input line, even if it contains newlines (but according to the problem statement, the input is a single line).

So, in Python:

s = input().strip()

But wait, the input may have leading or trailing spaces. But according to the problem statement, the input is correct. So it's better to read the entire line, stripping any leading/trailing whitespace.

So:

input_line = input().strip()

Then, tokenize this line.

Now, implementing the code.

Putting it all together:

class ParserError(Exception):
    pass

def tokenize(s):
    tokens = []
    n = len(s)
    i = 0
    while i < n:
        c = s[i]
        if c.isalpha():
            # Function name
            start = i
            while i < n and s[i].isalpha():
                i += 1
            func_name = s[start:i].lower()
            if i < n and s[i] == '(':
                tokens.append(func_name)
                tokens.append('(')
                i += 1
            else:
                # According to problem statement, this is impossible
                raise ParserError("Invalid function name")
        elif c == '"':
            # String literal
            start = i
            i += 1
            while i < n and s[i] != '"':
                i += 1
            if i >= n:
                raise ParserError("Unclosed string literal")
            i += 1
            tokens.append(s[start:i])
        elif c in '(),':
            tokens.append(c)
            i += 1
        elif c in '-0123456789':
            # Number
            start = i
            if c == '-':
                i += 1
                if i >= n or not s[i].isdigit():
                    raise ParserError("Invalid number")
            while i < n and s[i].isdigit():
                i += 1
            tokens.append(s[start:i])
        else:
            # Ignore any other characters (problem says input is correct)
            i += 1
    return tokens

def parse(tokens):
    index = 0
    n = len(tokens)
    
    def parse_expression():
        nonlocal index
        if index >= n:
            raise ParserError("Unexpected end of tokens")
        token = tokens[index]
        if token in ['concat', 'reverse', 'substr']:
            # Function call
            func_name = token
            index += 1
            if index >= n or tokens[index] != '(':
                raise ParserError("Expected '(' after function name")
            index += 1
            args = []
            while True:
                if index >= n:
                    raise ParserError("Unexpected end of tokens")
                if tokens[index] == ')':
                    index += 1
                    break
                arg = parse_expression()
                args.append(arg)
                if index < n and tokens[index] == ',':
                    index += 1
            return ('function', func_name, args)
        elif token.startswith('"'):
            # String literal
            s = token[1:-1]
            index += 1
            return ('string', s)
        elif token.lstrip('-').isdigit():
            # Number
            num = int(token)
            index += 1
            return ('number', num)
        else:
            raise ParserError(f"Unexpected token: {token}")
    
    return parse_expression()

def evaluate(node):
    if node[0] == 'string':
        return node[1]
    elif node[0] == 'number':
        return node[1]
    elif node[0] == 'function':
        func_name = node[1]
        args = [evaluate(arg) for arg in node[2]]
        if func_name == 'concat':
            return args[0] + args[1]
        elif func_name == 'reverse':
            return args[0][::-1]
        elif func_name == 'substr':
            x = args[0]
            a = args[1]
            b = args[2]
            step = 1
            if len(args) == 4:
                step = args[3]
            start = a - 1
            end = b - 1
            return x[start:end+1:step]
    else:
        raise ValueError("Unknown node type")

def main():
    input_line = input().strip()
    tokens = tokenize(input_line)
    try:
        ast = parse(tokens)
    except ParserError as e:
        print(f"Error during parsing: {e}")
        return
    result = evaluate(ast)
    print(f'"{result}"')

if __name__ == "__main__":
    main()

This code should handle all cases correctly.

Testing sample input 4:

input_line is 'reversE(concAT(substr("hello",1,2),sUbstr("world",1,5,1)))'.

The tokenizer will generate tokens:

['reverse', '(', 'concat', '(', 'substr', '(', '"hello"', ',', '1', ',', '2', ')', ',', 'substr', '(', '"world"', ',', '1', ',', '5', ',', '1', ')', ')', ')'].

Parsing this:

The root is 'reverse' function with one argument: concat(...).

concat has two arguments: substr("hello",1,2) and substr("world",1,5,1).

Evaluating substr("hello",1,2) → 'he'.

Evaluating substr("world",1,5,1) → 'world'.

concat gives 'heworld'.

Reverse → 'dlrow eh' → 'dlroweh' when written as a single string.

Thus, the code produces "dlroweh", which matches the sample output.

Other samples should also work.

The code reads the input, tokenizes, parses into the AST, evaluates, and prints the result enclosed in quotes.

Thus, this should be the correct solution.
</think>

```python
class ParserError(Exception):
    pass

def tokenize(s):
    tokens = []
    n = len(s)
    i = 0
    while i < n:
        c = s[i]
        if c.isalpha():
            start = i
            while i < n and s[i].isalpha():
                i += 1
            func_name = s[start:i].lower()
            if i < n and s[i] == '(':
                tokens.append(func_name)
                tokens.append('(')
                i += 1
            else:
                raise ParserError("Invalid function name")
        elif c == '"':
            start = i
            i += 1
            while i < n and s[i] != '"':
                i += 1
            if i >= n:
                raise ParserError("Unclosed string literal")
            i += 1
            tokens.append(s[start:i])
        elif c in '(),':
            tokens.append(c)
            i += 1
        elif c in '-0123456789':
            start = i
            if c == '-':
                i += 1
                if i >= n or not s[i].isdigit():
                    raise ParserError("Invalid number")
            while i < n and s[i].isdigit():
                i += 1
            tokens.append(s[start:i])
        else:
            i += 1
    return tokens

def parse(tokens):
    index = 0
    n = len(tokens)
    
    def parse_expression():
        nonlocal index
        if index >= n:
            raise ParserError("Unexpected end of tokens")
        token = tokens[index]
        if token in ['concat', 'reverse', 'substr']:
            func_name = token
            index += 1
            if index >= n or tokens[index] != '(':
                raise ParserError("Expected '(' after function name")
            index += 1
            args = []
            while True:
                if index >= n:
                    raise ParserError("Unexpected end of tokens")
                if tokens[index] == ')':
                    index += 1
                    break
                arg = parse_expression()
                args.append(arg)
                if index < n and tokens[index] == ',':
                    index += 1
            return ('function', func_name, args)
        elif token.startswith('"'):
            s = token[1:-1]
            index += 1
            return ('string', s)
        elif token.lstrip('-').isdigit():
            num = int(token)
            index += 1
            return ('number', num)
        else:
            raise ParserError(f"Unexpected token: {token}")
    
    return parse_expression()

def evaluate(node):
    if node[0] == 'string':
        return node[1]
    elif node[0] == 'number':
        return node[1]
    elif node[0] == 'function':
        func_name = node[1]
        args = [evaluate(arg) for arg in node[2]]
        if func_name == 'concat':
            return args[0] + args[1]
        elif func_name == 'reverse':
            return args[0][::-1]
        elif func_name == 'substr':
            x = args[0]
            a, b = args[1], args[2]
            step = args[3] if len(args) == 4 else 1
            start = a - 1
            end = b - 1
            return x[start:end+1:step]
    else:
        raise ValueError("Unknown node type")

def main():
    input_line = input().strip()
    tokens = tokenize(input_line)
    try:
        ast = parse(tokens)
    except ParserError:
        return
    result = evaluate(ast)
    print(f'"{result}"')

if __name__ == "__main__":
    main()
```