# First Unique Character in a String
# Problem Statement
# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
# Input

# s = "leetcode"
# Output

# 0
# Input

# s = "loveleetcode"
# Output

# 2
# Input

# s = "aabb"
# Output

# -1
def indexOf(i,s):
    for j in range(0,len(s)):
        if s[j] == i:
            return j
        
def firstUnique(s):
    hashmap={}
    for i in s:
        hashmap[i] = hashmap.get(i,0)+1
    for i in hashmap:
        if hashmap[i]==1:
            return indexOf(i,s)
    return -1

s= "leetcode"
print(firstUnique(s))