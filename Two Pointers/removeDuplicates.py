def removeDuplicates(arr):
    i,j=0,0
    while(i<len(arr) and j<len(arr)):
        if arr[i]==arr[j]:
            j+=1
        else:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return i+1



nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

# 0,0,1,1,1,2,2,3,3,4
# 0,1,0,1,1,2,2,3,3,4
