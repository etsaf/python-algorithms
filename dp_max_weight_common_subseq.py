#each letter is assigned weight
#Find maximum weight of common subsequence of 2 sequences
a = input()
b = input()
m = len(a)
n = len(b)
weight = dict()
letter = list(map(int, input().split()))
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
abc += ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
abc += ['u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(letter)):
    weight[abc[i]] = letter[i]
dp = []
for i in range(m + 1):
    dp.append([0] * (n + 1))
for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + weight[a[i - 1]]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[m][n])