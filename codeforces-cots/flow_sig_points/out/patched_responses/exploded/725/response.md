<think>
Okay, let's try to figure out this problem. So the problem is about determining whether all friends (both boys and girls) can become happy through a series of days where pairs are invited. Each day, the i-th day corresponds to inviting the (i mod n)-th boy and (i mod m)-th girl. When they meet, if either is already happy, the other becomes happy. And once someone is happy, they stay that way forever.

Hmm. The key is to model how happiness spreads through these meetings. Since the days go on infinitely (or until all are happy), we need to check if eventually every boy and girl becomes happy.

The input gives the initial happy boys and girls. The task is to determine if all can become happy through the process.

First, let's think about the process. Each pair (boy, girl) meets on days where i mod n = boy's index and i mod m = girl's index. For example, for boy 0 and girl 0, the day is when i is 0 mod n and 0 mod m. But since n and m can be different, the days when they meet are days that are congruent to their indices modulo LCM(n, m) maybe? Or perhaps it's the days that are in the solution to the congruence equations i ≡ a mod n and i ≡ b mod m. The Chinese Remainder Theorem comes into play here. So for a pair (a, b), their meeting days are all i that satisfy these congruences, which exist only if a ≡ b mod gcd(n,m). If that's the case, then they meet once every LCM(n,m) days, starting from the first solution.

Wait, but in the problem, each day i, the boy is i mod n and the girl is i mod m. So for each day, the pair (i mod n, i mod m) is formed. So the meetings are all possible pairs (a, b) where a cycles through 0..n-1 and b cycles through 0..m-1. But how often do specific pairs meet?

But perhaps instead of thinking about all possible pairs, we can model the spread of happiness through the meetings. The initial happy boys and girls will spread their happiness to others they meet. Then, those newly happy people will spread it further.

So the problem is similar to a BFS where each step can spread happiness. We need to see if all nodes (boys and girls) are reachable through this spreading process.

But the problem is that the meetings happen in a fixed order, but the days cycle in a certain pattern. However, since the process is infinite, if there exists any possible way for a pair (a, b) to meet where one is happy and the other is not, then the other will become happy. But the order in which they meet could affect the spread. Wait, but since the days are infinitely long, any pair (a, b) that can meet infinitely often will have the chance to meet whenever either a or b becomes happy. So perhaps the key is to model the connected components of the possible meetings.

Alternatively, since the process runs indefinitely, the problem reduces to whether for every boy and every girl, there exists a chain of meetings that can connect an initially happy person to them. So the spread is possible if the graph of possible connections (based on the meeting pairs) connects all nodes.

Wait, but how are the meetings structured? Let's think: each day, a boy and a girl meet. The pairs (b, g) that meet are those for which there exists some i such that i mod n = b and i mod m = g. The set of pairs (b, g) that are possible in the meetings are those pairs where (b - g) is congruent to 0 mod d, where d is the GCD of n and m. Because the system of congruences i ≡ b mod n and i ≡ g mod m has a solution if and only if b ≡ g mod d. So the possible pairs (b, g) that meet are those where b ≡ g mod d.

So for any boy b and girl g, if (b - g) mod d is zero, then there exists some day where they meet. Otherwise, they never meet.

So the problem can be thought of as a bipartite graph where boys and girls are nodes, and edges exist between boy b and girl g if b ≡ g mod d. Then, the spread of happiness is possible along these edges. Initially, some nodes are happy, and through these edges, happiness can spread. The question is whether the entire graph is covered by the spread from the initial nodes.

So, for example, if there's a connected component (in this bipartite graph) that has no initially happy nodes, then it's impossible to make all friends happy. Otherwise, if every connected component has at least one initially happy node (either boy or girl), then it's possible.

Wait, but in this bipartite graph, the connected components would be determined by the equivalence classes modulo d. Let's see: since the edges connect boy b to girl g if (b - g) mod d == 0. So for any boy, his possible connected girls are those in the same equivalence class modulo d. Similarly for girls.

So for example, the equivalence classes are based on their value modulo d. So the connected components are determined by the residue of the boy's index modulo d and the girl's residue modulo d. Because a boy's residue mod d is fixed (since when you subtract, their difference mod d must be zero). So each connected component is a set of boys and girls whose indices mod d are equal to a certain value.

Wait, more precisely: for any boy b, his residue is b mod d. For any girl g, her residue is g mod d. The edge between b and g exists if and only if (b mod d) == (g mod d). So the bipartite graph is partitioned into d connected components, each corresponding to a residue r mod d. In each component, all boys with b mod d = r and all girls with g mod d = r are connected. So each connected component is formed by all boys and girls in that residue class.

Therefore, the connected components are the residue classes modulo d.

So the problem reduces to checking whether in every residue class (from 0 to d-1), there is at least one initially happy boy or girl in that class. Because, for each residue class, if there's at least one happy person in that class (either a boy or a girl), then through the meetings in that component, all the others in the same component can become happy. But if there's a residue class where no one is happy initially, then the people in that class can't be made happy, because they can't connect to any initially happy person.

Wait, but the initial happy people may not be in the same residue class. Wait, no: the initial happy people are part of their residue classes. For example, an initially happy boy b has residue r = b mod d. So he can spread happiness to all girls in residue r, and those girls can spread to other boys in residue r, etc. So for each residue class r, if there is at least one initially happy person (boy or girl) in that class, then all boys and girls in that class can become happy. Otherwise, if a residue class has no initially happy people, then none in that class can become happy, so the answer is "No".

Therefore, the solution is to compute d = gcd(n, m), then for each residue r from 0 to d-1, check if there's any happy boy with residue r, or any happy girl with residue r. If for all r, this is true, then the answer is "Yes". Otherwise, "No".

Wait, but how to confirm this? Let's take the example:

First example:

n=2, m=3. d = gcd(2,3)=1. So all residues are 0. The initial happy boys are none. The initial happy girls are 0. The residue of 0 mod 1 is 0. So the only residue class has a happy girl, so all boys and girls can be covered. Hence, output is yes.

Second example:

n=2, m=4. d=2. So residues 0 and 1. The initial happy boys is 0 (residue 0 mod 2). The initial happy girls are 2 (residue 2 mod 2=0). So residue 0 has happy people. What about residue 1? The other residue. Are there any boys or girls in residue 1?

n=2: boys are 0 and 1. Their residues mod 2 are 0 and 1. So residue 1 has the boy 1. Girls: m=4, girls 0,1,2,3. Their residues mod 2 are 0,1,0,1. So girls in residue 1 are 1 and 3. The initial happy girl is 2 (residue 0). So residue 0 has happy people (boy 0 and girl 2). Residue 1: are there any initially happy boys or girls here? The initial happy boys are 0 (residue 0), initial happy girls is 2 (residue 0). So residue 1 has no initial happy people. So the boys 1 and girls 1,3 can't be made happy. Hence, output is no.

Third example:

n=2, m=3. d=1. So all are in residue 0. The initial happy boys are 0 (residue 0). The initial happy girls are 1 (residue 1 mod 1=0). So residue 0 has happy people. So all can be made happy. Output yes.

So this approach works for the examples.

So the algorithm is:

1. Compute d = gcd(n, m).

2. For each residue r in 0..d-1:

   a. Check if there's any happy boy with index ≡ r mod d.

   b. Check if there's any happy girl with index ≡ r mod d.

   c. If either a or b is true for this residue, then this residue is covered. Otherwise, return "No".

3. If all residues are covered, return "Yes"; else, "No".

So the steps are:

- For each residue class r (from 0 to d-1), check if there is at least one happy boy or girl in that class.

If all classes are covered, output yes; else no.

So now the code can be structured as follows.

Read n and m. Then read the list of happy boys and girls.

Compute d = gcd(n, m).

For each residue r in 0 to d-1:

   check if any boy in the happy boys has x mod d == r.

   check if any girl in the happy girls has y mod d == r.

   if either exists, then residue r is covered. Else, return No.

If all residues are covered, return Yes.

Now, how to implement this efficiently.

Given that n and m can be up to 100, the number of residues is up to 100 (since d can be up to min(n,m)). But since d is the gcd, which for 100 and 100 is 100, but for 100 and 99 is 1.

But even for d=100, checking 100 residues is manageable.

For each residue r in 0..d-1:

   boys_covered = any(b in happy_boys where b % d == r)

   girls_covered = any(g in happy_girls where g % d == r)

   if not (boys_covered or girls_covered):

       return "No"

So the code can be written with that logic.

Now, how to handle the initial happy boys and girls.

We can precompute the residues for all happy boys and store in a set. Similarly for girls.

For example:

Compute a set for boys' residues: boy_res = set(b % d for b in boys_list)

Similarly, girl_res = set(g % d for g in girls_list)

Then, for each residue r in 0..d-1:

   if r is in boy_res or r is in girl_res → covered.

Else → not covered.

So for each r in 0..d-1, check if r is present in boy_res or girl_res.

If all r are present in the union of the two sets → yes.

But wait, no. Because for each residue r, the requirement is that in the r-th residue class, there is at least one boy or girl from that class. So the set of residues covered is the union of boy_res and girl_res. But the required residues are all 0..d-1. So if the union is exactly the set {0,1,...,d-1}, then yes.

Wait, no. Let's see:

Each residue class r (from 0 to d-1) must have at least one happy boy or girl in that class.

So the union of the residues of happy boys and girls must include all possible residues from 0 to d-1.

If not, then there's a residue class that has no happy people, so output no.

So the code can be written as:

Compute d = gcd(n, m)

Compute the set of residues from happy boys (b % d for each b).

Compute the set of residues from happy girls (g % d for each g).

Union these two sets.

If the union is exactly {0, 1, ..., d-1} → yes, else no.

But wait, no. Because for example, if d=2, and the residues covered by boys and girls are {0,1}, then yes. If union is {0}, then no.

So the code can check whether the union's length is equal to d. But that's only possible if the union covers all residues from 0 to d-1.

For example, if d=3, and the union is {0,1,2}, then yes. If union is {0,0,1}, then the set is {0,1}, length 2 <3 → no.

So the code can compute the union of the residues and check if the size is at least d. Wait, no. Because if d=3, the union could have size 3 only if all residues 0,1,2 are present. So checking if the union's length is equal to d and the maximum residue is d-1 would be sufficient. But perhaps a more straightforward way is to loop through each residue r from 0 to d-1 and check if any in boy_res or girl_res.

So perhaps the code is better structured as:

d = gcd(n, m)

happy_boys = list of initial happy boys (from input)
happy_girls = list of initial happy girls (from input)

for r in 0 to d-1:
    if any(b % d == r for b in happy_boys) or any(g % d == r for g in happy_girls):
        continue
    else:
        print("No")
        exit()
print("Yes")

But in Python, how efficient is this?

But given that d can be up to 100, and for each residue r, we loop through the happy_boys and happy_girls lists (each up to 100 elements), this is acceptable.

For each residue r in 0..d-1:

Check if any boy in happy_boys has b mod d == r → O(B) per check.

Check if any girl in happy_girls has g mod d == r → O(G) per check.

Total time: O(d*(B + G)).

Since B and G are up to 100, and d up to 100, this is 100 * (100 + 100) = 20,000 operations, which is negligible.

So the code can proceed with this approach.

Now, the code steps:

Read n and m.

Read the second line: first integer is b, followed by b integers (the happy boys).

Read the third line: first integer is g, followed by g integers (the happy girls).

Compute d = gcd(n, m).

For each r in 0 to d-1:

   check if there exists a boy in happy_boys where boy % d == r.

   check if there exists a girl in happy_girls where girl % d == r.

   if neither exists, output "No".

If all r pass, output "Yes".

Now, code in Python.

But how to read the input?

The second line is: the first integer is b, then followed by b integers. Similarly for the third line.

So:

n, m = map(int, input().split())

boys = list(map(int, input().split()))
b = boys[0]
happy_boys = boys[1:] if b > 0 else []

girls = list(map(int, input().split()))
g = girls[0]
happy_girls = girls[1:] if g > 0 else []

But wait, what if b is 0? Then the second line is "0" and no other numbers. So boys would be [0], but boys[1:] would be empty. Similarly for girls.

Yes, that's correct.

Compute d = gcd(n, m).

Then for each r in 0 to d-1:

   boy_has_r = any( (x % d) == r for x in happy_boys )

   girl_has_r = any( (y % d) == r for y in happy_girls )

   if not (boy_has_r or girl_has_r):

       print("No")

       exit()

print("Yes")

Yes.

Testing the examples.

First example:

n=2, m=3. d=1.

r can only be 0.

Check if any boy has 0 mod 1=0. The boys list is empty (b=0) → no.

Check girls: initial girl is 0 mod 1=0. So yes. So all residues covered. Output yes.

Second example:

n=2, m=4. d=2.

r can be 0 and 1.

For r=0:

happy_boys: 0 → 0 mod 2=0 → yes. So covered.

For r=1:

Check happy_boys: none (happy_boys are [0], 0 mod 2=0. So no.

Check happy_girls: [2]. 2 mod 2=0. So no girls have mod 2=1. So residue 1 not covered. Output no.

Third example:

n=2, m=3. d=1.

r=0.

happy_boys: [0], 0 mod 1=0. So covered.

So output yes.

Another test case:

Suppose n=4, m=6. d=2.

Residues 0 and 1.

If the happy_boys are [0], happy_girls are [2].

0 mod 2=0, 2 mod 2=0. So residue 0 is covered. Residue 1 is not. So output no.

But if there is a girl with index 1 in happy_girls, then residue 1 is covered.

So the code correctly handles this.

Another case: d=3. Suppose happy_boys have residues 0,1 and happy_girls have 2. Then all residues are covered. So output yes.

So this approach should work.

Thus, the code is correct.
</think>

```python
import sys
import math

n, m = map(int, sys.stdin.readline().split())
boys = list(map(int, sys.stdin.readline().split()))
girls = list(map(int, sys.stdin.readline().split()))
happy_boys = boys[1:] if boys[0] > 0 else []
happy_girls = girls[1:] if girls[0] > 0 else []

d = math.gcd(n, m)

for r in range(d):
    boy_covered = any((x % d == r) for x in happy_boys)
    girl_covered = any((y % d == r) for y in happy_girls)
    if not (boy_covered or girl_covered):
        print("No")
        exit()
print("Yes")
```