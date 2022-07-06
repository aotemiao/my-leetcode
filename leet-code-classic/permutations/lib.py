import itertools
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutationspermutations(nums))

if __name__ == '__main__':
    print(permute(nums=[1, 2, 3]))