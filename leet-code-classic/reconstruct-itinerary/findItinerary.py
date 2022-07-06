from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routers = defaultdict(list)
        path = ["JFK"]
        for a, b in tickets:
            routers[a].append(b)

        def backtrack(start) -> bool:
            if len(path) == len(tickets) + 1:
                return True
            routers[start].sort()
            for _ in routers[start]:
                arrival = routers[start].pop(0)
                path.append(arrival)
                if backtrack(arrival):
                    return True
                routers[start].append(arrival)
                path.pop()

        backtrack("JFK")
        return path


if __name__ == '__main__':
    print(Solution().findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
