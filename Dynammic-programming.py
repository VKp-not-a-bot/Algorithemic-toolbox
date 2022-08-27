ncoins = int(input())
change = list(map(int,input().split(' ')))
money = int(input())
ans = []
ans.append(0)
change.sort()
for i in range(1,money+1):
    if(i-change[0]>=0):
        ans.append(ans[i-change[0]]+1)
    else:
        ans.append(0)
    j = 1
    while(j<ncoins):
        if(i-change[j]>=0):
            l = ans[i-change[j]]+1
            if(l<ans[i]):
                ans[i] = l
        j+=1
    
print(ans[money])

    