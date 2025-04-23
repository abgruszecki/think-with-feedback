<think>
Okay, let's tackle this problem. Hmm. The task is to determine if Bob's birth date can be rearranged in such a way that he is at least 18 years old on the finals date. Also, the birth date must be in the same century as the finals. Oh right, the century is important. Wait, the problem says the finals are between 2001-2099, so YY is 01 to 99. So the finals' year is 20YY, right? And the birth year BY is part of the same century. Wait, the participant's birth must be in the same century as the finals. Wait, the problem statement says: "eligible participant must be born in the same century as the date of the finals." So the birth year (after rearrangement) must be in the same century as the finals. Wait, the finals are in 20YY, so the century is 2001-2100 being the 21st century. So the birth date's year (after rearrangement) must be in the same century as the finals. Wait, but the finals are in 20YY (so year 20YY, which is 2000 + YY). So the century is 2001-2100. So the birth year must be in that same century. Wait, but the birth year BY is given as part of the BD.BM.BY. But when rearranged, the three parts (day, month, year) can be permuted. So the BY part is part of the possible permutations. Wait, no. Wait, the problem says: the BD.BM.BY is the original date, but Bob can rearrange the numbers (the three components: day, month, year) into any order, so the birth date could be any permutation of those three numbers. So for example, if BD is 05, BM is 04, BY is 03, then possible permutations could be 03.04.05 (as day, month, year). But each component is kept as two digits. So when permuting, the three numbers are rearranged. Each part (day, month, year) is a two-digit number. So the original three numbers are day, month, year. But when rearranged, any permutation of those three. So for example, the original day becomes the year in the rearranged date. But each is kept as a two-digit number.

So the problem is: find if any permutation of the three parts (d, m, y) from the birth date (BD, BM, BY) can form a valid date such that:

1. The birth date (after permutation) is a valid date (so day must be between 1 and the maximum days in that month, considering leap years if necessary for February).
2. The birth date is in the same century as the finals date. The finals date's year is 20YY. So the birth year (after permutation) must be in 2001 to 2099? Wait, the same century as the finals. Wait, the problem says "the same century as the date of the finals. So the finals' date's century is 2001-2100 (since the year is between 2001 and 2099). So the birth date's year (after permutation) must be in that same century. So the birth year (as a four-digit number) must be between 2001 and 2099. But wait, when the birth date is permuted, the BY is part of the three numbers, but the year is two digits. So how do we interpret that? Oh, right, the problem says that the birth date's year is part of the same century. Wait, the problem states that "the year is in the same century as the date of the finals". So the finals' year is 20YY. So the birth year must be in 20xx (same century as 20YY). So the birth year (as a four-digit number) is 20xx, where xx is the year part after permutation. So when the birth date's year component (after permutation) is, say, 80, then the full year is 2080. So, the birth date's year (four digits) is 20xx. So the two-digit part is from 00 to 99, making the full year 2000-2099. So when permuting the three parts (BD, BM, BY), the year part in the birth date must be between 00 and 99 (as per the input constraints, BY is in 01-99, but wait, no. The problem says that the input dates are correct. The input lines are correct dates. So BD and BM are valid day and month, and BY is between 01 and 99. But when permuting, the three parts can be rearranged, so the year could be, for example, the original BD (which is a day, so up to 31). So when permuting, the birth year (two digits) can be up to 31, making the full year 2031, which is in the same century.

Wait, no. For example, if the finals are in 2099 (YY is 99), the century is 2001-2100. So the birth year must be between 2001 and 2100. But since the birth year is in the same century as the finals, which is 20yy, the birth year's full is 20xx. So the two-digit part (xx) is from 00 to 99, so 2000 to 2099. But wait, the problem says that the finals are between 2001 and 2099. So the finals' year is 2001-2099. The birth year, after permutation, must be in the same century. So birth year (full) must be in 2001-2099. So the two-digit part is from 01 to 99 (since 2000 is part of the 20th century). Wait, but the problem says that the birth date's year (after rearrangement) must be in the same century as the finals. So the finals are in the 21st century (2001-2100), so the birth year must be in 2001-2100. But since the two-digit year part can be 00 (as part of the permutation, maybe), but 2000 would be part of the 20th century (since centuries are counted from year 1). So the problem's note says that the eligible participant must be born in the same century as the date of the finals. So, for example, if the finals are in 2001 (20YY where YY=01), then the same century would be 2001-2100. So birth years must be in that range. But how do we compute the four-digit year for the birth date's year part when it's a two-digit number?

Wait, according to the problem statement: the years of the finals are in 2001-2099. So the birth date's year (after permutation) must be between 2001 and 2099. So when the two-digit part is 00, the full year is 2000, which is part of the 20th century. So that would not be allowed. So the birth date's four-digit year must be 2001 <= Y <= 2099.

But when permuting the three parts (BD, BM, BY) of the birth date, the three parts are two-digit numbers. So the possible two-digit values for the year part can be BD, BM, or BY. For example, BD could be 31 (as a day), but when permuted as the year part, it becomes 2031. So that's allowed. So the birth year is 2031, which is in the same century as the finals (if the finals are in 20YY, which is 20xx as well). So as long as the two-digit year part is between 01 and 99, then the full year is between 2001 and 2099. Wait, no. Because 00 would be 2000. But according to the problem statement, BY is in 01-99, but BD and BM can be up to 31 and 12 respectively. So when permuting, the year part could be a value from BD, BM, or BY. So BD can be 01-31, BM can be 01-12, BY is 01-99. So the possible two-digit values for the year part after permutation are:

- From BD: 01-31 (since original date is valid, BD is a valid day, which is 1-31, but some months have fewer days, but the input is valid, so BD is at least 1 and up to the max days of its month. But when permuting, those constraints are not considered, except that the permuted date must be valid. So when permuting, for example, BD could be 31, which as a year part becomes 2031. That's allowed.

Wait, the problem says that the input dates (both finals and birth) are valid. So the original BD and BM are valid day and month. But when permuting, we have to check if the new arrangement is a valid date (day, month, year). So for each permutation of the three parts (d, m, y), where d, m, y are BD, BM, BY in some order, we need to check if d is a valid day, m is a valid month, and y is a valid two-digit year (but the problem allows any two-digit year, since the input's BY is 01-99 but permuting can lead to y being other numbers. Wait, the input's BD and BM are valid, but when permuted, the parts can have values that are invalid as day, month, etc. So each permutation must form a valid date. For example, if the birth date is 31.12.99, then permuting to 99 as the month would be invalid (12 is max), so that permutation is invalid.

So the steps for solving the problem are:

1. Generate all possible permutations of the three parts (d, m, y) from the birth date. For each permutation, check if it's a valid date (i.e., day is between 1 and the maximum days in the given month, considering leap years if the month is February and the year is a leap year). The year here is the two-digit part, which when combined with 20 gives the full year (since the birth must be in the same century as the finals, which is 20xx). So the full birth year is 20y, where y is the two-digit year part.

2. For each valid birth date (after permutation), check if the person is at least 18 years old on the finals date. Also, check that the birth year is in 2001-2099 (since same century as finals, which are in 2001-2099). Wait, the finals are in 20YY, which is 2000 + YY. So YY is 01 to 99, making the finals' year 2001-2099. So the birth date's full year must be 2001-2099. So the two-digit year part (y) must be between 01 and 99, but when permuting, the year part could be from BD (which can be up to 31, but 31 as a two-digit year is 2031, which is valid). So the full birth year is 20y, where y is the permuted year part. So to be in the same century, the birth year must be >=2001 and <=2099. Which implies that the two-digit year part (y) must be >=01 and <=99 (since 20y is 2001 when y is 01, and 2099 when y is 99). So when permuting, the year part can be 01-99. Wait, but the permuted year could be BD or BM, which could be 01-31 or 01-12. So as long as the two-digit y is between 01 and 99, the birth year is valid for the same century. So for example, if the permuted year is 01 (from BD=01), then full year is 2001, which is okay. So, for each permutation, after converting the three parts into day, month, year (d, m, y), the birth date's full year is 20y. Then, check if 20y is >=2001 and <=2099. Wait, but the problem says that the participant must be born in the same century as the finals. Since the finals are in 20yy (2001-2099), the same century is 2001-2100. But the birth year must be in the same century. So the birth year can be up to 2100. But the problem says that the finals are between 2001-2099, so the birth year is allowed to be in 2001-2099. Because 2100 is in the same century as 2001-2100, but the finals are not in 2100. Wait, the problem statement says that the finals are between 2001 and 2099. So the birth date's full year must be between 2001 and 2099. So the two-digit part y must be between 01 and 99. Because 2000 is not allowed. So, in this problem, the birth date's year (after permutation) must be 2001 <= Y <= 2099. So the two-digit y must be between 01 and 99.

So, during permutation checking, the permuted year part (y) must be between 01 and 99. Otherwise, the birth date is invalid. For example, if the permuted year is 00, then the full year is 2000, which is not in the same century as the finals (since 2000 is part of the 20th century, whereas the finals are in 21st). So such a permutation is invalid.

Therefore, for each permutation (d, m, y), we need to:

- Check that the full birth year is 20y, and 2001 <= 20y <= 2099. So y must be 01 <= y <=99.

- Check that (d, m, 20y) is a valid date. That is, d is a valid day for month m in year 20y (considering leap years for February).

Once we have a valid birth date, we need to check if Bob is at least 18 years old on the finals date.

How to compare the two dates:

We need to compute the birth date (after permutation) and the finals date. If the birth date is <= finals date minus 18 years, then it's valid. Or wait, if the finals date is on or after the birth date plus 18 years, then it's valid.

So, the algorithm would be:

For each valid permutation (birth date):

birth_date = (d, m, 20y)  # converted to a date object

finals_date = (dd, mm, 20yy)

We need to check if birth_date <= finals_date minus 18 years.

But how to handle dates when adding 18 years? For example, if the finals date is 2023-03-05, and the birth date is 2005-03-05, then adding 18 years would take birth date to 2023-03-05. So if finals date is on that day, it's allowed. If the birth date is 2005-03-04, then the 18th birthday would be 2023-03-04. So the finals date must be on or after that.

So the condition is: birth_date + 18 years <= finals_date.

So, we can model this by comparing the birth date plus 18 years to the finals date.

But how to handle the dates? Let's think in terms of years, months, days.

For example, if the birth date is 2000-02-29 (leap year), adding 18 years would result in 2018-02-28, since 2018 is not a leap year. So this needs to be considered.

So the approach is to compute the birth date's date (d, m, Y) and add 18 years, then see if the finals date is on or after that adjusted date.

But how to compute that adjusted date?

Alternatively, we can compare the two dates (finals date and birth date plus 18 years). If the finals date is >= the birth date plus 18 years, then it's allowed.

So for each valid permutation:

1. Compute the birth date (as a date object).

2. Add 18 years to the birth date. How?

Well, adding 18 years to the birth year, but also adjusting for leap days. For example, if the birth date is February 29, 2000, adding 18 years would take us to 2018, which is not a leap year. So the date becomes February 28, 2018.

So, in code, we can model the birth date plus 18 years as follows:

new_year = birth_year + 18

if the original birth month and day are February 29, and new_year is not a leap year, then set to February 28.

Else, same day and month.

So, to check if the finals date is on or after this new date.

But how to implement this in code?

Another approach: calculate the birth date plus 18 years, then compare to the finals date.

Let's see:

birth_year = 20y

after adding 18 years: new_year = 20y + 18

the new date is (d, m, new_year). But we need to check if this date is a valid date.

For example, if the original birth date is 2000-02-29 (leap year), adding 18 gives 2018. Since 2018 is not a leap year, 02-29 is invalid. So the adjusted date would be 2018-02-28.

So the adjusted date is min(d, last day of m in new_year).

So in code, for a given birth date (d, m, Y), when adding 18 years, we can:

- new_year = Y + 18

- check if m is February and d is 29, and new_year is not a leap year. If so, set d to 28.

Else, check if the date (d, m, new_year) is valid. If not, adjust to the last day of the month.

But for the purposes of this problem, perhaps we can compute the new date as (d, m, Y + 18), but adjusting the day if necessary. Then, compare this new date to the finals date.

So to implement this, perhaps we can:

For the adjusted birth date (d, m, Y +18):

If the month and day exist in that year, then it's the same day and month.

Else, adjust to the last day of the month.

Then, compare the finals date to this adjusted date.

But how to check if a date (d, m, Y +18) is valid?

We can use the same function we use to check the validity of any date.

So steps for each permutation:

- Check if the birth date (d, m, 20y) is valid. Also check that 20y is >=2001 and <=2099 (so y is 01-99).

If valid:

- Compute new_year = 20y + 18.

- Create a new date (d, m, new_year). Check if this date is valid. If not, adjust d to the last day of month m in new_year.

- Compare this adjusted date to the finals date (20yy, mm, dd). If the adjusted date <= finals_date, then this permutation is acceptable. So return YES.

So, for each valid birth date permutation, compute the 18th birthday's date (adjusted if necessary), and see if it's <= the finals date.

If any permutation satisfies this, then the answer is YES. Otherwise, NO.

Now, the problem is to generate all permutations of the three parts (BD, BM, BY) and check each permutation.

But how to generate all permutations. Since there are 3! =6 possible permutations. For each permutation, the order is (d, m, y), (d, y, m), (m, d, y), (m, y, d), (y, d, m), (y, m, d). Wait, no. The three parts can be arranged in any order. So permutations are all possible orderings of the three elements. So the three elements are BD, BM, BY, and for each permutation, the first element is the day, the second is the month, the third is the year. Or wait, no. Wait, in the problem statement, the three numbers are rearranged. So each permutation of the three numbers (BD, BM, BY) is considered. For example, if the original is 01.02.03, possible permutations are (01,02,03) (original), (01,03,02), (02,01,03), (02,03,01), (03,01,02), (03,02,01). So each of these six possibilities is considered. For each permutation, the day is the first element, the month the second, and the year the third. So each permutation represents a possible birth date (d, m, y), where d is BD, BM, or BY, and same for m and y.

So, the code needs to generate all possible permutations of the three components (BD, BM, BY), treating each as a possible (d, m, y) for the birth date. Then, for each permutation, check if it's a valid date, and whether the birth year is in 2001-2099. Then, for those valid dates, check if the 18th birthday is before or on the finals date.

Now, how to represent dates in code. Let's parse the finals date and the birth date's parts.

First, parse the finals date: the input is DD.MM.YY. So DD, MM, YY are two-digit strings. So the finals date is (DD, MM, YY). The finals' year is 20YY. For example, 01.01.98 is 01 January 2098.

The birth date's original is BD.BM.BY, and after permutation, the three parts are arranged into d, m, y. So the birth date's year is 20y. So for each permutation, we can get d, m, y (as strings, perhaps), then check:

1. 20y is >=2001 and <=2099. So y must be between 01 and 99. So when the permutation's y part is BD, which could be 31 (as a day), then 20y is 2031, which is allowed.

2. Check if the day (d) is valid for month m in year 20y (considering leap years for February).

Once that's valid, proceed to compute the 18th birthday's date.

Then, compare that date to the finals date.

So the steps in code would be:

Parse the finals date into (dd, mm, yy), then convert to integers. The finals' year is 2000 + int(yy). Similarly, the birth date's original parts (BD, BM, BY) are parsed.

Generate all permutations of (BD, BM, BY) as possible (d, m, y) for the birth date.

For each permutation:

- y must be between 01 and 99 (as a two-digit string). Wait, no. The two-digit y can be 00, but then 20y is 2000, which is not allowed. So y must be in 01-99. So for each permutation's y part (which is BD, BM, or BY), we need to check if when converted to a two-digit string, it's between 01 and 99. Because BY is given as 01-99 (since the input is correct). But BD and BM could be 01-31 or 01-12. So when permuting, the y part could be BD or BM. For example, BD is 31 (as a day), which as a two-digit year would be 31, so 2031. Which is allowed.

So for the permutation's y part, we need to check that it is between 01 and 99. Because 00 would be invalid (20y = 2000). So for example, if the permutation's y part is 00 (but the input would have such a value?), but the input constraints say that both dates are correct. Wait, the problem says that the input dates are correct. So BD, BM, BY in the birth date are valid. But BD is a valid day (so between 1 and 31, but possibly up to 30 or 28 depending on month). But when permuting, the y part can be BD, which could be, say, 31, which as a two-digit year is 31, which is allowed.

So in code:

For each permutation (d_part, m_part, y_part):

d_str = d_part

m_str = m_part

y_str = y_part

Check:

- y_str is between '01' and '99' (since 20y must be between 2001 and 2099). So y_str must be a two-digit string with value >=1 and <=99. So 00 is invalid. So, for example, if the permutation's y_part is '00', then 20y is 2000, which is invalid.

So first, check if the y_str is in '01' to '99'.

If not, skip this permutation.

Else, proceed.

Then, check if the birth date (d_str, m_str, 20y_str) is a valid date.

To check if a date is valid:

- Convert m_str to integer (month). Check if month is between 1 and 12.

- Convert d_str to integer (day). Check if day is between 1 and the maximum days of the month.

- For February, check if leap year. The leap year rule is given: a year is leap if divisible by four. Since the birth year is between 2001 and 2099, which is 2001 <= Y <= 2099. So to check leap year, Y is divisible by 4.

So for the birth date's year (Y = 2000 + int(y_str)), check if it's a leap year.

Then, for February, the maximum day is 29 if leap, else 28.

For other months, standard days (30 or 31).

If the day is valid for the month and year, then proceed.

Once the birth date is valid, proceed to calculate the 18th birthday date.

So:

birth_year = Y (20y_str)

new_year = birth_year + 18

new_month = month (m_str as integer)

new_day = day (d_str as integer)

Check if (new_day, new_month, new_year) is a valid date. If not, adjust to the last day of the month.

So:

If new_month is February:

   if new_year is leap:

      max_day = 29

   else:

      max_day = 28

Else:

   if new_month in [4,6,9,11]:

      max_day =30

   else:

      max_day=31

if new_day > max_day:

   adjusted_day = max_day

else:

   adjusted_day = new_day

So the adjusted date is (adjusted_day, new_month, new_year)

Now, compare this adjusted date to the finals date.

The finals date is (dd, mm, 20yy), where dd is the day, mm is the month, and 20yy is the year.

So, the finals date's components:

finals_day = int(dd)

finals_month = int(mm)

finals_year = 2000 + int(yy)

We need to check if the adjusted date (adjusted_day, new_month, new_year) is <= (finals_day, finals_month, finals_year).

We can compare the dates as tuples in order (year, month, day).

So:

adjusted_date = (new_year, new_month, adjusted_day)

finals_date = (finals_year, finals_month, finals_day)

if adjusted_date <= finals_date:

   then this permutation is valid, return YES.

So, for each permutation, if any of them satisfies all the conditions, output YES. Else, output NO.

Now, the code steps:

Parse the input:

Read two lines: finals_line and birth_line.

Split into parts.

For example:

finals_line = '01.01.98' → parts are ['01', '01', '98']

birth_line = '01.01.80' → parts are ['01', '01', '80']

So, birth_parts = [BD, BM, BY] → for the first example, BD is '01', BM is '01', BY is '80'.

Generate all permutations of birth_parts. So all possible orderings of the three elements. For each permutation, assign to d_part, m_part, y_part.

For each permutation:

Check y_part is between '01' and '99'. So, when converted to integer, it's between 1 and 99. So, for example, '00' is invalid. But in the input, since birth_line is a valid date, BY is between 01 and 99. But when permuting, the y_part could be BD or BM, which can be 01-31 or 01-12, but these are all >=01, so y_part is at least 01. Wait, for example, BD can be 01, but when permuted to y_part, it's '01' which is allowed. So in code, after permuting, the y_part is one of BD, BM, or BY, which are strings. BD is a valid day (so between 01 and 31), BM is a valid month (01-12), and BY is 01-99. So when permuting, the y_part is a two-digit string, which can be 01-31 (from BD), 01-12 (from BM), or 01-99 (from BY). So the y_part's integer value is between 1 and 99. Wait, 01 to 31, 01 to 12, or 01 to 99. So the minimum is 1, maximum is 99 (since BY is 01-99, but BD can be up to 31). So the y_part can be from 01 to 99. So the check of y_part being 01-99 is automatically satisfied. Wait, no. For example, if BD is 32 (but input is valid, so BD is a valid day. So BD can't be 32. So the permuted y_part can't be 32. Because the input is valid. So the original BD is a valid day for its month. So when the input is given, BD is in 01-31, but possibly less (like 30 for April, etc.). So when permuting, the y_part is BD (which is 01-31), BM (01-12), or BY (01-99). So when permuted, y_part is a two-digit string that is in 01-99. So the check that y is 01-99 is redundant. So in code, maybe we can skip that check. Because the original parts are valid, and permutation can't create a y_part outside of that.

Wait, no. For example, BM is a valid month (01-12). So when permuted to y_part, the maximum is 12. So y_part can be up to 12 (from BM), up to 31 (from BD), or up to 99 (from BY). So for BD's like 31 (which is a valid day for January), when permuted to y_part, it's 31. Which is allowed. So the birth year is 2031. So the check that 20y is >=2001 and <=2099 is automatically satisfied. Because 20y can be 2001 (y=01) to 2099 (y=99). So the code can skip checking that 20y is in 2001-2099. Because y_part is in 01-99. Wait, 20y_part is 20 followed by y_part. So y_part can be 01 (2001) to 99 (2099). So yes. So the code can skip checking this, as the input's BD, BM, BY are valid, and permutations of those parts would give y_part between 01 and 99.

Wait, wait. Suppose the birth date is 31.12.00. But according to the problem statement, the input BY is in 01-99. So the input can't have BY as 00. So for the input, BY is 01-99. But BD and BM can be 01-31 and 01-12, respectively. So when permuting, the y_part is BD, BM, or BY. All of which are >=01 and <=99 (since BD is at least 01, as it's a valid day; BM is at least 01 as a valid month; BY is 01-99). So y_part can't be 00. So the code can skip checking that y_part is between 01-99. So the first condition is automatically met.

Thus, the steps for each permutation are:

For permutation (d_part, m_part, y_part):

1. Check if (d_part, m_part) forms a valid day and month for the birth year (20y_part). Also, check that the month is valid (1-12).

So:

- m_int = int(m_part). If m_int not in 1-12 → invalid.

- d_int = int(d_part). Check if d_int is between 1 and max_days_for_month(m_int, 20y_part).

If either invalid → skip this permutation.

Else:

   compute the 18th birthday date.

So:

birth_year = 2000 + int(y_part)

new_year = birth_year + 18

new_month = m_int

new_day = d_int

Now, check if new_month is valid (since m_int is from the permutation's m_part, which could be BD or BM. Wait, but the permutation's m_part is from BD, BM, or BY. For example, if BD is 31, and m_part is BD (31), then m_int is 31, which is not a valid month (1-12). So this permutation would be invalid. So in code, step 1 (checking if m_int is 1-12) is necessary.

Ah, right. Because the permutation's m_part could be BD or BM or BY. BD is a valid day (but can be up to 31). So m_part can be BD (like 31), which is invalid as a month. So step 1 is necessary.

So, first, check that m_part is a valid month (1-12). Then, check that d_part is a valid day for that month and year.

So for example, if permutation is (31, 02, 80), then m_part is 02 (valid), but d_part is 31. For February (02), 31 is invalid. So this permutation is invalid.

So step 1: check that m_part is a valid month (1-12). If not, skip.

Else, proceed to check day.

So for each permutation:

m_int = int(m_part)

if m_int <1 or m_int >12 → invalid.

Else:

compute max_day for that month and year.

year = 2000 + int(y_part)

leap = (year %4 ==0) → since problem says for the years considered (2001-2099), leap years are those divisible by 4.

max_day = ... based on month and leap.

if d_int is between 1 and max_day → valid.

Else → invalid.

If valid, proceed.

Now, compute the adjusted date after adding 18 years.

new_year = year +18 → 20y_part +18.

new_month = m_int.

new_day = d_int.

Check if (new_day, new_month, new_year) is valid.

But new_year can be up to 2099 +18 = 2117, which is outside the problem's constraints, but during the 18th year addition, the new_year can be up to 2117. However, the finals date is in 20yy (2000 + yy, where yy is 01-99 → 2001-2099). So when adding 18 years, the new_year can be up to 2099 +18 = 2117, but the finals date is in 2001-2099. So the adjusted date's year could be 2019-2117.

But how does this affect the check?

For example, if the birth date is 2099-12-31 (year 2099), adding 18 years gives 2117-12-31. The finals date could be 2099-12-31. Then, the adjusted date (2117-12-31) is after the finals date (2099-12-31), so this permutation is invalid.

So in code:

We need to compute the adjusted date (new_day, new_month, new_year) and compare to the finals date.

But how to handle the adjusted date's validity.

For example, if new_month is 4 (April) and new_day is 31 → invalid. So adjust to 30.

So:

max_day_new = days_in_month(new_month, new_year)

adjusted_day = min(new_day, max_day_new)

adjusted_month = new_month

adjusted_year = new_year

Then, compare (adjusted_year, adjusted_month, adjusted_day) with finals_date_tuple.

So, code for this:

# compute max_day_new

if new_month ==2:

   leap_new = (new_year %4 ==0)

   if leap_new:

       max_day_new =29

   else:

       max_day_new =28

elif new_month in [4,6,9,11]:

   max_day_new =30

else:

   max_day_new=31

adjusted_day = min(new_day, max_day_new)

adjusted_date = (new_year, new_month, adjusted_day)

finals_date = (finals_year, finals_month, finals_day)

if adjusted_date <= finals_date:

   return True → this permutation is acceptable.

Now, the code steps:

Parse the input:

finals_line = input().strip().split('.') → [DD, MM, YY]

birth_line = input().strip().split('.') → [BD, BM, BY]

Then, for each permutation of [BD, BM, BY] (all 6 possible permutations):

For each permutation (d_part, m_part, y_part):

   # check if m_part is valid month

   m_int = int(m_part)

   if m_int <1 or m_int >12:

       continue

   # check if y_part is valid (we already know it's 01-99)

   # check day_part is valid for month m_int and year 20y_part

   year = 2000 + int(y_part)

   d_int = int(d_part)

   # compute leap for year

   leap = (year %4 ==0)

   if m_int ==2:

       max_day = 29 if leap else 28

   elif m_int in [4,6,9,11]:

       max_day =30

   else:

       max_day =31

   if d_int <1 or d_int > max_day:

       continue

   # Now, birth date is valid. Check adding 18 years.

   new_year = year +18

   new_month = m_int

   new_day = d_int

   # compute adjusted_day for new_month/new_year

   if new_month ==2:

       new_leap = (new_year %4 ==0)

       new_max_day = 29 if new_leap else 28

   elif new_month in [4,6,9,11]:

       new_max_day =30

   else:

       new_max_day =31

   adjusted_day = min(new_day, new_max_day)

   # adjusted date is (new_year, new_month, adjusted_day)

   # compare to finals_date

   finals_year = 2000 + int(finals_line[2])

   finals_month = int(finals_line[1])

   finals_day = int(finals_line[0])

   # create tuples for comparison

   adjusted_date = (new_year, new_month, adjusted_day)

   finals_date = (finals_year, finals_month, finals_day)

   if adjusted_date <= finals_date:

       print("YES")

       exit()

After checking all permutations, if none satisfy, output "NO".

So the code will generate all permutations of the birth parts, check each for validity, compute the adjusted date, and compare.

Now, generating all permutations. How to do this in Python.

The birth parts are a list of three elements. The permutations can be generated using itertools.permutations.

So:

from itertools import permutations

birth_parts = [BD, BM, BY]

for perm in permutations(birth_parts):

   d_part, m_part, y_part = perm

   proceed with checks.

Yes.

So code steps:

Read the two dates.

Split into parts.

Generate all permutations of birth_parts.

For each permutation, check if m_part is a valid month.

If not, skip.

Else, check if d_part is a valid day for that month and birth year.

If not, skip.

Else, compute the adjusted date after 18 years.

Compare to finals date.

If any permutation passes, output YES.

Else, output NO.

Now, considering the example inputs.

First example:

Input:

01.01.98 → finals_date is 01.01.2098 (year 2098)

birth date parts: 01, 01, 80 → permutations include (01, 01, 80) → birth date 01 Jan 2080. Adding 18 years → 2098-01-01. adjusted date is same as finals date. So 2098-01-01 <= 2098-01-01 → yes. So output YES.

Another example:

Input:

20.10.20 → finals date is 20 Oct 2020.

birth date parts: 10, 02, 30 → permutations include 30 as year. birth date would be 30 Feb (which is invalid). So any permutation where the month is 30 is invalid. So no valid permutations. Output NO.

Third example:

Input:

28.02.74 → finals date 28 Feb 2074.

birth date parts: 28,02,64 → permutations are 28,02,64 → birth date 28 Feb 2064. Adding 18 years: 2064 +18=2082. 28 Feb 2082 is valid. Compare to finals date 28 Feb 2074. 2082 is after 2074 → invalid. So no. So output NO.

So code should handle these.

Now, code in Python.

Need to read input, process permutations, check each.

But also, need to handle leading zeros. For example, parts like '01' must be parsed as 1.

So, for example, m_part is '01' → m_int is 1.

But in code, when we process the birth parts, they are strings. So when we generate permutations, the parts are strings.

But converting to integers is straightforward.

So code:

import sys
from itertools import permutations

def is_leap(year):
    return year %4 ==0

def main():
    # Read input
    finals = input().strip().split('.')
    birth = input().strip().split('.')
    # finals is DD.MM.YY → [dd, mm, yy]
    # birth is BD.BM.BY → [bd, bm, by]
    # Generate all permutations of birth parts
    for perm in permutations(birth):
        d_part, m_part, y_part = perm
        # Check month is valid
        try:
            m = int(m_part)
        except:
            continue
        if m <1 or m >12:
            continue
        # Check day is valid for month m and year 20y_part
        try:
            y = int(y_part)
            birth_year = 2000 + y
        except:
            continue
        try:
            d = int(d_part)
        except:
            continue
        # compute max_day for birth date
        if m ==2:
            max_day = 29 if is_leap(birth_year) else 28
        elif m in [4,6,9,11]:
            max_day =30
        else:
            max_day =31
        if d <1 or d> max_day:
            continue
        # Now, check 18 years later
        new_year = birth_year +18
        new_month = m
        new_day = d
        # compute adjusted_day
        if new_month ==2:
            new_max_day = 29 if is_leap(new_year) else 28
        elif new_month in [4,6,9,11]:
            new_max_day =30
        else:
            new_max_day=31
        adjusted_day = min(new_day, new_max_day)
        # finals date
        finals_dd, finals_mm, finals_yy = finals
        finals_year = 2000 + int(finals_yy)
        finals_month = int(finals_mm)
        finals_day = int(finals_dd)
        # compare dates
        adjusted_date = (new_year, new_month, adjusted_day)
        finals_date = (finals_year, finals_month, finals_day)
        if adjusted_date <= finals_date:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    main()

Hmm, this code should handle all cases. Let's test the first example.

Sample Input 1:

01.01.98 → finals date is 2098-01-01.

birth is 01.01.80 → permutations include (01, 01, 80). So birth year is 2080. Adding 18 → 2098. Birth date is 01 Jan 2080. 18 years later is 2098-01-01. adjusted date is same as finals date. So adjusted_date equals finals_date → YES.

Sample Input 2:

20.10.20 → finals date 2020-10-20.

birth parts 10,02,30. permutations include (30, 02, 10) → month is 02, day 30. For February, 30 days is invalid. So all permutations would either have invalid months or days. So output NO.

Sample Input 3:

28.02.74 → finals date 2074-02-28.

birth parts 28.02.64 → permutations (28, 02,64). birth date is 28 Feb 2064. Adding 18 → 2082. 28 Feb 2082 is valid. adjusted date is 2082-02-28. Which is after 2074-02-28. So no.

Thus, code should handle these correctly.

Another test case: if the birth date is 29.02.04 (year 2004, leap). Adding 18 years is 2022. 2022 is not a leap year, so adjusted day is 28. If finals date is 2022-02-28 → yes. If finals date is 2022-02-28 → equal → allowed.

So code should handle this.

Edge case: birth date is 29.02.04 (permuted). The code checks if 29 is a valid day for month 02 and year 2004. Yes (2004 is leap). Then, new_year is 2004+18=2022. new_month is 02. new_day is 29. Check if valid. 2022 is not leap, so adjusted_day is 28. So adjusted_date is 2022-02-28. If finals_date is 2022-02-28 → allowed.

So code will return YES.

Thus, the code should handle all possible permutations correctly.
</think>

```python
import sys
from itertools import permutations

def is_leap(year):
    return year % 4 == 0

def main():
    finals = sys.stdin.readline().strip().split('.')
    birth = sys.stdin.readline().strip().split('.')
    
    for perm in permutations(birth):
        d_part, m_part, y_part = perm
        
        try:
            m = int(m_part)
            if m < 1 or m > 12:
                continue
        except:
            continue
        
        try:
            y = int(y_part)
            birth_year = 2000 + y
        except:
            continue
        
        try:
            d = int(d_part)
        except:
            continue
        
        if m == 2:
            max_day = 29 if is_leap(birth_year) else 28
        elif m in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31
        
        if d < 1 or d > max_day:
            continue
        
        new_year = birth_year + 18
        new_month = m
        
        if new_month == 2:
            new_max_day = 29 if is_leap(new_year) else 28
        elif new_month in [4, 6, 9, 11]:
            new_max_day = 30
        else:
            new_max_day = 31
        adjusted_day = min(d, new_max_day)
        
        finals_year = 2000 + int(finals[2])
        finals_month = int(finals[1])
        finals_day = int(finals[0])
        
        if (new_year, new_month, adjusted_day) <= (finals_year, finals_month, finals_day):
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    main()
```