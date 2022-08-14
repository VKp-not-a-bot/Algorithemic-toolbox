#this program helps you distribute candies among babies



#print("enter the total no of  candies you want to distribute")
s =int(input())
def greed(n):
    i =1
    s=0
    while(s<=n):
        s = i*(i+1)/2
        i+=1
    return [i-2,n-(i-2)*(i-1)//2]
def arrange(l,num):
    for i in range(num):
        l.append(num-i) 
    

ans = []
temp =s 
j =greed(temp)

arrange(ans,j[0])
for m in range(j[1]):
    ans[m] = ans[m]+1
print(len(ans))
print(*ans , sep= ' ')




    