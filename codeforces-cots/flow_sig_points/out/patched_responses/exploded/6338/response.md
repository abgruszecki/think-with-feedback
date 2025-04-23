<think>
Okay, let's see. I need to solve this problem where BerCorp wants all employees to be connected through the languages they know. The goal is to find the minimum cost (which is the number of languages they need to learn) to achieve this. 

First, the problem says that any employee can correspond with any other, directly or indirectly. So this sounds like a graph problem where employees are nodes and edges exist if they can communicate (through a common language). The key is that the communication graph must be connected.

But how do the languages factor into this? Each employee knows some languages. Two employees can communicate if they share at least one language. But also, when employees learn new languages, that can create new edges. 

So the approach here is to model the employees as a graph where edges are based on shared languages, but with the possibility of adding edges by teaching employees new languages. The cost is the number of languages taught. We need to find the minimal cost to make this graph connected.

Wait, but perhaps another way to model this is by considering the languages. Each language forms a group of employees that know it. If two employees know the same language, they are connected. Then, the entire company is connected if all the language groups form a connected structure. But how?

Alternatively, think of the problem as building a graph where each connected component is a group of employees that can communicate with each other through a chain of languages. To connect all components, we can either:

1. Teach some employees new languages so that components merge.
2. If there's a component with no languages (like an employee who knows none), we might need to teach them a language first.

So the problem reduces to finding the number of connected components in the current setup, and then figuring out how to connect them with minimal cost.

Wait, but the current setup's connected components depend on the employees' languages. For example, if two employees share a language, they are in the same component. If they don't, but there's another employee who shares languages with both, then all three are in the same component.

But perhaps we can model this as a graph where employees are nodes and edges exist if they share at least one common language. Then, the connected components of this graph are the groups that can already communicate. But the problem allows adding edges by teaching languages.

But teaching a language to an employee allows them to connect to anyone who knows that language. So, if we teach a language L to a set of employees, then all those employees can connect to any component that has L. 

Alternatively, maybe we can model the problem by considering each language as a node and each employee as a node. Then, an employee is connected to all the languages they know. Two employees are connected if they share a language (they are connected through the language node). Then, the entire structure must be connected. But this might complicate things.

Alternatively, think in terms of connected components of the languages and employees. If two employees are in the same component, they can communicate. To connect all components, we need to find a way to merge them with minimal cost.

Hmm. Let's think about the connected components. For each employee, their languages determine which components they belong to. But perhaps the best way is to model this as a union-find (disjoint set) data structure. Each employee starts connected to all others who share a language with them. Then, the number of connected components is determined. The minimal cost would then be (number of components - 1) plus any adjustments needed for employees who know no languages.

Wait, but there's a catch. If there's an employee who knows zero languages, they can't communicate with anyone. So, they form a component by themselves. To connect them, they must learn at least one language. But which one? The minimal cost here would be to teach them a language that's part of the largest existing component, but perhaps that's not possible. Alternatively, if there are multiple such employees, each needs to be taught at least one language. But if all employees know zero languages, then each must learn at least one, and they can all be connected by choosing a common language.

So the steps might be:

1. Find all the connected components of the employees based on their current languages. Employees are in the same component if they share a language, or if they are connected through a chain of shared languages.
2. For each component, check if there's at least one employee in it who knows at least one language. If a component has all employees with zero languages (which can only be if the component is size 1?), then that component needs to be connected to others by teaching one of its employees a language. But how?

Wait, any component that has at least one language is part of a connected group. But a component with employees who all know zero languages can't be connected to anything unless they learn a language.

So the problem can be broken into:

- Determine the number of connected components where each component has at least one language. Let's call these "valid" components.
- Count the number of employees who know zero languages. Let's call this count "zero_employees".

Then, the minimal steps would be:

- If there are no valid components (all employees know zero languages), then all employees must learn at least one language. We can choose a common language for all, which would cost n (each of the n employees learns that language). But wait, in this case, the employees can all be connected by that language, so the total cost is n. But since they were all in separate components (each being their own component), the number of components is n. So to connect them, the cost would be (n - 1) + n (each employee must learn a language, and we need to connect n components). Wait, maybe this is not the right way to model it.

Alternatively, if all employees know zero languages, then each is a component. To connect them all, each must learn at least one language. The minimal cost here is to choose a single language and have all learn it. That costs n, which is the sum of 1 per employee. Then, all are connected through that language. So in this case, the answer is n.

But let's think of another approach. Let's model the connected components. For each employee, if they know a language, they are connected to others through shared languages. If an employee knows no languages, they are in their own component. 

The problem is to make all components connected. How?

The way to connect components is to either:

a) Teach a language to an employee in component A and a language to an employee in component B, such that those two languages are the same. Then, components A and B are merged.

But that's not efficient, since teaching two languages for each connection. Alternatively, perhaps we can create a bridge between components by teaching a single language to employees in different components.

Wait, let's think. Suppose we have two components, C1 and C2. If we can teach a language L to an employee in C1 and an employee in C2, then those two employees can communicate via L, merging the components. But that's two cost units. Alternatively, if there is a language L that is not used in any component, but teaching L to one employee in each component would cost 2. However, if one component already has a language (say C1 has L), then teaching L to an employee in C2 would cost 1, and the components are merged.

So the optimal approach is to select a common language that can be used to connect all components. The minimal cost would then be (number of components - 1) plus the number of employees who know zero languages (each of those must learn at least one language).

Wait, but how? Let's think step by step.

Suppose there are k connected components. Among these, some are "valid" (they have at least one employee who knows a language) and others are "invalid" (all employees in the component know no languages). Wait, but if a component has employees that know no languages, then that component is just a single employee (since you can't connect to anyone else without a language). Because if two employees both know zero languages, they can't communicate, so they are in separate components.

So the zero_employees are each in their own component. Then, the other components are connected via some language.

So total_components = k (number of connected components based on current languages) + zero_employees.

Wait, no. Because the employees with zero languages are each in their own component. The employees with at least one language form their own connected components based on language overlaps.

So the total number of components is the number of connected components in the language-based graph plus the number of zero_employees.

But how to model this.

Alternative approach:

Each employee is part of a connected component. Two employees are in the same component if they can communicate directly or via other employees. So:

- If two employees share a language, they are in the same component.
- If employee A shares a language with B, and B shares a language with C, then A and C are in the same component.

So the connected components are built based on these shared language edges.

Additionally, any employee who knows zero languages is in a component by themselves.

So the steps to model this:

1. For each employee, if they know zero languages, they are a component of size 1.
2. For the rest, group them into components where employees are connected via shared languages. 

Now, the problem is to connect all these components. The cost is the number of languages taught. Each time we teach a language to an employee, it's a cost of 1 per employee. But how does teaching a language help connect components.

Suppose we have two components, C1 and C2. To connect them, we can:

- Teach a language L to at least one employee in C1 and one in C2. Then, those two employees can communicate via L, merging the components. The cost here is 2.

But if there's a language that already exists in any component, perhaps we can choose that language and teach it to employees in other components. For example, if component C1 uses language L, and component C2 has no L, then teach L to one employee in C2. Then, C1 and C2 are connected. The cost here is 1.

So the minimal cost to connect all components would be (number of components - 1) plus the number of zero_employees (each must learn at least one language), but only if there is at least one existing language. Otherwise, all components are zero_employees, and the cost is n (teach each one a language, and since they all choose the same language, they can all communicate).

Wait, but maybe it's more complicated. Let's break it down:

Case 1: There are no employees who know any language (all employees have zero languages).

Then, each employee is a component. To connect them all, each must learn at least one language. The minimal way is to choose a common language. Each of the n employees learns this language. So cost is n. Then, all are connected.

Case 2: There is at least one employee who knows a language.

Let the number of connected components (including the zero_employees) be c. But among these components, there is at least one that has a language (since some employees have languages).

The zero_employees are each in their own component, and they need to be connected. For each zero_employee, they must learn at least one language, which adds them to an existing component. So the cost is the number of zero_employees (each must learn one language). But also, the existing components (those with languages) must be connected among themselves. The number of existing components (those that have at least one language) is (c_total - zero_employees). Because the c_total is the total components, which includes the zero_employees' individual components and the language-based components.

Wait, maybe the total components is:

c_non_zero_components (components formed by employees with at least one language) + zero_employees (each is a component of their own).

So, the total_components = c_non_zero_components + zero_employees.

If there are c_non_zero_components, then to connect them into a single component, we need to add (c_non_zero_components - 1) edges. Each edge is formed by teaching a language. But how?

If we can choose a language that exists in one of the non-zero components, say L, then teaching L to one employee in each other non-zero component would merge them. Wait, no. Each non-zero component already has some languages. So, for example, if two components A and B have some languages. To connect them, maybe there's a common language they can share. If not, then we need to teach a language to an employee in A and an employee in B.

Wait, but perhaps the existing components are already connected via their own languages. Wait, no. If two components (non-zero) are not connected, it's because there's no path between them via shared languages. So to connect them, we need to teach a common language.

Wait, but how?

For example, component A has employees who know language X. Component B has employees who know language Y. To connect A and B, we can teach X to an employee in B (cost 1). Then, that employee knows Y and X, so the components A and B are now connected through X.

So the minimal cost to connect all non-zero components is (c_non_zero_components - 1) because each merge requires one cost unit (teaching one language to one employee in a component).

But how?

Wait, suppose there are k non-zero components. To connect them all, we need k-1 bridges. Each bridge can be created by teaching a single employee in a component a language that's present in another component. So the minimal cost is (k-1) + (zero_employees). Because each zero_employee must learn at least one language (cost 1 each), and the non-zero components must be merged with (k-1) steps.

But if there are zero non-zero components (i.e., all employees are zero_employees), then it's case 1.

So putting it all together:

If all employees are zero_employees:

    cost = n (each must learn a language, and they all choose the same one)

Else:

    cost = (number of non-zero components - 1) + (number of zero_employees) 

But wait, no. Because for the non-zero components, the (number of non-zero components -1) is the number of edges needed to connect them into one component. Each such edge requires teaching one language (like connecting a component to the main one by teaching an employee in that component a language from the main component). 

So for example, if there are 3 non-zero components (A, B, C), you can teach a language from A to an employee in B (cost 1), then teach a language from A to an employee in C (cost 1). Total cost is 2, which is 3-1=2. So yes.

Therefore, the formula is:

if total_non_zero_components == 0:

    cost = n (all employees must learn a language, same one)

else:

    cost = (total_non_zero_components - 1) + zero_employees

But wait, in this case, the zero_employees each need to learn at least one language, which adds them to the main component. So each zero_employee is a component of 1, and to connect them to the main component, each needs to learn at least one language (cost 1 each). So the formula holds.

But let's test with the examples.

First example input:

5 5

1 2

2 2 3

2 3 4

2 4 5

1 5

All employees know languages. The non-zero components: let's see. All employees know languages connected through 2-3-4-5. So all are in the same component. So total_non_zero_components is 1. zero_employees is 0. So cost is (1-1) + 0 = 0. Which matches the sample.

Second sample:

8 7

0 (employee 1: zero languages)

3 1 2 3 (employee 2: knows 1,2,3)

1 1 (employee 3: knows 1)

2 5 4 (employee4: knows 5,4)

2 6 7 (employee5: knows 6,7)

1 3 (employee6: knows 3)

2 7 4 (employee7: knows7,4)

1 1 (employee8: knows 1)

So the components:

Employee1 is a zero_employee (cost 1).

Employees 2,3,6,8 know 1,2,3. Since 2 and 3 know 1, they are connected. Employee 6 knows 3 (so connected to 2,3). Employee8 knows 1, connected to 2,3. So component A: employees 2,3,6,8.

Employee4 knows 5,4. Component B.

Employee5 knows 6,7. But 6 is connected to component A (since employee5 knows 6 and 7, but employee6 knows 3. So employee5 is connected to component B via 6? Wait, no. Wait, employee5 knows 6 and7. But no other employee knows 6 or 7 except employee5 and maybe others. Wait, employee5 is part of component B?

Wait, let's re-examine:

Employee2 knows 1,2,3. So connected to employee3 (knows 1), employee6 (knows3), employee8 (knows1).

Employee4 knows 5 and4. Are they connected to anyone else? Let's see. Employee7 knows7 and4. So employee4 and 7 share 4. So they are connected. So component B: employee4 and7.

Employee5 knows6 and7. Shares 7 with employee7. So component B includes employee5, 4,7.

Employee5 is connected via 7 to employee7, which is connected via4 to employee4. So component B is employees4,5,7.

Employee5 also knows6, but no one else knows6 except employee5.

So component B includes 4,5,7.

Employee5 is part of component B. So component B's languages include 4,5,7,6.

Wait, no: employee5's languages are 6,7. Employee7's languages are 4,7. So employee5 and7 share 7. So component B includes employee5,7,4 (since employee4 and7 share4). So component B includes 4,5,7.

Employee6 knows3. So component A includes 2,3,6,8.

So non-zero components are component A (4 employees), component B (3 employees:4,5,7), and then employee5 is part of component B?

Wait, let me re-express:

Component A:

Employees 2,3,6,8 share languages 1,2,3.

Component B:

Employees 4,5,7 share languages 4,5,7, etc. Because:

Employee4 knows5,4. Employee7 knows4,7. So employee4 and7 share4. Employee7 and5 share7. So component B is 4,5,7.

Employee5 knows6 and7. So employee5 is connected via7 to employee7, which is connected via4 to employee4. So component B is 4,5,7.

Employee5 is part of component B. So component B has 3 employees.

Then, employee5 is part of component B.

So non-zero components are A and B. So total_non_zero_components is 2.

zero_employees is 1 (employee1). 

So cost is (2-1) +1 = 2, which matches the sample output.

Third example:

2 employees, 2 languages.

Employee1 knows language2.

Employee2 knows none.

So, non-zero components: employee1 (knows 2) is a component. Employee2 is a zero_employee (component of 1). So total_non_zero_components is1, zero_employees is1. So cost (1-1) +1=1. Which matches the sample.

So the formula works for the samples.

So the steps to compute the answer are:

1. Compute the number of zero_employees (employees with zero languages).

2. Compute the number of non-zero components (connected components formed by employees with at least one language, connected via shared languages).

3. If there are zero non-zero components (i.e., all employees are zero_employees), then the answer is n (each must learn a language).

Else, the answer is (non_zero_components -1) + zero_employees.

But wait, wait. Because in the formula, the zero_employees need to learn at least one language. So each zero_employee is a component. To connect them to the main component (the connected non-zero components), each must learn a language. So for each zero_employee, the cost is 1.

But how to model this in code.

So the steps are:

- For each employee, if they have zero languages, add to zero_employees count.

- For the rest, build a graph where employees are connected if they share a language.

- Find the number of connected components among these non-zero employees.

Then, if the number of non-zero components is zero (all are zero_employees), answer is n.

Else, answer is (non_zero_components -1) + zero_employees.

Wait, but even when there are non-zero components, but zero_employees is non-zero, the formula holds.

But how do we model the connected components for the non-zero employees?

Each non-zero employee has at least one language. They are connected if there's a path of shared languages. For example, employee A knows language X, employee B knows X and Y, employee C knows Y. Then A is connected to B (via X), B to C (via Y), so all three are in the same component.

So to model this, perhaps the best way is to model the languages and employees as a bipartite graph. Each employee is connected to the languages they know. Then, two employees are in the same component if they are connected through a language (i.e., they share a language directly or via intermediate languages and employees).

Alternatively, we can model the employees as nodes and connect two employees if they share a language. Then, the connected components are the groups of employees that can communicate directly or indirectly. But this approach requires O(n^2) checks, which is feasible since n is up to 100.

But for n=100, building a graph where edges are between employees who share any language is O(n^2) which is 10^4 operations. Then, finding connected components via BFS or DFS is manageable.

Alternatively, we can use a union-find (disjoint set) structure. For each employee, we can iterate through their languages and connect the employees via their languages.

Wait, perhaps another approach: For each language, group all employees that know it. Then, for each language, all employees in that group are connected. So, employees in the same language group are in the same component. Then, employees can belong to multiple languages, so their components are merged.

So the idea is:

Initialize each employee as their own parent in the union-find structure.

For each language, collect all employees that know it.

For each such group, merge all employees in the group into a single component. For example, if employees 1,2,3 know language X, then union 1 with 2, 1 with 3, etc. But union is a transitive operation, so merging all of them pairwise would result in them being in the same component.

Wait, but union is a transitive operation. So for a group of employees that share a language, we can take the first employee and union all others with the first. This way, all are in the same component.

So the steps would be:

- Initialize DSU (disjoint set union) structure for the employees.

- For each language in 1..m:

   - Collect all employees that know this language.

   - If there are at least two employees in this group, take the first employee as the root, and union all others with the first.

Wait, but even if there's only one employee in a language group, it's okay. Because that employee knows a language, so is part of a component (possibly of size 1).

But in the DSU approach, the component is built by merging all employees that share a language. So any employee that knows a language X will be merged with any other employee that knows X. Then, if an employee knows X and Y, they will merge the X group with the Y group.

This approach would correctly model the connected components.

So the plan is:

1. For each employee, keep track of their languages.

2. For each language, collect the list of employees that know it.

3. For each such list, union all employees in that list into the same component.

But wait, this would not capture the scenario where two employees share different languages. For example, employee A knows X, employee B knows Y, and employee C knows X and Y. Then, A is merged with C via X, B is merged with C via Y. So A, B, C are in the same component. But how?

But the DSU approach would handle that. Because when processing language X, A and C are merged. When processing Y, B and C are merged. So A, B, C are all in the same component.

Thus, the DSU approach correctly captures the connected components.

So the steps in code:

- Read n and m.

- Read each employee's languages.

- For each employee, if they have zero languages, add to zero_employees count.

- For employees with at least one language, add them to a list.

- Initialize DSU with n elements (each employee is their own parent).

- For each language L from 1 to m:

   - Collect all employees that have L in their list.

   - If there are any such employees, take the first one (say emp0), and for each other employee emp in the list, union emp0 and emp.

- Then, for all employees that have at least one language, find the number of connected components in the DSU.

But how? Because some employees might have languages but have not been merged with others. For example, an employee who knows a unique language not known by others would be in their own component.

So after processing all languages, for each employee (excluding zero_employees), we need to find the root of their component and count unique roots. That gives the number of non-zero components.

Once we have that, compute:

if there are zero non-zero components (i.e., all employees are zero_employees):

   answer is n

else:

   answer is (non_zero_components - 1) + zero_employees

So the code steps are:

Read n and m.

zero_employees = 0

employees = list for each employee's languages.

non_zero_employees = list of employees with at least one language.

Initialize DSU.

For each language L in 1..m:

   emps = list of employees (indices) that have L.

   if len(emps) >= 1:

      first = emps[0]

      for emp in emps[1:]:

          union(first, emp)

Then, collect all roots of non-zero employees.

roots = set()

for emp in 0..n-1:

   if len(employees[emp]) > 0:

      root = find(emp)

      roots.add(root)

non_zero_components = len(roots)

if non_zero_components == 0:

   print(n)

else:

   cost = (non_zero_components -1) + zero_employees

   print(cost)

Yes, this should work.

Now, let's test this logic against the examples.

Third example:

Employees 0 and 1.

Employee0 has language2. Employee1 has none.

zero_employees is 1.

non_zero_employees is [0].

Processing language2:

emps = [0]. So no unions.

So roots of non-zero employees is {0}. So non_zero_components is 1.

cost is (1-1) +1 =1.

Which is correct.

Second example:

Employee1 (index 0) has zero languages.

Other employees have some.

Processing each language.

For language1:

employees 1 (index1?), employee2 (index2?), employee7 (index7?), etc. Need to see.

But the code correctly unions all employees that share a language.

After processing all languages, the non-zero_components would be 2 (components A and B as before).

So the code gives (2-1) +1 =2.

Yes.

So the code seems correct.

Now, handling the DSU.

Implementing the DSU with path compression and union by rank.

In Python, the code can be written with a parent array, and rank array.

But since the employees are numbered from 0 to n-1, the DSU can be initialized with parent[i] = i, rank[i] = 1.

Then, for each language, collect all employees that know it. For each group, union the first with the others.

But how to collect the employees for each language?

We can create a dictionary for each language to list of employee indices.

Like:

lang_to_emps = defaultdict(list)

for i in range(n):

   langs = employees[i]

   for lang in langs:

       lang_to_emps[lang].append(i)

Then, for each lang in lang_to_emps:

   emps = lang_to_emps[lang]

   if len(emps) >=1:

      first = emps[0]

      for emp in emps[1:]:

          union(first, emp)

Yes.

So putting this all together.

Edge case where all employees are zero_employees:

n=3, m=5.

Each employee has 0 languages.

zero_employees=3.

non_zero_components=0. So answer is 3.

Another edge case: one employee has a language, others are zero_employees. For example, n=4, m=5.

Employee 0: [1]

Others: zero.

non_zero_components is 1.

zero_employees is3. cost (1-1) +3 =3.

Which is correct: each of the 3 must learn at least one language (probably the same as employee0's language).

So code works.

Now, code implementation.

In Python:

Read n and m.

Read next n lines.

employees = []

zero_employees =0

for each line:

   parts = list(map(int, input().split()))

   ki = parts[0]

   langs = parts[1:] if ki>0 else []

   employees.append(langs)

   if ki ==0:

      zero_employees +=1

Then, build the lang_to_emps:

from collections import defaultdict

lang_to_emps = defaultdict(list)

for i in range(n):

   for lang in employees[i]:

       lang_to_emps[lang].append(i)

Then, DSU:

class DSU:

   def __init__(self, size):

       self.parent = list(range(size))

       self.rank = [1]*size

   def find(self, x):

       if self.parent[x] != x:

           self.parent[x] = self.find(self.parent[x])

       return self.parent[x]

   def union(self, x, y):

       x_root = self.find(x)

       y_root = self.find(y)

       if x_root == y_root:

           return

       if self.rank[x_root] < self.rank[y_root]:

           self.parent[x_root] = y_root

       else:

           self.parent[y_root] = x_root

           if self.rank[x_root] == self.rank[y_root]:

               self.rank[x_root] +=1

Then, create DSU(n):

dsu = DSU(n)

for lang in lang_to_emps:

   emps = lang_to_emps[lang]

   first = emps[0]

   for emp in emps[1:]:

       dsu.union(first, emp)

Then, collect roots of non-zero employees.

roots = set()

for i in range(n):

   if len(employees[i]) >0:

       roots.add(dsu.find(i))

non_zero_components = len(roots)

if non_zero_components ==0:

   # all are zero_employees

   print(n)

else:

   cost = (non_zero_components -1) + zero_employees

   print(cost)

This code should work.

Testing against sample input 1.

```python
import sys
from collections import defaultdict


class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

def main(input_stream, output_stream):
    input = input_stream.read().split()
    ptr = 0
    n, m = int(input[ptr]), int(input[ptr+1])
    ptr +=2
    employees = []
    zero_employees = 0
    for _ in range(n):
        ki = int(input[ptr])
        ptr +=1
        if ki ==0:
            employees.append([])
            zero_employees +=1
            ptr += ki
            continue
        langs = list(map(int, input[ptr:ptr+ki]))
        ptr += ki
        employees.append(langs)
    
    lang_to_emps = defaultdict(list)
    for i in range(n):
        for lang in employees[i]:
            lang_to_emps[lang].append(i)
    
    dsu = DSU(n)
    for lang in lang_to_emps:
        emps = lang_to_emps[lang]
        first = emps[0]
        for emp in emps[1:]:
            dsu.union(first, emp)
    
    roots = set()
    for i in range(n):
        if len(employees[i]) > 0:
            roots.add(dsu.find(i))
    non_zero_components = len(roots)
    
    if non_zero_components ==0:
        print(n, file=output_stream)
    else:
        print((non_zero_components -1) + zero_employees, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8 7
0
3 1 2 3
1 1
2 5 4
2 6 7
1 3
2 7 4
1 1
""",
            "output": \
"""\
2
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

Another test case: third example.

n=2, m=2.

employees:

0: [2], 1: []

zero_employees=1.

lang_to_emps for lang 2: [0]

Processing lang 2: emps is [0], no unions.

roots for non-zero employees is {0}. non_zero_components=1. cost 0 +1=1.

Yes.

Another test case where all employees are zero_employees.

n=3, m=5.

employees all have zero languages.

zero_employees=3.

lang_to_emps is empty. So non_zero_components=0. So code prints 3.

Yes.

Another test case: one employee with a language, others zero.

n=4, zero_employees=3. non_zero_components=1. cost 0 +3=3.

Yes.

Thus, the code should work.
</think>

```python
import sys
from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = int(input[ptr]), int(input[ptr+1])
    ptr +=2
    employees = []
    zero_employees = 0
    for _ in range(n):
        ki = int(input[ptr])
        ptr +=1
        if ki ==0:
            employees.append([])
            zero_employees +=1
            ptr += ki
            continue
        langs = list(map(int, input[ptr:ptr+ki]))
        ptr += ki
        employees.append(langs)
    
    lang_to_emps = defaultdict(list)
    for i in range(n):
        for lang in employees[i]:
            lang_to_emps[lang].append(i)
    
    dsu = DSU(n)
    for lang in lang_to_emps:
        emps = lang_to_emps[lang]
        first = emps[0]
        for emp in emps[1:]:
            dsu.union(first, emp)
    
    roots = set()
    for i in range(n):
        if len(employees[i]) > 0:
            roots.add(dsu.find(i))
    non_zero_components = len(roots)
    
    if non_zero_components ==0:
        print(n)
    else:
        print((non_zero_components -1) + zero_employees)

if __name__ == "__main__":
    main()
```
