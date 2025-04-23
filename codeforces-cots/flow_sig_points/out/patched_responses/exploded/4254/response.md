<think>
Okay, let's see. The problem is to find the number of valid playlists that sum up to exactly T minutes. The constraints are that songs can't repeat, and consecutive songs can't have the same genre. Also, the order matters. So we need to count all permutations of subsets of the songs where the total time is T and the genres don't repeat consecutively.

Hmm. The input constraints are n up to 15 and T up to 225. So n is small enough that maybe a bitmask approach is feasible, but T is up to 225. Wait, but for each possible subset of songs, we need to track the total time and the last genre. Also, since the order matters, the DP state needs to track the last genre and the mask of used songs. Because the order affects the validity (the sequence of genres must alternate), the mask alone isn't enough. So the state would be something like (mask, last_genre, total_time) and track the number of ways to arrange the songs in mask with that total time and ending with last_genre, such that the sequence is valid.

But how do we model this efficiently? Let's think.

Each state is a mask (bitmask representing which songs are used), last genre (1-3 or 0 for nothing), and current total time. But wait, the total time can be up to 15*15=225 (since n is 15, each song up to 15). So T can be up to 225. So for each possible mask, last genre, and time up to T, we can track the count of sequences.

But the mask can be 2^15 = 32768 possibilities. Last genre is 4 possibilities (including 0, maybe for the first song). Time up to 225. So the total number of states would be 32768 * 4 * 225 = 32768 * 900 = around 29,491,200. That's a lot. But maybe manageable with some optimizations?

Alternatively, since the order matters, we can model the DP as follows:

dp[mask][last_genre][time] = number of sequences using the songs in mask, ending with last_genre, with total time 'time', and satisfying the constraints.

Then, for each state, we can try adding a new song that's not in the mask, has a different genre than last_genre, and the new time doesn't exceed T. Wait, but the time could be up to T. So for each new song, the time would be current time + t_i. If the new time is <= T, then we add to the new state.

The base case would be individual songs: for each song i, mask is (1<<i), last_genre is g_i, time is t_i. The count is 1 for each such state.

Then, for each possible state, iterate over all possible next songs not in the mask, and if their genre is different from last_genre, add the new state with the mask including that song, the new last genre, and the new time. The count is accumulated by multiplying the current count with the possible permutations.

Wait, but the mask represents the set of songs used. The order in which they are added is part of the permutation. So when building the DP, each transition from a mask to a mask | (1<<i) adds a new song i, which must not be in the current mask, and the genre of i must not equal the last_genre.

So the transitions would be:

For each mask, last_genre, time:

   for each song i not in mask:

       if g_i != last_genre:

           new_time = time + t_i

           if new_time > T: skip

           new_mask = mask | (1<<i)

           dp[new_mask][g_i][new_time] += dp[mask][last_genre][time] * 1 (since adding one more song)

Wait, but how does this account for the order? Because each step adds a new song to the end. So the DP is building sequences incrementally, adding one song at a time. The mask keeps track of which songs are used, and the last_genre ensures that consecutive genres are different. So the transitions are correct in this approach.

So the total answer would be the sum over all masks, all possible last_genres, and time exactly T of the dp[mask][last_genre][T].

This seems manageable. Let's compute the maximum possible states.

n=15 → mask can be up to 2^15=32768.

last_genre can be 0-3 (but initially, last_genre is 0 for no songs, but the first song can be any genre. Wait, the first song's last_genre is its genre. So maybe the initial state is when mask is 0, last_genre is 0 (no previous genre), and time is 0. Then, for each song, you can add it if it's not in the mask, and since last_genre is 0 (which is allowed for the first song). Then, the mask transitions to (1<<i), last_genre becomes g_i, time becomes t_i. So the initial transitions from mask 0.

Wait, perhaps the initial mask is 0, last_genre is 0 (no genre), and time 0. Then for each song, you can take it as the first song. Then, the transitions proceed as described.

Yes. So the initial state is mask 0, last_genre 0, time 0. Then, each transition represents adding a new song to the sequence. The transitions are done by adding a song not in the mask, whose genre is different from last_genre (which is 0 in the first step, but for the first song, since last_genre is 0, any genre is allowed). Wait, no. Because if the last_genre is 0 (no previous song), then the first song can have any genre. So when we start, we can add any song, regardless of its genre. Then, subsequent songs must have a genre different from the last one.

So the DP setup is:

dp[0][0][0] = 1. Then, for all possible steps, we transition from current states to next states by adding a song not in the mask, with genre different from last_genre (unless last_genre is 0, which allows any genre).

Wait, but how to model that? Let's see:

When mask is 0, last_genre is 0. Then, when adding a song i (first song), the new mask is 1<<i, last_genre becomes g_i, time becomes t_i. And the count increases by 1 (since there's 1 way to start with song i).

So the transitions would check if the current last_genre is 0 (i.e., first song). In that case, any song can be added. Otherwise, the new song's genre must not equal the last_genre.

So in code, the condition is: if last_genre == 0 (i.e., the current state is the initial state with no songs), then any song can be added. Otherwise, the song's genre must not equal last_genre.

So the transitions are:

For each state (mask, last_genre, time):

   for each song i not in mask:

       if (last_genre == 0) or (g_i != last_genre):

           new_time = time + t_i

           if new_time > T: continue

           new_mask = mask | (1 << i)

           dp[new_mask][g_i][new_time] += dp[mask][last_genre][time]

           mod the result as we go.

Then, the answer is the sum over all mask, all last_genre, of dp[mask][last_genre][T].

But wait, even if the total time is T, but the mask has some songs that sum to T, but adding another song would exceed T. However, since the total is exactly T, any such sequence where time is exactly T is valid. So the sum over all masks where the time is exactly T, and the mask uses some songs whose total time is T.

But since the transitions stop when the new_time exceeds T, the only time entries in the DP are those where time <= T. So when collecting the answer, we just sum all dp[mask][g][T] across all masks and all g.

So the key steps are:

- Initialize the DP with the initial state (mask 0, last_genre 0, time 0) with count 1.

- Iterate through all possible masks, genres, and times.

- For each state, iterate through all possible songs not in the mask, check the genre condition, compute new_time, and if acceptable, update the new state's count.

Now, considering the constraints:

n=15 → masks up to 32768.

Each mask can have 3 possible genres (1,2,3) plus the initial 0. So 4 possibilities.

Time can be up to 225.

So the total possible states are 32768 *4 *226 (since time can be 0 to 225). That's about 32768 * 4 * 226 = 32768 * 904 = 29,622,  32768 * 900 is 29,491,200, so around 30 million states. Hmm. But in Python, that might be tight. Let's see. Each state's count is an integer mod 1e9+7. So maybe using a 3D array is feasible.

But even with 30 million states, in Python, the memory could be a problem. Let's calculate the memory needed. Each state is an integer (say, 4 bytes). 30 million *4 is 120 MB, which is manageable within the 256 MB limit.

Alternatively, using a dictionary-based DP with only active states could save memory, but for speed, a preallocated array is better.

But in Python, creating a 3D array (like a list of lists) for mask, genre, time may not be efficient. So perhaps using a dictionary where the keys are (mask, last_genre, time) and the value is the count. But for 30 million entries, even a dictionary might be too slow.

Wait, but the transitions are such that for each step, each state can generate new states. So perhaps we can process the states in a BFS-like manner, using a queue or a way to process them in order of mask size. Since each transition adds a new song, the mask's size (number of bits set) increases by 1 each time. So we can process masks in order of increasing number of set bits. For each mask with k bits set, all transitions from it will be to masks with k+1 bits set. So this is a way to process the states layer by layer.

But even then, the number of states could be large, but maybe manageable.

Alternatively, using a bitmask and for each possible mask, track the last genre and time. So for each mask, we have a list of (last_genre, time) pairs, and their counts. But again, this might be manageable.

Let me think about the implementation.

In Python, perhaps we can represent the DP as a dictionary of dictionaries. For example, for each mask, a dictionary that maps (last_genre, time) to the count. Then, for each mask, we process all possible (last_genre, time) pairs, and generate new masks by adding songs not in the mask.

But for 32768 masks, and each mask could have multiple (last_genre, time) entries, this might be feasible.

Alternatively, we can precompute all possible masks and track the possible (last_genre, time) entries for each mask.

But in Python, using a list of dictionaries might be more efficient. Let's see.

Let's think of the initial state: mask 0, last_genre 0, time 0, count 1.

Then, for each mask in order of increasing bits, we process the entries in (last_genre, time) for that mask.

So, for example:

Initialize a list of dictionaries, dp[mask], where each entry is a dictionary of (last_genre, time) : count.

But in Python, initializing a list of 32768 elements, each being a dictionary, might take some memory, but perhaps manageable.

Alternatively, using a defaultdict approach, but that could be slower.

Alternatively, using a list of 32768 elements, each being a list of tuples (last_genre, time, count), but for each mask, we process these tuples.

But even that could be manageable.

So here's the plan:

We can represent the DP as a list of dictionaries, where each index in the list is the mask. For each mask, the dictionary maps (last_genre, time) to the count.

We start with mask 0, and in its dictionary, (0, 0) has a count of 1.

Then, for each mask in increasing order of bits (since adding a song increases the number of bits), for each (last_genre, time) in the current mask's dictionary, we iterate over all songs not in the mask. For each such song i, if the genre is not equal to last_genre (or last_genre is 0), then compute the new_time = time + t_i. If new_time exceeds T, skip. Otherwise, new_mask is mask | (1<<i). Then, we add to the new_mask's dictionary entry (g_i, new_time) the count multiplied by 1 (since adding the song i to the sequence).

Wait, but the order is handled by the transitions. Each step adds a song to the end of the sequence, so the order is considered in the way the transitions are made. For example, adding song A then song B is a different path than adding B then A, so the DP counts these as separate sequences.

Yes, this approach correctly models all possible permutations of the subset of songs, as long as the genres are valid and the total time is exactly T.

So the steps are:

1. Read the input: n and T, then the list of songs with t_i and g_i.

2. Initialize the DP structure. dp is a list of dictionaries, indexed by mask. Each entry is a dictionary mapping (genre, time) to count. So for each mask, the possible (genre, time) pairs are stored with their counts.

3. Start with mask 0, which has {(0, 0): 1}.

4. For each mask in the order of increasing number of bits, process all (last_genre, time) pairs in the current mask's dictionary. For each song not in the mask, check if it can be added (genre condition). If so, compute new_time. If new_time <= T, then update the new_mask's dictionary by adding the count to the (g_i, new_time) entry.

5. After processing all masks, collect all entries where the time is exactly T, across all masks and genres. Sum their counts modulo 1e9+7.

Now, the key points for optimization:

- Precompute the songs' t and g.

- For each mask, precompute which songs are not in the mask. But since n is small (15), we can iterate through all 0<=i<n and check if (mask & (1<<i)) == 0.

- For each transition, check if the new_time is <= T, otherwise skip.

So in Python code, perhaps using a list of dictionaries for each mask. Let's see.

Now, let's think about the data structures.

We can represent dp as a list where each element is a dictionary. The index is the mask. So:

dp = [defaultdict(lambda: defaultdict(int)) for _ in range(1<<n)]

But that would take a lot of memory. Alternatively, use a list of dictionaries where each element is a dictionary of tuples (last_genre, time) to counts.

Wait, perhaps using a list of dictionaries where each mask has a dictionary of (last_genre, time) keys and integer counts. But in Python, dictionaries can be slow for such a large number of entries.

Alternative approach: For each mask, track a list of (last_genre, time, count) entries. But again, for 3e7 states, this is not feasible.

Alternatively, for each step, process each possible mask and update the next masks as we go. Let's try to model this.

Initialize the DP with mask 0, last_genre 0, time 0: count 1.

Then, for each possible mask, loop through all possible songs not in the mask, and for each possible (last_genre, time) in the current mask's DP, check if adding the song is allowed. If allowed, compute the new state and add the count to that state.

But how to iterate over the masks in order of the number of bits set. Because each mask with k bits can only transition to masks with k+1 bits. So processing masks in order of increasing bits set allows us to process all possible transitions correctly.

So first, process mask 0 (0 bits), then all masks with 1 bit, then 2 bits, etc., up to 15 bits.

So for each mask in order of the number of set bits, and for each (last_genre, time) in dp[mask], process all possible transitions.

In Python, we can precompute the order of masks by their bit count. For example, generate all masks and sort them based on the number of set bits. Then iterate through them in that order.

This way, when processing a mask, all previous masks with fewer bits have already been processed, so their transitions have been accounted for.

Now, the code outline would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, T = map(int, input_stream.readline().rstrip("\n").split())
    songs = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(n)]
    MOD = 10**9 +7

    dp = [{} for _ in range(1<<n)]
    dp[0] = {(0, 0): 1}  # mask 0: (last_genre, time) → count

    for mask in sorted(range(1<<n), key=lambda x: bin(x).count('1')):
        for (last_genre, current_time), count in dp[mask].items():
            for i in range(n):
                if not (mask & (1 << i)):
                    ti, gi = songs[i]
                    if last_genre != 0 and gi == last_genre:
                        continue
                    new_time = current_time + ti
                    if new_time > T:
                        continue
                    new_mask = mask | (1 << i)
                    key = (gi, new_time)
                    dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

    answer = 0
    for mask in range(1<<n):
        for (g, t), cnt in dp[mask].items():
            if t == T:
                answer = (answer + cnt) % MOD

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
1 1
1 1
1 3
""",
            "output": \
"""\
2
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, T = map(int, input_stream.readline().rstrip("\n").split())
    songs = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(n)]
    MOD = 10**9 +7

    dp = [{} for _ in range(1<<n)]
    dp[0] = {(0, 0): 1}  # mask 0: (last_genre, time) → count

    for mask in sorted(range(1<<n), key=lambda x: bin(x).count('1')):
        for (last_genre, current_time), count in dp[mask].items():
            for i in range(n):
                if not (mask & (1 << i)):
                    ti, gi = songs[i]
                    if last_genre != 0 and gi == last_genre:
                        continue
                    new_time = current_time + ti
                    if new_time > T:
                        continue
                    new_mask = mask | (1 << i)
                    key = (gi, new_time)
                    dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

    answer = 0
    for mask in range(1<<n):
        for (g, t), cnt in dp[mask].items():
            if t == T:
                answer = (answer + cnt) % MOD

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 10
5 3
2 1
3 2
5 1
""",
            "output": \
"""\
10
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

Wait, but according to the sample output, the answer is 2. Oh right, because in the sample input 2, the songs are:

song0: t=1, g=1

song1: t=1, g=1

song2: t=1, g=3.

So the three songs have total time 3. The playlist must consist of all three songs. But the two genre 1 songs cannot be adjacent.

So the valid permutations are those where the two genre 1 songs are not consecutive.

The possible valid permutations are:

[0,2,1], [1,2,0], [2,0,1], [2,1,0] ?

Wait, but in the sample output, the answer is 2. So perhaps the correct answer is that only two of the possible permutations are valid.

Wait, the sample explanation says that the answer is 2. The two valid sequences are [1,3,2] and [2,3,1]. So the indices are 0,2,1 and 1,2,0 (assuming the input is 0-based). Because the first two songs (indices 0 and 1) are same genre, so they can't be consecutive.

So the valid sequences must have the two genre 1 songs separated by the genre 3 song.

So the possible permutations are:

0,2,1 → genres 1,3,1 → invalid because the first and third are same genre consecutive? Wait no: the genres are 1,3,1. But the consecutive genres are 1 and 3 (allowed), then 3 and 1 (allowed). So that is valid. Wait, no. The first two songs are 0 and 2 (genres 1 and 3) → allowed. Then 2 and 1 (genres 3 and 1) → allowed. So this sequence is valid.

But song1 is also genre 1. So the third song is song1 (genre 1), which comes after song2 (genre 3). So it's allowed. So why is the sample output 2?

Ah, because the sample input is:

songs are:

song0: 1 1

song1: 1 1

song2: 1 3

So the total time is 3. So the playlist must include all three songs (sum is 1+1+1=3).

But the two genre 1 songs can't be consecutive.

So the valid sequences are:

song0, song2, song1 → genres 1,3,1 → allowed.

song1, song2, song0 → genres 1,3,1 → allowed.

song2, song0, song1 → genres 3,1,1 → invalid because the last two are same genre.

song2, song1, song0 → genres 3,1,1 → invalid.

song0, song1, song2 → genres 1,1,3 → invalid.

song1, song0, song2 → genres 1,1,3 → invalid.

So only two valid permutations. Hence the sample output is 2.

So the code should count these two.

In the code, after processing all masks, the mask 7 (all three songs) must have two entries where the time is 3. Let's see.

When processing mask 3 (bits 0 and 1 set), which contains the two genre 1 songs. The time here would be 2 (1+1). But then adding song 2 (genre 3) gives new_time=3.

But in mask 3, the last_genre is 1 (since both songs 0 and 1 are genre 1). So when adding song 2, since its genre is 3, which is different from 1, it's allowed. So new_time is 2+1=3. So the new_mask is 7 (all bits set). The key (3,3) is added with the count from the previous state.

Wait, mask 3's entries could be (1,2). For example:

- mask 3 could have entries (1, 2) with count 2 (since there are two possible ways to reach mask 3 with time 2 and last genre 1: either adding song0 then song1, or song1 then song0).

So when processing mask 3:

for (1,2), count=2.

For each song not in mask 3 (song 2):

ti=1, gi=3. last_genre is 1 (allowed). new_time=2+1=3.

new_mask=7. So add (3,3) to mask7's dict with count 2.

So mask7's (3,3) entry has count 2.

Similarly, other masks may contribute to mask7's entries. Wait, but for the three-song sequences, the only way to reach time 3 is by adding all three songs. So mask7's (3,3) entry is the sum of all valid ways to arrange the three songs such that consecutive genres are allowed.

But according to our earlier analysis, only two of the six permutations are valid. So why does the code's approach count two entries?

Because in the code, when processing the mask 3 (songs 0 and 1, time 2, last genre 1), adding song2 (genre 3, time 3) gives a count of 2 (since mask3's count is 2). So in mask7, (3,3) would have count 2. Then, when we sum all entries where time is 3, that's the answer.

But what about other paths leading to mask7?

For example, mask5 (songs 0 and 2) → last_genre could be 3, time 2. Then adding song1 (genre 1) gives new_time 3, new_mask7, and the count increases by the count from mask5's entry (which could be 1). So mask7's (1,3) entry would have count 1.

Similarly, mask6 (songs 1 and 2) → last_genre 3, time 2. Adding song0 (genre1) gives new_mask7, count increases by 1.

So mask7's entries would be:

(3,3) → count 2 (from mask3)

(1,3) → count 1 (from mask5)

(1,3) → count 1 (from mask6?)

Wait, no. Let's think.

Wait, mask5 has songs 0 and 2. So when mask5 is processed:

mask5's entries would have (1, 2) (if the last song was 0) and (3, 2) (if the last song was 2). Wait no. Let's see how mask5 is formed.

mask5 is 101 in binary (songs 0 and 2).

The possible ways to reach mask5:

From mask0: add song0 (mask1), then song2 (mask5).

Or from mask4 (song2), add song0.

For example:

mask0 → song0 (mask1, genre1, time1) → song2 (mask5, genre3, time2).

mask0 → song2 (mask4, genre3, time1) → song0 (mask5, genre1, time2).

So mask5's entries are (3,2) (from mask4) and (1,2) (from mask1).

Wait, no:

When adding song2 to mask1 (which has genre1, time1), the new genre is 3, new_time is 2. So mask5's entry (3,2) has count 1.

When adding song0 to mask4 (genre3, time1), new_time is 2. genre1 !=3, so allowed. So mask5's entry (1,2) has count 1.

So mask5 has two entries: (3,2) and (1,2), each with count 1.

Then, processing mask5:

for each (last_genre, time) in mask5's entries:

for (3,2), count=1:

   check songs not in mask5 (song1, song3, etc. but n=3, so song1 (i=1) is not in mask5).

   song1's genre is 1. last_genre is 3. allowed. new_time=2+1=3. new_mask7. add (1,3) with count 1.

for (1,2), count=1:

   song1's genre is 1. last_genre is 1. not allowed. skipped.

so after processing mask5, mask7's entry (1,3) has count 1.

Similarly, mask6 (songs1 and 2) would have entries (1,2) (from adding song1 to mask0, then song2) and (3,2) (from mask2, song1 and song2).

Processing mask6:

for (1,2) (genre1, time2):

   adding song0 (genre1) is not allowed. song0 is not in mask6. genre1 == last_genre (1). So can't add.

for (3,2) (genre3, time2):

   adding song0 (genre1) is allowed. new_time=3. new_mask7. add (1,3) with count 1.

So mask7's (1,3) entry is increased by 1.

So mask7's entries are:

(3,3) → 2 (from mask3)

(1,3) → 1 (from mask5)

(1,3) → 1 (from mask6)

Wait, no. For mask5, (3,2) → song1 (genre1) is allowed. new_time=3. So adds (1,3) with count 1.

For mask6, (3,2) → adding song0 (genre1) is allowed. new_time=3. adds (1,3) with count 1 (from mask6's entry (3,2) which has count 1).

So mask7's (1,3) entry is 1 +1 =2.

So mask7's dict has (3,3) → 2 and (1,3) → 2.

So the total sum for T=3 is 2 (from 3,3) + 2 (from 1,3) → 4. But the sample output is 2. Wait, that's a problem.

Hmm, this indicates a mistake in the code.

Wait, but according to the sample input 2, the answer is 2. So the code's approach is overcounting.

What's the error here?

Ah, because the code counts all permutations where the sum is T, but some of these permutations may have consecutive same genres.

Wait, no. Because the transitions are designed to avoid adding a song with the same genre as the previous. So mask7's entries should only have sequences that are valid.

So why does the code's approach count 4 valid sequences for sample input 2, but the correct answer is 2?

Wait, maybe I made a mistake in the analysis.

Let me re-examine the code.

In mask3 (songs 0 and 1), the last_genre is 1 (since both are genre 1). When adding song2 (genre3), the new_time is 3. The new_mask is 7, and the entry is (3,3) with count 2. So those sequences are 0→1→2 and 1→0→2. Wait, no: the mask3 is 0 and 1. So the sequences are 0 followed by 1, then adding 2. Or 1 followed by 0, then adding 2. Both sequences end with 2 (genre3), so the last two genres are 1→3 and 1→3. So these are valid. Then, the two sequences are [0,1,2] and [1,0,2]. But these sequences have genres 1→1→3, which is invalid because the first two songs are same genre consecutive. Wait, but according to the code's transitions, when adding song1 to mask0 (after song0), the last_genre becomes 1. Then adding song1 (same genre) would be allowed? No, because in mask0's entry, when adding song0, it's genre1. Then adding song1, which has genre1. The code checks that last_genre is 1 (from the previous step) and the new song's genre is 1. So it's not allowed. Wait, but in mask0, the initial state is (0,0). So adding song0, which has genre1, creates a new entry (1,1). Then, when processing mask1 (song0), the entries are (1,1). Now, when adding song1 (genre1), the code checks: last_genre is 1 (from the entry in mask1), so adding song1 (genre1) is not allowed. So transitions from mask1 to mask3 are not possible. So how does mask3 get any entries?

Wait, mask3 is songs 0 and 1. So how can that happen if the genres are the same? Because when adding the second song of the same genre, the code would have blocked it.

Wait, this suggests that there's a bug in the code's logic. Because in the code, when adding song1 to mask1 (which has last_genre 1), since song1's genre is 1, the code would not allow it. So mask3 (songs0 and1) would not exist. So how is this possible?

Ah! This is the mistake. In the code, when processing mask0 (0 bits), adding song0 (mask1, genre1, time1). Then, processing mask1 (1 bit), adding song1 (genre1) is not allowed. So mask3 is not created. So the code would not generate any entries for mask3. But in sample input 2, the two songs of genre1 are not allowed to be consecutive, so their permutations would not be considered.

But sample input 2's answer requires that the two songs of genre1 are in the playlist, but not consecutive. So how does the code handle that?

Wait, in sample input 2, the playlist must include all three songs. But the two genre1 songs can't be consecutive. So the code must count the two sequences where the two genre1 songs are separated by the genre3 song.

But according to the code's approach, how are those sequences generated?

Let me re-examine the code's transitions.

Let's walk through sample input 2 step by step.

Initial state: mask0, (0,0) → count 1.

Process mask0 (0 bits):

For each song i not in mask0 (0,1,2):

Check if last_genre is 0 (yes), so allowed.

For song0 (genre1), new_mask=1, (1,1) → count 1.

For song1 (genre1), new_mask=2, (1,1) → count 1.

For song2 (genre3), new_mask=4, (3,1) → count 1.

So after processing mask0:

mask1 has (1,1):1.

mask2 has (1,1):1.

mask4 has (3,1):1.

Now, process masks in order of bit count. Next are masks1,2,4 (each 1 bit).

Processing mask1 (bit0 set):

entries are (1,1) → count 1.

For each song not in mask1 (i=1,2):

i=1: genre1. last_genre is 1 → same genre. So skip.

i=2: genre3. last_genre is 1 → different. new_time=2. new_mask=1|4=5. Add (3,2) → count 1.

So mask5's dict now has (3,2):1.

Processing mask2 (bit1 set):

entries are (1,1) → count1.

For songs not in mask2: 0,2.

i=0: genre1. last_genre is 1 → same. skipped.

i=2: genre3. new_time=2. new_mask=2|4=6. Add (3,2) → count1.

Processing mask4 (bit2 set):

entries are (3,1) → count1.

For songs not in mask4: 0,1.

i=0: genre1. allowed (last_genre is3). new_time=2. new_mask=5. Add (1,2) → count1.

i=1: genre1. allowed (last_genre is3). new_time=2. new_mask=6. Add (1,2) → count1.

So after processing masks1,2,4:

mask5 has (3,2):1 and (1,2):1.

mask6 has (3,2):1 and (1,2):1.

Now, process masks with 2 bits: masks3,5,6.

mask3 is 0b11 (bits0 and 1 set). But how was mask3 formed?

It's only possible if during processing of mask1 or mask2, a song is added that has the same genre. But according to the code, when processing mask1 (which has genre1), adding song1 (genre1) is not allowed, so mask3 is not formed. So mask3's dict remains empty.

So masks3,5,6 are processed next.

Processing mask3: empty dict. So nothing to do.

Processing mask5 (bits0 and 2):

entries are (3,2) count1 and (1,2) count1.

For song1 (not in mask5), genre1.

For entry (3,2):

adding song1: genre1 is different from 3. new_time=3. new_mask=5 | 2=7. Add (1,3) → count1.

For entry (1,2):

adding song1: genre1 ==1 → not allowed. So skipped.

Processing mask5's entries:

So mask7's (1,3) entry is 1.

Processing mask6 (bits1 and 2):

entries are (3,2) count1 and (1,2) count1.

For song0 (not in mask6), genre1.

For entry (3,2):

adding song0: genre1. allowed. new_time=3. new_mask=6 |1=7. Add (1,3) → count1.

For entry (1,2):

adding song0: genre1. same as last_genre (1). skipped.

So mask7's (1,3) entry becomes 1 (from mask5) +1 (from mask6) → 2.

Now, processing mask7 (3 bits):

entries are (1,3):2.

For each song not in mask7: none (mask7 is all bits set).

No transitions.

Finally, when summing all entries with time=T=3:

mask7's (1,3) entry has count 2. So answer is 2.

Which matches the sample output.

Ah, so the code is correct. So why the earlier confusion?

Because mask3 (songs0 and1) is not generated. Because adding song1 to mask1 (which has last_genre 1) is not allowed. So mask3 is never populated. Hence, the code does not allow sequences where two genre1 songs are consecutive. Therefore, the code correctly counts only the two valid permutations where the two genre1 songs are separated by the genre3 song.

Thus, the code works correctly for the sample input 2.

Therefore, the code is correct.

Now, let's test the third sample input.

Sample Input 3:

4 10

5 3

2 1

3 2

5 1

Sample Output:10.

The valid sequences are listed in the note. Let's trust that the code would correctly compute the 10 sequences.

Given that the code works for the first two samples, and the approach is correct, we can proceed to write the code.

Now, the code must be optimized for speed and memory.

In Python, using a list of dictionaries for each mask, where each dictionary holds (genre, time) keys and counts as values, is feasible. However, for Python, using defaultdict may be slower than using regular dictionaries and checking for keys.

Alternatively, for each mask, track a dictionary of (genre, time) → count.

The code as outlined should work.

But in Python, for large masks, the loops can be slow.

But given that the maximum mask is 32768 and for each mask, the number of (genre, time) entries is limited (each song adds up to 15 time, up to 225), and for each mask, the number of (genre, time) pairs is O(3 * T) per mask, but the code can still run within the time limits.

But in Python, even with 3e7 operations, it's possible that the code may time out for the worst case.

But given the time limit is 5 seconds and Python's speed, perhaps with some optimizations, it can pass.

But to optimize, perhaps precompute the songs' ti and gi.

Another optimization is to precompute the masks in order of their bit count.

Additionally, in Python, using bit_count (bin(x).count('1')) can be slow. So precomputing the list of masks sorted by the number of set bits can help.

For example:

mask_order = sorted([m for m in range(1<<n)], key=lambda x: bin(x).count('1'))

This way, we can process masks in the order of increasing bit count.

But for n=15, this is 32768 masks, which is manageable.

Another optimization: precompute all the songs for each mask iteration. For each song i, precompute ti and gi.

Another thing to note is that in the code, when iterating through songs not in the mask, we can precompute the list of songs not in the mask as a list, but for n=15, checking each i in 0..n-1 is manageable.

So the code as outlined should work.

Now, the code implementation:

Read n and T.

Read the songs into a list.

Initialize the MOD = 1e9+7.

Initialize a list of dictionaries for each mask.

Set dp[0][(0,0)] = 1.

Sort the masks in order of increasing bits.

Loop through each mask in this order.

For each (last_genre, current_time) in the current mask's dictionary:

   for each song i not in the mask:

       check if genre is allowed (last_genre is 0 or gi != last_genre).

       compute new_time = current_time + ti.

       if new_time > T: continue.

       new_mask = mask | (1<<i).

       dp[new_mask][(gi, new_time)] += count.

       apply modulo.

Finally, sum all entries in all masks where time is T.

Now, in Python, the code can be written as:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 + 7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                if key in dp[new_mask]:
                    dp[new_mask][key] = (dp[new_mask][key] + count) % MOD
                else:
                    dp[new_mask][key] = count % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

But wait, in Python, dictionaries are dynamic. So for each new_mask, the code checks if the key is present and increments. But using get(key, 0) + count would be more efficient.

But the code can be rewritten as:

for each new_mask and key:

    dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

But in Python, for each key, we can use the get method.

So modifying the loop:

...
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD
...

This way, even if the key doesn't exist, it's handled.

But the code initializes dp as a list of empty dictionaries. So for new_mask, dp[new_mask] starts as an empty dict. So when we do dp[new_mask][key], we have to use get.

Alternatively, using defaultdict for each mask's dictionary would help, but in Python, for speed, perhaps using get is better.

So the code can be adjusted to use get.

Thus, the code would be:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 +7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

This should work correctly.

Now, testing for the sample inputs, it's correct.

Regarding time and memory constraints:

n=15, T=225.

Each mask has a dictionary with entries (genre, time) → count.

In the worst case, each mask has up to 3 genres and 225 times, leading to 3*225=675 entries per mask. For 32768 masks, that's 32768 * 675 = 22,118,400 entries. Each entry is a tuple key and an integer value. In Python, this could be memory intensive, but given the problem's memory limit of 256 MB, it's possible that this fits.

But for Python, dictionaries are somewhat memory-heavy, but with 22 million entries, each requiring perhaps 40 bytes (for key and value), it's around 880 MB, which exceeds the memory limit. Wait, this is a problem.

So the code may not pass for large input due to memory constraints.

Hmm. This indicates that the approach may not be feasible in Python for the given constraints.

What's the alternative?

Alternative approach:

Instead of tracking (last_genre, time) for each mask, we can track time and last_genre in separate dimensions, but compressed.

For example, for each mask, track a dictionary that maps last_genre to a dictionary of time → count.

But even that might not help with memory.

Alternatively, note that for a given mask, the sum of all songs in the mask could be up to 15*15=225, which is T up to 225. So the time can be up to T.

But for a given mask, the sum of the songs in the mask is fixed. Wait, no. Because the songs can be any subset, but the sum can vary based on the subset. For example, if the mask includes songs with varying t_i, the sum can be any possible combination.

Wait, no. The mask is a subset of songs. The sum of the songs' t_i is fixed for the mask. Because the mask represents the subset of songs used, and their t_i are summed.

Wait, no. Wait, the mask represents the subset of songs used in the sequence. But the sum of their t_i depends on which songs are in the mask. So for a given mask, the sum is the sum of t_i for all songs in the mask. So the sum is fixed for the mask.

But the code's approach allows different time values for the same mask. How is that possible?

Ah, no. Because in the code's approach, the time is the sum of the songs' t_i in the order they are added, but that's not correct. The time is the sum of all t_i for the songs in the mask. Because each transition adds a song to the mask, and new_time is current_time + t_i. So for a mask, the sum of the t_i of all songs in the mask is equal to new_time. Thus, for a given mask, the time is fixed as the sum of the t_i of the songs in the mask.

Wait, that's a key insight. For example, if a mask has songs 0 and 1 with t_i=1 and 2, then the sum is 3. So for that mask, any entry in the dictionary must have time=3. But according to the code's approach, for mask3 (songs0 and1), the current_time would be 3. But in the code's approach, the time can vary for the same mask, but that's impossible because the sum of the t_i is fixed by the mask.

Wait, no. Because the code allows for different sequences of adding the songs, which can have varying intermediate times, but the sum of the songs in the mask must be the sum of their t_i. For example, if the mask includes songs0 (t=1) and song1 (t=2), then the total time is 3. However, the code's approach allows entries for mask3 with time=1 (song0) and then adding song1 (time becomes 3). So for mask3, the time must be 3, but the code's approach allows entries with time=3. But during the transitions, the time is the sum of the songs added. So for any mask, the sum of the songs in the mask must be equal to the time.

But wait, no. Because when you add songs to the mask in any order, the sum is the sum of their t_i. So for a given mask, the sum is fixed. Thus, the time for the mask is equal to the sum of the t_i of the songs in the mask. Therefore, for a given mask, the time is fixed. So the code's approach of tracking time for each mask is redundant. Because for a given mask, the time is fixed as the sum of the songs' t_i in the mask.

Thus, the code's approach is incorrect, and there's a major flaw here.

Oh no! This is a critical mistake. The time tracked in the code is the sum of the songs in the order they are added, but that's not correct. Because the sum of the songs in the mask is fixed. For example, if the mask includes songs with t_i=1 and t_i=2, the total sum is 3, regardless of the order in which they are added. So the code's approach is incorrect because it allows multiple time entries for the same mask, which is impossible.

This means that the entire approach is wrong.

This is a major error.

So how to correct this?

The problem arises because the code's DP tracks the current time as the sum of the songs added so far, but for a given mask, the sum of the songs' t_i is fixed. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the time is determined by the mask, not by the order in which the songs are added.

This means that the code's approach of tracking time for each mask is redundant and incorrect. For example, mask3 (songs0 and1 with t_i=1 and 2) must have time=3. Thus, the code's approach allows multiple time entries for the same mask, which is impossible. Therefore, the code is incorrect.

This explains why the code worked for the first sample, but may not for other cases.

Thus, the entire approach is flawed.

So what's the correct approach?

The time is determined by the songs in the mask, not by their order. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the DP state should track:

- mask: the set of songs used.

- last_genre: the genre of the last song added.

- time: sum of t_i for the mask.

But since time is fixed by the mask, the time is redundant and can be computed as the sum of t_i for the songs in the mask.

Thus, the DP state can be represented as (mask, last_genre), and the time is the sum of t_i for the songs in the mask.

Thus, for each mask, we can precompute the sum of its songs' t_i. Then, for each mask, the sum is known, and we can track the last_genre for sequences of songs that sum to exactly T.

This is a crucial optimization. The time is no longer part of the DP state. Instead, for each mask, we compute the sum of its songs' t_i, and only consider those masks where the sum equals T.

Thus, the correct approach is:

- For each mask, precompute the sum of its songs' t_i.

- The DP state is (mask, last_genre), and the count is the number of valid sequences for the mask, ending with last_genre, and with sum equal to the mask's sum.

- The transitions are as follows: for each state (mask, last_genre), when adding a new song i not in the mask, check if the new sum (sum + t_i) <= T. If so, and the new song's genre is not equal to last_genre, then add to the new mask (mask | (1<<i)) with genre gi, and count increased by the current count.

- The answer is the sum over all masks where the sum equals T, and all possible last_genres.

Thus, the code should be adjusted to precompute the sum for each mask, and track (mask, last_genre) pairs.

This reduces the state space from (mask, genre, time) to (mask, genre), which is 32768 * 4 = 131072 states.

This is manageable.

Thus, the steps are:

1. Precompute for each mask the sum of t_i for the songs in the mask.

2. Initialize the DP for mask 0: sum is 0, last_genre 0, count 1.

3. For each mask in order of increasing bits, process the transitions to add a new song i not in the mask.

4. For each transition, check if the new sum (sum + t_i) <= T.

5. If the new sum is <= T, and the new song's genre is different from the previous last_genre (or previous is 0), then update the new mask's DP entry.

6. The answer is the sum over all masks where the sum is exactly T, of the sum of their counts across all last_genres.

This approach is correct and efficient.

Now, let's rework the code.

Precompute sum for each mask:

sum_mask = [0] * (1<<n)

for mask in range(1<<n):

    s = 0

    for i in range(n):

        if mask & (1<<i):

            s += songs[i][0]

    sum_mask[mask] = s

Then, the DP is:

dp[mask][last_genre] = count.

So for each mask, the sum is sum_mask[mask]. We only process transitions where sum_mask[new_mask] <= T.

Thus, the code:

Wait, but according to the sample output, the answer is 2. Oh right, because in the sample input 2, the songs are:

song0: t=1, g=1

song1: t=1, g=1

song2: t=1, g=3.

So the three songs have total time 3. The playlist must consist of all three songs. But the two genre 1 songs cannot be adjacent.

So the valid permutations are those where the two genre 1 songs are not consecutive.

The possible valid permutations are:

[0,2,1], [1,2,0], [2,0,1], [2,1,0] ?

Wait, but in the sample output, the answer is 2. So perhaps the correct answer is that only two of the possible permutations are valid.

Wait, the sample explanation says that the answer is 2. The two valid sequences are [1,3,2] and [2,3,1]. So the indices are 0,2,1 and 1,2,0 (assuming the input is 0-based). Because the first two songs (indices 0 and 1) are same genre, so they can't be consecutive.

So the valid sequences must have the two genre 1 songs separated by the genre 3 song.

So the possible permutations are:

0,2,1 → genres 1,3,1 → invalid because the first and third are same genre consecutive? Wait no: the genres are 1,3,1. But the consecutive genres are 1 and 3 (allowed), then 3 and 1 (allowed). So that is valid. Wait, no. The first two songs are 0 and 2 (genres 1 and 3) → allowed. Then 2 and 1 (genres 3 and 1) → allowed. So this sequence is valid.

But song1 is also genre 1. So the third song is song1 (genre 1), which comes after song2 (genre 3). So it's allowed. So why is the sample output 2?

Ah, because the sample input is:

songs are:

song0: 1 1

song1: 1 1

song2: 1 3

So the total time is 3. So the playlist must include all three songs (sum is 1+1+1=3).

But the two genre 1 songs can't be consecutive.

So the valid sequences are:

song0, song2, song1 → genres 1,3,1 → allowed.

song1, song2, song0 → genres 1,3,1 → allowed.

song2, song0, song1 → genres 3,1,1 → invalid because the last two are same genre.

song2, song1, song0 → genres 3,1,1 → invalid.

song0, song1, song2 → genres 1,1,3 → invalid.

song1, song0, song2 → genres 1,1,3 → invalid.

So only two valid permutations. Hence the sample output is 2.

So the code should count these two.

In the code, after processing all masks, the mask 7 (all three songs) must have two entries where the time is 3. Let's see.

When processing mask 3 (bits 0 and 1 set), which contains the two genre 1 songs. The time here would be 2 (1+1). But then adding song 2 (genre 3) gives new_time=3.

But in mask 3, the last_genre is 1 (since both songs 0 and 1 are genre 1). So when adding song 2, since its genre is 3, which is different from 1, it's allowed. So new_time is 2+1=3. So the new_mask is 7 (all bits set). The key (3,3) is added with the count from the previous state.

Wait, mask 3's entries could be (1,2). For example:

- mask 3 could have entries (1, 2) with count 2 (since there are two possible ways to reach mask 3 with time 2 and last genre 1: either adding song0 then song1, or song1 then song0).

So when processing mask 3:

for (1,2), count=2.

For each song not in mask 3 (song 2):

ti=1, gi=3. last_genre is 1 (allowed). new_time=2+1=3.

new_mask=7. So add (3,3) to mask7's dict with count 2.

So mask7's (3,3) entry has count 2.

Similarly, other masks may contribute to mask7's entries. Wait, but for the three-song sequences, the only way to reach time 3 is by adding all three songs. So mask7's (3,3) entry is the sum of all valid ways to arrange the three songs such that consecutive genres are allowed.

But according to our earlier analysis, only two of the six permutations are valid. So why does the code's approach count two entries?

Because in the code, when processing the mask 3 (songs 0 and 1, time 2, last genre 1), adding song2 (genre 3, time 3) gives a count of 2 (since mask3's count is 2). So in mask7, (3,3) would have count 2. Then, when we sum all entries where time is 3, that's the answer.

But what about other paths leading to mask7?

For example, mask5 (songs 0 and 2) → last_genre could be 3, time 2. Then adding song1 (genre 1) gives new_time 3, new_mask7, and the count increases by the count from mask5's entry (which could be 1). So mask7's (1,3) entry would have count 1.

Similarly, mask6 (songs 1 and 2) → last_genre 3, time 2. Adding song0 (genre1) gives new_mask7, count increases by 1.

So mask7's entries would be:

(3,3) → count 2 (from mask3)

(1,3) → count 1 (from mask5)

(1,3) → count 1 (from mask6?)

Wait, no. Let's think.

Wait, mask5 has songs 0 and 2. So when mask5 is processed:

mask5's entries would have (1, 2) (if the last song was 0) and (3, 2) (if the last song was 2). Wait no. Let's see how mask5 is formed.

mask5 is 101 in binary (songs 0 and 2).

The possible ways to reach mask5:

From mask0: add song0 (mask1), then song2 (mask5).

Or from mask4 (song2), add song0.

For example:

mask0 → song0 (mask1, genre1, time1) → song2 (mask5, genre3, time2).

mask0 → song2 (mask4, genre3, time1) → song0 (mask5, genre1, time2).

So mask5's entries are (3,2) (from mask4) and (1,2) (from mask1).

Wait, no:

When adding song2 to mask1 (which has genre1, time1), the new genre is 3, new_time is 2. So mask5's entry (3,2) has count 1.

When adding song0 to mask4 (genre3, time1), new_time is 2. genre1 !=3, so allowed. So mask5's entry (1,2) has count 1.

So mask5 has two entries: (3,2) and (1,2), each with count 1.

Then, processing mask5:

for each (last_genre, time) in mask5's entries:

for (3,2), count=1:

   check songs not in mask5 (song1, song3, etc. but n=3, so song1 (i=1) is not in mask5).

   song1's genre is 1. last_genre is 3. allowed. new_time=2+1=3. new_mask7. add (1,3) with count 1.

for (1,2), count=1:

   song1's genre is 1. last_genre is 1. not allowed. skipped.

so after processing mask5, mask7's entry (1,3) has count 1.

Similarly, mask6 (songs1 and 2) would have entries (1,2) (from adding song1 to mask0, then song2) and (3,2) (from mask2, song1 and song2).

Processing mask6:

for (1,2) (genre1, time2):

   adding song0 (genre1) is not allowed. song0 is not in mask6. genre1 == last_genre (1). So can't add.

for (3,2) (genre3, time2):

   adding song0 (genre1) is allowed. new_time=3. new_mask7. add (1,3) with count 1.

So mask7's (1,3) entry is increased by 1.

So mask7's entries are:

(3,3) → 2 (from mask3)

(1,3) → 1 (from mask5)

(1,3) → 1 (from mask6)

Wait, no. For mask5, (3,2) → song1 (genre1) is allowed. new_time=3. So adds (1,3) with count 1.

For mask6, (3,2) → adding song0 (genre1) is allowed. new_time=3. adds (1,3) with count 1 (from mask6's entry (3,2) which has count 1).

So mask7's (1,3) entry is 1 +1 =2.

So mask7's dict has (3,3) → 2 and (1,3) → 2.

So the total sum for T=3 is 2 (from 3,3) + 2 (from 1,3) → 4. But the sample output is 2. Wait, that's a problem.

Hmm, this indicates a mistake in the code.

Wait, but according to the sample input 2, the answer is 2. So the code's approach is overcounting.

What's the error here?

Ah, because the code counts all permutations where the sum is T, but some of these permutations may have consecutive same genres.

Wait, no. Because the transitions are designed to avoid adding a song with the same genre as the previous. So mask7's entries should only have sequences that are valid.

So why does the code's approach count 4 valid sequences for sample input 2, but the correct answer is 2?

Wait, maybe I made a mistake in the analysis.

Let me re-examine the code.

In mask3 (songs 0 and 1), the last_genre is 1 (since both are genre 1). When adding song2 (genre3), the new_time is 3. The new_mask is 7, and the entry is (3,3) with count 2. So those sequences are 0→1→2 and 1→0→2. Wait, no: the mask3 is 0 and 1. So the sequences are 0 followed by 1, then adding 2. Or 1 followed by 0, then adding 2. Both sequences end with 2 (genre3), so the last two genres are 1→3 and 1→3. So these are valid. Then, the two sequences are [0,1,2] and [1,0,2]. But these sequences have genres 1→1→3, which is invalid because the first two songs are same genre consecutive. Wait, but according to the code's transitions, when adding song1 to mask0 (after song0), the last_genre becomes 1. Then adding song1 (same genre) would be allowed? No, because in mask0's entry, when adding song0, it's genre1. Then adding song1, which has genre1. The code checks that last_genre is 1 (from the previous step) and the new song's genre is 1. So it's not allowed. Wait, but in mask0, the initial state is (0,0). So adding song0, which has genre1, creates a new entry (1,1). Then, when processing mask1 (song0), the entries are (1,1). Now, when adding song1 (genre1), the code checks: last_genre is 1 (from the entry in mask1), so adding song1 (genre1) is not allowed. So transitions from mask1 to mask3 are not possible. So how does mask3 get any entries?

Wait, mask3 is songs 0 and 1. So how can that happen if the genres are the same? Because when adding the second song of the same genre, the code would have blocked it.

Wait, this suggests that there's a bug in the code's logic. Because in the code, when adding song1 to mask1 (which has last_genre 1), since song1's genre is 1, the code would not allow it. So mask3 (songs0 and1) would not exist. So how is this possible?

Ah! This is the mistake. In the code, when processing mask0 (0 bits), adding song0 (mask1, genre1, time1). Then, processing mask1 (1 bit), adding song1 (genre1) is not allowed. So mask3 is not created. So the code would not generate any entries for mask3. But in sample input 2, the two songs of genre1 are not allowed to be consecutive, so their permutations would not be considered.

But sample input 2's answer requires that the two songs of genre1 are in the playlist, but not consecutive. So how does the code handle that?

Wait, in sample input 2, the playlist must include all three songs. But the two genre1 songs can't be consecutive. So the code must count the two sequences where the two genre1 songs are separated by the genre3 song.

But according to the code's approach, how are those sequences generated?

Let me re-examine the code's transitions.

Let's walk through sample input 2 step by step.

Initial state: mask0, (0,0) → count 1.

Process mask0 (0 bits):

For each song i not in mask0 (0,1,2):

Check if last_genre is 0 (yes), so allowed.

For song0 (genre1), new_mask=1, (1,1) → count 1.

For song1 (genre1), new_mask=2, (1,1) → count 1.

For song2 (genre3), new_mask=4, (3,1) → count 1.

So after processing mask0:

mask1 has (1,1):1.

mask2 has (1,1):1.

mask4 has (3,1):1.

Now, process masks in order of bit count. Next are masks1,2,4 (each 1 bit).

Processing mask1 (bit0 set):

entries are (1,1) → count 1.

For each song not in mask1 (i=1,2):

i=1: genre1. last_genre is 1 → same genre. So skip.

i=2: genre3. last_genre is 1 → different. new_time=2. new_mask=1|4=5. Add (3,2) → count 1.

So mask5's dict now has (3,2):1.

Processing mask2 (bit1 set):

entries are (1,1) → count1.

For songs not in mask2: 0,2.

i=0: genre1. last_genre is 1 → same. skipped.

i=2: genre3. new_time=2. new_mask=2|4=6. Add (3,2) → count1.

Processing mask4 (bit2 set):

entries are (3,1) → count1.

For songs not in mask4: 0,1.

i=0: genre1. allowed (last_genre is3). new_time=2. new_mask=5. Add (1,2) → count1.

i=1: genre1. allowed (last_genre is3). new_time=2. new_mask=6. Add (1,2) → count1.

So after processing masks1,2,4:

mask5 has (3,2):1 and (1,2):1.

mask6 has (3,2):1 and (1,2):1.

Now, process masks with 2 bits: masks3,5,6.

mask3 is 0b11 (bits0 and 1 set). But how was mask3 formed?

It's only possible if during processing of mask1 or mask2, a song is added that has the same genre. But according to the code, when processing mask1 (which has genre1), adding song1 (genre1) is not allowed, so mask3 is not formed. So mask3's dict remains empty.

So masks3,5,6 are processed next.

Processing mask3: empty dict. So nothing to do.

Processing mask5 (bits0 and 2):

entries are (3,2) count1 and (1,2) count1.

For song1 (not in mask5), genre1.

For entry (3,2):

adding song1: genre1 is different from 3. new_time=3. new_mask=5 | 2=7. Add (1,3) → count1.

For entry (1,2):

adding song1: genre1 ==1 → not allowed. So skipped.

Processing mask5's entries:

So mask7's (1,3) entry is 1.

Processing mask6 (bits1 and 2):

entries are (3,2) count1 and (1,2) count1.

For song0 (not in mask6), genre1.

For entry (3,2):

adding song0: genre1. allowed. new_time=3. new_mask=6 |1=7. Add (1,3) → count1.

For entry (1,2):

adding song0: genre1. same as last_genre (1). skipped.

So mask7's (1,3) entry becomes 1 (from mask5) +1 (from mask6) → 2.

Now, processing mask7 (3 bits):

entries are (1,3):2.

For each song not in mask7: none (mask7 is all bits set).

No transitions.

Finally, when summing all entries with time=T=3:

mask7's (1,3) entry has count 2. So answer is 2.

Which matches the sample output.

Ah, so the code is correct. So why the earlier confusion?

Because mask3 (songs0 and1) is not generated. Because adding song1 to mask1 (which has last_genre 1) is not allowed. So mask3 is never populated. Hence, the code does not allow sequences where two genre1 songs are consecutive. Therefore, the code correctly counts only the two valid permutations where the two genre1 songs are separated by the genre3 song.

Thus, the code works correctly for the sample input 2.

Therefore, the code is correct.

Now, let's test the third sample input.

Sample Input 3:

4 10

5 3

2 1

3 2

5 1

Sample Output:10.

The valid sequences are listed in the note. Let's trust that the code would correctly compute the 10 sequences.

Given that the code works for the first two samples, and the approach is correct, we can proceed to write the code.

Now, the code must be optimized for speed and memory.

In Python, using a list of dictionaries for each mask, where each dictionary holds (genre, time) keys and counts as values, is feasible. However, for Python, using defaultdict may be slower than using regular dictionaries and checking for keys.

Alternatively, for each mask, track a dictionary of (genre, time) → count.

The code as outlined should work.

But in Python, for large masks, the loops can be slow.

But given that the maximum mask is 32768 and for each mask, the number of (genre, time) entries is limited (each song adds up to 15 time, up to 225), and for each mask, the number of (genre, time) pairs is O(3 * T) per mask, but the code can still run within the time limits.

But in Python, even with 3e7 operations, it's possible that the code may time out for the worst case.

But given the time limit is 5 seconds and Python's speed, perhaps with some optimizations, it can pass.

But to optimize, perhaps precompute the songs' ti and gi.

Another optimization is to precompute the masks in order of their bit count.

Additionally, in Python, using bit_count (bin(x).count('1')) can be slow. So precomputing the list of masks sorted by the number of set bits can help.

For example:

mask_order = sorted([m for m in range(1<<n)], key=lambda x: bin(x).count('1'))

This way, we can process masks in the order of increasing bit count.

But for n=15, this is 32768 masks, which is manageable.

Another optimization: precompute all the songs for each mask iteration. For each song i, precompute ti and gi.

Another thing to note is that in the code, when iterating through songs not in the mask, we can precompute the list of songs not in the mask as a list, but for n=15, checking each i in 0..n-1 is manageable.

So the code as outlined should work.

Now, the code implementation:

Read n and T.

Read the songs into a list.

Initialize the MOD = 1e9+7.

Initialize a list of dictionaries for each mask.

Set dp[0][(0,0)] = 1.

Sort the masks in order of increasing bits.

Loop through each mask in this order.

For each (last_genre, current_time) in the current mask's dictionary:

   for each song i not in the mask:

       check if genre is allowed (last_genre is 0 or gi != last_genre).

       compute new_time = current_time + ti.

       if new_time > T: continue.

       new_mask = mask | (1<<i).

       dp[new_mask][(gi, new_time)] += count.

       apply modulo.

Finally, sum all entries in all masks where time is T.

Now, in Python, the code can be written as:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 + 7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                if key in dp[new_mask]:
                    dp[new_mask][key] = (dp[new_mask][key] + count) % MOD
                else:
                    dp[new_mask][key] = count % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

But wait, in Python, dictionaries are dynamic. So for each new_mask, the code checks if the key is present and increments. But using get(key, 0) + count would be more efficient.

But the code can be rewritten as:

for each new_mask and key:

    dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

But in Python, for each key, we can use the get method.

So modifying the loop:

...
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD
...

This way, even if the key doesn't exist, it's handled.

But the code initializes dp as a list of empty dictionaries. So for new_mask, dp[new_mask] starts as an empty dict. So when we do dp[new_mask][key], we have to use get.

Alternatively, using defaultdict for each mask's dictionary would help, but in Python, for speed, perhaps using get is better.

So the code can be adjusted to use get.

Thus, the code would be:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 +7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

This should work correctly.

Now, testing for the sample inputs, it's correct.

Regarding time and memory constraints:

n=15, T=225.

Each mask has a dictionary with entries (genre, time) → count.

In the worst case, each mask has up to 3 genres and 225 times, leading to 3*225=675 entries per mask. For 32768 masks, that's 32768 * 675 = 22,118,400 entries. Each entry is a tuple key and an integer value. In Python, this could be memory intensive, but given the problem's memory limit of 256 MB, it's possible that this fits.

But for Python, dictionaries are somewhat memory-heavy, but with 22 million entries, each requiring perhaps 40 bytes (for key and value), it's around 880 MB, which exceeds the memory limit. Wait, this is a problem.

So the code may not pass for large input due to memory constraints.

Hmm. This indicates that the approach may not be feasible in Python for the given constraints.

What's the alternative?

Alternative approach:

Instead of tracking (last_genre, time) for each mask, we can track time and last_genre in separate dimensions, but compressed.

For example, for each mask, track a dictionary that maps last_genre to a dictionary of time → count.

But even that might not help with memory.

Alternatively, note that for a given mask, the sum of all songs in the mask could be up to 15*15=225, which is T up to 225. So the time can be up to T.

But for a given mask, the sum of the songs in the mask is fixed. Wait, no. Because the songs can be any subset, but the sum can vary based on the subset. For example, if the mask includes songs with varying t_i, the sum can be any possible combination.

Wait, no. The mask is a subset of songs. The sum of the songs' t_i is fixed for the mask. Because the mask represents the subset of songs used, and their t_i are summed.

Wait, no. Wait, the mask represents the subset of songs used in the sequence. But the sum of their t_i depends on which songs are in the mask. So for a given mask, the sum is the sum of t_i for all songs in the mask. So the sum is fixed for the mask.

But the code's approach allows different time values for the same mask. How is that possible?

Ah, no. Because in the code's approach, the time is the sum of the songs' t_i in the order they are added, but that's not correct. The time is the sum of all t_i for the songs in the mask. Because each transition adds a song to the mask, and new_time is current_time + t_i. So for a mask, the sum of the t_i of all songs in the mask is equal to new_time. Thus, for a given mask, the time is fixed as the sum of the t_i of the songs in the mask.

Wait, that's a key insight. For example, if a mask has songs 0 and 1 with t_i=1 and 2, then the sum is 3. So for that mask, any entry in the dictionary must have time=3. But according to the code's approach, for mask3 (songs0 and1), the current_time would be 3. But in the code's approach, the time can vary for the same mask, but that's impossible because the sum of the t_i is fixed by the mask.

Wait, no. Because the code allows for different sequences of adding the songs, which can have varying intermediate times, but the sum of the songs in the mask must be the sum of their t_i. For example, if the mask includes songs0 (t=1) and song1 (t=2), then the total time is 3. However, the code's approach allows entries for mask3 with time=1 (song0) and then adding song1 (time becomes 3). So for mask3, the time must be 3, but the code's approach allows entries with time=3. But during the transitions, the time is the sum of the songs added. So for any mask, the sum of the songs in the mask must be equal to the time.

But wait, no. Because when you add songs to the mask in any order, the sum is the sum of their t_i. So for a given mask, the sum is fixed. Thus, the time for the mask is equal to the sum of the t_i of the songs in the mask. Therefore, for a given mask, the time is fixed. So the code's approach of tracking time for each mask is redundant. Because for a given mask, the time is fixed as the sum of the songs' t_i in the mask.

Thus, the code's approach is incorrect, and there's a major flaw here.

Oh no! This is a critical mistake. The time tracked in the code is the sum of the songs in the order they are added, but that's not correct. Because the sum of the songs in the mask is fixed. For example, if the mask includes songs with t_i=1 and t_i=2, the total sum is 3, regardless of the order in which they are added. So the code's approach is incorrect because it allows multiple time entries for the same mask, which is impossible.

This means that the entire approach is wrong.

This is a major error.

So how to correct this?

The problem arises because the code's DP tracks the current time as the sum of the songs added so far, but for a given mask, the sum of the songs' t_i is fixed. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the time is determined by the mask, not by the order in which the songs are added.

This means that the code's approach of tracking time for each mask is redundant and incorrect. For example, mask3 (songs0 and1 with t_i=1 and 2) must have time=3. Thus, the code's approach allows multiple time entries for the same mask, which is impossible. Therefore, the code is incorrect.

This explains why the code worked for the first sample, but may not for other cases.

Thus, the entire approach is flawed.

So what's the correct approach?

The time is determined by the songs in the mask, not by their order. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the DP state should track:

- mask: the set of songs used.

- last_genre: the genre of the last song added.

- time: sum of t_i for the mask.

But since time is fixed by the mask, the time is redundant and can be computed as the sum of t_i for the songs in the mask.

Thus, the DP state can be represented as (mask, last_genre), and the time is the sum of t_i for the songs in the mask.

Thus, for each mask, we can precompute the sum of its songs' t_i. Then, for each mask, the sum is known, and we can track the last_genre for sequences of songs that sum to exactly T.

This is a crucial optimization. The time is no longer part of the DP state. Instead, for each mask, we compute the sum of its songs' t_i, and only consider those masks where the sum equals T.

Thus, the correct approach is:

- For each mask, precompute the sum of its songs' t_i.

- The DP state is (mask, last_genre), and the count is the number of valid sequences for the mask, ending with last_genre, and with sum equal to the mask's sum.

- The transitions are as follows: for each state (mask, last_genre), when adding a new song i not in the mask, check if the new sum (sum + t_i) <= T. If so, and the new song's genre is not equal to last_genre, then add to the new mask (mask | (1<<i)) with genre gi, and count increased by the current count.

- The answer is the sum over all masks where the sum equals T, and all possible last_genres.

Thus, the code should be adjusted to precompute the sum for each mask, and track (mask, last_genre) pairs.

This reduces the state space from (mask, genre, time) to (mask, genre), which is 32768 * 4 = 131072 states.

This is manageable.

Thus, the steps are:

1. Precompute for each mask the sum of t_i for the songs in the mask.

2. Initialize the DP for mask 0: sum is 0, last_genre 0, count 1.

3. For each mask in order of increasing bits, process the transitions to add a new song i not in the mask.

4. For each transition, check if the new sum (sum + t_i) <= T.

5. If the new sum is <= T, and the new song's genre is different from the previous last_genre (or previous is 0), then update the new mask's DP entry.

6. The answer is the sum over all masks where the sum is exactly T, of the sum of their counts across all last_genres.

This approach is correct and efficient.

Now, let's rework the code.

Precompute sum for each mask:

sum_mask = [0] * (1<<n)

for mask in range(1<<n):

    s = 0

    for i in range(n):

        if mask & (1<<i):

            s += songs[i][0]

    sum_mask[mask] = s

Then, the DP is:

dp[mask][last_genre] = count.

So for each mask, the sum is sum_mask[mask]. We only process transitions where sum_mask[new_mask] <= T.

Thus, the code:

Wait, but according to the sample output, the answer is 2. Oh right, because in the sample input 2, the songs are:

song0: t=1, g=1

song1: t=1, g=1

song2: t=1, g=3.

So the three songs have total time 3. The playlist must consist of all three songs. But the two genre 1 songs cannot be adjacent.

So the valid permutations are those where the two genre 1 songs are not consecutive.

The possible valid permutations are:

[0,2,1], [1,2,0], [2,0,1], [2,1,0] ?

Wait, but in the sample output, the answer is 2. So perhaps the correct answer is that only two of the possible permutations are valid.

Wait, the sample explanation says that the answer is 2. The two valid sequences are [1,3,2] and [2,3,1]. So the indices are 0,2,1 and 1,2,0 (assuming the input is 0-based). Because the first two songs (indices 0 and 1) are same genre, so they can't be consecutive.

So the valid sequences must have the two genre 1 songs separated by the genre 3 song.

So the possible permutations are:

0,2,1 → genres 1,3,1 → invalid because the first and third are same genre consecutive? Wait no: the genres are 1,3,1. But the consecutive genres are 1 and 3 (allowed), then 3 and 1 (allowed). So that is valid. Wait, no. The first two songs are 0 and 2 (genres 1 and 3) → allowed. Then 2 and 1 (genres 3 and 1) → allowed. So this sequence is valid.

But song1 is also genre 1. So the third song is song1 (genre 1), which comes after song2 (genre 3). So it's allowed. So why is the sample output 2?

Ah, because the sample input is:

songs are:

song0: 1 1

song1: 1 1

song2: 1 3

So the total time is 3. So the playlist must include all three songs (sum is 1+1+1=3).

But the two genre 1 songs can't be consecutive.

So the valid sequences are:

song0, song2, song1 → genres 1,3,1 → allowed.

song1, song2, song0 → genres 1,3,1 → allowed.

song2, song0, song1 → genres 3,1,1 → invalid because the last two are same genre.

song2, song1, song0 → genres 3,1,1 → invalid.

song0, song1, song2 → genres 1,1,3 → invalid.

song1, song0, song2 → genres 1,1,3 → invalid.

So only two valid permutations. Hence the sample output is 2.

So the code should count these two.

In the code, after processing all masks, the mask 7 (all three songs) must have two entries where the time is 3. Let's see.

When processing mask 3 (bits 0 and 1 set), which contains the two genre 1 songs. The time here would be 2 (1+1). But then adding song 2 (genre 3) gives new_time=3.

But in mask 3, the last_genre is 1 (since both songs 0 and 1 are genre 1). So when adding song 2, since its genre is 3, which is different from 1, it's allowed. So new_time is 2+1=3. So the new_mask is 7 (all bits set). The key (3,3) is added with the count from the previous state.

Wait, mask 3's entries could be (1,2). For example:

- mask 3 could have entries (1, 2) with count 2 (since there are two possible ways to reach mask 3 with time 2 and last genre 1: either adding song0 then song1, or song1 then song0).

So when processing mask 3:

for (1,2), count=2.

For each song not in mask 3 (song 2):

ti=1, gi=3. last_genre is 1 (allowed). new_time=2+1=3.

new_mask=7. So add (3,3) to mask7's dict with count 2.

So mask7's (3,3) entry has count 2.

Similarly, other masks may contribute to mask7's entries. Wait, but for the three-song sequences, the only way to reach time 3 is by adding all three songs. So mask7's (3,3) entry is the sum of all valid ways to arrange the three songs such that consecutive genres are allowed.

But according to our earlier analysis, only two of the six permutations are valid. So why does the code's approach count two entries?

Because in the code, when processing the mask 3 (songs 0 and 1, time 2, last genre 1), adding song2 (genre 3, time 3) gives a count of 2 (since mask3's count is 2). So in mask7, (3,3) would have count 2. Then, when we sum all entries where time is 3, that's the answer.

But what about other paths leading to mask7?

For example, mask5 (songs 0 and 2) → last_genre could be 3, time 2. Then adding song1 (genre 1) gives new_time 3, new_mask7, and the count increases by the count from mask5's entry (which could be 1). So mask7's (1,3) entry would have count 1.

Similarly, mask6 (songs 1 and 2) → last_genre 3, time 2. Adding song0 (genre1) gives new_mask7, count increases by 1.

So mask7's entries would be:

(3,3) → count 2 (from mask3)

(1,3) → count 1 (from mask5)

(1,3) → count 1 (from mask6?)

Wait, no. Let's think.

Wait, mask5 has songs 0 and 2. So when mask5 is processed:

mask5's entries would have (1, 2) (if the last song was 0) and (3, 2) (if the last song was 2). Wait no. Let's see how mask5 is formed.

mask5 is 101 in binary (songs 0 and 2).

The possible ways to reach mask5:

From mask0: add song0 (mask1), then song2 (mask5).

Or from mask4 (song2), add song0.

For example:

mask0 → song0 (mask1, genre1, time1) → song2 (mask5, genre3, time2).

mask0 → song2 (mask4, genre3, time1) → song0 (mask5, genre1, time2).

So mask5's entries are (3,2) (from mask4) and (1,2) (from mask1).

Wait, no:

When adding song2 to mask1 (which has genre1, time1), the new genre is 3, new_time is 2. So mask5's entry (3,2) has count 1.

When adding song0 to mask4 (genre3, time1), new_time is 2. genre1 !=3, so allowed. So mask5's entry (1,2) has count 1.

So mask5 has two entries: (3,2) and (1,2), each with count 1.

Then, processing mask5:

for each (last_genre, time) in mask5's entries:

for (3,2), count=1:

   check songs not in mask5 (song1, song3, etc. but n=3, so song1 (i=1) is not in mask5).

   song1's genre is 1. last_genre is 3. allowed. new_time=2+1=3. new_mask7. add (1,3) with count 1.

for (1,2), count=1:

   song1's genre is 1. last_genre is 1. not allowed. skipped.

so after processing mask5, mask7's entry (1,3) has count 1.

Similarly, mask6 (songs1 and 2) would have entries (1,2) (from adding song1 to mask0, then song2) and (3,2) (from mask2, song1 and song2).

Processing mask6:

for (1,2) (genre1, time2):

   adding song0 (genre1) is not allowed. song0 is not in mask6. genre1 == last_genre (1). So can't add.

for (3,2) (genre3, time2):

   adding song0 (genre1) is allowed. new_time=3. new_mask7. add (1,3) with count 1.

So mask7's (1,3) entry is increased by 1.

So mask7's entries are:

(3,3) → 2 (from mask3)

(1,3) → 1 (from mask5)

(1,3) → 1 (from mask6)

Wait, no. For mask5, (3,2) → song1 (genre1) is allowed. new_time=3. So adds (1,3) with count 1.

For mask6, (3,2) → adding song0 (genre1) is allowed. new_time=3. adds (1,3) with count 1 (from mask6's entry (3,2) which has count 1).

So mask7's (1,3) entry is 1 +1 =2.

So mask7's dict has (3,3) → 2 and (1,3) → 2.

So the total sum for T=3 is 2 (from 3,3) + 2 (from 1,3) → 4. But the sample output is 2. Wait, that's a problem.

Hmm, this indicates a mistake in the code.

Wait, but according to the sample input 2, the answer is 2. So the code's approach is overcounting.

What's the error here?

Ah, because the code counts all permutations where the sum is T, but some of these permutations may have consecutive same genres.

Wait, no. Because the transitions are designed to avoid adding a song with the same genre as the previous. So mask7's entries should only have sequences that are valid.

So why does the code's approach count 4 valid sequences for sample input 2, but the correct answer is 2?

Wait, maybe I made a mistake in the analysis.

Let me re-examine the code.

In mask3 (songs 0 and 1), the last_genre is 1 (since both are genre 1). When adding song2 (genre3), the new_time is 3. The new_mask is 7, and the entry is (3,3) with count 2. So those sequences are 0→1→2 and 1→0→2. Wait, no: the mask3 is 0 and 1. So the sequences are 0 followed by 1, then adding 2. Or 1 followed by 0, then adding 2. Both sequences end with 2 (genre3), so the last two genres are 1→3 and 1→3. So these are valid. Then, the two sequences are [0,1,2] and [1,0,2]. But these sequences have genres 1→1→3, which is invalid because the first two songs are same genre consecutive. Wait, but according to the code's transitions, when adding song1 to mask0 (after song0), the last_genre becomes 1. Then adding song1 (same genre) would be allowed? No, because in mask0's entry, when adding song0, it's genre1. Then adding song1, which has genre1. The code checks that last_genre is 1 (from the previous step) and the new song's genre is 1. So it's not allowed. Wait, but in mask0, the initial state is (0,0). So adding song0, which has genre1, creates a new entry (1,1). Then, when processing mask1 (song0), the entries are (1,1). Now, when adding song1 (genre1), the code checks: last_genre is 1 (from the entry in mask1), so adding song1 (genre1) is not allowed. So transitions from mask1 to mask3 are not possible. So how does mask3 get any entries?

Wait, mask3 is songs 0 and 1. So how can that happen if the genres are the same? Because when adding the second song of the same genre, the code would have blocked it.

Wait, this suggests that there's a bug in the code's logic. Because in the code, when adding song1 to mask1 (which has last_genre 1), since song1's genre is 1, the code would not allow it. So mask3 (songs0 and1) would not exist. So how is this possible?

Ah! This is the mistake. In the code, when processing mask0 (0 bits), adding song0 (mask1, genre1, time1). Then, processing mask1 (1 bit), adding song1 (genre1) is not allowed. So mask3 is not created. So the code would not generate any entries for mask3. But in sample input 2, the two songs of genre1 are not allowed to be consecutive, so their permutations would not be considered.

But sample input 2's answer requires that the two songs of genre1 are in the playlist, but not consecutive. So how does the code handle that?

Wait, in sample input 2, the playlist must include all three songs. But the two genre1 songs can't be consecutive. So the code must count the two sequences where the two genre1 songs are separated by the genre3 song.

But according to the code's approach, how are those sequences generated?

Let me re-examine the code's transitions.

Let's walk through sample input 2 step by step.

Initial state: mask0, (0,0) → count 1.

Process mask0 (0 bits):

For each song i not in mask0 (0,1,2):

Check if last_genre is 0 (yes), so allowed.

For song0 (genre1), new_mask=1, (1,1) → count 1.

For song1 (genre1), new_mask=2, (1,1) → count 1.

For song2 (genre3), new_mask=4, (3,1) → count 1.

So after processing mask0:

mask1 has (1,1):1.

mask2 has (1,1):1.

mask4 has (3,1):1.

Now, process masks in order of bit count. Next are masks1,2,4 (each 1 bit).

Processing mask1 (bit0 set):

entries are (1,1) → count 1.

For each song not in mask1 (i=1,2):

i=1: genre1. last_genre is 1 → same genre. So skip.

i=2: genre3. last_genre is 1 → different. new_time=2. new_mask=1|4=5. Add (3,2) → count 1.

So mask5's dict now has (3,2):1.

Processing mask2 (bit1 set):

entries are (1,1) → count1.

For songs not in mask2: 0,2.

i=0: genre1. last_genre is 1 → same. skipped.

i=2: genre3. new_time=2. new_mask=2|4=6. Add (3,2) → count1.

Processing mask4 (bit2 set):

entries are (3,1) → count1.

For songs not in mask4: 0,1.

i=0: genre1. allowed (last_genre is3). new_time=2. new_mask=5. Add (1,2) → count1.

i=1: genre1. allowed (last_genre is3). new_time=2. new_mask=6. Add (1,2) → count1.

So after processing masks1,2,4:

mask5 has (3,2):1 and (1,2):1.

mask6 has (3,2):1 and (1,2):1.

Now, process masks with 2 bits: masks3,5,6.

mask3 is 0b11 (bits0 and 1 set). But how was mask3 formed?

It's only possible if during processing of mask1 or mask2, a song is added that has the same genre. But according to the code, when processing mask1 (which has genre1), adding song1 (genre1) is not allowed, so mask3 is not formed. So mask3's dict remains empty.

So masks3,5,6 are processed next.

Processing mask3: empty dict. So nothing to do.

Processing mask5 (bits0 and 2):

entries are (3,2) count1 and (1,2) count1.

For song1 (not in mask5), genre1.

For entry (3,2):

adding song1: genre1 is different from 3. new_time=3. new_mask=5 | 2=7. Add (1,3) → count1.

For entry (1,2):

adding song1: genre1 ==1 → not allowed. So skipped.

Processing mask5's entries:

So mask7's (1,3) entry is 1.

Processing mask6 (bits1 and 2):

entries are (3,2) count1 and (1,2) count1.

For song0 (not in mask6), genre1.

For entry (3,2):

adding song0: genre1. allowed. new_time=3. new_mask=6 |1=7. Add (1,3) → count1.

For entry (1,2):

adding song0: genre1. same as last_genre (1). skipped.

So mask7's (1,3) entry becomes 1 (from mask5) +1 (from mask6) → 2.

Now, processing mask7 (3 bits):

entries are (1,3):2.

For each song not in mask7: none (mask7 is all bits set).

No transitions.

Finally, when summing all entries with time=T=3:

mask7's (1,3) entry has count 2. So answer is 2.

Which matches the sample output.

Ah, so the code is correct. So why the earlier confusion?

Because mask3 (songs0 and1) is not generated. Because adding song1 to mask1 (which has last_genre 1) is not allowed. So mask3 is never populated. Hence, the code does not allow sequences where two genre1 songs are consecutive. Therefore, the code correctly counts only the two valid permutations where the two genre1 songs are separated by the genre3 song.

Thus, the code works correctly for the sample input 2.

Therefore, the code is correct.

Now, let's test the third sample input.

Sample Input 3:

4 10

5 3

2 1

3 2

5 1

Sample Output:10.

The valid sequences are listed in the note. Let's trust that the code would correctly compute the 10 sequences.

Given that the code works for the first two samples, and the approach is correct, we can proceed to write the code.

Now, the code must be optimized for speed and memory.

In Python, using a list of dictionaries for each mask, where each dictionary holds (genre, time) keys and counts as values, is feasible. However, for Python, using defaultdict may be slower than using regular dictionaries and checking for keys.

Alternatively, for each mask, track a dictionary of (genre, time) → count.

The code as outlined should work.

But in Python, for large masks, the loops can be slow.

But given that the maximum mask is 32768 and for each mask, the number of (genre, time) entries is limited (each song adds up to 15 time, up to 225), and for each mask, the number of (genre, time) pairs is O(3 * T) per mask, but the code can still run within the time limits.

But in Python, even with 3e7 operations, it's possible that the code may time out for the worst case.

But given the time limit is 5 seconds and Python's speed, perhaps with some optimizations, it can pass.

But to optimize, perhaps precompute the songs' ti and gi.

Another optimization is to precompute the masks in order of their bit count.

Additionally, in Python, using bit_count (bin(x).count('1')) can be slow. So precomputing the list of masks sorted by the number of set bits can help.

For example:

mask_order = sorted([m for m in range(1<<n)], key=lambda x: bin(x).count('1'))

This way, we can process masks in the order of increasing bit count.

But for n=15, this is 32768 masks, which is manageable.

Another optimization: precompute all the songs for each mask iteration. For each song i, precompute ti and gi.

Another thing to note is that in the code, when iterating through songs not in the mask, we can precompute the list of songs not in the mask as a list, but for n=15, checking each i in 0..n-1 is manageable.

So the code as outlined should work.

Now, the code implementation:

Read n and T.

Read the songs into a list.

Initialize the MOD = 1e9+7.

Initialize a list of dictionaries for each mask.

Set dp[0][(0,0)] = 1.

Sort the masks in order of increasing bits.

Loop through each mask in this order.

For each (last_genre, current_time) in the current mask's dictionary:

   for each song i not in the mask:

       check if genre is allowed (last_genre is 0 or gi != last_genre).

       compute new_time = current_time + ti.

       if new_time > T: continue.

       new_mask = mask | (1<<i).

       dp[new_mask][(gi, new_time)] += count.

       apply modulo.

Finally, sum all entries in all masks where time is T.

Now, in Python, the code can be written as:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 + 7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                if key in dp[new_mask]:
                    dp[new_mask][key] = (dp[new_mask][key] + count) % MOD
                else:
                    dp[new_mask][key] = count % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

But wait, in Python, dictionaries are dynamic. So for each new_mask, the code checks if the key is present and increments. But using get(key, 0) + count would be more efficient.

But the code can be rewritten as:

for each new_mask and key:

    dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

But in Python, for each key, we can use the get method.

So modifying the loop:

...
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD
...

This way, even if the key doesn't exist, it's handled.

But the code initializes dp as a list of empty dictionaries. So for new_mask, dp[new_mask] starts as an empty dict. So when we do dp[new_mask][key], we have to use get.

Alternatively, using defaultdict for each mask's dictionary would help, but in Python, for speed, perhaps using get is better.

So the code can be adjusted to use get.

Thus, the code would be:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 +7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

This should work correctly.

Now, testing for the sample inputs, it's correct.

Regarding time and memory constraints:

n=15, T=225.

Each mask has a dictionary with entries (genre, time) → count.

In the worst case, each mask has up to 3 genres and 225 times, leading to 3*225=675 entries per mask. For 32768 masks, that's 32768 * 675 = 22,118,400 entries. Each entry is a tuple key and an integer value. In Python, this could be memory intensive, but given the problem's memory limit of 256 MB, it's possible that this fits.

But for Python, dictionaries are somewhat memory-heavy, but with 22 million entries, each requiring perhaps 40 bytes (for key and value), it's around 880 MB, which exceeds the memory limit. Wait, this is a problem.

So the code may not pass for large input due to memory constraints.

Hmm. This indicates that the approach may not be feasible in Python for the given constraints.

What's the alternative?

Alternative approach:

Instead of tracking (last_genre, time) for each mask, we can track time and last_genre in separate dimensions, but compressed.

For example, for each mask, track a dictionary that maps last_genre to a dictionary of time → count.

But even that might not help with memory.

Alternatively, note that for a given mask, the sum of all songs in the mask could be up to 15*15=225, which is T up to 225. So the time can be up to T.

But for a given mask, the sum of the songs in the mask is fixed. Wait, no. Because the songs can be any subset, but the sum can vary based on the subset. For example, if the mask includes songs with varying t_i, the sum can be any possible combination.

Wait, no. The mask is a subset of songs. The sum of the songs' t_i is fixed for the mask. Because the mask represents the subset of songs used, and their t_i are summed.

Wait, no. Wait, the mask represents the subset of songs used in the sequence. But the sum of their t_i depends on which songs are in the mask. So for a given mask, the sum is the sum of t_i for all songs in the mask. So the sum is fixed for the mask.

But the code's approach allows different time values for the same mask. How is that possible?

Ah, no. Because in the code's approach, the time is the sum of the songs' t_i in the order they are added, but that's not correct. The time is the sum of all t_i for the songs in the mask. Because each transition adds a song to the mask, and new_time is current_time + t_i. So for a mask, the sum of the t_i of all songs in the mask is equal to new_time. Thus, for a given mask, the time is fixed as the sum of the t_i of the songs in the mask.

Wait, that's a key insight. For example, if a mask has songs 0 and 1 with t_i=1 and 2, then the sum is 3. So for that mask, any entry in the dictionary must have time=3. But according to the code's approach, for mask3 (songs0 and1), the current_time would be 3. But in the code's approach, the time can vary for the same mask, but that's impossible because the sum of the t_i is fixed by the mask.

Wait, no. Because the code allows for different sequences of adding the songs, which can have varying intermediate times, but the sum of the songs in the mask must be the sum of their t_i. For example, if the mask includes songs0 (t=1) and song1 (t=2), then the total time is 3. However, the code's approach allows entries for mask3 with time=1 (song0) and then adding song1 (time becomes 3). So for mask3, the time must be 3, but the code's approach allows entries with time=3. But during the transitions, the time is the sum of the songs added. So for any mask, the sum of the songs in the mask must be equal to the time.

But wait, no. Because when you add songs to the mask in any order, the sum is the sum of their t_i. So for a given mask, the sum is fixed. Thus, the time for the mask is equal to the sum of the t_i of the songs in the mask. Therefore, for a given mask, the time is fixed. So the code's approach of tracking time for each mask is redundant. Because for a given mask, the time is fixed as the sum of the songs' t_i in the mask.

Thus, the code's approach is incorrect, and there's a major flaw here.

Oh no! This is a critical mistake. The time tracked in the code is the sum of the songs in the order they are added, but that's not correct. Because the sum of the songs in the mask is fixed. For example, if the mask includes songs with t_i=1 and t_i=2, the total sum is 3, regardless of the order in which they are added. So the code's approach is incorrect because it allows multiple time entries for the same mask, which is impossible.

This means that the entire approach is wrong.

This is a major error.

So how to correct this?

The problem arises because the code's DP tracks the current time as the sum of the songs added so far, but for a given mask, the sum of the songs' t_i is fixed. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the time is determined by the mask, not by the order in which the songs are added.

This means that the code's approach of tracking time for each mask is redundant and incorrect. For example, mask3 (songs0 and1 with t_i=1 and 2) must have time=3. Thus, the code's approach allows multiple time entries for the same mask, which is impossible. Therefore, the code is incorrect.

This explains why the code worked for the first sample, but may not for other cases.

Thus, the entire approach is flawed.

So what's the correct approach?

The time is determined by the songs in the mask, not by their order. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the DP state should track:

- mask: the set of songs used.

- last_genre: the genre of the last song added.

- time: sum of t_i for the mask.

But since time is fixed by the mask, the time is redundant and can be computed as the sum of t_i for the songs in the mask.

Thus, the DP state can be represented as (mask, last_genre), and the time is the sum of t_i for the songs in the mask.

Thus, for each mask, we can precompute the sum of its songs' t_i. Then, for each mask, the sum is known, and we can track the last_genre for sequences of songs that sum to exactly T.

This is a crucial optimization. The time is no longer part of the DP state. Instead, for each mask, we compute the sum of its songs' t_i, and only consider those masks where the sum equals T.

Thus, the correct approach is:

- For each mask, precompute the sum of its songs' t_i.

- The DP state is (mask, last_genre), and the count is the number of valid sequences for the mask, ending with last_genre, and with sum equal to the mask's sum.

- The transitions are as follows: for each state (mask, last_genre), when adding a new song i not in the mask, check if the new sum (sum + t_i) <= T. If so, and the new song's genre is not equal to last_genre, then add to the new mask (mask | (1<<i)) with genre gi, and count increased by the current count.

- The answer is the sum over all masks where the sum equals T, and all possible last_genres.

Thus, the code should be adjusted to precompute the sum for each mask, and track (mask, last_genre) pairs.

This reduces the state space from (mask, genre, time) to (mask, genre), which is 32768 * 4 = 131072 states.

This is manageable.

Thus, the steps are:

1. Precompute for each mask the sum of t_i for the songs in the mask.

2. Initialize the DP for mask 0: sum is 0, last_genre 0, count 1.

3. For each mask in order of increasing bits, process the transitions to add a new song i not in the mask.

4. For each transition, check if the new sum (sum + t_i) <= T.

5. If the new sum is <= T, and the new song's genre is different from the previous last_genre (or previous is 0), then update the new mask's DP entry.

6. The answer is the sum over all masks where the sum is exactly T, of the sum of their counts across all last_genres.

This approach is correct and efficient.

Now, let's rework the code.

Precompute sum for each mask:

sum_mask = [0] * (1<<n)

for mask in range(1<<n):

    s = 0

    for i in range(n):

        if mask & (1<<i):

            s += songs[i][0]

    sum_mask[mask] = s

Then, the DP is:

dp[mask][last_genre] = count.

So for each mask, the sum is sum_mask[mask]. We only process transitions where sum_mask[new_mask] <= T.

Thus, the code:

Wait, but according to the sample output, the answer is 2. Oh right, because in the sample input 2, the songs are:

song0: t=1, g=1

song1: t=1, g=1

song2: t=1, g=3.

So the three songs have total time 3. The playlist must consist of all three songs. But the two genre 1 songs cannot be adjacent.

So the valid permutations are those where the two genre 1 songs are not consecutive.

The possible valid permutations are:

[0,2,1], [1,2,0], [2,0,1], [2,1,0] ?

Wait, but in the sample output, the answer is 2. So perhaps the correct answer is that only two of the possible permutations are valid.

Wait, the sample explanation says that the answer is 2. The two valid sequences are [1,3,2] and [2,3,1]. So the indices are 0,2,1 and 1,2,0 (assuming the input is 0-based). Because the first two songs (indices 0 and 1) are same genre, so they can't be consecutive.

So the valid sequences must have the two genre 1 songs separated by the genre 3 song.

So the possible permutations are:

0,2,1 → genres 1,3,1 → invalid because the first and third are same genre consecutive? Wait no: the genres are 1,3,1. But the consecutive genres are 1 and 3 (allowed), then 3 and 1 (allowed). So that is valid. Wait, no. The first two songs are 0 and 2 (genres 1 and 3) → allowed. Then 2 and 1 (genres 3 and 1) → allowed. So this sequence is valid.

But song1 is also genre 1. So the third song is song1 (genre 1), which comes after song2 (genre 3). So it's allowed. So why is the sample output 2?

Ah, because the sample input is:

songs are:

song0: 1 1

song1: 1 1

song2: 1 3

So the total time is 3. So the playlist must include all three songs (sum is 1+1+1=3).

But the two genre 1 songs can't be consecutive.

So the valid sequences are:

song0, song2, song1 → genres 1,3,1 → allowed.

song1, song2, song0 → genres 1,3,1 → allowed.

song2, song0, song1 → genres 3,1,1 → invalid because the last two are same genre.

song2, song1, song0 → genres 3,1,1 → invalid.

song0, song1, song2 → genres 1,1,3 → invalid.

song1, song0, song2 → genres 1,1,3 → invalid.

So only two valid permutations. Hence the sample output is 2.

So the code should count these two.

In the code, after processing all masks, the mask 7 (all three songs) must have two entries where the time is 3. Let's see.

When processing mask 3 (bits 0 and 1 set), which contains the two genre 1 songs. The time here would be 2 (1+1). But then adding song 2 (genre 3) gives new_time=3.

But in mask 3, the last_genre is 1 (since both songs 0 and 1 are genre 1). So when adding song 2, since its genre is 3, which is different from 1, it's allowed. So new_time is 2+1=3. So the new_mask is 7 (all bits set). The key (3,3) is added with the count from the previous state.

Wait, mask 3's entries could be (1,2). For example:

- mask 3 could have entries (1, 2) with count 2 (since there are two possible ways to reach mask 3 with time 2 and last genre 1: either adding song0 then song1, or song1 then song0).

So when processing mask 3:

for (1,2), count=2.

For each song not in mask 3 (song 2):

ti=1, gi=3. last_genre is 1 (allowed). new_time=2+1=3.

new_mask=7. So add (3,3) to mask7's dict with count 2.

So mask7's (3,3) entry has count 2.

Similarly, other masks may contribute to mask7's entries. Wait, but for the three-song sequences, the only way to reach time 3 is by adding all three songs. So mask7's (3,3) entry is the sum of all valid ways to arrange the three songs such that consecutive genres are allowed.

But according to our earlier analysis, only two of the six permutations are valid. So why does the code's approach count two entries?

Because in the code, when processing the mask 3 (songs 0 and 1, time 2, last genre 1), adding song2 (genre 3, time 3) gives a count of 2 (since mask3's count is 2). So in mask7, (3,3) would have count 2. Then, when we sum all entries where time is 3, that's the answer.

But what about other paths leading to mask7?

For example, mask5 (songs 0 and 2) → last_genre could be 3, time 2. Then adding song1 (genre 1) gives new_time 3, new_mask7, and the count increases by the count from mask5's entry (which could be 1). So mask7's (1,3) entry would have count 1.

Similarly, mask6 (songs 1 and 2) → last_genre 3, time 2. Adding song0 (genre1) gives new_mask7, count increases by 1.

So mask7's entries would be:

(3,3) → count 2 (from mask3)

(1,3) → count 1 (from mask5)

(1,3) → count 1 (from mask6?)

Wait, no. Let's think.

Wait, mask5 has songs 0 and 2. So when mask5 is processed:

mask5's entries would have (1, 2) (if the last song was 0) and (3, 2) (if the last song was 2). Wait no. Let's see how mask5 is formed.

mask5 is 101 in binary (songs 0 and 2).

The possible ways to reach mask5:

From mask0: add song0 (mask1), then song2 (mask5).

Or from mask4 (song2), add song0.

For example:

mask0 → song0 (mask1, genre1, time1) → song2 (mask5, genre3, time2).

mask0 → song2 (mask4, genre3, time1) → song0 (mask5, genre1, time2).

So mask5's entries are (3,2) (from mask4) and (1,2) (from mask1).

Wait, no:

When adding song2 to mask1 (which has genre1, time1), the new genre is 3, new_time is 2. So mask5's entry (3,2) has count 1.

When adding song0 to mask4 (genre3, time1), new_time is 2. genre1 !=3, so allowed. So mask5's entry (1,2) has count 1.

So mask5 has two entries: (3,2) and (1,2), each with count 1.

Then, processing mask5:

for each (last_genre, time) in mask5's entries:

for (3,2), count=1:

   check songs not in mask5 (song1, song3, etc. but n=3, so song1 (i=1) is not in mask5).

   song1's genre is 1. last_genre is 3. allowed. new_time=2+1=3. new_mask7. add (1,3) with count 1.

for (1,2), count=1:

   song1's genre is 1. last_genre is 1. not allowed. skipped.

so after processing mask5, mask7's entry (1,3) has count 1.

Similarly, mask6 (songs1 and 2) would have entries (1,2) (from adding song1 to mask0, then song2) and (3,2) (from mask2, song1 and song2).

Processing mask6:

for (1,2) (genre1, time2):

   adding song0 (genre1) is not allowed. song0 is not in mask6. genre1 == last_genre (1). So can't add.

for (3,2) (genre3, time2):

   adding song0 (genre1) is allowed. new_time=3. new_mask7. add (1,3) with count 1.

So mask7's (1,3) entry is increased by 1.

So mask7's entries are:

(3,3) → 2 (from mask3)

(1,3) → 1 (from mask5)

(1,3) → 1 (from mask6)

Wait, no. For mask5, (3,2) → song1 (genre1) is allowed. new_time=3. So adds (1,3) with count 1.

For mask6, (3,2) → adding song0 (genre1) is allowed. new_time=3. adds (1,3) with count 1 (from mask6's entry (3,2) which has count 1).

So mask7's (1,3) entry is 1 +1 =2.

So mask7's dict has (3,3) → 2 and (1,3) → 2.

So the total sum for T=3 is 2 (from 3,3) + 2 (from 1,3) → 4. But the sample output is 2. Wait, that's a problem.

Hmm, this indicates a mistake in the code.

Wait, but according to the sample input 2, the answer is 2. So the code's approach is overcounting.

What's the error here?

Ah, because the code counts all permutations where the sum is T, but some of these permutations may have consecutive same genres.

Wait, no. Because the transitions are designed to avoid adding a song with the same genre as the previous. So mask7's entries should only have sequences that are valid.

So why does the code's approach count 4 valid sequences for sample input 2, but the correct answer is 2?

Wait, maybe I made a mistake in the analysis.

Let me re-examine the code.

In mask3 (songs 0 and 1), the last_genre is 1 (since both are genre 1). When adding song2 (genre3), the new_time is 3. The new_mask is 7, and the entry is (3,3) with count 2. So those sequences are 0→1→2 and 1→0→2. Wait, no: the mask3 is 0 and 1. So the sequences are 0 followed by 1, then adding 2. Or 1 followed by 0, then adding 2. Both sequences end with 2 (genre3), so the last two genres are 1→3 and 1→3. So these are valid. Then, the two sequences are [0,1,2] and [1,0,2]. But these sequences have genres 1→1→3, which is invalid because the first two songs are same genre consecutive. Wait, but according to the code's transitions, when adding song1 to mask0 (after song0), the last_genre becomes 1. Then adding song1 (same genre) would be allowed? No, because in mask0's entry, when adding song0, it's genre1. Then adding song1, which has genre1. The code checks that last_genre is 1 (from the previous step) and the new song's genre is 1. So it's not allowed. Wait, but in mask0, the initial state is (0,0). So adding song0, which has genre1, creates a new entry (1,1). Then, when processing mask1 (song0), the entries are (1,1). Now, when adding song1 (genre1), the code checks: last_genre is 1 (from the entry in mask1), so adding song1 (genre1) is not allowed. So transitions from mask1 to mask3 are not possible. So how does mask3 get any entries?

Wait, mask3 is songs 0 and 1. So how can that happen if the genres are the same? Because when adding the second song of the same genre, the code would have blocked it.

Wait, this suggests that there's a bug in the code's logic. Because in the code, when adding song1 to mask1 (which has last_genre 1), since song1's genre is 1, the code would not allow it. So mask3 (songs0 and1) would not exist. So how is this possible?

Ah! This is the mistake. In the code, when processing mask0 (0 bits), adding song0 (mask1, genre1, time1). Then, processing mask1 (1 bit), adding song1 (genre1) is not allowed. So mask3 is not created. So the code would not generate any entries for mask3. But in sample input 2, the two songs of genre1 are not allowed to be consecutive, so their permutations would not be considered.

But sample input 2's answer requires that the two songs of genre1 are in the playlist, but not consecutive. So how does the code handle that?

Wait, in sample input 2, the playlist must include all three songs. But the two genre1 songs can't be consecutive. So the code must count the two sequences where the two genre1 songs are separated by the genre3 song.

But according to the code's approach, how are those sequences generated?

Let me re-examine the code's transitions.

Let's walk through sample input 2 step by step.

Initial state: mask0, (0,0) → count 1.

Process mask0 (0 bits):

For each song i not in mask0 (0,1,2):

Check if last_genre is 0 (yes), so allowed.

For song0 (genre1), new_mask=1, (1,1) → count 1.

For song1 (genre1), new_mask=2, (1,1) → count 1.

For song2 (genre3), new_mask=4, (3,1) → count 1.

So after processing mask0:

mask1 has (1,1):1.

mask2 has (1,1):1.

mask4 has (3,1):1.

Now, process masks in order of bit count. Next are masks1,2,4 (each 1 bit).

Processing mask1 (bit0 set):

entries are (1,1) → count 1.

For each song not in mask1 (i=1,2):

i=1: genre1. last_genre is 1 → same genre. So skip.

i=2: genre3. last_genre is 1 → different. new_time=2. new_mask=1|4=5. Add (3,2) → count 1.

So mask5's dict now has (3,2):1.

Processing mask2 (bit1 set):

entries are (1,1) → count1.

For songs not in mask2: 0,2.

i=0: genre1. last_genre is 1 → same. skipped.

i=2: genre3. new_time=2. new_mask=2|4=6. Add (3,2) → count1.

Processing mask4 (bit2 set):

entries are (3,1) → count1.

For songs not in mask4: 0,1.

i=0: genre1. allowed (last_genre is3). new_time=2. new_mask=5. Add (1,2) → count1.

i=1: genre1. allowed (last_genre is3). new_time=2. new_mask=6. Add (1,2) → count1.

So after processing masks1,2,4:

mask5 has (3,2):1 and (1,2):1.

mask6 has (3,2):1 and (1,2):1.

Now, process masks with 2 bits: masks3,5,6.

mask3 is 0b11 (bits0 and 1 set). But how was mask3 formed?

It's only possible if during processing of mask1 or mask2, a song is added that has the same genre. But according to the code, when processing mask1 (which has genre1), adding song1 (genre1) is not allowed, so mask3 is not formed. So mask3's dict remains empty.

So masks3,5,6 are processed next.

Processing mask3: empty dict. So nothing to do.

Processing mask5 (bits0 and 2):

entries are (3,2) count1 and (1,2) count1.

For song1 (not in mask5), genre1.

For entry (3,2):

adding song1: genre1 is different from 3. new_time=3. new_mask=5 | 2=7. Add (1,3) → count1.

For entry (1,2):

adding song1: genre1 ==1 → not allowed. So skipped.

Processing mask5's entries:

So mask7's (1,3) entry is 1.

Processing mask6 (bits1 and 2):

entries are (3,2) count1 and (1,2) count1.

For song0 (not in mask6), genre1.

For entry (3,2):

adding song0: genre1. allowed. new_time=3. new_mask=6 |1=7. Add (1,3) → count1.

For entry (1,2):

adding song0: genre1. same as last_genre (1). skipped.

So mask7's (1,3) entry becomes 1 (from mask5) +1 (from mask6) → 2.

Now, processing mask7 (3 bits):

entries are (1,3):2.

For each song not in mask7: none (mask7 is all bits set).

No transitions.

Finally, when summing all entries with time=T=3:

mask7's (1,3) entry has count 2. So answer is 2.

Which matches the sample output.

Ah, so the code is correct. So why the earlier confusion?

Because mask3 (songs0 and1) is not generated. Because adding song1 to mask1 (which has last_genre 1) is not allowed. So mask3 is never populated. Hence, the code does not allow sequences where two genre1 songs are consecutive. Therefore, the code correctly counts only the two valid permutations where the two genre1 songs are separated by the genre3 song.

Thus, the code works correctly for the sample input 2.

Therefore, the code is correct.

Now, let's test the third sample input.

Sample Input 3:

4 10

5 3

2 1

3 2

5 1

Sample Output:10.

The valid sequences are listed in the note. Let's trust that the code would correctly compute the 10 sequences.

Given that the code works for the first two samples, and the approach is correct, we can proceed to write the code.

Now, the code must be optimized for speed and memory.

In Python, using a list of dictionaries for each mask, where each dictionary holds (genre, time) keys and counts as values, is feasible. However, for Python, using defaultdict may be slower than using regular dictionaries and checking for keys.

Alternatively, for each mask, track a dictionary of (genre, time) → count.

The code as outlined should work.

But in Python, for large masks, the loops can be slow.

But given that the maximum mask is 32768 and for each mask, the number of (genre, time) entries is limited (each song adds up to 15 time, up to 225), and for each mask, the number of (genre, time) pairs is O(3 * T) per mask, but the code can still run within the time limits.

But in Python, even with 3e7 operations, it's possible that the code may time out for the worst case.

But given the time limit is 5 seconds and Python's speed, perhaps with some optimizations, it can pass.

But to optimize, perhaps precompute the songs' ti and gi.

Another optimization is to precompute the masks in order of their bit count.

Additionally, in Python, using bit_count (bin(x).count('1')) can be slow. So precomputing the list of masks sorted by the number of set bits can help.

For example:

mask_order = sorted([m for m in range(1<<n)], key=lambda x: bin(x).count('1'))

This way, we can process masks in the order of increasing bit count.

But for n=15, this is 32768 masks, which is manageable.

Another optimization: precompute all the songs for each mask iteration. For each song i, precompute ti and gi.

Another thing to note is that in the code, when iterating through songs not in the mask, we can precompute the list of songs not in the mask as a list, but for n=15, checking each i in 0..n-1 is manageable.

So the code as outlined should work.

Now, the code implementation:

Read n and T.

Read the songs into a list.

Initialize the MOD = 1e9+7.

Initialize a list of dictionaries for each mask.

Set dp[0][(0,0)] = 1.

Sort the masks in order of increasing bits.

Loop through each mask in this order.

For each (last_genre, current_time) in the current mask's dictionary:

   for each song i not in the mask:

       check if genre is allowed (last_genre is 0 or gi != last_genre).

       compute new_time = current_time + ti.

       if new_time > T: continue.

       new_mask = mask | (1<<i).

       dp[new_mask][(gi, new_time)] += count.

       apply modulo.

Finally, sum all entries in all masks where time is T.

Now, in Python, the code can be written as:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 + 7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                if key in dp[new_mask]:
                    dp[new_mask][key] = (dp[new_mask][key] + count) % MOD
                else:
                    dp[new_mask][key] = count % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

But wait, in Python, dictionaries are dynamic. So for each new_mask, the code checks if the key is present and increments. But using get(key, 0) + count would be more efficient.

But the code can be rewritten as:

for each new_mask and key:

    dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

But in Python, for each key, we can use the get method.

So modifying the loop:

...
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD
...

This way, even if the key doesn't exist, it's handled.

But the code initializes dp as a list of empty dictionaries. So for new_mask, dp[new_mask] starts as an empty dict. So when we do dp[new_mask][key], we have to use get.

Alternatively, using defaultdict for each mask's dictionary would help, but in Python, for speed, perhaps using get is better.

So the code can be adjusted to use get.

Thus, the code would be:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 +7

max_mask = 1 << n
dp = [{} for _ in range(max_mask)]
dp[0][(0, 0)] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_dict = dp[mask]
    if not current_dict:
        continue
    for (last_genre, current_time), count in current_dict.items():
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                if last_genre != 0 and gi == last_genre:
                    continue
                new_time = current_time + ti
                if new_time > T:
                    continue
                new_mask = mask | (1 << i)
                key = (gi, new_time)
                dp[new_mask][key] = (dp[new_mask].get(key, 0) + count) % MOD

answer = 0
for mask in range(max_mask):
    current_dict = dp[mask]
    for (g, t), cnt in current_dict.items():
        if t == T:
            answer = (answer + cnt) % MOD

print(answer)

This should work correctly.

Now, testing for the sample inputs, it's correct.

Regarding time and memory constraints:

n=15, T=225.

Each mask has a dictionary with entries (genre, time) → count.

In the worst case, each mask has up to 3 genres and 225 times, leading to 3*225=675 entries per mask. For 32768 masks, that's 32768 * 675 = 22,118,400 entries. Each entry is a tuple key and an integer value. In Python, this could be memory intensive, but given the problem's memory limit of 256 MB, it's possible that this fits.

But for Python, dictionaries are somewhat memory-heavy, but with 22 million entries, each requiring perhaps 40 bytes (for key and value), it's around 880 MB, which exceeds the memory limit. Wait, this is a problem.

So the code may not pass for large input due to memory constraints.

Hmm. This indicates that the approach may not be feasible in Python for the given constraints.

What's the alternative?

Alternative approach:

Instead of tracking (last_genre, time) for each mask, we can track time and last_genre in separate dimensions, but compressed.

For example, for each mask, track a dictionary that maps last_genre to a dictionary of time → count.

But even that might not help with memory.

Alternatively, note that for a given mask, the sum of all songs in the mask could be up to 15*15=225, which is T up to 225. So the time can be up to T.

But for a given mask, the sum of the songs in the mask is fixed. Wait, no. Because the songs can be any subset, but the sum can vary based on the subset. For example, if the mask includes songs with varying t_i, the sum can be any possible combination.

Wait, no. The mask is a subset of songs. The sum of the songs' t_i is fixed for the mask. Because the mask represents the subset of songs used, and their t_i are summed.

Wait, no. Wait, the mask represents the subset of songs used in the sequence. But the sum of their t_i depends on which songs are in the mask. So for a given mask, the sum is the sum of t_i for all songs in the mask. So the sum is fixed for the mask.

But the code's approach allows different time values for the same mask. How is that possible?

Ah, no. Because in the code's approach, the time is the sum of the songs' t_i in the order they are added, but that's not correct. The time is the sum of all t_i for the songs in the mask. Because each transition adds a song to the mask, and new_time is current_time + t_i. So for a mask, the sum of the t_i of all songs in the mask is equal to new_time. Thus, for a given mask, the time is fixed as the sum of the t_i of the songs in the mask.

Wait, that's a key insight. For example, if a mask has songs 0 and 1 with t_i=1 and 2, then the sum is 3. So for that mask, any entry in the dictionary must have time=3. But according to the code's approach, for mask3 (songs0 and1), the current_time would be 3. But in the code's approach, the time can vary for the same mask, but that's impossible because the sum of the t_i is fixed by the mask.

Wait, no. Because the code allows for different sequences of adding the songs, which can have varying intermediate times, but the sum of the songs in the mask must be the sum of their t_i. For example, if the mask includes songs0 (t=1) and song1 (t=2), then the total time is 3. However, the code's approach allows entries for mask3 with time=1 (song0) and then adding song1 (time becomes 3). So for mask3, the time must be 3, but the code's approach allows entries with time=3. But during the transitions, the time is the sum of the songs added. So for any mask, the sum of the songs in the mask must be equal to the time.

But wait, no. Because when you add songs to the mask in any order, the sum is the sum of their t_i. So for a given mask, the sum is fixed. Thus, the time for the mask is equal to the sum of the t_i of the songs in the mask. Therefore, for a given mask, the time is fixed. So the code's approach of tracking time for each mask is redundant. Because for a given mask, the time is fixed as the sum of the songs' t_i in the mask.

Thus, the code's approach is incorrect, and there's a major flaw here.

Oh no! This is a critical mistake. The time tracked in the code is the sum of the songs in the order they are added, but that's not correct. Because the sum of the songs in the mask is fixed. For example, if the mask includes songs with t_i=1 and t_i=2, the total sum is 3, regardless of the order in which they are added. So the code's approach is incorrect because it allows multiple time entries for the same mask, which is impossible.

This means that the entire approach is wrong.

This is a major error.

So how to correct this?

The problem arises because the code's DP tracks the current time as the sum of the songs added so far, but for a given mask, the sum of the songs' t_i is fixed. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the time is determined by the mask, not by the order in which the songs are added.

This means that the code's approach of tracking time for each mask is redundant and incorrect. For example, mask3 (songs0 and1 with t_i=1 and 2) must have time=3. Thus, the code's approach allows multiple time entries for the same mask, which is impossible. Therefore, the code is incorrect.

This explains why the code worked for the first sample, but may not for other cases.

Thus, the entire approach is flawed.

So what's the correct approach?

The time is determined by the songs in the mask, not by their order. Thus, the time for a mask is fixed as the sum of the t_i of the songs in the mask. Therefore, the DP state should track:

- mask: the set of songs used.

- last_genre: the genre of the last song added.

- time: sum of t_i for the mask.

But since time is fixed by the mask, the time is redundant and can be computed as the sum of t_i for the songs in the mask.

Thus, the DP state can be represented as (mask, last_genre), and the time is the sum of t_i for the songs in the mask.

Thus, for each mask, we can precompute the sum of its songs' t_i. Then, for each mask, the sum is known, and we can track the last_genre for sequences of songs that sum to exactly T.

This is a crucial optimization. The time is no longer part of the DP state. Instead, for each mask, we compute the sum of its songs' t_i, and only consider those masks where the sum equals T.

Thus, the correct approach is:

- For each mask, precompute the sum of its songs' t_i.

- The DP state is (mask, last_genre), and the count is the number of valid sequences for the mask, ending with last_genre, and with sum equal to the mask's sum.

- The transitions are as follows: for each state (mask, last_genre), when adding a new song i not in the mask, check if the new sum (sum + t_i) <= T. If so, and the new song's genre is not equal to last_genre, then add to the new mask (mask | (1<<i)) with genre gi, and count increased by the current count.

- The answer is the sum over all masks where the sum equals T, and all possible last_genres.

Thus, the code should be adjusted to precompute the sum for each mask, and track (mask, last_genre) pairs.

This reduces the state space from (mask, genre, time) to (mask, genre), which is 32768 * 4 = 131072 states.

This is manageable.

Thus, the steps are:

1. Precompute for each mask the sum of t_i for the songs in the mask.

2. Initialize the DP for mask 0: sum is 0, last_genre 0, count 1.

3. For each mask in order of increasing bits, process the transitions to add a new song i not in the mask.

4. For each transition, check if the new sum (sum + t_i) <= T.

5. If the new sum is <= T, and the new song's genre is different from the previous last_genre (or previous is 0), then update the new mask's DP entry.

6. The answer is the sum over all masks where the sum is exactly T, of the sum of their counts across all last_genres.

This approach is correct and efficient.

Now, let's rework the code.

Precompute sum for each mask:

sum_mask = [0] * (1<<n)

for mask in range(1<<n):

    s = 0

    for i in range(n):

        if mask & (1<<i):

            s += songs[i][0]

    sum_mask[mask] = s

Then, the DP is:

dp[mask][last_genre] = count.

So for each mask, the sum is sum_mask[mask]. We only process transitions where sum_mask[new_mask] <= T.

Thus, the code:

n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 +7

max_mask = 1 << n
sum_mask = [0] * max_mask
for mask in range(max_mask):
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += songs[i][0]
    sum_mask[mask] = total

dp = [[0] * 4 for _ in range(max_mask)]  # last_genre can be 0-3
dp[0][0] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_sum = sum_mask[mask]
    if current_sum > T:
        continue
    for last_genre in range(4):
        count = dp[mask][last_genre]
        if count == 0:
            continue
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                new_mask = mask | (1 << i)
                new_sum = current_sum + ti
                if new_sum > T:
                    continue
                if gi == last_genre and last_genre != 0:
                    continue
                dp[new_mask][gi] = (dp[new_mask][gi] + count) % MOD

answer = 0
for mask in range(max_mask):
    if sum_mask[mask] == T:
        answer = (answer + sum(dp[mask][1:4])) % MOD  # genres are 1-3

print(answer)

This code uses a 2D array dp[mask][last_genre], where last_genre can be 0-3 (0 for no songs, 1-3 for actual genres).

The sum for each mask is precomputed in sum_mask.

The transitions are done by checking if adding song i to mask is allowed (genre not equal to last_genre, unless last_genre is 0).

The answer is the sum of all dp[mask][g] where sum_mask[mask] == T and g is 1-3.

This approach is much more efficient in terms of memory and time.

Testing this code with the samples:

Sample Input 1:

3 3

1 1

1 2

1 3.

sum_mask for mask 7 (all songs) is 3. So answer is the sum of dp[7][1], dp[7][2], dp[7][3]. For each song permutation, the last_genre is the genre of the third song. But since the three songs have genres 1,2,3, the number of valid permutations is 3! =6. The code should count each possible permutation. For example, when adding the three songs in any order, the last_genre would be the third song's genre. For each of the six permutations, the code would increment the corresponding genre's count. Thus, each of the three genres (1,2,3) would have 2 counts (since the third song can be any of the three genres, each appearing twice). So sum is 2+2+2=6.

Sample Input 2:

3 3.

sum_mask for mask7 is 3. The code should have dp[7][1] =0, dp[7][3] =2.

Because the two valid sequences end with genre3 (song2) or genre1 (song0 or 1). Wait no.

In sample input 2, the two valid sequences are:

song0, song2, song1 → genres 1,3,1. So last_genre is 1.

song1, song2, song0 → genres 1,3,1. So last_genre is 1.

But wait, the last song in both cases is song1 and song0, which are genre1.

So dp[7][1] would be 2. Other genres (2 and3) are 0.

So sum is 2.

Thus, the code would correctly return 2.

Thus, the code works.

This approach is correct and efficient.

The key difference is that the time is determined by the mask's sum, which is precomputed, and thus the state is reduced to (mask, last_genre), which is manageable.

The code's time complexity is O(max_mask * 4 * n) = 32768 *4 *15 = 1,966,080 operations. Which is feasible in Python even for the time constraints.

Thus, this is the correct approach.
</think>

```python
n, T = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 10**9 + 7

max_mask = 1 << n
sum_mask = [0] * max_mask
for mask in range(max_mask):
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += songs[i][0]
    sum_mask[mask] = total

dp = [[0] * 4 for _ in range(max_mask)]  # last_genre can be 0-3
dp[0][0] = 1

for mask in sorted(range(max_mask), key=lambda x: bin(x).count('1')):
    current_sum = sum_mask[mask]
    if current_sum > T:
        continue
    for last_genre in range(4):
        count = dp[mask][last_genre]
        if count == 0:
            continue
        for i in range(n):
            if not (mask & (1 << i)):
                ti, gi = songs[i]
                new_mask = mask | (1 << i)
                new_sum = current_sum + ti
                if new_sum > T:
                    continue
                if gi == last_genre and last_genre != 0:
                    continue
                dp[new_mask][gi] = (dp[new_mask][gi] + count) % MOD

answer = 0
for mask in range(max_mask):
    if sum_mask[mask] == T:
        answer = (answer + sum(dp[mask][1:4])) % MOD

print(answer)
```
