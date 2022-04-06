arr = [0] * 103  # arr 用于记录方案


def dfs(n, i, a):
    if n == 0 and i == m:
        print(arr[0:i])
    if i <= m:
        for j in range(a + 1, n + 1):
            arr[i] = j
            dfs(n - j, i + 1, j)  # 请仔细思考该行含义。


# 主函数
n, m = map(int, input().split())
dfs(n, 0, 0)
