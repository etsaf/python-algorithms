#number of non-increasing sequences that sum up to a given number
n = int(input())
dp = []
#return answer mod m
m = 1000000007
for i in range(n + 1):
    dp.append([0] * (n + 1))
dp[0][0] = 1
for i in range(n + 1):
    for j in range(n + 1):
        if i == j == 0:
            dp[i][j] = 1
            continue
        if j == 0:
            dp[i][j] = 0
            continue
        if j > i:
            dp[i][j] = dp[i][i]
            continue
        dp[i][j] = (dp[i][j - 1] + dp[i - j][j]) % m
print(dp[n][n] % m)