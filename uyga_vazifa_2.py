class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()

        coins_added, obtained, i = 0, 0, 0
        while obtained < target:
            if i < len(coins) and coins[i] <= obtained + 1:
                obtained += coins[i]
                i += 1
            else:
                obtained += obtained + 1
                coins_added += 1
        return coins_added
