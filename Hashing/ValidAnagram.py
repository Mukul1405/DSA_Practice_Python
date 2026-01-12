# Problem Statement
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram means:
# 	• Same characters
# 	• Same frequency
# 	• Order does NOT matter
# Input

# s = "anagram"
# t = "nagaram"
# Output

# true
# Input

# s = "rat"
# t = "car"
# Output

# false

def validAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        freqMap1 = {}
        freqMap2 = {}
        for i in s1:
            if i in freqMap1:
                freqMap1[i] = freqMap1[i]+1
            else:
                freqMap1[i]=1
        
        for i in s2:
            if i in freqMap2:
                freqMap2[i] = freqMap2[i]+1
            else:
                freqMap2[i]=1
        if freqMap1 != freqMap2:
            return False
    return True

s = "anagram"
t = "magaram"
print(validAnagram(s,t))


# More Optimized
# 
# def validAnagram(s1, s2):
#     if len(s1) != len(s2):
#         return False

#     freq = {}

#     for ch in s1:
#         freq[ch] = freq.get(ch, 0) + 1

#     for ch in s2:
#         if ch not in freq:
#             return False
#         freq[ch] -= 1
#         if freq[ch] < 0:
#             return False

#     return True

# 