s = "aaabc"
k = 1



def func(s,k):
    i,j=0,0
    freq_map= {}
    max_len=0
    while(j<len(s)):
        if len(freq_map)<k:
            freq_map[s[j]] = freq_map.get(s[j],0)+1
            j+=1
        else:
            if s[j] in freq_map:
                freq_map[s[j]] = freq_map.get(s[j],0)+1
                j+=1
            else:
                freq_map[s[i]] = freq_map.get(s[i],0)-1
                if freq_map[s[i]]==0:
                    del freq_map[s[i]]
                i+=1
        max_len = max(max_len,sum(freq_map.values()))
    return max_len



   

print(func(s,k))