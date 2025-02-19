class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if(len(coins)==0):
            return 0
        
        m = len(coins)
        n = amount
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        dp[0][0] = 0
        
        for i in range(1,n+1):
            dp[0][i]=amount+1
        
        for i in range(1,m+1):
            for j in range(n+1):
                if(j<coins[i-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j],1+dp[i][j-coins[i-1]])
        
        #print(dp)            
        if(dp[m][n]>amount):
            return -1
                    
        return dp[m][n]