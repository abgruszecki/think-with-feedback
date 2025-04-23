<think>
Okay, let's try to solve this problem. Hmm. So, the problem is about chain letters being sent through a network of friends, and we need to find out how many times the user (person n) receives the letter. The rules are that once a person receives the letter for the first time, they send it to all their contacts. But the user (n) doesn't forward. So the task is to model this process and count how many times the user gets the letter.

First, let's understand the setup. The input is an n x n matrix where each entry f[i][j] tells if i and j are contacts. Since it's symmetric and the diagonals are zero. Person 1 starts sending the letter to all their contacts. Then each person who receives it for the first time sends it to all their contacts. But each time someone sends, their contacts receive a copy. So the user (n) will get a copy every time someone who is connected to them sends the letter, except themselves.

Wait, but the user is person n. So any time a contact of theirs (other than themselves) sends the letter, if they are connected, they'll send a copy. But the user doesn't forward. So the question is, how many times will the user receive the letter.

The key here is that once a person is activated (receives the letter for the first time), they send to all their contacts. So each of their contacts will receive a copy. But this happens once per person when they are activated.

So the process is like a BFS. Person 1 is the initial source. They send to all their contacts. Each of those contacts, upon receiving it for the first time (since you only send once, when you first get it), send to all their contacts. And this repeats. The user (n) will accumulate copies each time someone sends to them. So for each sender that is a contact of the user, if that sender is activated (i.e., receives the letter at some point), then the user gets a copy from them.

Wait, but how does the sending happen? Let's think step by step.

Let's say the process is as follows:

- Person 1 starts by sending the letter to all their contacts. So for each contact j of person 1 (i.e., f[1][j] == '1'), j receives the letter. Then, each of those j's, upon first receipt, sends to all their contacts. So, for example, if j is person 2, and their contacts include person 3 and person n, then when j is activated (when they receive the letter for the first time), they send to all their contacts. So person 3 and person n would receive a copy from j. But for each contact of j, the time when j sends is when j is activated. So if person 3 is activated later (say, by someone else), they will send to their contacts then.

So each person can only send once: when they are first activated. So the copies sent are all at the moment of activation.

Therefore, the user will receive a copy from every contact of theirs (person i) where i is in the BFS tree of activation. Because once person i is activated, they send to all their contacts. If the user is one of i's contacts, then they get a copy.

So the problem reduces to: find all the nodes (people) that are reachable from person 1 (excluding themselves) via the BFS (or any order) of activation, and for each such node, if they are connected to the user (n), then that's a copy. The total count is the number of such nodes.

Wait, but wait: when a person is activated (they receive the letter for the first time), they send to all their contacts. So each contact of theirs will get a copy. So for the user (n), each time a contact of theirs sends (when activated), the user gets a copy. So the answer is the number of contacts of the user (n) that are in the set of activated people (excluding the user themselves, since the user doesn't send).

So the approach is:

1. Find all nodes that are reachable from node 1 (including node 1?), wait no: node 1 is the one who starts the chain. Wait, node 1's first action is to send to all their contacts, which is the first wave. So node 1 is activated, and sends to their contacts. Those contacts are activated when they receive the letter, and send to their contacts. So the activated set is {1} plus all nodes reachable via BFS from the contacts of 1. Because node 1 is the first to send.

Wait, node 1 is the initiator. So when node 1 starts, they send to all their contacts. Those contacts are activated (since they received it for the first time) and then send to their own contacts. So node 1 is the first in the queue, but sends to their contacts. Then each of those contacts is added to the queue (if not already activated), and when processed, send to their contacts.

So the activated set is all the nodes that can be reached through BFS starting from node 1's contacts. Because node 1 is the first to send, their contacts receive it first. Then those contacts send to their contacts (including possibly node 1 again, but node 1 is already activated, so they don't send again).

Wait, but node 1 is part of the process. Let's take the first example:

Sample Input 1:
4
0111
1011
1101
1110

The adjacency matrix is such that each person is connected to everyone else. So node 1's contacts are 2,3,4. So when node 1 sends, nodes 2,3,4 receive. Then, each of those nodes is activated. When activated, they send to their contacts. So node 2 sends to 1,3,4. But node 1 is already activated. Nodes 3 and 4 are activated. So when node 2 sends, the user (4) gets a copy from node 2. Then node 3 is activated, sends to 1,2,4. So user gets a copy from 3. Then node 4 (the user) is activated, but since the user doesn't send, their contacts (which include 1,2,3) don't get anything. Wait, but according to the problem statement, when a person receives the letter for the first time, they send to all their contacts. But the user (n) is person 4 here. So when node 4 is activated (from the initial send by node 1), they would send to their contacts (1,2,3). But since the user is person 4, they don't send. Wait, the problem statement says: "every person who receives the letter for the first time sends it to all his contacts. You are person n, and you don't forward the letter when you receive it."

Ah! So when the user (n) is activated (receives for the first time), they do not send. So the user's contacts (other than themselves) would not receive any copies from the user. So in the first example, node 4 is activated (receives from node 1's initial send). Then, when node 4 is activated, they do not send. So their contacts (1,2,3) don't get any copies from them. But for the other nodes, like 2 and 3, when they are activated, they send to their contacts. So when node 2 is activated (from the initial send by node 1), they send to 1,3,4. So user (4) receives a copy from node 2. Similarly, node 3 sends to 1,2,4 when activated, so user receives a copy. Node 4 sends to their contacts but since they are the user, they don't. So in total, the user receives copies from nodes 1 (initial send?), wait no. Wait, in the initial step, node 1 sends to all their contacts. So node 1's contacts are 2,3,4. So in the first step, nodes 2,3,4 each receive the letter for the first time. So node 4 (the user) receives one copy from node 1. Then, nodes 2 and 3 are activated, and each sends to all their contacts, including 4. So user receives copies from 2 and 3. Then, when node 4 is activated (from the first step), they don't send. So in total, the user gets three copies: from 1, 2, and 3. But wait, in the sample input 1, the output is 3. So yes.

Wait, but how does that fit into the logic. So the user is person 4. So the activated set is all the people that are activated, which includes 1's contacts (2,3,4). Then, the contacts of 2 (1,3,4) are activated. But 1 is already activated, so when 2 sends, the only new activations would be people not already activated. But no, the sending happens regardless. Wait, no: when a person is activated (receives the letter for the first time), they send to all their contacts. The sending is only done once, upon activation.

So in the first step, node 1 is the initiator. He sends to 2,3,4. Each of these three is activated. So each of them sends to their contacts. Let's see:

Node 2's contacts are 1,3,4. When node 2 is activated, he sends to these three. So:

- 1 receives a copy. But 1 is already activated, so he does nothing.
- 3 receives a copy. But 3 was activated when node 1 sent, so he's already activated. So he doesn't do anything.
- 4 (the user) receives a copy. The user is already activated (from the first step), so no action.

So the user receives a copy from node 2's activation.

Similarly, node 3's activation will send to 1,2,4. So user gets another copy.

Node 4's activation (from node 1's send) will send to 1,2,3. But since the user is 4, they don't send. So no copies from that.

So the user gets:

From node 1's send: when node 1 sends to their contacts (including 4), that's one copy.

Wait, wait, no. Wait, when node 1 sends to their contacts, each contact receives a copy. So node 4 receives a copy from node 1. Then, when node 2 is activated (from node 1's send), he sends to his contacts, including node 4. So node 4 gets another copy. Similarly for node 3's activation.

So the total number of copies the user receives is equal to the number of activated nodes (excluding the user themselves) that have an edge to the user. Because each such node, when activated, sends to all their contacts, including the user. So for each activated node i (i != n), if i is connected to n, then the user gets a copy.

Ah! So the key is: for each node i (i != n), if i is reachable from node 1 (i.e., part of the activation chain), and i is a contact of n, then the user gets a copy from i. So the answer is the count of all such i.

Because each such i, when activated, sends to their contacts, which includes n, thus n receives a copy. Additionally, node 1 may also be a contact of n, so if node 1 is connected to n, then n receives a copy from node 1's initial send.

Wait, but node 1 is the one initiating. So node 1's activation (they start the process by sending to all their contacts. So node 1's activation is the first step. So the initial sending is part of their activation? Or is node 1 considered activated before sending?

The problem statement says: "Person 1 starts sending the letter to all his contacts; every person who receives the letter for the first time sends it to all his contacts."

So node 1's activation is considered as the first step. So when node 1 sends to his contacts, those contacts receive the letter for the first time. So when they receive it, they are activated and send.

So node 1 is considered as part of the activated set. Because he starts the process. So in this scenario, the activated set includes all nodes that can be reached via BFS starting from node 1. Wait, no. Because node 1 is the first to send. So when node 1 sends to his contacts, those contacts are activated. Then each of those contacts sends to their own contacts. But node 1 may be in those contacts, but since he is already activated, he doesn't process again.

Wait, the way the BFS works is:

- Start with node 1 being activated. Then, when he is activated, he sends to all his contacts, causing each of those contacts to be activated (if not already activated). Those contacts are added to the queue. Then, each of those contacts, when processed (activated), send to their contacts, and so on.

Wait no. Because according to the problem statement, person 1 starts sending. So the initial step is that person 1 sends to all contacts, which causes those contacts to be activated. So node 1 is not part of the BFS. Because he starts the process. Or is node 1 considered as activated?

Wait, the problem says: "Person 1 starts sending the letter to all his contacts; every person who receives the letter for the first time sends it to all his contacts."

So, the initial step is that person 1 sends to all his contacts. So the sending is done by person 1, but they are not receiving the letter for the first time. Because they start the process. So how is person 1 activated?

Wait, perhaps the correct model is:

The activated set starts empty. Person 1 is the initiator, but perhaps he is not part of the activated set. Because he starts the process. Then, when he sends to his contacts, those contacts receive the letter for the first time and become activated. Then, those contacts send to their contacts, etc.

But according to the problem statement, person 1 is the one initiating, but maybe he is considered as part of the activated set. Because he starts sending. So when he sends to his contacts, those are activated. But perhaps person 1 is not considered as activated. Because he didn't receive the letter. He initiated it.

This is a bit ambiguous. Let's re-examine the problem statement:

The problem says:

"Person 1 starts sending the letter to all his contacts; every person who receives the letter for the first time sends it to all his contacts. You are person n, and you don't forward the letter when you receive it."

So person 1 starts by sending the letter. This implies that he is the source. But he may not have received the letter himself. So perhaps he is not part of the activated set. So the activated set includes all people who received the letter for the first time and thus sent it. Person 1 is initiating the process but hasn't received the letter, so he is not in the activated set. Therefore, when he sends to his contacts, those contacts are activated, and they then send to their contacts. But person 1 is not activated unless someone sends him the letter.

Wait, but the problem says "Person 1 starts sending the letter". So the initial step is person 1 sending to their contacts, regardless of whether they received the letter. So perhaps the initial step is that person 1 is considered to have the letter, and when he sends to his contacts, those contacts get activated. But the problem's model is that the letter is propagated by people who receive it for the first time. So person 1's sending is part of the initiation, and he doesn't need to receive the letter.

So in this scenario, the activated set is all people who receive the letter for the first time, and thus send it. So person 1 sends the letter, but his own activation is not part of the process. Wait, but then the activated set is all people except person 1, who receive the letter. Because person 1 starts sending without receiving.

But this is confusing. Let's look at the first sample input.

Sample Input 1:

4
0111
1011
1101
1110

In this case, person 1's contacts are 2,3,4. So when he sends, those three receive the letter. They are activated. Each of them sends to their contacts. So 2 sends to 1,3,4. 3 sends to 1,2,4. 4 sends to 1,2,3. But since the user is 4, they don't send. So when 2 is activated, he sends to 1,3,4. So 1 receives a copy. But 1 hasn't been activated before. So does this mean that 1 will now be activated and send to his contacts again?

No, because according to the problem statement, only people who receive the letter for the first time send it. So when person 1 sends the letter initially, he is not part of the activated set. Then, when 2 sends to 1, 1 receives the letter for the first time, so he is activated and sends to his contacts (again). But this would create a loop. However, in the sample input 1, the output is 3. So the user (4) gets copies from 2,3, and 1's initial send?

Wait, in sample input 1, the output is 3. The user is person 4. Let's think:

Person 1 sends to 2,3,4. So person 4 receives a copy (count 1). Then, 2 is activated and sends to 1,3,4. So 4 gets a copy (count 2). Similarly, 3 is activated and sends to 1,2,4 (count 3). Also, person 4 is activated and sends to 1,2,3, but since they are the user, they don't send. So total 3 copies. But what about when 1 receives a copy from 2's activation? Because when 2 sends to 1, that's the first time 1 receives the letter. So 1 is activated and sends to 2,3,4 again. So 4 would get another copy from 1's activation. But according to the sample output, the answer is 3. So this contradicts that. So there must be a misunderstanding here.

Hmm. So perhaps the initial activation is that person 1 is activated, and the process is:

The activated set starts with person 1. When a person is activated, they send to all their contacts, which may cause others to be activated.

Wait, perhaps the correct model is:

- Person 1 is activated (has received the letter for the first time, even though he initiated it?), so he sends to all his contacts. Those contacts receive the letter, and if it's their first time, they become activated and send.

But that would imply that person 1 is part of the activated set. Then, when 2 sends to person 1, which is already activated, nothing happens. So in the first sample:

Activated nodes are 1, 2, 3,4. Then, the user (4) is connected to 1, 2, 3. So the count is 3, which matches the sample output.

So the model is that person 1 is considered activated, so when he sends to his contacts, they receive the letter and are activated. Then, when those contacts send, they include their contacts (like 1, but 1 is already activated, so no further action). So the activated set is the set of nodes reachable via BFS from node 1. Then, for each node in the activated set except the user, if they are connected to the user, the user receives a copy. Because each activated node (except user) sends once to their contacts when activated. So the user gets a copy for each such node that is connected to them.

So the answer is the number of nodes in the activated set (excluding the user) that are connected to the user (i.e., f[i][n-1] == '1').

Wait, because in the matrix, the nodes are 0-based or 1-based? The problem statement says that the input is n lines, each is a string of n characters. The first line corresponds to person 1. So the indices in the matrix are 0-based? Or 1-based? For example, in the first sample, person 1's contacts are the j-th characters of the first string. Since the first string is "0111", the 0-th index (assuming 0-based) is 0, but then person 1's contacts are at positions 1,2,3 (since those are '1's). But in the problem statement, the people are numbered from 1 to n. So the strings are 0-based? No, probably not. The first line is person 1, so the first string is the row for person 1. The first character (index 0) is for person 1's contact with person 1 (but according to the problem statement, f[i][i] is 0). Then, the j-th character (from 0 to n-1) in the i-th string (from 0 to n-1) represents the contact between person i+1 and person j+1. Because when the input is n=4, the first line is person 1, and the characters are for person 1's contacts with 1, 2, 3, 4. But since f[i][i] is 0, the first character is 0. Then the next three are 1's, so person 1 is connected to 2,3,4.

Wait, the problem statement says:

"j-th character of i-th string (f[i][j]) is '1' if people i and j will send messages to each other, and '0' otherwise. It's guaranteed that f[i][j] = f[j][i], and f[i][i] = 0."

So the indices of the strings are 0-based. But the people are numbered 1-based. For example, the first line (i=0) corresponds to person 1. So for the first sample input:

n=4, the first line is '0111', which means person 1 (i=0) is connected to persons 2 (j=1), 3 (j=2), and 4 (j=3). Because f[0][1] is '1', which represents person 1 and 2 are connected.

So, when we have to check if a person i is connected to the user (person n), which is the nth person. Since the user is person n, their index is n-1 (since the indices start at 0). So for each person i (0-based index 0 to n-1), if i is in the activated set, and f[i][n-1] is '1', then the user receives a copy from them.

So the approach is:

1. Compute the activated set: all nodes reachable from person 1 (0-based index 0) via BFS. Because person 1 is activated and sends to his contacts, which are added to the queue, and so on.

Wait, but in this model, person 1 is part of the activated set. Because he is sending the initial message. But according to the problem statement, the initial sending is by person 1, but perhaps he is considered activated (so his contacts are activated, but he is part of the activated set). So the BFS starts with person 1. Then, for each person in the BFS, when they are processed (activated), their contacts are checked. If they haven't been activated before, they are added to the queue and considered activated. So the activated set includes all nodes that are reachable from person 1.

Wait, but in this model, person 1 is in the activated set, and when he is processed, he sends to his contacts, which are added to the activated set. But in the problem statement, person 1 starts by sending the letter. So perhaps the initial step is that person 1's contacts are activated, but person 1 is not part of the activated set. Because he initiated the sending, but did not receive the letter.

This is a crucial point. Let's re-examine the problem statement.

The problem says:

"Person 1 starts sending the letter to all his contacts; every person who receives the letter for the first time sends it to all his contacts."

So, person 1 sends the letter to his contacts. Those contacts receive it for the first time and send to their contacts. So person 1 is not part of the activated set (since he didn't receive the letter for the first time; he initiated it). So the activated set includes all people except person 1 who received the letter for the first time.

Wait, but how can person 1 ever be part of the activated set? Because if someone sends the letter to him, then he would receive it for the first time and become activated. For example, in the first sample input, after person 1 sends to his contacts (2,3,4), they become activated. Then, when person 2 sends to his contacts (1,3,4), person 1 receives the letter for the first time, becomes activated, and sends to his contacts again. But this would cause a loop.

But in the sample input 1, the answer is 3, which suggests that person 1's sending to his contacts is considered the initial step, and person 1 is not part of the activated set, so when he receives the letter from others, he is activated. Let's see:

Sample input 1:

n=4.

Activated set starts with the contacts of person 1: 2,3,4. Then, when each of those sends, their contacts (including 1) receive the letter. So person 1 receives the letter for the first time and becomes activated, sending to his contacts again. But this would cause his contacts (2,3,4) to receive the letter again. But since they have already been activated, they don't send again. So person 1's activation leads to sending to 2,3,4 again, which adds to the user's count (if they are connected to the user).

But according to the sample output, the answer is 3, which implies that the user receives copies from 1, 2, and 3. So perhaps in this case, when person 1 is activated, he sends to his contacts again, leading to the user receiving another copy. But that's not reflected in the sample output. So this suggests that perhaps the model is that the activated set is the set of people who receive the letter from the initial BFS, starting with person 1's contacts, and person 1 is not part of the activated set.

Alternatively, perhaps the model is that the activated set is all people who received the letter at any time, but only send once upon first receipt. But that's not possible as per the problem statement.

This is a bit confusing. Let's try to model the first sample step by step.

Sample input 1:

Persons 1,2,3,4. All connected to each other.

Step 1: Person 1 sends to 2,3,4. These three are activated. The user (4) gets a copy from person 1's initial send. Count = 1.

Step 2: Activated persons 2,3,4 are processed in some order.

Processing person 2: sends to 1,3,4. Person 1 receives for the first time (activated), sends to 2,3,4. So user (4) gets another copy (from person 2). Count = 2. Person 3 and 4 are already activated.

Processing person 3: sends to 1,2,4. User gets another copy (from 3). Count =3. Person 1 and 2 are already activated.

Processing person 4: since they are the user, they do not send. So no copies.

Processing person 1 (activated in step 2): sends to 2,3,4. User receives another copy (from 1). But then count would be 4. But sample output is 3. So this suggests that the model is different.

Ah! This indicates that the initial step is that person 1 is not part of the activated set. He sends to his contacts, but he is not considered as having been activated. So when person 2 sends to person 1, person 1 is activated and sends to his contacts. So in the first step, person 1's initial send activates 2,3,4. Then, when 2 sends to 1, 1 is activated. Then, 1's send to 2,3,4 would cause them to receive the letter again, but since they are already activated, they don't send again. But the user (4) would get a copy from person 1's send. So count becomes 1 (from 1's initial send) + 1 (from 2's send) + 1 (from 3's send) + 1 (from 1's send). But sample output is 3.

This is a contradiction. So perhaps the model is that the activated set is all people who received the letter for the first time, and send once. But person 1 is not part of the activated set. Because he initiated the process.

Alternatively, perhaps the initial send by person 1 is considered as part of the process, but he is not part of the activated set. So the steps are:

- Person 1 sends to his contacts (2,3,4). Each of these receive the letter for the first time, so they are added to the activated set. They each send to all their contacts. So the user (4) receives a copy from 1's initial send (count 1). Then, when 2 sends to their contacts (1,3,4), 1 receives the letter for the first time (activated), and sends to their contacts. So user (4) gets a copy from 2's send (count 2). Then, when 3 sends, user gets another (count 3). Then, when 1 is activated (after receiving from 2's send), sends to their contacts (2,3,4), user gets another (count 4). But sample output is 3. So this is a problem.

But according to the sample input, the output is 3. So this model is incorrect.

Hmm. So perhaps the correct model is that the activated set is all nodes that can be reached via BFS starting from person 1, but person 1 is not considered as activated. So the initial step is that person 1's contacts are added to the queue (activated). Then, each of those send to their contacts, and so on. So person 1 is not in the activated set. Let's see:

Sample input 1:

Person 1's contacts are 2,3,4. So activated set is {2,3,4}. Each of these send to their contacts.

For person 2: contacts are 1,3,4. So 1 is not activated (since activated set is 2,3,4). So sending to 1 adds 1 to the activated set, and he sends to his contacts (2,3,4). But when person 2 sends to 1, person 1 is added to the activated set.

So the activated set becomes {2,3,4,1}. Then, person 1's contacts are processed.

So for each activated node (except the user), if they are connected to the user, it's a count.

So activated nodes are 1,2,3,4 (but user is 4). So we need to count how many of these (excluding 4) are connected to 4.

In the first sample:

1 is connected to 4 (f[0][3] is '1'), yes.

2 is connected to 4 (f[1][3] is '1'), yes.

3 is connected to 4 (f[2][3] is '1'), yes.

So total 3, which matches the sample.

So the answer is the number of nodes in the activated set (excluding the user) that are connected to the user.

But how is the activated set determined?

The activated set is all nodes that are reachable through BFS where the initial nodes are the contacts of person 1. Then, each time a node is activated, their contacts are added to the BFS queue if not already activated.

Wait, no. Because in the first step, person 1 sends to their contacts, which are 2,3,4. These three are activated. Then, each of them sends to their contacts. For example, 2 sends to 1,3,4. 1 is not activated yet, so when 2 sends to 1, 1 is activated, added to the queue. Then, when 1 is processed, he sends to his contacts (2,3,4), but they are already activated, so no new activations.

So the activated set is {2,3,4,1}.

Thus, the answer is the count of nodes in {2,3,4,1} minus the user (4) that are connected to the user. So 1,2,3. All are connected. So count is 3.

So the approach is:

1. Find all nodes that are reachable from person 1's initial contacts via BFS. That includes any node that can be reached by following contacts from the initial contacts.

But how to model this?

Perhaps the BFS starts with person 1's contacts as the initial activated set. Then, for each node in the BFS, add their contacts that haven't been activated yet.

Alternatively, the BFS starts with person 1's contacts. Wait, no. Because person 1's contacts are the initial set. Each of them sends to their contacts. For example, person 2's contacts include person 1, who may not be activated.

So the correct way to model the BFS is:

- The initial activated set is the contacts of person 1. They are added to the queue.

- For each node in the queue:

   - For each contact of this node:

      - If the contact is not yet activated and not the user (n), then add to the queue and mark as activated.

Wait, but the user (n) can be part of the activated set. Because when the user receives the letter for the first time, they are activated but do not send. So the user is part of the activated set, but their contacts are not processed.

So the correct BFS model is:

- The activated set starts with the contacts of person 1 (excluding person 1 himself). These are the initial nodes.

- Then, for each node in the queue:

   - If the node is the user (n), skip processing (since they do not send).

   - Otherwise, for each contact of the node:

      - If the contact is not activated:

         - Mark as activated.

         - Add to the queue.

So, in this model, the BFS starts with the contacts of person 1. Those are the initial activated nodes. Then, each node's contacts are processed, adding any unactivated nodes (except the user, who, when added to the queue, does not process their contacts).

Wait, but the user can be part of the initial activated set. For example, in the first sample, the initial activated set is {2,3,4} (assuming person 1's contacts are 2,3,4). Then, when processing 4 (the user), they are skipped. So their contacts are not processed.

So the steps are:

Sample input 1:

Initial queue: 2,3,4 (person 1's contacts).

Process 2:

   Contacts are 1,3,4.

   Check if 1 is activated: initial activated set is {2,3,4}.

   1 is not activated. So activate him and add to queue.

   Contacts 3 and 4 are already activated.

Process 3:

   Contacts are 1,2,4.

   1 is not activated? No, he was added when processing 2.

Process 4:

   Since 4 is the user, skip processing.

Process 1 (added when processing 2):

   Contacts are 2,3,4. All are activated. So nothing to do.

So the activated set is {2,3,4,1}.

Thus, the answer is the number of activated nodes (excluding user) connected to user: 1,2,3. All are connected. So count is 3.

So the steps are:

1. Start with the initial activated nodes as person 1's contacts.

2. For each node in the queue:

   a. If it's the user (n), skip.

   b. For each of their contacts:

      i. If the contact is not in the activated set and is not the user (since the user can't send):

         - Add to activated set.

         - Add to queue.

      ii. If the contact is the user: they are part of the activated set, but since they don't send, they are added but their contacts are not processed.

Wait, but the user (n) is added to the activated set if they receive the letter. But their processing (sending) is skipped.

So the BFS proceeds as follows:

- The initial queue is the list of person 1's contacts.

- Each contact is checked: for example, if person 1's contact is the user (n), they are added to the queue but when processed, they are skipped.

So the algorithm is:

activated = set of person 1's contacts.

queue = deque(person 1's contacts)

while queue not empty:

   current = queue.popleft()

   if current is user: continue

   for each contact in current's contacts:

      if contact not in activated and contact != user:

          add to activated

          add to queue

      else:

          if contact is user:

              (but adding to activated is not needed here, since the user is already in activated if they are a contact of current)

Wait, but when current is a contact of the user, but the user is not in the activated set, how do they get added?

Wait, for example, in the case where the user is a contact of a node processed later.

Wait, perhaps the user (n) is added to the activated set if they are a contact of person 1. For example, if person 1's contacts include n, then in the initial step, the user is added to the activated set. Then, when processed, since they are the user, their contacts are not processed.

But how is the user's activation handled?

So the correct BFS steps:

Initialize activated as the set of person 1's contacts. If the user is among them, they are added.

Then, for each node in the queue (initially person 1's contacts):

   if node is user: continue

   for each contact in node's contacts:

      if contact not in activated and contact != user:

          add to activated

          add to queue

So the user can be in the activated set (if they are a contact of person 1 or any other activated node). But when processing the user's contacts (if any), we skip because when the user is processed, we do nothing.

Thus, the activated set includes all nodes that are reachable from the initial contacts of person 1, including the user if they are part of that path.

Once the activated set is computed, the answer is the number of nodes in the activated set (excluding the user) that have a connection to the user.

So, to find the answer:

count = 0

for each node in activated:

   if node is not user and f[node][user_index] == '1':

       count +=1

Thus, the steps are:

1. Read the matrix.

2. Find person 1's contacts (index 0's contacts, i.e., j where f[0][j] == '1').

3. Initialize the activated set as those contacts.

4. BFS/DFS those contacts, adding any new contacts (except the user, which can be in the activated set but doesn't send).

5. Then, count how many of the activated nodes (excluding user) are connected to the user.

Now, implementing this.

Let's see how to code this.

First, read n.

Then read the n strings. Note that each string is of length n, and represents the contacts for person i+1 (since the first string is person 1's contacts, which is index 0 in Python).

The user is person n, which is index n-1.

So user_index = n-1.

Now, the initial activated nodes are the contacts of person 1 (index 0). So for j in range(n) where f[0][j] == '1'.

Then, perform BFS starting with these nodes, but ensuring that the user is added to the activated set if encountered, but their contacts are not processed.

So:

from collections import deque

n = int(input())

f = [input().strip() for _ in range(n)]

user_index = n-1

activated = set()

# Get person 1's contacts (index 0)
initial_contacts = [j for j in range(n) if f[0][j] == '1']

activated = set(initial_contacts)

queue = deque(initial_contacts)

while queue:

    current = queue.popleft()

    # If current is the user, skip processing
    if current == user_index:
        continue

    # Check all contacts of current
    for contact in range(n):

        if f[current][contact] == '1':

            # If contact is not in activated and contact is not user (wait, no. Contact can be user, but we still add them to activated if they are not already)
            if contact not in activated:

                activated.add(contact)

                queue.append(contact)

                # even if contact is user, add to activated but when processed, they are skipped.

# Now, count the number of nodes in activated (excluding user) that have f[i][user_index] == '1'

count = 0

for node in activated:

    if node != user_index and f[node][user_index] == '1':

        count +=1

print(count)

Let's test this code against the sample inputs.

Sample Input 1:

4

0111

1011

1101

1110

n=4, user_index=3.

Initial contacts of person 1 (index 0) are j=0,1,2,3 where f[0][j] is '1'. So j=1,2,3. So initial_contacts is [1,2,3].

activated = {1,2,3}

queue = deque([1,2,3]).

Processing 1:

current is 1 (not user).

Check contacts where f[1][j] == '1':

j=0 (f[1][0] is '1'), j=1 (0), j=2 (f[1][2] is '1'), j=3 is '1'.

For each contact:

contact 0: not in activated (initial is {1,2,3}). So add 0 to activated, add to queue.

contact 2: already in activated.

contact 3: not in activated. So add 3 to activated (now activated is {0,1,2,3}), add to queue.

So queue now has 2,3,0,3.

Processing 2:

current is 2.

contacts are 0,1,3, which are in f[2][j] == '1'.

contact 0: already in activated.

contact 1: already in activated.

contact 3: already in activated.

No new nodes added.

Processing 3 (current is 3):

user_index is 3. So skip.

Processing 0 (added from processing 1):

current is 0.

Check contacts: 0's contacts are j=0 (0),1,2,3. So j=1,2,3.

contact 1: in activated.

contact 2: in activated.

contact 3: in activated.

No new nodes added.

Processing 3 (added earlier): skip.

So the activated set is {0,1,2,3}.

Now, count nodes in activated (excluding user_index=3) that have f[node][3] == '1'.

nodes are 0,1,2.

Check each:

node 0: f[0][3] is '1' → yes. count +=1.

node 1: f[1][3] is '1' → yes. count +=1.

node 2: f[2][3] is '1' → yes. count +=1.

Total count 3 → matches sample.

Sample Input 2:

4

0110

1010

1100

0000

user_index=3.

Person 1's contacts are j=0 (no, f[0][0] is 0), j=1 (f[0][1] is 1 → included), j=2 (f[0][2] is 1 → included), j=3 (f[0][3] is 0. So initial contacts are 1,2.

activated is {1,2}.

queue is deque([1,2]).

Processing 1:

current is 1.

contacts where f[1][j] is '1: j=0, 1 (0), j=2 (f[1][2] is '1'), j=3 (0).

So contacts are 0, 2.

Check contact 0: not in activated. Add to activated, add to queue.

contact 2: already in activated.

So queue now has 2,0.

Processing 2:

current is 2.

contacts where f[2][j] is '1': j=0,1,2 (0), j=3 (0). So contacts are 0,1.

contact 0: not in activated. Add to activated, add to queue.

contact 1: already in activated.

queue now has 0,0.

Processing 0 (from queue):

current is 0.

contacts: j=0 (0), j=1 (1), j=2 (1), j=3 (0).

contact 1: in activated.

contact 2: in activated.

No new nodes.

So activated set is {0,1,2}.

count nodes in activated (excluding user 3) that are connected to user.

user_index=3. f[0][3] is '0' (from first string, which is '0110'). So node 0's contact with user is '0'.

node 1's contact with user: f[1][3] is '0' (second string is '1010' → third character is '0').

node 2's contact with user: third string is '1100' → fourth character is 0.

So none are connected. So count is 0. Which matches sample 2.

Sample Input 3:

4

0101

1001

0001

1110

n=4, user_index=3.

Person 1's contacts (index 0):

Looking at first string '0101' → j=1 and 3 are '1's. So initial contacts are 1 and 3.

But 3 is user, so when processed, they are skipped.

activated = {1,3}.

queue = deque([1,3]).

Processing 1:

current is 1.

contacts where f[1][j] == '1'. The second string is '1001' → j=0, 3 are '1's.

contact 0: not in activated. Add to activated (now 0,1,3), add to queue.

contact 3: in activated.

Processing 3 (user): skip.

Processing 0:

current is 0.

contacts are j=0 (0), j=1 (1), j=2 (0), j=3 (1). So contacts are 1 and 3.

1 is already in activated. 3 is in activated.

No new nodes.

So activated set is {0,1,3}.

Now, count the nodes in activated (excluding user 3) connected to user.

0: f[0][3] is '1' → yes.

1: f[1][3] is '1' → yes.

So count is 2 → matches sample 3.

Thus, the code seems to work.
</think>

```python
from collections import deque

n = int(input())
f = [input().strip() for _ in range(n)]
user_index = n - 1

# Initialize activated with person 1's contacts (index 0)
initial_contacts = [j for j in range(n) if f[0][j] == '1']
activated = set(initial_contacts)
queue = deque(initial_contacts)

while queue:
    current = queue.popleft()
    if current == user_index:
        continue
    for contact in range(n):
        if f[current][contact] == '1' and contact not in activated:
            activated.add(contact)
            queue.append(contact)

count = 0
for node in activated:
    if node != user_index and f[node][user_index] == '1':
        count += 1
print(count)
```