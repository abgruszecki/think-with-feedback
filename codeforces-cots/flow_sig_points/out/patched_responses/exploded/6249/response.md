<think>
Okay, so I need to solve this programming problem where I have to determine the champions according to two different scoring systems based on the results of several races. Let's start by understanding the problem thoroughly.

The problem states that for each race, the top 10 drivers get points in a certain way. Then, the original system's champion is determined first by total points, then by number of first places, then seconds, etc. The alternative system first looks at the number of wins, then total points, then the same as original for remaining positions. And I have to output the champion for each system.

Hmm. Let's break it down. For each driver, I need to track two things: their points according to the original system and the alternative system. Wait, no. Wait, the alternative system's scoring isn't different in terms of points. Wait, no. Wait, the alternative system's champion isn't using a different point system. The alternative system's rules are about how to compare the drivers. Let me re-read the problem.

In the original system, the driver with the most points is the champion. Ties are broken by the number of wins (first places). If still tied, then the number of second places, etc.

In the alternative system, the champion is the one with the most wins. If tied, most points (using the original points). If still tied, compare the number of seconds, etc. So the points are the same, but the comparison criteria are different.

So, for each driver, I need to track:

- Total points in the original system.
- For each position (1st, 2nd, etc.), how many times they got that position across all races.

Because for tiebreakers, we need to compare in order of positions. For example, in the original system, if two drivers have the same points, we first check who has more first places. If they are equal, then check second places, and so on.

So, for each driver, I need to store:

- points (original system)
- a list that counts the number of times they got each position. For example, positions[0] is the count of 1st places, positions[1] is count of 2nd, etc. But since the races can have varying numbers of drivers (n can be up to 50), but positions are 1st, 2nd, etc. So for a race with n=3, only positions 1, 2, 3 are considered. So for a driver, their positions list can have up to the maximum number of positions possible across all races. But since the maximum n per race is 50, and there are up to 20 races, the maximum positions needed would be 50. So for each driver, we can track an array of size 50 (since in a race, the positions start at 1, which is index 0 in this array). So for each race, for each driver in the race, their position in that race (like 1st, 2nd, etc.) is their index+1 in the race's list. Then, for each such position, increment the count in the driver's positions array at index (position-1). For example, if a driver finishes 3rd in a race, their positions[2] is incremented by 1.

Wait, but the problem's tiebreaker compares the number of first places, then second, etc. So for a driver, their count of first places is the number of times they were first in any race. Similarly for second, etc. So for each race, the driver's position in that race (if they are in the top n of that race) determines their points and their counts for each position.

So for each driver, we need:

- total points (summing the points from each race according to original scoring)
- a list (or array) of counts for each position. For example, position_counts[i] is the number of times the driver got (i+1)th position. So for position 1, it's index 0, position 2 is index 1, up to position 50 (max possible in any race) at index 49.

Now, for the original system's comparison between two drivers A and B:

Compare their total points. If A's points are higher, A is better. If equal, compare the number of first places (position_counts[0]). If A has more, then A is better. If equal, compare second places (position_counts[1]), etc., until a difference is found.

For the alternative system's comparison:

First, compare the number of first places (position_counts[0]). If A has more, A is better. If equal, compare their total points. If still equal, compare the number of second places (position_counts[1]), then third, etc.

So, the key is to generate for each driver these two pieces of data (points and position counts), then sort the drivers according to the two different comparison rules, and pick the top one in each case.

Now, the steps to solve the problem:

1. Read the input and process each race.

2. For each race, iterate through the drivers in order (1st to nth place), and for each, update their points (according to the original system) and their position counts.

3. Once all races are processed, collect all drivers that have participated in at least one race.

4. For the original system, sort the drivers using the original comparison criteria.

5. For the alternative system, sort using the alternative criteria.

6. Output the first driver in each sorted list.

Now, the challenge is to represent the drivers efficiently and implement the comparison correctly.

Let's think about the data structures. For each driver, we can store a dictionary with their name as the key, and the value being a tuple of (points, position_counts), where position_counts is a list of integers of length 50 (since the maximum possible position is 50, as per the input constraints). Or, perhaps better, since the maximum possible position in any race is 50, but each race can have up to 50 drivers, the position in that race can be up to 50th. So for a driver, the position_counts list will track how many times they came 1st, 2nd, ..., 50th in any race. So for each race, for each driver in the race, we increment their count in the position index (their 1-based position minus 1).

So for example, in a race with 3 drivers:

1st driver: position 1 → index 0 → increment position_counts[0] by 1.

2nd driver: position 2 → index 1 → increment position_counts[1] by 1.

3rd driver: position 3 → index 2 → increment position_counts[2] by 1.

But for races with more than 10 drivers, the points are only given to the top 10. So for a race with n=15, the 11th driver gets 0 points. So, when processing a race, for each driver in the race, their points are added based on their position. The original points are given as follows:

Positions 1-10 get points according to the list [25,18,15,12,10,8,6,4,2,1]. Position 11 and above get 0.

So for each driver in a race, if their position (1-based) is <=10, add the corresponding points (the index in the points list is position-1). If position >10, add 0.

So, for each race, for each of the first 10 positions, we add points. Otherwise, no.

So the code for processing a race would be:

points_original = [25,18,15,12,10,8,6,4,2,1]

for each race in races:

    n = number of drivers in this race

    for i in 0 to n-1:

        driver = current driver's name

        if i < 10:

            driver's points += points_original[i]

        else:

            driver's points += 0

        position_in_race = i+1  # 1-based

        driver's position_counts[position_in_race -1] +=1

Wait, but position_in_race can be up to 50. So, for example, a driver comes in 20th in a race of 50 drivers. Then, their position is 20, so we increment position_counts[19] by 1.

So the code for processing each race is:

for race in races:

    read n

    for i in 0 to n-1:

        driver_name = input().strip()

        if driver not in the drivers dict:

            initialize with points 0, position_counts as [0] * 50

        driver = drivers[driver_name]

        # add points if in top 10

        if i <10:

            driver['points'] += points_original[i]

        # increment position count for this position (i+1)

        pos = i+1

        driver['position_counts'][pos-1] +=1  # since indexes are 0-based for position 1.

So the position_counts list is 0-based, index 0 is position 1, index 1 is position 2, up to index 49 for position 50.

Now, the next step is to compare the drivers according to the two different criteria.

For the original system, the key is to sort the drivers based on:

1. Descending points.

2. If points are equal, compare the number of first places (position_counts[0]) in descending order.

3. If still equal, compare position_counts[1] (number of second places), etc.

So the comparison function for the original system is: for two drivers A and B,

compare their points. If not equal, the one with higher points comes first.

If points are equal, compare their position_counts[0], then position_counts[1], etc., until a difference is found.

For the alternative system, the comparison is:

1. Descending number of first places (position_counts[0]).

2. If equal, compare total points in descending order.

3. If still equal, compare position_counts[1], then position_counts[2], etc.

So, how to implement these comparisons in Python?

In Python, when sorting, we can define a key function that returns a tuple. When tuples are compared, they are compared element-wise in order.

So for the original system, the key for each driver would be a tuple that starts with (-points), then followed by [-counts[0], -counts[1], ..., -counts[49]]. Wait, because when sorted in ascending order, the tuple with lower elements comes first. So using negative values allows us to sort in descending order. Wait, no. For example, if we have a list of numbers [5,3,7], and we want to sort them in descending order, we can use the key as -x. So sorted with key=lambda x: -x would order 7,5,3.

So, for the original system, the key for each driver would be:

(-points, -counts[0], -counts[1], ..., -counts[49])

Because when sorted in ascending order, the driver with the highest points comes first. If points are equal, the one with higher counts[0] comes first (since -counts[0] is smaller if counts[0] is larger), and so on.

Similarly, for the alternative system, the key would be:

(-counts[0], -points, -counts[1], ..., -counts[49])

Wait, for alternative system, the first priority is the number of first places (counts[0]), then points, then counts[1], etc.

So the key for alternative is:

(-counts[0], -points, -counts[1], -counts[2], ..., -counts[49])

But building such a tuple for each driver could be a bit tedious. However, since the maximum possible position is 50, the counts list has 50 elements. So for the original system's key, it's a tuple of (-points, -counts[0], -counts[1], ..., -counts[49]). For the alternative system's key, it's (-counts[0], -points, -counts[1], -counts[2], ..., -counts[49]).

But creating a tuple with 51 elements (original system) or 51 elements (alternative) for each driver is manageable.

So for each driver, when creating the key for the original system, the tuple starts with -points, then the list of -counts[0], -counts[1], ..., -counts[49]. For the alternative system, it's -counts[0], -points, followed by the same list as before.

In Python, you can create such a tuple by combining the required elements. For example, for the original key:

original_key = (-driver.points, ) + tuple(-count for count in driver.position_counts)

But wait, driver.position_counts is a list of 50 elements (positions 1-50). So for the original system, the key is (-points, -counts[0], -counts[1], ..., -counts[49]).

For the alternative system, the key is (-counts[0], -points, -counts[1], ..., -counts[49]).

So for each driver, the alternative key is:

alternative_key = (-driver.position_counts[0], -driver.points) + tuple(-count for count in driver.position_counts[1:])

Wait, no. Because after the first two elements, we need to compare the counts for position 2, 3, etc. So the alternative key is:

(-counts[0], -points, -counts[1], -counts[2], ..., -counts[49])

Which is equivalent to:

(-counts[0], -points) followed by the list of -counts[1], -counts[2], ..., -counts[49].

So for a driver, the alternative key is:

[ -counts[0], -points ] + [ -count for count in counts[1:50] ]

In code, for a driver's counts list (which is of length 50), the alternative key can be constructed as:

key = (-counts[0], -points, *(-counts[1:]))

Wait, in Python, you can't use * in a tuple like that. Wait, the counts is a list, say counts = [a, b, c, ..., z] (50 elements). Then, for the alternative key:

key = (-counts[0], -points) + tuple(-count for count in counts[1:])

Because counts[1:] is 49 elements. So the alternative key would be a tuple of 1 + 1 +49 = 51 elements.

So in code:

original_key = (-points,) + tuple(-count for count in position_counts)
alternative_key = (-position_counts[0], -points) + tuple(-count for count in position_counts[1:])

Once these keys are generated, the drivers can be sorted by these keys, and the first driver in the sorted list is the champion.

So, for each system, we generate a list of drivers, sort them using the respective key, and pick the first.

Now, the next challenge is to manage the drivers and their data.

In Python, we can use a dictionary to map driver names to their points and position_counts. For example:

drivers = {}

For each race:

read n.

for i in 0 to n-1:

    name = input().strip()

    if name not in drivers:

        # Initialize with points 0 and position_counts [0] *50

        drivers[name] = {

            'points': 0,

            'position_counts': [0] * 50

        }

    driver = drivers[name]

    # add points if in top 10 (i <10)

    if i <10:

        driver['points'] += points_original[i]

    # update position counts

    position = i +1  # 1-based position in the race

    driver['position_counts'][position-1] +=1

Once all races are processed, collect all the driver names into a list, and then sort them based on the two keys.

Now, for the original champion:

sorted_drivers_original = sorted(drivers.keys(), key=lambda name: (

    -drivers[name]['points'], 

    *tuple(-drivers[name]['position_counts'][i] for i in range(50))

))

Wait, but in Python, when you create a tuple inside a lambda, you need to properly generate the elements. So perhaps:

key=lambda name: (

    (-drivers[name]['points'],) + 

    tuple(-drivers[name]['position_counts'][i] for i in range(50))

)

Similarly for the alternative key:

key=lambda name: (

    (-drivers[name]['position_counts'][0], 

    -drivers[name]['points']) + 

    tuple(-drivers[name]['position_counts'][i] for i in range(1,50))

)

But this would create a tuple with first element -counts[0], second -points, then the rest.

Wait, for example, in code:

original_key = (-points, -count0, -count1, ..., -count49)

alternative_key = (-count0, -points, -count1, ..., -count49)

So for the original system, the key is:

key = (-points, ) + tuple( -counts[i] for i in range(50) )

For the alternative, it's:

key = (-counts[0], -points) + tuple( -counts[i] for i in range(1,50) )

Yes.

So in Python, the lambda for the original key is:

lambda x: (-drivers[x]['points'],) + tuple( -v for v in drivers[x]['position_counts'] )

Because drivers[x]['position_counts'] is a list of 50 elements. So for each element in that list, we take -v. Then, the tuple is (-points, -count0, -count1, ..., -count49).

Similarly, the alternative key is:

lambda x: (-drivers[x]['position_counts'][0], -drivers[x]['points']) + tuple( -v for v in drivers[x]['position_counts'][1:] )

Because for the counts after the first (position 0), we take the rest (from index 1 to 49, which are 49 elements). So the tuple is (-count0, -points, -count1, ..., -count49).

So using this key, sorting the list of driver names in ascending order will result in the driver with the highest original key being first, because tuples are compared element-wise.

Once sorted, the first element in the list is the champion for that system.

Now, considering the constraints. The number of drivers is up to 50. So sorting is O(m log m), which for m=50 is negligible. So even with multiple sorts (two sorts), it's acceptable.

Now, the code outline is:

Read t races.

Process each race, updating the drivers' points and position counts.

Collect all driver names into a list.

Sort the list according to the original key and alternative key.

Print the first element of each sorted list.

Now, let's test with the first example.

First example input:

3

3

Hamilton

Vettel

Webber

2

Webber

Vettel

2

Hamilton

Vettel

Processing the races.

First race:

n=3. The top 3 drivers. Points for first 3 positions: 25,18,15 (since i=0,1,2 <10).

Hamilton gets 25 points. Position 1: position_counts[0] +=1.

Vettel gets 18. Position 2: counts[1] +=1.

Webber gets 15. Position 3: counts[2] +=1.

Second race: n=2. Top 2 get 25, 18.

Webber is first: 25 points. Position 1 → counts[0] +=1.

Vettel is second: 18 points. Position 2 → counts[1] +=1.

Third race: n=2. Hamilton first (25), Vettel second (18).

Hamilton's points: 25 (from first race) + 25 (third race) → 50.

Vettel's points: 18 (first race) + 18 (second) +18 (third) → 54.

Webber's points: 15 (first) +25 (second) →40.

Now position counts:

Hamilton:

position counts for 1st place: 2 (first race and third race → counts[0] is 2).

Vettel:

positions: in first race, 2nd (counts[1] +=1). Second race: 2nd (counts[1] +=1). Third race: 2nd (counts[1] +=1. So counts[1] is 3. So in the original system, Vettel's points are 18+18+18=54. Hamilton has 50.

So original champion is Vettel.

Alternative system: compare number of wins (counts[0]).

Hamilton's counts[0] is 2 (he was first in first and third races).

Vettel's counts[0] is 0 (he was never first in any race). Webber's counts[0] is 1 (second race).

So in the alternative system, Hamilton has the most wins (2), so he is the champion.

Hence the output is Vettel and Hamilton.

So the code should process this correctly.

Now, let's think about data structures.

Each driver's data is stored in a dictionary. For each driver, position_counts is a list of 50 zeros, which is manageable.

In Python, using a dictionary of dictionaries is efficient enough for the constraints (t up to 20, n up to 50 per race, and up to 50 drivers total).

Now, the code steps:

Read t.

Initialize drivers as empty dict.

For each of t races:

   read n.

   read n lines, each a driver name.

   for each index i (0-based) in 0..n-1:

       driver_name = current line.

       if not in drivers, add to drivers with points 0 and position_counts [0]*50.

       driver = drivers[driver_name]

       if i <10:

           points = [25,18,15,12,10,8,6,4,2,1][i]

           driver['points'] += points

       position_in_race = i+1

       driver['position_counts'][position_in_race-1] +=1

Once all races processed.

Collect all driver names into a list, say, all_drivers = list(drivers.keys())

Sort all_drivers for original system:

original_sorted = sorted(all_drivers, key=lambda name: (-drivers[name]['points'],) + tuple(-count for count in drivers[name]['position_counts']))

Wait, but in Python, the + operator for tuples will concatenate. So (-points, ) + (tuple of -counts) gives the desired key.

Yes.

Similarly for alternative_sorted:

alternative_sorted = sorted(all_drivers, key=lambda name: (-drivers[name]['position_counts'][0], -drivers[name]['points']) + tuple(-count for count in drivers[name]['position_counts'][1:]))

Wait, but drivers[name]['position_counts'][1:] is a list of 49 elements. So tuple(-count for count in drivers[name]['position_counts'][1:]) is a tuple of 49 elements.

So the key for alternative is a tuple of 1 (count0) + 1 (points) +49 (counts 2-50) → total 51 elements.

Yes.

Once sorted, the first element of each list is the champion.

So print the first element of original_sorted and the first of alternative_sorted.

Now, possible edge cases: when the counts extend beyond 10, but the code should handle all positions up to 50.

Another example: if a driver has 1 win, but in a race with n=1, he gets 25 points. Another driver with 0 wins but more points (e.g., two 2nd places in races with n>10, but in the original system, points from those positions would be 18 each → total 36, which is higher than 25).

But according to the alternative system, the first driver has more wins (1 vs 0), so even though points are lower, he is the champion.

So the code handles that.

Now, code implementation.

But in Python, when creating the tuple for the key, how to generate the counts correctly.

Let's code this step by step.

First, process the races:

points_original = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

So for i in 0..9, the points are points_original[i], else 0.

So code:

t = int(input())
drivers = {}

for _ in range(t):
    n = int(input())
    for i in range(n):
        name = input().strip()
        if name not in drivers:
            drivers[name] = {
                'points': 0,
                'position_counts': [0] * 50
            }
        driver = drivers[name]
        if i < 10:
            driver['points'] += points_original[i] if i < len(points_original) else 0  # but the list has 10 elements, 0-9.
        # update position counts
        pos = i +1  # 1-based position
        driver['position_counts'][pos-1] +=1  # index is pos-1.

Then, collect the driver names and sort.

all_drivers = list(drivers.keys())

original_sorted = sorted(all_drivers, key=lambda name: (
    -drivers[name]['points'],
    *tuple(-count for count in drivers[name]['position_counts'])
))

Wait, no. In Python, the * operator can't be used in a tuple like that. Wait, inside a tuple, the * operator unpacks an iterable into elements. So (-drivers[name]['points'],) + tuple(-count for count in drivers[name]['position_counts']) would be correct.

So the key for original is:

key=lambda name: (-drivers[name]['points'],) + tuple(-count for count in drivers[name]['position_counts'])

Similarly, for the alternative:

key=lambda name: (-drivers[name]['position_counts'][0], -drivers[name]['points']) + tuple(-count for count in drivers[name]['position_counts'][1:])

Yes.

So code for sorting:

original_sorted = sorted(all_drivers, key=lambda name: (-drivers[name]['points'],) + tuple( -count for count in drivers[name]['position_counts'] ))

alternative_sorted = sorted(all_drivers, key=lambda name: (-drivers[name]['position_counts'][0], -drivers[name]['points']) + tuple( -count for count in drivers[name]['position_counts'][1:] ))

Once sorted, the first element is the champion.

So:

print(original_sorted[0])
print(alternative_sorted[0])

This should work.

Testing the first example:

After processing the races, the drivers are Hamilton, Vettel, Webber.

Original_sorted will be sorted based on their points, then position counts.

Vettel's points are 54 (18+18+18). So he is first.

Alternative_sorted is sorted by number of wins (counts[0]). Hamilton has counts[0] =2 (from first and third race). Vettel has 0. So Hamilton is first.

Hence output is Vettel and Hamilton.

Now, code.

But wait, for the alternative key, the code must have the order of comparison as:

number of wins (counts[0]) → points → counts[1], counts[2], etc.

Which is correctly captured by the key (-counts[0], -points, -counts[1], ...).

Yes.

So the code should work.

Now, possible issues:

- Drivers not present in all races. But the code correctly accumulates data from all races.

- Case sensitivity: the problem says that names are case-sensitive, so 'Hamilton' and 'hamilton' are different. The code uses the name as given, which is correct.

- The code uses a list of 50 elements for position counts, even if the maximum position in a race is 50. So for a race with n=50, the 50th driver is position 50, which is index 49 in the list. Correct.

Now, code.

The code reads the input correctly, processes each race, and the sorting is done as required.

Thus, the code should work.
</think>

```python
t = int(input())
drivers = {}

points_original = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

for _ in range(t):
    n = int(input())
    for i in range(n):
        name = input().strip()
        if name not in drivers:
            drivers[name] = {
                'points': 0,
                'position_counts': [0] * 50
            }
        driver = drivers[name]
        if i < 10:
            driver['points'] += points_original[i] if i < len(points_original) else 0
        pos = i + 1
        driver['position_counts'][pos - 1] += 1

all_drivers = list(drivers.keys())

# Determine original champion
original_sorted = sorted(all_drivers, key=lambda name: (
    -drivers[name]['points'], 
    *tuple(-count for count in drivers[name]['position_counts'])
))

# Determine alternative champion
alternative_sorted = sorted(all_drivers, key=lambda name: (
    -drivers[name]['position_counts'][0],
    -drivers[name]['points'],
    *tuple(-count for count in drivers[name]['position_counts'][1:])
))

print(original_sorted[0])
print(alternative_sorted[0])
```