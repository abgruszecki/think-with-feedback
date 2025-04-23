<think>
Okay, let's tackle this problem. So the task is to find the number of ways to pick a zebroid subsequence from a given sequence of marbles. The marbles form a zebroid, which means that the colors alternate. The answer needs to be modulo 1e9+7.

First, let's understand the problem. A zebroid is a sequence where each consecutive element alternates in color. For example, red, blue, red is a zebroid. Each single marble is also a zebroid. So the question is, how many such subsequences exist?

Wait, but the problem says that the original sequence is already a zebroid. Oh right! So the input sequence is a zebroid, which means that the colors alternate. So the sequence is either RBRB... or BRB..., etc. But the actual colors don't matter; the problem states that for the first sample, changing the initial sequence to BRB gives the same answer, so the actual colors don't affect the count. So the answer only depends on the length of the sequence and the fact that it's a zebroid.

So the key is to find a way to model the possible subsequences based on the length of the zebroid.

Let's think about the structure. For a sequence of length n, each position can be part of a subsequence. But the subsequence must alternate colors. Since the original sequence is a zebroid, any valid subsequence must also be a zebroid, but in the sense that the subsequence's colors alternate. Wait, but the original sequence alternates, so any subsequence that maintains the order of the original sequence and alternates colors would also form a zebroid. Because the original sequence alternates, any two consecutive elements in the original sequence are different colors. Therefore, any subsequence that takes elements in order will have alternating colors as long as consecutive elements are taken in the original sequence. Wait, no. Because if you take elements that are not consecutive in the original sequence, their colors could be the same. For example, in a sequence R B R, taking the first and third elements (both R) would form a sequence that's not a zebroid. So that's not allowed. So the problem is to count all possible non-empty subsequences where each consecutive pair in the subsequence alternates colors.

But since the original sequence is a zebroid, the colors alternate. So, in the original sequence, the i-th and i+1-th marbles are different. However, when taking a subsequence, the positions of the marbles in the original sequence matter. For example, if the subsequence includes elements i and j where j > i+1, then the color of j depends on the parity of j - i. For example, if the original sequence is R B R B R..., then the color of position i is R if i is odd, B otherwise. So any subsequence must have elements such that consecutive elements in the subsequence alternate colors, which is equivalent to their positions in the original sequence being consecutive in parity.

Wait, maybe there's a pattern here. Let's model the problem. Since the original sequence is a zebroid, the color of each marble is determined by its position. Let's assume the first marble is red (but since the problem says that the answer is the same regardless of the starting color, we can model it in either case). Then the colors alternate: R, B, R, B, etc. So the color of the i-th marble (1-based) is R if i is odd, B if even.

Now, any valid subsequence must have colors that alternate. So for a subsequence of length k, the colors must be R, B, R, ... or B, R, B, ... depending on the starting color. But since the original sequence alternates, the positions of the marbles in the subsequence must form a sequence where each consecutive pair in the subsequence is such that their positions in the original sequence are of opposite parity. For example, if a subsequence includes positions i and j (i < j), then if their colors are different, which in this case would mean that j is i+1. But wait, no. Because if the original sequence is R B R B, then the first and third positions are R and R. If a subsequence includes them, their colors are the same, so the subsequence is invalid. Therefore, the subsequence can only include elements that are consecutive in the original sequence, but that's not true. Wait, for example, take the sequence R B R. The subsequence consisting of the first and second is valid (R B), the second and third is valid (B R), but the first and third is invalid (R R). So for a subsequence to be valid, any two consecutive elements in the subsequence must be adjacent in the original sequence. Because otherwise, their colors would be the same. Wait, no. Let's see: the original sequence is R B R B R. So the colors are R, B, R, B, R. If I take positions 1,3,5: R R R. Not a valid subsequence. So any valid subsequence must consist of elements where consecutive elements in the subsequence are adjacent in the original sequence. Because otherwise, their colors would be same. Wait, but that's not necessarily the case. For example, in R B R B R, taking positions 1,3: R R is invalid. So the only way consecutive elements in the subsequence to have different colors is if they are consecutive in the original sequence. Therefore, the problem reduces to counting all non-empty increasing sequences of indices where each consecutive pair in the subsequence are consecutive in the original sequence. Because only then can their colors alternate. Wait, but that's not true. Because if you have a subsequence where the elements are not consecutive, but the colors alternate. For example, in the original sequence R B R B R, taking positions 1,2,4: R B B. That's invalid. Taking 1,2,3: R B R (valid). Taking 2,3,4: B R B (valid). So any valid subsequence must consist of elements that form a contiguous block in the original sequence. Because if there's a gap, then the colors would repeat. Wait, no. Let's see: take the original sequence R B R B. If I take positions 1,2,4: the colors are R, B, B. Not valid. So invalid. But take positions 2,3,4: B R B. That's valid. But what if the original sequence is R B R B R. Take positions 1,3,4. Colors R R B. The consecutive elements in the subsequence (R and R) are same. So invalid. So, the conclusion is: a valid subsequence can only consist of elements where consecutive elements are adjacent in the original sequence. Because otherwise, the colors would be same. Therefore, the problem reduces to counting all possible non-empty intervals (contiguous sequences) in the original sequence, but that's not the case. Wait, because even if you have a non-contiguous subsequence, but the colors alternate. Wait, but given that the original sequence alternates colors, consecutive elements in the original sequence are different. So, if a subsequence skips elements, then the next element in the subsequence would have the same color as the previous one. For example, in R B R B R, if you take elements 1 and 3: both R. Invalid. So the only valid way for the subsequence is to have consecutive elements in the original sequence. Therefore, the valid subsequences are all the contiguous subsequences. But wait, no. Because a contiguous subsequence in the original sequence is a consecutive sequence of elements, which alternates colors, so any such subsequence is a zebroid. So the number of such subsequences would be the sum of the lengths of all possible contiguous subsequences. For example, in a sequence of length 3: there are 3 length 1, 2 length 2, 1 length 3. Total 6, which matches the first example. Similarly, for n=4: sum 4+3+2+1 =10, but the sample output is 11. Wait the sample input 4 gives output 11. So this approach is incorrect.

Wait the second sample input is 4 and output 11. Let's see. If the original sequence is R B R B. The contiguous subsequences are:

Each single element: 4.

Length 2: 3 (positions 1-2, 2-3, 3-4). Each is valid.

Length 3: 2 (1-2-3, 2-3-4). Each is valid.

Length 4: 1. Valid.

So total is 4 +3 +2 +1 =10. But sample output is 11. So this approach is missing something.

Ah, the sample input 4's output is 11. So where does the extra 1 come from?

Wait perhaps the problem allows non-contiguous subsequences as long as the colors alternate. But how?

Wait let's think again. Let's take the second sample input. Let's say the original sequence is R B R B. Then, the possible valid subsequences include all contiguous ones (sum 10), plus maybe a non-contiguous one. But which one?

Wait, for example, the subsequence consisting of the first and fourth elements: R and B. Their colors are R and B, which alternate. So that's a valid subsequence of length 2. So this would add another possibility. So in the second sample, there's 10 contiguous plus 1 non-contiguous. So the answer is 11.

Ah, so the initial assumption that only contiguous subsequences are valid is incorrect. So how to model this?

So the problem allows non-contiguous subsequences as long as the colors alternate. So the key is that consecutive elements in the subsequence must have different colors, but their positions in the original sequence can be non-consecutive as long as their colors alternate.

Wait, but how can a non-consecutive pair in the original sequence have different colors? Because the original sequence alternates. For example, if the original sequence is R B R B R, then even positions are B, odd are R. So the color of position i is R if i is odd, B if even. So any two positions i and j where i < j, if i and j are of opposite parity (one even, one odd), then their colors are different. So if you have a subsequence where the positions alternate parity, then the colors alternate. So for example, in the original sequence of R B R B, the positions 1 (R), 4 (B) are of different parity (1 is odd, 4 is even). So their colors are R and B, different. So a subsequence [1,4] is valid. So the problem is more complex than just contiguous subsequences.

So the valid subsequences can be any sequence of positions where the parity alternates. For example, 1,3,4: positions 1 (odd, R), 3 (odd, R) -> same color, invalid. So no. But 1,4 (R, B) is valid. 2,3 (B, R) is valid. So the subsequence must consist of elements where each consecutive pair in the subsequence alternates parity. Because the color is determined by parity.

Wait, since the original sequence is a zebroid, the color of the i-th element is determined by i's parity. So, for the purpose of counting, the actual colors don't matter; only the parity of their positions. So any valid subsequence is a sequence of positions (indices) where the parity alternates. Because that's equivalent to the colors alternating.

Therefore, the problem reduces to counting all non-empty subsequences where the parity of the indices alternates (i.e., each consecutive pair in the subsequence has different parity). But also, the subsequence must maintain the order of the original sequence. So the positions in the subsequence must be in strictly increasing order.

So how do we model this?

Let's model it with dynamic programming. Let's consider two cases: subsequences that end with an even position, and those that end with an odd position. For each position i, we can track the number of valid subsequences ending at i with even or odd parity.

Wait, but for each position i, its parity is fixed. So, if the current position is even, then any subsequence ending here must have the previous element's parity be odd (if the subsequence has length >=2). Similarly, for an odd position, previous parity must be even.

So, perhaps we can model two variables: even and odd. even represents the total number of valid subsequences ending with an even index. odd represents the total ending with an odd index.

For each new element (i from 1 to n), if i is even:

- The new even count is 1 (the element itself) plus the previous odd count (since adding this even element to any subsequence that ended with an odd element would form a valid subsequence). So even_new = 1 + odd_prev.

- The odd count remains the same (since adding this even element to an even-ending subsequence would not create a valid one).

Wait, no. Because when processing the i-th element (even), the new even count is the sum of:

- The number of subsequences that end with an even element before i, plus the new subsequence consisting of just this element (1).

But wait, no. The even count is the number of subsequences that end with even, which can be formed by taking this element. So for each new even element, we can add it to all existing subsequences that end with an odd element (since even comes after and has opposite parity), plus the subsequence containing just this element.

So for example, when processing i (even):

even_new = (odd_prev + 1)
odd_new remains the same as before, since this element is even and cannot be added to any even-ending subsequences to form a valid one.

Similarly, when processing an odd element:

odd_new = (even_prev + 1)
even_new remains the same.

So this dynamic programming approach could work.

Let's see with the first example: n=3.

The indices are 1 (odd), 2 (even), 3 (odd).

Initialize even=0, odd=0.

Process index 1 (odd):

odd_new = even_prev (0) + 1 = 1.

even remains 0.

Total is 1.

Process index 2 (even):

even_new = odd_prev (1) +1 = 2.

odd remains 1.

Total is 1 (odd) + 2 (even) = 3.

Process index 3 (odd):

odd_new = even_prev (2) +1 =3.

even remains 2.

Total now is 3 (odd) +2 (even) =5. Wait but the sample output is 6.

Wait, what's wrong here?

Wait wait, let's track the variables step by step.

At each step, the variables even and odd represent the count of subsequences ending with even or odd, respectively.

Initial state: even=0, odd=0.

Processing i=1 (odd):

The new subsequences ending with odd are:

- The new single element (1): count 1.

- Adding i=1 to all existing even-ending subsequences (even is 0, so 0).

So new_odd = 0 (even_prev) +1 =1.

even remains 0.

Now, even=0, odd=1. Total so far is 0+1=1.

Processing i=2 (even):

new_even = odd_prev (1) +1 = 2.

even becomes 2.

odd remains 1.

Total is 2+1=3.

Processing i=3 (odd):

new_odd = even_prev (2) +1=3.

odd becomes 3.

even remains 2.

Total is 3+2=5.

But sample output is 6. Hmm, that's a problem. So this approach is missing something.

Wait, the sample input 3 has output 6. Let's see:

The valid subsequences are:

All single elements: 3.

Pairs: 1-2, 2-3, 1-2-3.

Wait, in the first sample, the answer is 6. Let's list all possible valid subsequences:

1. [1] (R)

2. [2] (B)

3. [3] (R)

4. [1,2] (R, B)

5. [2,3] (B, R)

6. [1,2,3] (R, B, R)

So total 6.

But according to the DP approach, after processing all 3 elements, the total is 3+2=5. So where's the mistake?

Ah! Because the DP approach for i=3 (odd) calculates new_odd = even_prev (which is 2) +1. So that's 3. So the odd count becomes 3, even remains 2. So total is 5. But sample answer is 6.

So this approach is missing something. Where?

Wait, perhaps the DP variables even and odd track the count of subsequences ending with even or odd parity, but the total is the sum of even and odd. But after processing all 3 elements, even=2, odd=3. Sum is 5. So why is the sample 6?

Hmm. Let's see:

After processing i=3:

even is 2 (subsequences ending with even), which are [2], and [1,2].

odd is 3 (subsequences ending with odd: [1], [3], [2,3], [1,2,3]). Wait, wait, that's 4 elements. Wait, what's the count here?

Wait, perhaps the DP approach isn't tracking all possible subsequences. Let's re-examine the approach.

When processing i=1 (odd):

The new_odd is 1 (just the single element [1]).

odd becomes 1.

Processing i=2 (even):

new_even is 1+1=2 (the previous odd count is 1, so adding this even to each of those, which gives 1, plus the new single element [2]. So the even count is 2. Those are [2], [1,2].

Processing i=3 (odd):

new_odd = even_prev (2) +1. So adding this new odd element to each of the even-ending subsequences (there are two: [2] and [1,2]) gives two new subsequences: [2,3] and [1,2,3], plus the new single element [3]. So total new_odd is 2+1=3. So the odd count becomes 3. So the total subsequences are even=2 (from i=2) and odd=3 (from i=3), sum 5. But sample answer is 6.

Ah, here's the problem. The DP approach is missing the subsequence [3], which is added when processing i=3. Because when we process i=3 (odd), new_odd is previous even (2) plus 1. So the 1 here is the new subsequence [3]. So the new_odd is 2+1=3. So the odd count is 3. So the sum is 2+3=5. But sample answer is 6.

Wait, but according to the sample, [3] is counted. So where's the discrepancy?

Wait, the DP's odd count after processing i=3 is 3. So that includes [1], [3], [2,3], [1,2,3]. Wait, that's 4 elements. But according to the calculation, new_odd is 2 (from even_prev) + 1 (the new single element). So the new_odd is 3. How does that break down?

Hmm. Let's track the possible subsequences:

After i=1:

odd: 1 (only [1])

After i=2:

even: 2 ( [2], [1,2] )

odd remains 1.

Total so far: 2+1=3.

After i=3:

For the new_odd, which is even_prev (2) +1.

The even_prev is 2 (the even count after i=2). So the even_prev is the number of even-ending subsequences before processing i=3, which are [2], [1,2].

So adding i=3 (odd) to each of these gives [2,3], [1,2,3]. That's 2 new subsequences. Plus the new single [3]. So total new_odd is 2+1=3. So the new_odd is 3. The existing odd count was 1 (from [1]). So when processing i=3, the new_odd becomes 3, which replaces the old odd count. So the odd count is now 3.

Wait, but how does that account for [1], [3], [2,3], [1,2,3], and [3]?

No. The new_odd is the number of subsequences ending with odd after processing i=3. These are:

All the subsequences that ended with even (from before) and then added i=3 (even_prev count is 2, so 2 subsequences: [2,3], [1,2,3]) plus the new single element [3].

So the new_odd is 2+1=3. So the subsequences ending with odd are:

- From previous odd (before i=3), which was 1 ([1])?

No, when processing i=3, the new_odd is 2 (even_prev) +1 (new single). The previous odd count is 1 ([1]). But when processing i=3, the new_odd is the sum of even_prev (the even count before i=3) +1 (the new single). The previous odd count is not part of the new_odd. Because the new_odd is replacing the existing odd count. Because the new_odd represents the new count of subsequences ending with odd after including i=3.

Wait, perhaps the DP transition is not additive. Let me think again.

At each step i, if the current position is even:

even_new = (previous_odd) + 1

The 1 is the new single element. previous_odd is the count of subsequences ending with odd, which can be extended by this even element.

The even_new replaces the previous even count. Because the new even count is the number of subsequences ending with even after processing i. The previous even count is not carried over, because those subsequences could not have included i (since they ended before i). Or wait, no. The even count before processing i includes subsequences up to previous elements. So for even_new, it's the new subsequences ending with even (i) which can be formed by adding i to subsequences ending with odd, plus the subsequence consisting of i alone. The previous even count is not added to even_new, because those are subsequences that end with even before i. So those subsequences are not modified by adding i, as they are already part of the count.

Wait, no. The even count after processing i is the count of all subsequences that end with even parity up to and including i. So, for example, if i is even, then the even count after processing i is equal to the number of subsequences that end with even (including those that existed before, but not including the new ones formed by adding i). Wait, no. The previous even count refers to subsequences that end before i, but with even parity. Since i is even, those subsequences can't include i. So when processing i, the new even count is the previous_odd (number of subsequences ending with odd, which can be extended by i) plus 1 (the new subsequence consisting of i alone). The previous even count is not part of even_new, because those subsequences are not extended by i (since they end with even, and i is even. Adding i to them would create a subsequence with consecutive even elements, which is invalid). So even_new = previous_odd + 1.

Similarly, if i is odd, then the new_odd is previous_even + 1, and even remains the same.

So in the first example:

Processing i=1 (odd):

odd_new = previous_even (0) +1 =1.

even remains 0.

Total after i=1: 1.

Processing i=2 (even):

even_new = previous_odd (1) +1 =2.

odd remains 1.

Total after i=2: 2+1=3.

Processing i=3 (odd):

odd_new = previous_even (2) +1=3.

even remains 2.

Total after i=3: 3+2=5.

But the sample answer is 6. So where is the mistake?

Wait, the sample's valid subsequences are 6. According to the DP approach, the sum is 5. So there's a missing case.

Hmm. Let's re-examine the possible subsequences for n=3.

The valid subsequences are:

Single elements: 3 (each is allowed).

Pairs: (1-2), (2-3) (each pair has different colors), and (1-3) (same colors, invalid). So 2 pairs.

Triples: (1-2-3), which alternates colors. So that's valid.

So total is 3+2+1=6. Which matches the sample.

But according to the DP approach, after processing i=3, the even count is 2 (subsequences ending with even: [2], [1-2], [2-3], [1-2-3]? No. Wait, even count after i=3 is 2. Because even count is the number of subsequences ending with even. For i=3, even count remains at 2 (from i=2). The even count after i=3 is 2. So even count includes [2], [1-2], [2-3], [1-2-3]?

Wait no. Because after i=2, even count is 2: [2], [1-2]. Then when processing i=3 (odd), the even count remains 2, as the even count is not modified. The even count includes all subsequences ending with even up to i=3. But i=3 is odd, so no new even subsequences are formed. So even count after i=3 is still 2.

The odd count after i=3 is 3: these are:

[1], [3], [1-2-3], [2-3], [1-3]? No. Wait, according to the DP transitions:

After i=3, the odd count is previous_even (2) +1 =3. The previous_even is 2 (from i=2: [2], [1-2]).

So adding i=3 to each of those gives [2-3], [1-2-3], and the new single [3].

So the odd count after i=3 is 3, which includes [1], [2-3], [1-2-3], [3]?

Wait, no. How does the DP approach track the count.

Let's track the possible subsequences step by step:

After i=1 (odd):

odd count =1 → [1].

After i=2 (even):

even count =2 → [2], [1-2].

odd count =1 (still [1]).

After i=3 (odd):

The new_odd is previous_even (2) +1 → 3. So the odd count becomes 3. These are:

- [2-3], [1-2-3] (from previous_even), and [3].

But what about the previous odd count (1)? Where does [1] go? 

Ah, the problem here is that the DP transition replaces the previous odd count. So when processing i=3, the new_odd is 3, which replaces the previous odd count of 1. So the new_odd count is 3, which includes:

- All the subsequences that were added by combining previous_even (even-ending) with i=3 (odd), which are [2-3] and [1-2-3], plus the new single [3].

But what about the previous odd-ending subsequences (like [1])? Are they included in the new_odd count?

No. Because the new_odd count represents subsequences that end with i. So the previous odd count (subsequences ending with odd before i=3) are not included. So in the DP approach, the odd count after processing i=3 is the number of subsequences that end with i=3 (odd) or that were formed by adding i=3 to even-ending subsequences. But the previous odd count (like [1]) is not part of this. So the total subsequences would be even + odd, which is 2 (even) +3 (odd) =5, which is missing the [1] and [1-2] subsequences.

Wait, this can't be right. Because when processing i=3, the even count remains 2 (the subsequences [2], [1-2], which were created at i=2. These are subsequences that end with even. The new_odd count is 3 (subsequences ending with i=3: [3], [2-3], [1-2-3]). The previous odd count (1, [1]) is still part of the total sum? Or not?

Ah, no. Because the DP variables even and odd represent the current count of subsequences ending with even or odd parity, respectively, up to the current position. So, when processing i=3, the even count remains 2, which are the subsequences ending with even (i=2). The odd count is now 3, which are the subsequences ending with odd (i=3). But the previous odd count (1, [1]) is not included anymore. Because the new_odd count replaces the old one. So this is the mistake in the approach.

Wait, no. Because when you process i=3, which is odd, the new_odd count is the number of subsequences that end with odd parity after including i=3. This includes the new subsequences formed by adding i=3 to previous even-ending subsequences, plus the single element [3]. The previous odd count (which was subsequences ending with odd before i=3) are not part of the new_odd count. So those subsequences (like [1]) are not counted anymore. Hence, the total sum would be even (2) + new_odd (3) =5, but the actual valid subsequences include [1], [2], [3], [1-2], [2-3], [1-2-3], which is 6.

So the DP approach is missing the previous odd count when processing new elements.

Wait, but how does the DP approach track all possible subsequences? Because the variables even and odd represent the count of subsequences that end with even or odd parity up to the current index. So when processing i=3 (odd), the new_odd count is 3. The even count is 2. So the total subsequences after processing i=3 is 2+3=5. But according to the sample, there are 6.

So what's wrong here?

Ah, the DP approach is incorrect. Because when processing a new element, the previous even and odd counts are not carried forward. For example, the previous odd count (1, [1]) is lost when processing i=3, because the new_odd count replaces it. But the [1] subsequence is still valid and should be part of the total count.

So the DP variables even and odd should accumulate the count of all subsequences ending with even or odd parity up to the current index. Not just the new ones.

Wait, perhaps the correct way is to keep track of two variables: the total number of subsequences ending with even and odd parity, including all possibilities up to that index. So when processing a new element, we can update these variables by adding the new possibilities. 

For example:

If the current element is even (parity), then:

- Any subsequence that ends with an even element can be formed by:

   a) appending the current element to a subsequence that ends with odd (since even after odd is allowed).

   b) starting a new subsequence with this even element.

So the new even count is (previous_odd) + 1. The previous even count is not added here, but existing even-ending subsequences are still valid and are part of the total count.

Wait, no. Because the even and odd variables represent the total number of subsequences ending with even or odd after processing each element. So the existing even-ending subsequences (from previous steps) are already accounted for in the even variable, and when a new even element is processed, those existing even-ending subsequences are not modified. The new even-ending subsequences are those formed by appending the current even element to previous odd-ending subsequences plus the new single element. The existing even-ending subsequences are not part of the new even count; they are still valid but are not extended. But wait, the new even count should include the previous even count plus the new possibilities. But that's not the case here. Because the new even count is only the new possibilities.

Ah, here's the mistake. The current even count after processing i is the sum of the existing even count (from before) plus the new even-ending subsequences formed by adding the current element. But that's not correct. Because the existing even count represents subsequences that end with even before processing i. When i is even, the new even-ending subsequences are the existing odd count plus 1 (the new single element). The existing even count is not part of this, but those subsequences are still valid. However, the DP approach's even variable after processing i is the number of even-ending subsequences up to i. So, for example, if the even count was x before processing i (even), then after processing i, the even count becomes x + (previous_odd + 1). Because the existing even-ending subsequences are still valid (they don't include i), and the new ones are previous_odd +1.

Wait, no. Because the even count after processing i should represent the total number of even-ending subsequences that include elements up to i. The previous even count (before processing i) is the number of even-ending subsequences up to i-1. So when processing i (even), the new even-ending subsequences are:

- All existing even-ending subsequences (they are still valid but do not include i).

- New even-ending subsequences formed by appending i to existing odd-ending subsequences.

- The new subsequence consisting of i alone.

But no, because existing even-ending subsequences (without i) are still valid and part of the even count. So the new even count should be (existing even count) + (previous_odd +1). Because the new even-ending subsequences are formed by adding i to previous_odd subsequences and adding the single i. The existing even count is not part of the new even-ending subsequences that include i, but they are still part of the total even count.

So the correct approach is to accumulate the even and odd counts. For example:

When processing i (even):

even_new = even_prev + (odd_prev + 1)

odd_new remains the same.

Wait, no. Because the existing even_prev are subsequences that end with even before i. They are still valid, but they don't include i. The new even subsequences are formed by adding i to odd_prev and the single i. But even_prev is not part of the new even count (since they are not modified by adding i). Wait, but the even_new is the number of even-ending subsequences after processing i. Which includes:

- existing even_prev (subsequences ending with even that do not include i).

- new subsequences ending with even (i) formed by adding i to any subsequence ending with odd (odd_prev) plus the single i.

So even_new = even_prev + (odd_prev + 1).

Similarly, for odd elements:

odd_new = odd_prev + (even_prev + 1).

Ah, this makes sense. Because when processing i-th element, which is even:

- The existing even_prev subsequences are still valid, but they do not include i. So they are part of the new even count.

- The new even subsequences are those formed by appending i to any subsequence that ended with odd (odd_prev) and the new single i.

So even_new = even_prev + (odd_prev + 1).

Similarly for odd elements.

Let's re-calculate the first sample with this approach.

Sample input 3:

Processing i=1 (odd):

even_prev =0, odd_prev=0.

odd_new =0 + (0 +1) =1.

even remains 0.

Total even+odd=0+1=1.

Processing i=2 (even):

even_new =0 + (1+1) =2.

odd remains 1.

Total 2+1=3.

Processing i=3 (odd):

odd_new =1 + (2+1) =4.

even remains 2.

Total 2+4=6. Which matches the sample.

Ah, this is correct.

So the correct dynamic programming approach is to model the even and odd counts as cumulative sums. Each step, when processing an element, we update the even or odd count by adding the previous opposite count plus 1 (for the new single element). So the recurrence is:

For each i from 1 to n:

If i is even:

   even += odd + 1

else:

   odd += even + 1

The initial values are even=0, odd=0.

Wait, but how is that possible? Let's re-express:

Initially, even = 0, odd =0.

For each position i:

if i is even:

   new_even = even + (odd + 1)

   new_odd = odd

else:

   new_odd = odd + (even + 1)

   new_even = even

So, for each i, even and odd are updated in this way.

Let's walk through the first sample:

i=1 (odd):

new_odd =0 + (0+1) =1.

even remains 0.

even=0, odd=1. Sum=1.

i=2 (even):

new_even =0 + (1+1) =2.

odd remains 1.

sum=3.

i=3 (odd):

new_odd =1 + (2+1)=4.

even remains 2.

sum=6. Which is correct.

Yes, this works. So the correct approach is to model even and odd as cumulative sums, adding the previous opposite count plus 1 for the current element.

Now, the question is how to implement this efficiently for large n (up to 1e6).

But for each step, we can compute even and odd in O(1) time. So the overall time complexity is O(n), which is acceptable for n=1e6.

So the algorithm is:

Initialize even =0, odd=0.

For each i from 1 to n:

   if i is even:

       even = (even + odd + 1) % MOD

   else:

       odd = (odd + even + 1) % MOD

The result is (even + odd) % MOD.

Wait, but in the first sample:

even after processing i=3 is 2, odd is 4. Sum is 6.

Yes.

Another example, sample input 4:

n=4.

Processing:

i=1 (odd):

odd =0 +0+1=1. even=0. sum=1.

i=2 (even):

even=0+1+1=2. sum=3.

i=3 (odd):

odd=1 +2+1=4. sum=6.

i=4 (even):

even=2 +4+1=7. sum=7+4=11.

Which matches the second sample's output of 11. So this approach works.

So the code should be straightforward.

Now, for n up to 1e6, this approach requires O(n) time and O(1) space. Which is acceptable.

Now, the code:

Read n.

Initialize even=0, odd=0.

MOD =1e9+7.

Loop from i=1 to n:

   if i is even:

       even = (even + odd + 1) % MOD

   else:

       odd = (odd + even + 1) % MOD

Result is (even + odd) % MOD.

But wait, in Python, for large n (1e6), this loop will take O(n) steps, which is acceptable, as 1e6 operations are manageable within 2 seconds.

Now, implement this.

But wait, in Python, the loop for 1e6 is acceptable. Let's test for n=4:

i=1: odd=1.

i=2: even=2.

i=3: odd=1+2+1=4.

i=4: even=2 +4+1=7.

sum is 7+4=11.

Yes.

So the code should be:

n = int(input())

MOD = 10**9 +7

even = 0
odd =0

for i in range(1, n+1):
    if i %2 ==0:
        even = (even + odd +1) % MOD
    else:
        odd = (odd + even +1) % MOD

print( (even + odd) % MOD )

This should work.

Testing for the first sample (n=3):

Loop for i=1: odd becomes 0 +0+1=1.

i=2: even becomes 0+1+1=2.

i=3: odd becomes 1 +2 +1=4.

sum 2+4=6.

Yes.

This code should be correct.
</think>

```python
n = int(input())
MOD = 10**9 + 7
even = 0
odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even = (even + odd + 1) % MOD
    else:
        odd = (odd + even + 1) % MOD
print((even + odd) % MOD)
```