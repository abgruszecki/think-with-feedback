<think>
Okay, let's try to solve this problem. Hmm. So the problem is about filling a grid with some constraints. Let's read it carefully.

The problem states that we have an n x m grid. Each cell is either 1 or -1. But some cells are already filled (the preserved data), and others are unknown. The key constraints are:

1. The product of each row must be -1.
2. The product of each column must be -1.
3. The number of preserved cells (k) is strictly less than max(n, m).

We need to find the number of possible valid grids that fit these conditions, modulo p.

First, let's think about the constraints. Each row's product is -1, which means that the number of -1's in the row must be odd. Because the product is the product of all elements. For example, if a row has even number of -1s, product is 1. If odd, product is -1. So each row must have an odd number of -1s. Similarly for each column: the product must be -1, so each column must have an odd number of -1s.

But wait, the rows and columns are interdependent. So, how do these constraints interact?

Let me think: Suppose we have a grid where each row product is -1. Then the product of all row products would be (-1)^n. But each column's product is -1, so the product of all column products is (-1)^m. But the product of all elements in the grid can be calculated in two ways: as the product of all row products, which is (-1)^n, or as the product of all column products, which is (-1)^m. Therefore, (-1)^n must equal (-1)^m. So n and m must have the same parity. Otherwise, there's no solution.

Wait, that's a critical point. If n and m have different parity, then it's impossible to have both row and column products being -1. Because the total product via rows would be (-1)^n, via columns (-1)^m. So for the grid to exist, n and m must be of the same parity (even or odd). If they're not, the answer is 0.

So first step: check if n and m have the same parity. If not, output 0.

But wait, what if some cells are already filled? For example, maybe the filled cells already impose that the parity is different. So even if n and m have same parity, maybe the filled cells make it impossible. So that's a possible case.

So the first thing to check is whether the given filled cells are compatible with the row and column product constraints.

But how?

Let me think. Let's model the problem.

Let's denote for each row i, the product of the preserved cells in that row. Similarly for each column j. Then, the remaining cells in the row must be filled such that the product of the entire row is -1. So the product of the remaining cells in row i must be (row_product_i) * (remaining product) = -1. So the remaining product must be (-1) / (row_product_i). Similarly for columns.

But each cell is part of a row and column. So the constraints are interdependent.

But how can we model this?

Another approach: Let's model variables for the rows and columns. Suppose that each row has a certain number of variables (unknown cells), and similarly for columns. But perhaps the problem can be reduced to a system where the variables are the rows and columns' parities, but given the constraints, some variables are determined.

Wait, perhaps the key insight is that once you set all but one rows and columns, the last row and column are determined. But there's a possibility that the constraints are conflicting.

Wait, here's an idea. The product constraints for rows and columns are such that the product of all rows' products is (-1)^n, and the product of all columns' products is (-1)^m. So if n and m have different parity, then this is impossible, so answer is 0.

But when n and m have the same parity, then it's possible. But how do the existing filled cells affect this?

Alternatively, perhaps the problem can be viewed as a system of equations. Each row contributes an equation that the product is -1, and each column contributes another equation. However, the system is over-constrained. So some conditions must be satisfied for the system to have solutions.

But how?

Let me think in terms of linear algebra. Let's model each cell as a variable that can be 1 or -1. The product constraints can be transformed into equations modulo 2. Since multiplying 1 and -1 is equivalent to summing their exponents modulo 2. For example, the product of a row being -1 is equivalent to the sum of the elements (mod 2) being 1 (since each -1 contributes 1 to the sum, and 1 contributes 0; the sum mod 2 gives the parity of the number of -1s, which must be odd).

Wait, maybe that's a better way to model this. Let's think of each cell as a variable x_ij which is 0 (if 1) or 1 (if -1). Then the row product being -1 is equivalent to the sum of x_ij in that row being 1 mod 2. Similarly, each column's sum is 1 mod 2.

So the problem reduces to solving a system of linear equations over GF(2). The variables are the cells, and the equations are:

sum_{j=1 to m} x_ij ≡ 1 (mod 2) for each row i.

sum_{i=1 to n} x_ij ≡ 1 (mod 2) for each column j.

Additionally, some variables are fixed (the preserved cells). So the problem becomes determining how many solutions exist to this system of equations, given the fixed variables.

But linear algebra over GF(2) can be used here. The system's solution space is a vector space, and the number of solutions depends on the rank of the system. If the system is consistent, the number of solutions is 2^d, where d is the number of free variables (the dimension of the solution space).

But the problem is that the system may have dependencies. For example, the sum of all row equations gives sum_{i,j} x_ij ≡ n mod 2. The sum of all column equations gives sum_{i,j} x_ij ≡ m mod 2. So for the system to be consistent, n and m must be congruent mod 2. Which aligns with our earlier observation.

So the first step is to check if n and m are of the same parity. If not, output 0.

Then, the system has equations for rows and columns. But these equations are not all independent. The sum of all row equations is equal to sum of all column equations if and only if n ≡ m mod 2.

So the system has rank (n + m - 1) if n and m are even or odd. Because the sum of all row equations equals the sum of all column equations (since n ≡ m mod 2), so the equations are dependent. So the total number of independent equations is (n + m - 1).

But also, the fixed cells (the preserved data) may introduce additional constraints. So the system's equations are a combination of the row and column equations and the fixed variables.

So, to model this, perhaps the variables are the cells, but some of them are fixed. The remaining variables are subject to the row and column constraints.

Alternatively, perhaps after substituting the fixed variables into the equations, we can model the remaining variables and the equations. Then, compute the number of free variables.

But how?

Let's proceed step by step.

First, check if n and m have the same parity. If not, output 0.

Second, check if the preserved cells already violate the constraints.

For each preserved cell, we can note that its value is fixed. For each row, compute the sum of the fixed cells in that row. Let's call this sum_fixed_row[i]. Then, the remaining variables in the row must satisfy sum_fixed_row[i] + sum_remaining_row[i] ≡ 1 mod 2. Similarly for columns.

But the problem is that the preserved cells can cause inconsistencies. For example, a row may already have sum_fixed_row[i] even, but all remaining cells in that row are already filled, so there's no way to get sum_remaining_row[i] = 1 mod 2.

But how do we check for such inconsistencies?

Alternatively, let's model the equations after substituting the fixed cells.

Each row i has:

sum (x_ij) = 1 mod 2.

sum (fixed x_ij) + sum (unknown x_ij) ≡ 1 mod 2.

So sum (unknown x_ij) ≡ (1 - sum_fixed_row[i]) mod 2.

Similarly for columns: sum (unknown x_ij) in column j ≡ (1 - sum_fixed_col[j]) mod 2.

So the equations are:

For each row i: sum (unknown variables in row i) ≡ r_i mod 2, where r_i = (1 - sum_fixed_row[i]) mod 2.

For each column j: sum (unknown variables in column j) ≡ c_j mod 2, where c_j = (1 - sum_fixed_col[j]) mod 2.

Now, the system is a combination of these row and column equations. The variables are the unknown cells (cells not in the preserved list).

But how to model the dependencies here.

Additionally, the sum of all row equations must equal the sum of all column equations.

sum r_i ≡ sum c_j mod 2.

But sum r_i = sum (1 - sum_fixed_row[i]) mod 2.

sum r_i = n - sum (sum_fixed_row[i]) mod 2.

sum c_j = m - sum (sum_fixed_col[j]) mod 2.

But since sum (sum_fixed_row[i]) is equal to the sum of all fixed cells across all rows, which is the same as sum (sum_fixed_col[j]), because it's the sum of all fixed cells. Let's call this S.

So sum r_i = (n - S) mod 2.

sum c_j = (m - S) mod 2.

But since n ≡ m mod 2, (n - m) mod 2 is 0. So (n - S) - (m - S) = n - m ≡ 0 mod 2. So sum r_i ≡ sum c_j mod 2.

Thus, the sum of the row equations is equal to the sum of the column equations, so the system is consistent in this aspect. But other constraints may make the system inconsistent.

So, after substituting the fixed variables, the system of equations (row and column equations) must be checked for consistency. If any equation is impossible (like sum_remaining in a row with no variables left but the sum must be 1 mod 2, etc.), then the answer is 0.

Otherwise, the number of solutions is 2^d, where d is the number of free variables in the system.

But how to compute d?

The system has (n + m) equations. However, one of them is redundant, as we saw. So the rank of the system is at most (n + m - 1). But the actual rank depends on the variables and equations.

But since variables are the unknown cells, which are connected in rows and columns, perhaps the system can be reduced to a certain structure.

Wait, perhaps the system can be modeled as a bipartite graph between rows and columns. Let me think.

Each unknown cell is in a row and column. So when you have an unknown cell (i,j), its x variable is part of equation i (row) and equation j (column). So the equations for row i and column j are connected through this variable.

This resembles a bipartite graph where rows and columns are nodes, and edges are the unknown variables. Each edge (i,j) represents a variable that is part of row i and column j.

But how to model this. Perhaps each variable contributes to the equations of row i and column j. So if we can model the system in terms of variables and equations, then the rank can be determined.

Alternatively, perhaps the system can be represented in terms of the variables being edges between rows and columns, and equations on rows and columns. So each row equation is the sum of variables in that row equals r_i. Each column equation is sum of variables in that column equals c_j.

In this case, the system is a bipartite graph, and the equations are the sum of variables for each row and column.

But solving such a system for GF(2) is possible. Let's think about this.

Each variable x_e (where e is an edge between row i and column j) appears in exactly two equations: row i and column j.

So, for each variable x_e, it's part of row i and column j.

The system is:

sum_{e in row i} x_e ≡ r_i mod 2, for all i.

sum_{e in column j} x_e ≡ c_j mod 2, for all j.

But how to compute the rank of this system.

This seems similar to a bipartition system. Let's consider that rows and columns are nodes, and variables are edges. Then, each variable is an edge between a row and a column.

The system of equations is such that each row node has an equation sum(edges) = r_i, and each column node has sum(edges) = c_j.

The sum of all row equations is equal to sum r_i, and the sum of all column equations is sum c_j. Since sum r_i ≡ sum c_j mod 2 (due to n ≡ m mod 2 and the way r_i and c_j are computed), the equations are dependent. So the rank is (number of row + column equations) minus 1, if the system is connected in some way.

But how?

Alternatively, the system's rank can be found by considering the connected components of the bipartite graph formed by the variables (edges). For each connected component, the equations for the nodes (rows and columns) in that component are connected, leading to a certain number of constraints.

But perhaps this is getting complicated. Let me think of an example.

Suppose there are two rows and two columns. All cells are variables. The equations are:

row1: x11 + x12 = r1

row2: x21 + x22 = r2

col1: x11 + x21 = c1

col2: x12 + x22 = c2

The sum of row equations is r1 + r2. The sum of column equations is c1 + c2. Which must be equal mod 2. But since n and m are same parity, sum r_i = sum (1 - sum_fixed_row[i]) mod 2. But if all variables are unknowns, then sum_fixed_row[i] is 0 for all i. So sum r_i = n mod 2. Similarly sum c_j = m mod 2, which are equal. So sum equations are equal.

But the system's equations here would have a rank of 3 (since 4 equations, one dependency). So the solution is 2^(4 - 3) = 2^1 = 2. Which matches the first example's output.

In the first example, n=2, m=2, k=0. So all variables are unknowns. The system has 4 equations, but one is redundant. The rank is 3. The number of variables is 4. So the solution is 2^(4-3) = 2. Which matches the sample output.

So, the approach is to model the variables as edges in a bipartite graph between rows and columns. The number of solutions is 2^d, where d is the number of variables (unknown cells) minus (rank of the system).

But how to compute the rank.

The key insight here is that the bipartite graph (rows and columns as nodes, edges as variables) forms connected components. For each connected component, the number of independent equations is (number of nodes in component) - 1. Because the sum of all equations in a connected component must be equal to the sum of the right-hand sides mod 2. But this introduces a dependency.

Thus, for each connected component, the rank is (number of nodes in component) - 1. The total rank is (total nodes across all components) - (number of components). Since each component contributes (size - 1) to the rank.

But the nodes are the rows and columns. So the bipartite graph's connected components are determined by the variables (unknown cells). For each unknown cell (i,j), there's an edge between row i and column j.

Thus, the bipartite graph is formed by the rows and columns connected via the unknown cells. Each connected component can be handled separately.

So, for each connected component, the number of equations (rows and columns in the component) is (a + b), where a is the number of rows in the component, and b the number of columns. The number of equations is (a + b). But the sum of all equations in the component is a constraint, so the rank is (a + b - 1).

Thus, the total rank across all components is sum over all components of (a + b - 1) for each component. But sum (a) over all components is the number of rows (n) plus the number of columns (m). Wait, no. Because a row or column can be part of exactly one component. So sum (a) for all components is the number of rows, and sum (b) is the number of columns.

So sum (a + b) over all components is (n + m). But each component contributes (a + b - 1) to the rank. So total rank is (n + m - c), where c is the number of connected components.

Thus, the rank of the system is (n + m - c - 1), since sum (a + b - 1) for all components is (n + m) - c.

Wait, wait. Let's think again. For each component, the rank is (number of nodes in the component) - 1. The number of nodes in the component is a (rows) + b (columns). So the component contributes (a + b -1) to the rank.

If there are c components, then sum (a + b -1) = (sum (a + b)) - c.

But sum (a) over all components is n (since each row is in exactly one component), sum (b) is m (same for columns). So sum (a + b) is n + m.

Thus, total rank is (n + m) - c - c? Wait, no. sum (a + b -1) = sum (a + b) - sum(1) for each component. sum (a + b) is (n + m), and sum(1) is c. So total rank is (n + m) - c.

Wait, that's right. For each component, (a + b -1) = (number of nodes) -1. So sum over all components is sum (number of nodes per component) - c. Since each component is considered once.

But the sum of the number of nodes per component is (number of rows + columns in the bipartite graph) which is n + m. So sum (number of nodes per component) is n + m. Therefore, the total rank is (n + m) - c.

But how does this relate to the total equations?

The original system has (n + m) equations, but one global dependency (the sum of row equations equals the sum of column equations). So the total number of independent equations is (n + m -1). But according to this approach, the rank is (n + m) - c. So this suggests that the two must be equal.

Wait, perhaps this is not the case. Because the bipartition approach and the system of equations may have different dependencies. So perhaps this needs a deeper analysis.

Alternatively, let's consider that each connected component contributes (number of nodes in component -1) to the rank. So for the entire graph, the total rank is sum (nodes_in_component -1) for all components) = (sum nodes_in_component) - c) = (n + m) - c. But the original system's equations are (n + m) equations with one dependency (sum row equations ≡ sum column equations mod 2). So the system's total rank is (n + m -1). However, according to the bipartition approach, the rank is (n + m - c). So (n + m - c) must equal (n + m -1) minus some other dependencies. This doesn't seem to add up. So perhaps I'm missing something here.

Alternatively, perhaps the bipartition approach is correct, and the total rank is (n + m - c) - 1. Because the sum of all equations is a dependency.

Wait, perhaps the system's equations can be viewed as follows:

Each connected component's equations can be solved, but there's a global dependency. So the bipartition approach's rank is (n + m - c), but the system's overall rank is (n + m - c) - 1. Because the sum of all equations is zero.

Hmm, this is getting confusing. Let's think of the sample input.

Sample 1:

n=2, m=2, k=0. All cells are unknown. So the bipartition graph is a connected component with 2 rows and 2 columns. The number of connected components c is 1.

According to the bipartition approach, the rank is (n + m - c) = 2 + 2 -1 = 3. Which matches the sample's case where the system has 4 equations with rank 3 (since one is dependent). So the solution is 2^(4 variables - 3) = 2^1 = 2. Which matches the sample.

Another example: suppose there are two connected components.

If c=2, then the rank would be (n + m - 2). But if the sum of all equations is a dependency, then the total rank would be (n + m - 2 -1) ?

Not sure.

Alternatively, perhaps the bipartition approach correctly computes the rank as (n + m - c). Then, the number of free variables is the number of variables (unknown cells) minus (n + m - c - 1), since there's a global dependency. Wait, no. Because the sum of all row equations and column equations must agree. So the total rank is (n + m - c) - 1? Or is the global dependency already accounted for in the bipartition approach.

Alternatively, the bipartition approach's rank (n + m -c) already includes the dependencies. Because when considering connected components, each component's equations are independent of the others, except for the global dependency.

Wait, perhaps in the bipartition approach, the rank is (n + m - c) and the global dependency is already considered. For example, the sample input has c=1. So the rank is 2+2-1=3, which aligns with the sample. Then, the number of solutions is 2^(E - R), where E is the number of variables (unknown cells) and R is the rank. So E is the number of unknown cells, which is (n * m) - k.

But wait, the sample input has n=2, m=2, k=0. So E=4. R=3. So 4-3=1. So 2^1=2. Correct.

Another example: if there are two connected components, say, each contributing (a + b -1) equations, then the total rank is sum (a + b -1) = (n + m) - c. So if c=2, then the rank is (n + m -2). But what is E in that case?

E is the number of variables (edges) in the bipartition graph. So variables are the unknown cells, which are edges in the bipartition graph. So E is the total number of edges (unknown cells) across all components.

So the number of solutions is 2^(E - (n + m - c) ) ?

Wait, no. Because the bipartition approach's rank is (n + m -c). So the number of free variables is E - (n + m -c). So the number of solutions is 2^(E - (n + m -c) + 1) ?

Wait, I'm getting stuck here. Let's try to re-express.

The number of variables is E (unknown cells).

The rank is R = (n + m - c). So the number of solutions is 2^(E - R), but only if the system is consistent.

But wait, in the sample input, R=3, E=4. 4-3=1. So 2^1=2. Which is correct.

So the formula seems to be 2^(E - R) when the system is consistent.

But why?

Because each equation reduces the degrees of freedom by 1, assuming the equations are independent. So the number of solutions is 2^(variables - rank).

So, if the system is consistent, then the answer is 2^(E - R), where R is the rank of the system.

Thus, the steps are:

1. Check if n and m have the same parity. If not, output 0.

2. Check the preserved cells for contradictions. For example, a row where the sum of fixed cells is s, and the remaining variables in the row have no unknowns but s + 0 is not congruent to 1 mod 2. Then, impossible.

3. For each row and column, compute the required sum for the remaining variables (r_i and c_j).

4. Build a bipartite graph where nodes are rows and columns, and edges represent the unknown cells.

5. For each connected component in this bipartite graph:

   a. Check if the sum of (r_i for rows in the component) plus (c_j for columns in the component) is even. Because the sum of equations in the component must equal the sum of the required sums. If not, no solution.

   Wait, for each connected component, the sum of the row equations and column equations in the component must be equal. Because each equation in the component is part of the component's connected graph. Let me think.

In a connected component, the sum of all row equations (sum x_ij ≡ r_i) for rows in the component plus the sum of column equations (sum x_ij ≡ c_j) for columns in the component) must be congruent to the sum of the variables in the component.

But each variable is part of exactly one row and column, so each variable is counted twice in the sum of all equations. So sum equations in component is sum (r_i) + sum (c_j) ≡ sum variables (x) * 2 ≡ 0 mod 2. So sum (r_i) + sum (c_j) ≡ 0 mod 2. So for each connected component, sum (r_i) + sum (c_j) must be even. Otherwise, no solution.

So for each connected component, we need to check that the sum of all r_i (rows in component) and sum of all c_j (columns in component) is even. If not, output 0.

Thus, the steps are:

For each connected component in the bipartite graph of unknown cells:

   sum_r = sum of r_i for rows in the component.

   sum_c = sum of c_j for columns in the component.

   if (sum_r + sum_c) % 2 != 0 → no solution.

So, if any component fails this check, the answer is 0.

Otherwise, the number of solutions is 2^(E - (n + m - c)), where E is the number of unknown cells, and c is the number of connected components in the bipartite graph.

Thus, the formula is:

number_of_solutions = 2^( (E) - (n + m - c) ) )

But how to compute E, c, and check the sum for each component.

Now, the steps to implement this:

1. Check if n and m have different parity. If yes, output 0.

2. Read the k preserved cells. For each cell (a, b, c), note that the cell is fixed. So store the values in a dictionary.

3. For each row i (1-based?), compute sum_fixed_row[i] = sum of preserved cells in row i. Each preserved cell is either 1 or -1, which we can convert to 0 or 1 (since x_ij is 0 for 1, 1 for -1).

   Similarly, compute sum_fixed_col[j] for each column j.

4. For each row i, compute r_i = (1 - sum_fixed_row[i]) % 2. This is the required sum of the unknown variables in row i.

   For each column j, compute c_j = (1 - sum_fixed_col[j]) % 2.

5. Now, check for any row i where the number of unknown variables is 0. For example, if all cells in row i are preserved. Then, check if r_i is 0. If not (sum of unknown is r_i, but unknown variables are zero), then the row is impossible. So output 0.

   Similarly for columns j. If all cells in column j are preserved and c_j is not zero, then output 0.

   But how to compute this:

   For a row i, the number of unknown cells is m - (number of preserved cells in row i). If this is zero, then sum_fixed_row[i] must be congruent to 1 mod 2. Otherwise, impossible.

   So for each row i:

      num_unknown = m - (number of preserved cells in row i)

      if num_unknown == 0 and (sum_fixed_row[i] % 2) != 1 → impossible.

   Similarly for columns j:

      num_unknown = n - (number of preserved cells in column j)

      if num_unknown == 0 and (sum_fixed_col[j] % 2) != 1 → impossible.

   If any of these checks fail, output 0.

6. Now, build the bipartite graph of unknown cells. Each unknown cell is an edge between row i and column j. For this, we need to find all cells not present in the preserved list.

   But how to do this efficiently.

   The preserved cells are stored in a set, so for each row i and column j, if (i, j) is not in the preserved set, then it's an unknown cell, and an edge in the bipartition graph.

   However, for n and m up to 1000, this is O(n*m), which is 1e6. Which is manageable, but in the worst case, when k is small (like 0), this would be O(1e6), which is acceptable.

   But wait, in the problem statement, k can be up to max(n, m) -1. So for n=1000, m=1000, k=999, this approach would generate 1e6 - 999 edges, which is still 999001 edges. Which is manageable, but perhaps we need a better way.

   Alternatively, the bipartition graph can be represented using adjacency lists. For each row, collect the unknown cells (columns j where (i,j) is not preserved), and similarly for columns.

   But for 1e3 rows and columns, and up to 1e6 edges, this is manageable.

7. Once the bipartition graph is built, find the connected components. For each connected component (which consists of some rows and columns connected via edges), compute sum_r (sum of r_i for rows in component) and sum_c (sum of c_j for columns in component). If sum_r + sum_c is odd, output 0.

8. Count the number of connected components (c).

9. Compute E, the number of unknown cells (edges in the bipartition graph). This is (n*m - k), since there are k preserved cells.

10. The answer is 2^(E - (n + m - c)) mod p.

But wait, how to compute E?

E is the number of unknown cells, which is (n * m - k). Because the preserved cells are exactly k, so the rest are unknowns.

So, yes.

So the formula is 2^(E - (n + m - c)) mod p, provided all the consistency checks are passed.

Now, the steps are:

- Check n and m parity. If different, output 0.

- Check each row and column for preserved cells that make it impossible (no unknowns but required sum is wrong).

- Build bipartition graph and check connected components for sum_r + sum_c even.

If all checks pass, compute the answer as 2^d mod p, where d = E - (n + m - c).

But how to compute c (number of connected components in bipartition graph) and the sum_r and sum_c per component.

Now, how to represent the bipartition graph. Since rows and columns are nodes, perhaps we can model them with a Union-Find (Disjoint Set Union) data structure. But since the nodes are rows and columns (which are separate entities), we can represent rows as 0..n-1 and columns as n..n+m-1. Then, for each unknown cell (i, j), we connect row i and column j.

But how to model this. Let's think of the bipartition graph as a graph where each node is either a row or a column. So for each unknown cell (i,j), we add an edge between row i and column j. Then, the connected components can be found using DSU.

Each time we add an edge between i and j, we can union the DSU of row i and column j.

Thus, the DSU will manage the connected components of rows and columns. The total number of nodes in the DSU is (n + m). For each unknown cell, we perform a union between row i and column j.

Once all edges are processed, the DSU will group rows and columns into connected components.

For each connected component, we need to collect all the rows and columns in that component, then compute sum_r and sum_c for that component.

So steps:

Initialize DSU with (n + m) nodes. Rows are numbered 0 to n-1. Columns are numbered n to n + m -1.

For each unknown cell (i, j) (i ranges from 1 to n, j from 1 to m):

   convert to 0-based: row is i-1, column is j-1 + n.

   union these two nodes.

Once all edges are processed, the DSU will have grouped connected components.

Then, for each component in the DSU, collect all rows and columns in it.

For each component:

   sum_r = sum of r_i for rows in component.

   sum_c = sum of c_j for columns in component.

   if (sum_r + sum_c) % 2 != 0 → invalid.

If any component is invalid, output 0.

Otherwise, the answer is 2^( (E - (n + m - c)) ) mod p.

So, how to compute E:

E is the number of unknown cells. Which is (n * m - k).

But the problem statement says k is given. So E = n * m - k.

But we need to verify that k is less than max(n, m). However, the problem says that k is given as such. So we can proceed.

Now, the code steps:

Implement the DSU.

Read n, m.

Check if (n % 2) != (m % 2). If yes, output 0.

Read k.

Read the k preserved cells. For each cell, store (a-1, b-1, c). Because rows and columns are 0-based in the code.

Build a set of preserved cells.

For each row i (0-based):

   sum_fixed_row[i] = sum of preserved cells in row i. For each preserved cell (i, j) in the row, add 1 if c is -1 (since x_ij is 1 for -1). Each preserved cell in row i has x_ij = 1 if c is -1, 0 otherwise.

   sum_r[i] = (1 - sum_fixed_row[i]) % 2.

Similarly for columns:

sum_fixed_col[j] = sum of preserved cells in column j. For each preserved cell (i, j) in column j, add 1 if c is -1.

sum_c[j] = (1 - sum_fixed_col[j]) % 2.

Check for rows with no unknown cells (m - preserved_in_row[i] == 0):

   if sum_fixed_row[i] % 2 != 1 → output 0.

Check for columns with no unknown cells (n - preserved_in_col[j] == 0):

   if sum_fixed_col[j] % 2 != 1 → output 0.

Build the DSU for rows and columns.

For each cell (i, j) in 0-based:

   if (i, j) is not in preserved set → add edge between row i and column j (i and n + j).

So for each unknown cell, union i and (n + j).

Once DSU is built, collect the components.

For each component in DSU:

   collect all row nodes (0..n-1) and column nodes (n..n+m-1) in the component.

   sum_r_in_component = sum of sum_r[i] for rows i in component.

   sum_c_in_component = sum of sum_c[j] for columns j in component (j is (component_node - n)).

   if (sum_r_in_component + sum_c_in_component) % 2 != 0 → output 0.

If all components pass, compute c as the number of connected components (from DSU). How to compute c: the number of unique parents in the DSU.

But the DSU's parent array can be used to count the number of unique roots.

But need to process all nodes (rows and columns) in the DSU. However, some nodes may not have any edges (if all their cells are preserved). In this case, they form a component by themselves.

But wait, the bipartition graph only includes nodes that are connected by edges. Or wait, the DSU includes all rows and columns, even if they have no edges. Because for example, a row with all cells preserved will have no edges, and will be in a component by itself. Similarly for a column with all cells preserved.

But in the bipartition graph, the nodes are rows and columns, and edges are the unknown cells. So a row with all cells preserved has no edges, and is in a component by itself. Similarly for a column with all cells preserved.

So the DSU must include all rows and columns, even those with no edges. Because they can form components of size 1 (row) or 1 (column), etc.

So when building the DSU, initially all rows and columns are separate. Then, for each unknown cell, we union the row and column. So rows and columns not connected by any edge will remain as individual components.

Thus, the DSU must be initialized with all rows and columns as separate nodes, then edges are added via unions.

So after processing all edges (unknown cells), each component is a group of rows and columns connected via edges.

Now, for each component (which may consist of rows and columns), but also, for components that are single rows or columns (if they have no edges), we need to check if their sum_r and sum_c are compatible.

Wait, no. Because a component is a set of rows and columns connected via edges. So a component that is a single row would have no edges (so no columns in the component). But how can a row be in a component by itself? Because edges are between row and column. So a row i can only be part of a component if there's a path connecting it via edges (unknown cells) to other nodes. If a row has all cells preserved (so no edges), then in the DSU, it's a component of size 1 (the row itself). Similarly for a column.

But such a row (with no edges) must have sum_r[i] equal to 0. Because if a row has no unknown cells, then sum_fixed_row[i] must be 1 mod 2 (checked earlier). So sum_r[i] is (1 - sum_fixed_row[i]) mod 2, which is 0. So sum_r[i] is 0. So for a component consisting of just row i, sum_r is 0, sum_c is 0 (since no columns). sum_r + sum_c = 0 → even. So it's valid.

Similarly for a component that is a single column j. sum_c[j] is 0 (since all cells in column are preserved), and sum_r is 0. So sum_r + sum_c = 0 → even.

Thus, components that are single rows or columns (with no edges) are valid.

So the code must process all components, including those with only rows or columns.

Thus, after building the DSU, the code must collect all components (each group of connected nodes) and compute sum_r and sum_c for each component.

But how to collect all the components:

We can iterate through all nodes (rows and columns) and track their root. For each root, collect all the nodes in that component.

But rows are 0..n-1, columns are n..n+m-1.

So for all nodes in 0..n+m-1:

   find their root.

   group them by root.

Then, for each group (component):

   collect the rows (nodes < n) and columns (nodes >=n) in the component.

   sum_r = sum sum_r[i] for each row i in component.

   sum_c = sum sum_c[j] for each column j (j = node - n) in component.

   check if (sum_r + sum_c) % 2 == 0. If not, invalid.

If any component fails this check, output 0.

Now, let's think about how to handle this in code.

Implementing this in Python:

First, read n and m.

Check if (n + m) % 2 is 1. Wait, no. Wait, n and m must have the same parity. So (n % 2) == (m % 2). So if n is even and m is odd, no solution.

So code:

if (n % 2) != (m % 2):
    print(0)
    exit()

Then read k.

preserved = a dictionary (set) of preserved cells (i, j), and their values.

sum_fixed_row = array of size n, initialized to 0.

sum_fixed_col = array of size m, initialized to 0.

preserved_in_row = array of size n, counts how many preserved cells are in each row.

preserved_in_col = array of size m, counts how many preserved cells are in each column.

for each preserved cell in input:
    a, b, c = input().split()
    a = int(a) -1  # 0-based row
    b = int(b) -1  # 0-based column
    val = 1 if c == '-1' else 0  # because x_ij is 1 for -1, 0 for 1.

    # check if (a, b) is already in preserved (given in the problem statement, but code may not be needed as input ensures no duplicates)
    # but code can proceed.

    sum_fixed_row[a] += val
    sum_fixed_col[b] += val

    preserved_in_row[a] += 1
    preserved_in_col[b] += 1

    # add to preserved set
    preserved.add( (a, b) )

Then, check each row for no unknowns and sum_fixed_row[i] %2 !=1:

for i in range(n):
    if preserved_in_row[i] == m:
        # all cells in row i are preserved
        if (sum_fixed_row[i] % 2) != 1:
            print(0)
            exit()

for j in range(m):
    if preserved_in_col[j] == n:
        if (sum_fixed_col[j] % 2) !=1:
            print(0)
            exit()

Then, compute sum_r and sum_c for each row and column:

sum_r = [ (1 - (sum_fixed_row[i] % 2)) % 2 for i in range(n) ]

sum_c = [ (1 - (sum_fixed_col[j] %2 )) % 2 for j in range(m) ]

Then, build the DSU for rows and columns:

rows are 0..n-1, columns are n..n+m-1.

Implement DSU:

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

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

dsu = DSU(n + m)

Then, for each cell (i, j) not in preserved, union row i and column j.

for i in range(n):
    for j in range(m):
        if (i, j) not in preserved:
            # row i is i, column j is n + j
            dsu.union(i, n + j)

Now, collect the components:

components = defaultdict(list)
for node in range(n + m):
    root = dsu.find(node)
    components[root].append(node)

Then, for each component:

for comp in components.values():

    rows_in_comp = [x for x in comp if x < n]
    cols_in_comp = [x - n for x in comp if x >=n]

    s_r = sum( sum_r[i] for i in rows_in_comp )
    s_c = sum( sum_c[j] for j in cols_in_comp )

    if (s_r + s_c) % 2 !=0:
        print(0)
        exit()

Now, compute c, the number of components:

c = len(components)

Compute E = n * m - k.

Compute exponent = E - (n + m - c)

But wait, the formula is exponent = (E - (n + m - c)) ?

Yes. Because the rank R is (n + m - c). So variables E minus rank R.

So exponent = E - R = E - (n + m - c).

Then, compute pow(2, exponent, p).

But wait, what if exponent is negative? That's impossible because:

E is the number of variables (unknown cells), which is (n*m -k). According to the problem statement, k < max(n, m). So E ≥ (n*m - max(n, m)).

But the rank R is (n + m - c). We need to ensure that exponent is >=0.

But how?

Since c is the number of connected components in the bipartition graph. The minimum possible value of c is 1 (all rows and columns connected). Maximum possible c is n + m (no edges, each node is a component).

But with edges, c can be up to min(n, m) + ... but it's not important.

But for the formula exponent = E - (n + m - c), the exponent must be >=0 for the solution to exist.

But how to ensure this?

In the problem statement, it's given that k < max(n, m). So E = n*m -k >= n*m - (max(n,m) -1). For example, if n=1000, m=500, then max(n,m) is 1000. So E >= 1000 * 500 - 999 = 500000 - 999= 499,001. So the exponent could be large.

But in code, we have to compute the exponent as (n*m -k) - (n + m - c). Which could be negative. But that would imply that the system is impossible, but our earlier checks passed.

So this is impossible.

Wait, no. How can E - (n + m -c) be negative?

E is the number of variables. R is (n + m -c). So E >= R? Not necessarily. But according to the problem's constraints, k < max(n, m). So E = n*m -k >= n*m - (max(n,m) -1).

So for n and m >=1, n*m is >= max(n,m). So E >= (max(n,m) - (max(n,m) -1)) = 1. But when n and m are large, the exponent could be E - (n +m -c). For example, n=1000, m=1000, k=0. Then E=1e6. R = (1000 + 1000 - c). So exponent is 1e6 - (2000 - c). If c=1, exponent is 1e6 - 1999 = 998001.

Which is positive.

But if c is large, like n + m, then (n +m -c) becomes negative. For example, n=2, m=2, c=4 (four components). Then R = 2+2 -4 = 0. So exponent E=4 -0=4. Which is correct for the first sample, but wait in the first sample, c is 1. So maybe my example is not correct.

Alternatively, perhaps when there are many components, like when all edges are present, but components are large. Hmm, this is getting complicated.

But according to the code, the exponent can be calculated as E - (n +m -c). So even if it's negative, the code would return 2^exponent. Which could be 0 in modulo p (if exponent is negative). But according to our earlier steps, this is not possible. Because the code should have passed all the checks. So why would exponent be negative?

It's possible that when the number of variables is less than (n + m -c). For example, if the number of edges is 0. But in this case, E=0. (n +m -c) = n +m - (n +m) ) =0. So exponent is 0. So 2^0=1.

But how?

Suppose n=1, m=1. Then, if k=0 (E=1). Check if n and m have same parity. Yes. Then, the component is row 0 and column 0 connected via the cell (0,0). So c=1. So exponent = 1 - (1+1-1) = 1-1=0. So 1 solution.

But what's the solution? The cell must be filled with a value such that row product is -1 and column product is -1. So the cell is -1. So one solution. So code is correct.

Another example: n=2, m=2, k=0. E=4. c=1. exponent 4 - (2+2-1) = 4-3=1. 2^1=2. Which is correct.

But in cases where E < (n +m -c), exponent would be negative. But how can this happen?

For example, n=3, m=3, k=8. So E=9-8=1. c= ?

Assuming that the one unknown cell is (i,j). The DSU would union row i and column j. So c = (3 rows + 3 columns) - 1 + 1? Not sure. The DSU would have row i and column j connected. The other rows and columns are separate. So the total components:

rows 0, 1, 2 and columns 0,1,2 (assuming the unknown cell is (0,0)). Then, components are:

- row 0 and column 0 → component 1.

- row1 → component 2.

- row2 → component3.

- column1 → component4.

- column2 → component5.

So total c=5.

So (n +m -c) = 3+3-5=1. So exponent=1-1=0. So 2^0=1.

Which is correct. Because the one unknown cell must be filled to satisfy both row and column.

So yes, in this case, exponent is 0.

Thus, even if E=1 and R=1, exponent is 0. So 2^0=1.

So code seems to handle this correctly.

So the code can proceed.

Finally, compute the result as pow(2, exponent, p).

But wait, exponent can be negative? How?

Suppose E=3, R=5. Then exponent is -2. 2^-2 mod p is not possible. So code would output 0, but according to the problem's constraints, this is impossible. So why can't this happen?

Because the code's earlier checks should ensure that the system is consistent, and thus the exponent is non-negative.

But how?

For example, if E=3 and R=5. Then, variables =3, equations =5. Which is impossible. So the system is over-constrained and thus no solution. But according to the code's earlier steps, this would have been detected.

But how?

Because when variables are 3 and the rank is 5, which is impossible. But the code's earlier steps would have found that the system is inconsistent. But in our steps, the code's checks include:

- Each component's sum_r + sum_c is even.

But perhaps in some cases, even with exponent being negative, the system is inconsistent.

But according to the code's steps, if the system is consistent (sum_r + sum_c even for each component), then the exponent is (E - R) and the answer is 2^exponent.

But how to ensure that E >= R.

But in our previous example, n=3, m=3, k=8, E=1. R=3+3 -c. c=5. So R=6-5=1. E-R=0.

Thus, E >= R in that case.

Another example: n=2, m=2, k=3. E=4-3=1.

Assume the one unknown cell is (0,0). So in the DSU, row 0 and column 0 are connected. So components:

row0 and column0 → component 1.

row1 → component2.

column1 → component3.

So c=3.

R = 2+2 -3=1.

E-R=0.

So exponent=0.

So 2^0=1.

Thus, code returns 1.

Which is correct, because the unknown cell's value must be chosen to satisfy row and column.

Thus, the code works.

So the code is correct.

Now, the code steps are:

Implement all the checks and steps as outlined.

Now, the code must be optimized for speed and memory.

Potential optimizations:

- The DSU can be implemented with path compression and union by rank, which is efficient.

- The preserved cells can be stored in a set of tuples for quick lookups.

- The loops for rows and columns can be optimized.

But for n and m up to 1e3, the code should be manageable.

Now, implementing the code in Python.

But there's a problem: for the bipartition graph, iterating over all n*m cells and checking if (i,j) is not in preserved. For n=1e3 and m=1e3, this is 1e6 iterations, which is acceptable.

But in Python, for 1e6 iterations, it's manageable, but the code should be optimized.

But given that the time limit is 2 seconds, which is tight for Python.

Alternative approach: precompute all unknown cells and process them.

But how to find unknown cells.

The preserved cells are stored in a set. So for each i in 0..n-1:

   for j in 0..m-1:

       if (i,j) not in preserved:

           add the edge between i and j.

But for n=1e3 and m=1e3, this is 1e6 iterations. In Python, each 'if (i,j) in preserved' is O(1), but with a hash lookup. So 1e6 iterations may take some time.

Alternative approach: for each row, track the preserved columns, then for each row, the unknown columns are those not in the preserved set. But in Python, this can be done via set operations. For example, for each row i, the preserved columns are stored in a dictionary, and the unknown columns are m - preserved_in_row[i]. But to get the list of columns in row i that are preserved, perhaps it's not stored, so this may not help.

But given the time constraints, the code must be as efficient as possible.

Alternatively, the code can process the DSU edges as follows:

For each cell (i,j) not in the preserved set:

   union row i and column j.

But how to iterate over all (i,j) not in preserved.

But given that preserved has k elements, and k < max(n, m), which for n=1e3, m=1e3, k is up to 999.

So the number of unknown cells is 1e6 - 999 = 999001. So in the worst case, we have 1e6 iterations. Which may be manageable.

But in Python, 1e6 loops are acceptable in 2 seconds, but with some optimizations.

Thus, the code can proceed as described.

Now, implementing the code.

Testing against sample input 1.

```python
import sys
from sys import stdin
from collections import defaultdict


class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
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
    n, m = map(int, input_stream.readline().split())
    if (n % 2) != (m % 2):
        print(0, file=output_stream)
        return
    k = int(input_stream.readline())
    preserved = dict()
    sum_fixed_row = [0] * n
    sum_fixed_col = [0] * m
    preserved_in_row = [0] * n
    preserved_in_col = [0] * m
    for _ in range(k):
        a, b, c = input_stream.readline().split()
        a = int(a) - 1
        b = int(b) - 1
        val = 1 if c == '-1' else 0
        sum_fixed_row[a] += val
        sum_fixed_col[b] += val
        preserved_in_row[a] += 1
        preserved_in_col[b] += 1
        preserved[(a, b)] = True
    # Check rows with all preserved and sum_fixed_row not 1 mod 2
    for i in range(n):
        if preserved_in_row[i] == m:
            if (sum_fixed_row[i] % 2) != 1:
                print(0, file=output_stream)
                return
    for j in range(m):
        if preserved_in_col[j] == n:
            if (sum_fixed_col[j] % 2) != 1:
                print(0, file=output_stream)
                return
    sum_r = [(1 - (sum_fixed_row[i] % 2)) % 2 for i in range(n)]
    sum_c = [(1 - (sum_fixed_col[j] % 2)) % 2 for j in range(m)]
    # Build DSU for rows and columns
    dsu = DSU(n + m)
    for i in range(n):
        for j in range(m):
            if (i, j) not in preserved:
                row_node = i
                col_node = n + j
                dsu.union(row_node, col_node)
    # Collect components
    components = defaultdict(list)
    for node in range(n + m):
        root = dsu.find(node)
        components[root].append(node)
    # Check each component's sum_r and sum_c
    for nodes in components.values():
        rows = []
        cols = []
        for node in nodes:
            if node < n:
                rows.append(node)
            else:
                cols.append(node - n)
        s_r = sum(sum_r[i] for i in rows)
        s_c = sum(sum_c[j] for j in cols)
        if (s_r + s_c) % 2 != 0:
            print(0, file=output_stream)
            return
    c = len(components)
    E = n * m - k
    exponent = E - (n + m - c)
    p = int(input_stream.readline())
    print(pow(2, exponent, p), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 2
1
1 1 -1
100
""",
            "output": \
"""\
1
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

Sample 2:

input:

2 2

1

1 1 -1

100

So preserved cell is (0,0) with value -1.

sum_fixed_row[0] = 1 (because -1 is 1 in x_ij).

sum_fixed_col[0] = 1.

sum_r[0] = (1 -1) mod2=0.

sum_r[1] = (1 -0) mod2=1.

sum_c[0] = (1-1) mod2=0.

sum_c[1] = (1-0) mod2=1.

Check rows and columns:

Row 0: preserved_in_row[0] =1 (m=2, so unknowns possible).

Row1: preserved_in_row[1] =0 (so unknowns possible).

Columns 0: preserved_in_col[0] =1 (n=2, so unknowns possible.

Column1: preserved_in_col[1] =0.

No rows or columns have all cells preserved.

Now, the DSU edges:

Unknown cells are (0,1), (1,0), (1,1).

For each cell:

(0,1): union 0 (row0) and 3 (column1).

(1,0): union 1 (row1) and 2 (column0).

(1,1): union 1 (row1) and 3 (column1).

So the components:

Row0 is connected to column1 (through cell (0,1)). Row1 is connected to column0 (cell (1,0)), and column1 (cell (1,1)). So all rows and columns are connected. So c=1.

Now, sum_r for the component:

sum_r[0] + sum_r[1] = 0 +1 =1.

sum_c[0] + sum_c[1] =0 +1=1.

Total sum_r + sum_c=2 → even.

Exponent = 3 (4-1=3) - (2+2-1) →3 -3=0. So 2^0=1. Output 1.

Which matches the sample.

Thus, the code works.

Now, the code can be written.
</think>

```python
import sys
from sys import stdin
from collections import defaultdict

class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
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
    n, m = map(int, stdin.readline().split())
    if (n % 2) != (m % 2):
        print(0)
        return
    k = int(stdin.readline())
    preserved = dict()
    sum_fixed_row = [0] * n
    sum_fixed_col = [0] * m
    preserved_in_row = [0] * n
    preserved_in_col = [0] * m
    for _ in range(k):
        a, b, c = stdin.readline().split()
        a = int(a) - 1
        b = int(b) - 1
        val = 1 if c == '-1' else 0
        sum_fixed_row[a] += val
        sum_fixed_col[b] += val
        preserved_in_row[a] += 1
        preserved_in_col[b] += 1
        preserved[(a, b)] = True
    # Check rows with all preserved and sum_fixed_row not 1 mod 2
    for i in range(n):
        if preserved_in_row[i] == m:
            if (sum_fixed_row[i] % 2) != 1:
                print(0)
                return
    for j in range(m):
        if preserved_in_col[j] == n:
            if (sum_fixed_col[j] % 2) != 1:
                print(0)
                return
    sum_r = [(1 - (sum_fixed_row[i] % 2)) % 2 for i in range(n)]
    sum_c = [(1 - (sum_fixed_col[j] % 2)) % 2 for j in range(m)]
    # Build DSU for rows and columns
    dsu = DSU(n + m)
    for i in range(n):
        for j in range(m):
            if (i, j) not in preserved:
                row_node = i
                col_node = n + j
                dsu.union(row_node, col_node)
    # Collect components
    components = defaultdict(list)
    for node in range(n + m):
        root = dsu.find(node)
        components[root].append(node)
    # Check each component's sum_r and sum_c
    for nodes in components.values():
        rows = []
        cols = []
        for node in nodes:
            if node < n:
                rows.append(node)
            else:
                cols.append(node - n)
        s_r = sum(sum_r[i] for i in rows)
        s_c = sum(sum_c[j] for j in cols)
        if (s_r + s_c) % 2 != 0:
            print(0)
            return
    c = len(components)
    E = n * m - k
    exponent = E - (n + m - c)
    p = int(stdin.readline())
    print(pow(2, exponent, p))

if __name__ == "__main__":
    main()
```
