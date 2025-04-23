import sys

from sys import stdin

from collections import defaultdict, deque

def main():

    data = list(map(int, stdin.read().split()))

    ptr = 0

    t = data[ptr]

    ptr +=1

    for _ in range(t):

        n = data[ptr]

        m = data[ptr+1]

        ptr +=2

        a = data[ptr:ptr+n]

        ptr +=n

        adj = [[] for _ in range(n+1)]

        adj_rev = [[] for _ in range(n+1)]

        for __ in range(m):

            u = data[ptr]

            v = data[ptr+1]

            ptr +=2

            adj[u].append(v)

            adj_rev[v].append(u)

        # Step 1: Kosaraju's algorithm

        visited = [False]*(n+1)

        order = []

        for i in range(1, n+1):

            if not visited[i]:

                stack = [(i, False)]

                while stack:

                    node, processed = stack.pop()

                    if processed:

                        order.append(node)

                        continue

                    if visited[node]:

                        continue

                    visited[node] = True

                    stack.append( (node, True) )

                    for neighbor in adj[node]:

                        if not visited[neighbor]:

                            stack.append( (neighbor, False) )

        # Step 2: process in reverse order

        visited_rev = [False]*(n+1)

        scc = []

        component_id = [0]*(n+1)

        for node in reversed(order):

            if not visited_rev[node]:

                current_scc = []

                stack = [node]

                visited_rev[node] = True

                while stack:

                    u = stack.pop()

                    current_scc.append(u)

                    for v in adj_rev[u]:

                        if not visited_rev[v]:

                            visited_rev[v] = True

                            stack.append(v)

                scc.append(current_scc)

                # Assign component_id for current_scc

                for u in current_scc:

                    component_id[u] = len(scc) -1

        # Build condensation DAG

        adj_cond = defaultdict(set)

        for u in range(1, n+1):

            for v in adj[u]:

                cu = component_id[u]

                cv = component_id[v]

                if cu != cv:

                    adj_cond[cu].add(cv)

        # Build adj_in: for each component, list of predecessors in condensation DAG

        adj_in = defaultdict(list)

        for c in adj_cond:

            for d in adj_cond[c]:

                adj_in[d].append(c)

        # Compute topological order using Kahn's algorithm

        in_degree = defaultdict(int)

        for c in adj_cond:

            for d in adj_cond[c]:

                in_degree[d] +=1

        # Initialize in_degree for all components (some may have 0 in_degree and not in the in_degree dict)

        total_components = len(scc)

        # Build queue with all components with in_degree 0

        queue = deque()

        for component in range(total_components):

            if in_degree.get(component, 0) ==0:

                queue.append(component)

        top_order = []

        # Process the queue

        while queue:

            u = queue.popleft()

            top_order.append(u)

            for v in adj_cond.get(u, set()):

                in_degree[v] -=1

                if in_degree[v] ==0:

                    queue.append(v)

        # Compute size and sum_a for each component

        size = [len(component) for component in scc]

        sum_a = [ sum( a[u-1] for u in component ) for component in scc ]

        # Initialize DP arrays

        dp_size = [0] * total_components

        dp_sum = [0] * total_components

        for c in top_order:

            current_size = size[c]

            current_sum = sum_a[c]

            max_size = current_size

            min_sum = current_sum

            # Check all predecessors in adj_in[c]

            for p in adj_in.get(c, []):

                candidate_size = dp_size[p] + current_size

                candidate_sum = dp_sum[p] + current_sum

                if candidate_size > max_size:

                    max_size = candidate_size

                    min_sum = candidate_sum

                elif candidate_size == max_size:

                    if candidate_sum < min_sum:

                        min_sum = candidate_sum

            dp_size[c] = max_size

            dp_sum[c] = min_sum

        # Find the maximum size and minimal sum

        max_len = max(dp_size) if dp_size else 0

        min_total = float('inf')

        for i in range(total_components):

            if dp_size[i] == max_len:

                if dp_sum[i] < min_total:

                    min_total = dp_sum[i]

        print(max_len, min_total)