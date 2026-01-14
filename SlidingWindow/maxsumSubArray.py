nums = [2, 1, 5, 1, 3, 2]
k = 3

def maxSumSubArray(arr,k):
    count,cur_sum,max_sum=0,0,0
    for i in range(len(arr)-k+1):
        if count<=k:
            count+=1
            cur_sum+=arr[i]
        else:
            cur_sum-=arr[i-k]
            cur_sum+=arr[i]
        if cur_sum>max_sum:
            max_sum=cur_sum
    return max_sum
print(maxSumSubArray(nums,k))