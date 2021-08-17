#inverse 0-1 knapsack: minimise sum of values of selected items
#while sum of their weights can't be less than given number

def knapsack(weights, values, limit, coeff=0):
    maxvalue = [float('-inf')] * (lim - coeff + 1)
    maxvalue[0] = 0
    for i in range(lim - coeff + 1):
        for weight, value in zip(weights, values):
            if weight <= i:
                maxvalue[i] = max(maxvalue[i], maxvalue[i - weight] + value)
    return max(maxvalue[lim:(lim - coeff + 1)])


n = int(input())
weights = []
values = []
for i in range(n):
    v, w = map(int, input().split())
    weights.append(w)
    values.append(-v)
lim = int(input())
print(-knapsack(weights, values, lim, 100 * min(values)))