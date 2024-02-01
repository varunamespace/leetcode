import math

n = 1
perfect = []
for i in range(1,n+1):
    if(math.sqrt(i).is_integer()):
        perfect.append(i)
print(perfect)

def coinChange(perfect,n):
    dp = ([n+1]*(n+1))
    dp[0] = 0
    for i in range(1,n+1):
        for c in perfect:
            if(i-c>=0):
                dp[i] = min(dp[i],1+dp[i-c])
    return dp[n] if dp[n]!=n+1 else -1
print(coinChange(perfect,n))




