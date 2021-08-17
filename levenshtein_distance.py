#levenshtein distance
a, b = input().split()
A = len(a)
B = len(b)
dp = []
for i in range(A + 1):
    dp.append([0] * (B + 1))
for i in range(1, A + 1):
    dp[i][0] = i
for i in range(1, B + 1):
    dp[0][i] = i
for i in range(1, A + 1):
    for j in range(1, B + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
print(dp[A][B])