<think>
Okay, let's see. The problem is about scheduling Devu's songs and Churu's jokes such that the total time doesn't exceed D minutes. We need to maximize the number of jokes. Hmm.

First, let's understand the constraints. Devu has to sing all his songs. Each song is followed by a 10-minute rest, except the last one. Oh right, because after the last song, he doesn't need rest anymore. So the total time Devu's part takes is sum of all ti plus 10*(n-1) minutes for the rests. Wait, right. Because after each song except the last, there's a 10-minute rest. So if there are n songs, there are n-1 rests. So the minimal time required for Devu's part is sum(ti) + 10*(n-1). If that's already larger than D, then output is -1.

So first step: calculate the minimal time required. If that's more than D, return -1. Otherwise, the remaining time can be filled with jokes. Each joke is 5 minutes. So the maximum possible jokes would be (remaining_time) // 5. Because each joke is 5 minutes. But wait, how to arrange the remaining time?

But wait, maybe the arrangement allows more jokes by inserting them between the songs. Like, before Devu starts, between songs, and after all songs. Because the rests are only after each song except the last. Oh, but the rests are part of Devu's time. Wait no: the problem says Devu needs a rest of 10 minutes after each song. So the rest is part of the schedule. So during those rests, can Churu perform jokes? Because the rest time is part of the event's time. So the rest time is already accounted for in the Devu's required time. So the schedule must include Devu's songs and rests. Then, any additional time left can be filled with jokes.

Wait, no. Wait, let's read the problem statement again. The total duration must be no more than D. The Devu must complete all songs, which implies that the songs and the required rests must fit into the time. Then, during the rest periods, or other times, Churu can do jokes. But how?

Wait, the problem says that the rest is 10 minutes after each song. So perhaps during those 10 minutes, Churu can do his jokes. Or maybe those 10 minutes are part of the required time, and any jokes must be scheduled in between. Hmm, this is a bit ambiguous. Let's look at the note from the first example.

In the first example, the schedule is:

Churu does a 5-minute joke.

Then Devu's first song (2 mins).

Then Churu does 2 jokes (10 mins total) during the rest period.

Then Devu's second song (2 mins).

Then Churu does 2 jokes (10 mins) during the rest.

Then Devu's last song (1 min).

Total time is 5+2+10+2+10+1=30.

Wait, so the rest periods are after each song. So after the first song, there's a 10-minute rest. But in that time, Churu can do jokes. So during those 10 minutes, he can do two jokes (each 5 mins). So those 10 minutes are part of the total time, and the jokes are placed in that time. So the total time for Devu's part is sum(ti) plus 10*(n-1) as before. But then, any remaining time after that can also be filled with jokes. Wait, no. Because the total time is allowed to be up to D. So the sum of Devu's time (songs and rests) plus the time for Churu's jokes must be <= D.

Wait, I think I had this wrong. Let's re-express the problem.

The total event time is the sum of:

- All Devu's songs (sum(ti)).

- All rests (10*(n-1) minutes).

- All jokes (each 5 minutes).

But the total of this sum must be <= d.

But also, the jokes can be placed anywhere in the schedule. So the rests are mandatory and part of the time. Then, the jokes can be inserted into the schedule in any order as long as the order of Devu's songs is preserved and the rests are after each song (except last). But during the rests, perhaps Churu can perform jokes. Or, perhaps the rests are fixed time periods where only rest is allowed. Wait, the problem statement says:

"People have mainly come to listen Devu. But you know that he needs rest of 10 minutes after each song. On the other hand, Churu being a very active person, doesn't need any rest."

So the rest is required for Devu. But during those 10 minutes, can Churu perform jokes? Because Churu doesn't need rest. So those 10 minutes are part of the schedule, and during those minutes, Churu can perform as many jokes as possible (each taking 5 minutes). So the 10-minute rest period can be filled with two jokes (2*5=10). Or if the rest is 10 minutes, then after Devu's song, there's 10 minutes, which Churu can fill with two jokes, which is exactly 10 minutes. So that way, the rests are used for jokes.

Alternatively, maybe the rests are mandatory and can't be used for anything else. But according to the first example's explanation, that's not the case. In the example, the first rest after the first song is filled with two jokes (10 minutes), which is the rest time. So the rest time is filled by the jokes.

So the key is: the rest time after each song (10 minutes) is a time that can be used for Churu's jokes. But also, there can be additional time before the first song, between songs (but after the rest?), or after all the songs. Wait, but the rest is after each song. So the rest is after each song, and during that rest, the 10 minutes can be used for jokes.

Additionally, any time before the first song can be filled with jokes. And after the last song's rest (but there's no rest after the last song) can be filled with jokes.

Wait, the rest occurs after each song except the last one. So after the last song, there's no rest. So after the last song, any remaining time can be filled with jokes.

So the total time is structured as follows:

Time can be divided into slots where:

- Before the first song: any number of jokes (each 5 mins) can be placed here. The total time here is x *5 mins.

- Then, Devu's first song (t1 mins). Then, 10 mins of rest (which can be filled with jokes). Then, song 2 (t2 mins). Then 10 mins rest (filled with jokes), and so on until the nth song. After the nth song, no rest. Then, any remaining time can be filled with jokes.

So the structure is:

[Churu's jokes] [Devu's song] [10-min rest (jokes)] [Devu's song] [10-min rest (jokes)] ... [Devu's song] [Churu's jokes]

The 10-min rest after each song (except last) must be filled with exactly 2 jokes each (since 2*5=10). Because during the rest, you can fit two jokes. Because otherwise, if you put less than two, there's remaining time which can't be filled (since each joke is 5 mins). Wait, but the rest is 10 minutes, so exactly two jokes. So for each rest slot, there are two jokes. So the number of jokes from the rest periods is 2*(n-1).

Then, the remaining time is:

Total available time: d.

The minimal required time for Devu is sum(ti) + 10*(n-1). Wait no: because during the 10 minutes of rest, Churu is performing two jokes (each 5 mins, total 10 mins). So the sum of Devu's time (songs and rests) is sum(ti) + 10*(n-1). But during the rests, Churu's jokes are filling that time. So the total time for Devu's part is sum(ti) + 10*(n-1). The jokes during the rests are part of the total time. So the total time for the event is sum(ti) + 10*(n-1) + (other jokes' time). Wait, no. Wait, the rests are part of the event time. But during those rests, Churu's jokes are filling that time. So the rests' time is exactly 10*(n-1) minutes, which is covered by two jokes per rest (2*(n-1)*5 = 10*(n-1) minutes). So the total time for Devu's part plus the rest is sum(ti) + 10*(n-1). Then, any additional time can be used for Churu's jokes either before the first song, between the song and rest (but after the song and before the rest?), or after the last song. Wait, no. Because the rest is after each song. So the structure is:

pre: jokes before first song.

then song 1, then rest (jokes), song 2, rest (jokes), etc. Then after song n, there's no rest, so we can have jokes.

So the total time is:

pre_jokes_time + sum(ti) + 10*(n-1) + post_jokes_time.

But the rests are 10*(n-1) minutes, which are filled by 2*(n-1) jokes.

So the total time is:

pre_jokes_time + sum(ti) + 10*(n-1) + post_jokes_time <= d.

But sum(ti) + 10*(n-1) is fixed. So the remaining time is d - (sum(ti) + 10*(n-1)) = remaining_time. This remaining_time must be >=0 (otherwise, it's impossible). If it's negative, output -1.

Then, this remaining_time can be split into pre and post jokes. But how to maximize the total number of jokes. Since each joke is 5 minutes, the maximum possible is remaining_time //5. Because the order of pre and post doesn't matter as long as the sum is <= remaining_time. So the maximum possible is (remaining_time) //5. So total jokes is 2*(n-1) + (remaining_time //5).

Wait, no. Because the rests are already accounted for in the 10*(n-1) minutes. The 2*(n-1) jokes are part of those rests. So total jokes from rests are 2*(n-1). Then, the remaining_time is d - (sum(ti) + 10*(n-1)). Then, the number of jokes that can fit in the remaining_time is (remaining_time //5). So the total jokes is 2*(n-1) + (remaining_time //5).

But wait, the remaining_time can be split into pre and post. But regardless of how you split, the maximum is (remaining_time //5) since each joke is 5 minutes. So adding that to the rest's 2*(n-1) gives the total.

So the steps are:

1. Compute the minimal time required for Devu's part: sum(t) + 10*(n-1).

   If this is greater than d, output -1.

2. Else, compute remaining_time = d - (sum(t) +10*(n-1)).

3. The maximum jokes is 2*(n-1) + (remaining_time //5).

But wait, wait. Let's check the first example:

Sample input 1:

3 30

2 2 1

sum(t) = 5. 10*(3-1)=20. sum+rest=25. remaining_time=30-25=5. 5//5=1. So total jokes is 2*(2) +1=5. Which matches the sample output.

Yes. So the approach seems correct.

Sample input 2:

3 20

sum(t) is 4. 10*(3-1)=20. sum+rest=24, which is more than d=20. So output is -1.

Another example:

Let's say n=1, d=5. t1=5.

sum(t) + 10*(0) =5. d=5. remaining_time=0. So jokes from rest: 0. plus 0//5=0. total 0. But wait, can we have jokes before or after?

Wait, when n=1, there's no rest. So the schedule is:

pre_jokes + song1 + post_jokes.

The song is 5 minutes, and the rests are zero. So sum(t)+rests is 5. So remaining_time is d -5 =0. So the jokes can be 0. But the problem requires that Devu's songs are completed, which they are. So maximum jokes is 0.

So the formula works here.

Another test case: n=2, d=25. t1=2, t2=3. Sum(t) =5. Rests:10*(1)=10. Sum+rest=15. d=25. remaining_time=10. 10//5=2. So total jokes is 2*(1) + 2 =4. But where?

The structure would be:

pre: 10 minutes (2 jokes). Then song1 (2), then rest (10: 2 jokes). Then song2 (3). Then post_jokes: 0 (since remaining_time was 10, but sum(t)+rest is 15, d=25. 25-15=10. So pre and post can be 10 minutes. But how? Because pre is before song1, and post is after song2.

Wait, the remaining_time is 10. So the maximum number of jokes is 10//5=2. So total jokes is 2*(n-1) + 2 = 2 +2=4. So total 4 jokes. So for example, 10 minutes of pre, then song1, rest (2 jokes), song2, then 0 post.

Alternatively, 0 pre, song1, rest (2), song2, then 10 minutes (2 jokes). Either way, total is 4.

So the formula is correct.

So the algorithm is:

Calculate the minimal time needed: sum_t = sum(t_i) + 10*(n-1).

If sum_t >d: output -1.

Else:

remaining_time =d - sum_t.

jokes = 2*(n-1) + (remaining_time //5).

But wait, why? Because the rests after each song (n-1 of them) take 10 minutes each, which allows exactly 2 jokes each. So 2*(n-1) jokes from the rests, plus as many as possible from the remaining_time (each 5 mins). So the total is correct.

Thus, the steps are straightforward.

Now, coding this.

In Python:

Read n and d.

Read list of ti.

sum_t = sum(ti) + 10*(n-1)

if sum_t >d: print(-1)

else:

remaining = d - sum_t

jokes = 2*(n-1) + (remaining //5)

print(jokes)

But wait, what if remaining is negative? No, because sum_t <=d, so remaining is >=0.

So code:

n, d = map(int, input().split())

t = list(map(int, input().split()))

sum_t = sum(t) + 10*(n-1)

if sum_t > d:

    print(-1)

else:

    remaining = d - sum_t

    jokes = 2*(n-1) + (remaining //5)

    print(jokes)

Testing the first sample:

Sample 1:

n=3, d=30.

t = [2,2,1]

sum_t=2+2+1 +10*(2) =5 +20=25. 25<=30. remaining 5.

jokes=2*2 +5//5=4+1=5. Correct.

Sample 2:

n=3, d=20.

sum_t = 2+1+1 +20=4+20=24. 24>20. Output -1.

Another test case where remaining_time is 12. Then 12//5=2 (10 mins used), so jokes added is 2.

Yes.

Another edge case: n=1, d=5, t=5. sum_t=5. remaining=0. jokes=0+0=0.

Another case: n=1, d=10, t=5. sum_t=5. remaining=5. jokes=0 +5//5=1. So total 1 joke.

So before the song, 5 mins (1 joke), then the song, then 0. Or after the song, 5 mins. Either way, 1 joke.

So code is correct.

So the code is straightforward. The key insight was to realize that the rests are 10 minutes each and can be filled with exactly 2 jokes. The remaining time can be filled with as many jokes as possible, regardless of where they are placed.

Thus, this code should work and handle all cases efficiently.
</think>

```python
n, d = map(int, input().split())
t = list(map(int, input().split()))
required = sum(t) + 10 * (n - 1)
if required > d:
    print(-1)
else:
    remaining = d - required
    print(2 * (n - 1) + remaining // 5)
```