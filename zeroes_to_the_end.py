#move all zeroes to the end of array
a = list(map(int, input().split()))
l = len(a)
counter = 0
for i in a:
    if i:
        a[counter] = i
        counter += 1
while counter < l:
    a[counter] = 0
    counter += 1
print(' '.join(map(str, a)))