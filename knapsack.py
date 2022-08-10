print("enter the number of items and total capacity divided by a space")
def ratio(e):
    return e[1]/e[0]
data = list(map(int,input().split(' ')))
i = 0
print("enter weight value pair divided by a space")
wndval = [] #the variable stores weight value pair
while(i<data[0]):
    wndval.append(list(map(int,input().split(' '))))
    i+=1
wndval.sort(reverse = True ,key=ratio)
i = 0
val = 0
wt = data[1] # assign the capacity of the bag to variable wt
while(wt>0):
    if(wndval[i][0]==0):
        i+=1
    elif(wt>=wndval[i][0]):
        wt = wt - wndval[i][0]
        val = val+ wndval[i][1]
        wndval[i][0] = 0
    elif(wt<=wndval[i][0]):
        
        val = val + wndval[i][1]*(wt/wndval[i][0])
        wt = 0
print(val)

    



    



