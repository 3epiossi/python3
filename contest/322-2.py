class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        length = len(coins)
        _coins = [coins[i] for i in range(length) if coins[i] <= amount]
        coins = []
        coins.extend(_coins)
        del _coins
        cache = {0:0}
        for amou in range(1, amount+1):
            cache[amou] = amount+1
            for coin in coins:
                diff = amou-coin
                if diff >= 0:
                    cache[amou] = min(cache[diff]+1, cache[amou])
                pass
            pass
        return cache[amount] if cache[amount] <= amount else -1

        
        