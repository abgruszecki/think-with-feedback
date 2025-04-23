<think>
Okay, I need to solve this problem where I have to find all possible XOR values from increasing subsequences of an array. Let's think about the approach here.

The problem says that the subsequence has to be increasing. So, for each element in the array, any subsequence that includes it must have elements in increasing order. The XOR of the elements in such a subsequence can be various values. My task is to collect all possible x values that can be obtained from any possible increasing subsequence, including the empty subsequence (which gives 0).

First, let's note that the maximum possible a_i is 500. Wait, but if the array is up to 1e5 elements, how can we process this efficiently?

The key here is that the maximum XOR possible is determined by the bits of the elements. Since each a_i is up to 500, the maximum possible XOR could be up to 511 (since 500 in binary is 111110100, which is 9 bits). So the possible x values are up to 2^9-1 = 511. That's manageable. So the possible x values are in a small range. That's a crucial observation. This means that for each position, we can track possible x values that can be achieved with subsequences ending at that position, and their maximum element (since the next elements in the subsequence must be larger).

So the approach could be dynamic programming. For each element a[i], we can track a set of possible (current_xor, last_element) pairs. But maintaining all possible pairs might be expensive if done naively. However, since the possible xors are limited (up to 511), and the last_element can be up to 500, maybe we can find an efficient way to represent this.

Wait, but for each element a[i], when considering adding it to existing subsequences, the existing subsequences must end with an element less than a[i]. So for each a[i], the new possible xors are formed by taking existing xors from elements j where a[j] < a[i], then XOR with a[i], and also include the subsequence consisting of just a[i] itself.

Additionally, the empty subsequence is allowed, which contributes x=0. So the initial state is x=0 (empty subsequence) and perhaps a set of xors built from non-empty subsequences.

But how to model this efficiently?

Let me think. The plan is to iterate through each element in the array, and for each element, we can track all possible xors that can be achieved by subsequences ending with elements less than the current a[i]. Then, for each such possible xor value, when we add a[i], the new xor is (previous_xor ^ a[i]), and the new subsequence ends with a[i]. We also need to track the maximum possible value of the last element in the subsequence for each xor value to ensure that we can efficiently check which previous elements can be used.

Wait, perhaps for each possible xor value x, we can track the minimal last element of the subsequence that produces x. Because when considering a new element a[i], any existing x whose last element is less than a[i] can be extended by a[i]. However, for a given x, if there are multiple possibilities with different last elements, we want to keep track of the minimal last element for each x. Why? Because if a new element a[i] is larger than the minimal last element, then any other larger last elements for the same x would also allow a[i] to be added, but keeping the minimal allows us to have the smallest possible last element, which would give more opportunities for future elements to be added (since future elements just need to be larger than the last element). So for each x, if we keep the minimal possible last element, that's sufficient.

So the idea is to maintain a dictionary (or a map) where for each possible x, we store the minimal last element of a subsequence that produces x. Then, when processing a new element a[i], we look for all existing x's in the current map where the stored last element is less than a[i]. For each such x, we compute a new x' = x ^ a[i], and check if the new x' already exists in the new map. If it does, we only keep the minimal last element (i.e., if a[i] is smaller than the existing value for x', we update it). Also, we need to include the subsequence consisting of just a[i] itself, which adds x = a[i] with last element a[i].

This approach can be efficient because the number of possible x's is up to 512 (since 2^9=512), and for each element, we process each possible x in the current map. Since n is up to 1e5 and each step is O(512), the total time should be acceptable.

So the steps would be:

1. Initialize a set/dictionary of possible x's. Initially, we have x=0 (from the empty subsequence) with last element being considered as -infinity or something, but wait, the empty subsequence doesn't have a last element. Hmm, perhaps we need to separate the empty subsequence case.

Wait, the empty subsequence contributes x=0, but any extension of it would start with a single element. So for the empty subsequence, when adding a new element a[i], the new x would be a[i], and the last element is a[i]. However, the empty subsequence's last element can be considered as non-existent, so any a[i] can be added to it. So perhaps the initial state is a map that includes x=0 with a last element of -infinity (so that any a[i] can be added to it). Alternatively, during the processing of each a[i], we can consider adding the empty subsequence's x (0) and create a new x (0 ^ a[i] = a[i]) with last element a[i].

But how to model this correctly. Let's think again.

The empty subsequence's XOR is 0, and its last element can be considered as a value that is smaller than any possible element in the array (since the empty subsequence can be extended by any element to form a subsequence of length 1). So when processing a[i], for the existing x=0, which has a last element of, say, -infinity, which is less than a[i], we can generate a new x of a[i] XOR 0 = a[i], with last element a[i]. Then, when considering the next elements, any element larger than a[i] can be added to this subsequence.

But how to represent the initial state. Let's model the map as follows: the initial map contains x=0 with last element of -infinity (or a very small number, like -1). Then, for each a[i], we process all existing entries in the current map where the last element is less than a[i]. For each such entry (x_val, last_val), we can compute new_x = x_val ^ a[i], and the new_last_val is a[i]. We then add this new_x and new_last_val to a temporary map. After processing all existing entries, we merge the temporary map into the main map, keeping for each x the minimal last_val.

Additionally, the current element a[i] itself can form a subsequence of length 1, which is x = a[i], last element a[i]. So this should also be considered. Wait, but if there was a previous x_val of 0 (from the empty subsequence), then when we process a[i], we would generate x_val a[i] via 0 ^ a[i]. So including the empty subsequence's 0 ensures that each element can be considered as a single-element subsequence.

So the steps for each a[i] would be:

- Create a temporary dictionary to hold the new entries generated by this a[i].
- Iterate over all existing entries (x, last) in the current dictionary where last < a[i]. For each such entry, compute new_x = x ^ a[i], and new_last = a[i]. For the temporary dictionary, we track new_x: new_last. But if new_x already exists in the temporary dictionary, we take the minimum of the existing new_last and the current new_last. So the temporary dictionary will have the minimal possible last for each new_x generated from this a[i].
- Also, we need to consider the possibility of starting a new subsequence with a[i] by itself. But that's equivalent to taking the empty subsequence's x=0 (last element -infinity) and adding a[i], which would generate x = 0 ^ a[i] = a[i], last element a[i]. So this is already handled by the existing entries if we have the initial x=0 with last element -infinity.
- After processing all existing entries, merge the temporary dictionary into the main dictionary. For each new_x in the temporary dictionary, if the main dictionary already has new_x, we compare the existing last value with the new one and keep the minimum. If it's not present, we add it with the new_last.

Wait, but merging the temporary entries into the main dict would accumulate all possible x values. But the main dict may have entries that were generated from previous elements, and the new entries from a[i] are added only if their x is not present or has a smaller last element.

Additionally, after processing a[i], the main dictionary should include all possible x values that can be formed by subsequences ending at or before i, with their minimal last elements.

Wait, perhaps the approach is:

- Maintain a dictionary, say dp, where dp[x] is the minimal last element of a subsequence that produces x.
- Initially, dp contains {0: -infinity} (or a very small number, like -1 to ensure that any a[i] >=0 can be added).
- For each a_i in the array:
   - Create a temporary dictionary tmp.
   - For each x in dp:
      - If dp[x] < a_i, then we can form a new_x = x ^ a_i with last element a_i.
      - In tmp, for new_x, we want to keep the minimal a_i. So if new_x is not in tmp, we add it with a_i. If it's already present, we take the minimum between the existing value and a_i.
   - Now, we merge tmp into the existing dp. For each new_x in tmp:
      - If new_x is not in dp, add it with the value from tmp.
      - Else, update dp[new_x] to be the minimum between the existing dp[new_x] and tmp[new_x].
   - Also, after merging, we can add the possibility of the subsequence [a_i], which is handled by the initial x=0 with last element -infinity. Because when we process x=0 (dp[0] = -infinity), which is less than a_i, new_x would be 0^a_i = a_i, and the new last element is a_i. So the tmp will already include this.

So this approach should capture all possible x values that can be formed by any increasing subsequence.

Once all elements are processed, the set of keys in the dp dictionary (excluding perhaps the initial x=0 with last -infinity, but wait no—the empty subsequence is allowed, so x=0 is a valid answer. Wait, the initial state is x=0 with last element -infinity. But when merging, the dp includes all possible x's. The empty subsequence's x=0 is kept in the dp, but when processing elements, we can add new x's. But the problem statement says that the empty subsequence is allowed, so the output must include 0. However, during processing, if there's a subsequence formed by the empty subsequence, then x=0 is already in the dp. So when we collect all x's in the dp, including 0, that's correct.

Wait, the empty subsequence's x=0 is included in the dp. So after processing all elements, the x=0 is part of the keys. However, when processing elements, the existing x=0 (with last element -infinity) allows us to create new subsequences starting with any a_i. So the initial x=0 remains in the dp throughout. Therefore, the final dp will include all possible x's generated by any increasing subsequences, including the empty one.

So the steps are:

Initialize dp as {0: -1} (assuming all a_i are >=0, so -1 is less than any a_i).

For each a_i in a:

   create tmp as empty.

   for each x in dp:

      if dp[x] < a_i:

          new_x = x ^ a_i

          if new_x not in tmp or a_i < tmp[new_x]:

              tmp[new_x] = a_i

   then, merge tmp into dp:

      for new_x in tmp:

          if new_x not in dp or tmp[new_x] < dp[new_x]:

              dp[new_x] = tmp[new_x]

This way, after processing all a_i, the keys of dp are all possible x values. However, in the initial dp, x=0 has a last element of -1, which is less than any a_i. So for each a_i, the first step would generate new_x = 0^a_i = a_i, which is added to tmp. Then, when merging into dp, if a_i is not in dp, it's added with a_i. If it is present, but perhaps from a previous element with a_i' < current a_i, then the new value (current a_i) would be larger than the existing one, so we take the minimum. Wait, no. For example, if dp has a new_x= a_j (from a previous element a_j) with last element a_j. Now, when processing a_i (which is larger than a_j?), no, a_i can be in any order. Wait, the a array is arbitrary. So when a_i is processed, and if there's a subsequence that ends with a_j < a_i, then the new subsequence would end with a_i. The key is that the last element must be smaller than a_i. So for x in dp where dp[x] < a_i, new_x is formed.

But the tmp captures all possible new_x values generated by appending a_i to existing subsequences that can be extended. Then, when merging into dp, for each new_x in tmp, we compare the current value in dp (if any) with the new value (a_i). If the new value (a_i) is smaller than the existing one, then we update it. Because a smaller last element allows more possibilities in the future (since future elements need to be larger than the last element).

Wait, yes. So for example, suppose in dp, there's a new_x=5 with last element 3. Then, when processing a_i=4, since 3 <4, we can create new_x=5^4=1 (assuming 5 XOR4=1) with last element 4. Now, suppose there's already a new_x=1 in dp with last element 5 (from a previous a_i=5). When merging, the new last element is 4, which is smaller than 5. So we update dp[1] to 4. This allows future elements larger than 4 to be added to this subsequence, whereas if we kept the 5, future elements would need to be larger than 5. So keeping the minimal last element is better for future possibilities.

Therefore, merging the tmp entries by taking the minimum last element for each new_x is correct.

Once all elements are processed, the keys of dp are all possible x values that can be achieved by any increasing subsequence. So the answer is all the keys in dp, sorted in increasing order.

Now, the problem is to implement this approach efficiently.

The key points are:

- The maximum possible x is 512 (since each a_i is up to 500, and the XOR of up to 1e5 elements would be up to 511, but even that's manageable since 512 possible x's).

- For each element in the array, we process each possible x in the current dp. Since the number of possible x's is up to 512, each step is O(512) operations. For n=1e5, this is O(5e7) operations, which should be manageable within the time constraints.

Now, implementing this in Python:

The initial dp is {0: -1}.

For each a_i in the array:

   create a temporary dictionary tmp.

   iterate over all x in dp:

      if dp[x] < a_i:

          new_x = x ^ a_i

          if new_x is not in tmp or a_i is less than tmp[new_x], then set tmp[new_x] = a_i.

   then, merge tmp into dp:

      for each new_x in tmp:

          if new_x is not in dp or tmp[new_x] < dp[new_x], then set dp[new_x] = tmp[new_x]

This way, after all elements are processed, the keys of dp are all possible x's.

Once all elements are processed, we collect the keys of dp, sort them, and output them.

Wait, but the initial x=0 (from the empty subsequence) is allowed. The empty subsequence is considered to have XOR 0. So the answer includes 0.

But according to the first sample input, the output includes 0 even though there's a 4, 2, etc. So this approach should capture that.

Testing the first sample input:

Sample Input 1:

4

4 2 2 4

Let's process each element:

Initial dp: {0: -1}

Processing first element 4:

a_i =4.

Iterate over x in dp: x=0. dp[x] =-1 <4. So new_x=0^4=4. tmp becomes {4:4}.

Merge into dp. So now dp is {0: -1,4:4}.

Processing second element 2:

a_i=2.

Iterate over x in dp:

x=0: dp[x]=-1 <2. new_x=0^2=2. tmp[2] =2.

x=4: dp[x]=4. 4 is not <2. So no.

So tmp is {2:2}.

Merge tmp into dp. Now, 2 is not in dp, so add it. dp is {0:-1,4:4, 2:2}.

Processing third element 2:

a_i=2.

Iterate over x in dp:

x=0: -1 <2. new_x=2. tmp[2] is 2 (since existing tmp is empty, add 2:2).

x=4: 4 is not <2. No.

x=2: 2 is not <2. No.

So tmp is {2:2}.

Now merging into dp: for new_x=2, tmp[2]=2. dp's current 2 has value 2. So no change. So dp remains the same.

Processing fourth element 4:

a_i=4.

Iterate over x in dp:

x=0: -1 <4 → new_x=0^4=4. If tmp has 4, compare existing value. Current tmp is empty. So tmp[4] =4.

x=4: 4 <4 → no.

x=2: 2 <4 → new_x=2^4=6. tmp[6] =4.

So tmp is {4:4, 6:4}.

Merge into dp:

Check existing dp:

dp has 4:4. tmp's 4 is 4. So no change.

6 is not in dp. Add 6:4.

So now dp is {0:-1, 2:2,4:4,6:4}.

So the keys are 0,2,4,6. Sorted, which matches the first sample's output. So this approach works.

Great. Now, the code.

In Python, to represent the dp, a dictionary is used. Since the possible x's are up to 512, the dictionary is manageable.

Now, for each a_i in the array, we process the current dp and generate tmp.

But in Python, iterating through a dictionary while modifying it can cause issues. However, since we are generating tmp first and then merging, this should not be a problem.

So the steps in code:

Read n.

Read the array a.

Initialize dp as {0: -1}.

For each num in a:

   tmp = {}

   for x in dp:

      last = dp[x]

      if last < num:

          new_x = x ^ num

          new_last = num

          if new_x in tmp:

              if new_last < tmp[new_x]:

                  tmp[new_x] = new_last

          else:

              tmp[new_x] = new_last

   # Now merge tmp into dp

   for new_x in tmp:

      new_last = tmp[new_x]

      if new_x in dp:

          if new_last < dp[new_x]:

              dp[new_x] = new_last

      else:

          dp[new_x] = new_last

Once all elements are processed, collect all keys of dp, sort them, and output.

But wait, in the initial step, the empty subsequence is allowed (x=0). So the code will include 0 in the keys.

Yes.

Now, let's test this code with the first sample input:

Sample Input 1:

4

4 2 2 4

Processing:

After first element (4):

dp is {0: -1, 4:4}.

After second element (2):

Processing tmp is {2:2}. dp becomes {0:-1,4:4,2:2}.

Third element (2):

Processing, for x=0: new_x=2, new_last=2. But existing 2 in dp is 2. So tmp is {2:2}. Merging, no change.

Fourth element (4):

x=0 gives new_x=4, new_last=4. x=2 gives new_x=6, new_last=4. So tmp is {4:4,6:4}.

Merge into dp:

existing 4:4 → new_last 4 is same as current. No change. 6 is new, added. So keys are 0,2,4,6. Sorted as 0,2,4,6. Correct.

Now, code:

But wait, the initial dp is {0: -1}, which is correct.

Now, handling the code in Python. However, for efficiency, since we have n up to 1e5 and per iteration O(512) steps, this should be manageable.

But in Python, dictionaries can be a bit slow. So perhaps using a list or a fixed-size array for the dp would be more efficient. Since the possible x can be up to 511, perhaps using a list of size 512, where each index represents the x value, and the value stored is the minimal last element for that x.

Yes, that's better. Because the maximum x possible is 511 (since 500 is 0b111110100, and XORing up to 1e5 elements can't exceed 9 bits). So using a list where the index is the x value, and the value is the minimal last element for that x. Also, we can track which x's are present.

So the initial dp can be represented as a list of size 512, initialized to a large value (like infinity), except for x=0, which has last element -1.

Then, for each a_i in the array:

   create a new temporary list (or use a dictionary) to collect the new x's.

   iterate over all x in 0..511 where dp[x] is not infinity and dp[x] < a_i.

   For each such x, compute new_x = x ^ a_i. Then, if the new_last (a_i) is less than the current value in tmp[new_x], update it.

Wait, but for the temporary storage, perhaps using a dictionary is better. Alternatively, for each a_i, iterate through all possible x's (0-511) where dp[x] < a_i. Then compute new_x and track the minimal a_i for each new_x.

But using a list for dp would allow faster access.

So the code can be optimized as follows:

Initialize a list dp where dp[x] is the minimal last element for x. Initialize all to a large value (like float('inf')), except dp[0] = -1.

Then, for each num in a:

   create a temporary dictionary (or a list) to collect new_x and their minimal new_last.

   for x in 0..511:

      if dp[x] < num:

          new_x = x ^ num

          new_last = num

          if new_x not in tmp or new_last < tmp[new_x]:

              tmp[new_x] = new_last

   # Now, merge tmp into dp.

   for new_x in tmp:

      if tmp[new_x] < dp[new_x]:

          dp[new_x] = tmp[new_x]

This approach uses a list for dp, which is faster than a dictionary. Since the x values are 0..511, we can loop through each possible x each time.

But in Python, looping through 512 elements for each a_i (which is 1e5 elements) is 1e5 * 512 = 5.12e7 operations, which is acceptable.

So in code:

max_xor = 512  # since 500 is 0b111110100 (9 bits), maximum possible XOR is 511.

n = int(input())
a = list(map(int, input().split()))

dp = [float('inf')] * (max_xor)
dp[0] = -1  # x=0 has last element -1.

for num in a:
    tmp = {}
    for x in range(max_xor):
        if dp[x] < num:
            new_x = x ^ num
            new_last = num
            if new_x in tmp:
                if new_last < tmp[new_x]:
                    tmp[new_x] = new_last
            else:
                tmp[new_x] = new_last
    # merge tmp into dp
    for new_x, new_last in tmp.items():
        if new_last < dp[new_x]:
            dp[new_x] = new_last

# collect all x where dp[x] is not infinity, or x=0.

result = []
for x in range(max_xor):
    if dp[x] != float('inf') or x ==0:
        # wait, x=0's dp[0] is -1, which is not infinity. So the x=0 is always included.

        # Wait, the initial dp[0] is -1. So after processing, if any x is possible, including x=0, which is included.

        # So collect all x where dp[x] is not infinity.

        if dp[x] != float('inf'):
            result.append(x)

result.sort()

print(len(result))
print(' '.join(map(str, result)))

Wait, but in the code, after processing, the x=0 has dp[0] = -1, which is not infinity. So it will be included in the result. All other x's that are possible have dp[x] not infinity. So the code correctly collects all possible x's.

Testing this code with the first sample input:

After processing the elements, the dp for x=0 is -1, x=2 is 2, x=4 is4, x=6 is4. So in the code, these x's are added to the result. Then sorted, which gives 0,2,4,6.

Yes.

Another test case: sample input 2.

Sample Input 2:

8

1 0 1 7 12 5 3 2

The output is 12 numbers.

But according to the code, this should process each element and compute the possible x's.

But the code would collect all x's where dp[x] is not infinity. Let's see if the code works.

The code seems correct.

Now, the only thing to note is that the code initializes dp with size 512 (max_xor is 512). But when the maximum possible x can be up to 511. So the code's max_xor is 512, which includes 0..511. That's correct.

Wait, the code uses max_xor =512, but the x can be up to 511, since 2^9=512, but the maximum possible XOR of 9 bits is 511 (binary 111111111). So the code should loop up to 511. So the code's max_xor is 512 (since x can be from 0 to 511 inclusive). The code uses a list of 512 elements (indices 0 to 511), so that's correct.

Yes.

Therefore, the code should work.

Another thing: the code uses 'float('inf')' as a marker for impossible x's. So during the initial step, all x's except x=0 have dp[x] = inf. Then, during processing, only x's that can be achieved have their dp[x] set to a value < inf.

So in the result collection, all x where dp[x] is not inf are valid x's.

This is correct.

Now, the code for sample input 2:

But how does the code handle elements in a different order. Let's see.

But according to the code's logic, it should track the minimal last element for each x, allowing future elements to be added. So even if the array is not sorted, the code should correctly track the possible increasing subsequences.

Yes.

Therefore, the code should be correct.
</think>

```python
def main():
    max_xor = 512  # Since 500 is 9 bits, max XOR is 511 (0b111111111)
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [float('inf')] * max_xor
    dp[0] = -1  # Initial state: XOR 0 with last element -infinity (represented as -1)
    
    for num in a:
        tmp = {}
        for x in range(max_xor):
            if dp[x] < num:
                new_x = x ^ num
                new_last = num
                if new_x in tmp:
                    if new_last < tmp[new_x]:
                        tmp[new_x] = new_last
                else:
                    tmp[new_x] = new_last
        
        for new_x, last in tmp.items():
            if last < dp[new_x]:
                dp[new_x] = last
    
    result = [x for x in range(max_xor) if dp[x] != float('inf')]
    result.sort()
    
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```