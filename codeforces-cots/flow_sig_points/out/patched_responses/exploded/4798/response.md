<think>
Okay, let's tackle this problem. Hmm, so the problem is about finding the optimal m-bit number Peter should choose to minimize or maximize the sum of all variables. The variables can be constants or depend on previous variables and Peter's number via bitwise operations. Oh right, and for each bit in Peter's number, we need to decide whether to set it to 0 or 1 such that the total sum is minimized or maximized, and if there's a tie, choose the smallest binary number.

First, let's understand the structure of the variables. Each variable is either a binary string (so a constant) or a combination of two operands with a bitwise operation. The operands can be a variable defined earlier or '?', which is Peter's number. So the dependencies are such that variables are processed in the order they are given, and each can refer only to previous ones or the '?'.

The key here is to model how each bit of Peter's choice affects each bit of each variable. Since each bit in the variables can be computed independently based on the bits of the operands, we can process each bit position (from the first to the m-th) separately. Because the sum of all variables is the sum of their individual bits (each bit contributes 2^bit_position to the total, but since all variables contribute their bits, for each bit position k, the total contribution is (number of variables with a 1 in bit k) multiplied by 2^(m-1 -k) assuming the bits are indexed from left to right as 0 to m-1 or something similar. Wait, the binary numbers are written in standard form. For example, 3 bits like '101' is 5 in decimal. So the leftmost bit is the highest order bit. So for each bit position in Peter's number (each bit from 0 to m-1, left to right), we need to determine whether setting it to 0 or 1 will lead to a minimal or maximal sum.

Wait, but how do the variables' bits depend on Peter's bits? For each variable, if it's a constant, then its bits are fixed. If it's an operation, then each bit of the result depends on the corresponding bits of the operands. So for each bit position, the value of the variable's bit is computed based on the two operands' bits in the same position. Because bitwise operations are performed bit-wise. So each bit can be considered independently.

Therefore, for each bit position k in Peter's number (from 0 to m-1), we can compute the contribution to the total sum when that bit is set to 0 or 1, and then decide for each bit whether to choose 0 or 1 to minimize or maximize the total sum.

This suggests that for each bit position in Peter's number, we can precompute the impact of that bit on the sum. Then, for each bit, choose 0 or 1 based on whether it's better for the current objective (min or max). Since each bit can be handled independently (due to the bitwise operations), this approach would work.

But how do we model the impact of a particular bit in Peter's number on the variables?

For each variable, we can track, for each bit position, the value of that bit as a function of the bits of the variables and Peter's number. However, since variables are processed in order, and each can refer to earlier variables, but not later ones, we can process the variables sequentially, and for each bit position, track how each bit of each variable depends on Peter's bits.

Wait, but for each variable, each of its bits may depend on the bits of the operands in the same position. So for each bit position k, the value of variable X's k-th bit is a function of the k-th bits of its operands. So, for each variable, and each bit position, we can compute the value based on the operands' bits in the same position.

So the key idea is: for each bit position k (from 0 to m-1, left to right?), we can compute the contribution of Peter's bit at position k (0 or 1) to the total sum. Then, for each bit, choose 0 or 1 for the min and max cases, considering the dependencies and how the variables' bits are computed.

Wait, but how do we compute the effect of Peter's k-th bit on the variables' bits? For example, if a variable is computed as ? XOR a, where a is a previous variable. Then, for each bit k, the result's k-th bit is (peter_bit_k) XOR (a's k-th bit). So the variables' bits are computed based on the same bit position of their operands. Therefore, the processing for each bit position is independent of other positions.

This means that for each bit position in Peter's number, we can process it independently. For each such bit, we can compute how many variables' bits are 1 when Peter's bit is 0 or 1, then the contribution to the sum is the count multiplied by 2^(m-1 -k) (since for a bit in position k of an m-bit number, it's worth 2^(m-1 -k), as the leftmost bit is the highest order).

Therefore, the approach is to process each bit of Peter's number (from left to right, i.e., from the most significant to the least significant) and for each bit position k, determine whether setting it to 0 or 1 gives a better (min or max) contribution to the total sum. Then, select the optimal bit, considering that in case of a tie (same contribution for 0 and 1), we choose 0 for the minimum case (since we want the smallest possible binary number), and 0 for the maximum case as well (since if the contributions are equal, the earliest bits being 0 would make the number smaller). Wait, but for the maximum case, if choosing 0 and 1 gives the same contribution, but we need the minimal number in case of a tie. So if the contribution is the same, we should choose 0 for the earlier bits to minimize the number.

So for each bit position k (from left to right), for both min and max scenarios, we need to compute the contribution of setting that bit to 0 or 1, and choose the best option (with tie broken by choosing 0).

The challenge is then to model, for each bit k, the effect of Peter's choice (0 or 1) on the sum.

Let's think about how to model the variables for a single bit position.

For each variable, when processing it, we need to track for each bit position k whether the variable's k-th bit is 0 or 1. However, since for each bit position, the processing is independent, perhaps we can process all variables for each bit position, considering the dependencies.

But if we process each bit position separately, then for each variable, we can compute its value for that bit based on the operands' bits in the same position and Peter's bit (if any of the operands is '?').

So here's the plan:

For each bit position k (from 0 to m-1), we can compute the total contribution to the sum when Peter's k-th bit is set to 0 or 1. Then, for each bit, decide whether to set it to 0 or 1 in the min and max cases.

But how do we compute the contribution for each possible choice (0 or 1) of Peter's bit in position k?

The steps would be:

1. For each variable, for each bit position k, compute the value of that bit when Peter's k-th bit is 0 or 1. Then, sum all variables' bits for each possible choice (0 or 1), and multiply by 2^(m-1 -k) to get the contribution to the total sum.

But variables can depend on other variables, which in turn depend on Peter's bit. So for each bit k, we need to process the variables in order, and for each, compute their bit value based on their operands.

But since variables can only refer to earlier variables, we can process them in the order given. For each variable, for each possible choice of Peter's bit (0 or 1 for k-th position), compute the value of that variable's k-th bit.

But variables can be either constants, or expressions involving operands (variables or '?') and a bitwise operation.

So, for each variable and each bit k, the value is determined as follows:

- If the variable is a constant, then the k-th bit is fixed (0 or 1).
- If it's an expression, then the k-th bit is the result of the operation applied to the k-th bits of the two operands.

But the operands can be variables (previously defined) or '?', which is Peter's choice. So for each operand:

- If the operand is a variable, then we can get its k-th bit (which has been computed already, since variables are processed in order).
- If the operand is '?', then its k-th bit is Peter's choice (0 or 1).

So, for each variable and each bit k, we can model the k-th bit as a function of Peter's k-th bit. For each variable, when we process it, we can compute for each k whether the bit depends on Peter's k-th bit (i.e., if any of the operands is '?').

But how?

Alternatively, for each bit k, we can compute for each variable, the value of their k-th bit in two scenarios: when Peter's k-th bit is 0 and when it's 1. Then, for each scenario, we can compute the sum of all variables' bits at position k. The total contribution to the sum for that bit would be (sum_0) * 2^(m-1 -k) when Peter's bit is 0, and (sum_1) * 2^... when it's 1. However, since each variable's k-th bit is computed based on the operands' k-th bits, which may include Peter's choice, we need to model for each scenario (Peter's bit 0 or 1), how the variables' bits look.

So, for each bit k, we can:

- Simulate the processing of all variables, for both possible values of Peter's k-th bit (0 and 1), and compute the sum of all variables' k-th bits in each case.

Once we have sum_0 and sum_1 for bit k, we can compute the contribution of this bit to the total sum as sum_0 * (2^ (m-1 -k)) and sum_1 * (same). Then, for the min and max scenarios, we can choose between the two options.

But how do we compute sum_0 and sum_1 for each bit k?

Let's see. For each bit k:

sum_0 is the sum of variables' bits when Peter's k-th bit is 0.

sum_1 is the sum when Peter's k-th bit is 1.

We can compute these by processing each variable in order, and for each, compute its k-th bit in both scenarios.

But variables can have operands that are '?', which in this case, in scenario 0, the operand's k-th bit is 0, and in scenario 1, it's 1.

So, for each variable:

If it's a constant, then its k-th bit is fixed, same in both scenarios.

If it's an operation, then for each scenario (0 or 1), compute the two operands' bits (for their k-th bit) and apply the operation.

So for each variable, and each scenario (0 or 1 for Peter's k-th bit), we can compute the variable's k-th bit. Then sum all variables' bits for each scenario.

This approach is feasible. For each of the m bits, we process each of the n variables, for two scenarios. The total time would be O(m * n). Since n can be up to 5000 and m up to 1000, that's 5,000 * 1000 * 2 = 10,000,000 operations, which should be manageable.

Once we have sum_0 and sum_1 for each bit, we can decide for each bit whether 0 or 1 is better for the min and max cases.

But wait, how do we compute the sum_0 and sum_1?

For each bit k:

sum_0 = sum of all variables' k-th bits when Peter's k-th bit is 0.

sum_1 = sum of all variables' k-th bits when Peter's k-th bit is 1.

But variables can refer to other variables. So, for each variable, when processing it, we need to compute its k-th bit based on the operands' k-th bits (which may have been computed for scenarios 0 and 1).

Let's think of variables as being processed in order. For each variable, we can precompute for each bit k, its value in both scenarios (0 and 1). Then, for each variable, for each scenario, the value of the k-th bit is stored.

So, for each variable, for each bit k, we can have two values: val_0 and val_1, indicating the bit's value when Peter's k-th bit is 0 or 1.

So the steps are:

For each bit k in 0..m-1:

   For each variable in order:

      If variable is a constant: val_0 and val_1 are the same as the k-th bit of the constant.

      Else (operation with op1, op, op2):

          For scenario 0 (Peter's k-bit is 0):

              a = get the value of op1 for scenario 0 and bit k.

              b = get the value of op2 for scenario 0 and bit k.

              compute the bit value using the operation.

          For scenario 1 (Peter's k-bit is 1):

              a = get the value of op1 for scenario 1 and bit k.

              b = get the value of op2 for scenario 1 and bit k.

              compute the bit value.

          Set val_0 and val_1 for this variable and bit k.

   sum_0 is the sum of all variables' val_0 for this bit k.

   sum_1 is the sum of all variables' val_1 for this bit k.

Then, for each bit k, the contribution to the sum is (sum_0) * 2^(m-1 -k) when Peter's bit is 0, and sum_1 * ... when 1.

But for the purpose of choosing between 0 and 1, the actual sum contribution is (sum_0 or sum_1) multiplied by the same 2^something. Since the 2^something is the same for both options, the decision between 0 and 1 is based on whether sum_0 is less than sum_1 (for the min case) or sum_1 is greater (for the max case). Because the multiplier is positive, so the choice is determined by the sum_0 and sum_1 for that bit.

Therefore, for each bit k:

For the minimum total sum:

   if sum_0 < sum_1: choose 0.

   elif sum_0 > sum_1: choose 1.

   else: choose 0 (to get the smallest possible number).

For the maximum total sum:

   if sum_1 > sum_0: choose 1.

   elif sum_1 < sum_0: choose 0.

   else: choose 0 (to minimize the number in case of tie).

So the plan is:

1. Precompute for each bit k, the sum_0 and sum_1.

2. For each bit k, decide whether 0 or 1 is better for min and max.

3. Construct the min and max binary strings by choosing for each bit the optimal value, breaking ties by choosing 0.

Now, the problem is how to compute sum_0 and sum_1 for each bit k and each variable.

Let's see how to model the variables.

Each variable can be stored as a structure that indicates whether it's a constant or an operation with operands and operator.

For each variable, we need to track, for each bit k, the value when Peter's bit is 0 or 1.

But storing this for all m bits and two scenarios per variable might be memory-intensive. For m=1000 and n=5000 variables, that's 5000 * 1000 * 2 = 10,000,000 bits, which is manageable (as 1.25 MB).

But perhaps we can compute this per bit and per scenario on the fly.

Let's think in terms of processing each bit separately.

For each bit k (from 0 to m-1):

   For each variable in order, compute val_0 and val_1 (the value of the variable's k-th bit when Peter's k is 0 or 1).

   Sum all val_0 and val_1 for sum_0 and sum_1.

This way, for each bit, we process all variables, and for each variable, compute its k-th bit for both scenarios.

This approach would require O(n) time per bit, leading to O(m * n) total time.

Yes, that's manageable.

So, the steps for each bit k:

Initialize two variables current_sum_0 and current_sum_1 as 0.

Create a dictionary to track for each variable (processed so far) their val_0 and val_1 for this bit.

Process each variable in order:

   If variable is a constant:

       binary_str = the constant's value (e.g., '101')

       bit_k = binary_str[k] (as '0' or '1')

       val_0 = bit_k == '1'

       val_1 = bit_k == '1'

   Else (operation):

       op1, op, op2 = the operands and operator.

       For scenario 0:

           a = get the value of op1 in scenario 0 (could be from a previous variable, or '?' which is 0)

           b = get the value of op2 in scenario 0 (same as above)

       For scenario 1:

           a_s1 = get the value of op1 in scenario 1 (could be from a previous variable, or '?' which is 1)

           b_s1 = get the value of op2 in scenario 1.

       Then compute the result for each scenario.

       So:

       For scenario 0:

           a_val = if op1 is '?', then 0 else lookup in the dictionary for the variable op1's val_0.

           b_val = if op2 is '?', then 0 else lookup in the dictionary for the variable op2's val_0.

           compute the operation (AND, OR, XOR) on a_val and b_val. The result is val_0.

       For scenario 1:

           a_val = if op1 is '?', then 1 else lookup in the dictionary for the variable op1's val_1.

           b_val = if op2 is '?', then 1 else lookup in the dictionary for the variable op2's val_1.

           compute the operation. The result is val_1.

   Then, add val_0 to current_sum_0 and val_1 to current_sum_1.

   Store val_0 and val_1 for this variable in the dictionary.

At the end of processing all variables for this bit k, sum_0 is current_sum_0 and sum_1 is current_sum_1.

So, for each bit, we process all variables, track their val_0 and val_1 for that bit, and accumulate the sum.

This approach seems feasible.

So, the main steps are:

- Preprocess all variables into a list, storing their type (constant or operation with operands and operator).

- For each bit k:

   Initialize a dictionary (like a hashmap) to hold the val_0 and val_1 for each variable processed so far.

   Initialize sum_0 and sum_1 to 0.

   For each variable in order:

       if it's a constant:

           bit = constant's k-th bit (0 or 1)

           val_0 = val_1 = bit

       else:

           op1, op, op2 = the operands.

           a0, b0: values of op1 and op2 in scenario 0 (Peter's bit is 0).

               a0 = 0 if op1 is '?', else variables[op1].val_0 for this bit.

               b0 = 0 if op2 is '?', else variables[op2].val_0.

           a1, b1: values of op1 and op2 in scenario 1 (Peter's bit is 1).

               a1 = 1 if op1 is '?', else variables[op1].val_1.

               b1 = 1 if op2 is '?', else variables[op2].val_1.

           compute the operation for scenario 0:

               if op is AND: val_0 = a0 & b0

               OR: val_0 = a0 | b0

               XOR: val_0 = a0 ^ b0

           compute for scenario 1:

               same using a1 and b1.

       add val_0 to sum_0 and val_1 to sum_1.

       store val_0 and val_1 in the dictionary for this variable.

   After all variables are processed, for this bit k:

       compare sum_0 and sum_1 to decide which choice (0 or 1) is better for min and max.

But how to track the variables' val_0 and val_1 for each bit?

Wait, for each variable, as we process them in order, we can store their val_0 and val_1 for the current bit. For each bit k, we need to process each variable again, as the values for the same variable can be different for different bits.

So, during processing each variable for a particular bit, the val_0 and val_1 are computed and stored in a temporary structure (like a dictionary) that's specific to that bit.

But since variables are processed in order, and each variable can only reference variables that came before it, the temporary dictionary can be built incrementally. For example, for variable i, when processing it, all variables before i have already been processed, so their val_0 and val_1 are in the dictionary.

Thus, for each bit k, the code would process each variable in order, compute their val_0 and val_1 based on the operands (which may be variables processed earlier), and accumulate the sum.

So, in code terms, for each bit k:

sum_0 = 0

sum_1 = 0

var_dict = {}  # maps variable name to (val0, val1)

for var in variables:

    if var is constant:

        bit = var.constant_value[k]

        val0 = (bit == '1')

        val1 = val0

    else:

        op1, op, op2 = var.operands

        # compute a0 and b0 (scenario 0)

        if op1 == '?':

            a0 = 0

        else:

            a0 = var_dict[op1][0]

        if op2 == '?':

            b0 = 0

        else:

            b0 = var_dict[op2][0]

        # compute operation for scenario 0

        if op == 'AND':

            res0 = a0 & b0

        elif op == 'OR':

            res0 = a0 | b0

        elif op == 'XOR':

            res0 = a0 ^ b0

        # scenario 1

        if op1 == '?':

            a1 = 1

        else:

            a1 = var_dict[op1][1]

        if op2 == '?':

            b1 = 1

        else:

            b1 = var_dict[op2][1]

        if op == 'AND':

            res1 = a1 & b1

        elif op == 'OR':

            res1 = a1 | b1

        elif op == 'XOR':

            res1 = a1 ^ b1

        val0 = res0

        val1 = res1

    sum_0 += val0

    sum_1 += val1

    var_dict[var.name] = (val0, val1)

So, after processing all variables, sum_0 and sum_1 are the sums for this bit when Peter's bit is 0 or 1.

This is the correct approach.

Now, in terms of code structure:

We can process each bit from 0 to m-1 (left to right). For each bit, process each variable, compute sum_0 and sum_1, and then decide the optimal bit for min and max.

The variables can be stored as a list of objects (or dictionaries) that indicate their type (constant or operation) and the necessary parameters.

So, in code:

First, parse the input variables.

Read n and m.

Then, read n lines. For each line:

Split into name, ':=', and the rest.

The rest is either a binary string (constant) or an operation.

So for each variable:

Store the name, and the type (constant or operation), and the details.

For example:

If the line is 'a := 101', then it's a constant with value '101'.

If the line is 'c := ? XOR b', then it's an operation where op1 is '?', op is 'XOR', op2 is 'b'.

So, variables can be represented as a list of dictionaries or objects.

Once variables are parsed, for each bit k in 0 to m-1:

Process the variables, track sum_0 and sum_1 for that bit.

Once we have sum_0 and sum_1 for each bit, we can decide for min and max.

Once all bits are processed, construct the binary strings for min and max cases.

Now, for each bit position k (from 0 to m-1, where 0 is the leftmost bit?), wait, the binary string is written as m bits. For example, in the first sample input, the variables are 3 bits. So the first character of the binary string is the most significant bit (bit 0?), and the last is the least significant (bit 2?).

Wait, the problem statement says "m-bit number". So, for example, the first sample input has m=3, and the variables are 3-bit numbers. So the bits are ordered from left (most significant) to right (least significant). For example, the first bit (position 0 in the string) is the highest order (value 2^(m-1 -0) = 2^2 =4). The next bit is position 1 (value 2^1=2), and position 2 (value 1).

So when processing each bit, the leftmost (position 0 in the binary string) contributes the most. So, when building the binary string for Peter's choice, the leftmost bit is the first character.

So, for each bit k (0-based, starting from the left), we need to decide whether to set it to 0 or 1 in the binary string.

In the code, when building the binary string for Peter's choice, the first character is the leftmost (most significant) bit, which corresponds to k=0.

Now, the code structure:

We need to process each of the m bits (from 0 to m-1, left to right), compute for each the sum_0 and sum_1, and then decide the optimal bit for min and max.

So, in code:

min_bits = []
max_bits = []

for k in 0 to m-1:

   compute sum_0 and sum_1 for bit k.

   for min case:

       if sum_0 < sum_1:

           choose 0

       elif sum_0 > sum_1:

           choose 1

       else:

           choose 0

       append '0' or '1' to min_bits.

   for max case:

       if sum_1 > sum_0:

           choose 1

       elif sum_1 < sum_0:

           choose 0

       else:

           choose 0

       append '0' or '1' to max_bits.

Once all bits are processed, combine the bits into strings.

So the code will generate two binary strings, min_bits and max_bits, which are the desired outputs.

But how to handle the order. For example, when k=0 is the leftmost bit (most significant), the code must build the strings in the correct order.

So, for each k from 0 to m-1 (inclusive), the bits are added to the list in order, then joined to form the binary string.

So, the code for processing each bit:

for each k in 0 to m-1:

   process variables and compute sum_0 and sum_1.

   decide min_bit and max_bit.

   append min_bit to min_bits list.

   append max_bit to max_bits list.

Finally, the min_bits and max_bits lists are joined into strings.

Now, the code in Python.

But how to represent the variables?

We can parse each variable as follows:

variables = []

for _ in range(n):

    line = input().split(' := ')

    name = line[0]

    expr = line[1]

    if expr[0] in '01':

        # it's a constant.

        variables.append( (name, 'constant', expr) )

    else:

        # it's an operation.

        op_parts = expr.split()

        op1 = op_parts[0]

        op = op_parts[1]

        op2 = op_parts[2]

        variables.append( (name, 'operation', op1, op, op2) )

Then, for each variable in variables, process in order.

But during processing each bit k, for each variable, we need to track val0 and val1.

So, for each bit k, we can create a dictionary (like var_dict) that maps variable names to their (val0, val1) for the current bit.

Thus, in code:

min_bits = []
max_bits = []

for k in range(m):

    var_dict = {}

    sum_0 = 0

    sum_1 = 0

    for var_info in variables:

        name = var_info[0]

        if var_info[1] == 'constant':

            binary_str = var_info[2]

            # get the k-th bit of the binary_str.

            # since binary_str is m bits, stored as a string, e.g., '101'

            # index 0 is leftmost (most significant).

            bit = binary_str[k]

            val0 = 1 if bit == '1' else 0

            val1 = val0  # same for both scenarios.

        else:

            # operation

            _, _, op1, op, op2 = var_info

            # compute for scenario 0 (Peter's bit is 0)

            # get a0 and b0

            a0 = 0 if op1 == '?' else var_dict[op1][0]

            b0 = 0 if op2 == '?' else var_dict[op2][0]

            # compute res0 based on op

            if op == 'AND':

                res0 = a0 & b0

            elif op == 'OR':

                res0 = a0 | b0

            elif op == 'XOR':

                res0 = a0 ^ b0

            # scenario 1 (Peter's bit is 1)

            a1 = 1 if op1 == '?' else var_dict[op1][1]

            b1 = 1 if op2 == '?' else var_dict[op2][1]

            if op == 'AND':

                res1 = a1 & b1

            elif op == 'OR':

                res1 = a1 | b1

            elif op == 'XOR':

                res1 = a1 ^ b1

            val0 = res0

            val1 = res1

        sum_0 += val0

        sum_1 += val1

        var_dict[name] = (val0, val1)

    # decide min and max bits.

    # for min:

    if sum_0 < sum_1:

        min_bit = '0'

    elif sum_0 > sum_1:

        min_bit = '1'

    else:

        min_bit = '0'

    min_bits.append(min_bit)

    # for max:

    if sum_1 > sum_0:

        max_bit = '1'

    elif sum_1 < sum_0:

        max_bit = '0'

    else:

        max_bit = '0'

    max_bits.append(max_bit)

Then, the min and max binary strings are the concatenation of min_bits and max_bits.

Finally, output ''.join(min_bits) and ''.join(max_bits).

Wait, but in the first sample input:

Variables:

a := 101 (bits 1,0,1)

b := 011 (bits 0,1,1)

c := ? XOR b.

For k=0 (the first bit):

Peter's bit can be 0 or 1.

For scenario 0 (Peter's bit 0):

c's first bit is 0 XOR b's first bit (0 XOR 0 (since b's first bit is 0 in the '011' string, which is bits 0:0, 1:1, 2:1. So for k=0, the first bit of b is 0. So c's first bit is 0 XOR 0 = 0.

sum_0 for bit 0 is a's first bit (1) + b's (0) + c's (0) → 1+0+0=1.

sum_1 for bit 0 when Peter's bit is 1: c's first bit is 1 XOR 0 (b's first bit is 0). So 1 XOR 0 is 1. sum is 1+0+1=2.

So for the first bit, sum_0 is 1 and sum_1 is 2. So for the min case, we choose 0 (sum_0 is smaller). For max, choose 1 (sum_1 is larger).

But in the sample output, the minimal number is 011, which in bits (k=0,1,2) is 0 1 1. For k=0 (first bit) it's 0.

Similarly for other bits.

Thus, the code should handle this correctly.

Another sample:

In the second sample:

Peter's choice doesn't affect the sum. So for all bits, sum_0 = sum_1 → choose 0 in both cases.

Thus, output is 0 for both min and max.

So the code seems correct.

Now, testing the code for the first sample.

Sample 1:

n=3, m=3.

variables:

a is '101' → bits 0:1, 1:0, 2:1.

b is '011' → bits 0:0, 1:1, 2:1.

c is ? XOR b.

For each bit k:

k=0 (leftmost):

sum_0: a's bit is 1, b's is 0, c's is 0 XOR 0 =0 → sum 1+0+0=1.

sum_1: a's 1, b's 0, c's 1 XOR 0=1 → sum 1+0+1=2.

so for min, choose 0. For max, choose 1.

k=1:

a's bit is 0, b's is 1.

c's operand is ? XOR b. For scenario 0 (Peter's bit 0):

0 XOR 1 = 1. sum_0: 0 +1 +1=2.

scenario 1: Peter's bit is 1 XOR 1 =0. sum_1: 0+1+0=1.

sum_0 (2) > sum_1 (1). So for min case, choose 1 (since sum_0 is larger, so choose scenario 1 → sum_1 is smaller. Wait, wait, for scenario 0 and 1 in this case, sum_0 is 2 (Peter's bit 0), sum_1 is 1 (Peter's bit 1). So for the min case, Peter's bit should be 1, leading to sum_1=1. So the code would see sum_0 (2) > sum_1 (1). So for the min case, choose 1 (since sum_1 is smaller).

But according to the code:

for min_bit:

if sum_0 < sum_1 → choose 0.

else if sum_0 > sum_1 → choose 1.

else 0.

sum_0 (2) > sum_1 (1), so choose 1 for min_bit.

Wait, but that's the opposite of what I thought. So the code will choose 1 for the min case here. Which leads to sum_1 (1), which is better.

Yes, that's correct.

So for k=1 (second bit), the code for min case would choose 1 (sum_1=1 is smaller than sum_0=2).

But in the sample output, the minimal Peter's number is 011, which in bits is 0 (k=0), 1 (k=1), 1 (k=2).

So for k=1, the code would choose 1.

Yes.

Similarly for the third bit (k=2):

a's bit is 1, b's is 1.

c's value for scenario 0 (Peter's bit 0): 0 XOR 1 = 1. sum_0: 1+1+1=3.

scenario 1: 1 XOR 1 =0. sum_1: 1+1+0=2.

sum_0 (3) > sum_1 (2). So for min case, choose 1 (sum_1 is smaller). So the bit is 1.

So the minimal Peter's number would be 0 (k=0), 1 (k=1), 1 (k=2) → 011, which matches the sample.

The code would generate this.

Yes, so the code is correct.

Now, the code in Python.

But for handling the variables, in each iteration of k, the code must process each variable in order, and for each, compute val0 and val1.

Now, possible optimizations:

- For variables that are constants, their val0 and val1 can be precomputed for all bits. But given that m can be up to 1000, and variables up to 5000, that's 5000 * 1000 = 5,000,000 entries. But for each variable and bit, the code can compute it once.

But in the current code, during processing each bit k, for a constant variable, the code is accessing the k-th bit of the binary string. So this is O(1) per access.

So for m=1000 and n=5000, the code's time is acceptable.

Now, the code needs to process each variable in order. For each variable, during each bit processing, it's checking if it's a constant or operation.

But for variables that are constants, the code can pre-process their binary strings into a list of integers (per bit) to avoid checking the string each time. For example, for a constant '101', precompute a list [1,0,1] for each bit. But even without that, accessing the string's character each time is O(1), so it's manageable.

But for code efficiency, perhaps precompute for all variables that are constants their bits as lists of integers.

But in Python, for code conciseness, perhaps we can process each bit by accessing the string directly.

So in code:

For a constant variable, binary_str is stored. Then, for each k in 0..m-1, binary_str[k] is checked.

But for m=1000, the binary string is of length m. So the code must ensure that all constants are exactly m bits. According to the input description, the binary numbers are exactly m bits, so the code can safely process them.

So, the code can proceed as follows.

Now, the code.

But in the code, the variables are stored as a list. For each variable in the list, during processing each bit, the code checks if it's a constant or operation.

Thus, in code:

n, m = map(int, input().split())

variables = []

for _ in range(n):

    parts = input().split(' := ')

    name = parts[0]

    expr = parts[1]

    if expr[0] in '01':

        # constant

        binary_str = expr

        variables.append( (name, 'constant', binary_str) )

    else:

        # operation

        op1, op, op2 = expr.split()

        variables.append( (name, 'operation', op1, op, op2) )

min_bits = []
max_bits = []

for k in range(m):

    var_dict = {}  # key: variable name, value: (val0, val1)

    sum0 = 0

    sum1 = 0

    for var in variables:

        name = var[0]

        if var[1] == 'constant':

            binary_str = var[2]

            bit = binary_str[k]

            val0 = 1 if (bit == '1') else 0

            val1 = val0

        else:

            # operation

            _, _, op1, op, op2 = var

            # scenario 0

            a0 = 0 if op1 == '?' else var_dict[op1][0]

            b0 = 0 if op2 == '?' else var_dict[op2][0]

            if op == 'AND':

                res0 = a0 & b0

            elif op == 'OR':

                res0 = a0 | b0

            else:  # XOR

                res0 = a0 ^ b0

            # scenario 1

            a1 = 1 if op1 == '?' else var_dict[op1][1]

            b1 = 1 if op2 == '?' else var_dict[op2][1]

            if op == 'AND':

                res1 = a1 & b1

            elif op == 'OR':

                res1 = a1 | b1

            else:  # XOR

                res1 = a1 ^ b1

            val0 = res0

            val1 = res1

        sum0 += val0

        sum1 += val1

        var_dict[name] = (val0, val1)

    # decide min and max bits for this position.

    # for min:

    if sum0 < sum1:

        min_bit = '0'

    elif sum0 > sum1:

        min_bit = '1'

    else:

        min_bit = '0'

    min_bits.append(min_bit)

    # for max:

    if sum1 > sum0:

        max_bit = '1'

    elif sum1 < sum0:

        max_bit = '0'

    else:

        max_bit = '0'

    max_bits.append(max_bit)

min_number = ''.join(min_bits)
max_number = ''.join(max_bits)

print(min_number)
print(max_number)

This should handle all cases.

Testing the first sample:

Sample input:

3 3

a := 101

b := 011

c := ? XOR b

For each bit:

k=0:

a is 1, b is 0.

c's scenario 0: 0 XOR 0 =0 → sum0=1+0+0=1.

scenario 1: 1 XOR 0=1 → sum1=1+0+1=2.

min_bit is 0 (sum0 is 1 < sum1 2).

max_bit is 1 (sum1 is 2> sum0 1).

k=1:

a's bit is 0, b's bit is 1.

c's scenario 0: 0 XOR 1 →1. sum0=0+1+1=2.

scenario 1: 1 XOR 1 →0. sum1=0+1+0=1.

sum0> sum1, so min_bit is 1 (sum1 is better), max_bit is 0.

k=2:

a's bit is 1, b's bit is 1.

c's scenario 0: 0 XOR 1 →1. sum0=1+1+1=3.

scenario 1: 1 XOR 1 →0. sum1=1+1+0=2.

sum0> sum1 → min_bit is 1 (sum1 is 2 < 3).

max_bit is 0.

Thus, min bits are [0,1,1] → '011'.

max bits are [1,0,0] → '100'.

Which matches the sample output.

Another test case:

Sample input 2:

5 1

a := 1

bb := 0

cx := ? OR a

d := ? XOR ?

e := d AND bb

Processing for k=0 (only bit):

sum0 and sum1:

Processing each variable:

a is '1' → val0=1, val1=1. sum0 +=1, sum1 +=1.

bb is '0' → val0=0, val1=0. sum0 +=0 (sum0=1), sum1 +=0 (sum1=1).

cx is ? OR a.

Scenario 0: a's val0 is 1. ? is 0. 0 OR 1 =1. → sum0 +=1 → sum0=2. val0=1.

Scenario 1: a's val1 is 1. ? is 1. 1 OR 1=1 → sum1 +=1 → sum1=2.

d is ? XOR ?.

Scenario 0: 0 XOR 0 =0. sum0 +=0 → sum0=2.

Scenario 1: 1 XOR 1=0. sum1 +=0 → sum1=2.

e is d AND bb.

Scenario 0: d's val0=0, bb's val0=0. 0 AND 0=0. sum0 +=0 → sum0=2.

Scenario 1: d's val1=0, bb's val1=0. 0 AND 0=0. sum1 +=0 → sum1=2.

So sum0=2, sum1=2.

So for both min and max, choose 0.

Thus, output is '0' for both.

Which matches the sample.

So the code works.

Thus, the code should handle all cases correctly.
</think>

```python
n, m = map(int, input().split())
variables = []
for _ in range(n):
    parts = input().split(' := ')
    name = parts[0]
    expr = parts[1]
    if expr[0] in '01':
        variables.append((name, 'constant', expr))
    else:
        op1, op, op2 = expr.split()
        variables.append((name, 'operation', op1, op, op2))

min_bits = []
max_bits = []

for k in range(m):
    var_dict = {}
    sum0 = 0
    sum1 = 0
    for var in variables:
        name = var[0]
        if var[1] == 'constant':
            binary_str = var[2]
            bit = binary_str[k]
            val0 = 1 if bit == '1' else 0
            val1 = val0
        else:
            _, _, op1, op, op2 = var
            a0 = 0 if op1 == '?' else var_dict[op1][0]
            b0 = 0 if op2 == '?' else var_dict[op2][0]
            if op == 'AND':
                res0 = a0 & b0
            elif op == 'OR':
                res0 = a0 | b0
            else:
                res0 = a0 ^ b0
            a1 = 1 if op1 == '?' else var_dict[op1][1]
            b1 = 1 if op2 == '?' else var_dict[op2][1]
            if op == 'AND':
                res1 = a1 & b1
            elif op == 'OR':
                res1 = a1 | b1
            else:
                res1 = a1 ^ b1
            val0, val1 = res0, res1
        sum0 += val0
        sum1 += val1
        var_dict[name] = (val0, val1)
    min_bit = '0' if sum0 <= sum1 else '1'
    max_bit = '1' if sum1 >= sum0 else '0'
    min_bits.append(min_bit)
    max_bits.append(max_bit)

print(''.join(min_bits))
print(''.join(max_bits))
```