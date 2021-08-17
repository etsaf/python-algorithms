#how fast can you print n letters using two printers
#if first one takes x seconds to print one, ans the second takes y

def f(t, x, y):
    return t // x + t // y


n, x, y = list(map(int, input().split()))
x, y = min(x, y), max(x, y)
if n == 1:
    print(x)
else:
    l = 0
    r = (n - 1) * y
    while r - l > 1:
        m = (l + r) // 2
        if f(m, x, y) >= n:
            r = m
        else:
            l = m
    print(r)


#find rightmost occurence of the element
from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
s = set(a)
ans = 0
for i in b:
    if i not in s:
        ans -= 1
    else:
        ans += (bisect_right(a, i) - 1)
print(ans)