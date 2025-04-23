<think>
Okay, I need to solve this problem. Let's try to understand it step by step.

So, there are n students arriving at a bus stop. Each student has a time ti when they arrive and a destination xi. The bus works in a certain way. The bus starts at 0 and can carry m passengers. When m students get on, or when the last student arrives, the bus departs. The bus drives to the farthest point, stopping at each required xi along the way. Then, after dropping everyone off, it returns to 0. Each drop-off takes 1 + floor(k/2) time, where k is the number of students getting off there. But the time when the student is considered to have gotten off is when the bus stops at their xi, not including the unloading time. Wait, the problem statement says: the moment a student got off is the moment the bus stopped at the stop, despite the unloading time. So the unloading time is added after that moment. So for example, if the bus arrives at a stop at time T, then the unloading takes S time, so the bus departs after T + S. But the student's time is T.

The bus then returns to the stop, and picks up the next batch of students. Students wait in a queue if the bus isn't there. The students board in the order they arrived.

The goal is to compute for each student the time they left the bus.

Hmm. So the challenge is to model the bus trips efficiently, considering each batch of up to m students, handling their destinations, and keeping track of the time.

First, let's think about how to model each trip.

Each batch of students is a group of up to m students. So, the students are grouped into batches of m, except the last group which could be smaller. But the order is determined by their arrival times, which are given in increasing order. Since the students are given in the order of strictly increasing ti, we can process them in groups of m. Each group is processed as a batch.

So the first thing is to split the students into batches. Each batch is a list of consecutive students, with each batch size up to m, except possibly the last.

For each batch:

- The bus departs when the batch is filled (m students) or when it's the last student.

But wait, the bus departs when m students are on board, or when the last student (n-th) gets on. So the batches are formed by taking the first m students, then next m, etc. But each batch's departure time is determined by the maximum between the arrival time of the last student in the batch and the time when the bus returns from the previous trip.

Wait, no. Let's clarify:

The students form a queue. When the bus is available (i.e., back at 0), students start boarding. They get on in the order they arrived. The bus leaves when either m students are on board, or there are no more students left. So the batches are formed as groups of m consecutive students, but each batch can only depart when the bus is back.

So the batches are processed in order. For each batch, the departure time is the maximum between the time when the last student in the batch arrives and the time when the bus becomes available (i.e., returns from the previous trip).

So for example, if the bus returns to 0 at time T_prev_return, and the first student in the batch arrives at ti which is after T_prev_return, then the bus departs at the time of that last student in the batch. But if the bus returns earlier than the ti of the first student in the batch, then the batch's departure time is the ti of the last student in the batch.

Wait, no. Because when the bus is available (at time T_available), the students who have arrived by then and are waiting in the queue will board the bus. The bus leaves when the m-th student boards, or when there are no more students left.

So for a batch, the students in the batch are the first m students in the queue when the bus is available. So the batch's departure time is the maximum between T_available and the arrival time of the last student in the batch. Because each student in the batch arrives in order. Since the students are given in order of increasing ti, the last student in the batch has the latest ti in that group.

So for the batch, the departure time is max(T_available, ti_of_last_student_in_batch).

Then, the bus departs, and during this trip, we need to process the stops.

So the steps for each batch are:

1. Determine the departure time of the batch: T_depart = max(T_available, last_student_ti).

2. The bus drives to the farthest xi in the batch. Because the bus goes in the positive direction, and stops at each xi where students get off. But the order in which they stop depends on their positions. Wait, the problem says: every time the bus passes a point where at least one student needs to get off, it stops. But the bus is moving in the positive direction, so the stops are in increasing order of xi. Wait, no. The bus is going to the maximum xi in the batch, then returns. So on the way to the maximum, it stops at all xi in the current batch in increasing order.

Wait, the problem says: the bus starts moving when m students are on board. Then, every time it passes a point where students need to get off, it stops. The students get off, which takes some time. Then the bus continues. Once all students are off, the bus turns around and returns to 0, without making any stops until it reaches 0.

So during the trip towards the maximum xi, the bus passes through all xi in the current batch, but the stops are made in order of increasing xi. So for example, if the batch has students with xi 5, 3, 5, then the maximum xi is 5. On the way to 5, the bus passes 3, then 5. So when passing 3, the students with xi=3 get off. Then when passing 5, the rest get off. Then the bus returns to 0.

So for a batch, we need to group the students by their xi, sorted in increasing order. For each xi in this sorted list, we calculate the time when the bus arrives there, and then process the unloading time.

But the arrival time at each xi is:

- The departure time T_depart plus the distance from 0 to xi (since the speed is 1). Wait, no: the first stop is the first xi in the sorted order. So the time taken to reach the first xi is (xi_1 - 0) = xi_1. Then the time to reach the next xi is (xi_2 - xi_1), and so on.

But the problem says that the bus stops each time it passes a point where students need to get off. So during the trip towards the maximum xi, the bus stops at all the xi's in the order they are encountered. So, the bus's path is 0 → x_max. Along this path, any xi where students are present (in the batch) are sorted in increasing order, and each is a stop. So the arrival time at each xi is T_depart plus the xi's distance from 0 (since the bus moves at speed 1).

Wait, no. Because the bus moves continuously. For example, if the first xi is 3, then the time to reach there is 3 units. Then from 3 to 5 is 2 units. So the arrival time at 5 is T_depart + 3 + 2 = T_depart +5. But that's the same as T_depart +5 (since 5 is the distance from 0 to 5). So regardless of the order, the arrival time for a student with xi is T_depart + xi. Because the bus is moving towards x_max, and passes each xi in order. So the arrival time for each xi is simply T_depart + xi.

But wait, that's only if xi is <= x_max. Because the bus is going to x_max. So all xi's in the batch are <= x_max. So the arrival time at xi is T_depart + xi. Because the bus is moving from 0 to x_max, and passes each xi in order.

Yes. So, all students in the batch have xi's that are <= x_max. So each student's arrival time at their xi is T_depart + xi.

Wait, no. For example, if the batch has students with xi 3, 5, then x_max is 5. The time to reach 3 is 3, and to reach 5 is 5. So the arrival time at 3 is T_depart +3, and at 5 is T_depart +5. So each student's arrival time is T_depart + their xi.

So for each student in the batch, their exit time is T_depart + xi. But wait, that's only for the current trip. So yes. Then, during that trip, the bus stops at each xi (sorted in increasing order), and each student's exit time is when the bus arrives there.

Then, after dropping all students, the bus needs to return to 0. The time taken to return is x_max (since distance x_max, speed 1). But the unloading time for each xi must be considered. Because after arriving at each xi, the bus spends 1 + floor(k/2) time unloading. But this unloading time adds to the total time.

So the total time for the trip is:

- The time to reach the farthest xi: T_depart + x_max.

- The sum of unloading times at each xi.

- The return time (x_max units, since the bus returns to 0 without stopping, so time is x_max).

But the unloading occurs after the arrival at each xi. So the order of processing is:

For each xi in sorted order:

1. Arrive at xi at time T_arrival = previous_time + (xi - previous_xi) ?

Wait, maybe I need to model this step by step.

Let me think again. The departure time of the batch is T_depart.

Then the bus starts moving towards x_max. It takes x_max units of time to reach x_max. But during this trip, it stops at each xi (sorted in increasing order) where there are students to drop off. At each stop, the unloading time is added.

So for example:

Batch has xi's sorted as [3,5], and x_max is 5.

The process is:

- Bus leaves at T_depart.

- Time to reach 3: T_depart +3.

- At 3, students get off. Their exit time is T_depart +3. Then, unloading takes S1 time (1 + floor(k/2), where k is the number of students here).

- Then, the bus continues to 5. Time taken is 5-3=2 units. So arrival at 5 is T_depart +3 + S1 + 2.

Wait, no. Because the unloading time is added after arriving. So the time to reach the next xi is the distance between xi and the previous xi, but the unloading time must be considered.

So the initial departure time is T_depart.

For each sorted xi in the batch's sorted list:

current_position = 0

current_time = T_depart

prev_position = 0

sorted_x = sorted list of unique xi's with their counts.

Wait, no. Wait, the students in the batch have various xi's. So we need to group them by xi, sorted in increasing order. For each xi in this sorted list:

- The time to reach xi from current_position is (xi - current_position). So current_time increases by that amount.

- Then, the arrival time is current_time. Each student with this xi has their exit time as current_time.

- Then, the unloading time for this xi is 1 + (number_of_students_here // 2). So current_time += unloading_time.

- Update current_position to xi.

After processing all xi's, the current_position is x_max. Then, the bus turns around and returns to 0. The time to return is x_max units (since moving from x_max to 0). But during the return trip, the bus doesn't stop. So the return time is x_max units added to current_time (after unloading the last xi).

So the total time for the entire trip (departure, unloading, return) is:

current_time (after all unloading) + x_max (return time) = T_return.

So the bus is available again at T_return.

Thus, for each batch, the steps are:

1. Collect all students in the batch (group of m students, or remaining students).

2. Determine the maximum xi in the batch (x_max).

3. Sort the students' xi's in increasing order, and group by xi.

4. For each xi in this sorted list:

   a. The time to reach xi is (xi - previous position) added to current_time.

   b. Record the arrival time as current_time for all students at this xi.

   c. Compute unloading time: 1 + (k // 2), where k is the number of students here.

   d. Add unloading_time to current_time.

5. After processing all xi's, add x_max to current_time (return time).

So the next batch's departure time is max(T_available, last_student_ti), where T_available is the return time of the previous batch.

Wait, but the batch is formed by the next m students. How do we group the students into batches?

The students are processed in the order they arrived, and each batch is formed by the first m students available when the bus returns. So if the bus returns at time T_available, the next batch is the next m students in the list, regardless of their arrival times. Because those students arrived before or after T_available, but when the bus is available, they form a queue and board in order. So even if a student arrives after T_available, they are part of the next batch once the previous batch is processed.

Wait, no. Wait, the problem statement says:

"students come to the stop and get on the bus. The bus has seating capacity m. At the moment when m students get on the bus, it starts moving. Also when the last (n-th) student gets on the bus."

So when the bus is not there (i.e., it's on a trip), arriving students form a queue. When the bus returns, it starts taking students from the queue in the order they arrived, up to m of them, and then departs. So the batches are formed by taking the first m students in the queue when the bus returns. However, the queue includes all students who arrived after the previous batches were dispatched and before the current bus returns.

So the batches are determined by the order of the students as they arrive, and the bus's availability. So the first batch is the first m students. Then, after the bus returns, the next batch is the next m students, etc. But the departure time of the next batch depends on the bus's return time and the arrival time of the last student in the batch.

Wait, no. Because the students are queued in the order of arrival. The bus takes the first m students in the queue when it returns. So for example, if the bus returns at time T, and there are k students in the queue (arrived before or at T), then the bus takes the first m (if k >= m) or all of them (if k < m) and departs. The departure time is max(T, the arrival time of the last student in the batch). But since the students are given in order of increasing ti, the last student in the batch has the maximum ti in that batch.

So the batches are consecutive groups of m students, but their departure time is determined by the max between the bus's available time and the last student's arrival time.

Wait, but the students could arrive after the bus is available. For example, the bus returns at time 10. The next student arrives at 15. So the bus can't depart until the student arrives. So the departure time for that batch is 15.

So for each batch, the departure time is the maximum between the bus's available time (T_available) and the arrival time of the last student in the batch.

But how do we group the students into batches? Since the students are given in order of increasing ti, the batches are formed as groups of m students. For example, students 0 to m-1 form the first batch, then m to 2m-1, etc. Because when the bus returns, the first m students in the queue (which are the next m in the list) are taken.

Yes. Because the students arrive in order, and the queue is in order of arrival. So the first batch is the first m students, the next is the next m, etc. The departure time of each batch is determined by the last student in that batch's ti and the bus's available time.

So the process is:

- The bus starts with T_available = 0 (initial available time).

- For each batch in groups of m students:

   a. Take the next m students (from current index to current index + m).

   b. The last student in the batch has ti = batch_last_ti.

   c. The departure time T_depart = max(T_available, batch_last_ti).

   d. Process the batch's trip (calculate arrival times, unloading times, return time).

   e. Update T_available to the return time after processing this batch.

So the key is to process each batch in order, grouping the students into consecutive m-sized groups.

Now, for each batch, we need to collect all students in the group, find their xi's, sort them, group by xi, then compute the time for each stop.

But how to efficiently compute the arrival times for all students in the batch.

Wait, the arrival time for a student in the batch is T_depart plus the distance to their xi. But during the trip, the bus stops at each xi in order, which takes time to unload. So the arrival time at a particular xi is not just T_depart + xi, because unloading previous stops takes time.

For example, suppose in a batch:

- Students have xi's 3 and 5.

- T_depart is 10.

Then, the bus leaves at 10. It takes 3 units of time to reach 3 (arrival at 13). Then, students get off. Unloading time is S1. Then, it takes 2 units to reach 5 (arrival at 13 + S1 + 2). Then, S2 unloading time. Then return takes 5 units (return time is 13 + S1 + 2 + S2 +5 = 20 + S1 + S2).

So the arrival time for the xi=3 students is 13, for xi=5 it's 13 + S1 + 2.

But S1 is the unloading time for the 3 stop, which is 1 + (k//2), where k is the number of students at 3.

So, for each batch, we need to process the sorted list of xi's, track the current time (starting at T_depart), and for each xi in order:

- current_time += (xi - previous_xi) → arrival_time = current_time

- record this arrival time for all students in this xi

- compute unloading time: 1 + (k //2)

- current_time += unloading_time

- previous_xi = xi

Then, after processing all xi's, add x_max (the maximum xi) to current_time for the return trip.

So the return time is current_time + x_max.

This return time becomes T_available for the next batch.

Thus, the steps for each batch are:

1. Group the m students (or remaining).

2. Extract their xi's.

3. Find x_max (the maximum xi in the batch).

4. Sort the xi's in ascending order, and group them (so all students at the same xi are processed together).

5. For each xi in the sorted order:

   a. Compute the distance from previous position (starts at 0 for the first xi).

   b. Add that distance to current_time (starting at T_depart).

   c. For all students at this xi, set their exit time to current_time.

   d. Compute the unloading time (1 + (k//2)), add to current_time.

6. After processing all xi's, add x_max to current_time (return time).

So, for the next batch, T_available is current_time (after step 6).

The challenge is to process all batches efficiently, given that n can be up to 1e5, and m up to 1e5. So the algorithm needs to be O(n), grouping the batches correctly.

So, to implement this:

We can process the students in batches of m. For each batch:

- Find the start and end indices (i to i+m-1 in the list of students).

- For each student in this batch, collect their xi.

- Find x_max.

- Create a list of (xi, count) sorted by xi. For example, for the batch, group all students by their xi, then sort the unique xi's in increasing order.

But grouping can be done by counting how many students are at each xi. For example, for the batch, we can create a dictionary mapping xi to the count of students. Then, sort the keys of the dictionary in increasing order.

But for a batch of m students, this could take O(m) time. Since m can be up to 1e5, and n is up to 1e5, the total time is O(n), which is acceptable.

Once the sorted xi list is generated, we can process each xi in order.

Now, the key is to, for each student in the batch, assign their exit time based on their xi's arrival time.

But how to efficiently track which students are at each xi.

Wait, but for the batch, all students in the batch are in the current group. So for each student in the batch, their xi is part of the group. So for the sorted list of xi's, each xi has a list of students (but we only need the count for the unloading time). But the students' exit times are the arrival time of their xi.

So for each xi in the sorted list, when we process it, all students in the batch at that xi get their exit time set to the current_time (arrival time). So for the students in the batch, we can collect them and then, during processing, assign their exit times.

Wait, but how do we track which students are in each xi?

Alternatively, for each batch:

- Collect all xi's of the students, and for each xi, note which students are there.

But this would require O(m) time per batch. For example, for a batch of m students:

Create a dictionary mapping xi to list of student indices.

Then, when processing each xi in sorted order, we can assign their exit times.

But with m up to 1e5 and n up to 1e5, this would be O(n) total time.

So the approach is:

- Split the students into batches of m. For each batch, the students are from start to start + m -1 (assuming 0-based).

- For each batch:

   a. The batch's students are the group.

   b. Find the x_max in the group.

   c. Sort the xi's in the group in increasing order, grouping students by xi.

   d. Process each xi in the sorted list, track arrival time, assign exit time to students at that xi.

So, the steps in code would be:

Initialize T_available = 0.

For each batch in 0 to (n//m) + 1:

   start = batch * m

   end = min(start + m, n)

   students_in_batch = students[start:end]

   batch_ti_last = students_in_batch[-1][0]

   T_depart = max(T_available, batch_ti_last)

   x_list = [xi for (ti, xi) in students_in_batch]

   x_max = max(x_list)

   # group by xi, sorted.

   xi_counts = {}

   for xi in x_list:

       xi_counts[xi] = xi_counts.get(xi, 0) + 1

   sorted_xis = sorted(xi_counts.keys())

   current_time = T_depart

   prev_pos = 0

   # process each xi in sorted_xis:

   for xi in sorted_xis:

       distance = xi - prev_pos

       current_time += distance

       # arrival_time is current_time

       # assign this time to all students in xi.

       count = xi_counts[xi]

       # find all students in the batch with xi == xi_val and set their exit time to current_time

       # but how to track which students are in this xi?

       # So for each student in the batch, check if their xi is xi_val.

       # But that's O(m) per batch. Which could be O(n) total, acceptable.

       # Alternatively, pre-process the students_in_batch into a list grouped by xi.

       # So for each student in the batch:

       # when xi == current xi in sorted_xis, set their exit time.

       # But this would require iterating over all students in the batch for each xi in sorted_xis, leading to O(m * k), where k is the number of unique xis. Which could be O(m^2) in worst case (all xis unique). That's bad.

       # So, we need a better way.

       # Alternative approach: create a dictionary mapping xi to list of student indices (within the batch) that have this xi.

       # So precompute for the batch:

       # xi_to_students = defaultdict(list)

       # for i, (ti, xi) in enumerate(students_in_batch):

       #     xi_to_students[xi].append(i)

       # Then, for each xi in sorted_xis:

       # for each student index in xi_to_students[xi], assign the current_time as their exit time.

       # This way, during processing, for each xi, we can quickly access the students in the batch that have that xi.

       # This is O(m) time for creating the mapping and O(k) steps for each batch.

       # So, this is acceptable.

       # So, during batch processing, precompute xi_to_students.

       # Let's adjust the code:

   # Preprocessing:

   xi_to_students = defaultdict(list)

   for idx_in_batch, (ti, xi) in enumerate(students_in_batch):

       xi_to_students[xi].append(idx_in_batch)

   # Then, sorted_xis is sorted(xi_to_students.keys())

   for xi in sorted_xis:

       distance = xi - prev_pos

       current_time += distance

       # arrival time is current_time

       # get the students in the batch with this xi

       student_indices = xi_to_students[xi]

       # these are the indices within the batch (0 to len(students_in_batch)-1)

       # the global indices are start + idx_in_batch

       for idx_in_batch in student_indices:

           global_idx = start + idx_in_batch

           result[global_idx] = current_time

       # compute unloading time

       k = len(student_indices)

       unloading_time = 1 + (k // 2)

       current_time += unloading_time

       prev_pos = xi

   # after all xis, add return time

   current_time += x_max

   T_available = current_time

So this approach requires for each batch:

- O(m) time to preprocess xi_to_students.

- O(k) time to process each xi, where k is the number of unique xis in the batch.

But since in the worst case, each batch has m unique xis, the total time is O(n) for all batches.

Thus, the algorithm is O(n), which is acceptable for n=1e5.

Testing the sample inputs:

For example, the first sample:

Input:

1 10

3 5

Batch is 1 student. T_available is 0. T_depart = max(0, 3) =3.

x_max=5.

sorted_xis is [5].

Processing:

current_time =3.

distance 5-0=5. current_time +=5 → 8. Assign to student 0 (global index 0) → result[0] =8.

unloading_time =1 + 0 (since k=1) → current_time 9.

Return time is 9 +5=14. So T_available is 14.

So output is 8. Which matches the sample.

Second sample:

n=2, m=1.

Batch 1: first student (3,5). T_available is 0. T_depart = max(0,3) =3.

Processing:

x_max=5. sorted_xis [5]. distance 5-0=5. current_time=3+5=8. assign to student 0. unloading_time 1+0=1. current_time 9. return time 9+5=14.

Batch 2: second student (4,5). T_available is 14. T_depart = max(14,4) =14. x_max=5. sorted_xis [5]. current_time=14. add 5: 19. assign to student 1. unloading time 1+0=1. current_time 20. return time 20+5=25.

So the exit times are 8 and 19, which matches the sample.

Third sample:

5 students, m=4.

students are:

3 5

4 5

5 5

6 5

7 1

Batch 1: first 4 students.

ti_last is 6. T_available is 0. T_depart = max(0,6) =6.

x_list is [5,5,5,5]. x_max=5.

sorted_xis is [5]. Processing:

distance 5-0=5 → current_time=6+5=11.

All 4 students in this xi. unloading_time =1 +4//2 =1+2=3. current_time=14.

return time 14+5=19.

Batch 2: 5th student (7,1). T_available is19. T_depart = max(19,7) =19. x_max=1. sorted_xis [1]. distance 1-0=1 → current_time=19+1=20. unloading_time=1+0=1. return time 20+1 +1 (return time 20+1=21, then add x_max=1 → 21+1=22? Wait, after processing xi=1, current_time is 20 (arrival) +1 (unloading) =21. Then add x_max (1) for return: 21 +1=22. So T_available becomes 22.

So exit time for the 5th student is 20.

But the sample output is 11 11 11 11 20. Which matches.

So the code seems correct.

Now, the code needs to:

- Read n and m.

- Read n lines of ti and xi, in order.

- For each batch, group m students, process as per above.

Now, in Python, for handling large n (up to 1e5), reading input via sys.stdin is better.

Also, preallocating a result list.

Implementing the code.

Let's outline the code:

Read n and m.

students = list of tuples (ti, xi), read from input.

result = [0]*n

T_available =0

for start in range(0, n, m):

    end = start + m

    if end >n: end =n

    batch = students[start:end]

    # batch_last_ti = batch[-1][0]

    batch_last_ti = batch[-1][0]

    T_depart = max(T_available, batch_last_ti)

    # collect xis in batch

    xi_to_students = defaultdict(list)

    x_list = []

    for idx_in_batch, (ti, xi) in enumerate(batch):

        xi_to_students[xi].append(idx_in_batch)

    sorted_xis = sorted(xi_to_students.keys())

    x_max = max(sorted_xis) if sorted_xis else 0  # but batch is non-empty.

    current_time = T_depart

    prev_pos =0

    for xi in sorted_xis:

        distance = xi - prev_pos

        current_time += distance

        # assign to students

        for idx_in_batch in xi_to_students[xi]:

            global_idx = start + idx_in_batch

            result[global_idx] = current_time

        k = len(xi_to_students[xi])

        unloading_time = 1 + (k //2)

        current_time += unloading_time

        prev_pos = xi

    # add return time

    current_time += x_max

    T_available = current_time

print(' '.join(map(str, result)))

But wait, in the code, x_max is the maximum xi in the batch. So sorted_xis is a sorted list of the unique xis. The maximum is sorted_xis[-1].

Yes.

Testing the code.

Sample input 3:

5 4

3 5

4 5

5 5

6 5

7 1

Batch 1: 4 students. x_max is 5. sorted_xis [5].

T_depart is max(0,6) =6.

current_time starts at6.

distance 5-0=5 → current_time 11.

unloading_time for 4 students:1 +4//2=3 → current_time 14.

return time 14 +5=19.

Batch 2: student 4 (7,1). T_available is19. T_depart is max(19,7) =19.

x_max=1. sorted_xis [1].

distance 1-0=1 → current_time 20.

unloading_time 1+0=1 → current_time 21.

return time 21 +1=22.

So the exit times for the first four students are 11, and the fifth is 20. Which matches the sample.

Sample input 2:

2 1:

Batch 0: student 0 (3,5). T_depart 3. x_max 5. sorted_xis [5]. current_time=3+5=8. unloading time 1. current_time 9. return time 9+5=14.

Batch 1: student 1 (4,5). T_available=14. T_depart max(14,4)=14. x_max=5. current_time=14+5=19. unloading time 1. current_time 20. return time 20+5=25.

So the exit times are 8 and 19.

Which matches sample 2.

So code should be correct.

Now, the code uses defaultdict for xi_to_students. But for speed, perhaps using a regular dict and checking for existence.

But in Python, defaultdict is efficient.

But for code efficiency, it's better to precompute the xi_to_students.

Now, possible optimizations:

- Precompute sorted_xis as a list, and x_max as sorted_xis[-1] if there are elements.

But in code, sorted_xis is sorted(xi_to_students.keys()), and since xi_to_students contains all unique xis in the batch, which is non-empty (since the batch is non-empty), x_max is the last element of sorted_xis.

So code is correct.

Another thing: when a batch has all students with the same xi, sorted_xis will have one element. So code works.

Now, for the code to read input correctly, since the students are given in order of strictly increasing ti, which is guaranteed by the problem statement.

So in the code, students are read in order.

Thus, the code should handle all cases.

Edge cases:

- m=1. Each batch has 1 student.

- m=1e5, n=1e5. One batch.

- All students have the same xi. So the sorted_xis is one element. Unloading time is 1 + (m //2) for that batch.

Another edge case: when the batch's xi's are in multiple steps. For example, m=3 students with xis 1,2,3.

Processing sorted_xis [1,2,3]. Each time, the current_time increases by the distance and unloading time.

But code handles that.

So the code seems correct.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    students = []
    for _ in range(n):
        ti, xi = map(int, sys.stdin.readline().split())
        students.append((ti, xi))
    
    result = [0] * n
    T_available = 0
    
    for start in range(0, n, m):
        end = start + m
        if end > n:
            end = n
        batch = students[start:end]
        batch_last_ti = batch[-1][0]
        T_depart = max(T_available, batch_last_ti)
        
        xi_to_students = defaultdict(list)
        for idx_in_batch, (ti, xi) in enumerate(batch):
            xi_to_students[xi].append(idx_in_batch)
        
        sorted_xis = sorted(xi_to_students.keys())
        if not sorted_xis:
            continue
        
        x_max = sorted_xis[-1]
        current_time = T_depart
        prev_pos = 0
        
        for xi in sorted_xis:
            distance = xi - prev_pos
            current_time += distance
            # Assign times to students at this xi
            for idx_in_batch in xi_to_students[xi]:
                global_idx = start + idx_in_batch
                result[global_idx] = current_time
            # Calculate unloading time
            k = len(xi_to_students[xi])
            unloading_time = 1 + (k // 2)
            current_time += unloading_time
            prev_pos = xi
        
        # Add return time
        current_time += x_max
        T_available = current_time
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```