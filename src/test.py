import time
def coinChange(coins,amount):
    coins.sort(reverse=True)
    coin_dp=[0 for _ in range(len(coins)+1)]
    coin_dp[-1]=amount
    starttime= time.time()
    coinChangeHelper(coins,coin_dp)
    print(coin_dp)
    print( time.time()-starttime)
def coinChangeHelper(coins,coin_dp):
    ind=0
    if coin_dp[-1]==0:
            return 0
    for coin in coins:
        if coin_dp[-1]-coin>=0:
            coin_dp[ind]+=1
            coin_dp[-1]-=coin
            
            if coin_dp[-1] >0 :
                coinChangeHelper(coins,coin_dp)
            else:
                completed=True
                return 0
        ind+=1

coinChange([2,5,10,25],9)
