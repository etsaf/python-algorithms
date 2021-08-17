from collections import deque
inq = deque() #(elem, min)
outq = deque()
#n = length of sequence, m = width of window
n, m = map(int, input().split())
#ith element a_i = (a_{i - 1} * x + y) % (10 ^ 9 + 7)
a0, x, y = map(int, input().split())
a = a0
inq.append((a, a))
#res = sum of all minimums
res = 0
num = 10 ** 9 + 7
currMin = a
for i in range(m - 1):
    a = (a * x + y) % num
    minn = inq[-1][1]
    if a < minn:
        inq.append((a, a))
    else:
        inq.append((a, minn))
    currMin = min(currMin, a)
res += currMin
for i in range(n - m):
    if not outq:
        while inq:
            el, mx = inq.pop()
            if not outq:
                outq.append((el, el))
            else:
                minn = outq[-1][1]
                if el < minn:
                    outq.append((el, el))
                else:
                    outq.append((el, minn))
    outq.pop()
    a = (a * x + y) % num
    if not inq:
        inq.append((a, a))
    else:
        minn = inq[-1][1]
        if a < minn:
            inq.append((a, a))
        else:
            inq.append((a, minn))
    if not outq:
        res += inq[-1][1]
    else:
        res += min(inq[-1][1], outq[-1][1])
print(res)