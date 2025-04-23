<think>
Okay, let's try to understand this problem. So, we need to find the number of valid evolution plans, which are permutations of the types, such that when all Pokemons evolve according to the permutation, each gym's type counts remain the same as before. 

Hmm, the key here is that after applying the permutation f, for each gym, the count of each type must be the same as before. Wait, but how does that work? Because when you apply f, every type x in the gym is replaced by f(x). So, for each gym, the multiset of types must remain the same after permutation. Oh right, but for each gym, the counts of each type in the original gym must equal the counts of the new types after permutation. 

Wait, no. Let me think. Let's say in a gym, before evolution, there are a certain number of each type. After evolution, each type x is replaced by f(x). So for the gym, the count for type y after evolution is the sum of the counts of all x such that f(x) = y. But the protocol says that for each type in the gym, the count before and after must be the same. Wait, no, the problem statement says: "the number of Pokemon of that type before evolving any Pokemon should be equal the number of Pokemon of that type after evolving all the Pokemons according to the evolution plan." So for each gym, for each original type x, the count of x in the gym must equal the count of f(x) after evolution. Wait, no. Because after evolution, all x's become f(x), so the count of f(x) in the gym after evolution is the sum of all original counts of y where f(y) = f(x). Wait, maybe I'm getting this wrong.

Wait, for each gym, let's say before evolution, the count of type x is c_x. After evolution, the count of type y (in the gym) is the sum of c_x for all x such that f(x) = y. The protocol requires that for every type x, c_x (original count) must equal the count of f(x) in the gym after evolution. So for each gym, for each x, c_x (original) must equal the sum of c_{x'} where f(x') = f(x). Because after evolution, x' becomes f(x'), so the count of f(x) is sum_{x' : f(x') = f(x)} c_{x'}. 

But the protocol says that for each type x in the original gym, the original count c_x must equal the count of f(x) after evolution. So for all x, c_x = sum_{x' in f^{-1}(f(x))} c_{x'}. But since f is a permutation, each x' is mapped to a unique y. Wait, no: a permutation is a bijection, so each y is the image of exactly one x. So f is a permutation, which means that f is a bijective function. So for any y, there's exactly one x such that f(x) = y. Therefore, for the sum, sum_{x' where f(x')=y} c_{x'} would be c_{x'} where x' is the pre-image of y under f. So for each x, f(x) must be a type such that in every gym, the count of x in the original gym equals the count of f(x) in the original gym. Because after evolution, the count of f(x) would be the count of x's original count (since f is a permutation, x is the only type that maps to f(x)). 

Wait, that makes sense. Because f is a permutation, each y is the image of exactly one x. So after evolution, the count of y in the gym is equal to the original count of x, where x is f^{-1}(y). But the protocol says that for every original type x, the original count of x must equal the count of f(x) after evolution, which is the original count of x's pre-image under f. Wait, maybe I'm getting confused here. Let's rephrase.

Let’s consider a permutation f. For each gym, after applying f to all types, the count of each type y in the gym must be equal to the original count of x, where x is f^{-1}(y). But according to the protocol, this must equal the original count of x. Wait, no. The protocol states that in each gym, for every original type x, the count of x (original) must equal the count of f(x) (after evolution). So the count of f(x) after evolution is sum_{x' in f^{-1}(f(x))} c_{x'}, which is c_{x} because f is a permutation (so f^{-1}(f(x)) is just x). Therefore, in this case, the sum would be c_x. So the protocol's condition is that c_x (original) must equal the count of f(x) after evolution, which is c_x. So that condition is automatically satisfied. Wait, that can't be right. What's the problem here?

Wait, no. If f is a permutation, then for each y in the new types, the count of y in a gym after evolution is the count of x where f(x) = y. But since f is a permutation, for each y, there is exactly one x such that f(x) = y. So the count of y after evolution is the original count of x. Then the protocol requires that for each original type x, the count of x in the original gym must equal the count of f(x) in the evolved gym. But the count of f(x) after evolution is the original count of x. So the condition becomes, for every original x in every gym, original count x == original count x. Which is always true. So that would imply that any permutation is allowed. But the first sample input shows that this isn't the case. So my reasoning must be wrong.

Wait, no. Wait the first sample input:

Sample input 1:
2 3
2 1 2
2 2 3

Sample output 1: 1.

So according to that, the only valid permutation is the identity. But according to my previous reasoning, any permutation would satisfy the condition. So there's a mistake here.

Ah! Wait, maybe I misunderstood the protocol. Let me re-read the problem statement.

The problem says: 

"the protocol of the mountain states that in each gym, for every type of Pokemon, the number of Pokemon of that type before evolving any Pokemon should be equal the number of Pokemon of that type after evolving all the Pokemons according to the evolution plan."

Wait, the wording here is slightly ambiguous. Does "that type" refer to the same type before and after? Or, in other words, for each type x (original), the count of x in the gym before evolution must equal the count of x after evolution. Or is it that for each type x, the count before of x must equal the count after of f(x)? Or is it that for each type y (after evolution), the count of y in the gym after evolution must equal the count of the original type x where f(x) = y (i.e., the count of x before)?

No. The problem says: for every type of Pokemon (original, I think), the count before equals the count after of that type. Wait, no. Let me parse this sentence again.

"... for every type of Pokemon, the number of Pokemon of that type before evolving any Pokemon should be equal the number of Pokemon of that type after evolving all the Pokemons according to the evolution plan."

So, for each type x (original), the count of x before is equal to the count of x after evolution. But after evolution, the type x may have changed. So this seems to require that for each type x, the count of x in the gym before equals the count of x in the gym after. But that's not possible unless f(x) = x for all x, which is only possible if the permutation is the identity. But the sample input 2 has a valid answer of 6, which is 3! permutations. So clearly, my understanding is wrong.

Ah, maybe I've misinterpreted the problem. Let's re-read the problem statement.

The problem statement says: 

"the number of Pokemon of that type before evolving any Pokemon should be equal the number of Pokemon of that type after evolving all the Pokemons according to the evolution plan."

So, for each type y (after evolution), the count of y in the gym after evolution must equal the count of y in the gym before evolution. Wait, that makes more sense. Because after evolution, the types have changed. So, for example, suppose a gym had two type 1 Pokemons. If in the evolution plan, type 1 evolves to type 2, then after evolution, the gym has two type 2 Pokemons. So the original count of type 1 was 2, but the count after of type 1 is zero, which would not be equal. So this would not satisfy the protocol unless f(y) = y for all y. But sample input 2 has the output 6, which suggests that all permutations are allowed. 

Wait, sample input 2 is:

1 3
3 1 2 3

The output is 6, which is 3! So all permutations are allowed. But according to the protocol, after evolution, each type's count in the gym must equal its original count. Wait, after permutation, the counts of the types are permuted. For example, if the permutation f is (1→2, 2→3, 3→1), then after evolution, the gym has 3 Pokemons of types 2,3,1. So the counts for each type in the gym after would be: type 1: 1, type 2: 1, type3:1. But the original counts were 3, each type appearing once. So in this case, after evolution, the counts are the same as before: each type (1,2,3) has exactly 1 count. So the protocol is satisfied. 

Ah! So the protocol is not requiring that each original type's count equals its own count after evolution. Instead, the protocol is requiring that for each type y (as in the types after evolution), the count of y after evolution must equal the count of y before evolution. So, for example, if after evolution, there are two type 2 Pokemons in the gym, then in the original gym, there must have been two type x Pokemons where x is the type that evolves into 2. But since f is a permutation, the original x must be f^{-1}(2). 

Wait, perhaps another way to look at this: For the evolution plan f to be valid, for every gym, the multiset of types after evolution must be the same as the multiset before. Because each type x in the original is mapped to f(x) in the new. So the multiset after is {f(x1), f(x2), ..., f(xg)} where x1..xg are the original types. The protocol requires that for each type y, the number of times y appears in the original multiset is equal to the number of times y appears in the evolved multiset. Wait, no. Because in the original gym, the count of y is the original count, and after evolution, the count of y is the number of x's that map to y (since each x becomes f(x)). So the protocol requires that for each y, the original count of y is equal to the number of x's that map to y multiplied by their original counts? No, that's not right. 

Wait, for each gym, the original count of each type x is c_x. After evolution, the count of type y is sum_{x in f^{-1}(y)} c_x. The protocol requires that this sum must be equal to the original count of y in the gym, for all y. So for each gym, and for each type y, sum_{x where f(x) = y} c_x (original) must equal the original count of y in the gym. 

So the permutation f must be such that for each gym and for each type y, the sum of the original counts of all x that map to y in the permutation must equal the original count of y in that gym. 

Wait, that's a critical point. Let's restate the condition: For each gym, for every type y, the sum of the original counts of all x in the gym where f(x) = y must equal the original count of y in that gym. 

So, for example, if in a gym, y=2 has a count of 3, then for the permutation f, all x that map to y=2 must have their original counts in the gym sum to 3. 

But this must hold for all gyms. So the permutation f must group together types x that, in every gym, their counts sum up to the count of y. 

So, the problem reduces to finding permutations f where, for every x, f(x) is such that, in every gym, the sum of the counts of all types in the equivalence class (those that map to the same y) must equal the count of y in each gym. 

Wait, perhaps the way to model this is that the permutation f must group types into equivalence classes where, for each class, the counts of each type in the class, across all gyms, must be the same as the counts of the target type. Wait, this is getting complicated.

Alternatively, for the permutation f to be valid, the multiset of types in each gym must be invariant under permutation f. That is, for each gym, when you apply f to each type in the gym, the multiset remains the same. Because the protocol requires that for each type y, the count after evolution (which is the number of x's in the original that map to y) equals the original count of y. So, the multiset after evolution is exactly the same as the original. 

Wait, no. Because after evolution, the multiset is {f(x1), f(x2), ..., f(xg)}. The protocol requires that for each y in the new multiset, the count of y in this new multiset must equal the count of y in the original. So the new multiset is a permutation of the original multiset. Therefore, the multiset after evolution must be the same as the original. So, applying f to each element of the original multiset must result in the same multiset. So, the permutation f must permute the multiset elements such that the result is identical to the original. 

In other words, for each gym, when you apply f to all types in the gym, the multiset must remain the same. So, for each gym, f must be an automorphism of the multiset of types in that gym. 

But since the permutation is applied globally (same for all gyms), the permutation f must be such that for every gym, f is an automorphism of the gym's multiset. 

So, the valid permutations are those that are automorphisms for all gyms' multisets. 

The total number of such permutations is the product over each type's group of possible permutations, but considering the constraints across all gyms. 

But how to model this? 

Let me think of the constraints. For a permutation f to be valid, for each gym's multiset, applying f must leave the multiset unchanged. So for each x in the multiset, f(x) must be another element in the multiset with the same count. 

But for the permutation to work across all gyms, the permutation must be such that for any type x, all occurrences of x in any gym must be mapped to a type y such that in every gym where x appears, y has the same count as x in that gym. 

Wait, perhaps we can model the types into equivalence classes where, for any two types x and y in the same class, in every gym, the count of x is equal to the count of y. 

Because then, a permutation can permute within these equivalence classes. 

Because if two types x and y have the same count in every gym, then swapping them in the permutation would not affect the counts after evolution. 

For example, if in every gym, the count of x and y are the same, then swapping x and y in the permutation would result in the same counts in each gym. 

So, the valid permutations are those that permute types within their equivalence classes, where the equivalence classes are defined as groups of types that have identical count vectors across all gyms. 

So the approach is:

1. For each type x, compute the vector of counts across all gyms. For example, type x's vector is (count_in_gym_1, count_in_gym_2, ..., count_in_gym_n). 

2. Two types x and y are in the same group if and only if their vectors are identical. 

3. Then, the valid permutations are those that permute the types within each group. 

Because for any permutation that maps a type x to another type y in the same group, the count vectors of x and y are identical in all gyms. So when you apply the permutation, the sum of counts for each group in each gym will remain the same. 

Thus, the number of valid permutations is the product of the factorials of the sizes of each group. 

For example, if there are k groups, each of size s_1, s_2, ..., s_k, then the answer is s_1! * s_2! * ... * s_k! mod (1e9+7). 

Yes! Because for each group, you can permute the types in any order within the group. Since each type in the group has the same count vector, permuting them within the group will not change the sum of counts for each y in any gym. 

So the steps are:

- For each type (from 1 to m), compute the count in each gym. 

- For each type, create a tuple (count_gym_1, count_gym_2, ..., count_gym_n). 

- Group types by their tuples. 

- For each group with size s, multiply the result by s! (mod 1e9+7). 

This matches the sample inputs. 

Let's check sample input 1:

Sample 1:

n=2, m=3. 

Gyms:

Gym 1: 2 1 2 → counts are 1 for 1, 1 for 2, 0 for 3. 

Gym 2: 2 2 3 → counts are 0 for 1, 1 for 2, 1 for 3. 

So each type's count vector:

Type 1: (1, 0)

Type 2: (1, 1)

Type 3: (0, 1)

Each has a unique vector. So all groups are size 1. The product is 1! *1! *1! =1, which matches the sample. 

Sample 2:

n=1, m=3. 

Gym 1 has 3 Pokemons: 1, 2, 3. So counts are 1 for each type. 

So each type's vector is (1). So all three types are in the same group. So 3! =6. 

Sample 3:

n=2, m=4. 

Gym 1: 2 1 2 → counts for 1:1, 2:1; 3:0, 4:0. 

Gym 2:3 2 3 4 → counts for 2:1, 3:1,4:1; 1:0. 

So the count vectors are:

Type1: (1,0)

Type2: (1,1)

Type3: (0,1)

Type4: (0,1)

So groups:

Type1: group size 1.

Type2: group size 1.

Types3 and 4: group size 2. 

So the product is 1! *1! * 2! =2. Which matches sample 3. 

Sample4:

n=2, m=2. 

Gym1:3 2 2 1 → counts for 1:1, 2:2. 

Gym2:2 1 2 → counts for 1:1, 2:1. 

So the count vectors:

Type1: (1,1)

Type2: (2,1)

These are distinct. So each group has size 1. The product is 1! *1! =1. Which matches sample4. 

Sample5:

3 7

Gyms:

2 1 2 → counts for 1:1, 2:1; others 0. 

2 3 4 → counts for 3:1,4:1; others 0. 

3 5 6 7 → counts for 5:1,6:1,7:1; others 0. 

So the count vectors:

Type1: (1,0,0)

Type2: (1,0,0)

Type3: (0,1,0)

Type4: (0,1,0)

Type5: (0,0,1)

Type6: (0,0,1)

Type7: (0,0,1)

So groups:

Type1 and 2: size 2.

Types3 and4: size 2.

Types5,6,7: size3. 

So the product is 2! *2! *3! = 2*2*6=24. Which matches sample5. 

So this approach is correct. 

Now, the challenge is to compute the count vector for each type efficiently. 

Constraints:

n up to 1e5, m up to 1e6. Sum of all gi is up to 5e5. 

For each gym, we can process each type in it, and for each type, increment the count for that gym. 

But how to represent the count vector for a type? For example, for m=1e6 types and n=1e5 gyms, storing a list of n counts per type is impossible due to memory. 

But in the problem, for each gym, most types are not present. So for a type x, the count in gym i is 0 if the gym does not contain x. 

So, for each type x, the count vector is a sparse representation: a dictionary where keys are gym indices (from 0 to n-1) where the type x has a non-zero count, and the value is the count. 

But when comparing two types x and y, their count vectors (sparse or not) must be identical in all gyms, including those where the count is zero. 

Wait, no. Because the count vector is all the counts in all gyms. For example, if type x has count 0 in gym 5, but type y has count 0 in gym 5 as well. So their count vectors are the same. But if in another gym, say gym 10, x has count 3 and y has count 3, but in gym 15, x has 0 and y has 0. Then their count vectors are the same. 

But for a type x, the count in gym i is 0 if it's not present. So, the problem is that for types that are not present in any gym, their count vectors would be all zeros. 

Wait, but the problem allows m up to 1e6. So even if a type is not present in any gym, its count vector is all zeros. So such types would form a group. 

But in the problem's examples, all types are present in at least one gym, but perhaps in the actual test cases, there are types with count vectors of all zeros. 

So the approach is:

For each type from 1 to m, compute the count in each gym. However, storing this as a full array (size n) is impossible for m=1e6 and n=1e5. 

But in practice, for each type x, most gyms have 0 count. So for each type x, we can store a dictionary (or a sorted list) of gym indices where the count is non-zero. Then, two types x and y have the same count vectors if and only if, for all gyms, their counts are equal. 

But comparing two types x and y's count vectors would require comparing their non-zero counts in each gym, and ensuring that in all other gyms (where they have zero counts), the other type also has zero. 

But how to do this efficiently? 

Alternative approach:

For each type x, represent its count vector as a tuple of (gym_index, count) pairs, sorted by gym index, and including all gyms where count is non-zero. Then, to compare two types x and y, their sorted lists of (gym, count) must be identical. 

But this would work, but for types with a lot of non-zero counts, this could be time-consuming. 

Another way: For each type x, create a hashable representation of its count vector. For example, a tuple of (gym indices sorted, with their counts), but even better, a hash that uniquely represents the count vector. 

But how to compute this hash efficiently. 

Wait, but for each type x, the count vector is a list of counts for each gym. Since n can be 1e5, but m is 1e6, and sum of all gi is 5e5, the average number of gyms per type is (sum of gi) / m = 5e5 / 1e6 = 0.5. So for most types, they are not present in any gym. 

So for each gym, we can process the types present in it, and for each such type, increment the count for that gym. 

So the steps to process the input:

1. Initialize for each type x, a dictionary (defaultdict) that maps gym indices to counts. 

But for m=1e6, creating a dictionary for each type is possible, but perhaps memory-intensive. 

Alternative approach: For each gym, process its Pokemons, and for each type in the gym, increment the count for that type in the gym. 

We can represent the count vectors as a list of dictionaries, where for each type x, counts[x] is a dictionary mapping gym index to count. 

But again, for m=1e6, this is problematic. 

Alternative approach: 

We can create a global dictionary, where the keys are types (x), and the value is a dictionary that maps gym indices to counts. 

But how to build this efficiently. 

Let me think. 

For each gym i (from 0 to n-1):

   Read gi numbers, which are the types in the gym. 

   For each type x in the gym, we need to count how many times x appears in this gym. 

So, for gym i, create a frequency dictionary (using collections.Counter), then for each x in the gym's list, increment the count for x in the gym. 

Then, for each type x in the gym's frequency dictionary, we add the entry (i, count) to the type's count vector. 

But for types not present in any gym, their count vectors are all zeros, which can be represented as an empty dictionary. 

But when comparing two types x and y, we need to compare their count vectors across all gyms, including those where they have zero counts. 

So, for two types x and y to be in the same group, their count dictionaries must be identical. That is, for all gyms i, x's count in i is equal to y's count in i. 

But how to represent this. 

But how to compare x and y's count vectors? For example, x has a count of 3 in gym 5, and y has a count of 3 in gym 5, and in all other gyms, they have zero. So their count vectors are the same. 

But for a type x that is present in some gyms and not others, the count vector is represented by the set of gyms where it has a non-zero count. 

So, two types x and y are in the same group if and only if:

- For every gym i where x has a non-zero count, y has the same count in that gym. 

- For every gym i where y has a non-zero count, x has the same count in that gym. 

Which is equivalent to their count dictionaries being the same. 

So, for each type x, the count dictionary is a set of (gym i, count). 

So, the hashable representation for the count vector can be the tuple of sorted (gym i, count) pairs. 

So, for type x, we can create a tuple of sorted (i, cnt) pairs, sorted by gym index, which represents its count vector. 

Then, two types x and y are in the same group if their tuples are equal. 

Thus, the steps are:

1. Read all gyms, and for each type x, collect the gyms and counts where it is present. 

2. For each type x, create a sorted tuple of (gym index, count) pairs. 

3. For all types x, group them by their sorted tuples. 

4. The answer is the product of (size of each group)! modulo 1e9+7. 

Now, the problem is to compute this efficiently, given the constraints. 

The main challenge is to handle the case where m is up to 1e6, but the sum of all gi is up to 5e5. 

So, the number of types that appear in at least one gym is up to 5e5. The rest of the types (up to 1e6) would have zero count in all gyms. 

So, for all types that are not present in any gym, their count vectors are all zeros. So all of them are in the same group. 

So, the group for all-zero count vectors would have size (m - number of types present in any gym). 

So, the steps are:

- For each type present in any gym, compute the tuple and group them. 

- Then, handle the types not present in any gym (count vector is all zeros) as a single group. 

So, let's process the input:

Initialize a dictionary, count_vectors, which maps a tuple (the sorted (i, count) pairs) to the number of types in that group. 

Then, after processing all gyms, we need to add the number of types that have zero count vectors. 

So:

For each gym i in 0..n-1:

   Read the list of types in the gym. 

   Use Counter to count the occurrences of each type in the gym. 

   For each type x in the Counter:

       Append (i, count) to x's list. 

Then, for each type x present in any gym:

   Sort the list of (i, count) by gym index. 

   Convert it to a tuple and use it as a key in count_vectors. 

After processing all present types, check how many types were not present (m_total = m, so m - len(present_types)). 

If there are k such types (all-zero count vectors), add a key of an empty tuple with count k. 

Then, compute the product of factorials of all group sizes. 

Now, the code needs to handle this efficiently. 

In Python, using a defaultdict to track the count for each type. But for m up to 1e6, but sum of gi up to 5e5, the number of types present is up to 5e5. 

So, in code:

Read n and m. 

Then, for each gym in n gyms:

   Read the gi and the list of types. 

   Create a frequency dictionary (Counter) for the types. 

   For each (x, cnt) in the Counter:

       Append (gym_index, cnt) to x's list. 

Then, for each x in the frequency dictionaries (collected across all gyms):

   Sort the list of (gym_index, cnt) by gym_index. 

   Convert to a tuple, which is the key. 

   Use a defaultdict(int) to count the frequency of each key. 

Then, the number of types not present in any gym is (m - the total number of types that were present in any gym). 

If this number is greater than zero, then add a group for them with size (m - num_present). 

Finally, compute the product of factorials of all group sizes. 

But how to collect all the types present. 

Wait, in the code, when processing each gym's types, for each x in that gym, we process it. So, to collect all x's that have appeared in any gym, we can use a set. 

But for m=1e6, this is manageable. 

Wait, but in Python, if we have a defaultdict for each x's list, but only those x's that appear in any gym will have entries. 

So, the code steps:

Initialize a dictionary, say, type_counts = defaultdict(list). 

For each gym index i in 0..n-1:

   Read the line, split into gi and the gi types. 

   cntr = Counter(types) 

   for x, c in cntr.items():

       type_counts[x].append( (i, c) )

Once all gyms are processed, for each x in type_counts, we sort the list of (i, c) pairs by i, then create a tuple as the key. 

Then, the group counts are handled as follows:

count_vectors = defaultdict(int)

present_types = 0

for x in type_counts:

    vec = tuple(sorted(type_counts[x], key=lambda t: t[0]))

    count_vectors[vec] += 1

    present_types += 1

Then, the number of types not present is m - present_types. 

If that number is positive:

   count_vectors[ () ] += (m - present_types)

Then, compute the product of factorials of the values in count_vectors. 

But how to compute factorials up to m (which can be 1e6) modulo 1e9+7. 

So, precompute factorials modulo MOD up to 1e6. 

MOD = 1e9 +7 

precompute fact = [1]*(max_fact+1)

for i in 2 to max_fact:

   fact[i] = fact[i-1] *i % MOD 

But since the maximum group size can be up to m (for the all-zero types group, which can be up to 1e6). 

So, precompute factorial up to 1e6. 

But in Python, precomputing factorial up to 1e6 is manageable. 

So, code outline:

precompute fact array. 

Read n and m. 

process all gyms, build type_counts. 

build count_vectors. 

add the missing types to count_vectors if necessary. 

compute the product of fact[s] for all s in count_vectors.values(). 

Output the product mod MOD. 

Now, let's test this with sample input 1. 

Sample 1:

n=2, m=3. 

Gym 0: 2 1 2 → Counter {1:1, 2:1}

Gym 1: 2 2 3 → Counter {2:1, 3:1}

type_counts:

1: [(0,1)]

2: [(0,1), (1,1)]

3: [(1,1)]

For each x:

x=1: sorted list is [(0,1)] → tuple key. 

x=2: sorted list is [(0,1), (1,1)] → key is ((0,1), (1,1)). 

x=3: sorted list is [(1,1)] → key is ((1,1)). 

So count_vectors has:

key ((0,1)) → count 1 (type 1)

key ((0,1), (1,1)) → count 1 (type2)

key ((1,1)) → count 1 (type3)

present_types =3. 

m=3, so missing types is 0. 

product is 1*1*1 =1. 

Sample2:

n=1, m=3. 

Gym0:3 1,2,3 → Counter {1:1, 2:1,3:1}

type_counts:

1: [(0,1)]

2: [(0,1)]

3: [(0,1)]

Each x's list is [(0,1)], so sorted tuple is same. 

So count_vectors for the key ((0,1)) is 3. 

present_types=3. 

m=3, so missing is 0. 

3! =6. 

Sample3:

n=2, m=4. 

Gym0: 2 1 2 → types 1 and 2 → counts 1 each. 

Gym1:3 2 3 4 → types 2,3,4. Counts 1 each. 

So type_counts:

1: [(0,1)]

2: [(0,1), (1,1)]

3: [(1,1)]

4: [(1,1)]

type3 and 4 have the same sorted tuple [(1,1)], so their group is 2. 

So count_vectors:

((0,1)) →1

((0,1), (1,1)) →1

((1,1)) →2. 

product is 1*1*2! =2. 

Sample5:

types 1 and 2: their lists are [(0,1)] (gym0) and [(0,1)] (gym0). Wait no:

Wait, in sample5:

n=3 gyms. 

Gym0: 2 1 2 → counts 1:1, 2:1. 

Gym1:2 3 4 → counts3:1,4:1. 

Gym2:3 5 6 7 → counts5:1,6:1,7:1. 

So:

type1: [(0,1)]

type2: [(0,1)]

type3: [(1,1)]

type4: [(1,1)]

types5,6,7: each [(2,1)].

So the tuples are:

type1: [(0,1)] 

type2: [(0,1)] 

so same key → group size 2. 

types3 and4: same key [(1,1)] → group size 2. 

types5,6,7: same key [(2,1)] → group size 3. 

So product is 2! *2! *3! =2*2*6=24. 

Thus, the code works. 

Now, the code must be implemented efficiently. 

In Python, using a defaultdict to track type_counts is manageable. 

But for m up to 1e6 and sum of gi up to 5e5, the number of types present in any gym is up to 5e5. 

The precomputation of factorials up to 1e6 is possible. 

But what if m is 1e6 and all types are present once, leading to group sizes of 1 each. Then the product is 1^1e6 =1, but the code would compute that. 

Now, code steps:

1. Precompute factorials mod 1e9+7 up to 1e6. 

2. Read n and m. 

3. Read n gyms. For each gym, count the types present. 

4. For each type present in any gym, collect the list of (gym index, count). 

5. For each such type, sort the list and use as a key in a dictionary. 

6. Compute the count of each key. 

7. Add the missing types (those with zero counts in all gyms) as a single group. 

8. Multiply the factorials of all group sizes. 

Now, in Python, when building the type_counts, using a defaultdict(list) to collect the gym and count for each type. 

But for each gym, the code must process the types, count their occurrences, and for each, append (gym index, count) to the type's list. 

But for efficiency, perhaps using a list to collect the counts for each type. 

But let's see:

In code:

Testing against sample inputs 1, 4.

```python
from collections import defaultdict, Counter


def main(input_stream, output_stream):
    MOD = 10**9 +7

    max_fact = 10**6  # since m can be up to 1e6

    fact = [1]*(max_fact+1)

    for i in range(2, max_fact+1):

        fact[i] = fact[i-1] *i % MOD

    n, m = map(int, input_stream.readline().rstrip("\n").split())

    type_counts = defaultdict(list)

    present_types = set()

    for gym_idx in range(n):

        parts = list(map(int, input_stream.readline().rstrip("\n").split()))

        gi = parts[0]

        types = parts[1:]

        cntr = Counter(types)

        for x, c in cntr.items():

            type_counts[x].append( (gym_idx, c) )

        present_types.update(types)

    # Now, process the type_counts into groups

    count_vectors = defaultdict(int)

    for x in type_counts:

        # sort the list by gym index

        vec = tuple(sorted(type_counts[x], key=lambda t: t[0]))

        count_vectors[vec] +=1

    # handle the missing types

    num_missing = m - len(present_types)

    if num_missing >0:

        count_vectors[ () ] += num_missing

    # compute the product

    result = 1

    for s in count_vectors.values():

        result = result * fact[s] % MOD

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 3
3 1 2 3
""",
            "output": \
"""\
6
""",
        }, 
        {
            "input": \
"""\
3 7
2 1 2
2 3 4
3 5 6 7
""",
            "output": \
"""\
24
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

But let's test another sample. 

Sample input 4:

n=2, m=2. 

Gym1:3 2 2 1 → types 2,2,1. 

Gym2:2 1 2. 

present_types is {1,2}, len is 2. m=2. So num_missing is 0. 

Thus, the code proceeds. 

The types 1 and 2's count vectors are:

For type1: in gym0 (gym_idx 0?), count is 1. In gym1, count is1. 

type1's vector is [(0,1), (1,1)]? 

Wait, the code uses gym indices starting from 0. 

Wait, in code, for gym_idx in range(n):

so the first gym is 0, second is 1, etc. 

In sample4:

gym0: types 2,2,1. 

so type_counts for 1: [(0,1)]

type_counts for 2: [(0,2)]

gym1: types 1, 2. 

type_counts for 1: [(0,1), (1,1)]

type_counts for 2: [(0,2), (1,1)]

so for type1: list is [(0,1), (1,1)]. sorted → same as type1's list. 

type2's list is [(0,2), (1,1)]. 

So their count vectors are different. 

Thus, groups are 1 and 1. So product is 1. 

Which matches sample4. 

Thus, the code is correct. 

So this should be the correct approach.
</think>

```python
from collections import defaultdict, Counter

MOD = 10**9 + 7

# Precompute factorials up to 1e6 modulo MOD
max_fact = 10**6
fact = [1] * (max_fact + 1)
for i in range(2, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

n, m = map(int, input().split())

type_counts = defaultdict(list)
present_types = set()

for gym_idx in range(n):
    parts = list(map(int, input().split()))
    gi = parts[0]
    types = parts[1:]
    cntr = Counter(types)
    for x, c in cntr.items():
        type_counts[x].append((gym_idx, c))
    present_types.update(types)

count_vectors = defaultdict(int)
for x in type_counts:
    sorted_vec = tuple(sorted(type_counts[x], key=lambda t: t[0]))
    count_vectors[sorted_vec] += 1

# Handle types not present in any gym
num_missing = m - len(present_types)
if num_missing > 0:
    count_vectors[()] += num_missing

result = 1
for s in count_vectors.values():
    result = result * fact[s] % MOD

print(result)
```
