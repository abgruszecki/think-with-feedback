import sys
from sys import stdin

class DSU:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)
        self.size = [1] * (size + 1)

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
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

def main():
    n = int(stdin.readline())
    k = int(stdin.readline())
    friends = []
    for _ in range(k):
        u, v = map(int, stdin.readline().split())
        friends.append((u, v))
    m = int(stdin.readline())
    dislikes = []
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        dislikes.append((u, v))

    dsu = DSU(n)
    for u, v in friends:
        dsu.union(u, v)

    roots = set()
    for i in range(1, n+1):
        roots.add(dsu.find(i))

    valid = {root: True for root in roots}

    for u, v in dislikes:
        root_u = dsu.find(u)
        root_v = dsu.find(v)
        if root_u == root_v:
            valid[root_u] = False

    max_size = 0
    for root in valid:
        if valid[root]:
            current_size = dsu.size[root]
            if current_size > max_size:
                max_size = current_size

    print(max_size if max_size > 0 else 0)

if __name__ == "__main__":
    main()