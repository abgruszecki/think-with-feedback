<think>
Okay, so I need to solve this programming problem where the question is whether building a second oven will reduce the total time to get n cakes. Let's see the problem statement again.

The problem says that one oven takes t minutes to make k cakes. All cakes are done at once. Arkady needs at least n cakes. He can build a second oven, which takes d minutes to build. While building, the first oven is working. Once the second is built, both ovens work. We need to check if building the second oven will reduce the time needed. If it's the same, it's not considered useful.

Hmm. So the approach is to calculate the time without building the second oven, then calculate the time with building it, and compare them.

First, let's calculate the time without building the second oven. That's straightforward. How many batches are needed? Each batch gives k cakes. The number of batches is ceil(n/k). Multiply by t. Let's call this time1.

Then, the time with building the second oven. This is trickier. Because during the time d minutes (building time), the first oven is working. So we need to calculate how many cakes are produced during the building phase, then see how much time is needed after that with both ovens.

Wait, but how does the building time affect the schedule. Let's think step by step.

The building starts at time 0. The building takes d minutes. During those d minutes, the first oven can bake cakes. So how many full batches can the first oven do in d minutes?

Each batch takes t minutes. So in d minutes, the number of batches is floor(d / t). But wait, if the oven starts a batch at time 0, then it completes at time t. If d is, say, 5 and t is 6 (like the first example), then during the first 5 minutes (the time to build the second oven), the first oven hasn't completed a batch yet. So in the first example, during the 5 minutes of building, the first oven is still working on the first batch, which takes 6 minutes. So during the building time (d=5), the first oven doesn't complete any batches. Wait, no. Wait, during the d minutes, the first oven can start batches as usual, but any batches that start before d minutes will complete.

Wait, no. Let's model the time. The building starts at time 0. The building process takes d minutes. So the second oven becomes available at time d. So during these d minutes, the first oven is active. Let's model how many batches the first oven can complete in the first d minutes.

Each batch takes t minutes. So the number of batches is (d // t). Because each batch takes t minutes. So for example, if d is 5 and t is 6 (like first example), then 5//6 is 0. So during the building time of 5 minutes, the first oven hasn't completed any batches. But if d is 6, then 6//6=1. So after 6 minutes, the first oven has completed one batch.

But wait, the first oven is running all the time. So during the building phase (time 0 to d), the first oven is active. So during that time, it can produce batches. So the number of batches is (d // t) multiplied by k. Then, after the second oven is built, both ovens are active. So after time d, the two ovens can start producing batches in parallel. Each batch takes t minutes. So the total cakes after building the second oven can be calculated.

So, the steps with building the second oven are:

1. During the building time d, the first oven produces some cakes: batches1 = d // t → cakes1 = batches1 * k.

2. The remaining cakes needed is rem = max(0, n - cakes1).

3. After time d, both ovens are active. Each oven can produce a batch every t minutes. So combined, they produce 2k cakes per t minutes.

   So the number of batches needed is ceil(rem / (2k)). The time for these batches is batches2 * t.

   So total time is d + batches2 * t.

But wait, the batches start after d minutes. So the total time is d + (batches2 * t). Because each batch takes t minutes. For example, if rem is 8 and 2k is 4 (like first example), then batches2 is 2 (8/4=2). So time is d (5) + 2*6= 5+12=17? Wait, but in the first example, the sample output says that with the second oven, the time is 11 minutes. Wait, I must be making a mistake here.

Wait, the first example input is n=8, t=6, k=4, d=5.

Original time without the oven: ceil(8/4)*6 = 2*6=12.

With the second oven:

Building time is 5 minutes. During those 5 minutes, first oven can produce 0 batches (5//6=0). So cakes1=0.

Remaining is 8-0=8.

After building, two ovens. Each produces 4 cakes every 6 minutes. So each batch of both ovens produces 8 cakes in 6 minutes. So for 8 cakes, they need 1 batch (8/8=1). So time is 5 + 6=11. Which is less than 12. So answer is yes.

Ah, right. So my initial approach is correct. So in that case, the code for batches2 is ceil(rem / (2*k)), and multiply by t.

So the time with building the oven is d + (ceil(rem/(2*k))) * t.

But what if rem is zero? That is, the cakes produced during the building phase are already enough. Then, the time would be just the time when the building is done and the remaining is zero. So in that case, the time is the building time d, but perhaps the first oven's batches during the building phase have already produced n cakes, but that's possible only if cakes1 >=n.

Wait, but in that case, if during the building phase, the first oven has already produced enough cakes, then building the second oven isn't needed, but the code would compare the two times.

Wait, but let's model that.

For example, suppose n=4, t=2, k=1, d=4.

Wait, the first example's fourth test case: input is 4 2 1 4. Output is YES.

Wait, let's see. Without building, how much time? 4 batches *2 =8.

With building:

Building takes 4 minutes. During that time, first oven can do 4//2=2 batches. So 2*1=2 cakes. Remaining is 4-2=2.

After building, two ovens. 2 cakes needed. Each oven can make 1 per 2 minutes. So two ovens produce 2 per 2 minutes. So 2/2=1 batch. Time is 4 + 2*1=6. Which is less than 8. So answer is yes.

So the calculation is correct.

So the steps are:

1. Compute time1 = ceil(n /k) * t.

2. Compute time2:

   a. batches_during_building = d // t.

   b. cakes_during = batches_during_building *k.

   c. rem = max(0, n - cakes_during).

   d. batches_after = ceil(rem/(2*k)).

   e. time2 = d + batches_after * t.

   f. However, if cakes_during >=n, then time2 is (batches_during_building *t). Because maybe the first oven already produced enough before the building is done.

Wait, this is a mistake. Because if during the building time (d minutes), the first oven has already produced enough cakes, then the time is the minimum between d and the time taken by the first oven to finish the required batches.

For example, suppose n=4, k=4, t=5, d=10.

So during building time d=10, the first oven can do 10//5=2 batches. So 2*4=8 cakes. If n is 5, then rem=5-8 would be negative, so rem=0. So batches_after is zero. But time2 would be d + 0*5 =10. But the first oven actually completed the required cakes at 2*5=10 minutes. Which is exactly when the building is done. So the time is 10.

But in the case where the first oven can finish before the building is done, the time is when the first oven finishes, not when the building is done.

Wait, no. The building takes d minutes. Suppose during that time, the first oven can produce enough cakes. Then the total time is the time when the first oven completes the required batches. But that may be earlier than d.

For example, let's say n=4, k=4, t=5, d=20.

The first oven can make 4 cakes every 5 minutes. Let's say during building time d=20, which is 4 batches (20//5=4). So 4*4=16 cakes. If n is 4, then after the first batch (5 minutes), the oven has made 4 cakes. So the time would be 5 minutes, which is less than d (20). But in this case, the building is still ongoing. So the total time is 5 minutes, because the first oven already produced enough.

So the time with building is the minimum between the time when the first oven finishes the required cakes and (d + ...). So in this case, the time2 is min(time_without_building, time_using_two_ovens).

Wait, but that's not correct. Because building the second oven takes d minutes, but if during the building phase, the first oven already made all the cakes needed, then building the second oven is not required, but the code's calculation of time2 would be the time when the first oven finishes. So the building is not done yet, but since the cakes are already there, the time is when the first oven finishes.

So for the case where during the building phase, the first oven produces enough cakes, the time2 is the same as time1. Because building the second oven didn't happen, but the code would think that the building process was started, but the first oven completed the cakes before the building was done.

Wait, but the problem says that Arkady can build the oven. So he starts building it, but if the first oven produces enough cakes before the building is done, then the process would finish earlier. So in that case, the time2 is the time when the first oven finishes, which is possibly earlier than d.

So how to model that?

Hmm. Let's think again. The building starts at time 0. The building takes d minutes, so the second oven is available at time d. But during those d minutes, the first oven is working. So each batch starts at time 0, t, 2t, etc. So the first oven's batches are completed at times t, 2t, 3t, etc. So during the building time (0 to d), the first oven can complete m batches, where m is floor(d / t). Then, after that, during the remaining time (d - m*t), the first oven is in the middle of a batch. But that batch will only complete at (m+1)*t. But the building completes at d. So if (m+1)*t <=d, then that batch completes before or during the building. Otherwise, it's still ongoing.

Wait, perhaps I'm overcomplicating this. Let's model the total cakes produced by the first oven during the building phase as m *k, where m is the number of batches completed. So m is (d) // t.

But during the building phase, the first oven starts a batch at time 0, which takes t minutes. So for example, if d is 5 and t is 6, then during 5 minutes, the first oven hasn't completed a batch. So m=0. If d is 6, then m=1. If d is 7, the first oven starts at 0, completes at 6. Then starts another batch at 6, which takes until 12. But the building completes at d=7, so during the building phase (0-7), the first oven has completed 1 batch. So m=7//6=1.

So the number of batches is indeed floor(d / t).

So the cakes during building are m*k. Then, after the building is done (time d), the first oven is in the middle of a batch that started at m*t. That batch will complete at (m+1)*t. But since the building is done at d, and both ovens are now active, the first oven's current batch (if any) is ongoing. So after time d, the first oven's next batch completion is (m+1)*t. Similarly, the second oven starts at time d, and can start its first batch at d. So the next completion for the second oven is d + t.

So after d, both ovens are active, but the first oven may be in the middle of a batch.

This complicates things. Because the first oven's next batch completion is (m+1)*t, and the second oven's next is d +t. So the earliest next completion is the minimum of those two times.

Hmm. But how to model the total time required after d to produce the remaining cakes.

This seems complicated, but perhaps there's a smarter way. Let's think about the optimal scenario when building the second oven. The total time is the minimum possible between the time when the first oven alone finishes (which is time1) and the time when building the second oven, and then using both.

But the problem says that Arkady can choose to build the oven. So even if building the oven is started but the first oven finishes before the building is done, the total time is the earlier of the two.

Wait, no. Because building the oven takes d minutes. So when you start building, you can't interrupt it. So if you start building and the first oven finishes before the building is done, then the total time is the time when the first oven finishes, because you already have enough cakes. But in that case, building the oven would not have been necessary. But the problem says to compare two scenarios: either build the oven or not. So in the scenario where you build the oven, the time is the minimum between the time when the first oven completes (if that happens during the building phase) or the time when the building is done plus the time to produce the remaining cakes with two ovens.

So the time for building the second oven scenario is the minimum between the time when the first oven alone would finish (which is time1) and the time when the building is done plus the time after building. Wait, no. Because once you start building the oven, you have to spend d minutes on it. So even if the first oven can finish before the building is done, the building process is ongoing. So in that case, the total time is when the first oven finishes, regardless of whether the building is done.

Wait, no. Because the building takes d minutes. So during those d minutes, the first oven is working. So if during that time, the first oven can produce all required cakes, then the building is not completed (since it takes d minutes), but the cakes are done. So the total time is when the first oven finishes. But in that case, building the second oven is not completed. So the process of building the oven is started but not completed. However, according to the problem statement, Arkady can build one more oven. So building the oven takes d minutes. So if he starts building, but before the building is done, he has enough cakes, then the total time is the time when the first oven finishes. But in that case, the building process is not completed, but the problem states that he can build at most one oven, which he has done (even if he didn't finish building it). Wait, no. Because the building takes d minutes. So if he starts building the oven, but the first oven finishes before d minutes, then he can't use the second oven. Because the building hasn't completed. So in that case, the building is not done, and the second oven is not available.

So in the scenario where he decides to build the oven, but the first oven finishes before the building is done, then the time is when the first oven finishes, and the building process is aborted. But the problem statement says he can build one more oven. So he can choose to build it, but if he starts building and the first oven can finish before the building is done, then the building is not completed, but he has to compare the time1 (without building) and the time when he stops building (but that's not possible, because building is a one-time process that takes d minutes, but if he stops building, then he doesn't have the second oven). Wait, this is getting complicated.

Alternatively, perhaps the building is a process that must be completed. Once started, it takes d minutes, and during that time, the first oven is working. After d minutes, the second oven is available. So the building process can't be interrupted. So even if the first oven finishes all the cakes during the building process, the building process continues. But in that case, the total time is when the first oven finishes. Because the cakes are already done. So the building process is irrelevant once the cakes are done. So the time in the scenario where building is started is the minimum between the time when the first oven finishes (during building) and the time when the building is done plus the time to produce the remaining cakes with two ovens.

So in code:

time2 = min(time1, time_after_building)

But time_after_building is d + batches_after *t.

Wait, but time1 is the time without building. But if during the building process, the first oven can produce the required cakes, then the time with building is the same as time1. Because the building process is ongoing, but the first oven finishes earlier, so the time is the same as if he didn't build. So in that case, building the oven doesn't help. So time2 is the same as time1.

Wait, that can't be right. For example, if during the building phase (d minutes), the first oven can produce all required cakes in m batches, where m*t <=d. Then the time with building is m*t, which is same as time1 (since time1 is ceil(n/k)*t). Wait, not necessarily. For example, if the building time is d=10, and the first oven can produce enough in 5 minutes. Then time1 would be 5 minutes (assuming n <=k). Then building the oven would take 10 minutes, but the first oven finishes in 5. So the time2 is 5, which is same as time1. So building the oven is not helpful. So the answer is no.

But in that case, the code would compute time2 as the minimum between m*t (5) and d + ... (which is 10 + ...). Since 5 is same as time1, the time with building is same as time without, so answer is no.

But how do we compute m*t?

Wait, m is the number of batches the first oven completes during building (d minutes). So m = d//t. So the cakes during building are m*k. If this is >=n, then the time needed is m*t. But m*t could be less than d. For example, t=5, d=10, m=2. Then m*t=10, which is same as d. But if t=3, d=7. Then m=7//3=2. So m*t=6. Which is less than d=7. So the first oven completes 2 batches (6 minutes), which is before the building is done (7 minutes). So the time2 in this case is 6 minutes, which is the same as the time1 (if the required cakes are 2*k, then time1 is 2*3=6).

So in this case, building the oven would not help, because the time2 is same as time1.

So the code for time2 is:

Compute the number of cakes produced during the building phase (d minutes) by the first oven: cakes_during = (d//t) *k.

If cakes_during >=n: then time2 is (d//t)*t. But that's same as time1 (since time1 is ceil(n/k)*t. If (d//t)*k >=n, then (d//t) >= ceil(n/k), so time1 is (d//t)*t. Wait, no. Suppose n=5, k=4. ceil(5/4)=2. So time1=2*t. If d//t=1, but 1*4=4 <5. So cakes_during=4. Then time2 is d + ... but if during building, the cakes are not enough.

So the code must first check if cakes_during >=n. If yes, then time2 is (d//t)*t. Else, after building the oven, both ovens are used. So the remaining cakes are rem =n - cakes_during. The number of batches needed is ceil(rem/(2k)), each taking t minutes. So time2 is d + batches_after * t.

So the time2 is:

if cakes_during >=n:

   time2 = (d//t)*t → but this is the time when the first oven completed the batches. Which could be less than d.

Else:

   time2 = d + ceil(rem/(2*k)) *t.

But then, we need to compare time2 (this scenario) with the time1. So the final time in the building scenario is the minimum between time1 and time2. Because if building the oven takes longer than time1, then building is not done. Wait, no. Because once the building is started, the time is the time to get the cakes, which could be either during the building phase (time1) or after. So the actual time when building is started is the minimum between the two possible outcomes: either the first oven finishes during building, or we have to wait for building and then produce the remaining.

So time_with_building = min( (m * t), (d + batches_after * t) )

But m*t is the time when the first oven finishes during building phase. However, m*t could be less than d. For example, t=3, d=7. m=2. m*t=6 <7. So the first oven finishes two batches in 6 minutes. If those two batches are enough (cakes_during >=n), then the time is 6. But in the building scenario, the building is started, but after 6 minutes, the cakes are done, so the building is aborted. So the time is 6, which is same as time1 (if time1 is 6). So in this case, building the oven is not helpful.

So the code for time_with_building is:

cakes_during = (d//t) *k

if cakes_during >=n:

   time_with_building = (d//t) * t

else:

   rem =n - cakes_during

   batches_after = ceil(rem/(2*k))

   time_with_building = d + batches_after *t

Then, compare time_with_building and time1. If time_with_building < time1 → output YES, else NO.

But wait, time_with_building could be (d//t)*t, which may be less than time1. For example, suppose n=4, k=1, t=2, d=4. So time1 is 4*2=8.

But when building, during d=4 minutes, the first oven can do 4//2=2 batches. So 2*1=2 cakes. rem=4-2=2. Then, batches_after=ceil(2/(2*1))=1. time_with_building =4 +1*2=6. Which is less than 8. So output YES.

But in the case where cakes_during >=n:

Suppose n=4, k=2, t=3. So time1 is 4/2=2 batches, 2*3=6.

If we build an oven with d=5. During d=5 minutes, the first oven can do 5//3=1 batch. So 2 cakes. Not enough. Then, after building, rem=2. batches_after=1. time_with_building=5+3=8. Which is larger than 6. So output is NO.

But if d=6. Then during building, 6//3=2 batches → 4 cakes. So rem=0. So time_with_building is 2*3=6, which is same as time1. So output is NO.

So the code needs to:

Compute time1 = ceil(n/k) * t.

Compute cakes_during = (d // t) *k.

if cakes_during >=n:

   time_with_oven = (d//t)*t → but this is the time taken by the first oven alone, which is same as time1 only if (d//t)*k >=n.

Wait, no. For example, if n=5, k=3, then ceil(5/3)=2. So time1=2t. If during building phase, (d//t) is 1, and 1*3=3 <5. So cakes_during is 3. So the code proceeds to the else clause.

But if d//t is 2, and 2*3=6 >=5. Then time_with_oven is 2t. Which is same as time1 (2t). So building the oven gives the same time. So output NO.

But time1 is 2t, which is the same as time_with_oven. So the code would output NO.

So the code's steps are:

Compute time1 = ceil(n /k) * t.

Compute cakes_during = (d // t) *k.

if cakes_during >=n:

   time_with_oven = (d//t)*t.

else:

   rem =n - cakes_during

   batches_after = (rem + 2*k -1) // (2*k) # ceil division

   time_with_oven = d + batches_after * t.

if time_with_oven < time1 → YES else NO.

So the code must compute these two times and compare.

So for the problem's test cases:

First example:

n=8, t=6, k=4, d=5.

time1= (8/4)*6=12.

cakes_during: d//t=5//6=0 → 0*4=0 <8. So rem=8.

batches_after=8/(2*4)=1 → 8/(8)=1. So time_with_oven=5 +1*6=11 <12 → YES.

Second example:

n=8, t=6, k=4, d=6.

time1=12.

cakes_during:6//6=1 →4 cakes. rem=4.

batches_after=4/(8)=0.5 → ceil to 1 → time_with_oven=6+6=12. So time_with_oven=12. So 12 is not less than 12 → NO.

Third example:

n=10, t=3, k=11, d=4.

time1: ceil(10/11)=1 → 3*1=3.

cakes_during:4//3=1 →11 cakes. 11 >=10 → time_with_oven=3. Which is same as time1 → NO.

Fourth example:

n=4, t=2, k=1, d=4.

time1=4*2=8.

cakes_during:4//2=2 →2*1=2 <4. rem=2.

batches_after=ceil(2/(2*1))=1 → time_with_oven=4+2=6 <8 → YES.

So the code seems to handle all these cases.

Now, the code must read the four integers n, t, k, d.

Compute time1.

Compute cakes_during = (d // t) *k.

If cakes_during >=n:

   time_with_oven = (d//t) *t.

Else:

   rem =n - cakes_during.

   batches_after = (rem + 2*k -1) // (2*k)

   time_with_oven = d + batches_after *t.

Then, compare time_with_oven < time1 → YES else NO.

Now, code in Python.

But wait, the code needs to handle the case when k is zero? No, according to the constraints, all variables are >=1. So k is at least 1.

So code steps:

Read n, t, k, d.

time1 = ((n +k -1)//k) *t

Then:

m = d // t

cakes_during = m *k

if cakes_during >=n:

   time2 = m *t

else:

   rem =n - cakes_during

   batches_after = (rem + 2*k -1) // (2*k)

   time2 = d + batches_after * t

if time2 < time1:

   print("YES")

else:

   print("NO")

Yes.

Now, code:

n, t, k, d = map(int, input().split())

time1 = ((n + k -1) //k) * t

m = d // t

cakes_during = m *k

if cakes_during >=n:

    time2 = m *t

else:

    rem = n - cakes_during

    batches_after = (rem + 2*k -1) // (2*k)

    time2 = d + batches_after * t

print("YES" if time2 < time1 else "NO")

Wait, let's test the first example:

Input:8 6 4 5

time1: (8+4-1)//4= (11//4)=2 →2*6=12.

m=5//6=0 →0. cakes_during=0<8.

rem=8.

batches_after= (8 +8-1) //8 →15//8=1. 1*6=6. time2=5+6=11 <12 →YES.

Second example:

8 6 4 6.

time1= (8+4-1)//4= (11//4=2) →12.

m=6//6=1 →4. rem=8-4=4.

batches_after= (4+8-1)//8 → (11)//8=1. time2=6+6=12. 12 not <12 →NO.

Third example:

n=10, t=3, k=11, d=4.

time1= (10 +11-1)//11 →20//11=1 →3*1=3.

m=4//3=1 →11 >=10. time2=3. 3 not <3 →NO.

Fourth example:

n=4, t=2, k=1, d=4.

time1= (4+1-1)//1=4 →4*2=8.

m=4//2=2 →2*1=2 <4.

rem=2.

batches_after= (2+2-1)//2 → (3)//2=1 →1*2=2. time2=4+2=6 <8 → YES.

All tests pass.

Another test case:

Input:

4 2 1 4 → output YES.

Yes.

So the code should work.
</think>

```python
n, t, k, d = map(int, input().split())

time_with_one = ((n + k - 1) // k) * t
m = d // t
cakes_during = m * k

if cakes_during >= n:
    time_with_two = m * t
else:
    rem = n - cakes_during
    batches_after = (rem + 2 * k - 1) // (2 * k)
    time_with_two = d + batches_after * t

print("YES" if time_with_two < time_with_one else "NO")
```