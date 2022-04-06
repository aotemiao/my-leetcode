graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def DFS(graph, s):
    stack = []
    stack.append(s)  # 向list添加元素，用append()
    seen = set()  # 此处为set, python里set用的是hash table, 搜索时比数组要快。
    seen.add(s)  # 向set添加函数，用add()
    while (len(stack) > 0):
        vertex = stack.pop()  # 弹出最后一个元素
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print("当前出栈的是", vertex)


DFS(graph, 'A')
