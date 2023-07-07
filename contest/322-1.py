class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        cache = {0:{0}}
        length = len(coins)
        _coins = [coins[i] for i in range(length) if coins[i] <= amount]
        coins = []
        coins.extend(_coins)
        del _coins
        
        step = 1
        while True:
            if len(cache[step-1]) == 0:
                return -1
            cache[step] = set()
            for coin in coins:
                for sub in cache[step-1]:
                    new = coin+sub
                    if new > amount:
                        continue
                    if new == amount:
                        return step
                    cache[step].add(new)
            step += 1
