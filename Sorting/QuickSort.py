m = 0

def findMedian(a, b ,c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c  

def partition(A, l, r):
    p = A[l]
    i = l + 1
    #print(A[l])
    #print(l)
    #print(r)
    for j in range(i, r+1):
        if(A[j] < p):
            #print(i)
            #print(A[j] < p)
            A[i], A[j] = A[j], A[i]
            i+=1
            #print(A)
        # else:
        #     print(A[j] < p)
        
    A[l], A[i-1] = A[i-1], A[l]
    #print(A)
    
    return A 
            

def QuickSort(A, l, r):
    global m
    if(l < r):
        #Choose pivot here
        a = A[l]
        b = A[r]
        middle = (r+l)//2
        c = A[middle]
        median = findMedian(a, b, c)
        indexOf = A.index(median)
        p = A[indexOf]
        m += r-l
        A[indexOf], A[l] = A[l], A[indexOf]
        A = partition(A, l, r)
        index = A.index(p)
        #print("index")
        #print(index)
        A = QuickSort(A, l, index - 1)
        A = QuickSort(A, index + 1, r)
        return A
    else:
        #print("Array was of length 1")
        return A

