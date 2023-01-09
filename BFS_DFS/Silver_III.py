"""
n=int(input())

dp=[0]*(n+1)

for i in range(2,n+1):
    dp[i]=dp[i-1]+1

    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[n])
print(dp)
"""
"""
t=int(input())

zero=[1,0,1]
one=[0,1,1]

def fibo(num):
    length=len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num], one[num])

for _ in range(t):
    k=int(input())
    fibo(k)

"""

m=int(input())

def dp(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return dp(n-1)+dp(n-2)+dp(n-3)

for _ in range(m):
    n=int(input())
    print(dp(n))







































