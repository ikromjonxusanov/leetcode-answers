from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = dict()

        for n in nums:
            if data.get(n) is None:
                data[n] = 1
                continue
            return True
        return False
