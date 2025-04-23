<think>
Okay, let's see. I need to find the minimal time for all students to reach the top. The problem is about scheduling the groups into the cablecars, considering their color preferences and the order of the cars. Hmm.

So the cablecars come in a cycle: red, green, blue, red, green, blue, etc. Each color's car arrives every 3 minutes. For example, red at 0, 3, 6... green at 1,4,7..., blue at 2,5,8..., and so on. Each car can take up to two people. Each car takes 30 minutes to reach the top, so the arrival time at the top is the time the car was taken (departure time) plus 30. The total time needed is the maximum of all arrival times of the students.

The goal is to assign the students (r, g, b) to their respective cars in such a way that the latest arrival time is minimized.

Let me think about how to model this. For each color group, we need to calculate the times when their cars are used. Then, for each car, track how many students are in it (up to 2), and compute the arrival time. The latest of all those times is the answer.

So, for each color, the cars come every 3 minutes starting at their initial time (0 for red, 1 for green, 2 for blue). For example, red's cars are at t=0,3,6,... Each car can carry up to two students. The students in each color group must be assigned to their color's cars. The number of cars needed for a group is ceil(number_of_students / 2). For example, if a group has 3 students, they need 2 cars (ceil(3/2) = 2).

But the order in which the groups use their cars might affect the maximum arrival time. For example, if red uses cars at 0,3,6 and green uses 1,4,7, etc. But each group's cars are used in their own sequence. However, the problem is that each group's car usage is independent, but their departure times are in their own sequence. The latest departure time plus 30 is what matters. So the maximum arrival time is the maximum (car_depart_time +30) across all cars used.

Wait, but the departure time is when the car arrives at the bottom. The arrival at the top is 30 minutes later. So the arrival time is departure_time +30.

So for each color group, we need to calculate all the departure times of the cars used for that group, then add 30 to each, and find the maximum among all those.

The challenge is to find the arrangement of the cars used for each color that results in the latest arrival time being as small as possible.

Wait, but for a color group, the departure times are fixed. For example, red's first car is at 0, then 3, 6, etc. So the number of cars needed for red is ceil(r/2). Each of those cars departs at 0,3,6,...,3*(k-1) where k is the number of cars. The last car's departure time is 3*(ceil(r/2)-1). Then arrival time is that plus 30. Similarly for green and blue.

Wait, no. Because the cars for each color come every 3 minutes. For example, red's cars are at 0,3,6,9, etc. So the nth red car departs at time 3*(n-1). So if red needs 2 cars, their departure times are 0 and 3. The arrival times are 30 and 33. So the maximum arrival time for red would be 3* (ceil(r/2) -1) +30.

Similarly for green: the cars are at 1,4,7,... So departure times are 1 +3*(k-1) for the kth car.

Blue's cars are at 2,5,8,...

So for each color, the departure times of their cars are: color's first departure time (0,1,2 for red, green, blue) plus 3*(i-1) for i-th car.

Then the arrival time for each car is departure_time +30.

So for each color group, the last arrival time is (first_departure_time + 3*(n-1)) +30, where n is the number of cars needed (ceil(st/2)).

The total maximum arrival time is the maximum among all three groups' last arrival times.

But wait, maybe there's an overlap where even though one group's last arrival time is earlier, another group's last arrival time is later, but there's some cars in between that have higher times. However, since each group's cars are assigned in their own sequence, the last arrival time for each group is their last car's arrival time. So the maximum of these three values is the answer.

So the problem reduces to:

For each color, compute the number of cars needed (ceil(st/2)), then compute the last departure time (3*(n-1) + color_offset), add 30, and take the maximum among the three.

So for example:

Take the first sample input:

r=1, g=3, b=2.

Red: ceil(1/2)=1 car. Departure at 0. Arrival 30.

Green: ceil(3/2)=2 cars. Departure times 1 and 4. Arrival times 31, 34.

Blue: ceil(2/2)=1 car. Departure at 2. Arrival 32.

The max is 34, which matches the sample.

Another sample:

Input is 3 2 1.

Red: ceil(3/2)=2 cars. Departures 0 and 3. Arrival 30 and 33.

Green: ceil(2/2)=1. Departure 1. Arrival 31.

Blue: ceil(1/2)=1. Departure 2. Arrival 32.

Max is 33.

Which matches the sample.

So the approach is:

1. For each color (r, g, b), calculate the number of cars needed (ceil(st/2)).

2. For each color, compute the last departure time: (cars_needed -1)*3 + color_offset.

   The color_offset is 0 for red, 1 for green, 2 for blue.

3. The arrival time is last_departure_time +30.

4. The answer is the maximum of the three arrival times.

But wait, this seems too straightforward. But according to the sample inputs, this approach works.

Let me test another case. Let's say r=0, g=0, b=4.

So b needs 2 cars (ceil(4/2) = 2). Departure times are 2 and 5. Arrival times 32 and 35. So answer is 35.

Yes. Another example: all colors have 0 except one. So for example, r=5. Then ceil(5/2)=3. Departure times 0,3,6. Last arrival is 6+30=36.

So the approach is to compute for each color, the last arrival time, and take the maximum.

But why does this work? Because each color's cars are scheduled in their own sequence, and their departure times are fixed. The order of the cars is fixed (red, green, blue every three minutes). So for each group, the cars they use are their own, so the last car's arrival time is the latest one for that group.

Thus, the answer is the maximum among the three groups' last arrival times.

So the steps are:

- Compute for each group the number of cars (ceil(r/2), ceil(g/2), ceil(b/2)).

- For each group, compute last departure time: (cars_needed-1)*3 + color_offset.

- Add 30 to get the arrival time.

- Take the maximum of these three.

So the code can be structured as follows:

Read r, g, b.

Compute for each color:

red_cars = (r +1) // 2

green_cars = (g +1) //2

blue_cars = (b +1) //2

Then:

red_last = (red_cars -1)*3 *1 + 0 +30 if red_cars>0 else 0.

Wait, no. For red_cars, each car departs at 0,3,6, etc. So for red_cars n, the last departure is 3*(n-1). So arrival is 3*(n-1)+30.

Same for green: (n-1)*3 +1 +30.

Blue: (n-1)*3 +2 +30.

But if a group has 0 students, then the number of cars is 0. So we can ignore that group.

So the code would calculate for each color:

if the number of students >0:

   cars = (students +1) //2

   last_departure = (cars-1)*3 + color_offset

   arrival = last_departure +30

else:

   arrival is 0 (since no students, but we take maximum, so 0 can be ignored if other groups have values)

But if all groups have 0 except one, then the maximum will be the correct value.

So code:

r, g, b = map(int, input().split())

def compute_time(st, offset):

    if st ==0:

        return 0

    cars = (st +1) //2

    last_depart = (cars -1)*3 + offset

    return last_depart +30

red_time = compute_time(r, 0)

green_time = compute_time(g, 1)

blue_time = compute_time(b, 2)

result = max(red_time, green_time, blue_time)

print(result)

Wait, let's test this with the first sample.

Sample1: r=1, g=3, b=2.

red_time: (1+1)//2=1. (1-1)*3 +0 =0. 0+30=30.

green_time: (3+1)/2=2. (2-1)*3 +1=3+1=4. 4+30=34.

blue_time: (2+1)/2=1.5 → 1.5 rounded down? Wait, (2+1)//2 in Python is (2+1)//2 = 3//2 =1. So 1 car. (1-1)*3 +2=0+2=2. 2+30=32.

Max is 34. Correct.

Sample2: r=3, g=2, b=1.

red_cars: (3+1)/2=2. (2-1)*3+0=3. 3+30=33.

green: (2+1)/2=1.5 → 1. (1-1)*3 +1=0+1=1. 1+30=31.

blue: (1+1)/2=1. (1-1)*3 +2=0+2=2. 2+30=32.

Max is 33. Correct.

Another test case: all zero except one, like r=5.

cars = (5+1)//2=3. (3-1)*3=6. 6+30=36.

Yes.

Another case where two groups have overlapping times. For example, r=4 (ceil(4/2)=2 cars: 0,3 → arrival 30 and 33), g=4 (cars=2: 1 and 4 → arrival 31 and 34), b=4 (cars=2: 2 and 5 → arrival 32 and 35). So max is 35.

Yes.

So this code should work.

Wait, but what if all three groups have cars that are scheduled in a way that the latest departure is not the last of their own sequence?

Like, suppose two groups have their cars overlapping. But according to the problem statement, each group's cars are in their own sequence. So the last car for each group is indeed their own last departure time. Therefore, the maximum arrival time is the maximum of the last arrivals of each group.

Therefore, the code as written is correct.

But wait, let's think of a case where one group's last arrival is 33, another's is 34, and the third's is 35. The code will return 35. Which is correct.

So the code works.

Now, what about when a group has zero students? For example, r=0. Then compute_time returns 0, which when compared to others will be ignored. But if all groups are zero except one, then the code returns the correct time.

So this approach seems correct.

Thus, the code should be as written above.
</think>

```python
r, g, b = map(int, input().split())

def calculate_max_time(count, offset):
    if count == 0:
        return 0
    cars = (count + 1) // 2
    return (cars - 1) * 3 + offset + 30

red_time = calculate_max_time(r, 0)
green_time = calculate_max_time(g, 1)
blue_time = calculate_max_time(b, 2)

print(max(red_time, green_time, blue_time))
```