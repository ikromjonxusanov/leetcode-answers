class Solution:
    def isUgly(self, n: int) -> bool:
        return False if n <= 0 else (2 * 3 * 5) ** 32 % n == 0
