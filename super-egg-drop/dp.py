class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()

        def dp(k: int, n: int) -> int:
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = 2 ** 40
            # for i in range(1, n + 1):
            #     res = min(
            #         res,
            #         max(
            #             dp(k - 1, i - 1),  # 鸡蛋碎了
            #             dp(k, n - i)  # 鸡蛋没碎
            #         ) + 1
            #     )
            # memo[(k, n)] = res
            # return res
            lo, hi = 1, n
            while lo <= hi:
                x = (lo + hi) // 2
                broken = dp(k - 1, x - 1)
                not_broken = dp(k, n - x)

                if broken < not_broken:
                    lo = x + 1
                    res = min(res, not_broken + 1)
                else:
                    hi = x - 1
                    res = min(res, broken + 1)

            memo[(k, n)] = res
            return res

        return dp(k, n)


if __name__ == '__main__':
    print(Solution().superEggDrop(4, 100))
