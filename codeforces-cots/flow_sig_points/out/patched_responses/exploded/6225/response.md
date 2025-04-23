<think>
Okay, I need to solve this problem. Let's read the problem carefully.

The task is to find superstitions that appear in the most countries. Then output all such superstitions in lowercase, sorted alphabetically.

So the input consists of countries and their superstitions. Each country starts with a line (the country name), followed by lines that start with "* " followed by the superstition. The superstition entries are unique per country. Countries are separated by their names.

The key points here are:

1. Parsing the input correctly. Each country starts with a line that's not a superstition (since superstitions start with "* "). So, the lines are either country names or superstitions.

2. For each country, collect all their superstitions (normalized to lowercase, and considering that spacing between words can vary, but sequences of words are compared case-insensitively). Wait, the problem says that two names are equal if their sequence of words is equal. So for example, "Friday the 13th" and "Friday   the 13th" (with multiple spaces) are considered the same because when split into words, they become ["Friday", "the", "13th"]. So, when processing each superstition, we need to split the line (after the asterisk and space) into words, normalize the spacing (split into words and join with single spaces), then convert to lowercase.

Wait, no. Wait, the problem statement says: "You shouldn't consider the case of the letters when you compare the words." So, when comparing two superstitions, their words are compared case-insensitively. But the output requires the superstition to be written in lowercase. So, for each superstition entry, we need to process it by splitting into words (split by one or more spaces), then joining with single spaces, and converting each word to lowercase.

For example, if a line is "* Friday the   13th", we split into ["Friday", "the", "13th"], then convert each word to lowercase: ["friday", "the", "13th"], then join with single spaces to get "friday the 13th".

So the processing steps for a superstition line are:

- Remove the leading "* ".
- Split the rest into words (split on any whitespace, multiple spaces treated as a single separator).
- Convert each word to lowercase.
- Join the words with a single space between them.
- That's the key to group superstitions across countries.

The countries are considered unique by their name (case-sensitive?), but the problem says that all country names are distinct, so we don't need to process their names for uniqueness. Each country's name is a line that's not starting with "* ".

So the plan is:

1. Read the input line by line.

2. For each line, determine if it's a country name or a superstition.

3. For each country, collect all its superstitions (processed as described) into a set (since each country's entries are unique).

4. For each superstition in the country's set, increment a counter in a dictionary that maps the processed superstition string to the count of countries it appears in.

Once all data is processed:

- Find the maximum count value.

- Collect all superstitions that have this maximum count.

- Sort them lexicographically (the alphabetical order of their names as sequences of words). Lexicographical order here is the standard string comparison since after processing, the superstitions are in lowercase and joined with single spaces. So comparing the strings directly would be correct.

Output each of these in order, each on a new line.

Now, how to parse the input.

The input is a sequence of lines. The first line is a country name. Then, the lines that follow until the next country line are superstitions of that country.

So, the approach to parse the input would be:

Initialize current_country as None. Then for each line in the input:

- if the line starts with "* ", it's a superstition of the current country.

- else, it's a new country. So, add the previous country (if any) to the data, then set current_country to this line.

But wait, the first line is a country. Then, the next lines until the next country (a line that doesn't start with "* ") are superstitions of that country.

So, perhaps:

Initialize a list of countries. Each country entry is a tuple of (name, set of superstitions).

Read the first line as the first country's name.

Then read the next lines:

For each line:

If it starts with "* ", process as a superstition for the current country.

Else, it's a new country. So, we add the current country (name and its superstitions set) to the list, then start a new country with this line as the name, and a new empty set of superstitions.

At the end of the loop, add the last country to the list.

Wait, but the first country is processed as: current_country is initialized to the first line. Then, each subsequent line that is a superstition adds to its set. When a new country line is found, add the current country to the list and create a new one.

So:

current_country = None

superstitions = set()

countries = []

for line in lines:

    if line starts with '* ':

        # process as superstition

        processed_superstition = process_line(line)

        superstitions.add(processed_superstition)

    else:

        # new country

        if current_country is not None:

            # add previous country to list

            countries.append( (current_country, superstitions) )

        current_country = line

        superstitions = set()

After processing all lines, add the last country.

Yes.

Then, for each country in countries, iterate through their superstitions and update a dictionary that counts per-superstition the number of countries.

So, the counts dictionary is:

counts = defaultdict(int)

for country, sups in countries:

    for sup in sups:

        counts[sup] += 1

Then find the maximum value in counts.values().

Collect all superstitions with that count.

Sort them lexicographically (sorted in Python does lex order by default), then print each in order.

So the steps are:

Parse the input into countries with their superstitions (processed as per rules).

Count each superstition's occurrence in countries.

Find the max count.

Collect all superstitions with max count.

Sort them.

Print each.

Now, processing the lines:

For a line starting with '* ', we process it as:

- line[2:] gives the part after the asterisk and space.

- Split into words by splitting on whitespace (so, any number of whitespaces between words are considered a single separator). So, using split() (which splits on any whitespace, including multiple spaces, tabs, etc. but in the problem description, the input lines have words separated by spaces only).

For example, line = "* Friday the   13th"

After stripping the "* ", we have "Friday the   13th".

Split into words: ["Friday", "the", "13th"]

Each word is converted to lowercase: ["friday", "the", "13th"]

Join with single spaces: "friday the 13th"

Thus, the code for processing a superstition line is:

def process_superstition_line(line):

    words = line[2:].split()

    processed = ' '.join(word.lower() for word in words)

    return processed

So, that's how each superstition is normalized.

Now, the parsing loop:

But how to read all lines? Since the input can be up to 50 lines, and each line up to 50 characters. So in Python, read via input(). But when reading multiple lines, perhaps we can read until EOF.

But in Python, the standard way is to read all lines at once using sys.stdin.read().splitlines().

But in code submission, sometimes using a loop with input() is better. But for code, the code can read all lines with:

import sys

lines = [line.rstrip('\n') for line in sys.stdin]

But since the problem says that each line has no leading or trailing spaces, and no trailing newline (since the problem says "No line has leading or trailing spaces." So each line in the input is stripped of leading/trailing spaces. So perhaps reading via sys.stdin.read().splitlines() is sufficient.

In code:

lines = sys.stdin.read().splitlines()

Then process each line.

So, the code outline:

Read all lines.

Initialize current_country as the first line.

Then lines[0] is the first country name.

Then, for lines[1:]:

Loop through each line.

Wait, no. Let's redo the parsing code.

lines = sys.stdin.read().splitlines()

countries = []

current_country = None

current_sups = set()

for line in lines:

    if line.startswith('* '):

        # superstition line

        sup = process_superstition_line(line)

        current_sups.add(sup)

    else:

        # country line

        if current_country is not None:

            countries.append( (current_country, current_sups) )

        current_country = line

        current_sups = set()

# after loop, add the last country

if current_country is not None:

    countries.append( (current_country, current_sups) )

Then, process each country's superstitions.

Then, count for each superstition how many countries have it.

counts = defaultdict(int)

for country, sups in countries:

    for sup in sups:

        counts[sup] += 1

if counts is empty? But the problem says each country has at least one superstition. Wait, no. Wait, the input contains at least one superstition. Because the first line is a country, followed by at least one superstition. So each country has at least one superstition? Wait, the problem says:

"The input will contain at least one superstition."

So for example, the input can be:

CountryA

* a

So one country, one superstition.

But in the code, countries is a list of country and their superstitions. So for each country, current_sups could be empty? No, because the input has at least one superstition. Because the first line is a country, and the next lines must be superstitions until the next country. So the first country must have at least one superstition. Because the input has at least one superstition.

But perhaps the code should handle cases where a country has no superstitions. But according to the problem statement, the input will have at least one superstition. So perhaps all countries except possibly the first have superstitions. Wait no. Because the first line is a country, then the next lines must be superstitions until the next country.

So the first country's lines are the first line (country name) followed by zero or more superstition lines until another country line. But the problem states that the input contains at least one superstition. So the first country must have at least one superstition.

Wait, let's look at the first example input:

Ukraine

* Friday the   13th

* black   cat

* knock the   wood

USA

* wishing well

* friday   the   13th

Holland

France

* Wishing Well

Wait, in this example, Holland is a country line. Then the next line is France. So Holland's superstitions are empty? But the problem says that each country has at least one superstition. Wait, the problem says that "each entry of the list is unique within each country. The first line of input will represent a country. The input will contain at least one superstition."

Wait, the input will contain at least one superstition. So the data may have countries with zero superstitions? No. Because each country's list is the lines after the country line until the next country line. So if a country line is followed by another country line, then that country has no superstitions.

But according to the problem statement, the input contains at least one superstition. So, the first country must have at least one superstition, but others may not. But that's possible. For example:

Country1

* a

Country2

Country3

* b

In this case, Country2 has no superstitions. But according to the problem statement, is this allowed?

The problem says, "each entry of the list is unique within each country. The input will contain at least one superstition."

So the input must have at least one superstition, but individual countries can have zero. But in code, when processing Country2 (the line after Country1's superstitions), current_sups is empty. So when adding to countries, Country2's sups is empty. Then, when processing Country3's superstitions, they are added.

But according to the problem statement, countries are guaranteed to have distinct names, but there's no restriction on whether a country has any superstitions.

But the code should handle countries with zero superstitions. Because the problem allows that.

But in the code, when a country has zero superstitions, then when we process it, current_sups is empty. So, when adding to the counts, for each sup in current_sups (which is empty), the loop doesn't run. So the country's superstitions (zero) contribute nothing to the counts.

But the problem says that each country has a list of superstitions. Wait, looking back:

The problem says:

"country name on a separate line, followed by a list of superstitions popular in it, one entry per line. Each entry of the list is formatted as an asterisk..."

So the country name line is followed by the list of superstitions. So if a country's name is followed by another country name line, that country's list of superstitions is empty. But according to the problem statement, is that possible?

The problem says "The input will contain at least one superstition." But that's the total, not per country.

So the code must handle countries with zero superstitions. Because the problem allows that.

But in the code, such countries would not contribute to any counts. So their inclusion doesn't affect the result.

In any case, the code as written will handle this correctly.

Now, for the code:

Implement the steps:

Read all lines.

Process each line, grouping into countries and their superstitions.

Once countries are processed, collect counts.

Find the maximum count.

Collect all superstitions with that count.

Sort lexicographically.

Output each in order.

Now, code.

In Python:

But we need to be careful about the order of processing.

So the code steps:

Read lines.

Process the lines into countries and their superstitions.

Compute the counts.

Find max_count.

Collect sorted list of superstitions with that count.

Print each in order.

Implementing in code.

Now, the code:

import sys

from collections import defaultdict

def process_superstition(line):

    words = line[2:].split()

    return ' '.join(word.lower() for word in words)

def main():

    lines = sys.stdin.read().splitlines()

    if not lines:

        return  # but according to problem, input has at least 2 lines.

    countries = []

    current_country = None

    current_sups = set()

    for line in lines:

        if line.startswith('* '):

            # process superstition

            sup = process_superstition(line)

            current_sups.add(sup)

        else:

            # new country

            if current_country is not None:

                countries.append( (current_country, current_sups) )

            current_country = line

            current_sups = set()

    # add the last country

    if current_country is not None:

        countries.append( (current_country, current_sups) )

    # compute counts

    counts = defaultdict(int)

    for _, sups in countries:

        for sup in sups:

            counts[sup] +=1

    if not counts:

        # but the problem says input has at least one superstition

        # so this can't happen

        print('')

        return

    max_count = max(counts.values())

    max_sups = [sup for sup in counts if counts[sup] == max_count]

    # sort lexicographically

    max_sups.sort()

    for sup in max_sups:

        print(sup)

if __name__ == '__main__':

    main()

Testing this code against the examples.

First example input:

Ukraine

* Friday the   13th

* black   cat

* knock the   wood

USA

* wishing well

* friday   the   13th

Holland

France

* Wishing Well

The countries parsed:

- Ukraine has superstitions: "friday the 13th", "black cat", "knock the wood"

USA has "wishing well", "friday the 13th"

Holland has none.

France has "wishing well".

So counts:

friday the 13th appears in Ukraine and USA: count 2.

wishing well appears in USA and France: count 2.

Others have 1.

So the output is these two, sorted.

The sorted order is "friday the 13th" comes before "wishing well".

Yes, which matches the first example's output.

Second example input:

Spain

* Tuesday the 13th

Italy

* Friday the 17th

Russia

* Friday the 13th

England

* rabbit foot

Each country has one superstition.

So counts:

Tuesday the 13th: 1

Friday the 17th:1

Friday the 13th: 1 (from Russia, and Spain is Tuesday, Russia is Friday. So Spain's is Tuesday, Russia's is Friday. So Friday the 13th is once.

Wait, Spain's line is "* Tuesday the 13th", which becomes "tuesday the 13th".

Italy's is "friday the 17th".

Russia's is "friday the 13th".

England's is "rabbit foot".

So counts:

Each has count 1. So the maximum is 1. So all four superstitions are output, sorted.

Which gives the four lines in the output, sorted lex.

Which matches the second example's output.

So the code works for the examples.

Now, possible edge cases.

Another test case where a country has multiple entries of the same superstition. But the problem states that entries are unique within each country, so no need to handle that.

What about multiple spaces between words in a superstition?

Like, "*   a   b   c  " (but according to the problem, input lines have no leading or trailing spaces. So the line starts with "* " followed by the rest, which may have varying spaces. But after processing, they become "a b c" in lowercase.

So code handles that correctly.

Case where a superstition is in multiple countries, but varying case and spacing.

For example:

Country1

* Hello World

Country2

* HELLO   WORLD

These will be processed to "hello world", which is same for both. So count is 2.

Yes.

Thus, the code should handle all cases.

Now, considering performance.

The constraints: input up to 50 lines. So the code's time and memory usage is acceptable.

Each country's processing is O(k), where k is the number of superstitions per country. But with 50 lines maximum, even with 50 countries (each having one line), the code is fast.

Thus, the code is optimal.
</think>

```python
import sys
from collections import defaultdict

def process_superstition(line):
    words = line[2:].split()
    return ' '.join(word.lower() for word in words)

def main():
    lines = sys.stdin.read().splitlines()
    countries = []
    current_country = None
    current_sups = set()

    for line in lines:
        if line.startswith('* '):
            sup = process_superstition(line)
            current_sups.add(sup)
        else:
            if current_country is not None:
                countries.append(current_sups)
            current_country = line
            current_sups = set()
    if current_country is not None:
        countries.append(current_sups)

    counts = defaultdict(int)
    for sups in countries:
        for sup in sups:
            counts[sup] += 1

    if not counts:
        return

    max_count = max(counts.values())
    max_sups = [sup for sup in counts if counts[sup] == max_count]
    max_sups.sort()

    for sup in max_sups:
        print(sup)

if __name__ == '__main__':
    main()
```