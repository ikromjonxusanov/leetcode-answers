from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        data = dict()
        arr = []
        for num in nums:
            if data.get(num) is None:
                data[num] = 1
                continue
            arr.append(num)
        return arr
