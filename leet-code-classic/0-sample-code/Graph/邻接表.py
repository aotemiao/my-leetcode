n = int(input("input node count:"))
m = int(input("edge count:"))

vis = [False] * (n + 1)
adj = [[]] * (n + 1)

for i in range(1, m + 1):
    u, v = map(lambda x:int(x), input().split())
    adj[u].append(v)

def find_edge(u, v):
    for i in range(0, len(adj[u])):
        if adj[u][i] == v:
            return True
    return False

def dfs(u):
    if vis[u]:
        return
    vis[u] = True
    for i in range(0, len(adj[u])):
        dfs(adj[u][i])