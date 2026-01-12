# i=0
# j=1

# 1,0,0,3,12

# i+=1
# i=1
# j+=1 until number

# i=1
# j=3
# swap
# 1,3,0,0,12

def moveZeroesToEnd(arr):
    i,j=0,0
    while(i<len(arr)):
        if arr[i]==0:
            break
        i+=1
    j=i
    while(j<len(arr)):
        if arr[j]!=0:
            break
        j+=1
    
    while(i<=j and j<len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1

    print(arr)


arr = [1,0,1]

moveZeroesToEnd(arr)