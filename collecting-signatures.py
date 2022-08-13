
def contain(a,b):
    if(b[0]<=a<=b[1]):
        return True
    else:
        return False
def index(l,a):
    i = 0
    j = 0
    for i in range(len(l)):
        if(contain(a,l[i])):
            j+=1
    return j

print("enter number of line segments")
nsegments = int(input())

l =[]
print("please enter the coordinates of the line segments you wish to enter")
for i in range(nsegments):
   
    l.append(list(map(int,input().split(' '))))
   
   

l.sort(key=lambda x:x[1])
print(l)
ans = []
i = 0
temp = 0
while(i<nsegments):
    ans.append(l[i][1])
    temp = l[i][1]
    i = index(l,temp)
print(ans)
print(len(ans))
   

    



