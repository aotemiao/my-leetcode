# Python Version

n = int(input("input node count:"))
m = int(input("edge count:"))

vis = [False] * (n + 1)
adj = [[False] * (n + 1) for _ in range(n+1)]

for i in range(1, m + 1):
    u, v = map(lambda x: int(x), input().split())
    adj[u][v] = True


def find_edge(u, v):
    return adj[u][v]


def dfs(u):
    if vis[u]:
        return
    vis[u] = True
    for v in range(1, n + 1):
        if adj[u][v]:
            dfs(v)
