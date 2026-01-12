# Subarray Sum Equals K
# Problem Statement
# Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.
# A subarray is a contiguous part of the array.
# Input

# nums = [1, 1, 1]
# k = 2
# Output

# 2
# Explanation
# 	• Subarray [1,1] (indices 0–1)
# 	• Subarray [1,1] (indices 1–2)
# Constraints
# 	• 1 ≤ len(nums) ≤ 2 × 10⁴
# 	• -1000 ≤ nums[i] ≤ 1000
# -10⁷ ≤ k ≤ 10⁷

def func(arr,k):
    hashmap = {0:1}   #understand it like prefix sum as 0 and occurence of 0 is 1
    count = 0
    prefix_sum = 0

    for i in range(0,len(arr)):
        prefix_sum +=arr[i]

        if prefix_sum-k in hashmap:
            count+=hashmap[prefix_sum-k]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1
    # print(hashmap)
    return count
        
    

# {0:4}
# 6 
    

# arr=[1,2,3,3,4,2,3,1]
# k=3
arr= [0,0,0,0]
k=0
print(func(arr,k))
# {
# 0:0,
# 1:0,
# 2,0
# }