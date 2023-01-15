
t=int(input())
dp = [0] * (11)
dp[1] = 1
dp[2] = 1 + 1
dp[3] = 1 + 2 + 1
for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(t):
    print(dp[int(input())])


