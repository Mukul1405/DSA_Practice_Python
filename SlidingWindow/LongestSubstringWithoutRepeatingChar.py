s = "abcabcbb"
s="bbbb"
def longestSubstringWithoutRepeat(s):
    i,j=0,0
    max_length=0
    dummy_set = set()
    while(j<len(s)):
        if(s[j] in dummy_set):
            while s[j] in dummy_set:
                dummy_set.remove(s[i])
                i+=1
            
        else:
            dummy_set.add(s[j])
            j+=1
            
        max_length = max(max_length,j-i)
    return max_length
        
print(longestSubstringWithoutRepeat(s))