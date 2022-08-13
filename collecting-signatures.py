
def contain(a,b):
    if(b[0]<=a<=b[1]):
        return True
    else:
        return False
def index(l,a,k,n):
    i = k-1

    j = k
    while(i<n):
        if(contain(a,l[i])):
            j+=1
            
            
        i+=1
    return j

#print("enter number of line segments")
nsegments = int(input())

l =[]
#print("please enter the coordinates of the line segments you wish to enter")
for i in range(nsegments):
   
    l.append(list(map(int,input().split(' '))))
   
   

l.sort(key=lambda x:x[1])
#print(l)
ans = []
i = 1
temp = 0


while(i<nsegments):
    ans.append(l[i-1][1])
   
    temp = l[i-1][1]
    i = index(l,temp,i-1,nsegments)
    i+=1
    
    
print(len(ans))
print(*ans,sep = ' ')

   

    



