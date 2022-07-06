graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    queue = []
    queue.append(s)  # 向list添加元素，用append()
    seen = set()  # 此处为set, python里set用的是hash table, 搜索时比数组要快。
    seen.add(s)  # 向set添加函数，用add()
    while (len(queue) > 0):
        vertex = queue.pop(0)  # 提取队头
        nodes = graph[vertex]  # 获得队头元素的邻接元素
        for w in nodes:
            if w not in seen:
                queue.append(w)  # 将没有遍历过的子节点入队
                seen.add(w)  # 标记好已遍历
        print("当前出队的是：", vertex)


BFS(graph, 'A')