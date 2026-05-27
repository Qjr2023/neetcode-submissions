class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxDiff = 0

        for i in range(1, len(prices)):
            if prices[i] >= minPrice:
                diff = prices[i] - minPrice
                maxDiff = max(maxDiff, diff)
            
            else:
                minPrice = prices[i]
        
        return maxDiff
                

            

        