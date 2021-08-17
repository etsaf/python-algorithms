#kth element in a growing sequence

from collections import deque
from heapq import heappop, heappush, heapify
n, k = map(int, input().split())
#ith element: a_i = (a_{i-1} * x + y) % (10 ^ 9 + 7)
a0, x, y = map(int, input().split())
#ans = sum of partial kth elements
ans = 0
a = deque()
h_max = []
h_min = [] #len k
a.append(a0)
heappush(h_min, a0)
c = 1
f = a0
if k == 1:
    ans += a0
else:
    ans += -1
for i in range(n - 1):
    f = (f * x + y) % (10 ** 9 + 7)
    if len(h_min) < k:
        heappush(h_min, f)
    elif f >= h_min[0]:
        heappush(h_min, f)
        heappop(h_min)        
    if len(h_min) < k:
        ans += -1
    else: 
        ans += h_min[0]
    c += 1
print(ans)