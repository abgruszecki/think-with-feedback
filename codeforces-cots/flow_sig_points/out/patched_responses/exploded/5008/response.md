<think>
Okay, I need to solve this problem. Let's read it carefully.

The problem is: Valera has an array a of n integers. The function f(x) sums the elements a_i where the i-th bit in x's binary representation is set. We need to find the maximum f(x) for x between 0 and m inclusive. The binary representation of m is given as a string.

Hmm. So the task is to find the x <= m (binary given) where the sum of a_i for the set bits is maximum.

The constraints are n up to 1e5. So any O(n^2) approach is out. Need an O(n) or O(n log n) solution.

Let's think about how to model this.

First, the maximum possible x is m. But sometimes, a number less than m can have a higher sum. For example, if a higher bit in m is set but the a_i for that bit is low, but turning it off allows lower bits to be set which have higher a_i's. Like the first example: m is 2 (binary 10), and a is [3,8]. The maximum is x=1 (binary 01), sum 3. Because for m=2 (binary 10), the sum is 8, but wait, wait no. Wait the first example's input is:

n=2
array 3 8
binary is '10' which is 2. So m=2. So x can be 0,1,2.

f(0) is 0. f(1) is a0=3. f(2) is a1=8. Oh but the sample output is 3. Wait, the first sample's output is 3. That's conflicting. Wait the first sample's input says:

Sample input 1:

2
3 8
10

So m is '10' in binary, which is 2. So x can be 0,1,2.

But a0 is 3 and a1 is 8. So x=1 (binary 01) gives sum 3. x=2 (binary 10) gives sum 8. So why is the output 3? Oh wait, maybe I misread the problem. Wait the function f(x) is summing a_i multiplied by the bit(i). Wait the problem says, bit(i) is 1 if the binary representation of x contains a 1 on the i-th position. Wait, but in the first example, the binary of x=2 is 10. The i-th positions are 0-based. So bit 0 is 0, bit 1 is 1. So sum is a1 =8. But the sample output is 3. So that can't be right. Wait the first sample's output is 3. So something's wrong here. Oh wait, maybe the bits are ordered differently. Wait in the problem statement, the function f(x) is sum a_i * bit(i), where bit(i) is 1 if x's binary has a 1 at the i-th position. Wait but the example in the note says:

In the first test case, m is 20 (but wait 20 in base 10 is 10100, but the input is n=2 and the binary string is '10', which is 2. So perhaps there's a typo. Oh wait the note says, m=20? No, maybe it's a typo, but the sample input is:

First input line: 2

Second line: 3 8

Third line: 10 (binary for 2). But the note says m=20 which is conflicting. Wait that can't be. So perhaps the note's example is for a different case. Oh maybe the note is referring to the first sample input. Let's check the note again.

First sample's note says: In the first test case m=20 =1, which seems conflicting. Wait perhaps there's a mistake in the note. Wait the note says m=20 equals 1. That can't be. So maybe there's a typo in the note, perhaps the binary is '10' which is 2 in decimal, but the note says m=2 and the possible x's are 0,1,2. Then f(1) is 3, which is the maximum. So the sample output is 3. That makes sense.

Wait the first sample input is binary '10', which is 2. So x can be up to 2. The a array is [3,8]. So for x=0: sum 0. x=1: sum 3. x=2: sum 8. So why is the output 3? That's impossible. So what's going on here. Oh wait maybe the bits are ordered the other way. Like the first bit is the most significant bit, but perhaps the problem considers the i-th position as the 2^i bit. So for x=2, the binary is 10, so bit 0 is 0, bit 1 is 1. So a1 is added. So the sum is 8. But the sample output is 3. So this suggests that the sample input's output is 3, which would imply that the correct x is 1. So how can that be?

Wait in the first sample input, perhaps the binary string is read in reverse order. Because the problem says that the binary string s_0 s_1 ... s_{n-1} represents m as sum 2^i * s_i. Wait no: the problem says, the third line is a sequence of digits s0 s1 ... sn-1, and m is sum 2^i * s_i. So s0 is the 0-th bit (LSB), s1 is the 1st bit, etc. Wait wait no, if the binary string is s_0 s_1 ... s_{n-1}, then for m, each s_i is multiplied by 2^i. So for example, if the string is "10", then s_0 is 1 (LSB) and s_1 is 0 (next bit). So m is 1*2^0 + 0*2^1 = 1 +0 =1. Oh! Oh right! So the binary string is written in the order s0 s1 ... sn-1, which corresponds to bits from least significant to most significant. So in the first sample, the binary string is '10' (n=2), which is s0=1, s1=0. So m =1*1 + 0*2 =1. So x can be 0,1. So for x=0, sum is 0. x=1, sum is a0=3. So output is 3, which matches the sample. Oh! So that's the key point. The binary string is given in s_0 to s_{n-1}, which are the bits for 2^0 up to 2^{n-1}. So for example, the binary string '10' with n=2 represents 1*2^0 + 0*2^1 =1. So m is 1. So the possible x is 0 or 1. Hence the first sample's output is 3.

So the problem is to read the binary string correctly as the bits of m, where the first character is the least significant bit (2^0), and the last character is the most significant bit (2^{n-1}).

So that's crucial. Now the approach.

The goal is to find x <= m (binary as per the input) such that the sum of a_i for the bits set in x is maximum.

To maximize the sum, ideally, we take all bits where a_i is positive. But we have to make sure that x doesn't exceed m.

So the problem is similar to finding the maximum subset of bits (positions) where the combination of bits forms a number <= m, and the sum of a_i for those bits is maximum.

This seems similar to the problem where you want to choose bits greedily, but need to account for m's constraints.

An approach could be to process the bits from the most significant to least significant. For each bit position, decide whether to set it or not, based on whether setting it (and possibly all higher bits) allows for the maximum sum, but ensuring that the number formed doesn't exceed m.

But how to model this?

Alternatively, let's think of the binary representation of m. For each bit position i (from highest to lowest), we can decide whether to take the a_i if possible. If setting the current bit is allowed (i.e., the prefix up to this bit is <= the prefix of m up to this bit), then we can choose to set it if a_i is positive, but only if doing so doesn't make the number exceed m.

Wait, perhaps a better way is to model the process of building x bit by bit, starting from the highest bit down to the lowest. At each step, we decide whether to set the current bit. If setting the bit would not make x exceed m, then we can choose to set it if a_i is positive. Otherwise, we can't set it.

Wait but the bits are ordered from 0 (LSB) to n-1 (MSB) in the array a. Wait, no. The array a is a_0 to a_{n-1}, where a_0 corresponds to the 0-th bit (LSB), a_1 to the 1st bit (next), up to a_{n-1} (MSB). So the binary string s_0 is the LSB, s_1 the next, and so on. So for example, the binary string '10' (n=2) is s_0=1, s_1=0: which is 1*1 +0*2=1. So m=1.

So the bits in m are ordered from LSB to MSB in the string. So to process the bits in the order of MSB to LSB, which is the standard way, perhaps we need to reverse the bits.

Wait, for example, n=5, binary string is '11010' (third line in the second sample). s_0 is '1', s_1 '1', s_2 '0', s_3 '1', s_4 '0'. So m is 1*1 + 1*2 + 0*4 + 1*8 + 0*16 =1+2+8=11. So m is 11.

But the binary representation of 11 is 1011. Wait, but according to the input, the binary is '11010' (s_0 to s_4). Wait, perhaps I'm miscalculating. Let's see:

s_0 is the first digit in the string, which is the first character. For example, in the second sample input's third line is "11010", which is s_0=1, s_1=1, s_2=0, s_3=1, s_4=0. So the bits are:

bit 0 (2^0): 1
bit 1 (2^1): 1
bit 2 (2^2): 0
bit 3 (2^3): 1
bit 4 (2^4): 0

So m is 1*1 +1*2 +0*4 +1*8 +0*16 =1+2+8=11. So the binary of m is 1011, which is 11 in decimal. So the input's binary string is a representation of m's bits from LSB to MSB.

But when processing the bits in order from MSB to LSB (as is common in bit manipulation), we need to process the bits starting from the highest (n-1) down to 0.

So the approach would be:

1. Convert the binary string into a list of bits (s_0 to s_{n-1}), which represents m as sum_{i=0 to n-1} s_i * 2^i.

2. Now, to process the bits in order from highest (MSB) to lowest (LSB). For each bit position i (starting from n-1 down to 0), we need to decide whether to set it in x, considering the current state of x's bits and whether setting this bit would allow x to remain <= m.

The challenge is to choose the bits in a way that maximizes the sum of a_i for the set bits, while ensuring that x does not exceed m.

This is similar to the problem where you try to form the largest possible number less than or equal to m, but here the "value" of each bit is a_i, which may not be in the same order as the bit's numerical value. So for example, a higher bit (like 2^4) may have a_i=0, so it's better to not set it even if possible, and set lower bits with higher a_i.

So the optimal approach would be to:

- For each bit from the highest (i = n-1) down to 0:

   a. Check if setting this bit in x is possible without exceeding m, considering the bits already set.

   b. If setting this bit is possible, decide whether it's beneficial to set it (i.e., a_i is positive). If a_i is positive, we should set it if possible. If a_i is negative, not setting it may be better, but we have to ensure that even if we don't set it, the remaining bits can be set optimally.

But how to model this?

An alternative approach is to build x bit by bit, making decisions at each step that maximize the sum while ensuring that the bits chosen so far, along with the remaining bits, do not exceed m.

This seems like a greedy approach. Let's outline it:

Initialize x to 0.

We process each bit from the highest (i = n-1) to the lowest (i=0).

At each step, we decide whether to set the current bit in x.

If setting the current bit would not make x exceed m, then:

   If a_i is positive, set it (because that adds to the sum).

   Else, leave it unset (since setting it would reduce the sum).

But how do we check if setting the current bit would allow the remaining bits (lower than i) to be set in a way that x <= m.

Wait, perhaps the approach is similar to constructing the maximum possible number <= m, but with a twist that each bit's value is a_i instead of 2^i.

Wait, perhaps the standard approach for such problems is to find the bits where a_i is positive and set them as much as possible, but ensuring that the resulting x is <= m.

But how?

Another way to look at it: the sum is maximized by including as many a_i with positive values as possible. But when including a_i, the corresponding bit in x must be set, which may cause x to exceed m. So the problem is to select a subset of bits where the bits that are set in x form a number <= m, and the sum of their a_i is maximum.

This is similar to the knapsack problem, but with a constraint that the sum of 2^i for selected bits is <= m. However, with n up to 1e5, a DP approach is impossible.

Thus, a greedy approach is needed.

The key is to process the bits in order of descending a_i, but this might not work. Alternatively, process bits from the highest (most significant) to the least significant, and decide whether to set them based on whether the a_i is positive, and whether setting them can still allow the number to be <= m.

Wait, let's think of it this way:

We start with x = 0. We process the bits from the highest (i = n-1) down to 0.

For each bit i:

If the current prefix of x (bits higher than i) is less than the prefix of m, then we can choose to set the i-th bit or not. If we set it, then for the remaining bits (lower than i), we can set all bits with positive a_i. Because even if their sum of 2^i would make x exceed m, since the higher bits are already lower, adding lower bits can't make x exceed m.

But if the current prefix of x is equal to the prefix of m, then we must not set any bit higher than what m has. So, in this case, we can only set the i-th bit if m's i-th bit is set, and then we have to follow m's bits for lower bits.

Wait, this is similar to the approach used in the problem where you want to find the maximum XOR less than or equal to m. But here, it's about choosing bits to maximize sum of a_i, while keeping x <= m.

Let me formalize this:

At each step i (from MSB to LSB), we have two possibilities:

1. The bits chosen so far (bits higher than i) are exactly the same as the corresponding bits in m. Then, for the current bit i, if m's i-th bit is 1, we can choose to set it to 0, but then for all lower bits, we can set any bits (as long as a_i is positive) because x would be less than m.

Alternatively, if m's i-th bit is 1, we can set the current bit to 1, and proceed to the next bits with the same constraint (i.e., the prefix is still the same as m's).

If m's i-th bit is 0, then we can't set the current bit to 1, because that would make the prefix higher than m's.

2. The bits chosen so far are less than m's prefix. Then, for the current bit i, we can choose to set it if a_i is positive (since we can set it and still have x <= m). If a_i is positive, set it; else, leave it.

So the algorithm would track whether the current x is already less than m's prefix. If yes, then for all remaining bits, we can set them if a_i is positive. If not, then we have to follow m's bits.

So the steps would be:

Initialize sum = 0

Initialize tight = True (meaning that the current prefix is exactly the same as m's up to now)

For i from n-1 downto 0:

   If tight:

       if m's i-th bit is 1:

           option1: set this bit to 1. Then, the sum += a_i. For the remaining bits, we can decide whether to set them (if a_i is positive) but we have to check if tight remains.

           option2: set this bit to 0. Then, sum remains. But for the remaining bits, tight becomes False, so we can set any bits with a_i positive.

           Choose the option that gives the maximum possible sum.

       else:

           must set this bit to 0. sum remains. tight remains.

   else:

       if a_i is positive, set this bit to 1, sum += a_i.

But how to model this recursively or iteratively?

But given that n is up to 1e5, a recursive approach is impossible. So we need an iterative approach.

The problem is that when tight is True, we have to consider both possibilities (set or not set the current bit if allowed). This could lead to a lot of possibilities, but perhaps we can model this with some variables.

The key idea is to track two possibilities at each step:

1. The current prefix is exactly the same as m's (tight case).

2. The current prefix is already less than m's (non-tight case).

At each step, for each of these possibilities, we can compute the maximum sum possible.

This is a dynamic programming approach with two states: tight and not tight.

Let's formalize it:

We can represent the state as (current_max_sum, is_tight).

For each bit i from n-1 down to 0:

   For each state (sum_so_far, is_tight):

      if is_tight:

          if m's i-th bit is 1:

              option1: set this bit. sum becomes sum_so_far + a_i. The new is_tight is (the next bits are also set as per m's bits). Wait no, if we set the bit (which is 1), then for the next bits, the tightness depends on whether the current prefix equals m's prefix up to i. So if we set the bit (same as m's), then the new tight is True. Then, proceed to the next bit.

              option2: not set the bit. sum remains. The new is_tight is False, because the current prefix is now less than m's (since m's bit is 1, and we set 0 here). Then, for the remaining bits, we can choose any bits with a_i positive.

              So we take the maximum of the two options.

          else:

              can't set the bit (since m's bit is 0). So sum remains. The new is_tight is True only if the current bit is not set (but m's is 0, so it's already the same).

      else:

          can choose to set the bit if a_i is positive. The sum increases by a_i if set.

So for the DP approach, for each bit, we track two possible maximum sums: one where the prefix is tight (exactly matches m's bits up to now), and one where it's not tight (prefix is less).

We can model this with two variables: max_tight (the maximum sum when the prefix is tight) and max_loose (the maximum sum when the prefix is not tight).

Initially, for the highest bit (n-1), which is the first bit we process, if the bit is part of m's bits, we start with the possibilities.

Wait, let's think of the steps:

Initialize max_tight and max_loose.

Initially, before processing any bits, max_tight is 0 (sum is 0), and the prefix is exactly matching m's (since nothing is processed). But for the first bit (n-1), if the bit is 1, then processing it can choose to set or not set, but for the next bits.

Wait, maybe the initial state is that we're tight (all higher bits processed so far, which are none, are equal to m's). So initial max_tight is 0, and max_loose is negative infinity (since we can't be loose yet).

Wait, perhaps the initial state is:

max_tight = 0 (sum is 0, and tight is True)

max_loose = -infinity (sum is 0, and tight is False. But initially, tight is True.)

Then, for each bit from n-1 downto 0:

   new_max_tight = -infinity

   new_max_loose = -infinity

   if the current bit's m is 1:

       // In the tight case:

       // Option 1: set the bit (1), sum += a_i. New tight is True.

       option1 = max_tight + a_i if a_i is positive? No. Because if the m's bit is 1, and we're tight, setting the bit (same as m) and proceed.

       Wait, but the decision to set the bit depends on whether it's beneficial. But in the DP approach, for each possible state, we compute the maximum possible sum.

       So for the tight case:

           if the current m's bit is 1:

               // Option 1: set the bit.

               new_tight_sum = max_tight + a_i

               new_tight = True (since the bit is set to 1, same as m's bit)

               // This contributes to new_max_tight.

               // Option 2: not set the bit (0). Then, sum remains max_tight. Now, tight becomes False, and for the remaining bits, we can set any bits with a_i positive.

               new_loose_sum = max_tight

               new_loose = False

               So, for the new_max_loose, we can take the maximum between existing new_max_loose and new_loose_sum.

               Also, new_max_tight is the maximum between current new_max_tight and new_tight_sum.

           else:

               // m's bit is 0. So in tight case, we can't set the bit.

               new_tight_sum = max_tight

               new_max_tight = new_tight_sum

               // no option here.

       So for each step, we have to consider the possibilities.

       Then, for the loose case:

           if loose, we can set the bit if a_i is positive. So sum += a_i if a_i is positive.

           So in the loose state, the new_loose_sum is max_loose + (a_i if a_i >0 else 0)

           new_max_loose would take the maximum between existing new_max_loose and this value.

   So combining all possibilities.

This approach can be implemented with O(n) time, which is acceptable for 1e5.

So the steps are:

Initialize max_tight = 0 (sum is 0, tight)

max_loose = -infinity (not possible)

For each bit i from n-1 downto 0:

   current_bit = s[i] (since s is the binary string, but s_0 is the LSB. Wait no. Wait the binary string is s_0 s_1 ... s_{n-1}, where s_0 is the LSB (2^0), s_1 is 2^1, etc. So to process from MSB to LSB, we need to process s in reverse order. For example, for n=2, s is '10' (s_0=1, s_1=0). The MSB is s_1 (0), and LSB is s_0 (1). So to process from MSB to LSB, the bits are s_1, s_0.

Wait, this is a crucial point. So the binary string is given as s_0 (LSB) to s_{n-1} (MSB). So the MSB is the last character in the string. So to process the bits from highest to lowest (MSB to LSB), we need to process the string in reverse order.

Wait no. Wait, the MSB is the (n-1)-th bit, which is 2^{n-1}.

For example, if the binary string is '10' (n=2), then s_0 is 1 (LSB, 2^0), s_1 is 0 (2^1). So m =1*1 +0*2=1.

So the MSB is s_1 (bit 1, 2^1). So when processing from MSB to LSB, we start with i = n-1 =1 (s_1), then i=0 (s_0).

So the binary string is processed in reverse order for the bits. For example, the string is '11010' (second sample's third line), which is s_0=1, s_1=1, s_2=0, s_3=1, s_4=0. The bits are 2^0 (1), 2^1 (1), 2^2 (0), 2^3 (1), 2^4 (0). The MSB is s_4 (0). So processing bits from 4 (i=4) down to 0.

Thus, the binary string is s[0] is LSB, s[1] is next, etc. So to process from MSB to LSB, the indices are from n-1 down to 0. So for each i in 0..n-1, the bit value is 2^i. But in the binary string, s[i] is the value of the 2^i bit.

So to process the bits in order from highest to lowest (i from n-1 downto 0), we can just iterate from the end of the string to the beginning.

Wait no. Wait for n=5, the binary string is '11010'. The indices are 0,1,2,3,4. The bits are 2^0 (s[0] =1), 2^1 (s[1]=1), 2^2 (s[2]=0), 2^3 (s[3]=1), 2^4 (s[4]=0). So the MSB is 2^4 (s[4]). So processing from i=4 downto 0 gives the order from MSB to LSB.

So yes, the order is correct.

Thus, the code will process the binary string in reverse order (from i =n-1 downto 0). For each i, the bit is s[i], which is the 2^i bit. Wait, no. Wait, the bits are s_0 (2^0), s_1 (2^1), etc. So the i-th position in the array is the 2^i bit. So when processing from i =n-1 downto 0, that's the 2^{n-1} bit down to 2^0. So in this case, for i in range(n-1, -1, -1), processing each bit as 2^i. But when we process the bits in this order, the MSB is processed first.

Thus, the code will loop through each i from n-1 downto 0.

Now, for each bit i (processed in order from MSB to LSB), the code will compute the new_max_tight and new_max_loose.

Let's formalize the transitions:

At each step i:

current_bit = s[i] (either '0' or '1').

The current a_i is a[i] (since a is given in the same order: a[0] corresponds to the 0-th bit (LSB), which is 2^0. So a is ordered from LSB to MSB. So a[i] is the value for bit i (2^i).

Wait, no. Wait the problem says that for x, the function f(x) is sum of a_i * bit(i), where bit(i) is 1 if x's binary has a 1 on the i-th position. So i is the bit position (0-based). So a[i] is the coefficient for the 2^i bit.

Thus, for the code:

the a array is a[0], a[1], ..., a[n-1], which correspond to the bits 2^0, 2^1, ..., 2^{n-1}.

The binary string s is s_0 to s_{n-1}, which are the bits for 2^0 to 2^{n-1}, respectively. So the binary string's first character is the 2^0 bit.

Thus, when processing bits from MSB to LSB (i from n-1 downto 0), the bit positions are 2^{n-1}, 2^{n-2}, ..., 2^0. So for each i in this order, the bit is 2^i. So the code loops over i in the order of n-1 downto 0.

But this is correct, because the MSB is the largest bit.

Thus, the code will process each bit i (from n-1 downto 0), and for each, check if the current bit in m is set (s[i] == '1').

Now, for each i, the transitions are:

If the current state is tight (max_tight):

   if current_bit is '1':

       option1: set the bit. sum += a[i]. The new state is tight (if the bit is set as per m, which it is here). So new_max_tight would be updated with max_tight + a[i].

       option2: don't set the bit. sum remains. The new state is not tight. For the remaining bits, can choose to set any bits with a[i] positive. So new_max_loose is max(max_loose, max_tight).

       So new_max_tight would take the maximum of the previous new_max_tight and option1.

       new_max_loose would take the maximum of previous new_max_loose and option2.

   else:

       can't set the bit (since current_bit is 0 and state is tight). So must not set it. sum remains. new_max_tight is max_tight (since we are still tight).

If the current state is loose (max_loose):

   can choose to set the bit if a[i] is positive. So sum increases by max(a[i], 0). So new_max_loose is max_loose + max(a[i], 0).

So the code would have:

for each i in reversed(range(n)):

   current_bit = s[i]

   a_i = a[i]

   new_tight = -infinity

   new_loose = -infinity

   # handle transitions from tight state
   if current_bit == '1':
       # option1: set the bit (sum += a_i)
       temp = max_tight + a_i
       new_tight = max(new_tight, temp)
       # option2: don't set, sum remains, state becomes loose
       new_loose = max(new_loose, max_tight)
   else:
       # can't set, sum remains, state remains tight
       new_tight = max(new_tight, max_tight)

   # handle transitions from loose state
   # in loose state, can choose to set or not based on a_i
   best = max(a_i, 0)
   temp = max_loose + best
   new_loose = max(new_loose, temp)

   # also, if max_tight is possible, but if current state is tight, it's handled above.

   # update max_tight and max_loose for next iteration
   max_tight, max_loose = new_tight, new_loose

Wait, but for the first iteration, max_loose is -infinity, which can't contribute. So after the first step, the transitions would be:

For example, in the first step (i =n-1, the MSB):

current_bit is s[i], which is the MSB of m.

If current_bit is '1':

   from the tight state (initial max_tight is 0), option1 is to set the bit (sum becomes 0 + a_i). new_tight is a_i. option2 is sum remains 0, new_loose is 0.

   from the loose state (max_loose is -infinity, so no contribution).

So after this step, max_tight is a_i (if a_i is added), and max_loose is 0.

But if a_i is negative, then setting it would reduce the sum. So in this case, option1 is worse than option2.

Wait, this approach doesn't account for the a_i's sign. Because in the tight state, if current_bit is '1', we can choose to set or not. If a_i is negative, it's better to not set it. But the code above will add a_i regardless of its value. So the code as written will not work, because it always adds a_i in option1, which is incorrect.

Ah, right! So the mistake in the above approach is that when processing a tight state and current_bit is '1', the code should choose to set the bit only if a_i is positive. Because setting the bit adds a_i to the sum. Otherwise, it's better to not set it.

So the code needs to take into account the a_i's value when deciding whether to set the bit in the tight state.

So for the tight state transitions:

If current_bit is '1', then in option1 (set the bit), we add a_i to the sum. So this is only beneficial if a_i is positive. Otherwise, it's better to not set it.

Similarly, option2 (not set the bit) adds nothing to the sum but allows us to set any lower bits (as loose state).

So for option1, when current_bit is '1':

   sum_tight = max_tight + a_i

But if a_i is negative, setting the bit is worse than not setting it. So in the tight state, when current_bit is '1', the best option is to take the maximum between setting it (if a_i is positive) and not setting it.

Thus, the code for the tight state transitions when current_bit is '1' should be:

option1: set the bit (sum += a_i). new_tight_sum = max_tight + a_i. Only beneficial if a_i is positive. Otherwise, setting it would decrease the sum.

But since in the tight state, setting the bit is allowed (since m's bit is 1), but the decision depends on a_i's value.

So, in this case, when current_bit is '1' and the state is tight:

   option1: sum is max_tight + a_i (if a_i is positive, this is better; else, worse than not setting)

   option2: sum is max_tight (but state becomes loose)

But we have to choose the maximum of the two options. So the code would have:

temp_set = max_tight + a_i if a_i > 0 else max_tight

Wait no. Wait in option1, even if a_i is negative, setting the bit adds a_i, but the sum would decrease. So in this case, it's better to not set the bit (option2).

But how to model this in the code.

Wait, the correct way is to compare the two options and choose the maximum between them.

So for tight state and current_bit is '1':

   option1_sum = max_tight + a_i (whether a_i is positive or not)

   option2_sum = max_tight (since we don't set the bit)

   best_option = max(option1_sum, option2_sum)

   But option1 leads to new_tight = True (since we set the same as m's bit)

   option2 leads to new_loose = True.

Thus, for option1, if we choose to set the bit, the new state is tight.

For option2, not setting the bit, the new state is loose.

So the code should be:

if current_bit == '1':

   # option1: set the bit (state remains tight)

   new_tight_candidate = max_tight + a_i

   new_tight = max(new_tight, new_tight_candidate)

   # option2: don't set the bit (state becomes loose)

   new_loose_candidate = max_tight

   new_loose = max(new_loose, new_loose_candidate)

But this ignores the possibility that a_i is negative. For example, if a_i is negative, setting the bit would result in a smaller sum than not setting. So, in this case, option2 is better.

But how to model this in the code. Because in the code above, option1 is to add a_i regardless of its value.

Ah, so this is the problem. The code as written would add a_i even if it's negative, leading to a worse sum.

Thus, the code needs to decide whether to set the bit when possible (current_bit is 1), but only if it's beneficial.

So for tight state and current_bit is '1':

   if a_i > 0:

       option1_sum = max_tight + a_i

       new_tight = max(new_tight, option1_sum)

       option2_sum = max_tight

       new_loose = max(new_loose, option2_sum)

   else:

       option1_sum = max_tight + a_i (which is worse than max_tight)

       option2_sum = max_tight

       new_loose = max(new_loose, option2_sum)

       new_tight = max(new_tight, option1_sum) (but this would be worse than option2)

But how to handle this in code.

Alternatively, for tight state and current_bit '1', the best option is to choose between setting (sum + a_i) and not setting (sum) whichever is larger.

So the code should compute both options and take the maximum for the new state.

But then, the new states will have different tight/loose status.

For example:

When tight, current_bit is '1':

   setting the bit gives new_tight = sum + a_i, and state remains tight.

   not setting gives sum remains, state becomes loose.

So in the code, for the new_tight, the only contribution is from setting the bit. For the new_loose, the contribution is from not setting the bit.

But in terms of maximum sum, we have to consider which option gives a higher sum.

But the code currently adds both options, but without considering a_i's value.

So for example, if a_i is negative:

   setting the bit would give sum + a_i (which is less than sum)

   not setting gives sum (max_tight), but state becomes loose.

Thus, for tight state, current_bit is '1':

   option1_sum = max_tight + a_i

   option2_sum = max_tight

   new_tight would take option1_sum if it's better than previous options for new_tight.

   new_loose would take option2_sum if it's better than previous options for new_loose.

But the code as written adds both options, regardless of a_i's value.

Thus, the code will choose the better of the two options.

But how does that work?

For example, if a_i is positive:

   option1_sum is better than option2_sum.

   So new_tight will be option1_sum.

   new_loose will be option2_sum.

But since a_i is positive, setting the bit is better. So new_tight becomes option1_sum, and new_loose can be option2_sum (but only if it's better than other options).

But for the tight state, the new_tight is the maximum of all possible ways to remain tight. So in this case, option1 is the only way to stay tight. So new_tight is option1_sum.

If a_i is negative:

   option1_sum is worse than option2_sum.

   So new_tight will take option1_sum (since that's the only way to stay tight, but sum is worse), but new_loose will take option2_sum.

But why would we want to choose to stay tight in this case?

Because perhaps, even though the current bit's a_i is negative, by staying tight, we can set higher a_i's in the next bits. But in this case, since we're processing the bits from highest to lowest, there are no higher bits left. So for the current bit i, which is the highest bit, the code would process it, and the next bits are lower.

Wait, no. The processing is from highest to lowest. So after processing the current bit (i), the next bit is i-1, which is lower.

So, for example, if i is the MSB (n-1), after processing it, the next bits are lower.

If in the MSB, the a_i is negative, then setting it would reduce the sum, but not setting it would allow us to set the lower bits (which may have positive a_i's) without constraints.

Thus, in this case, the optimal choice is to not set the bit (even though m's bit is 1), and take the sum max_tight (which is 0 initially), and then in the loose state, set lower bits with positive a_i.

But according to the code's current approach, for tight state and current_bit '1', the code would compute both options, and the new_tight and new_loose would take the maximum.

Thus, for the case where a_i is negative:

   option1_sum = 0 + (-5) = -5.

   option2_sum = 0.

   So new_tight would be -5 (if no other options contribute), and new_loose would be 0.

But in the next steps, when processing lower bits, the loose state would allow setting any a_i positive.

Thus, the code would proceed to choose for new_loose the sum of 0 plus any positive a_i's.

But if a_i is negative, setting the bit would decrease the sum. So the code's current approach would automatically choose not to set it (since the option to not set it gives higher sum).

Thus, the code as written would handle this case correctly.

So perhaps the code doesn't need to explicitly check whether a_i is positive. Because the maximum between option1_sum and option2_sum would naturally choose the better option.

But wait, in the code, when tight state and current_bit is '1':

   new_tight is updated with option1_sum (sum_tight + a_i), and new_loose is updated with option2_sum (sum_tight).

But what if a_i is negative?

In that case, option1_sum is sum_tight + a_i (which could be less than sum_tight). But the code would still add it to new_tight. Which would be worse than the previous value of new_tight.

For example, initially, max_tight is 0.

If a_i is -5:

   option1_sum = 0 + (-5) =-5.

   new_tight would be max(-inf, -5) →-5.

   option2_sum is 0.

   new_loose is max(-inf, 0) →0.

So for the next step, the max_loose is 0.

Thus, when processing the next bits, the loose state can choose to add a_i if it's positive.

This seems correct.

So the code's current approach of adding both options and taking the maximum is correct.

Thus, the code as written is correct, even if a_i is negative. Because the maximum between the two options (set or not) is taken.

But wait, the code for the tight state is:

if current_bit == '1':

   new_tight_candidate = max_tight + a_i

   new_tight = max(new_tight, new_tight_candidate)

   new_loose_candidate = max_tight

   new_loose = max(new_loose, new_loose_candidate)

else:

   new_tight_candidate = max_tight

   new_tight = max(new_tight, new_tight_candidate)

So for current_bit '1', the code adds the option to set the bit (sum increases by a_i, state remains tight) and option to not set (sum remains, state becomes loose).

The code then takes the maximum between existing new_tight and the candidate.

But in the case where a_i is negative, the new_tight_candidate (sum + a_i) will be worse than the previous new_tight (which may have been set to sum from other transitions). However, in this case, for the first bit (MSB), new_tight is initially -infinity, so new_tight_candidate would be the first option. For example, initial max_tight is 0.

So the code would add new_tight_candidate (0 + a_i) to new_tight, and new_loose_candidate (0) to new_loose.

But if a_i is negative, then new_tight_candidate is 0 + (negative) → negative. new_loose_candidate is 0. Thus, new_loose becomes 0.

In the next steps, when processing lower bits, the loose state can add any positive a_i's.

Thus, this approach is correct.

Thus, the code doesn't need to explicitly check if a_i is positive. The maximum between the options will automatically choose the better path.

Now, the code for the loose state:

In the loose state, for each bit i, we can choose to set it if a_i is positive. So the sum increases by max(a_i, 0).

Thus, the code for the loose state transition is:

new_loose_candidate = max_loose + max(a_i, 0)

new_loose = max(new_loose, new_loose_candidate)

Thus, this correctly adds a_i to the sum if it's positive.

Now, putting it all together.

The steps are:

Initialize max_tight = 0 (sum is 0, state is tight)

max_loose = -infinity (state is loose, sum is impossible)

For each i from n-1 downto 0:

   current_bit = s[i]

   a_i = a[i]

   new_tight = -infinity

   new_loose = -infinity

   # handle transitions from tight state
   if current_bit == '1':
       # option1: set the bit (sum += a_i), state remains tight
       temp_tight = max_tight + a_i
       if temp_tight > new_tight:
           new_tight = temp_tight
       # option2: don't set the bit (sum remains), state becomes loose
       temp_loose = max_tight
       if temp_loose > new_loose:
           new_loose = temp_loose
   else:
       # current_bit is 0. Must not set the bit. sum remains, state remains tight
       temp_tight = max_tight
       if temp_tight > new_tight:
           new_tight = temp_tight

   # handle transitions from loose state
   temp_loose = max_loose + max(a_i, 0)
   if temp_loose > new_loose:
       new_loose = temp_loose

   # update the max_tight and max_loose for next iteration
   max_tight, max_loose = new_tight, new_loose

At the end, the maximum sum is the maximum between max_tight and max_loose.

Wait, but what about cases where after processing all bits, the max_loose is higher than max_tight?

Yes. So the final answer is the maximum of max_tight and max_loose.

But how to handle the initial conditions.

Initially, max_loose is -infinity. So for the first iteration, transitions from loose state are not possible (since max_loose is -infinity plus anything is still -infinity, which is worse than other options).

Thus, the code correctly builds the possible sums.

Testing with the first sample:

Sample 1:

n=2

a = [3,8]

s= '10' → m is s[0] = '1' (LSB, 2^0), s[1] = '0' (MSB, 2^1). So m is 1*1 + 0*2 =1.

Processing i=1 (MSB) first.

current_bit is '0'.

a_i is a[1] =8.

For tight state:

current_bit is '0', so must not set. sum remains 0. new_tight is 0.

For loose state: max_loose is -infinity. So no contribution.

So after i=1:

max_tight =0.

max_loose remains -infinity.

Next, process i=0 (LSB).

current_bit is '1'.

a_i is 3.

For tight state:

current_bit is '1'.

option1: set it. sum is 0 +3=3. state remains tight.

option2: don't set. sum remains 0. state becomes loose.

new_tight is 3.

new_loose is 0.

For loose state:

max_loose is -infinity. So contribution is -inf + max(3,0) = -inf. new_loose remains 0.

So after processing i=0:

max_tight =3.

max_loose = max(0, -inf+3) =0.

The final maximum is max(3, 0) =3. Which matches the sample.

Another test case: sample 2.

Sample 2:

n=5

a = [17, 0,10,2,1]

binary string '11010' → s[0] =1, s[1]=1, s[2]=0, s[3]=1, s[4]=0.

Processing bits from i=4 downto 0.

m is sum 2^0*1 + 2^1*1 + 2^2*0 + 2^3*1 + 2^4*0 →1+2+0+8+0=11.

So m is 11.

a is [17,0,10,2,1].

The bits are processed in order i=4 (s[4]='0'), i=3 (s[3]='1'), i=2 (s[2]='0'), i=1 (s[1]='1'), i=0 (s[0]='1').

Let's walk through the code.

Initial: max_tight =0, max_loose =-inf.

Processing i=4 (current_bit '0', a_i=1):

Tight transitions:

current_bit is '0'. So must not set. sum remains 0. new_tight =0.

Loose transitions:

max_loose is -inf. no change.

So after i=4:

max_tight=0, max_loose=-inf.

Processing i=3 (current_bit '1', a_i=2):

Tight transitions:

current_bit is '1'.

option1: set bit. sum=0+2=2. new_tight=2.

option2: don't set. sum=0. new_loose=0.

Loose transitions:

max_loose is -inf. add max(2,0)=2. But sum is -inf +2 → -inf. no contribution.

So new_loose for this step is max(0 (from option2), -inf) →0.

So after i=3:

max_tight=2, max_loose=0.

Processing i=2 (current_bit '0', a_i=10):

Tight transitions:

current_bit '0'. must not set. sum remains 2. new_tight=2.

Loose transitions:

max_loose is 0. add max(10,0) =10. sum becomes 0+10=10. new_loose=10.

So after i=2:

max_tight=2, max_loose=10.

Processing i=1 (current_bit '1', a_i=0):

Tight transitions:

current_bit '1'.

option1: set bit. sum=2+0=2. new_tight=2.

option2: don't set. sum=2. new_loose=2.

Loose transitions:

max_loose=10. add max(0,0)=0. sum becomes 10+0=10. new_loose is max(2,10) →10.

So after i=1:

max_tight=2, max_loose=10.

Processing i=0 (current_bit '1', a_i=17):

Tight transitions:

current_bit '1'.

option1: set. sum=2+17=19. new_tight=19.

option2: don't set. sum=2. new_loose=2.

Loose transitions:

max_loose=10. add max(17,0)=17. sum becomes 10+17=27. new_loose = max(2,27) →27.

So after i=0:

max_tight=19, max_loose=27.

The final maximum is max(19,27) =27, which matches the sample.

Thus, the code works.

Now, implement this in Python.

But need to read the input correctly.

The binary string is given as a sequence of digits. So for example, the third line in the input is a string like '11010'.

So, the steps for reading input are:

Read n.

Read the array a as a list of integers.

Read the binary string s.

Process the bits in reverse order (from s[0] to s[n-1], but processing from i =n-1 downto 0).

Wait no. Wait the binary string is s_0 s_1 ... s_{n-1}, which corresponds to bits 0 (LSB) to n-1 (MSB). So to process bits from MSB to LSB, the code needs to process the string in reverse order. For example, for the string '10', s is ['1', '0'], but processing from i=1 downto 0 (n=2).

Thus, in Python, the code would loop for i in range(n-1, -1, -1).

But the binary string is read as a string, and for each i in 0..n-1, s[i] is the character.

But for processing from MSB to LSB, the code needs to process i from n-1 downto 0.

Thus, in code:

s = input().strip()

for i in reversed(range(n)):

   current_bit = s[i]

   a_i = a[i]

Thus, this correctly processes the bits from MSB to LSB.

Now, the code:

Read n.

Read a as list of integers.

Read s as a string.

Initialize max_tight =0, max_loose = -infinity.

Loop for i in reversed(range(n)):

   current_bit = s[i]

   a_i = a[i]

   new_tight = -infinity

   new_loose = -infinity

   # tight transitions

   if current_bit == '1':

       # option1: set the bit, sum increases by a_i, state remains tight

       candidate = max_tight + a_i

       if candidate > new_tight:

           new_tight = candidate

       # option2: don't set, sum remains, state becomes loose

       candidate = max_tight

       if candidate > new_loose:

           new_loose = candidate

   else:

       # current_bit is 0: can't set, sum remains, state remains tight

       candidate = max_tight

       if candidate > new_tight:

           new_tight = candidate

   # loose transitions

   candidate = max_loose + max(a_i, 0)

   if candidate > new_loose:

       if new_loose < candidate:

           new_loose = candidate

   # update the variables

   max_tight, max_loose = new_tight, new_loose

At the end, output the maximum between max_tight and max_loose.

But in Python, initializing max_loose as negative infinity.

Now, considering edge cases.

For example, when m is 0. Then, the only possible x is 0. So the sum is 0.

Another case: all a_i are negative. Then the best sum is 0 (x=0).

The code should handle this.

Another case: a_i is all positive. Then the code should set as many bits as possible without exceeding m.

Thus, the code seems correct.

Now, implement this in Python.

But wait, in the code, a[i] is taken from the list a. The list a is read in the order a_0, a_1, ..., a_{n-1}, which correspond to bits 0 to n-1. Which is correct.

Thus, the code should work.

Now, let's write the code.

Read n.

Read a: list(map(int, input().split())).

Read s: input().strip()

Initialize max_tight =0.

max_loose = -infinity.

Loop i from n-1 downto 0:

   current_bit = s[i]

   ai = a[i]

   new_tight = -inf

   new_loose = -inf

   # process tight transitions

   if current_bit == '1':

       # option1: set, tight remains

       temp_tight = max_tight + ai

       if temp_tight > new_tight:

           new_tight = temp_tight

       # option2: not set, loose

       temp_loose = max_tight

       if temp_loose > new_loose:

           new_loose = temp_loose

   else:

       # current_bit is 0, can't set

       temp_tight = max_tight

       if temp_tight > new_tight:

           new_tight = temp_tight

   # process loose transitions

   temp_loose = max_loose + max(ai, 0)

   if temp_loose > new_loose:

       new_loose = temp_loose

   # update

   max_tight, max_loose = new_tight, new_loose

At the end, print(max(max_tight, max_loose)).

But in Python, the initial max_loose is set to -inf, which is correct.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    import sys
    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    s = input_stream.readline().strip()
    
    max_tight = 0
    max_loose = -float('inf')
    
    for i in reversed(range(n)):
        current_bit = s[i]
        ai = a[i]
        new_tight = -float('inf')
        new_loose = -float('inf')
        
        # Process tight transitions
        if current_bit == '1':
            # Option 1: set the bit, remains tight
            candidate_tight = max_tight + ai
            if candidate_tight > new_tight:
                new_tight = candidate_tight
            # Option 2: not set, becomes loose
            candidate_loose = max_tight
            if candidate_loose > new_loose:
                new_loose = candidate_loose
        else:
            # Current bit is 0, cannot set, remains tight
            if max_tight > new_tight:
                new_tight = max_tight
        
        # Process loose transitions
        candidate_loose = max_loose + max(ai, 0)
        if candidate_loose > new_loose:
            new_loose = candidate_loose
        
        max_tight, max_loose = new_tight, new_loose
    
    print(max(max_tight, max_loose), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
17 0 10 2 1
11010
""",
            "output": \
"""\
27
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

Sample 2:

As discussed, code works.

Edge case: all a_i are negative.

For example, n=1, a=[-5], s='0'.

m=0. Only x=0. sum 0.

Code:

Processing i=0:

current_bit '0'.

tight transitions: can't set. new_tight is 0.

loose transitions: max_loose is -inf. no change.

Final max is max(0, -inf) =0.

Another case: n=1, a=[-5], s='1'.

m=1. x can be 0 or 1.

sum for x=0 is 0. x=1: sum -5. So the maximum is 0.

Code:

i=0:

current_bit '1'.

tight transitions:

option1: 0 + (-5) =-5 → new_tight=-5.

option2: new_loose=0.

loose transitions: max_loose is -inf. no contribution.

So new_loose is 0.

Final max is max(-5,0) →0.

Thus, code works.

Thus, the code seems correct.
</think>

```python
def main():
    import sys
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    s = sys.stdin.readline().strip()
    
    max_tight = 0
    max_loose = -float('inf')
    
    for i in reversed(range(n)):
        current_bit = s[i]
        ai = a[i]
        new_tight = -float('inf')
        new_loose = -float('inf')
        
        # Process tight transitions
        if current_bit == '1':
            # Option 1: set the bit, remains tight
            candidate_tight = max_tight + ai
            if candidate_tight > new_tight:
                new_tight = candidate_tight
            # Option 2: not set, becomes loose
            candidate_loose = max_tight
            if candidate_loose > new_loose:
                new_loose = candidate_loose
        else:
            # Current bit is 0, cannot set, remains tight
            if max_tight > new_tight:
                new_tight = max_tight
        
        # Process loose transitions
        candidate_loose = max_loose + max(ai, 0)
        if candidate_loose > new_loose:
            new_loose = candidate_loose
        
        max_tight, max_loose = new_tight, new_loose
    
    print(max(max_tight, max_loose))
    
if __name__ == "__main__":
    main()
```
