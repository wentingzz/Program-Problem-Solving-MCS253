class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ret = 1
        for x in range(m + n - 2, m - 1, -1):
            ret *= x
        for x in range(n - 1, 1, -1):
            ret //= x
        return ret

# 20 = 44
# 35 45
# 56 46
# 84 47
# 120 48