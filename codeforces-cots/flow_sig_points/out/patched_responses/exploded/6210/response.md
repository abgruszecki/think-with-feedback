<think>
Okay, let's see. The problem is about Andryusha taking socks out of a bag and managing them on the table. The goal is to find the maximum number of socks that were on the table at the same time. 

Hmm. So the process is: when he takes a sock, if the pair is already on the table, then he removes both and puts them into the wardrobe. Otherwise, he adds this sock to the table. Wait, no, wait. Wait, according to the problem statement: when he takes a sock, he checks if the pair has been taken out already. If not (meaning the pair is still in the bag), he puts the current sock on the table. Otherwise, he puts both into the wardrobe. Wait, no. Wait the problem says: If the pair of this sock has already been taken out (i.e., the pair is on the table?), then he puts both into wardrobe. Or maybe, the logic is: when he takes a sock, he checks if the pair's other sock has already been taken out (from the bag) but not yet moved to the wardrobe. So if the other sock is already on the table, then when this sock is taken, they are both moved to wardrobe, so the table's count decreases by one (since each pair contributes two socks, but when both are taken, they are removed). Wait, no. Let me read the problem again carefully.

The problem says: for each sock, Andryusha checks whether the pair of this sock has already been taken out of the bag. If not (the pair is still in the bag), he puts the current sock on the table. Otherwise, he puts both into the wardrobe. Wait, no. Wait, the wording is a bit tricky. Let's parse it again.

When he takes a sock, he checks if the pair of this sock has been already took out of the bag. So, the 'pair' here refers to the other sock. So, when he takes a sock, he looks if the other sock of the same pair was already taken out before. If the other sock is not yet taken (i.e., still in the bag), then he puts the current sock on the table. If the other sock was already taken (i.e., already on the table?), then he adds this sock to the wardrobe along with the previous one. Wait, but how can that be? Because once the other sock is taken, according to this logic, when the current sock is taken, the pair is completed. So, the two socks are moved to the wardrobe, and thus removed from the table. 

Wait, no. Let me think of the process. Let's take the first example:

Input is 1, then 1 1. 

First sock is taken. The pair's other sock is still in the bag. So he puts this sock on the table. Now, the table has 1 sock. Then the second sock is taken. Now, the pair's other sock was already taken (because the first sock was taken and is on the table). So he puts both into wardrobe. So the table count goes from 1 to 0. So the maximum was 1.

Another example: input 3, 2 1 1 3 2 3.

Let's walk through the steps:

Step 1: Take 2. Pair's other sock is in the bag. Put on table. Table count 1.

Step 2: Take 1. Pair's other is in bag. Add to table. Count 2. Max now is 2.

Step 3: Take 1. Now, the other sock (from pair 1) is already on the table. So he moves both to wardrobe. So table count decreases by 1 (since pair 1's two socks were on the table and now removed). So count is 2-2 +0 (since after adding the third sock, but then removing two). Wait, maybe the process is: when adding a sock, if the pair is already present on the table, then we remove both. Otherwise, add the current sock.

Wait, maybe the way to model this is to track a set of socks currently on the table. Each time a sock comes in:

- Check if the pair is already present in the table. If yes, remove the pair from the table. Because both are moved to wardrobe. So the current sock isn't added to the table. Instead, the existing one is removed. If the pair isn't present, add the current sock to the table.

Wait, but the problem says: when he takes a sock, he checks if the pair has already been taken out (from the bag). So if the other sock has already been taken out (i.e., was in the table but possibly not anymore?), then he puts both into wardrobe. Wait, no. Because the other sock could have been taken out earlier, but then removed from the table when its pair was processed. Hmm. 

Wait, let me re-examine the problem statement:

"If not (that means the pair of this sock is still in the bag), he puts the current sock on the table. Otherwise, he puts both socks from the pair to the wardrobe."

So 'the pair of this sock has been already took out of the bag' — which means, the other sock was taken out earlier. So, when processing a sock, if the other sock has already been taken out (i.e., was in the table and then possibly removed?), then he puts this sock and the other into the wardrobe. Wait, but once the other sock was taken out, it's either on the table or has already been moved to wardrobe. So how can the problem statement's 'already took out' include the case where the other sock was in the wardrobe?

Wait, the problem says, for each sock, check if the pair of this sock has been already took out of the bag. So the pair (i.e., the other sock) has been taken out of the bag. So if the other sock was taken out of the bag (regardless of whether it's still on the table or not), then when this sock is taken out, the pair is put into wardrobe. But that can't be right. Because once a sock is moved to wardrobe, it's no longer in the bag. But the process is that he takes the socks one by one from the bag. So the pair's other sock could have been taken out of the bag and then moved to wardrobe. But according to the problem statement's logic, when he takes a sock, he checks if the pair (other sock) was already taken out of the bag. So even if the other sock was taken, processed, and then moved to wardrobe, the answer is yes. So, for example, if the first sock is processed and put on the table, then the next is the same pair, then both are moved to wardrobe. Later, if another sock of the same pair is taken (which can't happen because each pair has exactly two socks), but the problem states that each pair has exactly two socks. So each xi appears exactly twice.

Wait, the problem says, "It is guaranteed that Andryusha took exactly two socks of each pair." So each number from 1 to n appears exactly two times in the list. So each pair is processed exactly twice.

So, when processing a sock, the other sock of the same pair has either been processed before (i.e., already taken out of the bag) or not. 

So for each sock, if the other sock was taken out of the bag before (i.e., this is the second time the pair is being processed), then he puts both into the wardrobe. So the current sock is not added to the table. Instead, he checks if the other sock was already taken out. If so, then this sock is the second one, and both are moved to wardrobe, so the current sock is not added. But what about the first sock? Let's model this.

Let's think of a data structure that tracks for each pair whether the first sock has been processed. For example, a dictionary that counts how many times each pair has been processed so far. For a given sock x_i, when processing it:

If the count for x_i is 0 (this is the first time), then increment the count to 1, and add the sock to the table. Current table size increases by 1.

If the count is 1 (this is the second time), then we have to check: when the first sock was processed, it was added to the table. Now, when processing the second sock, we see that the pair was already taken (since count is 1). So, we need to remove the first sock from the table. So the current table size decreases by 1 (since the first sock was in the table, and now both are moved to wardrobe).

Wait, but in this model, when the second sock comes in, we subtract 1 from the current count of table socks. But how do we track which socks are in the table?

Alternatively, for each pair, when the first sock is processed, it's added to the table. When the second is processed, the pair is completed, so the first sock is removed from the table, and the second sock is not added. So the table's size increases by 1 when the first sock is processed, and decreases by 1 when the second sock is processed. 

In this case, the maximum number of socks on the table is the maximum value of the current count during this process.

Wait, let's take the first example:

Socks are 1, 1.

Processing first 1: count is 0 → add to table. Current count is 1. Max is 1.

Processing second 1: count was 1. Now, since the pair was already taken once (the first sock), the second sock is processed. So the pair is now complete. So the table count decreases by 1. So current count is 0. Max remains 1.

So the example is correct.

Second example:

Socks are 2,1,1,3,2,3.

Processing steps:

1. 2: count is 0 → add to table. Current count is 1. Max is 1.

2. 1: count is 0 → add. Current count 2. Max is 2.

3. 1: count is 1 → so this is the second sock. So we subtract 1 from the current count (since the first sock was on the table). Current becomes 1. Max is still 2.

4. 3: count 0 → add. Current 2. Max becomes 2 again.

5. 2: count was 1 (since first 2 was processed). So this is the second 2. Subtract 1 → current becomes 1.

6. 3: count was 1 → subtract 1 → current 0.

So the maximum was 2.

Which matches the example.

So the key here is to track, for each sock pair, whether we've seen an odd or even number of socks (i.e., 0 or 1). Each time a sock is processed:

- If it's the first occurrence (count is 0), we add 1 to the current table size.
- If it's the second occurrence (count is 1), we subtract 1 from the current table size.

The maximum value of the current table size during this process is the answer.

But wait, the count can be tracked with a hash map (or array, since the pairs are numbered from 1 to n), which keeps track of how many times each pair has been processed so far. For each sock in the sequence, we check the count. If even (0), add 1 to current and increment the count. If odd (1), subtract 1 from current and increment the count. Wait, but count can be up to 2? No. Because each pair is exactly two socks. So for each pair, the count can be 0, 1, or 2. Wait no, because the first sock is processed, count becomes 1, and when the second is processed, count becomes 2. But once count is 2, that's the end. But in the problem, each pair has exactly two socks. So the count for each pair can be 0, 1, or 2. But the problem says that each pair is processed exactly twice, so the count for each pair will end at 2.

But for our problem, we need to track whether the first sock of a pair has been processed. So when processing the current sock x_i, if the count of x_i is 0 → it's the first sock, so add 1 to the current table size. Then increment the count to 1. If the count is 1 → it's the second sock. Then subtract 1 from the current table size. Then increment the count to 2.

So the steps are:

Initialize a list (or array) of size n+1 (since pairs are 1-based) to track the count for each pair. All counts start at 0.

Initialize current_size = 0 and max_size = 0.

For each sock in the sequence:

    if count[x] == 0:
        current_size += 1
        count[x] += 1
    else:
        current_size -= 1
        count[x] += 1
    max_size = max(max_size, current_size)

So this would track the current size correctly. 

Let's test this with the first example.

n=1, sequence [1,1].

Processing first 1:

count[1] is 0 → current becomes 1. max is 1. count becomes 1.

Processing second 1:

count[1] is 1 → current becomes 0. max remains 1. count becomes 2.

Yes.

Second example:

sequence [2,1,1,3,2,3].

Processing steps:

current_size = 0, max=0.

1st sock: 2. count is 0 → current 1. max 1. count[2]=1.

2nd sock: 1. count is 0 → current 2. max 2. count[1]=1.

3rd sock: 1. count is 1 → current 1. max remains 2. count[1]=2.

4th sock:3. count 0 → current 2. max remains 2. count[3]=1.

5th sock:2. count is 1 → current 1. max 2. count[2] becomes 2.

6th sock:3. count is 1 → current 0. max remains 2.

So the answer is 2. Correct.

So this approach seems correct.

Now, considering the constraints: n can be up to 1e5, and the sequence has 2n elements.

In Python, using a list to track counts (since the pairs are 1-based) is efficient. For each of the 2n elements, we perform O(1) operations. So time complexity is O(n), which is acceptable for n=1e5.

Memory-wise, the count array is O(n), which is also acceptable (1e5 elements take about 400KB in Python, which is way under the 256MB limit).

So the optimal approach is to track the counts and current size, updating the max each step.

Therefore, the code can be written as follows:

Read n.

Read the list of 2n integers.

Initialize a list (array) of size n+1, initialized to 0.

current = 0

max_count = 0

for x in the list:

    if counts[x] == 0:

        current +=1

        counts[x] +=1

    else:

        current -=1

        counts[x] +=1

    if current > max_count:

        max_count = current

print(max_count)

Wait, but in the problem statement, the second example, when the first sock of a pair is processed, the current increases. When the second is processed, it decreases.

So the code should correctly track the max.

Yes.

Now, in Python, for n=1e5, the list counts can be initialized as [0]*(n+1), which is manageable.

So the code would be:

Read n.

Then read the second line as a list of integers.

Then process each as described.

Now, handling the input is important. For n=1e5, the input line has 2e5 elements. Using input().split() could be a problem if not read properly. But in Python, input().split() is efficient for that.

So the code:

n = int(input())

socks = list(map(int, input().split()))

counts = [0]*(n+1)

current = 0

max_socks = 0

for x in socks:

    if counts[x] == 0:

        current +=1

        counts[x] +=1

    else:

        current -=1

        counts[x] +=1

    if current > max_socks:

        max_socks = current

print(max_socks)

Testing the first example:

Input:

1

1 1

Processing:

counts initialized to [0, 0]

First x=1:

counts[1] is 0 → current becomes 1. counts[1] becomes 1. max_socks is 1.

Second x=1:

counts[1] is 1 → current 0. counts[1] becomes 2. max remains 1.

Output 1.

Second example:

3

2 1 1 3 2 3

Processing:

counts starts as [0,0,0,0]

Process 2 → counts[2] is 0 → current 1. counts[2] =1. max 1.

Process 1 → counts[1] is 0 → current 2. max 2.

Process 1 → counts[1] is 1 → current 1. counts[1] becomes 2.

Process 3 → counts[3] is 0 → current 2. max remains 2.

Process 2 → counts[2] is 1 → current 1.

Process 3 → counts[3] is 1 → current 0.

max is 2.

So output is 2. Correct.

This code should handle all test cases correctly.

Time and memory-wise, this code is optimal. For n=1e5, the counts array is 1e5+1 elements, which is acceptable.

Thus, the code is correct.
</think>

```python
n = int(input())
socks = list(map(int, input().split()))
counts = [0] * (n + 1)
current = 0
max_socks = 0

for x in socks:
    if counts[x] == 0:
        current += 1
        counts[x] = 1
    else:
        current -= 1
        counts[x] = 0  # Since each pair is exactly two, setting to 0 isn't necessary but correct after both are processed. However, the code can be optimized by toggling between 0 and 1.

    if current > max_socks:
        max_socks = current

print(max_socks)
```

Wait, I just realized that in the original code I wrote, when processing the second sock of a pair, counts[x] was incremented to 2, but in the code here, after the first sock is processed (count becomes 1), when processing the second sock, counts[x] is set to 0. Wait, this is a mistake. Let me re-examine.

In the original reasoning, the code in the thinking part was:

counts[x] is initialized to 0. For each x in socks:

if counts[x] == 0:

   current +=1

   counts[x] +=1

else:

   current -=1

   counts[x] +=1

But in the code written here, the else part does counts[x] = 0. That's incorrect.

Oh right! The code in the code block above is different from the original reasoning. So this is an error.

Because, the original reasoning used counts to track how many times each sock was seen. So for a pair, counts[x] can be 0, 1, or 2. But when processing the second sock, the counts[x] is incremented again.

But in the code above, after processing a sock, counts[x] is toggled between 0 and 1. Which is a mistake.

This explains why the code would work for the first example but may fail others.

Wait, for example, let's take the first example:

Processing first sock (1):

counts[1] is 0 → current becomes 1, counts[1] =1.

Processing second sock (1):

counts[1] is 1 → current becomes 0, counts[1] =0.

But in the original reasoning, counts[x] was incremented to 2.

But this code would set counts[x] to 0 again. So for a third occurrence (which can't happen here), but in the problem, each pair has exactly two socks. So counts[x] can be 0 or 1, but the code's approach is to toggle between 0 and 1 for each occurrence.

This approach is correct. Because, for each pair x, the first sock is processed when counts[x] is 0 → becomes 1. The second sock is processed when counts[x] is 1 → becomes 0. Because the pair is processed exactly twice.

Thus, the code in the code block above is correct. Because for each pair x, the first sock is processed (counts[x] 0 → 1), and the second sock is processed (counts[x] 1 → 0). Because in the problem, each x appears exactly twice, so after processing both, counts[x] is 0 again.

Wait, this would work because the code is using counts[x] as a boolean (0 or 1) indicating whether the first sock has been processed. So for each pair, the two socks are processed in the sequence. The first sets counts[x] to 1, the second sets it to 0. So the code works.

But why? Because for the first sock, when counts[x] is 0, we add 1 to current. For the second sock, when counts[x] is 1, subtract 1 from current. Thus, the code correctly tracks the current number of socks on the table.

Yes, this code is correct and more efficient. Because instead of incrementing counts[x] each time, it toggles between 0 and 1. Thus, for each sock in the sequence, we check if it's the first or second occurrence, and update the counts and current accordingly.

So the code in the code block is correct. Let's test the first example again.

First example:

n=1, socks [1,1].

Processing first 1: counts[1] is 0 → current becomes 1. counts[1] =1. max is 1.

Processing second 1: counts[1] is 1 → current becomes 0. counts[1] =0. max remains 1.

Second example:

sequence 2,1,1,3,2,3.

Processing:

counts initialized to [0,0,0,0,0] (n=3, indexes 0-3).

Processing 2:

counts[2] 0 → current 1. counts[2] =1. max 1.

Processing 1: counts[1] 0 → current 2. counts[1]=1. max 2.

Processing 1: counts[1] 1 → current 1. counts[1]=0.

Processing 3: counts[3] 0 → current 2. max 2. counts[3] =1.

Processing 2: counts[2] is 1 → current 1. counts[2]=0.

Processing 3: counts[3] is 1 → current 0. counts[3]=0.

Thus, max is 2. Correct.

So the code in the code block is correct. The initial mistake in the code (setting counts[x] to 0 or 1) is actually correct and more efficient. Because for each pair, the code uses a toggle, and each sock is processed in O(1) time.

Thus, the code is correct. The original reasoning was slightly different, but the code is correct.