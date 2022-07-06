
# Python Version
class Edge:
    u = 0
    v = 0

n, m = map(lambda x:int(x), input().split())

e = [Edge()] * m; vis = [False] * n

for i in range(0, m):
    e[i].u, e[i].v = map(lambda x:int(x), input().split())

def find_edge(u, v):
    for i in range(1, m + 1):
        if e[i].u == u and e[i].v == v:
            return True
    return False

def dfs(u):
    if vis[u]:
        return
    vis[u] = True
    for i in range(1, m + 1):
        if e[i].u == u:
            dfs(e[i].v)