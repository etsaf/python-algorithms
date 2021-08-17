#split array into two subsets with minimum difference between subset sums
n = int(input())
a = list(map(int, input().split()))
summ = sum(a)
dp = []
for i in range(n + 1):
    dp.append([0] * (summ // 2 + 1))
for row in range(n + 1):
    dp[row][0] = 1
for col in range(1, summ // 2 + 1):
    dp[0][col] = 0
for i in range(1, n + 1):
    for j in range(1, summ // 2 + 1):
        dp[i][j] = dp[i - 1][j]
        if a[i - 1] <= j:
            if dp[i][j] or dp[i - 1][j - a[i - 1]]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
for j in range(summ // 2, -1, -1):
    if dp[n][j]:
        ans = summ - (2 * j)
        break
#minimum difference
print(ans)

