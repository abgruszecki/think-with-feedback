<think>
Okay, so I've got this programming problem to solve. Let's see what it's about. The problem says that given a number x with n digits, and a positive integer k less than n, we need to find the smallest beautiful integer y that's greater than or equal to x. A beautiful integer is one where each digit b_i is equal to b_{i+k} for all applicable i. 

Hmm. So the beautiful integer's structure is such that the digits repeat every k positions. Wait, not exactly every k. For example, if the beautiful number has m digits, then for each i from 1 to m-k, the i-th digit must equal the (i+k)-th. So the pattern is that the digits at positions i and i+k must be the same. So the structure is determined by the first k digits, and then the rest are copies. Or maybe not exactly. Let's think. Suppose k is 2. Then the first digit determines the third, fifth, etc. The second determines the fourth, sixth, etc. So the beautiful number has a period of k, but the digits are arranged in such a way. So for example, if the first two digits are '13', then the number would be 1313... etc. So the entire number is made by repeating the first k digits as necessary.

Wait, but the length of the beautiful number could be longer than k. For example, in the sample input 4 2, the output is 1313 which is exactly four digits, repeating the first two. So the first two digits are 13, then the third is 1 (same as first), fourth is 3 (same as second). So the length can be any as long as the pattern holds. But when we generate the minimal beautiful number y >= x, how do we approach this?

So the key idea is that the beautiful number's structure is determined by the first k digits. The rest of the digits are copies of the first k. So the beautiful number must consist of a prefix of k digits, and then the remaining digits are copies of the first k digits. For example, if the prefix is '12' and k=2, then the number is 121212... up to m digits, where m can be equal to or larger than k. But m must be such that when you take the first k digits, the rest follow the pattern. So the beautiful number is essentially the first k digits repeated as much as needed. Therefore, the entire number is built by taking the first k digits as a base and then extending them by repeating as needed. So if the original x has n digits, then the minimal y could either be the same length as x (if possible) or longer. But how?

The approach here would be to generate the candidate y by taking the first k digits of x, then extending them to form a beautiful number of length n. If that number is >=x, then that's the minimal. If not, then we need to increment the first k digits by 1 (with possible carryover) and then form the beautiful number. However, when we increment, the length might increase (like 999 becomes 1000). So in that case, the beautiful number would have length n+1, but wait, n is the original length. The problem allows y to have a larger m than n. For example, if x is 999 and k=1, then the beautiful number is 999 (since each digit must equal the next one when k=1). But if you can't find a number with the same length, maybe you have to go to the next possible length. But how?

So the steps are:

1. Check if the original x can be made into a beautiful number by taking the first k digits and repeating. If yes, return x.

2. If not, then we need to generate the next possible candidate by incrementing the first k digits. But when we increment, the first k digits may have a carryover that increases their length. For example, if the first k digits are 99, incrementing gives 100. Then the beautiful number would be 100100..., which has length k+1, but the original x was length n. So the minimal y might be longer than n in this case.

Wait, but how does the minimal y compare in length? If the first approach (using the original k digits) doesn't work, then the next candidate is the first k digits plus one. But when we do that, the length of the candidate could be the same (if there's no carryover) or increased by 1 (if there's a carryover). For example, if k is 2 and the first two digits are 99, then adding 1 gives 100, so the new k becomes 3? Wait, no. Wait, the beautiful number's first k digits are the base. So when we increment, the first k digits are modified. But if incrementing causes the number of digits to increase (like from 99 to 100), then the length of the beautiful number becomes m = k + (k) (like for k=2, 100100...). But wait, the problem states that k is a given value (for the original x). Wait, no. Wait, the beautiful number's k is fixed as the input k. Wait, no. Wait, the problem says that in the beautiful integer, b_i = b_{i+k} for each i where possible. So for the beautiful number, the same k is used as in the problem. So the structure is determined by the input k. So the first k digits of the beautiful number must be a base, and every digit after that is a copy of the digit k positions back.

So the length of the beautiful number can be any, but the structure must follow the input k, not a different k. So for example, if k is 2, the beautiful number's length can be 3 (like 121), but then the third digit must equal the first. So for the first k digits (digits 1 and 2), the third digit is 1 (same as first), but then there's no fourth digit. So in that case, the number is 121, which is acceptable.

But for the problem, when we are looking for the minimal y >=x, the minimal y could have the same length as x (if possible) or a longer length. For example, if x is 999 and k=1, the minimal beautiful y is 999 (same length). But if x is 999, k=2, then perhaps the minimal y is 999 (since each digit repeats every 2 positions. Wait, in that case, the third digit must equal the first. So 9 in position 1, 9 in position 3. Which is true. So 999 is beautiful for k=2. So that's possible. So in that case, the same length works.

So the approach is:

First, take the first k digits of the original x, and generate the minimal beautiful number by repeating these digits. Then check if this number is >= x. If yes, then return it. If not, then we need to generate the next candidate by incrementing the first k digits, then creating a beautiful number of possibly same or increased length.

But when you increment the first k digits, you may get a carryover. For example, if the first k digits are '99', incrementing gives '100', which has k+1 digits. Then, the beautiful number would be '100100...', but the length must be at least k +1? Or how?

Wait, the first k digits are the base. So if you increment them and the number becomes longer than k digits (like 999 becomes 1000 when k=3), then the beautiful number would have a base of 1000. Then, the next digits are copies from the first k digits. Wait, but if the new base is k+1 digits long, then how can the structure fit the original k? Because the original k is given as part of the input. For example, if the original k is 2, and the base after incrementing is 3 digits (like 100), then the beautiful number would have digits that are copies every 2 positions. So for example, 100100..., but then the third digit (0) must equal the first (1), which is not possible. So that's impossible. So how does incrementing the base work in such cases?

Wait, this suggests that when you increment the base (the first k digits), the resulting base must have exactly k digits. Otherwise, the structure of the beautiful number would not be possible. So perhaps the correct approach is to generate the base (the first k digits) as a k-digit number, possibly with leading zeros. Wait, but in the problem statement, the leading digit can't be zero. So the base must start with a non-zero digit.

So here's the problem: if the first k digits, when incremented, have a carryover that increases their length beyond k, then we can't use that as a base. For example, if k=2, and the base is 99. Incrementing gives 100. But 100 is 3 digits. So how can we form a base of k digits (which is 2 in this case) from that? It's impossible. So in such a case, the minimal y would have to have a base of k digits where the base is the minimal possible (like 10 for k=2?), but that's leading with a 1 followed by 0. Then the beautiful number would be 1010... but the original x could be 999, which would require a longer length. So in such a case, the minimal y would be of length k+1, but that's impossible because the base is k digits. Wait, maybe when the base is k digits, the minimal length is k, and any longer length is allowed as long as it follows the pattern.

Wait, no. The beautiful number's length can be any m >= k. Because the pattern must hold for all i where 1 <=i <= m -k. So for example, if the base is k digits, then the beautiful number can be exactly k digits (so no i's to check), or longer. But when it's longer, each digit after the k-th must equal the one k positions back.

So the key is that the base is the first k digits. So if the base after incrementing is a number with more than k digits, that's impossible. Therefore, in such a case, the minimal y must have a longer length than the original x. For example, if the original x is 999 (n=3) and k=2. Then, the base is 99. Incrementing gives 100, which is 3 digits. But since k=2, the base must be 2 digits. So 100 is invalid as a base. So the next possible base is 10 (since after 99, the next possible 2-digit number is 100, but that's 3 digits, so invalid). Wait, but that's not possible. So in this case, the minimal y must be 1001 (with m=4 digits). The base is 10, and the next two digits are 10. So the number is 1010. Wait, but then the third digit is 1 (must equal the first) and the fourth is 0 (must equal the second). So yes, 1010 is a beautiful number for k=2. So when the base is 10, the number is 1010... So in this case, for x=999 and k=2, the minimal y is 1010, which is larger than 999.

But in this scenario, the original x is 999. The base is 99, which gives 999 as the beautiful number, which is equal to x, so that's acceptable. Wait, but 99 is the base. Then the beautiful number is 999, which would have digits 9 (i=1), 9 (i=2), 9 (i=3). For i=1, i+k = 3, so 9 must equal 9. That's true. So 999 is a beautiful number for k=2. So why would the sample not consider that? Because maybe the original x is 999, which is beautiful. So the answer would be 999. 

Ah, right. So the problem comes when the base (the first k digits) is such that the generated beautiful number (by repeating) is >=x. If that's the case, we can just use that. Otherwise, we need to increment the base and generate a new beautiful number. But when incrementing the base, the base must remain a k-digit number. If it overflows (like 99 → 100), then the base is now longer than k digits, which is invalid. So in that case, the minimal possible base is 100...0 (with k zeros), which is 10...0 (k digits), which is 1 followed by k-1 zeros. Then, the beautiful number would be 100...0 repeated as necessary. For example, k=2, the base is 10, so the beautiful number is 1010... which is larger than any number with k digits (like 99) but requires a longer length.

Wait, but how do we handle the case where the base overflows when incremented? For example, if the base is 999 (k=3), then incrementing gives 1000 (4 digits). But the base must be k digits. So this is invalid. So in this case, the minimal y is the smallest possible beautiful number that has a base of k digits, which is 1000 (but that's 4 digits, which is not possible for k=3). Wait, no. For k=3, the base must be 3 digits. So if the original base is 999, then the next possible base is 1000, which is invalid. So we can't use that. So there's no possible 3-digit base larger than 999. So the only option is to create a base that is 1000...0 (k+1 digits?), but that's impossible. So in this case, the minimal y would have to be a base of 100 followed by 0 (for k=3), but that's 100, which is a 3-digit base. Wait, no. Wait, the base must be k digits, so 3 digits. So after 999, the next possible base is 1000, which is 4 digits, which is invalid. So there's no way to increment. So what's the solution here?

Ah, this is a problem. Because when the base is the maximum possible for k digits (like 999 for k=3), incrementing it would cause it to become 1000, which is invalid. So in this case, there's no possible base of k digits that's larger than the original. So the minimal y must be a beautiful number of length n + 1 digits, with a base of 100 (if k=3, for example) but how?

Wait, perhaps when the base is incremented and overflows, the minimal y is a beautiful number of length m = n+1, which has a base of 1 followed by k-1 zeros. Because that's the smallest possible base that can be formed. For example, if the original base is 999 (k=3), then the next possible base is 1000 (invalid), so we have to generate a base of 100 (k=3 digits?), but 100 is a 3-digit number. Then, the beautiful number would be 100100... So for m=3+1=4 digits, the number is 1001. Which is 1001. So this would be larger than 999. 

So the approach in such cases is to generate a new base of 1 followed by k-1 zeros, and then create a beautiful number of length m = max(n, k) + 1? Or perhaps m must be the minimal possible such that the beautiful number is at least x. 

So the algorithm would be:

1. Take the first k digits of x, call this base.

2. Generate the candidate y by repeating the base to form a number of length n digits. For example, if k=2, n=3, then the candidate is base[0], base[1], base[0].

3. If this candidate is >=x, then return it.

4. Otherwise, increment the base as a number, ensuring that it remains a k-digit number. If the increment causes an overflow (e.g., 999 → 1000 for k=3), then the new base is 100 (with leading 1 followed by zeros to make k digits?), but wait, 100 is 3 digits. So yes.

Wait, wait. When you increment the base, you must treat it as a k-digit number. So for example, if the original base is 99 (k=2), then incrementing gives 100, but that's 3 digits. But since we need a k-digit base, this is invalid. So in this case, the minimal possible solution is to create a base of 100...0 (k digits), which would be 10 for k=2. Then, the beautiful number would be 1010... which is 10 digits repeated. So for example, if the original x is 999 (n=3), then the candidate y would be 1010 (m=4), which is larger than 999.

But how to handle this in code?

So the steps are:

- First, check if the base (the first k digits) can be extended to a number of length n that is >= x. If yes, return that.

- If not, increment the base. But how?

Incrementing the base as a number. But we have to make sure that the base remains k digits. So if the base is '999' (k=3), incrementing would be 1000, which is 4 digits. So in this case, the next possible base is '100' (1 followed by k-1 zeros). Because 999 + 1 is 1000, which is longer than k digits. So the next possible base is the minimal possible, which is 100...0 (k digits), which is 10...0 (k digits). Then, the beautiful number would be this base followed by as many digits as needed to reach the minimal m where m is >=n. But wait, m can be n or m can be larger. For example, if n is 3 and k is 2, then the new base is 10 (k=2 digits). The beautiful number can be 101 (m=3), which is 10 followed by 1 (since m=3, the third digit must equal the first (1). So 101. But if x was 999, then 101 is smaller than 999, so this isn't acceptable. So in that case, we need a longer m. Wait, but 10 followed by 10 would be 1010 (m=4), which is larger than 999. So the minimal y is 1010.

But how to compute the minimal possible m?

Ah, the minimal possible m is the minimal possible such that the generated beautiful number has m digits and is >=x. But when the base is incremented, the generated beautiful number could have the same length as x (if possible) or a longer length.

So the algorithm is:

After incrementing the base, if the new base is still a k-digit number:

   generate the candidate y with length n. If that is >=x, return it. Otherwise, the minimal y must have length n+1, formed by the new base followed by the first (n+1 -k) digits of the base. For example, if the new base is 13 (k=2), and n=4, then the candidate is 1313. But if n=3, the candidate is 131 (digits 1,3,1). 

Wait, but when the new base is generated, and even if the candidate of length n is still smaller than x, then we need to generate a longer length. But how?

Alternatively, when the base is incremented (successfully, without overflow), the minimal candidate is to generate the beautiful number of length n. If that's not possible (because the generated number is still smaller than x), then we need to generate a number of length n+1. But how can that be?

Wait, perhaps when the base is incremented, the minimal beautiful number is formed by taking the new base and generating the number of length n. But if even that is not possible (due to the new base being larger than the original base, but when extended to n digits, it's still smaller than x), then the next option is to generate a longer number.

But that's getting complicated. Let's think of examples.

Sample input 2:

4 2

1234 → Output is 1313.

Original x is 1234, k=2. The first k digits are '12'. The beautiful number generated by '12' would be 1212 (since for n=4, it's 12 followed by 12). 1212 is less than 1234. So we need to increment the base.

Increment '12' to '13'. Now, the generated number is 1313. Which is 1313 >= 1234. So output that.

Another example: x is 999 (n=3), k=2. The base is 99. The beautiful number is 999. Which is equal to x. So output 999.

Another example: x is 999 (n=3), k=1. Then, the base is 9. The beautiful number must have all digits equal to 9. So 999 is valid. So output 999.

Another example: x is 100, k=1. The base is 1. The beautiful number is 111. Which is larger than 100. But wait, the original x is 100, and the minimal beautiful number is 100 (since all digits must be equal to the next one. Wait, for k=1, each digit must equal the next one. So 100 is not beautiful. The digits are 1,0,0. 1 != 0 (i=1, i+k=2). So the beautiful number must have all digits the same. So the minimal y would be 111.

So in this case, the base is 1. Then the generated number is 111 (length 3). Which is larger than x.

But let's see another example: x is 111, k=1. Then the beautiful number is 111. So output is 111.

Another example: x is 999, k=2. The base is 99. The beautiful number is 999. Which is equal to x. So output is 999.

But if x is 999, k=2. Let's say the base is 99. The beautiful number is 999. So correct.

Another example: x is 9999, k=3. The base is 999. The beautiful number is 9999 (since after 999, the next digit is 9 (position 4 must equal position 1). So 9999. Which is equal to x. So output is x.

So, the steps are:

Check if the base can generate a beautiful number of length n that is >=x. If yes, return it. Else, increment the base. If incrementing leads to a carryover that makes the base longer than k digits, then create a new base of 1 followed by k-1 zeros, and the beautiful number will be this new base followed by the necessary digits to reach m = k + (n -k) or something. Wait, perhaps in this case, the minimal possible beautiful number is 10...0 (k digits) followed by the first (m -k) digits of the base, where m is the minimal possible length such that the number is >=x. But when the original length is n, and the new base is 1 followed by k-1 zeros, the minimal possible m is k. But that's a shorter length than n. So in this case, perhaps the minimal m is the minimal between n and k+ something. Wait, no. For example, if the original x is 999 (n=3), and k=2, and the base is 99, which generates 999. If we have to increment the base, it becomes 100 (3 digits, which is invalid for k=2). So the new base is 10 (k=2 digits), and the minimal beautiful number is 1010 (m=4 digits), which is larger than 999.

So the algorithm must handle both cases: when the incremented base is a valid k-digit number, and when it's not (overflow). In the latter case, the minimal beautiful number is the base 100...0 (k digits), but when extended to form a beautiful number, which may be longer than n digits.

So, the steps are:

1. Check if the current base (first k digits) can form a beautiful number of length n that is >=x. If yes, return it.

2. Else, attempt to increment the base. If the base can be incremented (i.e., remains k digits after increment), then generate the beautiful number of length n and see if it's >=x. If yes, return it. If not, then the beautiful number must have length n+1, which is formed by the new base followed by the first (n+1 -k) digits of the base.

3. If the base cannot be incremented (overflow), then create the new base as 1 followed by (k-1) zeros. Then, the beautiful number is this base followed by the necessary digits, which will have a length of k + (k) = 2k digits? Or perhaps the minimal possible length is k+1 digits. Wait, no. The beautiful number can be any length >=k. So for the new base (10...0, k digits), the minimal possible beautiful number that is >=x is the minimal possible m, which could be k digits (10...0), but that's 100...0 with k digits, which is 10^k-1. But if x is 999 (n=3) and k=2, then 10...0 is 10 (k=2 digits), and the minimal beautiful number is 1010 (m=4 digits). So in this case, m is n+1.

So the approach when the base increment overflows is:

Create a new base of 1 followed by k-1 zeros. Then, the minimal beautiful number would be this base followed by the first (n -k) digits of the base. But since the new base's length is k, and the original n may be larger than k, perhaps the generated number must have a length of m = n, but the new base's length is k. Wait, but when we form a beautiful number of length n using the new base, it's possible. For example, k=2, new base is 10. Then for n=4, the beautiful number is 1010. For n=3, it's 101. So in this case, if the original x is 999 (n=3), then the new base's beautiful number of length 3 is 101, which is 101 < 999. So we need to create a longer beautiful number. So the minimal m is 4, which is 1010.

So, when the base is incremented and overflows, the new base is 10...0 (k digits), and the beautiful number is formed by repeating this base enough times to reach a length of m digits where m is the minimal possible such that the number is >=x. But how to compute m?

Alternatively, when the base is 10...0 (k digits), the beautiful number can be formed by repeating the base as many times as needed. So the minimal possible beautiful number in this case is the base followed by the first (m -k) digits of the base. For m >=k. But the minimal m must be such that the beautiful number is >=x.

But how to compute that?

In this case, the beautiful number will be the minimal possible, which is the base repeated enough times to be at least x. Since the new base is 10...0, the generated number will be 10...0 repeated, which is 10...010...0 etc. So this is the minimal possible beautiful number after overflow. And it's possible that this is the smallest possible, but how to compute the required length.

But perhaps when overflow occurs, the minimal possible beautiful number is the base (10...0) followed by the base again, forming a 2k-digit number, which is 10...010...0. Then, if that is not sufficient, perhaps longer lengths. But this approach could be expensive for large n. But given that n can be up to 2e5, we need an efficient way to generate the beautiful number.

But how to compare the beautiful numbers with x.

Alternatively, when the base is 10...0, the beautiful number's digits are all the same as the base's digits. So for example, for k=2, the base is 10. The beautiful number is 1010... for even length, 101 for length 3. The minimal beautiful number here would be 10 followed by 1 (for length 3) which is 101. But if x is 999, then 101 is not enough, so the next possible is 1010 (length 4), which is 1010. So the minimal m is the smallest m >= len(x) such that the beautiful number of length m is >=x. But how to compute that.

Alternatively, when the overflow occurs, the minimal possible beautiful number is the new base followed by enough digits to make it at least as long as x. If x has length n, then the minimal m is the smallest possible m >=n such that the beautiful number of length m is >=x. But the minimal m could be n or n+1. Wait, no. For example, x is 999 (n=3), the new base is 10. The beautiful numbers of length 3 and 4 are 101 and 1010. 101 is smaller than 999, 1010 is larger. So m is 4.

So the minimal m when overflow occurs is the smallest m where m >=n and the beautiful number of length m is >=x. But how to compute this m.

But given that the beautiful number is formed by the base (10...0) followed by the first (m -k) digits of the base. So the beautiful number is the base's digits repeated as necessary. So the number is the base repeated m//k times, and then the first (m mod k) digits of the base.

But for the case when the base is 10...0, the generated beautiful number will be 10...0 followed by 10...0 and so on, which is the base repeated. So the minimal possible m is the minimal m such that the beautiful number is >=x and m >=n.

But how to find m in this case?

Wait, since the beautiful number formed by the new base (10...0) is the smallest possible when the overflow occurs (since the base is the smallest possible after incrementing), perhaps the minimal m is the minimal possible length that is >=n and such that the beautiful number of that length is >=x. If the beautiful number of length n is larger than x, then m is n. Otherwise, m is n+1, and so on. But how to compute this efficiently.

But when the base is 10...0, the beautiful number of length m is the base repeated ceil(m/k) times. For example, k=2, base 10. For m=3, it's 10 1 → 101. For m=4, it's 10 10 → 1010. For m=5, 10 10 1 → 10101. But this may not be the case. Wait, no. For a beautiful number of length m, the first k digits are the base, then each subsequent digit is equal to the one k positions back. So for the base 10 (k=2), the digits are:

1, 0, 1, 0, 1, 0, etc. So the beautiful number is 101010... So for any m >=k, the digits are the base's digits repeated. So for m=3, the digits are 101. For m=4, 1010. For m=5, 10101, etc.

So the beautiful number is formed by taking the first k digits as the base, and then each digit after that is equal to the digit k positions earlier. So in this case, the beautiful number is a repetition of the base as much as possible.

So the beautiful number for the new base (10...0) is the base repeated as necessary. So the number is 10...010...010..., etc. So the minimal m where this number is >=x can be computed as follows:

If the base's length is k, then the beautiful number of length n is the first n digits of the base repeated. So the minimal m is the smallest m >=n such that the beautiful number of length m is >=x. But even this may not be sufficient. For example, if x is 9999 (n=4), and the base is 10 (k=2), the beautiful number of length 4 is 1010, which is 1010 <9999. So the minimal m is 5, which gives 10101, but that's 10101 which is still less than 9999. Wait, no. 10101 is 10 thousand and 101, which is larger than 9999. So in this case, the beautiful number of length 5 is 10101, which is 10101, which is larger than 9999. So m=5.

So in this case, when the base is 10, the minimal m is 5.

But how to compute this m efficiently.

Alternatively, the beautiful number after overflow is the smallest possible which is the new base followed by as many digits as needed to make it larger than x. But the new base is 10...0, which is the smallest possible k-digit number. So the minimal beautiful number in this case is the new base followed by its digits as necessary. So the beautiful number is 10...0 repeated enough times to have m digits, where m is the minimal possible such that the number is >=x.

So the algorithm would be:

If the base can be incremented (without overflow):

   generate the new base.

   check if the new base's beautiful number of length n is >=x. If yes, return it.

   else, return the new base's beautiful number of length n+1.

Else:

   generate the new base as 1 followed by k-1 zeros.

   generate the minimal m >=n such that the beautiful number of length m is >=x.

But how to compute this m.

Wait, the beautiful number for the new base is always the same pattern. For example, new base is 10 (k=2). The beautiful numbers are 10, 101, 1010, 10101, etc. Each step adds one digit, which is the same as the digit two positions back.

So the numbers increase with m. For example, 10 is 10, 101 is 101, 1010 is 1010, etc. So the longer the m, the larger the number. So the minimal m is the minimal m >=n such that the beautiful number of length m is >=x.

But how to compute this quickly.

But the beautiful number's digits for the new base can be generated as follows:

The first k digits are the base (10...0), and each subsequent digit is the same as the one k positions before. So the entire beautiful number is the base repeated as needed. For example, base 10 (k=2), the number for any m is the base concatenated floor(m/k) times, plus the first m%k digits of the base.

Wait, no. For m=3, the digits are 1,0,1 (base is 10, then third digit is first digit of base). For m=4, 1,0,1,0 (base repeated twice). For m=5, 1,0,1,0,1. So the pattern is base repeated as many times as needed, and the digits are the first m digits of that infinite repetition.

So to generate the beautiful number for the new base, it's the first m digits of the infinite repetition of the base.

So when the base is 10...0 (k digits), the beautiful number of length m is the first m digits of the base repeated infinitely.

So for example, base is '100' (k=3), the beautiful numbers are:

m=3: 100

m=4: 1001 (since the fourth digit is the first digit of the base)

m=5: 10010 (fifth digit is the second digit of the base)

m=6: 100100 (third digit of base is 0)

So when m is larger than k, the digits are determined by the base's digits in a cyclic manner.

So to compute the minimal m where this beautiful number is >=x, we can compare the beautiful number for m = n and m = n+1, etc. But for large n (up to 2e5), generating the entire digits for each m would be time-consuming.

But perhaps the minimal m is n or n+1. Let's see:

Take x=999 (n=3), k=2. The new base is 10. The beautiful number for m=3 is 101, which is 101 <999. The next m is 4: 1010 (1010 >=999). So m=4.

Another example: x is 9999 (n=4), k=2. New base is 10. Beautiful number for m=4 is 1010 <9999. So m=5: 10101 (5 digits) which is 10101 >=9999.

Another example: x is 10100 (n=5), k=2. New base is 10. Beautiful number for m=5 is 10101 → 10101 <10100? No. 10101 is larger than 10100. So m=5 is sufficient.

So, the minimal m is the smallest m >=n such that the beautiful number of length m is >=x. Since the beautiful number increases with m, the first possible m that satisfies this is the answer. So how to find m?

But generating the beautiful number for m >=n could be time-consuming for very large n. So we need an efficient way to compare the beautiful number with x.

But how? Because the beautiful number for m >=n has digits that are the base's digits repeated. So for example, for the new base (k digits), the beautiful number's first n digits are the base followed by the first (n -k) digits of the base.

Wait, for example, base is 10 (k=2), n=4. The beautiful number is 1010. Which is base (10) followed by base again (10). For n=5, it's 10101 (10 10 1).

So for m >=k, the beautiful number is the base repeated (m // k) times, plus the first (m % k) digits of the base.

So for the new base, the beautiful number of length m is the concatenation of the base (k digits) as many times as possible, and then the first (m mod k) digits of the base.

But since the new base is 10...0 (k digits), this means that the beautiful number is 1 followed by (k-1) zeros, then 1, followed by (k-1) zeros, etc. So for any m, the digits alternate between 1 and 0 in the first position of each k-block.

So for example, when k=3, the base is 100. The beautiful number for m=4 is 1001, for m=5 is 10010, for m=6 is 100100, etc.

So how to compare this beautiful number with x, which is a given digit string of length n.

But since the new base's beautiful number is the smallest possible after overflow, perhaps the minimal m is either n or n + (k - (n % k)), but this is just a guess.

Alternatively, since the beautiful number for the new base is the smallest possible for each m, the minimal m is the smallest m >=n such that the beautiful number is >=x.

So to compute this, we can generate the beautiful number of length n. If it's >=x, then m=n. Else, generate for m = n +1, and so on. But for large n (like 2e5), this approach is not feasible.

But we can compare the beautiful number's digits with x's digits, but in an efficient way.

Let's think: for the new base's beautiful number, the first k digits are 10...0. Then, the next digits are the same as the first digits. So the beautiful number is a repetition of the base's digits. So the digits are:

base[0], base[1], ..., base[k-1], base[0], base[1], ..., base[k-1], etc.

So for any position i (0-based), the digit is base[i % k].

So the beautiful number's digit at position i is base[i mod k].

So to compare the beautiful number of length m with x:

- If m <n: impossible, since m must be >=n.

Wait, no. Because the problem says that y must be >=x, but y can have m digits larger than n. For example, if x is 999 (3 digits), m can be 4, which is larger than n.

So the beautiful number for the new base has m digits, where m is >=n.

So the steps would be:

1. Compute the minimal m where m >=n and the beautiful number of m digits (based on new base) is >=x.

2. Compare the beautiful number of length m digits with x.

But how to compute this comparison efficiently.

But the x has length n. The beautiful number has length m. So if m >n, then the beautiful number is larger (since it has more digits). So the minimal m is either n (if the beautiful number of length n is >=x) or n+1 (since for m>n, the beautiful number is larger than x).

But wait, no. For example, x is 999 (n=3), and the beautiful number of m=4 digits is 1010, which is 1010 >=999, so m=4 is sufficient. But the beautiful number of length 4 digits is larger than x (since it's 4 digits, which is more than 3). So if m >n, then the beautiful number is larger than x, regardless of its digits. Because any number with more digits is larger than a number with fewer digits.

Ah! So if m >n, then the beautiful number is automatically >=x. So the minimal possible m is either:

a) n, if the beautiful number of length n is >=x.

b) n+1, otherwise.

Because for m =n+1, the beautiful number has more digits than x, thus it's larger.

So, in the case where the base is 10...0 (after overflow), the minimal m is either n (if the beautiful number of length n is >=x) or n+1.

But wait, what if x has n digits and the beautiful number of m =n digits is less than x, but m =n+1 digits is larger than x (since it has more digits). Then the minimal m is n+1.

So the algorithm for the overflow case is:

Generate the beautiful number of length n. If it's >=x, return it. Else, return the beautiful number of length n+1.

But how to generate the beautiful number for length n and compare with x.

But generating the entire beautiful number for length n (which can be up to 2e5 digits) is feasible? Well, in Python, strings are handled efficiently, but we need to generate the beautiful number's digits and compare them with x's digits.

But comparing two large numbers as strings can be done digit by digit.

So the steps are:

For the overflow case:

1. Create the new base as '1' followed by '0's to make k digits.

2. Generate the beautiful number of length n.

   This is done by repeating the base's digits as needed. So for each position i in 0..n-1, the digit is base[i % k].

   So, for example, base is '10' (k=2), n=3: digits are 1,0,1.

3. Compare this generated number (length n) with x.

   If it's >=x, then return it with m =n.

4. Else, generate the beautiful number of length n+1, which will automatically be larger than x (since it's one digit longer).

So for the overflow case, the minimal m is either n or n+1.

So the algorithm becomes:

After the overflow:

   Generate candidate of length n. If >=x → return.

   Else, return candidate of length n+1.

This is efficient, as generating the candidate for length n is O(n) time.

So, putting all together:

The algorithm is:

1. Extract the first k digits of x as the initial base.

2. Generate the beautiful number of length n using this base. Let's call this candidate 'current'.

   Compare 'current' with x. If current >=x, return it.

3. Else, increment the base. Check if the incremented base has k digits.

   a. If yes:

      Generate the candidate of length n. Compare with x. If >=x, return.

      Else, generate the candidate of length n+1. Return.

   b. If no (overflow):

      Generate the new base as '1' followed by (k-1) zeros.

      Generate candidate of length n. Compare with x. If >=x, return.

      Else, generate candidate of length n+1. Return.

But wait, in case 3a, after incrementing the base and generating the candidate of length n, if it is still less than x, then the minimal candidate is of length n+1. But how can that be? Because the base has been incremented, the candidate of length n is the new base's beautiful number. For example, original base is 12 (k=2), increment to 13. Generate candidate 1313 (for n=4). If x is 1314, then the candidate is 1313 <1314. So the minimal candidate would be 1313, but it's less than x. So in this case, the next candidate would be 13131 (n+1=5 digits). Which is larger than x. So for this case, the algorithm must generate the candidate of length n+1.

But wait, the minimal y must be the smallest possible. So in this scenario, the base is 13, and the beautiful number of length 4 is 1313 <1314. Then the beautiful number of length 5 is 13131 (5 digits), which is larger than 1314. So the answer is 13131.

So the algorithm in case 3a would generate the beautiful number of length n, and if that's not sufficient, generate length n+1.

So the steps for case 3a are:

- After incrementing the base (now valid k digits):

   generate candidate of length n.

   if >=x → return.

   else → generate candidate of length n+1, return.

So now, the code steps are:

Implement the following:

- Generate current candidate from base.

- Check if >=x. If yes, output.

- Else, increment base. Handle overflow.

So, in code:

We need to handle the initial base, then the incremented base.

But how to handle the increment? For example, the base is a string of digits. We need to increment it as a number, ensuring that it remains a k-digit number. If incrementing causes it to overflow (i.e., becomes k+1 digits), then handle the overflow case.

So, the code steps:

1. Read n, k.

2. Read the digits of x as a list.

3. Extract the initial base: first k digits.

4. Generate the candidate y by repeating the base's digits to form a number of length n.

   Compare y with x. If y >=x, output.

5. Else:

   a. Attempt to increment the base.

   b. If the increment succeeds (base remains k digits):

      i. Generate candidate of length n. If >=x, output.

      ii. Else, generate candidate of length n+1. Output.

   c. Else (increment leads to overflow):

      i. Create new base as '1' followed by (k-1) zeros.

      ii. Generate candidate of length n. Compare with x. If >=x, output.

      iii. Else, generate candidate of length n+1. Output.

But how to increment the base as a string, considering that leading zeros are not allowed (since the first digit of the base must be non-zero).

So, the code for incrementing the base:

We can treat the base as a string of digits. To increment it as a number, we can parse it as an integer, add 1, and then format it back as a string with leading zeros to make k digits. But for very large k (up to 2e5), this is impossible, as converting to integer is not feasible.

Wait, but the base can be up to 2e5 digits. So we can't treat it as an integer. So we need to handle the increment as a string.

Handling the increment as a string:

We start from the end of the string and increment each digit, handling carry.

For example:

Base is '999'. Increment:

Start at index 2: 9 → 0, carry 1.

Index 1: 9 + 1 → 0, carry 1.

Index 0: 9 + 1 → 0, carry 1.

Now, we have carry 1. So the new number is '1000', which is k+1 digits. So overflow.

So the code must handle this.

So the algorithm for incrementing the base string:

1. Convert the base string into a list of characters for easy manipulation.

2. Start from the end (index k-1) and move left.

3. For each digit, add 1. If the digit becomes 10, set to 0 and carry 1. Else, carry is 0.

4. If after processing all digits, there is a carry, then the new base has k+1 digits → overflow.

5. Else, the new base is the modified digits.

But in the code, the base must have exactly k digits. So if incrementing leads to a carryover, the new base has k+1 digits and is invalid.

So in code:

def increment_base(base):

    carry = 1

    digits = list(base)

    for i in range(len(digits)-1, -1, -1):

        d = int(digits[i]) + carry

        if d == 10:

            digits[i] = '0'

            carry = 1

        else:

            digits[i] = str(d)

            carry = 0

            break  # no more carry

    if carry == 1:

        return None  # overflow

    return ''.join(digits)

Wait, but this code only increments the digits once, and stops once there's no carry. Because after adding 1 to the current digit and no carry, we break.

Yes, because incrementing by 1 only requires adding once.

So, for example:

base = '1234'

increment: 1235.

base = '1999'

increment: 2000.

But if the base is '999', incrementing would carry all the way. After processing all digits, carry is 1. So returns None, indicating overflow.

So in code, after incrementing, if the new base has k digits, return it. Else, return None.

So this function handles the incrementing.

So, in the code:

After step 4, if the initial candidate is not sufficient, we need to increment the base.

If the increment is possible (returns a new base), then generate the new candidate of length n. Compare with x. If sufficient, output. Else, output the new candidate of length n+1.

If increment is not possible (returns None), then create the new base as '1' followed by k-1 '0's. Then generate candidate of length n. Compare. If sufficient, output. Else, generate candidate of length n+1.

Now, the problem is to generate the candidate numbers (as strings) for comparison.

Generating the candidate for a given base and m:

def generate_candidate(base, m):

    # base is a string of length k.

    # m is the desired length of the candidate.

    k = len(base)

    res = []

    for i in range(m):

        res.append(base[i % k])

    return ''.join(res)

Yes. Because for each position i in 0..m-1, the digit is base[i %k].

So for example, base '10', m=4 → '1010'.

Now, comparing two numbers represented as strings.

Comparing two digit strings a and b:

If len(a) > len(b): a is larger.

If len(a) < len(b): a is smaller.

Else: compare digit by digit from left to right.

So:

def is_greater_or_equal(a_digits, b_digits):

    if len(a_digits) != len(b_digits):

        return len(a_digits) > len(b_digits)

    for a, b in zip(a_digits, b_digits):

        if a > b:

            return True

        elif a < b:

            return False

    return True  # equal

So, in code:

original_x = input_digits (list of strings)

base_candidate = generate_candidate(base, len(original_x))

if is_greater_or_equal(base_candidate, original_x):

    output this candidate.

Else:

 proceed.

So, putting it all together.

Now, handling the code.

But given that n can be up to 2e5, the code must be efficient.

In Python, generating the candidate for m=2e5 can be done efficiently with list comprehensions or string operations.

But the code must read the input, process, and output the results without any delays.

So, the code steps:

Read n, k.

Read the digits of x as a string.

Extract the initial base: first k digits.

Generate the candidate for m =n.

Compare with x.

If yes, output.

Else:

 increment the base.

 if increment is possible (returns new_base):

   generate candidate for m =n. Compare with x.

   if yes → output.

   else:

     generate candidate for m =n+1. Output.

 else:

   new_base is '1' followed by (k-1) '0's.

   generate candidate for m =n. Compare with x.

   if yes → output.

   else:

     generate candidate for m =n+1. Output.

So, code steps:

Now, the code.

First, read input:

n, k = map(int, input().split())

x = list(input().strip())

Then, extract the initial base:

base = x[:k]

Generate candidate:

candidate = generate_candidate(base, n)

if candidate >= x:

   output.

Else:

   try to increment the base.

So, code for increment:

def increment_base(base):

    # returns None if overflow, else new base.

    digits = list(base)

    carry = 1

    for i in range(len(digits)-1, -1, -1):

        new_d = int(digits[i]) + carry

        if new_d >= 10:

            digits[i] = '0'

            carry = 1

        else:

            digits[i] = str(new_d)

            carry = 0

            break

    if carry == 1:

        return None

    return digits

Wait, the base is a list of characters (from x[:k]). So the code for increment_base takes a list of characters, not a string.

Wait, in the code:

base is initially x[:k], which is a list of characters. So when we increment, we process this list.

So, modifying the code:

def increment_base(digits):

    # digits is a list of characters.

    # returns new digits as list, or None if overflow.

    carry = 1

    for i in range(len(digits)-1, -1, -1):

        new_d = int(digits[i]) + carry

        if new_d >= 10:

            digits[i] = '0'

            carry = 1

        else:

            digits[i] = str(new_d)

            carry = 0

            break

    if carry == 1:

        return None

    return digits

So, initial base is base = x[:k].

Then:

new_base = increment_base(base.copy())

If new_base is not None:

   candidate = generate_candidate(new_base, n)

   if candidate >=x:

      output.

   else:

      candidate = generate_candidate(new_base, n+1)

      output.

Else:

   new_base is '1' + '0'*(k-1)

   candidate = generate_candidate(new_base, n)

   if candidate >=x:

      output.

   else:

      candidate = generate_candidate(new_base, n+1)

      output.

So, the code for the increment_base function and generating candidates.

Now, the code for generate_candidate:

def generate_candidate(base, m):

    # base is a list of characters, length k.

    # returns the candidate digits as a list.

    k = len(base)

    return [base[i % k] for i in range(m)]

But since in Python, lists are zero-based, and the problem's digits are 1-based, but the code uses zero-based indices.

So for example, base is ['1', '0'], k=2. For m=3, the candidate is ['1', '0', '1'].

Now, comparing the candidates with x.

The x is a list of characters.

The function to compare two digit lists:

def is_ge(a, b):

    # compare a and b as digit lists.

    if len(a) != len(b):

        return len(a) > len(b)

    for ai, bi in zip(a, b):

        if ai > bi:

            return True

        elif ai < bi:

            return False

    return True

So, in code:

current_candidate = generate_candidate(base, n)

if is_ge(current_candidate, x):

   output.

Else:

 proceed.

So, putting it all together.

Now, code:

n, k = map(int, input().split())

x = list(input().strip())

base = x[:k]

def generate_candidate(base, m):

    k = len(base)

    return [base[i % k] for i in range(m)]

def is_ge(a, b):

    if len(a) != len(b):

        return len(a) > len(b)

    for ai, bi in zip(a, b):

        if ai > bi:

            return True

        elif ai < bi:

            return False

    return True

current = generate_candidate(base, n)

if is_ge(current, x):

    print(n)

    print(''.join(current))

else:

    # Increment base

    def increment_base(digits):

        carry = 1

        for i in reversed(range(len(digits))):

            new_d = int(digits[i]) + carry

            if new_d >= 10:

                digits[i] = '0'

                carry = 1

            else:

                digits[i] = str(new_d)

                carry = 0

                break

        if carry == 1:

            return None

        return digits

    new_base = increment_base(base.copy())

    if new_base is not None:

        candidate = generate_candidate(new_base, n)

        if is_ge(candidate, x):

            print(n)

            print(''.join(candidate))

        else:

            # Generate candidate of n+1 digits

            candidate = generate_candidate(new_base, n+1)

            print(n+1)

            print(''.join(candidate))

    else:

        # Overflow, create new_base as '1' followed by k-1 zeros.

        new_base = ['1'] + ['0']*(k-1)

        candidate = generate_candidate(new_base, n)

        if is_ge(candidate, x):

            print(n)

            print(''.join(candidate))

        else:

            # Generate candidate of n+1 digits

            candidate = generate_candidate(new_base, n+1)

            print(n+1)

            print(''.join(candidate))

But wait, when generating the new_base in the overflow case, the new_base is ['1'] followed by k-1 '0's. So for example, k=2 → ['1', '0'], which is correct.

But when generating the candidate for m= n+1, the length increases by one.

This code should handle all cases.

Let's test the sample inputs.

Sample 1:

Input:

3 2

353

base is ['3','5'].

Generate candidate of length 3: 3,5,3 → 353. Compare with x, which is 353. Equal. So output.

Sample 2:

Input:

4 2

1234

base is ['1','2']. candidate is '1212' → 1212 <1234. So increment base.

Increment ['1','2']:

start from index 1: 2 +1 → 3. carry 0.

new_base is ['1','3'].

generate candidate of 4 digits: 1,3,1,3 → 1313. Compare to 1234 → yes. So output.

Another test case where increment leads to overflow.

For example, x is 999, k=2, n=3.

Initial base is ['9','9']. candidate is 999 → equal to x. So output.

Another test case where initial base is 99, n=3, k=2. x is 999. candidate is 999, which is equal. So output.

Another case where x is 999, k=2, n=3. Then initial candidate is 999. So output.

Another test case where increment leads to overflow. For example, x is 999, k=2, n=3.

Wait, but the initial base is ['9','9'], candidate is 999. So output.

Now, if x is 9999, k=3, and the initial base is 999. Candidate is 9999 → equal. Output.

Now, if x is 9999, k=3, and the initial base is 999. candidate is 9999. Output.

Another case where increment leads to overflow:

x is 999, k=2, n=3. Then base is 99 → candidate is 999. equal. So output.

If x is 999, k=2, but the base is 99. Then output is 999.

Another example where the base is 99, x is 990. Then candidate is 999, which is larger. So output.

But in code, the candidate is generated correctly.

So, the code seems to handle all cases.

Now, for the overflow case: base is 999 (k=3), increment leads to overflow. New base is 100.

Generate candidate of length n (3) → 100. Wait, no. For k=3, new base is 100. The candidate of length 3 is 100. So if x is 999, the candidate 100 is 100 <999. So generate candidate of length 4: 1001. But 1001 is 4 digits, which is larger than x's 3 digits. So output is 1001.

So code would output 1001 as the candidate of length 4.

Thus, the code should be correct.
</think>

```python
n, k = map(int, input().split())
x = list(input().strip())
base = x[:k]

def generate_candidate(base, m):
    k = len(base)
    return [base[i % k] for i in range(m)]

def is_ge(a, b):
    if len(a) != len(b):
        return len(a) > len(b)
    for ai, bi in zip(a, b):
        if ai > bi:
            return True
        elif ai < bi:
            return False
    return True

current = generate_candidate(base, n)
if is_ge(current, x):
    print(n)
    print(''.join(current))
else:
    def increment_base(digits):
        carry = 1
        copied = digits.copy()
        for i in reversed(range(len(copied))):
            new_d = int(copied[i]) + carry
            if new_d >= 10:
                copied[i] = '0'
                carry = 1
            else:
                copied[i] = str(new_d)
                carry = 0
                break
        return copied if carry == 0 else None

    new_base = increment_base(base)
    if new_base is not None:
        candidate = generate_candidate(new_base, n)
        if is_ge(candidate, x):
            print(n)
            print(''.join(candidate))
        else:
            candidate = generate_candidate(new_base, n+1)
            print(n+1)
            print(''.join(candidate))
    else:
        new_base = ['1'] + ['0'] * (k-1)
        candidate = generate_candidate(new_base, n)
        if is_ge(candidate, x):
            print(n)
            print(''.join(candidate))
        else:
            candidate = generate_candidate(new_base, n+1)
            print(n+1)
            print(''.join(candidate))
```