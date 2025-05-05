n = int(input())

a = list(map(int, input().split()))

edges = [[] for _ in range(n)]

for _ in range(n-1):

   u, v = map(int, input().split())

   u -=1

   v -=1

   edges[u].append(v)

   edges[v].append(u)

# Precompute smallest prime factors (SPF) up to 2e5.

max_a = 2 *10**5

spf = list(range(max_a +1))

for i in range(2, int(max_a**0.5) +1):

   if spf[i] == i:

       for j in range(i*i, max_a+1, i):

           if spf[j] == j:

               spf[j] = i

# Function to get unique primes of x

def get_primes(x):

   primes = set()

   if x ==1:

       return primes

   while x !=1:

       p = spf[x]

       primes.add(p)

       while x % p ==0:

           x = x//p

   return primes

# For each node, get its primes.

primes_list = [get_primes(x) for x in a]

# Build prime_to_nodes dictionary.

from collections import defaultdict

prime_to_nodes = defaultdict(list)

for i in range(n):

   for p in primes_list[i]:

       prime_to_nodes[p].append(i)

max_diameter = 0

# For each prime in prime_to_nodes, process its nodes.

for p, nodes in prime_to_nodes.items():

   m = len(nodes)

   if m ==0:

       continue

   # The maximum possible diameter for this group is at least 1 (if m >=1)

   # But maybe there's a larger one.

   # We need to process connected components.

   # Create a visited array for this group.

   visited = [False]*n

   # Iterate through all nodes in nodes.

   for u in nodes:

       if not visited[u]:

           # BFS to find connected component.

           component = []

           q = deque([u])

           visited[u] = True

           component.append(u)

           while q:

               current = q.popleft()

               for v in edges[current]:

                   if not visited[v] and p in primes_list[v]:

                       visited[v] = True

                       q.append(v)

                       component.append(v)

           # Compute diameter of this component.

           # component is a list of nodes.

           # component_set = set(component)

           # compute diameter.

           if not component:

               continue

           # First BFS to find farthest node.

           start = component[0]

           max_dist = 1

           farthest_node = start

           visited_bfs = {node:False for node in component}

           q = deque([(start, 1)])

           visited_bfs[start] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

                   farthest_node = node

               for v in edges[node]:

                   if v in component and not visited_bfs[v]:

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # Second BFS from farthest_node.

           max_dist = 1

           visited_bfs = {node:False for node in component}

           q = deque([(farthest_node, 1)])

           visited_bfs[farthest_node] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

               for v in edges[node]:

                   if v in component and not visited_bfs[v]:

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # Update max_diameter.

           if max_dist > max_diameter:

               max_diameter = max_dist

print(max_diameter if max_diameter >=1 else 0)