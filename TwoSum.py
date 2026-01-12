# Problem Statement
# You are given an array of integers nums and an integer target.
# Return indices of the two numbers such that they add up to target.
# 	• You may assume exactly one solution exists
# 	• You may not use the same element twice
# 	• You can return the answer in any order
# Input

# nums = [2, 7, 11, 15]
# target = 9
# Output

# [0, 1]


def twoSum(arr,k):
    seen = {}
    for i in range(0,len(arr)):
        if arr[i] in seen:
            return(seen[arr[i]],i)
        else:
            seen[k-arr[i]]=i
    return None
    




arr=[2, 7, 11, 15,3,3]
target= 6
print(twoSum(arr,target))