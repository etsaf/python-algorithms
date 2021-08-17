#supermarket problem - matching each arriving customer to a first free counter

from heapq import heappop, heappush, heapify
#number of counters
n = int(input())
#how fast each cashier handles one item
speed = list(map(int, input().split()))
#number of customers
m = int(input())
#items per each customer
client = list(map(int, input().split()))
#number of a first free counter for each customer
ans = []
h = [] #[time, ind]
for i in range(min(m, n)):
    ans.append(i + 1)
    heappush(h, [client[i] * speed[i], i])
if m > n:
    for i in range(n, m):
        a = heappop(h)
        ind = a[1]
        ans.append(ind + 1)
        heappush(h, [a[0] + client[i] * speed[ind], ind])
print(*ans)