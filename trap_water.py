#height = [4,2,0,3,2,5]
#height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [5,4,1,2]
#height = [2,0,2]
def trap(height):
    dp = [0]*(len(height))
    for i in range(0,len(height)-1):
        if height[i]+dp[i]>height[i+1]+dp[i+1]:
            dp[i+1] = height[i]+dp[i]- height[i+1]
    dp[-1] = 0
    for i in range(len(dp)-2,0,-1):
        if(height[i]>height[i+1]+dp[i+1]):
            dp[i] = 0
        else:
            if(height[i]+dp[i]>height[i+1]+dp[i+1]):
                if(height[i]>height[i+1]):
                    dp[i] = 0
                else:
                    dp[i] = height[i]+dp[i]-(height[i+1]+dp[i+1])
    print(dp)
    print(sum(dp))
#trap(height)

print("hello",1)