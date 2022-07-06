# Python Version
# head[u] 和 cnt 的初始值都为 -1
def add(u, v):
    cnt = cnt + 1
    nex[cnt] = head[u] # 当前边的后继
    head[u] = cnt # 起点 u 的第一条边
    to[cnt] = v # 当前边的终点

# 遍历 u 的出边
i = head[u]
while ~i: # ~i 表示 i != -1
    v = to[i]
    i = nxt[i]