<think>
Okay, so I need to solve this problem where Alice and Bob are distributing pie slices, and they use this decider token. The goal is to compute the maximum amount each can get when both play optimally. Let's see how to approach this.

Hmm, the problem says that for each slice, the decider gives the current slice to one person and the token to the other. And the decision has to be made optimally to maximize their own totals. So this feels like a dynamic programming problem. Because at each step, the decision affects the remaining steps, and we need to track the state.

Wait, the state here probably depends on two things: which slice we're currently deciding (the index), and who has the decider token at that step. Because the choice made at each step affects the next state. So for each position i in the pie slices, and for a state where either Alice or Bob is the decider, we can model the maximum difference the current player can achieve.

But how do we model the state transitions? Let's think. For each step i (like, the i-th slice in the order), if the current decider is, say, Bob, then he can choose to take the current slice and pass the decider to Alice, or give the slice to Alice and keep the decider himself. Wait, no. Wait, according to the problem statement: the decider gives the next slice to one participant and the decider token to the other. So when you give the slice to someone, you pass the token to the other person.

So the current decider picks who gets the current slice. Then, the other person (the one who received the slice) gets the decider token for the next step. Wait, no. Let me read again: the decider token is passed to the other participant. Wait, no. The problem says, "the other participant". So when the decider gives the next slice to one, they give the decider token to the other. So for example, if Bob is the decider for the current slice, he can choose to give the slice to himself (Bob) and give the token to Alice. Or give the slice to Alice and give the token to Bob. Wait, no. The problem says, "give the next slice of pie to one of the participants, and the decider token to the other participant." So when the decider gives the slice to one person, the token goes to the other. So the next decider is the other person.

So the next state's decider is the other person. So the current decider has two options: assign the current slice to themselves, and then the next decider is the other. Or assign the slice to the other, and then the next decider is themselves? Wait, no. Let me rephrase: when the current decider is, say, Bob, he gives the slice to Alice or Bob, and gives the decider token to the other. So if Bob gives the slice to himself, then the next decider is Alice. Because the token is given to the other participant. Wait, the other participant of the two? So when you give the slice to yourself, the other participant is the one who didn't get the slice. So in that case, the decider token is passed to the other participant. For example, current decider is Bob. He gives the current slice to himself (Bob) → the other participant is Alice, so the token goes to Alice. Or he gives the slice to Alice → the other participant is Bob, so the token goes to Bob. Wait, no. Let's think again. The token is given to the other participant of the current decision. So when the decider gives the slice to one, the token is given to the other. So, if the current decider is Bob and he gives the slice to Alice, then the token is given to Bob (the other participant). Wait, that can't be right. Because the two participants are Alice and Bob. So when the decider is Bob, he gives the slice to one (say, himself), then the other participant (Alice) gets the token. Or if he gives the slice to Alice, then the other participant (Bob) gets the token. Wait, that can't be. Because in that case, if he gives the slice to Alice, the token would go to Bob again. So he can keep the token for himself. That seems to allow the same person to make all decisions, which can't be right.

Wait, maybe I got this wrong. Let me read the problem statement again:

"the decider token will give the next slice of pie to one of the participants, and the decider token to the other participant."

Ah, right. So when the current decider gives the next slice to one person (could be themselves or the other), the other person (the one not getting the slice) receives the decider token. Wait, no: the person who gives the slice gives it to one participant, and the other participant gets the token. Wait, maybe the slice is given to one, and the token is given to the other. So the next decider is the other participant, regardless of who gets the slice.

Wait, no. Let me think: when you give the slice to someone, the other person gets the token. So, for example, if the current decider is Bob, and he gives the slice to Alice, then the token goes to Bob's other participant, which is Alice? No, that can't be. Wait, maybe the way to think is that the decider gives the slice to either themselves or the other, and the decider token is given to the other. So, regardless of who gets the slice, the token is given to the other participant.

Wait, no. Let me rephrase. The decider gives the slice to one (could be themselves) and the token to the other. So for example:

Current decider is Bob. He can choose to:

- Assign the current slice to himself. Then, the decider token for the next round is given to Alice.

OR

- Assign the current slice to Alice. Then, the decider token for the next round is given to Bob.

Wait, no. Because the other participant is the one not given the slice. Wait, no. The problem says, "the other participant" here refers to the person not given the slice. So if the current decider is Bob and he gives the slice to himself, then the other participant is Alice. So the token goes to Alice. If he gives the slice to Alice, then the other participant is Bob (since he was the one who gave it to Alice), and the token goes to Bob. Wait, no. Because in that case, when Bob gives the slice to Alice, the token is given to the other participant, which would be Bob. So the next decider would be Bob again. That can't be right, because then Bob could keep the token forever. But that's not possible because the token alternates based on the decision.

Wait, maybe the decider gives the slice to one, and the token to the other. So the next decider is the person who received the token. So for example:

If current decider is Bob. He can choose between two options:

1. Give the slice to Bob, and the token to Alice. Next decider is Alice.

OR

2. Give the slice to Alice, and the token to Bob. Next decider is Bob.

Wait, that makes more sense. So when you give the slice to yourself, the token goes to the other. When you give the slice to the other, the token goes to yourself. So in either case, the next decider is the other person.

Wait, no. Wait, the problem statement says: "the decider token will give the next slice of pie to one of the participants, and the decider token to the other participant." So the decider gives the slice to one and the token to the other. So the 'other participant' here is the other person involved in the transaction. So for example, if the current decider is Bob, then when he gives the slice to Alice, the token is given to the other participant (Bob himself). Or when he gives the slice to himself, the token is given to Alice.

Ah, right. So the decider (current holder) gives the slice to either themselves or the other, and the token goes to the other. So the next decider is the person who received the token, which is the other participant.

So for example:

Current decider is Bob. He can:

Option 1: Take the slice (Bob gets the slice), and give the token to Alice. So next decider is Alice.

Option 2: Give the slice to Alice, and give the token to Bob. Wait, no. Because in this case, the 'other' is Bob. Wait, no. Let's clarify. When the decider gives the slice to a participant (could be themselves), the token is given to the other participant. So the 'other' is the one not given the slice. So:

If the current decider is Bob, and he gives the slice to Alice, then the other participant is Bob. So the token goes to Bob. So next decider is Bob.

Wait, that's possible. So if Bob gives the slice to Alice, then the next decider is Bob again. So he can retain the token. But how? Let me think.

Wait, the problem says, the decider gives the next slice to one participant and the decider token to the other. So for example, if the current decider is Bob, and he gives the slice to Alice, then the token is given to the other participant (Bob, since Alice is the one receiving the slice). So the next decider is Bob again. That's possible, which would allow Bob to retain the token if he gives the slice to Alice.

But then, Bob can make all the decisions. For example, if he gives all slices to Alice and keeps the token, then he can decide each step. But that's not allowed, because each step the decider can choose to pass the token.

Wait, perhaps I'm misunderstanding the problem statement.

The problem statement says: "give the next slice of pie to one of the participants, and the decider token to the other participant." So when the current decider gives the slice to a participant (either himself or the other), he must give the token to the other participant. So the 'other participant' here refers to the person who did not receive the slice. For example:

If current decider is Bob. He gives the slice to himself. Then, the other participant (Alice) gets the token. So next decider is Alice.

If he gives the slice to Alice, then the other participant (Bob) gets the token. So next decider is Bob again.

So in this case, when Bob gives the slice to Alice, he retains the token. Because the other participant is Bob (since Alice was the one receiving the slice), so the token goes to Bob. Wait, that's not possible. Because when Bob gives the slice to Alice, the other participant is Bob. So the token is given to Bob. So next decider is Bob again.

So this way, if Bob gives the slice to Alice, he keeps the token. So he can choose to give the next slice again. But that would allow him to make consecutive decisions, which might be beneficial.

But the players are trying to maximize their own total. So Bob would make the choice that maximizes his total. So in each step, the decider has two choices: take the slice and pass the token, or give the slice and keep the token (if possible).

Wait, no. Let's take the first example given:

3

141 592 653

The initial decider is Bob.

In the first step, Bob has to decide. The note says Bob takes 141 for himself, gives the token to Alice. So next decider is Alice.

Then Alice gives 592 to Bob, and keeps the token (so next decider is Alice again? Wait, no. Because when Alice gives the slice to Bob, the other participant is Alice, so the token goes to her. So the next decider would be Alice. Then she gives 653 to herself, passing the token to Bob. But after all slices are done, the sum is 653 for Alice and 141+592=733 for Bob.

So the process is:

Bob (decider) → gives himself 141, token to Alice.

Alice (decider) → gives 592 to Bob, token to Alice (because when she gives the slice to Bob, the other participant is Alice, so token goes to Alice). So next decider is Alice again.

Then Alice (decider) → gives herself 653, token to Bob.

So the next decider is Bob, but there are no slices left.

So in this scenario, Alice can make two consecutive decisions. So the token can be kept by the same person if the decision is to give the slice to the other.

So this implies that the state transitions can allow the same person to hold the token again. So the state transitions are:

For each step, the current decider can choose to:

1. Take the current slice, and the next decider is the other person.

OR

2. Give the current slice to the other, and the next decider is the current decider.

Wait, that's the key. So when you take the slice (option 1), the next decider is the other. When you give the slice (option 2), the next decider is yourself.

Because the token is given to the other participant. So if you take the slice, the other participant (the one not getting the slice) gets the token. If you give the slice to the other, then the other participant is you (since you are the one not getting the slice), so the token goes to you. Wait, I'm getting confused here.

Alternatively, perhaps the correct way to model it is:

At each step, the decider can choose to take the slice. Then, the next decider is the other player. Or, give the slice to the other player, and the next decider is the other player.

Wait, no. Because in the first example, when Alice is the decider, she gives the slice to Bob. So the next decider is Alice again. Because according to the note, after that, she can take the next slice for herself.

So when you give the slice to the other player, the next decider is you again. So how does that work?

Hmm, perhaps the correct way to model the next decider is: when the current decider gives the slice to someone (could be themselves or the other), the next decider is the other person. Because the token is passed to the other participant.

Wait, but according to the problem statement, the decider gives the slice to one and the token to the other. So the next decider is the other participant. So regardless of who they give the slice to, the next decider is the other participant.

Wait, maybe the problem's wording is that the decider gives the slice to one, and the token to the other. So for example:

If current decider is Bob, and he gives the slice to himself, then the token is given to Alice (the other participant). So next decider is Alice.

If he gives the slice to Alice, the token is given to Bob (the other participant?), which would be himself? That doesn't make sense. Wait, maybe the other participant is the one not receiving the slice. So when the decider gives the slice to themselves, the other participant is the other person (Alice). So the token goes to Alice. When the decider gives the slice to Alice, the other participant is Bob (the decider), so the token goes to Bob.

Wait, that can't be right. Because if Bob gives the slice to Alice, the token would go to Bob, making him the decider again. Then he can give the next slice to Alice again, and keep the token. But in the first example, after Bob gives himself the first slice, the token goes to Alice. Then Alice gives Bob the next slice, and the token goes to Bob again. Then Alice can't make the next decision. But according to the note, after the second step, Alice is the decider again.

Wait, this suggests that my understanding is wrong. Let's re-examine the first example's note:

In the first example, after Bob gives himself the first slice, the decider token goes to Alice. Then Alice gives the 592 slice to Bob. Then she keeps the decider token. So next step, she is the decider again. How?

Ah, this implies that when Alice gives the slice to Bob, the decider token is given to herself. So the next decider is Alice.

But according to the problem statement, when you give the slice to a participant, you give the token to the other. So when Alice is the decider and gives the slice to Bob, the other participant is Alice. So the token is given to Alice. So next decider is Alice.

So the rule is:

When the current decider is X, and they give the slice to Y (could be X or the other), then the token is given to Z, where Z is the other participant of Y. Wait, maybe not. Let's think: the other participant is the one not receiving the slice. So if you give the slice to yourself (X), then the other is Y (the other person). If you give the slice to Y (the other), then the other is X (the decider). So the token is given to the other of the slice's recipient.

So, the next decider is the other of the slice's recipient.

So for example:

Current decider: X.

Option 1: X gives slice to X → recipient is X, other is Y. So next decider is Y.

Option 2: X gives slice to Y → recipient is Y, other is X. So next decider is X.

Wait, this makes sense. So when the current decider (X) gives the slice to themselves, the next decider is Y. When they give the slice to Y, the next decider is X. Because the token is given to the other participant of the slice recipient.

So this way, when X gives the slice to Y, the token is given to X (since Y is the recipient, the other is X). So next decider is X.

Wait, no. The other of the recipient is X. So the token is given to X. So next decider is X. So when X gives the slice to Y, the next decider is X again.

So in that case, the same decider can make consecutive decisions. But how?

But according to the note in the first example, after Alice gives the slice to Bob (step 2), the next decider is Alice again. Because she gives the slice to Bob (so the recipient is Bob), the other is Alice. So the token is given to Alice. So she is the decider again.

Ah, so the next decider is the other of the recipient. So when the current decider is X and gives the slice to Y, the next decider is X (since Y's other is X). So X becomes the decider again.

Wait, perhaps this is the correct model.

So for each step:

Current decider is D.

D can choose to assign the current slice to A or B.

But according to the problem statement, the decider gives the slice to one and the token to the other. So the 'other' here is the other participant in the slice assignment.

Wait, maybe the token is given to the other participant of the current decision. So when D gives the slice to X (could be D or the other), the token is given to the other participant (the one not receiving the slice). So the next decider is that other participant.

So in code terms:

next_decider = other_participant_of(slice_recipient)

So if current decider is D, and slice is given to X, then next decider is the other of X.

So for example:

D is Bob. He gives the slice to Bob (X = Bob). The other is Alice. So next decider is Alice.

If D is Bob and gives slice to Alice (X = Alice), other is Bob. So next decider is Bob.

So in this case, when a decider gives the slice to the other person, the next decider is themselves again.

Wait, that's possible. So in the first example, after Bob gives the slice to himself, the next decider is Alice. Then Alice gives the slice to Bob, so next decider is Alice (since Bob is the recipient, other is Alice → next decider is Alice). Then Alice gives herself the slice, so next decider is Bob (other of Alice is Bob).

But according to the example, after the third step, Alice is the decider again. Let's see:

Step 1: Bob (decider) → gives slice to Bob. Next decider is Alice.

Step 2: Alice (decider) → gives slice to Bob. Next decider is Alice (since Bob is the recipient, other is Alice. Wait, no. The recipient is Bob. The other participant of the recipient (Bob) is Alice. So next decider is Alice.

So Alice is the decider again for step 3.

Step3: Alice (decider) → gives slice to herself. Next decider is Bob.

So the three slices are assigned as Bob, Bob, Alice. Sum Bob: 141+592=733, Alice: 653. Which matches the example.

So the model here is that when the decider gives the slice to someone, the next decider is the other participant of that someone.

So the next decider is determined based on who gets the current slice.

Thus, the state transitions are:

For each slice i, and current decider D (could be Alice or Bob), the decider can choose to take the slice (for themselves), in which case the next decider is the other of D. Or give the slice to the other, in which case the next decider is D.

Wait, no. Let me rephrase.

If the current decider is D (either Alice or Bob), and they give the slice to X (D or the other):

- If X is D (they take the slice), then the next decider is the other of D. Because the other of X (D) is the other participant.

- If X is the other (they give the slice to the other), then the next decider is the other of X (which is D). So next decider is D again.

So for example:

D is Bob.

Case 1: Take the slice. Next decider is Alice.

Case 2: Give slice to Alice. Next decider is Bob.

So in this case, the next decider is determined by the choice of who receives the slice.

This is the correct model.

So the DP state is:

dp[i][d] = maximum difference (current decider's total - the other's total) that the decider can achieve from slice i onwards, given that the current decider is d (0 for Alice, 1 for Bob, perhaps).

But wait, the players are trying to maximize their own total. So when the decider is making a decision, they will choose the option that gives them the maximum possible total, considering the other player's optimal play.

So for the DP approach, the state is the current slice index and the current decider.

At each state, the decider can choose to take the slice, add it to their total, and the next state is i+1 with the other decider. Or give the slice to the other, subtract it from their total (since the other gets it), and the next state is i+1 with the same decider.

Wait, but how to model this.

Alternatively, the DP[i][d] can represent the maximum possible difference (current decider's total minus the other's total) that the decider can obtain from the slices starting at index i onwards.

So for each i and d (decider), the decider can choose to take the slice, add its value to their own total, and then the next decider is the other. So the next state is DP[i+1][other_d], but since the next decider is the other, their optimal play will subtract from the current difference.

Alternatively, when the current decider (d) takes the slice, the difference becomes slice[i] + (the next state's difference from the other's perspective). Because the next decider is the other, and they will choose the optimal option for their own benefit.

Wait, maybe the DP needs to represent the maximum possible difference (from the current decider's perspective) that can be achieved from slice i onward.

Let's think recursively. Suppose the current decider is d. For slice i, they can choose to take it, leading to the next decider being the other. The other will then choose optimally, leading to a difference (from the current decider's perspective) of slice[i] - result of the next state (since the next state is the other's turn, and their result is the difference from their perspective, which is the opposite of the current decider's).

Alternatively, the DP[i][d] is the maximum possible (current decider's total - the other's total) that can be achieved from slice i onward, given that d is the current decider.

So for each i and d, the decider can choose between:

1. Take the current slice (add to their total), then the next decider is the other. The other will then make choices to maximize their own difference, which is equivalent to the current decider's difference being (current slice) - next state's difference (since the next state is from the other's perspective). So the total difference is (slice[i] + next_diff), where next_diff is the result of the next state, but since the other is choosing, it's the maximum between the two options. Wait, perhaps not.

Wait, when the current decider takes the slice, the difference becomes slice[i] plus the difference from the next state (since the next state is handled by the other decider, which will try to maximize their own difference. Since the other's difference is (their total - current decider's total), which is the negative of the current decider's difference. So the next state's result (from the current decider's perspective) would be -DP[i+1][other_d].

So for example, if current decider is d, takes the slice, then the next decider is other_d. The next state's DP[i+1][other_d] gives the maximum difference (other_d's total - d's total). So from d's perspective, the difference is slice[i] - DP[i+1][other_d].

Alternatively, if the current decider gives the slice to the other, then the difference is (the other's slice) which is subtracted from the current difference. Then the next state is handled by the same decider (since the next decider is the same). So the difference would be (-slice[i]) + DP[i+1][d].

Wait, this is getting a bit complicated. Let's model this step by step.

Suppose we have a DP table where dp[i][d] represents the maximum possible difference (current decider's total minus the other's) that can be achieved starting from slice i, given that the current decider is d.

For the current step i, the decider can choose between two options:

Option 1: Take the slice.

- The current decider's total increases by slice[i].

- The next decider is the other (other_d).

- The next state is i+1, decider is other_d.

The difference contributed by the next state is dp[i+1][other_d], which represents (other_d's total - current decider's total) from that point onwards.

But from the current decider's perspective, their total difference is slice[i] (their gain) minus the difference that the next state will bring. Because whatever difference the next state's decider (other_d) can achieve (which is other_d's total - current decider's total in the next steps) is subtracted from the current gain.

So the total difference for option 1 is slice[i] - dp[i+1][other_d].

Option 2: Give the slice to the other.

- The other's total increases by slice[i], so the current difference is -slice[i].

- The next decider is the current decider (since the other's other is the current decider, so the token is given back to the current decider).

- The next state is i+1, decider is d.

The difference contributed by the next state is dp[i+1][d], which is (d's total minus other's total) from that point onwards.

So the total difference for option 2 is (-slice[i]) + dp[i+1][d].

The current decider will choose the maximum between option 1 and option 2.

So the recurrence is:

dp[i][d] = max( slice[i] - dp[i+1][other_d],   // option 1
                -slice[i] + dp[i+1][d] )       // option 2

The base case is when i == N (all slices processed), dp[N][d] = 0.

So for each i from N-1 down to 0, and for each decider d (0 or 1, representing Alice and Bob), we compute the maximum difference.

Now, the initial decider is Bob (d=1). So the final difference is dp[0][1].

But wait, the problem requires us to output Alice's total and Bob's total.

But the difference (Bob's total - Alice's total) is equal to the DP[0][1]. Because Bob is the initial decider, and the DP returns Bob's total minus Alice's total.

But according to the problem statement, the initial decider is Bob, so the initial state is i=0 (first slice), d=1 (Bob). The DP gives the maximum difference (Bob's total - Alice's) when both play optimally.

Once we have this difference (diff), we can compute Alice's and Bob's totals.

The sum of all slices is S = sum(slices). So:

Bob's total - Alice's total = diff.

Bob's total + Alice's total = S.

So solving these two equations:

Alice's total = (S - diff) / 2

Bob's total = (S + diff) / 2

So the final answer is Alice's total and Bob's total.

Now, the steps to implement this:

1. Read N and the list of slices.

2. Compute the sum S.

3. Implement the DP.

Since N can be up to 50, and for each i and d (0 and 1) we compute the DP, this is manageable. Because 50 slices and 2 states (Alice or Bob as decider) → 100 states. For each state, we compute in O(1) time. So total time is O(N), which is acceptable.

So the plan is to use a memoization DP, or iterative DP.

But in Python, for N=50, even a recursive approach with memoization would work, but an iterative approach is probably better for speed.

Let's think about the iterative approach.

We can create a 2D array (dp) of size (N+1) x 2, initialized to 0 for i=N.

Then, for i from N-1 down to 0:

   for d in 0, 1:

       other_d = 1 - d

       take = slices[i] - dp[i+1][other_d]

       give = -slices[i] + dp[i+1][d]

       dp[i][d] = max(take, give)

So for each i in reverse order.

Once filled, the initial difference is dp[0][1] (since initial decider is Bob, d=1).

Then compute Alice's and Bob's totals.

Now, for the sample input:

Sample 1:

3

141 592 653

S = 141+592+653 = 1386

dp[0][1] is the difference between Bob's and Alice's totals.

In the first example, according to the note, the difference is 733-653 = 80. So dp[0][1] = 80.

Then, Alice's total is (1386 -80)/2 = 1306/2 = 653, Bob's is (1386+80)/2=1466/2=733. Which matches.

So the approach works.

Sample 2:

5

10 21 10 21 10 → sum is 72.

The output is 31 and 41 → sum 72. Difference is 10.

dp[0][1] = 10. So (72-10)/2=31 for Alice, and 41 for Bob.

Yes.

So the DP approach seems correct.

Now, implementing this in Python.

First, read N and the slices.

Then, compute sum_slices.

Then, initialize dp as a 2D array. But since N can be up to 50, we can use a list of lists.

But since for each i, we only need the next i+1's state, we can even optimize space by using two 1D arrays (current and next). But given that N is small (50), it's not necessary. Using a 2D array is acceptable.

So code steps:

Read N.

Read slices as a list.

sum_slices = sum(slices).

Initialize dp as a list of lists. For i from 0 to N, and d in 0 and 1.

But for iterative approach:

We can loop i from N-1 downto 0.

For each i, compute the dp[i][0] and dp[i][1].

So code:

n = int(input())

slices = list(map(int, input().split()))

sum_s = sum(slices)

# Initialize DP table.

dp = [[0]*2 for _ in range(n+1)]  # dp[i][d] for i from 0 to n.

for i in range(n-1, -1, -1):

    for d in range(2):

        other_d = 1 - d

        # Option 1: take the slice.

        # The next state is i+1, decider is other_d.

        take = slices[i] - dp[i+1][other_d]

        # Option 2: give the slice to the other.

        # The next state is i+1, decider is d.

        give = -slices[i] + dp[i+1][d]

        dp[i][d] = max(take, give)

diff = dp[0][1]

alice = (sum_s - diff) // 2

bob = (sum_s + diff) // 2

print(alice, bob)

Wait, but let's test this code with the first sample.

Sample 1:

i=2 (third slice, since slices are 0-based?), but in Python, the slices are [141, 592, 653]. n is 3.

For i in range(2, -1, -1):

i starts at 2 (third slice?), then 1, then 0.

But let's see.

n=3.

slices is [141, 592, 653].

sum_s = 141+592+653=1386.

The dp array is of size n+1 =4. For i=3, dp[i][0] and [1] are 0.

Now, for i=2 (third slice), d in 0 and 1.

For d=0:

other_d=1.

take = 653 - dp[3][1] → 653 -0=653.

give = -653 + dp[3][0] → -653 +0 =-653.

So dp[2][0] = max(653, -653) → 653.

For d=1:

take =653 - dp[3][0] →653-0=653.

give =-653 + dp[3][1] →-653+0= -653.

So dp[2][1] =653.

Then i=1 (second slice).

For d=0:

other_d=1.

take =592 - dp[2][1] →592-653= -61.

give =-592 + dp[2][0] →-592 +653=61.

So max(-61,61) →61. dp[1][0] =61.

For d=1:

take=592 - dp[2][0] →592-653= -61.

give= -592 + dp[2][1] →-592 +653=61.

So max(-61,61) →61. dp[1][1] =61.

Then i=0 (first slice).

d=0:

other_d=1.

take=141 - dp[1][1] →141-61=80.

give= -141 + dp[1][0] →-141+61= -80.

max(80, -80) →80. So dp[0][0] =80.

d=1:

take=141 - dp[1][0] →141-61=80.

give= -141 + dp[1][1] →-141+61= -80.

max(80, -80) →80. So dp[0][1] =80.

So diff is 80. alice = (1386-80)/2 = 1306/2=653. Bob (1386+80)/2=1466/2=733. Correct.

So the code works for the first sample.

Now the second sample:

Sample 2:

5

10 21 10 21 10 → sum 72.

The output is 31 and 41. So difference is 41-31=10. So dp[0][1] =10.

But let's see.

But calculating this code for the second sample would be tedious, but let's assume the code works.

So the code seems correct.

Now, check the code for correctness.

Now, code is written as:

Read n.

Read slices.

sum_s = sum(slices).

Initialize dp as (n+1) x 2 array.

Loop i from n-1 downto 0.

For each d in 0,1.

Compute take and give, etc.

Yes.

So the code should work.

Thus, this is the correct approach.
</think>

```python
n = int(input())
slices = list(map(int, input().split()))
sum_s = sum(slices)
dp = [[0] * 2 for _ in range(n + 1)]

for i in range(n-1, -1, -1):
    for d in range(2):
        other_d = 1 - d
        take = slices[i] - dp[i+1][other_d]
        give = -slices[i] + dp[i+1][d]
        dp[i][d] = max(take, give)

diff = dp[0][1]
alice = (sum_s - diff) // 2
bob = (sum_s + diff) // 2
print(alice, bob)
```