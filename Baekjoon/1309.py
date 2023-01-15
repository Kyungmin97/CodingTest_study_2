MAX=10**5
n=int(input())
dp=[0]*(MAX+1)

dp[1]=1+2
dp[2]=1+4+2

for i in range(3,n+1):
    dp[i]=2*dp[i-1]+dp[i-2]
    dp[i]%=9901

print(dp[n])
print(dp[:100])