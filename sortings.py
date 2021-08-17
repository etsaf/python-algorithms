#Selection sort
def selectsort(a):
    for i in range(len(a)):
        min_ind = i
        for j in range(i + 1, len(a)):
            if a[min_ind] > a[j]:
                min_ind = j
        a[i], a[min_ind] = a[min_ind], a[i]
    return a


#Insertion sort
def insertsort(a):
    for i in range(len(a) - 1):
        j = i + 1
        while a[j] < a[j - 1] and j > 0:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


#Bubble sort
def bubblesort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


#Bucket sort (sort of)
def bucketsort(a):
    for i in range(len(a)):
        a[i] = list(map(int, list(a[i])))
    #print(a)
    n = len(a[0])
    buckets = []
    for i in range(10):
        buckets.append([])
    for i in range(len(a)):
        end = a[i][n - 1]
        buckets[end].append(a[i])
    #print(buckets)
    for i in range(1, n):
        buckets1 = []
        for f in range(10):
            buckets1.append([])        
        for j in range(10):
            for k in buckets[j]:
                end = k[n - i - 1]
                buckets1[end].append(k)
        buckets = buckets1
        #print(buckets)
    a = []
    for bucket in buckets:
        for elem in bucket:
            a.append(''.join(map(str, elem)))
    return a


#Mergesort
def merge(right, left, res):
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    if len(left) > l:
        for i in range(l, len(left)):
            res.append(left[i])
    elif len(right) > r:
        for j in range(r, len(right)):
            res.append(right[j]) 
    return res

def mergesort(arr):
    b = len(arr)
    if b > 1:
        mid = b // 2
        return merge(mergesort(arr[:mid]), mergesort(arr[mid:]), [])
    else:
        return arr


#Quick Sort ????
def partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if arr[i] <= arr[begin]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[begin] = arr[begin], arr[pivot]
    return pivot
def quicksort(arr, begin, end):
    if begin < end:
        pivot = partition(arr, begin, end)
        quicksort(arr, begin, pivot - 1)
        quicksort(arr, pivot + 1, end)
        return arr

a = list(map(int, input().split()))
print(quicksort(a, 0, len(a) - 1))