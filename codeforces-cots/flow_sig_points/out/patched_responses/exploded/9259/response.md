<think>
Okay, so I need to solve this problem where I have to find all the percentages from 0 to 100 that are shown on both progress bars at the same time during the copying of files. Let me try to understand the problem step by step.

The problem says that each file is copied one after another. For each byte copied in the current file, two percentages are calculated. The first is the percentage of the current file that's been copied, and the second is the overall percentage of all data copied. Both are floored to the nearest integer. We need to find all the integers that appear in both progress bars at the same time for some moment.

Hmm. So for each byte copied in each file, we compute both percentages and check if they are equal. Then collect all such values and output them sorted.

But if I try to simulate every single byte, especially for large files, that's going to be computationally expensive. Wait, but the constraints say that each a_i is up to 1000, and n is up to 100. So the total bytes could be up to 100 * 1000 = 1e5. That's manageable. So perhaps simulating each byte is feasible here.

Wait, for example, if each a_i is 1000, and n is 100, then the total is 1e5 bytes. For each of those 1e5 steps, we calculate the two percentages. Then, for each of those steps, check if the two percentages are equal, and collect those values. Then we just need to output all unique values found, sorted.

So the plan is:

1. Compute the total sum of all a_i to get the denominator for the overall percentage.
2. For each file i:
   a. For each byte x in 1 to a_i:
      i. Compute current percentage: (100 * x) // a_i
      ii. Compute the sum so far: sum_prev_files + x
      iii. Overall percentage: (100 * sum_so_far) // total_sum
      iv. Check if the two percentages are equal. If yes, add to a set.
3. Also, initial state (0% for both) is included. Wait, the note says that in the first example, the output includes 0. Because when no bytes have been copied, both are 0. Wait, the problem statement says "the very beginning of copying, both bars show 0%." So the initial state (before any bytes are copied) is considered. But according to the description, the bytes are copied in order, and the update happens after each byte is copied. Wait, the initial state is when x=0. Wait, no. Wait, the problem says that after copying the x-th byte, the percentages are computed. So the initial state (before any bytes are copied) is x=0. Let's see:

Wait, the problem statement says:

After copying the x-th byte of file i, the first progress bar shows floor(100x/a_i), and the second shows floor(100*(sum_prev + x)/total). But initially, before any bytes are copied, both are 0? Or is x=0 considered? Let me check the example 1:

Input is 1 file of 6 bytes. The output includes 0. Let's see:

At x=0 (before any bytes are copied?), but according to the problem statement, the progress bars are updated after each byte. Wait, maybe the first step is after copying the first byte. So for the first byte (x=1), the percentages are 100*1//6=16, and (1*100)/(6) = 16.666... floored to 16. So both would be 16. Then, after x=2, 200//6 is 33.333 floored to 33. Then x=3 is 50, etc. So the initial state (x=0) is when no bytes have been copied, but according to the problem statement, the very beginning (before any bytes) shows 0. So when x=0 is considered?

Wait, the problem says: "В самом начале копирования оба прогресс-бара показывают 0 процентов." So the very start (before any bytes are copied) is when x=0. So for each file, we have x ranging from 0 to a_i. Wait, but the copying of each byte happens one after another. For example, for a file of 6 bytes, we have 6 bytes copied. So after each byte, the x increments. So for x=1, x=2, ..., x=6. Wait, but for x=6, that's the entire file. So the first progress bar would be 100*6/6=100%. So for the first example, the steps are x=0 (0%), then after each byte, x goes from 1 to 6. So in that case, the percentages would be 16, 33, 50, 66, 83, 100. So the output includes 0 and all those percentages. Which matches the first example.

So the initial state (x=0) is considered. So for each file, before any bytes are copied (x=0), the current file's percentage is 0 (since x=0), and the total is sum_prev_files + 0. Sum_prev_files is the sum of all previous files. For the first file, sum_prev is 0, so x=0 gives total_sum of 0. So the overall percentage is 0. So for the initial state of each file, x=0, both percentages are (0, sum_prev + 0 / total). Wait, but the initial state is only once, right? Like, before any files are copied. Or do we consider x=0 for each file?

Wait, the files are copied in order. For each file, you copy a_1 bytes, then a_2, etc. For each file i, x ranges from 1 to a_i. After each x, the percentages are updated. Wait, no. Because in the problem statement, "после копирования каждого байта" — after copying each byte. So for each byte copied (from the current file), x is the number of bytes copied so far in the current file. So for each file i, the first byte is x=1, then x=2, etc., up to x=a_i. However, the initial state is when no bytes have been copied. So x=0 for all files. Wait, no. The initial state is before any files are copied, so x=0 for the first file. Then after copying the first byte, x=1. Then after the a_1 bytes, the next file starts, and x starts at 0 again? No. Because when you start copying a new file, the first byte is x=1. So the x for each file i starts at 1 and goes up to a_i. But the problem statement says that after copying the x-th byte of file i, the percentages are calculated. So for each file i, the x ranges from 1 to a_i. But what about x=0 for the next files?

Wait, no. Because when you start a new file, you haven't copied any bytes yet. So the first byte is x=1. Wait, maybe I need to model each step as x from 1 to a_i. But then the initial state (before any files) is x=0 for the first file, which would give 0% for both. Then after the first byte of the first file, x=1. So the initial state (all files not started) is x=0 for the first file. Then, after the first byte, x=1, and so on. Hmm, this is a bit confusing.

Let me re-examine the problem statement:

Formally, after copying the x-th byte from file i, the first progress bar shows floor(100x/a_i), the second shows floor(100*(sum_prev + x)/total). Sum_prev is a_1+...+a_{i-1}.

So during the copying of the first file, x starts at 1 (after first byte) and goes up to a_1. But before any bytes are copied (x=0), both bars are 0. So the initial state is considered. For example, in the first sample, the output starts with 0. So when the copying starts, x=0 for the first file (since no bytes have been copied yet), which gives 0% for both. Then after each byte (x=1 to 6), we get the other percentages.

Wait, but according to the problem statement, the initial state (before any bytes are copied) is when both are 0. So for each file, before copying any bytes of that file, x=0. But how?

No, perhaps the initial state is x=0 for the first file. Then, after the first byte, x=1, and so on. Then, after finishing the first file (x=a_1), the next file starts with x=0 again (but no, because the next file's x starts at 1 when the first byte is copied). Wait, perhaps for each file, the x is the number of bytes copied in that file. So when you start a new file, x starts at 0 (no bytes copied yet), and after each byte, x increments. But according to the problem statement, after copying each byte, x is the count of bytes copied in the current file. So for the first byte of a file, x=1, and so on.

Wait, maybe the problem's x is 1-based. So after the first byte of the file, x is 1. So for each file i, the possible x values are 1, 2, ..., a_i. But then, what about x=0? The problem states that the very beginning (before any bytes are copied) is when both are 0. So for x=0 in the first file. So for each file i, when it's the current file, x can be from 0 (before any bytes are copied in this file) to a_i (after all bytes are copied). Wait, no. Because the first progress bar for file i is calculated as x divided by a_i. When x=0, it's 0%. But after the first byte (x=1), it's 100*1/a_i.

So the initial state (before any files) is x=0 for the first file, and sum_prev is 0. Then, when the first byte is copied, x becomes 1. Then, after copying all a_1 bytes, x=a_1, and move to the next file. For the next file, x starts at 0 (so sum_prev is a_1 + ... + a_{i-1}, and x is 0). But then, when the first byte of the next file is copied, x becomes 1, and so on.

Wait, this is confusing. Let's take the first sample input:

n=1, a_1=6.

The output is 0, 16, 33, 50, 66, 83, 100.

So the initial state (x=0) gives 0. Then after each byte (x=1 to 6):

x=1: 100*1/6 = 16.666, floored to 16. Sum_prev is 0, sum_prev + x = 1. total is 6. So 100*1/6 = 16.666 floored to 16. So both are 16. So 16 is included.

x=2: 200/6=33.333 → 33. sum_so_far is 2 → 33.333 →33.

So each x from 1 to 6 in the first file gives those percentages. Then, when x=6 (the last byte), 100% for both.

So the initial x=0 (before any bytes) is considered as part of the first file. Then for each subsequent file, when the file starts, x is 0 again. But how? Because after the first file, when the second file starts, the sum_prev is a_1, and x starts at 0. Then after each byte, x increments. So for example, in the second sample:

Input is 2 files with 100 and 500 bytes. The output includes 0, 95-100. Let's see:

The total is 600.

The first file's x ranges from 0 to 100. Wait, no. Because when the first file is being copied, x is the bytes copied in that file. So after each byte of the first file, x is 1 to 100. Then when the first file is done, the sum_prev is 100, and the second file starts. For each byte in the second file (x=1 to 500), we compute:

First bar: 100*x/500 → but for x in 1-500.

Second bar: (100 + x)/600 *100 → floored.

But when the second file starts, x can be 0 (before any bytes are copied) → sum_prev + x = 100 + 0 = 100. So (100*100)/600 = 16.666 →16. So first bar is 0%, second is 16.666 → 16. So percentages are 0 and 16. Not equal. So this is a possible step. But when the second file starts (x=0), but according to the problem statement, after copying each byte. So the x=0 for the second file is only present before any bytes are copied in that file. But when does that happen? Because after the first file is copied (x=100), we proceed to the second file. Then, before copying any bytes, the x is 0. But according to the problem statement, the progress bars are updated after each byte. So during the transition between files, is there a step where x=0 for the new file? Or is the x=0 for the new file only considered when the file hasn't started yet?

This is a critical point. Because if x can be 0 for each file (before any bytes are copied in that file), then for the second sample, during the transition between the first and second file, there's an x=0 step. But according to the problem statement, after copying each byte. So between files, there's no copying happening, so there's no step where x=0 for the new file. The x=0 step occurs only once, before any files are copied.

Wait, the problem says: after copying the x-th byte of file i. So during the copying of file i, x ranges from 1 to a_i. So for the first file, the steps are x=1, 2, ..., a_1. For the second file, x=1, 2, ..., a_2. So there is no x=0 for the second file. Then how does the initial x=0 (sum_prev=0) come into play?

Ah! The initial state is before any bytes are copied. So before the first file starts. So x=0 for the first file, sum_prev=0. So both percentages are 0. So that's the first occurrence of 0. Then, after each byte copied, the steps are x=1, 2, etc. So for each file i, x runs from 1 to a_i. But there's an initial x=0 step only once, before the first byte of the first file.

Wait, but according to the problem statement, the very beginning (before any bytes) is considered. So that's the only x=0 step. So how to model this.

So for all files, the steps are:

- Initial step: x=0 in the first file. Both percentages are 0. This is included.

Then, for each file i:

   for x in 1 to a_i:

      compute current_percent and overall_percent.

So the initial step is separate, and then for each file, we process each x from 1 to a_i.

Yes, that makes sense. Because when you start, you have copied zero bytes. Then, you copy the first byte (x=1), and so on. So the steps are:

Initial step: 0% for both.

Then, for each file in order:

   for x from 1 to a_i:

      calculate the percents.

So, the code needs to:

- Process the initial x=0 for the first file (sum_prev=0, x=0) → both percents are 0.

- Then, for each file i from 0 to n-1:

   sum_prev = sum of a_0 to a_{i-1}

   for x in 1 to a_i:

      current_percent = (100 * x) // a_i

      sum_so_far = sum_prev + x

      overall_percent = (100 * sum_so_far) // total_sum

      if current_percent == overall_percent, add to the set.

But wait, sum_prev for the first file is 0. So for i=0 (assuming 0-based), sum_prev is 0. For x=1 to a_0.

Wait, maybe the code structure should be:

Compute total_sum = sum(a_i).

Initialize sum_prev = 0.

Check the initial state (x=0 for first file):

current_percent = (0 * 100) // a[0] → 0.

sum_so_far = sum_prev + 0 →0.

overall_percent = 0.

So both are 0. So add 0 to the set.

Then, for each file in order:

   current_a = a[i]

   sum_prev_files = sum of all previous files.

   for x in 1 to current_a:

      current_percent = (100 * x) // current_a

      sum_so_far = sum_prev_files + x

      overall_percent = (100 * sum_so_far) // total_sum

      if current_percent == overall_percent:

          add to the set.

   sum_prev_files += current_a

But then, after the first file, sum_prev_files is a_0. Then the second file's x ranges from 1 to a_1.

So this way, the initial step is handled once, and all other steps are handled per byte.

So, for the first sample, the initial step (0,0) is added. Then x runs from 1 to 6.

For each x, compute current_percent and overall_percent. For example, x=1:

current_percent = 100 * 1 //6 =16.

sum_so_far =0 +1=1.

overall_percent=100 *1//6=16. So 16 is added.

x=6:

current_percent=100*6//6=100.

sum_so_far=6.

overall_percent=100*6//6=100.

So 100 is added.

So the code needs to handle the initial x=0 case (once), and then process each x from 1 to a_i for each file.

So, the steps are:

- Add the initial 0.

- For each file i:

   sum_prev = sum of a[0..i-1]

   for x in 1 to a[i]:

      current = (100 *x )//a[i]

      sum_so_far = sum_prev +x

      overall = (100 * sum_so_far) // total_sum

      if current == overall → add to set.

So that's the plan.

Now, how to implement this efficiently.

The constraints are n up to 100, a_i up to 1000. So total bytes is up to 1e5. So even with n=100, a_i=1000 each, that's 100*1000=1e5 steps. For each step, compute two percentages and check equality. That's manageable.

So code steps:

Read n.

Read a as a list.

Compute total = sum(a).

If total is zero → but a_i are at least 1, so sum is >=1.

Initialize a set, result, and add 0 (from the initial step).

sum_prev =0.

for each i in 0 to n-1:

    current_a = a[i]

    for x in 1 to current_a:

        curr_percent = (100 *x) // current_a

        sum_so_far = sum_prev +x

        overall = (100 * sum_so_far) // total

        if curr_percent == overall:

            add to result.

    sum_prev += current_a

Finally, after processing all files, add 100% if possible.

Wait, but when x equals a_i, the current_percent is 100% (since 100 * a_i / a_i =100). The sum_so_far would be sum_prev +a_i = sum_prev_files +a_i. sum_prev_files is the sum of all files before i. So sum_so_far is sum_prev_files +a_i → sum_prev_files +a_i = sum_prev_files +a_i → sum_prev is sum_prev_files, then sum_prev +=a_i. So sum_so_far for x=a_i is sum_prev_files +a_i → sum_prev after processing this file is sum_prev_files +a_i. So the overall percent is (100 * sum_so_far) // total → sum_so_far is sum_prev_files +a_i, which is sum_prev after this file. So in the case when x=a_i, sum_so_far is sum_prev after processing this file.

But the code above processes x from 1 to a_i. So for each x, including a_i.

Wait, for example, if a_i is 100, then x ranges from 1 to 100. For x=100, curr_percent is 100.

sum_so_far is sum_prev +100. So if sum_prev +100 is the total, then overall percent is 100. So for the last file, when x=a_i, sum_prev +a_i is sum of all files. So overall percent is 100. So curr_percent is 100. So 100 is added.

But in the code above, this case is handled in the loop. So for x=a_i, which is processed in the loop.

So for example, the first sample's last x=6:

sum_prev is 0 (since it's the first file). x=6.

sum_so_far is 6. total is 6. 100*6//6=100. So curr_percent and overall are 100. So added to the set.

So the code includes 100 in the set.

So after processing all files, do we need to check anything else?

No. Because the initial step is 0, and the final step (x=a_n) would have sum_so_far equal to total sum → overall 100, and current_percent is 100. So 100 is added.

But wait, if the total is zero? But the constraints say a_i >=1. So sum is at least 1. So division by zero is impossible.

So the code is correct.

Now, what about the second sample:

Input: 2

100 and 500. Total is 600.

The initial step adds 0.

Then for the first file (100):

sum_prev is 0.

x ranges from 1 to 100.

For x in 1-100:

current_percent = (100x)/100 = x. So 1,2,...,100.

sum_so_far =0 +x.

overall = (100x) //600.

For example, x=100:

sum_so_far is 100. (100*100)/600 = 16.666... →16. So current_percent is 100. So 100 vs 16: not equal. So not added.

But for x=95:

sum_so_far is 95. overall = (95*100)//600 →9500/600=15.833 →15. current_percent is 95. Not equal.

So during the first file's processing, the only case where current_percent equals overall_percent is when x is 0 (initial step) and possibly x=0. But wait, x is 1-100 here.

So during the first file, for x=1:

current is 1.

sum_so_far=1. overall= 0.166 →0. 1 vs 0: not equal.

So no matches here.

Then, the first file is processed. sum_prev becomes 100.

Then, process the second file (500 bytes):

x from 1 to500.

current_percent is (100x)/500 → 0.2x → x//5.

sum_so_far is sum_prev +x =100 +x.

overall is (100*(100 +x))//600.

So for each x in 1-500:

current = x//5.

overall = (100(100+x)) //600.

We need to find x where x//5 == (100(100+x))//600.

The output of the second sample is 0,95-100, 100.

Wait, the sample output is 0, 95,96,97,98,99,100.

So how do these numbers come about?

In the second sample, during the second file's processing.

For x=475: current =475//5=95. sum_so_far=100+475=575. overall= (575 *100)/600= 95.833... →95. So 95 equals 95. So add 95.

x=475 gives 95.

x=476: 476//5=95.2 →95. sum_so_far 576 →57600/600=96.0 →96. 95 !=96.

Wait, no. 576 *100 /600 = 57600 /600 = 96. So overall percent is 96.

current_percent is 476//5=95. So 95 !=96. So no.

But in the sample output, 95 is present.

So when x=475, sum_so_far=575. 575*100/600= 95.833, floored to 95. So current is 475//5=95. So 95=95 → added.

x=480: 480//5=96. sum_so_far 100+480=580 →580*100/600=96.666 →96. So 96 ==96 → added.

x=480 gives 96.

Similarly:

x=485 →485//5=97. sum_so_far 585 →58500/600=97.5 →97. 97 ==97 → added.

x=485: current 97, overall 97.5→97. So yes.

x=490 →490//5=98. sum_so_far 590 →59000/600=98.333 →98. 98=98 → added.

x=495 →495//5=99. sum_so_far 595 →59500/600=99.166 →99. So added.

x=500 →500//5=100. sum_so_far 600 →100% → added.

So these x values (475,480,485,490,495,500) in the second file's processing contribute 95,96,97,98,99,100.

But how?

Wait, let's compute for x=475:

sum_so_far =100 +475=575.

575 *100 /600 = 57500/600 = 95.833 →95.

current_percent is 475//5=95. So 95 equals 95 → added.

x=480: sum_so_far=580. 580*100/600=58000/600=96.666 →96. current_percent=480//5=96. So 96 equals 96 → added.

Similarly for other x's.

So during the processing of the second file, x ranges from 1 to 500. For some x's, the current and overall percents are equal.

Thus, the code correctly processes all these steps.

So the code is correct.

Now, code steps:

Read n.

Read a list.

Compute total = sum(a).

Initialize a set with 0 (from the initial step).

sum_prev =0.

Loop over each file in a:

   current_a = a[i]

   for x in 1 to current_a inclusive:

      curr = (100 *x) // current_a

      sum_so_far = sum_prev +x

      overall = (100 * sum_so_far) // total

      if curr == overall:

          add to the set.

   sum_prev += current_a

Finally, sort the set and print each element.

But wait, in the second sample, when processing the second file (500), x=475 is in the loop. The code adds 95. Similarly for other x's.

Thus, this approach should collect all possible values.

Now, testing the code with the samples.

Sample 1:

Input 1 6.

sum_prev starts as 0.

Initial step adds 0.

Processing the first file (6 bytes):

for x in 1-6:

x=1: curr=16 (100/6=16.666 →16), sum_so_far=1. overall=100*1/6=16.666→16. So 16 is added.

x=2: 33.333 →33, sum_so_far=2 →33.333→33. So added.

x=3: 50 → sum_so_far=3 →50.

x=4: 66.666 →66. sum_so_far=4 →66.666→66.

x=5:83.333 →83. sum_so_far=5 →83.333→83.

x=6:100 → sum_so_far=6 →100.

So all these percentages are added, plus 0 and 100. So the output is 0,16,33,50,66,83,100 → correct.

Sample 2:

After processing the initial 0, then first file (100) gives no matches. Then sum_prev becomes 100. Then for the second file (500), the code processes x from 1-500 and adds 95,96,97,98,99,100. Also, the final x=500 adds 100. So the output is 0,95,96,97,98,99,100 → correct.

Sample3:

Input4, 1000,2,2,998.

sum_prev starts 0.

Initial step 0.

Processing 1000 bytes (file 0):

x ranges from 1-1000.

current_percent is (100x)/1000 = x//10.

sum_so_far is x.

overall is (100x)/ (1000+2+2+998)= 2000.

So sum_so_far is x.

overall = (x *100) /2000 = x/20.

floor(x/20).

current is x//10.

So when is x//10 == x//20?

When x is 0 (but x ranges from 1-1000). So no matches here except x=0.

Wait, for x=0, it's the initial step. But in the code, for the first file, x starts at 1. So during the first file's processing, no matches. sum_prev becomes 1000.

Then the second file (2 bytes):

sum_prev=1000.

current_a=2.

for x in 1,2.

x=1:

current = (100*1)/2=50.

sum_so_far=1000+1=1001.

overall = (1001*100)/2000 →100100//2000=50.05 →50.

So 50 ==50 → added.

x=2:

current= (200)/2=100.

sum_so_far=1000+2=1002.

overall= (1002 *100)/2000 →100200/2000=50.1 →50. So 100 !=50 → no.

So x=1 adds 50.

sum_prev becomes 1000+2=1002.

Third file (2 bytes):

sum_prev=1002.

x runs 1-2.

x=1:

current (100*1)/2=50.

sum_so_far=1002+1=1003.

overall=1003*100//2000=50.15 →50. So 50 ==50 → added.

x=2:

current=100.

sum_so_far=1004 →1004*100//2000=50.2 →50. 100 !=50 → no.

sum_prev becomes 1004.

Fourth file (998 bytes):

sum_prev=1004.

for x in 1-998:

current = (100x)/998 → floor.

sum_so_far=1004 +x.

overall = (1004+x)*100 //2000.

We need to find x where (100x//998) == ((1004 +x)*100 //2000).

At x=996:

sum_so_far=1004+996=2000. overall=2000*100//2000=100.

current = (996*100)/998 = (99600//998). Let's compute:

99600 ÷ 998 ≈ 99.799... →99.

So current is 99. sum_so_far is 2000 →overall 100. 99 !=100. So no.

But when x=998:

sum_so_far=1004+998=2002. overall=2002*100//2000 →200200//2000=100.1 →100.

current = (998*100)/998 =100. So 100=100 → added.

Also, sum_so_far=2000 when x=996 → sum_so_far=1004 +996=2000. overall=2000*100//2000=100. current for x=996 is (996*100)/998 →99600/998= 99.799... →99. So 99 !=100. Not added.

So in the fourth file, x=998 gives current 100, overall 100 → added.

So the code adds 0,50,99,100. But according to the sample3, output is 0,50,99,100.

Wait, but sample3's output includes 0,50,99,100.

So where does 99 come from?

Wait, during processing of the fourth file (998 bytes):

x= 99 * 998 /100 = 99 →99%?

Wait, maybe for some x in 1-998, current percent is 99 and overall percent is 99.

Let's find such x.

current_percent = (100x) //998 →99.

Which implies 99 ≤ (100x)/998 <100 → 99*998 ≤ 100x <100*998 → 99*998/100 ≤x <998 → 98802/100=988.02 ≤x <998 →x >=989.

So x ranges from 989 to 997.

sum_so_far=1004 +x.

overall_percent= (1004 +x)*100 //2000 → must be 99.

So (1004 +x)*100 must be >=99*2000 =198000 →1004+x >=1980 →x>=1980 -1004=976.

But also (1004+x)*100 < (99+1)*2000 → (1004+x)*100 < 200000 →1004 +x <2000 →x <996.

Wait, this is conflicting.

Wait, for overall_percent to be 99:

99 ≤ ( (1004 +x)*100 ) /2000 <100 → multiply all parts by 2000:

198000 ≤ (1004 +x)*100 <200000 →1980 ≤1004 +x <2000 →1980-1004 ≤x <2000-1004 →976 ≤x <996.

x must be in [976, 995], inclusive.

At the same time, current_percent must be 99:

x >=989 (from previous).

So x must be in [989, 995], and in [976,995].

So x ranges from 989 to 995.

So for x in 989 to 995:

current_percent is 99.

sum_so_far=1004 +x.

overall_percent= (1004 +x)*100//2000.

We need to check if this is 99.

So for x=989:

sum_so_far=1004 +989=1993.

1993*100=199300 →199300//2000=99.65 →99.65 floored to 99.

Yes. So overall_percent is 99. So current 99, overall 99 → add 99.

Similarly for x=989 to 995.

So in this case, there are multiple x's in the fourth file that contribute 99.

So the code will add 99 to the set.

Thus, the code will capture that.

So sample3's code will have 0 (initial), 50 (from second and third files), 99 (from fourth file), and 100 (from x=998). So the output is 0,50,99,100 → correct.

Thus, the code works.

Now, code.

Read n.

Read list a.

Compute total = sum(a).

Initialize a set with 0.

sum_prev =0.

for i in 0..n-1:

   current_a = a[i]

   for x in 1 to current_a:

       curr = (100 *x) // current_a

       sum_so_far = sum_prev +x

       overall = (100 * sum_so_far) // total

       if curr == overall:

           add to set.

   sum_prev += current_a

After processing all files, sort the set and print each element in order.

Now, code in Python:

But wait, in Python, for the initial 0, do we need to process it?

Yes, because the initial state is x=0 for the first file. Which is handled by adding 0 to the set.

But in the code above, after the initial step, when processing the first file, sum_prev is 0, which is correct.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    total = sum(a)

    result = {0}

    sum_prev = 0

    for size in a:

        for x in range(1, size + 1):

            current = (100 * x) // size

            sum_so_far = sum_prev + x

            overall = (100 * sum_so_far) // total

            if current == overall:

                result.add(current)

        sum_prev += size

    # Also, check if 100 is in the result. Because when x=size, sum_so_far is sum_prev + size. sum_prev is sum of previous files. So sum_prev +size = sum_prev_new. And sum_prev_new is sum_prev + size. sum_prev_new is the sum up to this file. But x is processed in the loop. For example, the last file's x=size is processed, sum_so_far is sum_prev + size. Which is sum_prev_new. So when x=size, sum_so_far is sum_prev_new. sum_prev_new is sum of all files processed so far. So when it's the last file, sum_prev_new is total. So 100 is added.

    sorted_result = sorted(result)

    print('\n'.join(map(str, sorted_result)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
100 500
""",
            "output": \
"""\
0
95
96
97
98
99
100
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

Now, let's test sample3's case where 99 is added.

In code, during the fourth file (size=998), x ranges from 1 to 998.

At x=989:

current = (100 *989) //998 → 98900//998=99.099… →99.

sum_so_far=1004 +989=1993.

overall= (1993 *100) //2000 →199300//2000=99.65 →99.

So current == overall →99 is added.

Similarly, x=990: 100*990//998=99000//998=99.199… →99.

sum_so_far=1004+990=1994 →199400//2000=99.7 →99.

So 99 is added.

Thus, the code adds 99 to the set.

So the code is correct.

Thus, the code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
result = {0}
sum_prev = 0

for size in a:
    for x in range(1, size + 1):
        current = (100 * x) // size
        sum_so_far = sum_prev + x
        overall = (100 * sum_so_far) // total
        if current == overall:
            result.add(current)
    sum_prev += size

print('\n'.join(map(str, sorted(result))))
```
