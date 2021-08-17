def findmax(d, length, out):
    currMax = d[-1]
    index = length - 1
    for i in range(length - 1, -1, -1):
        if d[i] == out:
            return i
        if d[i] > currMax:
            index = i
            currMax = d[i]
    return index


from collections import deque
d = deque() #can find sum, max, index of max
length = 0
summ = 0
index = 0
n = int(input())
for i in range(n):
    a = input().split()
    k = a[0]
    if k == 'push':
        x = int(a[1])
        d.append(x)
        length += 1
        summ += x
        if x >= d[index]:
            index = length - 1
    elif k == 'pop':
        out = d[-1]
        summ -= out
        d.pop()
        length -= 1
        if length and index == length:
            index = findmax(d, length, out)
    elif k == 'sum':
        print(summ)
    elif k == 'max':
        if not length:
            print(0)
        else:
            print(d[index])
    elif k == 'index of max':
        if not length:
            print(0)
        else:
            print(length - index)