class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(59)]
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9
        dp[7] = 12
        dp[8] = 18
        dp[9] = 27
        dp[10] = 36
        for num in range(11,n+1):
            dp[num] = dp[num//2]*dp[num-num//2]
            dp[num] = max(dp[num], dp[num//2-1]*dp[num-num//2+1])
        return dp[n]