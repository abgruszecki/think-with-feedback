<think>
Okay, let's see. I have to expand a polynomial given as factors of (x + a_i) into its standard form. Then output each term properly, omitting unnecessary parts. The constraints are n up to 9. Hmm, even with n=9, the number of terms in the expansion is manageable, since for each multiplication step, the coefficients can be tracked.

First, I need to model how the coefficients are computed. The product of (x + a1)(x + a2)...(x + an) will result in a polynomial where each coefficient corresponds to the sum of products of subsets of the a_i's. For example, the coefficient of x^(n-1) is the sum of all a_i's, the coefficient of x^(n-2) is the sum of all products of two distinct a_i's, and so on, down to the constant term, which is the product of all a_i's.

So the approach is to compute these coefficients step by step. Start with the initial factor (x + a1), then multiply each subsequent (x + a_i), updating the coefficients each time.

The way to model this is using dynamic programming. Let's represent the coefficients as a list where the index represents the degree. For example, after multiplying k factors, the list coeffs will have coefficients from x^k down to x^0. Initially, with one factor (x + a1), the coefficients are [1 (for x^1), a1 (for x^0)].

Then, for each subsequent a_i, we multiply the current polynomial by (x + a_i). The new polynomial's coefficients can be computed as follows: for each term x^{k} in the current polynomial, multiplying by x gives x^{k+1} (so the coefficient for x^{k+1} is the same as the current x^k's coefficient), and multiplying by a_i gives a coefficient for x^k (current x^k's coefficient * a_i). So, when adding a new a_i, the new coefficients are formed by shifting the current coefficients (adding a new leading 1 for x^{current degree + 1}) and adding a_i multiplied by each coefficient. Wait, no. Wait, the existing polynomial is of degree m. Multiplying by (x + a) gives a polynomial of degree m+1. The new coefficients can be computed as:

new_coeffs[0] = 1 (since x^(m+1) is the leading term from x * x^m)
Wait, no. Wait, maybe not. Let's think again. Suppose we have a polynomial P(x) = c0 x^m + c1 x^{m-1} + ... + cm. Then, multiplying by (x + a) gives:

P(x) * x = c0 x^{m+1} + c1 x^m + ... + cm x
plus P(x) * a = a c0 x^m + a c1 x^{m-1} + ... + a cm.

So combining these, the new coefficients would be:

For x^{m+1}: c0 (from x term)
For x^m: c1 (from x term) + a c0 (from a term)
...
For x^1: cm (from x term) + a cm-1 (from a term)
For x^0: a cm (from a term)

Wait, no. Let's model this step by step.

Let's say the current polynomial is represented as a list where coeffs[i] is the coefficient for x^{m - i}, where m is the degree. Hmm, maybe not the best way. Alternatively, let's have a list where coeffs[k] is the coefficient of x^k. So for a degree m polynomial, coeffs has length m+1, with indices from 0 (x^0) up to m (x^m). Wait, no. Wait, perhaps it's easier to have the list reversed. For example, for (x + a1), the coefficients are [a1, 1], where index 0 is the x^0 term (a1) and index 1 is x^1. Then, when multiplying by (x + a_i), we need to compute the new coefficients. Let me think.

Wait, let's take an example. Suppose we have (x + a) * (x + b) = x² + (a + b)x + ab. The coefficients for x², x^1, x^0 are 1, a+b, ab. So in a list, [1, a+b, ab], but the index would correspond to the degree. So coeffs[0] is the x^0 term? Or the other way around. Maybe it's better to have coeffs[degree] as the coefficient of x^degree. So in this example, coeffs[2] = 1, coeffs[1] = a+b, coeffs[0] = ab. Wait, no, that's not right. For x² + (a+b)x + ab, the coefficients are: x² term is 1 (degree 2), x term is a+b (degree 1), constant term is ab (degree 0). So the list would be [ab, a+b, 1], with indices 0, 1, 2 corresponding to degrees 0, 1, 2. Wait, no. Let's say coeffs is a list where coeffs[k] is the coefficient of x^k. So for x², the list would be [ab, a+b, 1], since x² has degree 2, and the list is index 2. Wait, no. For example, in code, perhaps the list is ordered from x^0 up to x^n. So for a polynomial of degree m, the list is of length m+1. So for (x + a), the list is [a, 1]. For (x +a)(x +b) = x² + (a+b)x + ab, the list would be [ab, a+b, 1].

So the approach is to start with the first (x + a1) as [a1, 1], then for each subsequent a_i, multiply the current polynomial by (x + a_i). Each multiplication step would generate a new list of coefficients.

So, for each step, the new polynomial is (current_coeffs) * (x + a_i). To compute the new coefficients:

The new degree is current_degree + 1. The new coefficients can be computed as:

new_coeffs[0] = current_coeffs[0] * a_i

new_coeffs[k] = current_coeffs[k-1] + current_coeffs[k] * a_i for k from 1 to current_degree

new_coeffs[current_degree + 1] = current_coeffs[current_degree] * 1 (since the x term adds a new highest degree)

Wait, maybe not. Let's think: when you multiply the current polynomial (which is of degree m) by (x + a_i), the new polynomial is of degree m+1.

The coefficient for x^{m+1} is the same as the coefficient of x^m in the current polynomial multiplied by x. So that's current_coeffs[m] * 1 (since x * x^m is x^{m+1}).

Then, for each term x^k in the current polynomial, multiplying by x gives x^{k+1} and multiplying by a_i gives a_i x^k. So the new coefficients for x^{k+1} would be current_coeffs[k] added to the new_coeffs[k+1], and a_i * current_coeffs[k] added to new_coeffs[k].

Wait, no. Let's model this properly. Suppose current_coeffs is a list where current_coeffs[k] is the coefficient of x^k. So the current polynomial is sum_{k=0 to m} current_coeffs[k] x^k.

Multiplying by (x + a_i) gives sum_{k=0 to m} current_coeffs[k] x^{k+1} + sum_{k=0 to m} current_coeffs[k] a_i x^k.

So combining these terms:

The new polynomial will be sum_{k=1 to m+1} current_coeffs[k-1] x^k + sum_{k=0 to m} current_coeffs[k] a_i x^k.

So the coefficients for x^k in the new polynomial are:

for k=0: current_coeffs[0] * a_i (from the second sum)

for 1 <= k <= m: current_coeffs[k-1] (from the first sum) + current_coeffs[k] * a_i (from the second sum)

for k=m+1: current_coeffs[m] (from the first sum)

So the new coefficients can be computed as follows:

new_coeffs = [0] * (m+2)

new_coeffs[0] = current_coeffs[0] * a_i

for k in 1 to m:
    new_coeffs[k] = current_coeffs[k-1] + current_coeffs[k] * a_i

new_coeffs[m+1] = current_coeffs[m]

So that's the correct way to compute each step.

So starting with the first factor (x + a1), which is represented as [a1, 1]. Then for each subsequent a_i, perform this multiplication step.

Once all factors are processed, the coefficients list will be of length n+1 (since the product of n factors of degree 1 is a polynomial of degree n). The coefficients are ordered from x^0 (constant term) up to x^n (leading term).

Wait no: for example, the first factor (x + a1) gives a polynomial x + a1, which is x^1 + a1 x^0. So in the coefficients list, index 0 is a1 (x^0 term), index 1 is 1 (x^1 term). So the list is [a1, 1]. Then when we multiply by (x + a2), the new coefficients will be for x^0, x^1, x^2.

So the initial approach is correct.

Once all factors are multiplied, the coefficients list will be [c_0, c_1, ..., c_n], where c_0 is the constant term (x^0), c_1 is the x^1 coefficient, and so on, up to c_n which is the x^n coefficient (which is 1, since all factors are (x + a_i) and when expanded, the leading term is x^n). Wait, no. Wait, the leading term is x multiplied n times, so it's x^n. So the coefficient for x^n is 1. So in the coefficients list, the last element (index n) is 1. But according to the multiplication steps above, when you multiply the first factor (x + a1), you have [a1, 1], which is x^1 + a1. Then, when multiplied by (x + a2), the new_coeffs would be:

new_coeffs[0] = a1 * a2

new_coeffs[1] = a1 (from x term) + a2 * 1 (from a_i term)

new_coeffs[2] = 1 (from x term)

So the coefficients list becomes [a1*a2, a1 + a2, 1], which is x^2 + (a1 + a2) x + a1 a2. Which is correct.

So the coefficients list is ordered from x^0 to x^n. So for the final polynomial, the coefficients are stored as [c_0, c_1, ..., c_{n}], where c_k is the coefficient for x^k. Wait no, because the indices are for x^0, x^1, etc. So the list is [c_0, c_1, ..., c_n], where c_0 is x^0 term (constant), c_1 is x^1 term, ..., c_n is x^n term.

But when building the output, we need to start from the highest degree (x^n) and go down to x^0. So the order to process the coefficients is from highest to lowest.

So after computing all coefficients, we reverse the list (excluding the leading 1?), wait no. Let's see.

Wait, after all factors are multiplied, the coefficients list will be of length n+1. The last element is the coefficient for x^n, which is 1 (since each multiplication step adds x * the previous leading term, which is 1 each time). Wait, let's see. For example, if n=3, then after multiplying all factors (x + a1)(x + a2)(x + a3), the leading term is x^3. So the coefficient for x^3 is 1. So in the coefficients list, the element at index 3 is 1.

So the coefficients list is [c_0, c_1, c_2, c_3], where c_0 is the constant term (product of all a_i's), c_3 is 1.

So when generating the terms, the order is from x^n down to x^0. So the coefficients we need to process are in reverse order (from c_n to c_0), except that the first term is x^n (c_n is 1), then the next term is c_{n-1} x^{n-1}, etc., until c_0.

But wait, in the coefficients list, the index corresponds to the x^degree. So to get the term for x^k, the coefficient is in coefficients[k]. So for the highest degree (n), the coefficient is coefficients[n] (which is 1). Then, next is coefficients[n-1] for x^{n-1}, etc.

So the order is: we process from x^n down to x^0, but the coefficients for each are coefficients[k], where k is the degree.

So for the output, the terms are:

For k in range(n, 0, -1):

Wait, no. Let's see. For example, in the first sample input:

n=2, a1=-1, a2=1.

The polynomial is (x -1)(x +1) = x² -1. The coefficients list is [-1 (x^0), 0 (x^1), 1 (x^2)]. Wait no. Wait, in that case, the product is x² + (a1 + a2)x + a1a2. Here, a1 is -1, a2 is 1.

So a1 + a2 = 0, a1*a2 = -1. So coefficients list is [-1, 0, 1]. So x^0 term is -1, x^1 is 0, x^2 is 1.

So when outputting, the terms are x^2 (1*x^2), then x^1 term is 0 (so omitted), then x^0 term is -1. So output is X^2-1.

So in this case, the order is x^2, x^0. So when processing the coefficients, we need to look from k = n down to 0, but the terms with coefficient 0 are skipped (except when n is 0? But n is at least 1 according to constraints).

So the plan is:

1. Compute the coefficients list, which starts as [a1, 1] for the first factor. Then for each subsequent a_i, compute the new coefficients as per the multiplication step.

2. After processing all a_i, the coefficients list is of length n+1, with coefficients[k] being the coefficient for x^k. However, the leading term (x^n) has coefficient 1.

3. Then, for output, we generate terms in order from x^n down to x^0, but:

   a. The x^n term is 1, so we output "X^K" where K is n. But if the coefficient is 1, we can omit the coefficient, except for x^0 term.

   b. For other terms, we check if the coefficient is non-zero. If it's zero, skip the term.

   c. For each non-zero term, format it properly:

      i. Coefficient is 1 and the exponent is 1: e.g., X^1 becomes X. If the exponent is 0, then it's just the coefficient (like 1*X^0 is 1).

      Wait, but in the problem statement, the output terms must be in the form "C*X^K". So how to handle coefficients of 1 and -1, and exponents of 0 and 1?

      Let's look at the examples:

      First example: output is X^2-1. So for x^2 term: coefficient is 1. The term is written as X^2. The constant term (x^0) is -1, written as -1.

      Second example: X^2+2*X+1. The x^2 term is 1 (so X^2), x term is 2*X, and constant is 1*X^0 which is 1.

      So the rules are:

      - For the term C*X^K:

        - If K is 0, then it's just C (since X^0 is 1, so C*1 is C).

        - If K is 1, then X^1 is written as X.

        - If C is 1 (and K > 0), then it's written as X^K (without the 1* part). Except when K is 0, which is handled above.

        - If C is -1 (and K >0), then it's written as -X^K.

        - Otherwise, it's written as C*X^K.

        - But wait, for example, in the second sample, the x term is 2*X. So when K=1, the exponent is written as X, not X^1.

      So the steps for formatting a term with coefficient C and exponent K (K >=0):

      If K is 0:

          Term is str(C)

      Else:

          if C == 1:

              part = "X"

              if K != 1:

                  part += f"^{K}"

          elif C == -1:

              part = "-X"

              if K != 1:

                  part += f"^{K}"

              # but the sign is part of the term. Wait, but in the case of C=-1, K=2, the term would be -X^2.

              # But in the first sample, the constant term is -1, which is written as -1.

          else:

              part = f"{C}*X"

              if K !=1:

                  part += f"^{K}"

      Then, when combining all terms, the sign is considered. For example, if a term is positive, it's prefixed with a '+', except the first term which can be without the '+'.

      So the plan is:

      For each term in order (from x^n down to x^0):

          Skip if coefficient is zero.

          Format the term as per the rules.

          Determine the sign (positive or negative) to prepend.

          For the first term, if positive, don't add a '+', but if negative, add '-'.

          For subsequent terms, add '+' if positive, '-' if negative.

      So the steps for formatting the entire polynomial:

      - Start with an empty list of terms.

      - Iterate over each possible exponent from n down to 0.

      - For each exponent K, get the coefficient C = coefficients[K].

      - If C is zero, skip.

      - Otherwise, format the term as per the rules.

      - Then, determine the sign and how to combine with previous terms.

      For example, the first sample's terms are:

      K=2: C=1 → "X^2"

      K=1: C=0 → skip

      K=0: C=-1 → "-1"

      So combined as "X^2" + "-1" → "X^2-1".

      The second sample:

      K=2: C=1 → "X^2"

      K=1: C=2 → "2*X"

      K=0: C=1 → "1"

      Combined as "X^2+2*X+1".

      Another example: suppose coefficient for x^3 is -1, x^2 is 3, x^0 is -5. Then the terms would be:

      -X^3+3*X^2-5.

      So the sign handling is important.

      So the way to handle the signs is:

      - For each term (except the first), if the coefficient is positive, prepend '+', else prepend '-'. However, the actual coefficient's absolute value is part of the term. Except when the coefficient is +1 or -1 (but only for exponents >0).

      So when formatting each term, the sign is part of the term. Wait, but the coefficients can be positive or negative. For example, if the coefficient is -3 for x^2, then the term is "-3*X^2".

      So the process is:

      For each non-zero term (after the first), check if the coefficient is positive or negative. Then, for the sign:

      If it's positive, prepend '+', else prepend '-'. Then, the term is formatted with the absolute value of the coefficient (but adjusted for 1 or -1 cases).

      Wait, but perhaps it's easier to include the sign in the coefficient when formatting the term. For example, when C is negative, the term's string starts with '-'.

      Let's think again. For a term with coefficient C:

      - If C is positive and it's the first term, we output the term without a '+'.

      - If C is positive and not the first term, we prepend '+'.

      - If C is negative, prepend '-', regardless of position (since even if it's the first term, it's a negative term).

      But how does this work for the first sample:

      The first term is C=1 (X^2), which is positive. So no '+'.

      The next term is C=-1 (constant term), which is negative. So '-1'.

      So the combined output is "X^2-1".

      Another example: if the first term is C=-1 (like in a polynomial like -x^3 + ...), then the first term is "-X^3".

      So the approach is:

      For each term:

          Format the term part (without sign), considering the absolute value of C.

          Then, determine the sign:

              if it's the first term:

                  if C is positive → no sign (but in the formatted term, it's already included, like 1 becomes X^3, but if C is negative, the formatted term starts with '-', like -X^3.

              else:

                  if the term's coefficient is positive → add '+', else add '-'.

      Wait, maybe I should structure the code to track the sign correctly.

      Let's see. For each term's coefficient C (non-zero):

          The formatted term (without sign) is based on |C|, but for the case when |C| is 1 and K>0.

          Then, the sign is determined by C's sign.

      So for example, if C is -2 and K is 3:

          formatted term part is "2*X^3", and the sign is '-'.

          So the term becomes "-2*X^3".

      If C is -1 and K is 2:

          formatted term part is "X^2", and the sign is '-', so "-X^2".

      So, to format each term, we need to:

      - Take the absolute value of C for the coefficient part (except for 0, but we already skip zero terms).

      - But for C=1 or -1, and K>0, we omit the coefficient.

      So the code for formatting the term is:

      def format_term(c, k):

          if k == 0:

              return f"{c}"

          abs_c = abs(c)

          sign = '-' if c < 0 else ''

          # handle coefficient part

          if abs_c == 1 and k != 0:

              coeff_part = ''

              # but for 1, the coefficient is omitted, except when k is 0.

              # since k is not 0 here.

          else:

              coeff_part = f"{abs_c}*"

          # handle X part

          x_part = 'X'

          if k == 1:

              x_part = 'X'

          else:

              x_part = f'X^{k}'

          term = f"{coeff_part}{x_part}"

          if term == '':

              term = '1'  # but this would only be when k=0.

          # combine with sign

          return sign + term

      Wait, but for c=-1 and k=2, the code would generate:

          sign is '-', abs_c is 1, coeff_part is '', x_part is 'X^2' → '-X^2'

      For c=1 and k=2 → sign is '' → 'X^2'.

      For c=5 and k=3 → sign is '+', but since in code, the code returns sign (which for c=5 is '') and coeff_part is '5*', x_part 'X^3' → '5*X^3'.

      Wait, but the sign is handled outside of this function. Because the way the terms are combined depends on their order and whether they are the first term.

      Oh right. So perhaps the formatting function should return the term part (without the sign), and then the sign is handled when building the output string.

      Wait, perhaps that's better.

      So for example, for c=2, k=3: the term is "2*X^3".

      For c=-2, k=3: the term is "2*X^3", and the sign is '-'.

      So the formatting function would return the term part (without sign), and the sign is determined by the coefficient's sign.

      Then, when building the output, the first term's sign is added as '-', if needed, and others are added with '+' or '-'.

      Let's think again. For the first term:

          if the coefficient is positive: term is formatted without a sign (since the leading term's sign is implied as positive if there's no sign). But wait, the leading term's coefficient is 1 (since it's x^n) but perhaps in code, after expanding, the coefficients might have a different sign. Wait, no. Because in the problem statement, the polynomial is a product of (x + a_i) terms. So each a_i can be positive or negative, but the leading term is x multiplied by each term's x, so the leading term is x^n, coefficient 1.

          Wait, that's correct. So the leading term is always 1 * x^n. Because when you multiply (x + a1)(x + a2)... (x + an), the leading term is x * x * ... * x = x^n. So the coefficient for x^n is always 1. So in the coefficients list, the last element (index n) is 1.

          So the first term (x^n) will always have coefficient 1, so it's written as "X^n", unless n is 0. But the constraints say n >=1. So the first term is always "X^n", with no sign (since 1 is positive). Then, subsequent terms are added with their signs.

          Wait, but that's only if all the a_i's are such that the leading term is x^n. Because when you multiply (x + a_i) terms, the leading term is x^n, so coefficient is 1. So in the coefficients list, coefficients[n] is 1.

          So for the output, the first term is "X^K", where K is n, and since coefficients[n] is 1, which is positive. So the first term is "X^n".

          Then, the other terms (from x^{n-1} down to x^0) are processed. Each of their coefficients can be positive or negative.

          So for these terms:

              if the coefficient is positive: prepend '+'.

              if negative: prepend '-'.

          So the code can be structured as:

          output = []

          # first term is x^n, which is 1*X^n. So format as "X^n"

          output.append("X^" + str(n) if n != 1 else "X")

          # then process the rest terms from x^{n-1} to x^0:

          for k in range(n-1, -1, -1):

              c = coefficients[k]

              if c == 0:

                  continue

              # format the term part (without sign)

              term = format_term_part(c, k)

              # determine the sign to prepend (based on c's sign)

              sign = '+' if c > 0 else '-'

              # append the sign and term part

              output.append(sign + term)

          # then, join all parts. But wait, the first term has no sign, but the code's first element is "X^n", and the subsequent terms have their sign.

          Wait, but for example, in the first sample:

          The coefficients are [-1, 0, 1]. So for k=2 (x^2), c=1 → part of first term. Then, for k=1 (0, skipped), and k=0 (-1). The term for k=0 is -1. So the code after the first term would process k=0, c=-1. The sign is '-', and the term part is '1' (since c is -1, and k=0. So format_term_part would be '1'? Wait, no.

          Let's re-examine.

          For the code:

          After the first term (x^2), the next terms are for k=1 (c=0, skipped) and k=0 (c=-1). For k=0:

              c is -1, so sign is '-', term_part is '1' (since k=0, the term is '1').

              So the term is '-1'.

              So the output list is ["X^2", "-1"], which is joined as "X^2-1".

          Correct.

          For the second sample:

              coefficients are [1, 2, 1]. Wait, no. Wait, the polynomial is (x+1)(x+1) = x² +2x +1. So coefficients[0] is 1 (x^0 term), coefficients[1] is 2 (x^1), coefficients[2] is 1 (x^2). So the code's first term is "X^2". Then, for k=1 (c=2) → sign '+', term_part is '2*X' (since k=1). So output is "+2*X". Then k=0 (c=1) → sign '+', term_part is '1'. So output list is ["X^2", "+2*X", "+1"], which when joined becomes "X^2+2*X+1".

          So this approach would work.

          So the code steps are:

          1. Compute the coefficients list.

          2. The first term is "X^" + str(n) if n >=2, else "X" (for n=1).

          3. For the remaining terms (k from n-1 downto 0):

              a. If coefficients[k] is zero, skip.

              b. Else, format the term part (without sign) using the absolute value of coefficients[k], and considering the exponent k.

              c. Determine the sign: '+' if coefficients[k] is positive, else '-'.

              d. Prepend the sign to the term part and add to the output list.

          4. Join all elements of the output list into a single string.

          Now, the function format_term_part must handle the coefficient's absolute value and the exponent k.

          So for example:

          For k=0:

              if c is 5 → term_part is '5'

              if c is -3 → term_part is '3'

          For k=1:

              if c is 1 → term_part is 'X'

              if c is -1 → term_part is 'X'

              if c is 5 → term_part is '5*X'

          For k=2:

              c is 1 → term_part is 'X^2'

              c is -1 → term_part is 'X^2'

              c is 5 → term_part is '5*X^2'

          For k=0, regardless of c (as long as it's not zero):

              term_part is str(abs(c)) if k=0 and c !=0.

          Wait, no. For k=0, the term is C * X^0 = C. So the term_part is the absolute value of C (if sign is handled by the sign variable). So if c is -5, then sign is '-', term_part is '5'.

          But in the first sample, for k=0 and c=-1, the term_part is '1' and the sign is '-', leading to "-1".

          So for the term_part, when k=0, it's just the absolute value of the coefficient. For example, c=3 → '3', c=-5 → '5', c=1 → '1', etc.

          So the format_term_part function can be written as:

          def format_term_part(c, k):

              abs_c = abs(c)

              if k == 0:

                  return f"{abs_c}"

              # for k >0

              if abs_c == 1:

                  coeff_part = ''

              else:

                  coeff_part = f"{abs_c}*"

              x_part = 'X'

              if k == 1:

                  x_part = 'X'

              else:

                  x_part = f'X^{k}'

              return f"{coeff_part}{x_part}"

          So for c=1, k=2 → 'X^2'

          c=2, k=3 → '2*X^3'

          c=-3, k=0 → '3'

          c=-1, k=1 → 'X'

          So with this function, the term_part for the code in the second sample is:

          For k=1, c=2 → abs_c=2, k=1 → term_part is '2*X'

          So the sign is '+', and the term is '+2*X'.

          For k=0, c=1 → term_part is '1', sign '+', term '+1'.

          So the code works.

          Now, the steps to compute the coefficients list.

          The initial coefficients list for the first factor (x + a1) is [a1, 1].

          Then for each subsequent a_i, compute new coefficients.

          So for example, when adding a new a_i, the current coefficients list is of length m+1 (for a polynomial of degree m). Multiplying by (x + a_i) gives a new polynomial of degree m+1.

          The new coefficients list is of length (m+1)+1 = m+2.

          So the code can represent the coefficients as a list, starting with the first factor, then for each a_i in the list (after the first), perform the multiplication.

          So steps:

          1. Read n.

          2. Read a list of n integers (a1, a2, ..., an). Note that the order is important. The factors are (x + a1)(x + a2)...(x + an). The order of multiplication affects the coefficients.

          3. Initialize coefficients as [a1, 1] (for the first factor).

          4. For each a_i in the list from index 1 to n-1:

              a. current_length = len(coeffs) = m+1 (current degree m).

              b. new_coeffs is a list of length m+2.

              c. new_coeffs[0] = coeffs[0] * a_i.

              d. new_coeffs[m+1] = coeffs[m] (since it's the x^(m+1) term, which is coeffs[m] (current x^m term multiplied by x).

              e. for k from 1 to m:

                  new_coeffs[k] = coeffs[k-1] + coeffs[k] * a_i.

              f. set coeffs = new_coeffs.

          So for example, after the first factor, coeffs is [a1, 1].

          Adding the second factor (x + a2):

              new_coeffs has length 3.

              new_coeffs[0] = a1 * a2.

              new_coeffs[2] = 1 (from coeffs[1] * 1).

              for k=1:

                  new_coeffs[1] = coeffs[0] + coeffs[1] * a2 → a1 + 1*a2.

              So new_coeffs = [a1a2, a1+a2, 1], which is correct.

          So the code can implement this step.

          Now, implementing this in Python.

          Let's code this step.

          Read n.

          Then read n lines of a_i.

          Then:

          if n ==0: # but according to constraints, n >=1.

          else:

              a_list = [int(input()) for _ in range(n)]

              coeffs = [a_list[0], 1]

              for i in range(1, n):

                  ai = a_list[i]

                  m = len(coeffs) -1 # current degree is m.

                  new_coeffs = [0]*(m+2)

                  # new_coeffs[0] = coeffs[0] * ai

                  new_coeffs[0] = coeffs[0] * ai

                  # new_coeffs[m+1] = coeffs[m]

                  new_coeffs[-1] = coeffs[-1]

                  # for k in 1..m:

                  for k in range(1, m+1):

                      new_coeffs[k] = coeffs[k-1] + coeffs[k] * ai

                  coeffs = new_coeffs

              # after processing all a_i, coeffs has length n+1. coeffs[k] is the coefficient of x^k.

              # but wait, no. Let's see:

              For example, n=2. After first factor, coeffs is length 2 (a1, 1). Then after second factor, it's length 3. So yes, for n factors, the coefficients list is length n+1.

              So for n factors, the code after the loop, coeffs is [c_0, c_1, ..., c_n], where c_k is the coefficient of x^k.

              Then, the first term is x^n, which is c_n. But wait, according to the code, for n=2, the coeffs after processing two factors would be:

              coeffs[0] is a1*a2, coeffs[1] is a1+a2, coeffs[2] is 1.

              So yes, x^2 term is 1.

              So the code is correct.

          Now, once the coefficients are computed, the next step is to generate the output.

          So for the first term, it's x^n, coefficient 1 → "X^" + str(n) if n>1, else "X".

          Then, for k from n-1 downto 0:

              c = coeffs[k]

              if c is zero, skip.

              else, format_term_part(abs(c), k), and prepend '+' or '-' based on c's sign.

              So code:

              terms = []

              # first term is x^n, coefficient 1.

              if n == 1:

                  terms.append("X")

              else:

                  terms.append(f"X^{n}")

              for k in range(n-1, -1, -1):

                  c = coeffs[k]

                  if c == 0:

                      continue

                  term_part = format_term_part(abs(c), k)

                  sign = '+' if c > 0 else '-'

                  terms.append(sign + term_part)

              # join the terms.

              result = ''.join(terms)

              print(result)

          Let's test this with the first sample:

          n=2, a_list is [-1, 1].

          coeffs after processing:

          initial coeffs: [-1, 1]

          Then multiply by (x + 1) (ai=1):

              m=1 (len coeffs-1 =1).

              new_coeffs length 3.

              new_coeffs[0] = -1 *1 = -1.

              new_coeffs[2] = 1 (coeffs[1] = 1).

              for k=1:

                  new_coeffs[1] = coeffs[0] (which is -1) + coeffs[1] *1 (1*1=1) → -1 +1 =0.

              So coeffs is [-1, 0, 1].

              Then, generating terms:

              first term: X^2.

              then k=1: coeffs[1] is 0 → skipped.

              k=0: coeffs[0] is -1 → term_part is '1', sign '-', so '-1'.

              terms are ['X^2', '-1'] → output "X^2-1".

          Correct.

          Second sample:

          n=2, a_list [1,1].

          coeffs after first factor: [1,1].

          multiply by (x+1):

              m=1.

              new_coeffs[0] =1*1=1.

              new_coeffs[2] =1.

              for k=1:

                  new_coeffs[1] = coeffs[0] (1) + coeffs[1] *1 → 1 +1=2.

              coeffs becomes [1,2,1].

              Generating terms:

              first term: X^2.

              k=1: c=2 → term_part '2*X', sign '+', term '+2*X'.

              k=0: c=1 → '+1'.

              output is X^2+2*X+1.

          Correct.

          Now, another test case: n=3, a_i's are 1,1,1.

          The polynomial is (x+1)^3 = x^3 +3x² +3x +1.

          coeffs after processing:

          Let's see:

          After first factor: [1,1]

          second factor: multiply by (x+1):

              new_coeffs[0] =1*1=1.

              new_coeffs[2] =1.

              new_coeffs[1] =1 +1*1=2.

              coeffs becomes [1,2,1]

          third factor: multiply by (x+1):

              new_coeffs[0] =1*1=1.

              new_coeffs[3] =1.

              for k=1: coeffs[0] (1) + coeffs[1] *1 (2*1=2) → 1+2=3.

              for k=2: coeffs[1] (2) + coeffs[2] *1 (1*1=1) → 2+1=3.

              new_coeffs is [1,3,3,1].

              So coefficients for x^0 is 1, x^1 is3, x^2 is3, x^3 is1.

              So generating terms:

              first term X^3.

              then k=2: c=3 → term_part '3*X^2', sign '+', '+3*X^2'.

              k=1: c=3 → '+3*X'.

              k=0: c=1 → '+1'.

              So output: X^3+3*X^2+3*X+1.

          Correct.

          Another test case: n=1, a1=5.

          The polynomial is x+5. So output is X+5.

          coeffs after processing is [5,1].

          So first term is X (n=1), then k=0: c=5 → '+5'. So output X+5.

          Another case: n=3, a_i's are 0,0,0 → product is (x)^3 → x^3. So coefficients are [0,0,0,1]. So output is X^3.

          Another case: n=3, a_i's are 2, -3, 4. Then the product is (x+2)(x-3)(x+4).

          Let's compute the coefficients:

          First factor (x+2): coeffs [2,1].

          Multiply by (x-3):

              new_coeffs[0] =2*(-3) =-6.

              new_coeffs[2] =1.

              new_coeffs[1] =2 +1*(-3) =2-3 =-1.

              coeffs now [-6, -1, 1].

          Multiply by (x+4):

              new_coeffs[0] =-6 *4 =-24.

              new_coeffs[3] =1.

              for k=1: new_coeffs[1] = coeffs[0] (-6) + coeffs[1] *4 (-1*4=-4) → -6-4= -10.

              for k=2: coeffs[1] (-1) + coeffs[2] *4 (1*4=4) → -1+4=3.

              So new_coeffs is [-24, -10, 3, 1].

          So terms:

          X^3.

          k=2: coefficient 3 → '+3*X^2'.

          k=1: coefficient -10 → '-10*X'.

          k=0: coefficient -24 → '-24'.

          So output: X^3+3*X^2-10*X-24.

          Which is correct.

          Now, what about a term with coefficient zero? For example, (x-1)(x+1)(x^2 +1) is (x²-1)(x^2+1) =x^4-1. But in our case, with factors (x + a_i), but if a_i's are arranged such that certain terms have zero coefficients.

          So the code skips any term with coefficient zero.

          So, in code, after the first term (which is x^n, coefficient 1), for each other term, if c is zero, skip.

          Now, the code should handle all cases.

          Now, code implementation:

          Read n.

          Read a_list.

          Compute the coefficients.

          Generate the terms.

          Now, code:

          Read n.

          Then, read n lines as a_list.

          Then, if n is zero (but n >=1 according to constraints), so ignore.

          Now, code:

          n = int(input())

          a_list = [int(input()) for _ in range(n)]

          if n ==0:

              # not possible, but handle if needed.

              print("0")

          else:

              # compute coefficients.

              coeffs = [a_list[0], 1]

              for ai in a_list[1:]:

                  m = len(coeffs) -1

                  new_coeffs = [0]*(m+2)

                  new_coeffs[0] = coeffs[0] * ai

                  new_coeffs[-1] = coeffs[-1]

                  for k in range(1, m+1):

                      new_coeffs[k] = coeffs[k-1] + coeffs[k] * ai

                  coeffs = new_coeffs

              # generate terms.

              terms = []

              # first term is x^n.

              if n ==1:

                  terms.append("X")

              else:

                  terms.append(f"X^{n}")

              for k in range(n-1, -1, -1):

                  c = coeffs[k]

                  if c ==0:

                      continue

                  # format term part.

                  if k ==0:

                      term_part = f"{abs(c)}"

                  else:

                      if abs(c) ==1:

                          coeff_part = ''

                      else:

                          coeff_part = f"{abs(c)}*"

                      if k ==1:

                          x_part = 'X'

                      else:

                          x_part = f'X^{k}'

                      term_part = f"{coeff_part}{x_part}"

                  sign = '+' if c >0 else '-'

                  terms.append(sign + term_part)

              # join terms.

              print(''.join(terms))

          Now, let's test this code with the samples.

          First sample:

          Input:

          2

          -1

          1

          coeffs becomes [-1,0,1]

          terms:

          X^2.

          k=1: c=0 → skipped.

          k=0: c=-1 → term_part '1', sign '-', term '-1'.

          Output: X^2-1.

          Correct.

          Second sample:

          Input:

          2

          1

          1

          coeffs: [1,2,1]

          terms: X^2, then k=1 (2 → '+2*X'), k=0 (1 → '+1').

          Output: X^2+2*X+1.

          Correct.

          Third test case: n=1, a=5.

          coeffs: [5,1].

          terms: 'X' (n=1), then k=0:5 → '+5'.

          Output: X+5.

          Another test case: n=3, a_list [0,0,0]. Coefficients after processing:

          Initial: [0,1]

          Multiply by (x+0): new coeffs [0*0=0, 0 +1*0=0, 1].

          Then multiply by (x+0) again: new coeffs [0*0=0, 0 +0*0=0, 0 +1*0=0, 1].

          So coeffs are [0,0,0,1].

          terms:

          X^3.

          k=2:0 → skipped.

          k=1:0 → skipped.

          k=0:0 → skipped.

          So output is X^3.

          Correct.

          Another case: n=3, a_list [2,-3,4]. As before, the code produces X^3+3*X^2-10*X-24.

          Now, code seems correct.

          Edge cases:

          n=1, a=0 → x+0 → x. Output: X.

          coeffs: [0,1].

          terms:

          X.

          k=0:0 → skipped.

          Output: X.

          Another case: n=1, a=10. Output X+10.

          Now, handle the case where a term has coefficient -1.

          For example: (x -1) → x-1. So code for n=1:

          coeffs is [-1,1].

          terms:

          X (n=1).

          k=0: c=-1 → term_part '1', sign '-', term '-1'.

          Output X-1.

          Another example: (x-1)(x-2) → x²-3x+2. Coefficients [2, -3, 1].

          terms:

          X^2.

          k=1: c=-3 → '-3*X'.

          k=0: 2 → '+2'.

          So output X^2-3*X+2.

          Correct.

          Another example with coefficient -1 and exponent 2:

          (x-1)(x-1)(x+0) → (x²-2x+1)(x) → x³ -2x² +x. Coefficients [0, 1, -2, 1].

          terms:

          X^3.

          k=2: -2 → '-2*X^2'.

          k=1: 1 → '+X'.

          k=0: 0 → skipped.

          So output X^3-2*X^2+X.

          Correct.

          Now, handle the case when a coefficient is 1 in a lower term.

          So for example, (x+1)(x-1) = x²-1. The code correctly outputs X^2-1.

          Now, code should handle all these cases.

          So the code seems correct.
</think>

```python
n = int(input())
a_list = [int(input()) for _ in range(n)]

coeffs = [a_list[0], 1]
for ai in a_list[1:]:
    m = len(coeffs) - 1
    new_coeffs = [0] * (m + 2)
    new_coeffs[0] = coeffs[0] * ai
    new_coeffs[-1] = coeffs[-1]
    for k in range(1, m + 1):
        new_coeffs[k] = coeffs[k-1] + coeffs[k] * ai
    coeffs = new_coeffs

terms = []
if n == 1:
    terms.append("X")
else:
    terms.append(f"X^{n}")

for k in range(n-1, -1, -1):
    c = coeffs[k]
    if c == 0:
        continue
    if k == 0:
        term_part = f"{abs(c)}"
    else:
        coeff_part = '' if abs(c) == 1 else f"{abs(c)}*"
        x_part = 'X' if k == 1 else f'X^{k}'
        term_part = f"{coeff_part}{x_part}"
    sign = '+' if c > 0 else '-'
    terms.append(sign + term_part)

print(''.join(terms))
```