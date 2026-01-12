# Problem: Container With Most Water
# Problem Statement

# You are given an integer array height where height[i] represents the height of a vertical line drawn at position i.

# Choose two different indices i and j such that together with the x-axis they form a container that can hold water.

# Return the maximum amount of water the container can store.

# Input
# height = [1,8,6,2,5,4,8,3,7]

# Output
# 49

def maxWaterStored(arr):
    l,r=0,len(arr)-1
    max_water= 0
    while(l<r):
        stored_water= min(arr[l],arr[r])*(r-l)
        if stored_water>max_water:
            max_water=stored_water
        if(arr[l]>arr[r]):
            r-=1
        else:
            l+=1
    print(max_water)

height = [1,8,6,2,5,4,8,3,7]
maxWaterStored(height)