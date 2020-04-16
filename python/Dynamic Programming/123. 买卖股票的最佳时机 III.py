

class Solution:
    def maxProfit(self, prices):
        if prices==[]:
            return 0
        length=len(prices)
        #结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp=[ [[0,0,0],[0,0,0] ] for i in range(0,length) ]
        #第一天休息
        dp[0][0][0]=0
        #第一天买入
        dp[0][1][0]=-prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        #第一天不可能已经卖出
        dp[0][1][1]=float('-inf')
        dp[0][1][2]=float('-inf')
        for i in range(1,length):
            #未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0]=0
            #未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
            #未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
            #持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
            #持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
            #持股，卖出过2次，不可能
            dp[i][1][2]=float('-inf')
        return max(dp[length-1][0][1],dp[length-1][0][2],0)

prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))