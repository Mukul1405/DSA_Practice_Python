prices = [7,1,5,3,6,4]
i=0
j=1
max_profit = 0
while(i<j and j<len(prices)):
    if prices[i]<prices[j]:
        profit= prices[j]-prices[i]
        if profit>max_profit:
            max_profit=profit
        j+=1
    else:
        i=j
        j+=1

print(max_profit)