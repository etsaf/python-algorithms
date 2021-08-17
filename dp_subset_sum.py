#find subset of array with sum equal to given
w, n = map(int, input().split())
a = list(map(int, input().split()))
dp = []
for i in range(n + 1):
    dp.append([0] * (w + 1))
for i in range(n + 1):
    dp[i][0] = [-1]
for i in range(1, w + 1):
    dp[0][i] = False
for i in range(1, n + 1):
    for j in range(1, w + 1):
        if j < a[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j - a[i - 1]]:
                dp[i][j] = dp[i - 1][j - a[i - 1]] + [i]
            else:
                dp[i][j] = False
if not dp[n][w]:
    print(-1)
else:
    print(len(dp[n][w]) - 1)
    print(*dp[n][w][1:])