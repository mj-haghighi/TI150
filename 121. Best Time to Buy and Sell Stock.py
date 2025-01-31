class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        buy = prices[0]
        profit = 0

        for p in prices:
            if p < buy:
                buy = p
            elif p - buy > profit:
                profit = p - buy

        return profit
