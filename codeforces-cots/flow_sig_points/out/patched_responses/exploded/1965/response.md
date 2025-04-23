<think>
Okay, let's see. We need to determine if there's a way to assign positive integers to the stores such that for every day, the LCM of Dora's chosen stores is strictly greater than the LCM of Swiper's stores (which are all the stores not chosen by Dora that day).

Hmm. The problem is to check the existence of such a_i values. So, we don't have to find them, just check if possible.

First, let's think about what conditions must be satisfied. For each day, the LCM of Dora's set must be > LCM of Swiper's set. But how can we model this?

An approach might be to model the problem as constraints on the primes in each a_i. But that's probably too vague. Alternatively, maybe we can model this using a bipartition of primes. Wait, perhaps there's a way to assign primes such that Dora's set has a higher product. But LCM is not the product. However, if all primes are unique in Dora's set, then LCM would be their product. But if Swiper's set includes any primes, their LCM would be the product of their primes. So maybe we can assign primes in a way that Dora's stores have primes not present in Swiper's stores, and vice versa. But how?

Alternatively, perhaps the problem can be transformed into a graph where each store is a node, and edges represent constraints. Wait, maybe each day imposes certain constraints on the a_i's. Let's think: For each day i, Dora's set S_i and Swiper's set T_i (which is the complement of S_i). The LCM(S_i) must be > LCM(T_i). How can we ensure this?

Let's think about the LCM. The LCM of a set is the product of the primes in their maximum exponents present in the set. So, for example, if a set has numbers with primes 2^3, 3^2, then the LCM is 2^3 *3^2. So the LCM is determined by the maximum exponents of each prime in the set.

So, for the LCM of S_i to be greater than that of T_i, it's necessary that there's at least one prime where the maximum exponent in S_i is higher than the maximum in T_i. But wait, maybe not. Because even if all primes in S_i are present in T_i, but arranged in such a way that their exponents in S_i's LCM are higher.

Alternatively, perhaps we can model this as follows: For each day, the LCM of S_i must be greater than that of T_i. How can we arrange the a_i's to satisfy this?

An alternative approach is to model this as a bipartite graph problem. Each store can be assigned a prime number, but maybe not. Or perhaps, for each day, the set S_i must contain a prime that is not present in T_i. Because if S_i has a prime that T_i doesn't, then the LCM of S_i will have that prime, while T_i's LCM will not, making S_i's LCM larger. Conversely, if T_i has a prime not present in S_i, then S_i's LCM can't include that, which would make their LCM smaller. So perhaps the key is to ensure that for each day, S_i contains at least one prime that is not present in T_i (i.e., S_i has a prime not in T_i). But wait, that's not sufficient. Because suppose S_i has a prime p, and T_i has a prime q. Then, the LCM of S is p, and of T is q. If p is larger than q, then S's LCM is larger. But if q is larger than p, then no. So this approach may not work directly.

Alternatively, perhaps the problem can be transformed into a set cover problem. For each day, we need that S_i has at least one unique prime not present in T_i (i.e., in the other stores). But T_i is all the other stores not in S_i. So for S_i, if there exists a store in S_i that has a prime that is not present in any of the T_i (which is the same as not present in any store not in S_i). So that prime is present only in S_i's stores. Then, the LCM of S_i will have that prime, while the LCM of T_i will not, so S_i's LCM is larger.

So, if for each day i, there exists at least one store in S_i that is assigned a unique prime that's not present in any of the other stores (i.e., stores not in S_i). Then, for each day, the LCM of S_i would include that prime, making it larger than T_i's LCM (since T_i can't have that prime). 

But how can we assign such primes? Each day's S_i must have at least one store with a unique prime not present in any other store. But each such prime can only be used once. Because if two days require their S_i to have a unique prime, but those primes are in different stores, then that's possible. But each store can have multiple primes, but perhaps for the purpose of the LCM, the primes in the store's a_i contribute to the LCM.

Wait, but if a store's a_i has multiple primes, then those primes are part of its factors. So, for example, if a store is assigned 6 (2*3), then it contributes primes 2 and 3. 

But in order for a day's S_i to have a prime that's not present in T_i, that prime must be present in at least one store in S_i and in none of the stores in T_i. So, for all stores not in S_i (i.e., in T_i), their a_i's must not have that prime. So the prime must be exclusive to the S_i's stores.

So, for each day i, there must exist at least one prime that is present in S_i's stores and not present in any of T_i's stores. That way, the LCM of S_i will have that prime, and the LCM of T_i will not, making S_i's LCM larger.

So the problem reduces to: can we assign primes to the stores such that for each day i, there's a prime that's in at least one store in S_i and in no stores outside S_i.

If this is possible, then the answer is possible. Otherwise, impossible.

So the problem is equivalent to: for each day i, the set S_i must not be entirely covered by the union of other days' S_j sets. Wait, perhaps not. Let me think.

Alternatively, each day i must have a store in S_i that is not present in any other day's T_j. Wait, because the T_j of other days would be their own complements. Hmm, maybe not.

Alternatively, for each day i, there exists a store x in S_i such that x is not present in any other day's T_j. Wait, because T_j is the complement of S_j. So if x is not present in any other S_j (since if x is not in T_j, then x is in S_j). So for x to be in S_i and not present in any other T_j, x must be in S_i and in all other S_j's T_j's complements, i.e., x is not in any S_j for j != i. Because T_j is the complement of S_j, so if x is in T_j, then x is not in S_j. So x is in S_i but not in any S_j (for j != i), which would mean that x is only in S_i.

Therefore, if there exists a store x that is only in S_i and no other S_j, then x can be assigned a unique prime. So in this case, for day i, the LCM of S_i would include that prime, and the LCM of T_i would not, making it possible.

So the problem reduces to: for each day i, there exists at least one store x that is present only in S_i (i.e., x is not present in any S_j for j != i). If this is true, then we can assign each such x a unique prime, and that would ensure that each day's S_i's LCM is larger than T_i's.

But in cases where a store x appears in multiple S_i's, then that x can't be used as a unique prime for those days. So those days must have another store that is unique to them.

So the problem becomes: can we find for each day i, a store that is unique to S_i (i.e., only appears in S_i), then assign each such store a unique prime, and for the other stores, assign 1. Then, for each day i, the LCM of S_i is the product of primes from the unique stores in S_i. Since T_i (the complement) doesn't include any of S_i's unique stores (since they are not in any other S_j, which are the days j != i), then T_i's LCM will be 1 (since all other stores not in S_i have a_i=1). Therefore, S_i's LCM would be at least the unique prime, which is >1, so condition is satisfied.

Wait, but what if S_i has multiple unique stores? Then the LCM would be the product of their primes, which is even larger. But even if there's one unique store, then LCM(S_i) is the prime assigned to that store (since others are 1), which is >1.

So the key idea is: if for each day i, S_i contains at least one store that is not present in any other day's S_j, then the answer is possible. Because we can assign each such unique store a distinct prime, and set all other stores to 1. Then, for each day i, the LCM of S_i would be the product of primes of the unique stores in S_i (at least one prime), and the LCM of T_i would be 1 (since all stores not in S_i are set to 1, so their LCM is 1). So the condition is satisfied.

Conversely, if there's a day i where all stores in S_i are present in at least one other day's S_j, then it's impossible. Because for that day i, all stores in S_i are present in some other S_j. But the T_i (the complement of S_i) includes all stores not in S_i, which includes the stores in other S_j's. So for the LCM of S_i to be greater than T_i's LCM, S_i's LCM must include a prime not present in any of the T_i's stores. But T_i's stores include all stores not in S_i. So any store not in S_i is in T_i. But if all stores in S_i are present in other days' S_j's, then those S_j's may include other stores. Wait, this is getting a bit complicated.

But let's take the second sample input:

Sample Input 2:
10 10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

Each day's S_i is a single store. So for each day i, S_i is {i}, and T_i is all others. So for each day i, the LCM of S_i must be > LCM of T_i. But in this setup, T_i includes all other stores. So for example, on day 1, S_1 is {1}, T_1 is {2,3,4,5,6,7,8,9,10}. To have LCM([a1]) > LCM([a2,...,a10]). But a2 is part of S_2, which is {2}, etc. So if we assign each a_i to a distinct prime, then for day 1, LCM(a1) is p1. The LCM of T_1 is LCM(p2, p3, ..., p10) which is the product of all p2-p10. But p1 is just one prime, while the product of 9 other primes would be way larger. So in this case, the LCM of S_i (p1) is less than the LCM of T_i (product of p2-p10). So this setup would not work. Hence, the answer is impossible.

So in this case, even though each S_i has a unique store (each S_i is a singleton, and each store is only in their own S_i), the approach of assigning unique primes would not work. Because the T_i's LCM for each day i would include the primes from all other days, which are many more primes than S_i's.

Wait, but this contradicts our earlier idea. Because according to the earlier idea, if each S_i has a unique store (which is the case here), then we can assign primes to those stores and set others to 1. But in this case, the other stores are not in T_i. Wait no: the S_i's are {1}, {2}, etc. So for day 1, S_1 is {1}, T_1 is {2,3,...,10}. So the T_i's a_j's for j in T_i are 2,3,..,10. If we set a1=2 (prime), and all other a_j=1. Then for day 1, the LCM of S_1 is 2, and the LCM of T_i is 1. So 2>1. So that day's condition is satisfied. But for day 2, S_2 is {2}, T_2 is {1,3,4,...,10}. But in our assignment, a2 is 1 (since other days' unique stores are not 2), but wait no. Wait according to the earlier idea, for each day, the unique store is assigned a unique prime. So in this sample, each S_i has a unique store (each is in exactly one S_i). So we can assign each store i a unique prime. So a1 = p1, a2 = p2, etc. Then, for day i, S_i is {i} and T_i is all others. So the LCM of S_i is p_i. The LCM of T_i is LCM of all p_j where j != i. But since all p_j's are distinct primes, the LCM of T_i would be the product of all p_j where j != i. So p_i must be greater than that product, which is impossible because all p_i's are primes. For example, p1 would need to be greater than p2*p3*...*p10, which is impossible. So in this case, even though each day's S_i has a unique store, the approach fails. So the initial idea is wrong.

So what's wrong with the earlier reasoning? Because in this case, even though each S_i has a unique store, the T_i's LCM can be larger than S_i's. So the earlier approach of assigning unique primes is not sufficient.

Hmm, this suggests that the initial approach is incorrect. So we need a different approach.

Alternative idea: For each day i, the set S_i must have at least one store that is not present in any other S_j. But even this is not sufficient, as the sample input 2 shows. Because in sample 2, each S_i has a store that is not in any other S_j. So according to the initial idea, the answer should be possible. But according to the sample input 2, the answer is impossible.

So this suggests that the initial approach is incorrect. So the problem requires a different approach.

So what's the correct approach here?

Alternative approach: For each day, the LCM of S_i must be greater than the LCM of T_i. Let's model the problem with variables for each store. Let's think of the a_i as variables, and the constraints that for each day, product (or LCM) of S_i's variables is greater than product (or LCM) of T_i's variables.

But since LCM can be tricky to model, perhaps we can use exponents of primes. Let's assign each a_i to be a distinct prime. Then the LCM of a set is the product of the primes in the set. Because each a_i is a distinct prime, their LCM is the product of all primes in the set.

So in this model, the problem becomes: for each day i, the product of the primes in S_i must be greater than the product of the primes in T_i.

But how can this be possible?

For example, in sample input 2, each S_i is a singleton. So the product of S_i is a_i. The product of T_i is the product of all other a_j. So for each day i, a_i must be > product of all other a_j. Which is impossible because each a_i is a prime. Because for any i, the product of the other primes will be much larger than any individual prime.

So in this case, the answer is impossible, which matches the sample.

So this suggests that the problem is equivalent to the following: can we assign primes to the stores such that for each day i, the product of primes in S_i is greater than the product of primes in T_i.

But this seems impossible when S_i is small compared to T_i. For example, if S_i is a single store and T_i is all others, then the product of S_i is p, and T_i's product is the product of n-1 primes, which is way larger. So in such a case, the answer is impossible.

So the problem reduces to a system of inequalities. Each day i imposes the constraint: product(S_i) > product(T_i). We need to assign primes (or perhaps some numbers) such that all these inequalities are satisfied.

But how can we model this? Since primes are unique and their product increases rapidly, perhaps the constraints can be satisfied only if for each day i, the set S_i is a superset of all other days' T_j. But that's probably not possible.

Alternative idea: For each day i, the set S_i must include at least one prime that is not present in any other day's S_j. Because if a prime is present only in S_i, then T_i (which is the complement of S_i) doesn't include that prime. Thus, the product of S_i's primes includes that prime, while the product of T_i's primes does not. So if the prime is large enough, then S_i's product can be larger.

Wait, perhaps. For example, assign for each day i, a unique prime p_i that is present only in S_i's stores and nowhere else. Then, for day i, the product of S_i's primes includes p_i, while the product of T_i's primes does not. So if p_i is larger than the product of all other primes in T_i's stores, then the inequality holds. But how to choose the primes?

Alternatively, assign primes in such a way that each day's unique prime is very large. For example, for day i, assign a prime p_i that is larger than the product of all primes in T_i's stores. Then, the product of S_i's primes (which includes p_i) would be greater than T_i's product (since p_i is larger than their product).

But how can we arrange this? Because each day's T_i may include many primes from other days.

Alternatively, arrange the primes in such a way that for each day i, the prime assigned to S_i is larger than the product of all primes in T_i. But T_i's primes are those in the stores not in S_i. So, for each day i, we need a prime p_i such that p_i > product of all primes not in S_i. But these primes not in S_i may include primes from other days.

This seems challenging. For example, in sample input 2, each S_i is {i}, and T_i is all other stores. So for day i, p_i must be larger than the product of all p_j for j !=i. But since this must be true for all days, this is impossible. Because for day 1, p1 must be > p2*p3*...*p10. For day 2, p2 must be > p1*p3*...*p10. But these two inequalities can't hold at the same time.

So, the problem is to find if such an assignment of primes exists.

But how can we model this in general?

This seems like a problem that can be reduced to a graph where each day's constraint is a comparison between two products. However, it's difficult to model.

Alternative approach: Assign each store a_i = 2^x_i, where x_i is a non-negative integer. Then, the LCM of a set is 2^max(x_i in the set). For Dora's LCM to be greater than Swiper's, the maximum x_i in S_i must be greater than the maximum x_i in T_i.

So this reduces the problem to assigning exponents x_i such that for each day i, the maximum x in S_i is greater than the maximum x in T_i.

But how can we model this? For each day i, there must be a store in S_i whose x is greater than all x's in T_i.

So for day i, let M_i be the maximum x in T_i. Then, there must exist a store in S_i with x > M_i.

But how can we arrange this for all days?

This seems similar to a problem where we need to arrange the maximum in each S_i to be higher than the maximum in the corresponding T_i.

But this might require a certain ordering of the x's. Let's see.

For example, in sample input 1:

Stores 1-5.

Day 1: S_1 = {1,2,3}, T_1 = {4,5}.

We need max(x1, x2, x3) > max(x4, x5).

Day 2: S_2 = {3,4,5}, T_2 = {1,2}.

max(x3, x4, x5) > max(x1, x2).

So, to satisfy both days:

We can set x4 and x5 to be small. Let's say x4 =0, x5=0. Then for day 1, max(x1, x2, x3) > 0. So at least one of them must be >0.

For day 2, max(x3, x4, x5) is x3 (since x4 and x5 are 0). So we need x3 > max(x1, x2).

So, arrange x1 and x2 to be, say, 1, and x3=2. Then for day 1, the max in S_i is 2>0. For day 2, max in S_i is 2>1. So conditions are met. So possible.

Thus, in this approach, the problem can be modeled as follows: assign to each store a value x_i such that for each day i, the maximum x in S_i is greater than the maximum x in T_i.

This is a simpler problem. Let's model it as a graph problem where each day imposes that the maximum in S_i is higher than the maximum in T_i.

But how can we assign the x_i's to satisfy all these constraints?

This seems similar to a problem where each day i requires that some node in S_i has x higher than all nodes in T_i.

So for each day i:

There exists a store u in S_i such that x_u > x_v for all v in T_i.

But how can this be possible? Because T_i's stores are the complement of S_i.

Let's think of the x_i's as levels. For each day i, the highest level in S_i must be higher than the highest level in T_i.

So, for each day i, the maximum x in S_i must be greater than the maximum x in T_i.

Let’s denote by M_i the maximum x in S_i, and N_i the maximum x in T_i. We need M_i > N_i for all i.

But how can we assign x_i's to satisfy all these inequalities?

Each M_i and N_i are determined by the x_i's.

This seems like a problem that can be modeled with topological sorting. Each day i imposes that M_i > N_i.

But how?

Let's think of the variables as the maximum x in each S_i and T_i. But each S_i and T_i are sets, so their maximum depends on the x's of their elements.

Alternatively, perhaps we can model this by assigning to each store a level, and for each day, the maximum in S_i must be higher than the maximum in T_i.

But the problem is that the same store can be part of multiple S_i's and T_i's. For example, a store in S_i for day i and in T_j for day j.

This seems complicated. Let's think of possible assignments.

An optimal strategy would be to assign the x's in such a way that for each day i, the maximum x in S_i is higher than the maximum x in T_i. One way to achieve this is to assign a high x to a store that is present in S_i and not present in T_j for any other day j. Because then, that store's x can be set higher than any other x's in T_i.

Wait, but T_i is the complement of S_i. So a store in S_i for day i is not in T_i. But other days may include that store in their S_j or T_j.

So, suppose there's a store u that is present only in S_i. Then, for day i, the T_i is all other stores, which don't include u. So in the x assignment, if we set x_u to be a very high value, then in day i, M_i (maximum of S_i) is x_u, and N_i (maximum of T_i) is the maximum of all other x's. If x_u is higher than any other x's, then M_i > N_i.

But if u is present in other days' S_j's, then for those days j, u is in S_j. So for day j, T_j is the complement of S_j. If u is not in T_j (since it's in S_j), then the maximum x in T_j is the maximum x of all stores not in S_j. So, for day j, the maximum x in S_j must be higher than the maximum x in T_j. But if u is the highest x in S_j and is also present in other days' S sets, then the maximum x in T_j could include other high x's.

This suggests that if a store is present in multiple S_j's, it's possible that its high x helps multiple days. But we need to ensure that for each day, the maximum x in its S_i is higher than the maximum x in its T_i.

But how to manage this?

Perhaps the solution is to assign x_i's as follows: For each day, select a store that is unique to that day's S_i (i.e., not present in any other S_j) and assign it a high enough x. Then, other stores can be assigned lower x's. This way, for each day i, the unique store's x is higher than any other x's in T_i (which are from other stores not in S_i, and their x's are lower).

But in cases where no such unique store exists for some day i, then this approach won't work. So the problem reduces to whether for each day i, S_i contains at least one store that is not present in any other S_j.

But in sample input 2, each day i has a unique store (S_i is {i}, and other days have different stores). So according to this approach, each day's S_i has a unique store, so we can assign each of these stores a very high x. But how?

Wait, but in sample input 2, each day's S_i is {i}, and T_i is all other stores. So for day i, the unique store is i, which is not present in any other S_j. So according to the approach, assign x_i to a high value, and all other x_j's to lower values. But for day i, the maximum in S_i is x_i. The maximum in T_i is the maximum of all x_j's except x_i. For this to be true for all days, we need for each day i, x_i > max(x_j for j !=i). But this is impossible because in day 1, x1 must be greater than all x2, x3, ..., x10. Similarly, for day 2, x2 must be greater than all others, including x1. Which is impossible. Hence, the sample input 2 is impossible.

So the approach of assigning unique stores to high x's works only when each day's S_i has a unique store and the assignment is possible. But in cases where multiple days require their unique stores to be higher than all others, it's impossible.

This suggests that the problem is more complex than just checking for the existence of unique stores in each S_i. There's a dependency between the days.

So what's the correct way to model this?

Alternative idea: The problem can be modeled as a directed hypergraph where each day i imposes a constraint that the maximum x in S_i is greater than the maximum x in T_i. The goal is to assign x_i's such that all constraints are satisfied.

But how to find such an assignment?

Let’s consider that the maximum x in S_i is higher than the maximum x in T_i for each day i. For each day, this can be rewritten as: the maximum x in S_i must be higher than the maximum x in (all stores not in S_i).

Let’s denote the global maximum x as X. Then, the store(s) with x=X must be in the intersection of all S_i's for days where X is part of their S_i's. Because if there exists a day i where the store with X is not in S_i, then T_i includes that store, so the maximum x in T_i would be X, making it impossible for S_i's maximum to be greater than X.

Wait, this suggests that the store(s) with the global maximum x must be present in every S_i. Because if there's a day i where the global maximum x is not in S_i, then T_i includes that store, so the maximum x in T_i is X, and the maximum x in S_i must be greater than X, which is impossible. Hence, the global maximum x must be present in all S_i's.

But this is possible only if all S_i's share at least one common store. For example, in sample input 1, the S_i's are {1,2,3} and {3,4,5}. The common store is 3. So if store 3 has the global maximum x, then all S_i's include it, and their T_i's do not. So for each day i, the maximum x in S_i is the global maximum, which is higher than the maximum x in T_i (which is the maximum of the other stores). Hence, the conditions are satisfied.

But in sample input 2, each S_i is a singleton, and there's no common store across all S_i's. So the global maximum x must be in all S_i's, which is impossible. Hence, sample input 2's answer is impossible.

This suggests that the problem's solution depends on the existence of a common store across all S_i's. If there is at least one store that is present in all S_i's, then it's possible to assign that store a very high x (higher than all other stores), and other stores' x's can be lower. Then, for each day i, the maximum x in S_i is the global maximum (store in the intersection), and the maximum x in T_i is the maximum of the other stores, which is lower. Thus, all constraints are satisfied.

But if there's no store present in all S_i's, then it's impossible to have a global maximum store. In such cases, we need to have multiple maximum stores, which can't happen because the global maximum must be present in all S_i's.

So, this leads to the conclusion that the answer is "possible" if and only if there exists at least one store that is present in every S_i. Because then, we can assign that store a very large x, and all other stores a lower x. For each day i, the maximum x in S_i is that store's x (since it's present in S_i), and the maximum x in T_i is the maximum of the other stores (which is lower than the global maximum).

So, the problem reduces to checking whether the intersection of all S_i's is non-empty.

Let's test this hypothesis with the sample inputs.

Sample Input 1:

The two S_i's are {1,2,3} and {3,4,5}. The intersection is {3}, which is non-empty. Hence, possible. Which matches the sample output.

Sample Input 2:

Each S_i is a singleton, and none are common across all days. The intersection is empty. Hence, impossible. Which matches the sample output.

Another test case: Suppose m=2, n=3. S1={1,2}, S2={1,3}. The intersection is {1}, which is non-empty. So possible.

Another test case: m=2, n=3. S1={1}, S2={2}. Intersection is empty. So impossible.

Thus, the correct approach is to check if the intersection of all S_i's is non-empty. If yes, then possible. Otherwise, impossible.

Because if there's a common store x in all S_i's, then assign a_x to a very large prime (or any large number), and assign other stores a_i=1. Then, for each day i, the LCM of S_i is a_x (since x is in S_i and a_x is larger than 1), and the LCM of T_i is the LCM of the other a_i's (which are 1, so LCM is 1). Thus, the condition is satisfied.

If there's no such common store, then there's no way to assign a_i's to satisfy all days. Because for each day i, the maximum x in S_i must be higher than the maximum x in T_i. But if there's no common store in all S_i's, then for any store x, there exists at least one day where x is not in S_i. For that day, the maximum x in T_i would be the maximum of the other stores. Hence, it's impossible to have a store that is present in all S_i's, so you can't have a global maximum that is higher than all T_i's maxima.

Thus, the solution is to compute the intersection of all S_i's. If it's non-empty, output possible; else, impossible.

So the algorithm is:

1. For each day, read the set of stores in S_i.
2. Compute the intersection of all these sets.
3. If the intersection is non-empty, output "possible"; else, "impossible".

This approach is very efficient. For m up to 50 and n up to 1e4, storing each S_i as a set and computing the intersection is feasible.

In Python, we can read each S_i as a set, then compute the intersection by initializing it as the first set and then intersecting with each subsequent set. If at any point the intersection becomes empty, we can break early.

So, the code would be:

Read m and n.

Initialize the intersection as the first S_i's stores.

For each subsequent day's S_i, compute the intersection with the current intersection.

If at any point the intersection is empty, break.

Finally, if the intersection is not empty, output possible; else, impossible.

This is O(m * k), where k is the average size of the S_i's. For m=50 and each S_i up to 1e4, this is manageable.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    m, n = map(int, input_stream.readline().rstrip("\n").split())
    if m == 0:
        print("possible", file=output_stream)
        return

    # Read the first day's stores
    s1 = list(map(int, input_stream.readline().rstrip("\n").split()))
    common = set(s1[1:])

    for _ in range(m-1):
        si = list(map(int, input_stream.readline().rstrip("\n").split()))
        current_set = set(si[1:])
        common &= current_set
        if not common:
            break

    print("possible" if common else "impossible", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
""",
            "output": \
"""\
impossible
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

Each day's S_i is {1}, {2}, etc. The intersection is empty after the second day. So impossible.

Another example where intersection is non-empty: yes.

Thus, the code is straightforward.

Now, let's write the code.

We need to read m and n.

Then read m lines. For each line, read s_i followed by s_i integers. Collect these into a set for each day.

Compute the intersection of all these sets.

If the intersection is non-empty, output possible; else impossible.

In Python:

Read m and n.

If m is 0, then possible (but m >=1 per constraints).

Else:

current_intersection = set of first day's stores.

for each of the remaining days:

   current_intersection = current_intersection.intersection( this day's stores )

   if not current_intersection:

       break

if current_intersection is not empty: possible else impossible.

Yes.

This is efficient.

Thus, the code is as follows.
</think>

```python
m, n = map(int, input().split())
if m == 0:
    print("possible")
    exit()

# Read the first day's stores
s1 = list(map(int, input().split()))
common = set(s1[1:])

for _ in range(m-1):
    si = list(map(int, input().split()))
    current_set = set(si[1:])
    common &= current_set
    if not common:
        break

print("possible" if common else "impossible")
```
