<think>
Okay, let's see. I need to solve this programming problem. Let's read the problem carefully.

So the problem is about determining whether Lesha's problem is similar to any in the archive. The similarity is calculated based on finding a permutation of Lesha's words that appears as a subsequence in an archive problem. Then, among all possible permutations that form a subsequence, we pick the one with the smallest number of inversions, and compute the similarity p based on that.

The output depends on whether any archive problem has such a permutation. If none do, output "Brand new problem!". Otherwise, find the archive problem with the maximum p value (since p is higher when x is smaller), and if there's a tie, pick the earliest one.

Hmm. So the key steps are:

1. For each archive problem, check all permutations of Lesha's words to see if any is a subsequence of the archive's word sequence.
2. For those permutations that are subsequences, compute the number of inversions.
3. Among all valid permutations for an archive problem, find the one with the smallest inversion count (since this would maximize p).
4. Compute p for each archive problem. The maximum p among all archive problems (and the earliest index if there's a tie) will determine the output.

But wait, the problem says that for each archive problem, we need to select the permutation of Lesha's problem that is a subsequence of the archive's problem and has the minimal number of inversions. Then, for that permutation, compute p.

If there are no such permutations for any archive problem, output the brand new message. Otherwise, among all archive problems that have at least one valid permutation, select the one with the largest p. If multiple, the earliest.

So the plan is:

For each archive problem:
- Generate all permutations of Lesha's words (since n can be up to 4, there are 4! =24 permutations possible at max).
- For each permutation, check if it's a subsequence of the archive's problem's words.
- For those permutations that are a subsequence, compute their inversion count (relative to Lesha's original order).
- Among these, find the permutation with the smallest inversion count. Then compute p as (n*(n-1)/2 - x +1), where x is that minimal inversion count. Then, the p for this archive problem is that value. If no permutations are possible, the p is zero or not considered.

Then, among all archive problems, find the one with the highest p. If p is same, choose the earliest. If all p are zero (i.e., no archive has any permutation as subsequence), output brand new.

So, the steps are:

1. Preprocess Lesha's words into a list, and note the original order. The original order is the one given in the input, and inversion counts for permutations are determined by comparing to this original order.

Wait, the note says that the inversion count is based on the original problem's order. For example, in the note, the original is "add two numbers" and the permutation "numbers add two" has two inversions. So, the inversion count is determined by how the permutation's elements are ordered compared to their positions in Lesha's original list.

So the inversion count for a permutation is the number of pairs (i,j) in the permutation where in the original order, the element at position i comes before the element at j, but in the permutation, it's the opposite. So, for example, in the original list, the order is [a, b, c], and a permutation is [c, a, b]. The inversions here are (c vs a), (c vs b), but since in the original, a comes before c, and b comes before c. So the inversion pairs are (c,a) and (c,b), which are two inversions.

Wait, the inversion count is the number of pairs in the permutation where the order is reversed compared to the original order. So for each pair of positions i < j in the permutation, if in the original order, the element at permutation[i] comes after the element at permutation[j], then it's an inversion.

So, for example, original order is [A, B, C, D]. A permutation [B, A, D, C] would have inversions between B and A (since in original, A comes before B), D and C (original order C before D). So inversion count is 2.

So, to compute the inversion count of a permutation (relative to original), we can compare each pair of elements in the permutation. For each i < j in the permutation's indices, check if the original index of permutation[i] is greater than the original index of permutation[j]. If yes, then this is an inversion.

So the inversion count can be computed as follows:

Original_order is a dictionary mapping each word to its index in Lesha's list. For a permutation perm, the inversion count is the number of pairs (i,j) where i < j and original_order[perm[i]] > original_order[perm[j]].

Yes. So for each permutation, we can compute this.

So for each permutation, we need to check two things:

- Is it a subsequence of the archive's problem's words?
- If yes, compute its inversion count.

So the steps for each archive problem are:

For each permutation of Lesha's words:

Check if the permutation is a subsequence of the archive's problem's word list.

If it is, calculate the inversion count for that permutation.

Once we have all permutations that are valid (i.e., subsequences), we need to find the one with the minimal inversion count. The minimal x (inversion count) will lead to the maximum p for that archive.

If there are no valid permutations for an archive problem, then it's not considered. Otherwise, the p is computed as (n*(n-1)/2 - x +1), where x is the minimal inversion count for that archive.

Once we have the maximum p across all archives, we select the archive with the highest p (earliest if tie).

So the first step is to process each archive problem, check all permutations of Lesha's words to see if any is a subsequence of the archive's words, then for those that are, find the one with minimal inversion count, compute p, and track the maximum.

But how to check if a permutation is a subsequence of the archive's words?

Checking if a permutation is a subsequence can be done as follows: for each word in the permutation, find the next occurrence in the archive's list after the current position.

For example, the permutation is [w1, w2, w3], and the archive's list is [a, w1, b, w2, c, w3]. Then it is a subsequence. But if the archive's list is [w1, w3, w2], then the permutation [w1, w2, w3] is not a subsequence, because after w1, there's w3 but not w2 in order.

So the standard way to check if a list is a subsequence of another is to iterate through both, and see if you can match all elements in order.

So for a given permutation, we can check if it's a subsequence of the archive's words by:

Initialize a pointer for the permutation (i=0), and a pointer for the archive's words (j=0). While j < len(archive_words) and i < len(permutation):

if permutation[i] == archive_words[j], then i += 1, j +=1.

Else, j +=1.

At the end, if i == len(permutation), then it's a subsequence.

So that's the algorithm.

Now, considering that n is up to 4, and m up to 10, and each archive problem can have up to 20 words, this approach is feasible.

But generating all permutations for each archive problem can be manageable. For each archive problem, checking 24 permutations (for n=4), each of which requires O(k) time (where k is up to 20) for the subsequence check. So total steps for all m=10 archives would be 10 * 24 * 20 = 4800 operations. That's very manageable.

So the plan is:

Read Lesha's words, store their original order (as a dictionary: word -> index).

For each archive problem:

   Read k and the words.

   For all permutations of Lesha's words:

      Check if the permutation is a subsequence of the archive's words.

      If yes, compute inversion count for this permutation.

   Collect all inversion counts for valid permutations.

   If there are any, find the minimal x among them. Compute p = (n*(n-1)/2 - x +1). Record this p for the archive.

   Else, p is 0 (or not considered).

Once all archives are processed:

Collect all archives where p > 0. If none, output brand new.

Else, among these, select the archive with the highest p. If multiple have the same p, choose the earliest one (smallest index).

Then output the index and the p as per the format.

Now, the steps in code:

First, read n, then Lesha's words. Then m, then m lines for each archive.

But for Lesha's words, since the problem states that Lesha's problem has no repeated words, so the list is unique. So for permutations, all elements are distinct.

Now, the code steps:

Read n, leshas_words = list of words. original_order is a dict {word: index for index, word in enumerate(leshas_words)}.

Then read m, and then for each of m lines, split into k and the words (archive_words).

For each archive, process as follows:

Initialize best_x (minimal inversion count) as something large (like infinity). For each permutation of leshas_words:

   Check if this permutation is a subsequence of archive_words.

   How to check:

   Initialize i = 0 (points to permutation), j =0 (points to archive_words).

   while i < len(perm) and j < len(archive_words):

      if perm[i] == archive_words[j], then i +=1, j +=1.

      else, j +=1.

   after loop, if i == len(perm), then it's a subsequence.

   If it is a subsequence:

      compute x (inversion count) for this permutation.

      compare x to best_x. If x is smaller, update best_x.

So, after checking all permutations for this archive, if best_x is updated (i.e., there is at least one valid permutation), then compute p for this archive as (n*(n-1)//2 - best_x +1). Otherwise, p is 0.

But in code, initially best_x is set to infinity. If after checking all permutations, best_x remains infinity, then no valid permutation exists. So for such an archive, we ignore it. Otherwise, compute p.

So for each archive, after processing, we have a p (if any).

Then, among all archives with p computed (i.e., those that have at least one valid permutation), select the one with the maximum p, earliest index if tie.

Now, code implementation.

In Python, generating permutations can be done with itertools.permutations.

So for leshas_words, permutations(leshas_words) gives all possible permutations.

But note that permutations returns tuples, so we need to convert them to lists for easier processing.

So, for each perm in permutations(leshas_words):

Check if it's a subsequence.

If yes, compute inversion count.

Now, the inversion count calculation:

For the permutation perm (which is a tuple of words), we need to compare each pair (i,j) where i < j. For each such pair, check if original_order[perm[i]] > original_order[perm[j]]. If yes, increment x.

So for a permutation of length n, there are n*(n-1)/2 possible pairs.

So for each perm, x is sum(1 for i in range(len(perm)) for j in range(i+1, len(perm)) if original_order[perm[i]] > original_order[perm[j]]).

But for n=4, this is 6 pairs per permutation, which is manageable.

So code-wise:

x = 0

for i in range(n):

   for j in range(i+1, n):

      if original_order[perm[i]] > original_order[perm[j]]:

          x +=1

But since perm is a tuple of words, and original_order is a dict mapping each word to its index in leshas_words.

Yes.

So, for each valid permutation, compute x, and track the minimal x for the archive.

Now, the code structure.

Read input:

n = int(input())

leshas_words = input().split()

original_order = {word: idx for idx, word in enumerate(leshas_words)}

m = int(input())

archives = []

for idx in range(m):

   parts = input().split()

   k = int(parts[0])

   words = parts[1:]

   archives.append( (k, words) )

Then, process each archive in the list.

For each archive in archives (with index starting at 1), process:

k, words = archive.

Generate all permutations of leshas_words.

For each permutation, check if it's a subsequence of words.

If yes, compute x.

Track the minimal x.

Once all permutations are checked, compute p for the minimal x (if any).

Now, code for checking if a permutation is a subsequence:

def is_subsequence(perm, archive_words):

   i = 0

   j = 0

   len_perm = len(perm)

   len_archive = len(archive_words)

   while i < len_perm and j < len_archive:

       if perm[i] == archive_words[j]:

           i += 1

       j += 1

   return i == len_perm

Yes.

So in code:

from itertools import permutations

...

for each archive in archives:

   archive_words = words

   best_x = None

   for perm in permutations(leshas_words):

       if is_subsequence(perm, archive_words):

           # compute x

           x = 0

           for i in range(len(perm)):

               for j in range(i+1, len(perm)):

                   if original_order[perm[i]] > original_order[perm[j]]:

                       x +=1

           if best_x is None or x < best_x:

               best_x = x

   if best_x is not None:

       n_val = len(leshas_words)

       max_inversion = n_val * (n_val -1) // 2

       p = max_inversion - best_x +1

       # add to possible candidates

       candidates.append( (p, -archive_idx, archive_idx) )

So the candidates can be stored as tuples (p, -index, index) so that when sorted in reverse, higher p comes first, and for same p, smaller index comes first.

Wait, to handle the maximum p and earliest index in case of ties, we can collect all archives with their p and index, then sort them in descending order of p, and ascending order of index. So the first element after sorting will be the desired one.

Alternatively, for each archive, we can track p, and keep track of the maximum p found so far, and the earliest index.

So during processing each archive, we can compute p (if any) and compare it with the current maximum.

So variables like max_p = -1, best_archive_index = -1.

Then, for each archive index (starting from 1 to m):

   compute p as above.

   if p is None (no permutation found), skip.

   else:

       if p > max_p:

           max_p = p

           best_archive_index = current index

       elif p == max_p:

           if current index is less than best_archive_index:

               best_archive_index = current index

So, this way, after processing all archives, if max_p remains -1, output brand new. Else, output the best_archive_index and the p.

So this approach is O(m * perms * check_subseq * compute_x).

But perms is up to 24 (for n=4), and check_subseq is O(k) (k up to 20). Compute_x is O(n^2), which is up to 16 steps. So for m=10, 10*24*20*16 = 76,800 operations. That's acceptable.

Now, code.

But in Python, itertools.permutations returns tuples, so the perm is a tuple, and in the is_subsequence function, we can compare each element.

Now, code outline:

Read inputs as before.

max_p = -1

best_archive = -1

for archive_idx in 1..m:

   k, words = archives[archive_idx-1]

   best_x = None

   for perm in permutations(leshas_words):

       if is_subsequence(perm, words):

           x = compute inversion count

           if best_x is None or x < best_x:

               best_x = x

   if best_x is not None:

       n = len(leshas_words)

       total_pairs = n*(n-1)//2

       p = total_pairs - best_x + 1

       if p > max_p:

           max_p = p

           best_archive = archive_idx

       elif p == max_p:

           if archive_idx < best_archive:

               best_archive = archive_idx

If after processing all, max_p remains -1, output "Brand new problem!".

Else, output the best_archive index and the p.

Now, let's test this against the examples.

First example:

Input:

4

find the next palindrome

1

10 find the previous palindrome or print better luck next time

Lesha's words: ["find", "the", "next", "palindrome"]

Original_order: "find"->0, "the"->1, "next"->2, "palindrome"->3.

For the archive problem, words are ["find", "the", "previous", "palindrome", "or", "print", "better", "luck", "next", "time"].

Check all permutations of lesha's words for being a subsequence.

One of the permutations is ["find", "the", "palindrome", "next"].

Check if this is a subsequence of the archive words.

Looking through the archive's words:

find is at position 0.

the is at position 1.

palindrome is at position 3.

next is at position 8. So yes, the permutation is a subsequence.

Now, the inversion count for this permutation: original_order of "find" is 0, "the" is 1, "palindrome" is 3, "next" is 2.

So in the permutation, the order is 0,1,3,2. The inversion is between 3 and 2. So x is 1.

So p is (4*3/2) -1 +1 = 6 -1 +1 =6? Wait, wait, 4*3/2 is 6. So 6 -1 +1 =6.

Wait, in the sample output, the similarity p is 6, as the output is [:||||||:], which is 6 |'s.

But in the first sample's note, the permutation used is "find the next palindrome" rearranged as "find the palindrome next". Wait, maybe I made a mistake in the example.

Wait the first sample's note says that the permutation is "find the next palindrome" becomes "find the palindrome next", which has one inversion (palindrome and next). In the original order, next is at index 2, palindrome is at 3. So in the permutation, next comes after palindrome. So original_order of 'palindrome' is 3, 'next' is 2. So 3>2, so this pair is an inversion. So x is 1. Then p is 6-1+1=6. So the output is 6 |'s. Which matches the sample.

So the code would generate this.

Another example: third sample input.

Lesha's words: these papers are formulas. Original order: these:0, papers:1, are:2, formulas:3.

Archive problem 1's words are: what are these formulas and papers.

Check permutations. For example, the permutation [these, are, papers, formulas]. Check if it's a subsequence. Let's see:

Looking for 'these' in the archive words. 'these' is at index 2.

Then 'are' at index 1 (after index 2?), no. Wait the archive words are ['what', 'are', 'these', 'formulas', 'and', 'papers'].

Wait, the permutation [these, are, papers, formulas]. Let's see:

Check if this permutation is a subsequence.

First word: these. In archive_words, 'these' is at index 2.

Second word: are. Need to find 'are' after index 2. But in the archive_words, 'are' is at index 1, which is before 2. So no.

Hmm. So perhaps the correct permutation is [what, are, these, formulas, and, papers]. Wait no. The permutation must be of Lesha's words, which are 'these', 'papers', 'are', 'formulas'.

Wait, let's think of a permutation of these four words that is a subsequence of the archive's words.

The archive's words are: what are these formulas and papers.

So the words are: 'what' (0), 'are' (1), 'these' (2), 'formulas' (3), 'and' (4), 'papers' (5).

So possible permutations of Lesha's words that are subsequences.

For example, the permutation 'are these papers formulas' would not be a subsequence, since 'papers' is after 'formulas' in the archive.

But another permutation: 'these are formulas papers'?

Check:

Looking for 'these' (index 2), then 'are' after 2: the next 'are' is index 1, which is before, so no.

Alternatively, 'are these formulas papers':

Check if this is a subsequence.

'are' is at index 1. Then 'these' at index 2. 'formulas' at index3. 'papers' at index5. So yes. So this permutation is a valid subsequence.

Inversion count for this permutation:

Original order is: these (0), papers (1), are (2), formulas (3).

The permutation is: are (2), these (0), formulas (3), papers (1).

Inversion count:

Compare each pair:

i=0, j=1: are (2) comes before these (0). Original order for these (0) comes before are (2). So in permutation, these comes after are. So this is an inversion. So count +=1.

i=0, j=2: are and formulas. Original order, formulas (3) comes after are (2). So in permutation, are is before formulas: no inversion. So no.

i=0, j=3: are and papers. In original, papers (1) comes before are (2). So in permutation, are comes before papers. So this is an inversion (since in original, papers comes before are). So inversion count +=1.

i=1, j=2: these and formulas. Original order: these (0) comes before formulas (3). In permutation, these comes before formulas: no inversion. So no.

i=1, j=3: these and papers. Original order, papers (1) comes after these (0). So in permutation, these comes before papers. So no inversion.

i=2, j=3: formulas and papers. Original order, papers (1) comes before formulas (3). So in permutation, formulas comes before papers. This is an inversion. So inversion count +=1.

Total inversion count is 1+1+1 =3.

So x=3.

n is 4. n*(n-1)/2 =6. So p=6-3+1=4.

But according to the sample output, the answer is p=4, but the output is [:||||:], which is 4 |'s. So that's correct.

But perhaps there's another permutation with a lower x.

Wait, perhaps the permutation 'are these papers formulas' is possible. Let's check if it's a subsequence.

In archive's words: 'are' (1), 'these' (2), 'papers' (5), 'formulas' (3). Wait 'formulas' is at index3, which is before 'papers' (5). So in the permutation, after 'papers' (5), there's no 'formulas' after that. So this permutation would not be a subsequence.

So the permutation 'are these formulas papers' is valid. So x=3. Are there other permutations with lower x?

Another permutation: 'these are formulas papers' — check if it's a subsequence.

These is at 2. are is after 2? The next 'are' is at index1, which is before 2. So no. So not a valid subsequence.

Another permutation: 'are formulas these papers' — check.

'are' (1), then formulas (3), then these (2) which is after 3? No. So invalid.

Hmm. So the permutation 'are these formulas papers' is valid and has x=3. Are there other permutations?

What about 'are these papers formulas'? The subsequence would be are (1), these (2), papers (5). Then, formulas would need to be after 5, but in the archive, formulas is at 3. So no.

So the only valid permutation for this archive is the one with x=3.

So p is 6-3+1=4. The output is [:||||:], which matches the sample.

So the code should capture this.

Now, code implementation.

Potential optimizations:

Since permutations can have duplicates (but in our case, since Lesha's words are unique, permutations are all unique). So no problem.

But for checking the permutation as a subsequence, perhaps we can memoize or cache, but for n=4, it's manageable.

Now, code.

Implement the is_subsequence function as a helper.

But in Python, for each permutation, check it as a list, and pass to the helper.

Now, code:

Testing against sample input 1.

```python
import sys
from itertools import permutations


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    leshas_words = input_stream.readline().split()
    original_order = {word: idx for idx, word in enumerate(leshas_words)}
    m = int(input_stream.readline())
    archives = []
    for _ in range(m):
        parts = input_stream.readline().split()
        k = int(parts[0])
        words = parts[1:]
        archives.append(words)

    max_p = -1
    best_idx = -1

    for archive_idx, words in enumerate(archives, 1):
        best_x = None
        for perm in permutations(leshas_words):
            # Check if perm is a subsequence of words
            i = 0
            j = 0
            len_perm = len(perm)
            len_words = len(words)
            while i < len_perm and j < len_words:
                if perm[i] == words[j]:
                    i += 1
                j += 1
            if i == len_perm:
                # Compute x for this permutation
                x = 0
                for a in range(len(perm)):
                    for b in range(a + 1, len(perm)):
                        if original_order[perm[a]] > original_order[perm[b]]:
                            x += 1
                if best_x is None or x < best_x:
                    best_x = x
        if best_x is not None:
            n_val = n
            total_pairs = n_val * (n_val - 1) // 2
            p = total_pairs - best_x + 1
            if p > max_p or (p == max_p and archive_idx < best_idx):
                max_p = p
                best_idx = archive_idx

    if best_idx == -1:
        print("Brand new problem!", file=output_stream)
    else:
        print(best_idx, file=output_stream)
        line = "[:"
        line += "|" * max_p
        line += ":]"
        print(line, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
add two numbers
3
1 add
2 two two
3 numbers numbers numbers
""",
            "output": \
"""\
Brand new problem!
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

Testing against sample input 3.

```python
import sys
from itertools import permutations


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    leshas_words = input_stream.readline().split()
    original_order = {word: idx for idx, word in enumerate(leshas_words)}
    m = int(input_stream.readline())
    archives = []
    for _ in range(m):
        parts = input_stream.readline().split()
        k = int(parts[0])
        words = parts[1:]
        archives.append(words)

    max_p = -1
    best_idx = -1

    for archive_idx, words in enumerate(archives, 1):
        best_x = None
        for perm in permutations(leshas_words):
            # Check if perm is a subsequence of words
            i = 0
            j = 0
            len_perm = len(perm)
            len_words = len(words)
            while i < len_perm and j < len_words:
                if perm[i] == words[j]:
                    i += 1
                j += 1
            if i == len_perm:
                # Compute x for this permutation
                x = 0
                for a in range(len(perm)):
                    for b in range(a + 1, len(perm)):
                        if original_order[perm[a]] > original_order[perm[b]]:
                            x += 1
                if best_x is None or x < best_x:
                    best_x = x
        if best_x is not None:
            n_val = n
            total_pairs = n_val * (n_val - 1) // 2
            p = total_pairs - best_x + 1
            if p > max_p or (p == max_p and archive_idx < best_idx):
                max_p = p
                best_idx = archive_idx

    if best_idx == -1:
        print("Brand new problem!", file=output_stream)
    else:
        print(best_idx, file=output_stream)
        line = "[:"
        line += "|" * max_p
        line += ":]"
        print(line, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
add two decimals
5
4 please two decimals add
5 decimals want to be added
4 two add decimals add
4 add one two three
7 one plus two plus three equals six
""",
            "output": \
"""\
3
[:|||:]
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

Fourth sample:

Lesha's words: add two decimals. Original_order: add (0), two (1), decimals (2).

Archive problem 3's words: 'two', 'add', 'decimals', 'add'.

Check permutations. For example, 'add two decimals' is a permutation. Check if it's a subsequence.

The archive's words are ['two', 'add', 'decimals', 'add'].

Check the permutation 'add two decimals':

Looking for 'add' in the words. The first 'add' is at index1.

Then 'two' needs to be after index1. Words after 1 are 'decimals' and 'add' — no 'two' found. So this permutation is not a subsequence.

Another permutation: 'two add decimals'.

Check:

two is at index0. add is at index1. decimals is at index2. So yes. The permutation is a subsequence.

Inversion count: original_order['two'] is 1, 'add' is 0. So in the permutation, two comes before add. Original order add (0) comes before two (1). So this is an inversion. Then 'add' and 'decimals' (0 and 2): no inversion. 'two' and 'decimals' (1 and 2): no inversion. So x=1.

So p is 3*(3-1)/2 -1 +1 =3-1+1=3. So p=3. So the output is [:|||:].

Which matches the sample.

So the code seems to handle these cases.

Potential edge cases:

- n=1. Then there's only one permutation, which is the word itself. So check if it's a subsequence. If yes, p is (0 -0 +1)=1.

For example, n=1, word 'a'. An archive has 'a a a', then p is 1. Output is 1 and [:|:].

Another edge case: Lesha's words have all permutations as subsequence, but which permutation has the minimal x.

So the code should handle this.

Now, code is written, and seems correct.
</think>

```python
import sys
from itertools import permutations

n = int(sys.stdin.readline())
leshas_words = sys.stdin.readline().split()
original_order = {word: idx for idx, word in enumerate(leshas_words)}
m = int(sys.stdin.readline())
archives = []
for _ in range(m):
    parts = sys.stdin.readline().split()
    words = parts[1:]
    archives.append(words)

max_p = -1
best_idx = -1

for archive_idx, words in enumerate(archives, 1):
    best_x = None
    for perm in permutations(leshas_words):
        i = j = 0
        len_perm, len_words = len(perm), len(words)
        while i < len_perm and j < len_words:
            if perm[i] == words[j]:
                i += 1
            j += 1
        if i == len_perm:
            x = 0
            for a in range(len(perm)):
                for b in range(a + 1, len(perm)):
                    if original_order[perm[a]] > original_order[perm[b]]:
                        x += 1
            if best_x is None or x < best_x:
                best_x = x
    if best_x is not None:
        total_pairs = n * (n - 1) // 2
        p = total_pairs - best_x + 1
        if p > max_p or (p == max_p and archive_idx < best_idx):
            max_p = p
            best_idx = archive_idx

if best_idx == -1:
    print("Brand new problem!")
else:
    print(best_idx)
    print(f"[:{'|' * max_p}:]")
```
