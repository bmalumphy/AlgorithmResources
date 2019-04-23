
def Count(array, n):
    if(n == 1):
        return 0
    else:
        a = array[0:(n/2)]
        b = array[(n/2):n]
        # print(array)
        # print(a)
        # print(b)
        x = Count(a, len(a))
        y = Count(b, len(b))
        z = CountSplitInversions(array, n)
        #print(x+y+z)
        return x+y+z
    
    # if(length == 1):
    #     return array
    # else:
    #     newArray1 = array[0:(length/2)]
    #     newArray2 = array[(length/2):length]
    #     # print(len(newArray1))
    #     # print(len(newArray2))
        
def CountSplitInversions(array, n):
    d = [None]*n
    b = sorted(array[0:(n/2)])
    c = sorted(array[(n/2):n])
    i = 0
    j = 0
    # print(array)
    # print(b)
    # print(c)
    length1 = len(b)
    length2 = len(c)
    count = 0
    for k in range(0, n-1):
        # print(n)
        # print(i)
        #print(j)
        length1 = len(b)
        length2 = len(c)
        # print(i)
        # print(j)
        if(b[i] < c[j]):
            d[k]=b[i]
            if((i+1) == length1):
                # print("returned in i " + str(count))
                return count

            else:
                i+=1
            
        elif(c[j] < b[i]):
            d[k]=c[j]
            count += (length1-i)
            # print(count)
            if((j+1) == length2):
                # print("returned in j " + str(count))

                return count
            j+=1
    return count
    

