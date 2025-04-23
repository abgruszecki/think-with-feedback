<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about finding the minimal time for Edward to get from his apartment to Natasha's. The building has some circular structure for the entrances. So entrances are arranged in a circle. The main points are about moving between entrances, using stairs or elevator, and considering the best path.

First, I need to model the positions of both apartments. Each apartment's entrance, floor, and position within the floor can be determined. But since each floor has exactly k apartments, and each entrance has m floors, the way to compute entrance, floor, and position is similar to converting the apartment number into a coordinate.

Let's think about how to convert a apartment number to its entrance, floor, etc. For a given apartment number x:

Total apartments per entrance: m * k. So entrance number is (x-1) // (m*k) + 1. But wait, since entrances are numbered 1 to n, if the result is more than n, that's not possible. Wait, no. The input a and b are guaranteed to be within 1 to n*m*k, so x will be in that range. So entrance is ((x-1) // (m*k)) + 1. Then, within entrance, the remaining apartments are (x-1) % (m*k) + 1. Then, floor is (remaining-1) // k + 1. And the position on the floor is (remaining-1) % k +1, but maybe we don't need the position since it's only about the entrance and floor. Because moving within the same entrance's same floor is instant. So for the problem, the important parts are the entrance and the floor.

So for both a and b, we need to compute their entrance (p_ed, p_na), floor (f_ed, f_na), and maybe the position (but perhaps not needed).

Once we have these, Edward needs to get from his entrance and floor to Natasha's entrance and floor, possibly moving through different entrances and floors, choosing between stairs or elevator, and directions around the building (clockwise or counter-clockwise).

The key steps are:

1. Compute the entrance and floor of Edward and Natasha.

2. Calculate the minimal time considering all possible paths: using stairs, using elevator, and choosing the direction (clockwise or counter-clockwise) when moving between entrances.

Let's think about the possible steps Edward can take:

Option 1: Use stairs to go down to the first floor of his entrance, then move around the building to Natasha's entrance (either direction), then use stairs to go up to her floor.

Option 2: Take the elevator down to the first floor (waiting 10 seconds, then time for elevator to go from his floor to first), then move around, then take stairs up.

Option 3: Take stairs to first floor, move around, take elevator up to her floor.

Option 4: Take elevator to first, move around, take elevator to her floor.

Additionally, when moving between entrances, the time depends on the number of entrances he passes through. For example, in a circular arrangement of n entrances, the minimal steps between entrance A and B can be either (B - A) mod n steps clockwise or (A - B) mod n steps counter-clockwise. The minimal of these two is the minimal number of steps, each step taking 15 seconds. But perhaps he can choose the direction with the least steps, then multiply by 15.

Wait, the problem states that Edward can choose to go in either direction. So the minimal time to move between entrances is the minimal of the two possible directions. For example, if there are 4 entrances, moving from 1 to 4 can be done by going clockwise (3 steps: 1→2→3→4 →3 steps ×15 = 45) or counter-clockwise (1 step: 1→4 →15 seconds). So the minimal is 15. So the number of steps between the two entrances is the minimal of (d, n -d), where d is the clockwise distance. So for entrance p_ed and p_na, d_clock = (p_na - p_ed) % n. The steps would be min(d_clock, n -d_clock), each step 15 seconds.

So first, compute the minimal steps between the two entrances. Let's call this steps_entrance, time_entrance = steps_entrance *15.

Now, once Edward is at the entrance, he can get to the first floor instantly. So the problem is: how to get from his current floor (f_ed) to first floor, then move steps_entrance entrances, then get from first floor to Natasha's floor (f_na), in the minimal time.

But there are other possibilities. For example, Edward might choose to use the elevator in his entrance to get to the first floor, then walk around, then use stairs or elevator in Natasha's entrance. Or he could take the stairs to first, then walk around, then take elevator. Or perhaps even take the elevator both ways. So all combinations of using elevator or stairs for the departure and arrival need to be considered.

So for each of the departure (from Edward's floor) and arrival (to Natasha's floor) steps, there are two options: stairs or elevator. So four possible combinations:

1. Stairs down, stairs up.

2. Stairs down, elevator up.

3. Elevator down, stairs up.

4. Elevator down, elevator up.

But wait, Edward is starting in his apartment. To get to the first floor of his entrance, he can choose between stairs (time: 5 seconds per floor) or elevator (10 seconds wait + 1 per floor). Similarly for Natasha's entrance: once he arrives at the entrance, he's on first floor, and needs to get to her floor. He can use stairs (5 per floor) or elevator (call elevator, which takes 10 seconds, then 1 per floor). But he has to make that choice for both ends.

Wait, but when he arrives at Natasha's entrance, he's on the first floor. So to get to her floor (f_na), he can choose between stairs (time (f_na -1)*5 seconds) or elevator (time 10 + (f_na -1)*1). So that's two options.

Similarly, for leaving Edward's entrance: he's on floor f_ed. To get to first floor, he can take stairs (time (f_ed -1)*5) or elevator (10 + (f_ed -1)*1).

So the four possibilities are:

1. Stairs down (time: (f_ed -1)*5), then stairs up (time: (f_na -1)*5).

2. Stairs down (time: (f_ed -1)*5), elevator up (time: 10 + (f_na -1)*1).

3. Elevator down (time: 10 + (f_ed -1)*1), stairs up (time: (f_na -1)*5).

4. Elevator down (time: 10 + (f_ed -1)*1), elevator up (time: 10 + (f_na -1)*1).

But also, for each of these, we have the time for moving between entrances (time_entrance = steps_entrance *15). So for each of the four options, the total time is:

time_down (stairs or elevator) + time_entrance + time_up (stairs or elevator).

So the minimal time is the minimal of all these four options, plus the minimal time_entrance.

But wait, the steps_entrance depends on the direction chosen. Wait, no: the steps_entrance is the minimal number of steps between the two entrances. Because Edward can choose the direction with the least steps, and the time is steps_entrance ×15. So steps_entrance is the minimal possible.

So first, compute steps_entrance as the minimal between the clockwise and counter-clockwise directions.

Once that's determined, the time_entrance is fixed as steps_entrance ×15.

So the total time would be:

(time to get from f_ed to first) + (steps_entrance ×15) + (time to get from first to f_na).

So the four combinations for stairs and elevator are:

For the departure:

Stairs: (f_ed -1)*5

Elevator: 10 + (f_ed -1)*1

For the arrival:

Stairs: (f_na -1)*5

Elevator: 10 + (f_na -1)*1

Then, the four possible combinations are:

stairs_down + stairs_up

stairs_down + elevator_up

elevator_down + stairs_up

elevator_down + elevator_up

So the minimal among these four, plus the steps_entrance ×15.

Wait, but what if Edward and Natasha are in the same entrance? Then steps_entrance is zero, so time_entrance is zero. Then, Edward is already on his entrance's first floor (after getting down) and needs to move up to Natasha's floor. But in that case, the steps_entrance is zero, so time_entrance is zero. So the total time would be (time to get down) + (time to get up). But if they are in the same entrance, then the steps_entrance is zero, so Edward can just go down to first (if needed) and then up. Wait, but if they are in the same entrance, then after getting down to first, moving between entrances (steps_entrance=0), then up to Natasha's floor.

But in that case, the movement between entrances is zero. So the time_entrance is zero. So the time is the sum of the time to get down and up.

But what if Edward's apartment is already on the first floor, and Natasha's is on the same entrance but higher floor. Then, he can take stairs or elevator up.

So, the algorithm is:

1. Compute the entrance and floor for a and b.

2. If entrances are same, then the time_entrance is zero. So the options are:

   a. Take stairs down (0 time, since already on first floor?), wait no: if Edward's floor is not first, then he has to get down. Wait, no, the problem says that Edward can exit the entrance only from the first floor. So regardless of his starting floor, he needs to get to the first floor of his entrance. So even if he is on the first floor, getting down takes 0 time. But if he is on the first floor, then the time to get down via stairs is zero. Similarly, elevator would take 10 seconds (waiting) plus zero movement. So for same entrance, Edward can choose between stairs (time 0) or elevator (10 seconds). But that's worse. So in that case, he must take stairs to get down (no time if he's already on first), then take stairs or elevator up.

Wait, Edward is in his entrance's floor f_ed. To exit the entrance, he must be on the first floor. So regardless of his starting floor, he needs to get down to first. So even if he is on first, he is already there, so time to get down is zero. So for same entrance:

time_down (stairs: (f_ed-1)*5, elevator: 10 + (f_ed-1)*1) → but if f_ed is 1, stairs down is 0, elevator is 10. So in that case, he would choose stairs.

Then, he is on first floor. Then, time_entrance is zero. Then, he needs to get up to f_na. So time_up can be stairs (f_na-1)*5 or elevator 10 + (f_na-1)*1.

So for same entrance, total time is (time_down) + (time_up). So the four possibilities are same as before.

So the steps are:

For all cases, whether same entrance or not, compute the minimal steps_entrance (which is zero if same entrance) and time_entrance (steps_entrance ×15). Then, compute the four possible combinations of stairs and elevator for getting down and up, sum each with time_entrance, and find the minimal.

So the steps to compute the minimal time are:

Compute for both a and b their entrance (p1, p2) and floor (f1, f2).

Compute the clockwise distance between p1 and p2: (p2 - p1) % n.

Then, the minimal steps_entrance is min(d_clock, n - d_clock), since Edward can choose the direction with fewer steps.

Then, time_entrance is steps_entrance *15.

Then, for the four combinations of departure and arrival methods (stairs/elevator), compute the total time.

The minimal of these four plus time_entrance is the answer.

So the code steps are:

1. Read n, m, k.

2. Read a and b.

3. Compute for a: entrance p1, floor f1.

4. Compute for b: entrance p2, floor f2.

5. Compute d_clock = (p2 - p1) % n.

   steps_entrance = min(d_clock, n - d_clock).

   time_entrance = steps_entrance *15.

6. Compute the four possible combinations:

   a. stairs_down + stairs_up.

      time_down = (f1 -1) *5.

      time_up = (f2 -1)*5.

      total = time_down + time_entrance + time_up.

   b. stairs_down + elevator_up.

      time_down = (f1-1)*5.

      time_up = 10 + (f2-1)*1.

      total = time_down + time_entrance + time_up.

   c. elevator_down + stairs_up.

      time_down = 10 + (f1-1)*1.

      time_up = (f2-1)*5.

      total = ... same.

   d. elevator_down + elevator_up.

      time_down = 10 + (f1-1)*1.

      time_up = 10 + (f2-1)*1.

      total = ... same.

7. The minimal of these four totals is the answer.

Wait, but what about when the two are in the same entrance (steps_entrance is 0). Then, time_entrance is zero, so the total is time_down + time_up.

But in that case, what about the time between the two floors? For example, if Edward is on floor 5, and Natasha is on 3. Then, Edward can take stairs down to first (4 floors ×5 =20) then take stairs up to 3 (2 floors ×5=10) → total 30. Or take elevator down (10 +4=14) then elevator up (10 +2=12 → total 14+12=26). Or any combination. So the four possibilities are still valid.

So the code is correct for same entrance as well.

So the code structure is:

First, write a function to get p and f from a given x.

Then, compute the four options and select the minimal.

Let's test this logic against the examples.

First example:

Input:

4 10 5

200 6

So n=4, m=10, k=5. So per entrance, 10*5=50 apartments.

a=200. Let's compute p1 and f1.

200-1=199.

199 // (10*5) = 199 //50=3. So p1=3+1=4.

199 %50=199-3*50=199-150=49.

49 //5=9 → floor is 9+1=10.

So p1=4, f1=10.

b=6:

6-1=5.

5//50=0 → p2=1.

5%50=5.

5//5=1 → floor is 1+1=2.

So p2=1, f2=2.

d_clock = (1 -4) mod4 = ( -3) mod4 = 1? Because (1-4) is -3, mod4 is 1 (since 4* (-1) =-4, -3 - (-4) =1). So d_clock is 1.

n-d_clock = 4-1=3. So steps_entrance is 1. time_entrance 15*1=15.

Now compute the four options:

Option a: stairs_down + stairs_up.

f1-1=9 → 9*5=45. f2-1=1 →5. Total 45+15+5=65.

But in the example, the answer is 39.

Wait, this is conflicting. Wait, what's the example's explanation.

In the first example, Edward is in entrance 4, floor 10. Natasha in entrance 1, floor 2.

The steps_entrance is min(1, 3) →1. So time_entrance 15.

So according to the options, the four possibilities are:

a. stairs down (9*5=45) + stairs up (1*5=5). Total 45+15+5=65. But the example's answer is 39. So why the discrepancy?

Ah, because the example uses elevator for the down and stairs for up.

Wait, in the example's explanation, Edward uses elevator down: 10 seconds wait plus 9 floors (from 10 to 1 →9 steps ×1 sec →9 sec) → total 19. Then, time_entrance 15 (steps_entrance 1), then stairs up (5 sec). Total 19+15+5=39.

So this is option c: elevator_down (10+9=19) + stairs up (5). So total 19 +15 +5=39. Which is better than option a's 65.

So the code's approach would compute the four options and select the minimal. So in this case, option c gives 19+15+5=39, which is indeed the minimal.

So the code would compute all four options and take the minimal.

So the code's approach is correct.

Second example:

Input:

3 1 5

7 2

So n=3, m=1, k=5.

a=7: per entrance, m*k=5 apartments. 7-1=6. 6//5=1. So entrance 1+1=2. 6%5=1. floor is (1//5=0) +1=1. So p1=2, f1=1.

b=2: 2-1=1. 1//5=0 →p2=1. 1%5=1 →floor 1.

So p1=2, p2=1. d_clock = (1-2) mod3 → ( -1) mod3 →2. steps_entrance= min(2, 3-2=1) →1. time_entrance=15*1=15.

But wait, steps_entrance is 1. So moving from entrance 2 to 1: minimal steps is 1 (counter-clockwise, as 3 entrances, 2 to 1 is 1 step counter-clockwise, which is same as 2 steps clockwise. So minimal is 1). So time_entrance is 15.

Now, compute the four options:

f1=1 → stairs_down time is 0 (f1-1=0). elevator_down: 10 +0=10.

For f2=1: stairs_up is 0, elevator_up is 10+0=10.

So four options:

a: 0 +15 +0 →15.

b:0 +15+10 →25.

c:10 +15+0 →25.

d:10+15+10 →35.

So minimal is 15. Which matches the sample output.

So the code's approach works.

So the code is correct.

Now, the code must compute for a and b their p and f, then steps_entrance, then the four options.

Now, code structure:

Read n, m, k.

Read a and b.

Compute p1, f1 from a.

Compute p2, f2 from b.

Compute d_clock = (p2 - p1) %n.

steps_entrance = min(d_clock, n -d_clock).

time_entrance = steps_entrance *15.

Compute four options:

option1 = (f1-1)*5 + (f2-1)*5 + time_entrance.

option2 = (f1-1)*5 + (10 + (f2-1)*1) + time_entrance.

option3 = (10 + (f1-1)*1) + (f2-1)*5 + time_entrance.

option4 = (10 + (f1-1)*1) + (10 + (f2-1)*1) + time_entrance.

minimal_time = min(option1, option2, option3, option4).

Print minimal_time.

But wait, in code, how to compute p1 and f1?

For a given x (a or b), compute:

entrance_p = (x-1) // (m*k) +1.

But since m and k can be up to 1e3, m*k can be up to 1e6. Then x can be up to 1e3 *1e3 *1e3 =1e9, but (x-1) // (m*k) is manageable as integer division.

Wait, but in Python, integer division is done with //.

So for x:

entrance = (x-1) // (m * k) + 1

But since the problem allows n up to 1e3, but (x-1)//(m*k) could be up to (n*m*k-1)//(m*k) = n-1, so entrance is up to n. Which is correct.

Then, remaining = x - (entrance-1)*m*k.

Then, floor = (remaining -1) //k +1.

Yes.

Wait, no: after entrance, the remaining apartments are (x-1) % (m*k) +1.

Wait, let's see:

For x, the entrance is p = (x-1) // (m*k) +1.

Then, the position within the entrance is (x-1) % (m*k) +1. Let's call this rem.

Then, floor is (rem-1) //k +1.

Yes.

So code for a:

def get_p_f(x):

    per_entrance = m *k

    p = (x-1) // per_entrance +1

    rem = x - (p-1)*per_entrance

    # rem is 1-based within entrance.

    f = (rem-1) //k +1

    return p, f

Wait, for example, x=1: (1-1)// (m*k) =0 →p=1. rem=1. (0)//k=0 →f=1.

For x=5, m=1, k=5: rem=5. (5-1)//5=0 →f=1.

x=6: (6-1) //5=1 → rem=6-5=1. (1-1)//5=0 →f=1.

Yes.

So the code can compute p and f correctly.

Now, code:

Read n, m, k.

a, b = map(int, input().split())

Compute p1, f1 = get_p_f(a)

Compute p2, f2 = get_p_f(b)

Compute d_clock = (p2 - p1) %n

steps_entrance = min(d_clock, n -d_clock)

time_entrance = steps_entrance *15

Compute the four options:

option1 = (f1-1)*5 + (f2-1)*5 + time_entrance

option2 = (f1-1)*5 + (10 + (f2-1)*1) + time_entrance

option3 = (10 + (f1-1)*1) + (f2-1)*5 + time_entrance

option4 = (10 + (f1-1)*1) + (10 + (f2-1)*1) + time_entrance

minimal_time = min(option1, option2, option3, option4)

print(minimal_time)

But wait, the code should not have any debug outputs. So no prints except the final answer.

This code should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().rstrip("\n").split())
    a, b = map(int, input_stream.readline().rstrip("\n").split())

    def get_p_f(x):
        per_entrance = m * k
        p = (x - 1) // per_entrance + 1
        rem = x - (p - 1) * per_entrance
        f = (rem - 1) // k + 1
        return p, f

    p1, f1 = get_p_f(a)
    p2, f2 = get_p_f(b)

    d_clock = (p2 - p1) % n
    steps_entrance = min(d_clock, n - d_clock)
    time_entrance = steps_entrance * 15

    option1 = (f1 - 1) * 5 + (f2 - 1) * 5 + time_entrance
    option2 = (f1 - 1) * 5 + (10 + (f2 - 1) * 1) + time_entrance
    option3 = (10 + (f1 - 1) * 1) + (f2 - 1) * 5 + time_entrance
    option4 = (10 + (f1 - 1) * 1) + (10 + (f2 - 1) * 1) + time_entrance

    print(min(option1, option2, option3, option4), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 1 5
7 2
""",
            "output": \
"""\
15
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

Sample input 2:

3 1 5

7 2.

a=7:

per_entrance=1*5=5.

p1=(7-1)/5=6/5=1 →p1=1+1=2.

rem=7- (2-1)*5=7-5=2.

f1=(2-1)//5 +1 →0 +1=1.

b=2:

p2=(2-1)/5=0 →1.

rem=2.

f2= (2-1)//5 +1=0+1=1.

d_clock=(1-2) mod3 → (-1 mod3)=2 →steps_entrance=min(2,1)=1.

time_entrance=15.

options:

option1:0+0+15=15.

others: 15+10=25, etc. So minimal is 15. Correct.

So the code works for the samples.

Another test case: same entrance.

n=3, m=5, k=2.

a= (entrance 1, floor 3, apartment 1. So a= (entrance-1)*m*k + (floor-1)*k +1 → (0)*5*2 + (2)*2 +1= 0 +4 +1=5.

b= same entrance, floor 5. So b= (0)*10 + (4)*2 +1= 8+1=9.

So a=5, b=9.

p1=1, f1=3.

p2=1, f2=5.

steps_entrance=0.

time_entrance=0.

four options:

option1: (3-1)*5 + (5-1)*5 →10 +20 =30.

option2:10 + (10 +4) →10+14=24.

option3: (10+2) +20 →12+20=32.

option4:12+14=26.

So minimal is 24.

So code would return 24.

But what's the actual minimal time?

Edward is on floor 3 of entrance 1. To exit, he must get to first floor. Then, move to entrance 1 (steps_entrance 0), then get to floor 5.

Option2: stairs down (2 floors →10 sec), then elevator up (10 +4 →14). Total 24.

Yes.

So code works.

Now, code is correct.
</think>

```python
n, m, k = map(int, input().split())
a, b = map(int, input().split())

def get_p_f(x):
    per_entrance = m * k
    p = (x - 1) // per_entrance + 1
    rem = x - (p - 1) * per_entrance
    f = (rem - 1) // k + 1
    return p, f

p1, f1 = get_p_f(a)
p2, f2 = get_p_f(b)

d_clock = (p2 - p1) % n
steps_entrance = min(d_clock, n - d_clock)
time_entrance = steps_entrance * 15

option1 = (f1 - 1) * 5 + (f2 - 1) * 5 + time_entrance
option2 = (f1 - 1) * 5 + (10 + (f2 - 1) * 1) + time_entrance
option3 = (10 + (f1 - 1) * 1) + (f2 - 1) * 5 + time_entrance
option4 = (10 + (f1 - 1) * 1) + (10 + (f2 - 1) * 1) + time_entrance

print(min(option1, option2, option3, option4))
```
