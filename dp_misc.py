#minimum number of steps needed to get n out of 1
#by either adding 1, multiplying by 2 or multiplying by 3
n = int(input())
dp = [0] * (n + 1)
for x in range(2, n + 1):
    if x % 3 == 0 and x % 2 == 0:
        dp[x] = min(dp[x - 1], dp[x // 2], dp[x // 3])
    elif x % 3 == 0:
        dp[x] = min(dp[x - 1], dp[x // 3])
    elif x % 2 == 0:
        dp[x] = min(dp[x - 1], dp[x // 2])
    else:
        dp[x] = dp[x - 1]
    dp[x] += 1
print(dp[n])

#there are n rocks, 2 players, each player takes 1, a or b in his turn.
#the one, who takes the last one, wins. Who has a winning strategy?
n, a, b = map(int, input().split())
win = [0] * (n + 1)
win[0] = 2
for i in range(n + 1):
    if win[i - a] == 2 or win[i - b] == 2 or win[i - 1] == 2:
        win[i] = 1
    else:
        win[i] = 2
print(win[n])