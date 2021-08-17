#longest non-decreasing subsequence

def binsearch(a, end, l, r, find):
    while r - l > 1:
        m = (r + l) // 2
        if a[end[m]] >= find:
            r = m
        else:
            l = m
    return r


n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = (a[i], i)
end = [0] * (n + 1)
prev = [-1] * (n + 1)
ll = 1
for i in range(1, n):
    if a[i] < a[end[0]]:
        end[0] = i
    elif a[i] > a[end[ll - 1]]:
        prev[i] = end[ll - 1]
        end[ll] = i
        ll += 1
    else:
        new = binsearch(a, end, -1, ll - 1, a[i])
        prev[i] = end[new - 1]
        end[new] = i
ind = end[ll - 1]
ans = []
while ind >= 0:
    ans.append(a[ind][0])
    ind = prev[ind]
ans.reverse()
print(ll)
print(*ans)
