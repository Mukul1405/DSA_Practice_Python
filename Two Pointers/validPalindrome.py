# Problem Statement

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# A palindrome reads the same forward and backward after cleaning.

# Input
# s = "A man, a plan, a canal: Panama"

# Output
# true

# Input
# s = "race a car"

# Output
# false

def validPalindrome(s):
    # s = s.lower()
    # newString = ""
    # for i in s:
    #     if i.isalnum():
    #         newString+=i
    i=0
    j=len(s)-1
    while(i<j):
        if not s[i].isalnum():
            i+=1
            continue
        if not s[j].isalnum():
            j-=1
            continue
        if s[i].isalnum() and s[j].isalnum():
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
                continue
            else:
                return False

    return True

# s = "A man, a plan, a canal: Panama"
s = ".,a"

print(validPalindrome(s))