# Gráfos - Course Schedule (Kahn-algoritmus)
# https://cses.fi/problemset/task/1679/

import sys
from collections import deque

data = sys.stdin.readline().split()

n = int(data[0])
m = int(data[1])

adj = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    u = queue.popleft()
    result.append(u)

    for v in adj[u]:
        indegree[v] -= 1

        if indegree[v] == 0:
            queue.append(v)

if len(result) == n:
    print(*result)
else:
    print("IMPOSSIBLE")